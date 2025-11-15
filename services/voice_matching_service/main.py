from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from difflib import SequenceMatcher
from typing import Any, Dict, List, Optional, Tuple

import psycopg
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ConfigDict
from psycopg.rows import dict_row

try:  # Optional direct import when running inside the monorepo
    from NLU.app import parse_single_text as _local_parse_single_text  # type: ignore
except Exception:  # pragma: no cover - fallback to HTTP only
    _local_parse_single_text = None

try:
    from services.substitution_service.availability import (  # type: ignore
        get_line_ids_for_gtins,
        get_db_conninfo,
    )
except Exception:  # pragma: no cover - DB lookup is optional
    get_line_ids_for_gtins = None
    get_db_conninfo = None

logger = logging.getLogger("voice-matching-service")
logging.basicConfig(
    level=os.getenv("VOICE_MATCHING_LOG_LEVEL", "INFO").upper(),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

NAME_MATCH_THRESHOLD = float(os.getenv("VOICE_MATCHING_NAME_THRESHOLD", "0.55"))


def _normalize_code(raw: Optional[str]) -> Optional[str]:
    if raw is None:
        return None
    s = str(raw).strip()
    if not s:
        return None
    if s.endswith(".0"):
        s = s[:-2]
    return s


def _normalize_name(raw: Optional[str]) -> str:
    return " ".join(str(raw or "").lower().split())


def _name_similarity(a: str, b: str) -> float:
    na = _normalize_name(a)
    nb = _normalize_name(b)
    if not na or not nb:
        return 0.0
    return SequenceMatcher(None, na, nb).ratio()


class OrderItem(BaseModel):
    model_config = ConfigDict(extra="ignore")

    lineId: Optional[int] = Field(default=None, description="warehouse line id")
    productCode: Optional[str] = Field(
        default=None, description="GTIN / warehouse product code"
    )
    name: str = Field(..., min_length=1, description="Human readable product name")
    qty: Optional[float] = Field(
        default=None,
        ge=0,
        description="Quantity ordered (used for reference only)",
    )
    unit: Optional[str] = Field(default=None, description="Unit of measure")


class OrderPayload(BaseModel):
    model_config = ConfigDict(extra="ignore")

    orderId: Optional[str] = Field(default=None, description="Order identifier")
    customerId: Optional[str] = Field(default=None, description="Customer identifier")
    items: List[OrderItem] = Field(..., min_length=1)


class VoiceOrderMatchRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    text: str = Field(..., min_length=1, description="Voice-to-text transcript")
    order: OrderPayload
    context: Optional[Dict[str, Any]] = Field(
        default=None, description="Optional NLU context payload"
    )
    sessionId: Optional[str] = Field(
        default=None, description="Optional NLU session identifier"
    )


class MatchedItem(BaseModel):
    lineId: Optional[int]
    productCode: Optional[str]
    orderName: Optional[str]
    orderedQty: Optional[float]
    unit: Optional[str]
    detectedName: Optional[str]
    detectedGtin: Optional[str]
    detectedQuantity: Optional[float]
    detectedQuantityUnit: Optional[str]
    entityConfidence: Optional[float]
    matchScore: float
    matchSource: str
    overallConfidence: float


class VoiceOrderMatchResponse(BaseModel):
    orderId: Optional[str]
    intent: str
    intentConfidence: float
    matchedLineIds: List[int]
    matchedItems: List[MatchedItem]
    nluResponse: Dict[str, Any]


class LineIdLookupRequest(BaseModel):
    name: str = Field(..., min_length=1, description="Product name to look up")
    limit: int = Field(
        default=3, ge=1, le=20, description="Maximum number of candidate matches"
    )


class LookupResult(BaseModel):
    lineId: int
    productCode: Optional[str]
    name: str
    score: float


class LineIdLookupResponse(BaseModel):
    query: str
    count: int
    results: List[LookupResult]


@dataclass
class PreparedOrderItem:
    index: int
    line_id: Optional[int]
    product_code: Optional[str]
    original_product_code: Optional[str]
    name: str
    qty: Optional[float]
    unit: Optional[str]


class NLUClient:
    def __init__(self):
        self.base_url = os.getenv("NLU_BASE_URL")
        self.timeout = float(os.getenv("NLU_TIMEOUT_SECONDS", "10"))

    def parse(
        self, *, text: str, context: Optional[Dict[str, Any]], session_id: Optional[str]
    ) -> Dict[str, Any]:
        payload = {"text": text}
        if context:
            payload["context"] = context
        if session_id:
            payload["session_id"] = session_id

        if self.base_url:
            url = self.base_url.rstrip("/") + "/nlu/parse"
            try:
                response = requests.post(url, json=payload, timeout=self.timeout)
            except requests.RequestException as exc:  # pragma: no cover - network failure
                logger.error("Failed to call NLU API: %s", exc)
                raise HTTPException(
                    status_code=502, detail="Failed to reach NLU service"
                ) from exc

            if response.status_code >= 400:
                logger.error(
                    "NLU API returned %s: %s", response.status_code, response.text
                )
                raise HTTPException(
                    status_code=502,
                    detail=f"NLU service error: {response.status_code}",
                )
            return response.json()

        if _local_parse_single_text is not None:
            return _local_parse_single_text(text, context, session_id)

        raise HTTPException(
            status_code=500,
            detail="NLU backend is not configured. Set NLU_BASE_URL or install NLU module.",
        )


class OrderMatcher:
    def __init__(self, items: List[OrderItem]):
        self.items = items
        self.prepared = self._prepare_items()

    def _prepare_items(self) -> List[PreparedOrderItem]:
        resolved_by_code: Dict[str, int] = {}

        missing_codes = [
            _normalize_code(it.productCode)
            for it in self.items
            if it.lineId is None and it.productCode
        ]
        normalized_missing = [code for code in missing_codes if code]

        if normalized_missing and get_line_ids_for_gtins is not None:
            try:
                resolved = get_line_ids_for_gtins(normalized_missing)
                resolved_by_code = {
                    _normalize_code(code): line_id for code, line_id in resolved.items()
                }
            except Exception as exc:  # pragma: no cover - DB optional
                logger.warning("Failed to resolve line ids from DB: %s", exc)

        prepared: List[PreparedOrderItem] = []
        for idx, item in enumerate(self.items):
            normalized_code = _normalize_code(item.productCode)
            line_id = item.lineId
            if line_id is None and normalized_code:
                line_id = resolved_by_code.get(normalized_code)
            prepared.append(
                PreparedOrderItem(
                    index=idx,
                    line_id=line_id,
                    product_code=normalized_code,
                    original_product_code=item.productCode,
                    name=item.name,
                    qty=item.qty,
                    unit=item.unit,
                )
            )
        return prepared

    def match(
        self, products: List[Dict[str, Any]], quantities: List[Dict[str, Any]]
    ) -> Tuple[List[MatchedItem], List[int]]:
        matched_items: List[MatchedItem] = []
        matched_line_ids: List[int] = []
        used_indices: set[int] = set()

        for idx, product_entity in enumerate(products):
            match = self._match_single_entity(product_entity, used_indices)
            if not match:
                continue

            detected_quantity = self._select_quantity(idx, quantities)
            matched_items.append(
                self._build_matched_item(match, product_entity, detected_quantity)
            )

            if match.line_id is not None:
                matched_line_ids.append(match.line_id)
            used_indices.add(match.index)

        return matched_items, matched_line_ids

    def _match_single_entity(
        self, entity: Dict[str, Any], used_indices: set[int]
    ) -> Optional[PreparedOrderItem]:
        gtin = _normalize_code(entity.get("gtin"))
        entity_name = entity.get("name")

        if gtin:
            for item in self.prepared:
                if (
                    item.product_code
                    and item.product_code == gtin
                    and item.index not in used_indices
                ):
                    entity["_match_source"] = "gtin"
                    entity["_match_score"] = 1.0
                    return item

        if not entity_name:
            return None

        best_item: Optional[PreparedOrderItem] = None
        best_score = 0.0
        for item in self.prepared:
            if item.index in used_indices:
                continue
            score = _name_similarity(entity_name, item.name)
            if score > best_score:
                best_item = item
                best_score = score

        if best_item and best_score >= NAME_MATCH_THRESHOLD:
            entity["_match_source"] = "name"
            entity["_match_score"] = best_score
            return best_item

        return None

    @staticmethod
    def _select_quantity(
        idx: int, quantities: List[Dict[str, Any]]
    ) -> Optional[Dict[str, Any]]:
        if not quantities:
            return None
        if idx < len(quantities):
            return quantities[idx]
        return quantities[-1]

    @staticmethod
    def _combine_confidence(entity_conf: float, match_score: float) -> float:
        return min(1.0, 0.4 * entity_conf + 0.6 * match_score)

    def _build_matched_item(
        self,
        item: PreparedOrderItem,
        entity: Dict[str, Any],
        detected_quantity: Optional[Dict[str, Any]],
    ) -> MatchedItem:
        entity_confidence = float(entity.get("confidence", 0.0))
        match_score = float(entity.get("_match_score", 0.0))
        match_source = str(entity.get("_match_source", "name"))

        detected_qty_value = None
        detected_qty_unit = None
        if detected_quantity:
            detected_qty_value = detected_quantity.get("value")
            detected_qty_unit = detected_quantity.get("unit")

        return MatchedItem(
            lineId=item.line_id,
            productCode=item.product_code or item.original_product_code,
            orderName=item.name,
            orderedQty=item.qty,
            unit=item.unit,
            detectedName=entity.get("name"),
            detectedGtin=_normalize_code(entity.get("gtin")),
            detectedQuantity=detected_qty_value,
            detectedQuantityUnit=detected_qty_unit,
            entityConfidence=entity_confidence,
            matchScore=round(match_score, 4),
            matchSource=match_source,
            overallConfidence=round(
                self._combine_confidence(entity_confidence, match_score), 4
            ),
        )


def _fetch_warehouse_items_by_name(
    name: str, max_candidates: int = 100
) -> List[Dict[str, Any]]:
    if get_db_conninfo is None:
        raise HTTPException(
            status_code=503, detail="Warehouse DB connection is not configured"
        )
    tokens = [tok.strip().lower() for tok in name.split() if tok.strip()]
    if not tokens:
        return []

    clauses = []
    params: List[Any] = []
    for token in tokens:
        clauses.append("LOWER(name) LIKE %s")
        params.append(f"%{token}%")

    where_clause = " AND ".join(clauses) if clauses else "TRUE"
    query = f"""
        SELECT line_id, product_code, name
        FROM warehouse_items
        WHERE {where_clause}
        LIMIT %s
    """
    params.append(max_candidates)

    conninfo = get_db_conninfo()
    try:
        with psycopg.connect(conninfo, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                return cur.fetchall()
    except psycopg.Error as exc:
        logger.error("Warehouse DB lookup failed: %s", exc)
        raise HTTPException(status_code=502, detail="Warehouse DB lookup failed") from exc


def _lookup_line_id_by_name(name: str, limit: int = 3) -> List[Dict[str, Any]]:
    cleaned = name.strip()
    if not cleaned:
        return []
    candidates = _fetch_warehouse_items_by_name(cleaned)
    scored: List[Dict[str, Any]] = []
    for candidate in candidates:
        candidate_name = candidate.get("name", "")
        score = _name_similarity(cleaned, candidate_name)
        scored.append(
            {
                "line_id": int(candidate["line_id"]),
                "product_code": candidate.get("product_code"),
                "name": candidate_name,
                "score": score,
            }
        )
    scored.sort(key=lambda item: item["score"], reverse=True)
    return scored[:limit]


nlu_client = NLUClient()
app = FastAPI(
    title="Voice Order Matching Service",
    version="0.1.0",
    description="Matches NLU product mentions to order items and returns warehouse line ids.",
)


@app.get("/health")
def health() -> Dict[str, Any]:
    return {
        "status": "ok",
        "nlu_backend": "remote" if nlu_client.base_url else "in-process",
        "items_supported": True,
    }


@app.post("/warehouse/lookup", response_model=LineIdLookupResponse)
def warehouse_lookup(request: LineIdLookupRequest) -> LineIdLookupResponse:
    matches = _lookup_line_id_by_name(request.name, request.limit)
    results = [
        LookupResult(
            lineId=match["line_id"],
            productCode=match.get("product_code"),
            name=match.get("name", ""),
            score=round(float(match.get("score", 0.0)), 4),
        )
        for match in matches
    ]
    return LineIdLookupResponse(
        query=request.name,
        count=len(results),
        results=results,
    )


@app.post("/orders/match", response_model=VoiceOrderMatchResponse)
def match_voice_order(request: VoiceOrderMatchRequest) -> VoiceOrderMatchResponse:
    logger.info(
        "Matching voice input for order %s with %d items",
        request.order.orderId,
        len(request.order.items),
    )

    nlu_response = nlu_client.parse(
        text=request.text, context=request.context, session_id=request.sessionId
    )

    entities = nlu_response.get("parameters", {}).get("entities", {})
    products = entities.get("products", []) or []
    quantities = entities.get("quantities", []) or []

    matcher = OrderMatcher(request.order.items)
    matched_items, matched_line_ids = matcher.match(products, quantities)

    return VoiceOrderMatchResponse(
        orderId=request.order.orderId,
        intent=nlu_response.get("intent", "unknown"),
        intentConfidence=float(nlu_response.get("confidence", 0.0)),
        matchedLineIds=matched_line_ids,
        matchedItems=matched_items,
        nluResponse=nlu_response,
    )


if __name__ == "__main__":  # pragma: no cover
    import uvicorn

    uvicorn.run(
        "services.voice_matching_service.main:app",
        host=os.getenv("VOICE_MATCHING_HOST", "0.0.0.0"),
        port=int(os.getenv("VOICE_MATCHING_PORT", "8085")),
        reload=bool(int(os.getenv("VOICE_MATCHING_RELOAD", "0"))),
    )


