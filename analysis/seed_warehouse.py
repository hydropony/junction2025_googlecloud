from __future__ import annotations

import argparse
import random
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

import psycopg
from psycopg.rows import dict_row

# Ensure repo-root imports
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from services.substitution_service.data_loaders import product_data_df  # noqa: E402
from services.substitution_service.candidates import _normalize_id  # noqa: E402
from services.substitution_service.availability import get_db_conninfo  # noqa: E402


def extract_name(product: Dict[str, Any]) -> Optional[str]:
    sd = product.get("synkkaData")
    if isinstance(sd, dict):
        names = sd.get("names")
        if isinstance(names, list):
            preferred = ["en", "fi", "sv"]
            first_any: Optional[str] = None
            for n in names:
                if isinstance(n, dict) and isinstance(n.get("value"), str):
                    if first_any is None:
                        first_any = n["value"]
            for lang in preferred:
                for n in names:
                    if isinstance(n, dict) and n.get("language") == lang and isinstance(n.get("value"), str):
                        return n["value"]
            if first_any:
                return first_any
    vendor = product.get("vendorName")
    if isinstance(vendor, str) and vendor:
        return vendor
    return None


def extract_unit(product: Dict[str, Any]) -> str:
    su = product.get("salesUnit")
    if isinstance(su, str) and su:
        return su
    return "ST"


def choose_products(
    df, limit: int, categories: Optional[Set[str]] = None
) -> List[Dict[str, Any]]:
    pool = df
    if categories:
        pool = pool[pool["category"].astype(str).isin(categories)]
    if limit and len(pool) > limit:
        pool = pool.sample(n=limit, random_state=42)
    return [row._asdict() if hasattr(row, "_asdict") else row.to_dict() for _, row in pool.iterrows()]


def seed_items(products: List[Dict[str, Any]], qty_min: float, qty_max: float, zero_prob: float) -> int:
    conninfo = get_db_conninfo()
    total = 0
    with psycopg.connect(conninfo, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            for prod in products:
                code = _normalize_id(prod.get("salesUnitGtin"))
                if not code:
                    continue
                name = extract_name(prod) or f"Product {code}"
                unit = extract_unit(prod)
                # Random qty with some zero-probability for out-of-stock examples
                if random.random() < zero_prob:
                    qty = 0.0
                else:
                    qty = round(random.uniform(qty_min, qty_max), 2)
                line_id = abs(hash(code)) % 2_000_000_000
                cur.execute(
                    """
                    INSERT INTO warehouse_items (line_id, product_code, name, qty, unit)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (line_id) DO UPDATE SET
                        product_code = EXCLUDED.product_code,
                        name = EXCLUDED.name,
                        qty = EXCLUDED.qty,
                        unit = EXCLUDED.unit
                    """,
                    (line_id, code, name, qty, unit),
                )
                total += 1
        conn.commit()
    return total


def main() -> None:
    ap = argparse.ArgumentParser(description="Seed warehouse_items from product catalog.")
    ap.add_argument("--limit", type=int, default=500, help="Max number of products to seed")
    ap.add_argument("--categories", type=str, default=None, help="Comma-separated category ids to include")
    ap.add_argument("--qty-min", type=float, default=1.0, help="Minimum non-zero qty")
    ap.add_argument("--qty-max", type=float, default=20.0, help="Maximum qty")
    ap.add_argument("--zero-prob", type=float, default=0.15, help="Probability to seed qty=0 (out of stock)")
    args = ap.parse_args()

    cats: Optional[Set[str]] = None
    if args.categories:
        cats = {c.strip() for c in args.categories.split(",") if c.strip()}

    df = product_data_df()
    if "salesUnitGtin" not in df.columns:
        print("[seed] salesUnitGtin not found in product data")
        return
    # Normalize GTINs and drop nulls
    df = df.assign(salesUnitGtin=df["salesUnitGtin"].apply(_normalize_id))
    df = df.dropna(subset=["salesUnitGtin"])

    products = choose_products(df, args.limit, cats)
    count = seed_items(products, args.qty_min, args.qty_max, args.zero_prob)
    print(f"[seed] Upserted {count} items into warehouse_items")


if __name__ == "__main__":
    main()


