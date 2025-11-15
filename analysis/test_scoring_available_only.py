from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any, Dict, List

# Ensure repo root on path
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from services.substitution_service.candidates import (  # noqa: E402
    suggest_candidates_by_gtin,
)
from services.substitution_service.candidates import _normalize_id  # noqa: E402
from services.substitution_service.main import _extract_display_name  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser(description="Test feature scoring using only available products from DB.")
    ap.add_argument("--sku", required=True, help="Original GTIN (salesUnitGtin)")
    ap.add_argument("--k", type=int, default=3, help="Top-K results")
    ap.add_argument("--required-qty", type=float, default=None, help="Required qty; filter candidates with qty >= this")
    args = ap.parse_args()

    orig, scored = suggest_candidates_by_gtin(
        args.sku,
        k=args.k,
        available_qty_by_code=None,   # let the generator resolve availability via DB
        required_qty=args.required_qty,
    )

    out = {
        "original": {
            "sku": _normalize_id((orig or {}).get("salesUnitGtin")) if isinstance(orig, dict) else args.sku,
            "category": (orig or {}).get("category") if isinstance(orig, dict) else None,
            "name": _extract_display_name(orig) if isinstance(orig, dict) else None,
        },
        "results": [
            {
                "sku": sku,
                "score": round(score, 4),
                "name": _extract_display_name(_cand),
            }
            for (sku, score, _cand) in scored
        ],
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()


