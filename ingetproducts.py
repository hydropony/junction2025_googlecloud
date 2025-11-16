#!/usr/bin/env python3
"""
Select two product categories from the @vaimo_products JSON dataset and output
12 products (6 per category) grouped into clusters of three mutually substitutable
items. Substitution compatibility is determined via the substitution_service
heuristics (suggest_candidates_by_gtin).
"""

from __future__ import annotations

import importlib
import itertools
import json
import math
import sys
from collections import defaultdict
from datetime import datetime
from types import SimpleNamespace
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Tuple

if sys.platform == "darwin":
    _ORIGINAL_PLATFORM = sys.platform
    sys.platform = "linux"
    import numpy as _np  # noqa: F401  # ensure numpy initializes without macOS check
    sys.platform = _ORIGINAL_PLATFORM
else:
    import numpy as _np  # noqa: F401

import pandas as pd

try:
    import dotenv  # noqa: F401
except ModuleNotFoundError:
    sys.modules["dotenv"] = SimpleNamespace(load_dotenv=lambda *args, **kwargs: False)

from services.substitution_service.candidates import (
    _normalize_id,
    suggest_candidates_by_gtin,
)
from services.substitution_service.data_loaders import product_data_df

MAX_PRODUCTS_PER_CATEGORY = 80
RECOMMENDATIONS_PER_PRODUCT = 15
REQUIRED_CATEGORIES = 2
TRIADS_PER_CATEGORY = 2
GROUP_SIZE = 3


ProductDict = Dict[str, Any]


def _patch_availability_module() -> None:
    """
    Ensure substitution_service availability lookups never hit the warehouse DB.
    We replace get_availability_for_gtins with a cheap stub that marks every
    candidate as available, keeping the heuristic scoring intact while avoiding
    external dependencies.
    """

    module_name = "services.substitution_service.availability"
    try:
        module = importlib.import_module(module_name)
    except Exception:
        module = SimpleNamespace()
        sys.modules[module_name] = module  # type: ignore[assignment]

    def _fake_availability(gtins: Iterable[str]) -> Dict[str, float]:
        return {str(g): float("inf") for g in gtins if g}

    setattr(module, "get_availability_for_gtins", _fake_availability)
    if not hasattr(module, "get_line_ids_for_gtins"):
        setattr(module, "get_line_ids_for_gtins", lambda gtins: {})


