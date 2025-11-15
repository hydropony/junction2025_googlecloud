from __future__ import annotations

import os
import random
from typing import Dict

import psycopg
import pytest
from psycopg.rows import dict_row

from services.substitution_service.availability import get_db_conninfo, get_availability_for_gtins


def _can_connect() -> bool:
    try:
        with psycopg.connect(get_db_conninfo(), row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                cur.fetchone()
        return True
    except Exception:
        return False


pytestmark = pytest.mark.skipif(not _can_connect(), reason="Warehouse DB not reachable")


def _upsert_item(code: str, qty: float) -> None:
    # Ensure deterministic and single row per product_code for tests
    try:
        line_id = int(str(code)[-9:])  # use last 9 digits for a stable integer
    except Exception:
        line_id = 1
    with psycopg.connect(get_db_conninfo(), row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            # Remove any existing rows for this product_code to avoid stale values
            cur.execute("DELETE FROM warehouse_items WHERE product_code = %s", (code,))
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
                (line_id, code, f"Test {code}", qty, "ST"),
            )
        conn.commit()


def test_get_availability_for_gtins_roundtrip():
    # Seed two codes
    codes = ["6408430001132", "6408430001064"]
    _upsert_item(codes[0], 12.0)
    _upsert_item(codes[1], 3.0)
    avail: Dict[str, float] = get_availability_for_gtins(codes)
    assert isinstance(avail, dict)
    assert avail.get(codes[0]) == pytest.approx(12.0, rel=0, abs=1e-6)
    assert avail.get(codes[1]) == pytest.approx(3.0, rel=0, abs=1e-6)


