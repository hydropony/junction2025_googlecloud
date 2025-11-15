from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import pandas as pd

# Ensure repo root imports
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from services.substitution_service.data_loaders import product_data_df  # noqa: E402
from services.substitution_service.candidates import _normalize_id  # noqa: E402


def _find_columns(df: pd.DataFrame) -> Optional[Tuple[str, str]]:
    """
    Try to detect original and replacement GTIN columns in the replacement orders CSV.
    Returns a tuple (orig_col, repl_col) or None if not found.
    """
    candidates = [
        ("original_gtin", "replacement_gtin"),
        ("orig_gtin", "repl_gtin"),
        ("gtin_original", "gtin_replacement"),
        ("original_sku", "replacement_sku"),
        ("original_product_code", "replacement_product_code"),
        ("orig_product_code", "repl_product_code"),
    ]
    cols_lower = {c.lower(): c for c in df.columns}
    for oc, rc in candidates:
        if oc in cols_lower and rc in cols_lower:
            return cols_lower[oc], cols_lower[rc]
    return None


def _category_index() -> Dict[str, str]:
    """
    Build a GTIN -> category map from product catalog.
    """
    df = product_data_df()
    mapping: Dict[str, str] = {}
    if "salesUnitGtin" not in df.columns:
        return mapping
    for _, row in df.iterrows():
        gt = _normalize_id(row.get("salesUnitGtin"))
        cat = row.get("category")
        if gt and cat is not None:
            mapping[gt] = str(cat)
    return mapping


def build_pairs_from_replacement_orders(
    replacements_csv: Path,
    max_neg_per_pos: int = 5,
) -> List[Tuple[str, str, int]]:
    df = pd.read_csv(replacements_csv)
    det = _find_columns(df)
    if not det:
        raise RuntimeError(
            "Could not detect original/replacement columns in CSV. "
            "Expected one of: original_gtin/replacement_gtin, orig_gtin/repl_gtin, "
            "gtin_original/gtin_replacement, original_sku/replacement_sku, "
            "original_product_code/replacement_product_code, orig_product_code/repl_product_code."
        )
    orig_col, repl_col = det
    # Normalize identifiers
    df["_orig"] = df[orig_col].apply(_normalize_id)
    df["_repl"] = df[repl_col].apply(_normalize_id)
    df = df.dropna(subset=["_orig", "_repl"])
    # Positives
    pairs: List[Tuple[str, str, int]] = []
    pos_by_orig: Dict[str, Set[str]] = {}
    for _, r in df.iterrows():
        o = r["_orig"]
        c = r["_repl"]
        if o and c and o != c:
            pairs.append((o, c, 1))
            pos_by_orig.setdefault(o, set()).add(c)
    # Negatives: sample within same category where available, else global
    gtin_to_cat = _category_index()
    cat_to_gtins: Dict[str, List[str]] = {}
    if gtin_to_cat:
        for g, cat in gtin_to_cat.items():
            cat_to_gtins.setdefault(cat, []).append(g)
    for o, pos_set in pos_by_orig.items():
        neg_needed = max_neg_per_pos * len(pos_set)
        neg_added = 0
        # Within category if known
        pool: List[str]
        cat = gtin_to_cat.get(o)
        if cat and cat in cat_to_gtins:
            pool = cat_to_gtins[cat]
        else:
            pool = list(gtin_to_cat.keys()) if gtin_to_cat else []
        if not pool:
            continue
        banned = set(pos_set)
        banned.add(o)
        for cand in pool:
            if cand not in banned:
                pairs.append((o, cand, 0))
                neg_added += 1
                if neg_added >= neg_needed:
                    break
    return pairs


def main() -> None:
    ap = argparse.ArgumentParser(description="Build labeled pairs from replacement orders CSV.")
    ap.add_argument("--csv", required=True, help="Path to replacement orders CSV with original/replacement columns.")
    ap.add_argument("--out", default="Data/pairs_from_replacements.csv", help="Output CSV path")
    ap.add_argument("--max-neg-per-pos", type=int, default=5)
    args = ap.parse_args()
    pairs = build_pairs_from_replacement_orders(Path(args.csv), max_neg_per_pos=args.max_neg_per_pos)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["orig_gtin", "cand_gtin", "label"])
        for o, c, y in pairs:
            w.writerow([o, c, y])
    print(f"[pairs] wrote {len(pairs)} rows to {out_path}")


if __name__ == "__main__":
    main()