def _convert_value(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, dict):
        return {k: _convert_value(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_convert_value(v) for v in value]
    if isinstance(value, datetime):
        return value.isoformat()
    if hasattr(value, "isoformat") and not isinstance(value, (str, bytes)):
        try:
            return value.isoformat()
        except Exception:
            pass
    if hasattr(value, "item") and not isinstance(value, (str, bytes)):
        try:
            return _convert_value(value.item())
        except Exception:
            pass
    if isinstance(value, float):
        if math.isnan(value):
            return None
        return float(value)
    if isinstance(value, (int, str, bool)):
        return value
    if pd.isna(value):
        return None
    return value


def _extract_gtin(product: ProductDict) -> Optional[str]:
    gtin = _normalize_id(product.get("salesUnitGtin"))
    if gtin:
        return gtin
    synkka = product.get("synkkaData")
    if isinstance(synkka, dict):
        gtin = _normalize_id(synkka.get("gtin"))
        if gtin:
            return gtin
    return None


def _build_catalog() -> Tuple[Dict[str, ProductDict], Dict[str, List[str]]]:
    df = product_data_df()
    product_lookup: Dict[str, ProductDict] = {}
    category_to_gtins: Dict[str, List[str]] = defaultdict(list)

    for _, row in df.iterrows():
        product = {col: _convert_value(val) for col, val in row.items()}
        gtin = _extract_gtin(product)
        category = product.get("category")
        if not gtin or category is None:
            continue
        category_str = str(category)
        if gtin in product_lookup:
            continue
        product_lookup[gtin] = product
        category_to_gtins[category_str].append(gtin)

    for gtins in category_to_gtins.values():
        gtins.sort()

    return product_lookup, category_to_gtins


def _compute_recommendations(
    gtins: Sequence[str],
    allowed: Set[str],
    k: int,
) -> Tuple[Dict[str, List[str]], Dict[Tuple[str, str], float]]:
    rec_map: Dict[str, List[str]] = {gtin: [] for gtin in gtins}
    score_map: Dict[Tuple[str, str], float] = {}

    for gtin in gtins:
        try:
            _, recs = suggest_candidates_by_gtin(gtin, k=k)
        except Exception:
            continue
        for cand_gtin, score, _ in recs:
            normalized = _normalize_id(cand_gtin) or cand_gtin
            if not normalized or normalized not in allowed:
                continue
            rec_map[gtin].append(normalized)
            score_map[(gtin, normalized)] = float(score)

    return rec_map, score_map


def _build_mutual_map(rec_map: Dict[str, List[str]]) -> Dict[str, Set[str]]:
    mutual: Dict[str, Set[str]] = {gtin: set() for gtin in rec_map}
    for origin, candidates in rec_map.items():
        for candidate in candidates:
            peers = rec_map.get(candidate)
            if peers is None:
                continue
            if origin in peers:
                mutual[origin].add(candidate)
    return mutual


def _triad_score(triad: Tuple[str, str, str], score_map: Dict[Tuple[str, str], float]) -> float:
    total = 0.0
    count = 0
    for a, b in itertools.permutations(triad, 2):
        score = score_map.get((a, b))
        if score is not None:
            total += score
            count += 1
    return total / count if count else 0.0


def _find_triads(
    rec_map: Dict[str, List[str]],
    score_map: Dict[Tuple[str, str], float],
) -> List[List[str]]:
    mutual = _build_mutual_map(rec_map)
    triads: List[Tuple[float, List[str]]] = []
    seen: Set[Tuple[str, str, str]] = set()

    for anchor, neighbors in mutual.items():
        if len(neighbors) < 2:
            continue
        for b, c in itertools.combinations(sorted(neighbors), 2):
            if c not in mutual.get(b, set()):
                continue
            triad = tuple(sorted((anchor, b, c)))
            if triad in seen:
                continue
            seen.add(triad)
            triads.append((_triad_score(triad, score_map), list(triad)))

    triads.sort(key=lambda item: item[0], reverse=True)
    return [triad for _, triad in triads]


def _pick_disjoint_triads(triads: List[List[str]], needed: int) -> List[List[str]]:
    selected: List[List[str]] = []
    used: Set[str] = set()
    for triad in triads:
        if any(gtin in used for gtin in triad):
            continue
        selected.append(triad)
        used.update(triad)
        if len(selected) == needed:
            return selected
    return []


def _select_category_groups(
    category_to_gtins: Dict[str, List[str]],
) -> List[Tuple[str, List[List[str]]]]:
    selections: List[Tuple[str, List[List[str]]]] = []
    sorted_categories = sorted(
        category_to_gtins.keys(),
        key=lambda key: len(category_to_gtins[key]),
        reverse=True,
    )

    for category in sorted_categories:
        gtins = category_to_gtins[category]
        if len(gtins) < GROUP_SIZE * TRIADS_PER_CATEGORY:
            continue
        sample = gtins[:MAX_PRODUCTS_PER_CATEGORY]
        rec_map, score_map = _compute_recommendations(sample, set(sample), RECOMMENDATIONS_PER_PRODUCT)
        triads = _find_triads(rec_map, score_map)
        chosen = _pick_disjoint_triads(triads, TRIADS_PER_CATEGORY)
        if not chosen:
            continue
        selections.append((category, chosen))
        if len(selections) == REQUIRED_CATEGORIES:
            break

    if len(selections) < REQUIRED_CATEGORIES:
        raise RuntimeError(
            "Unable to find two categories that contain two disjoint triads of mutual substitutes."
        )

    return selections


def _assemble_output(
    selections: List[Tuple[str, List[List[str]]]],
    product_lookup: Dict[str, ProductDict],
) -> Dict[str, Any]:
    payload = {
        "source": "@vaimo_products",
        "categories": [],
    }
    total_products = 0

    for category, groups in selections:
        group_entries = []
        for idx, triad in enumerate(groups, start=1):
            products = [product_lookup[gtin] for gtin in triad]
            group_entries.append(
                {
                    "groupIndex": idx,
                    "products": products,
                }
            )
            total_products += len(products)
        payload["categories"].append(
            {
                "categoryId": category,
                "groups": group_entries,
            }
        )

    expected = REQUIRED_CATEGORIES * TRIADS_PER_CATEGORY * GROUP_SIZE
    if total_products != expected:
        raise RuntimeError(f"Expected {expected} products, but gathered {total_products}.")

    payload["totalProducts"] = total_products
    return payload


def main() -> None:
    _patch_availability_module()
    product_lookup, category_to_gtins = _build_catalog()
    selections = _select_category_groups(category_to_gtins)
    payload = _assemble_output(selections, product_lookup)
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()

