from __future__ import annotations

import os
from typing import Dict, Iterable, List, Optional

import psycopg
from psycopg.rows import dict_row


def _env(key: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(key)
    return v if v is not None else default


def get_db_conninfo() -> str:
    host = _env("WAREHOUSE_DB_HOST", "localhost")
    port = _env("WAREHOUSE_DB_PORT", "6000")
    db = _env("WAREHOUSE_DB_NAME", "warehouse")
    user = _env("WAREHOUSE_DB_USER", "warehouse_user")
    pwd = _env("WAREHOUSE_DB_PASSWORD", "warehouse_pass")
    return f"host={host} port={port} dbname={db} user={user} password={pwd}"


def get_availability_for_gtins(gtins: Iterable[str]) -> Dict[str, float]:
    """
    Query warehouse_items for the provided product codes (GTINs) and return qty per product_code.
    """
    codes = [g for g in {str(g) for g in gtins} if g]
    if not codes:
        return {}
    conninfo = get_db_conninfo()
    result: Dict[str, float] = {}
    # Use a simple IN clause; psycopg can expand list with ANY as well
    placeholders = ", ".join(["%s"] * len(codes))
    query = f"""
        SELECT product_code, qty
        FROM warehouse_items
        WHERE product_code IN ({placeholders})
    """
    with psycopg.connect(conninfo, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute(query, codes)
            for row in cur.fetchall():
                code = str(row["product_code"])
                qty = float(row["qty"])
                # Keep max qty if duplicates (shouldn't happen with PK, but safe)
                prev = result.get(code)
                result[code] = max(qty, prev if prev is not None else 0.0)
    return result


