from __future__ import annotations

import argparse
import os
from typing import List

import psycopg
from psycopg.rows import dict_row

# Ensure repo-root imports
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from services.substitution_service.availability import (  # noqa: E402
    get_availability_for_gtins,
    get_db_conninfo,
)


def upsert_item(product_code: str, qty: float, unit: str = "ST", name: str = "Test item") -> None:
    conninfo = get_db_conninfo()
    with psycopg.connect(conninfo, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            # If line_id is PK, create a deterministic one from hash
            line_id = abs(hash(product_code)) % 2_000_000_000
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
                (line_id, product_code, name, qty, unit),
            )
        conn.commit()


def main() -> None:
    parser = argparse.ArgumentParser(description="Test warehouse availability retrieval.")
    parser.add_argument("--codes", nargs="+", required=True, help="Product codes (GTINs) to query")
    parser.add_argument("--seed", action="store_true", help="Seed warehouse_items with qty for provided codes")
    parser.add_argument("--qty", type=float, default=10.0, help="Qty to seed when --seed is used")
    args = parser.parse_args()

    if args.seed:
        for code in args.codes:
            upsert_item(product_code=code, qty=args.qty)
        print(f"[seed] Upserted {len(args.codes)} items with qty={args.qty}")

    avail = get_availability_for_gtins(args.codes)
    print("[availability]", avail)


if __name__ == "__main__":
    main()


