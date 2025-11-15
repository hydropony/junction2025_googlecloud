from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional, Dict, Any
import sys

# Ensure repo root is on sys.path so `services.*` imports work
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from services.substitution_service.data_loaders import product_data_df  # noqa: E402
from services.substitution_service.main import _extract_display_name  # noqa: E402
from services.substitution_service.candidates import _normalize_id  # noqa: E402
from services.substitution_service.availability import (  # noqa: E402
    get_db_conninfo,
)
import psycopg
from psycopg.rows import dict_row


def get_name_by_sku(gtin: str) -> Optional[str]:
    df = product_data_df()
    # Normalize GTINs so we can match even if stored as floats like 6408430001071.0
    df = df.assign(_gtin=df["salesUnitGtin"].apply(_normalize_id))
    target = _normalize_id(gtin) or str(gtin)
    row = df[df["_gtin"] == target].head(1)
    if row.empty:
        return None
    prod = row.iloc[0].to_dict()
    return _extract_display_name(prod)


def get_name_by_line_id(line_id: int) -> Optional[str]:
    """
    Lookup warehouse_items by line_id and return its `name` column.
    """
    conninfo = get_db_conninfo()
    with psycopg.connect(conninfo, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT name FROM warehouse_items WHERE line_id = %s",
                (line_id,),
            )
            row: Optional[Dict[str, Any]] = cur.fetchone()
            if not row:
                return None
            return str(row["name"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Lookup product name by GTIN (salesUnitGtin) or by warehouse line_id."
    )
    parser.add_argument(
        "--gtin",
        help="GTIN / salesUnitGtin of the product (catalog name lookup)",
    )
    parser.add_argument(
        "--line-id",
        type=int,
        help="warehouse_items.line_id (DB name lookup)",
    )
    args = parser.parse_args()

    name: Optional[str] = None
    if args.line_id is not None:
        name = get_name_by_line_id(args.line_id)
    elif args.gtin is not None:
        name = get_name_by_sku(args.gtin)
    else:
        parser.error("Provide either --gtin or --line-id")

    if name is None:
        print("NOT FOUND")
    else:
        print(name)

