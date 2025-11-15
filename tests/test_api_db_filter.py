from __future__ import annotations

from typing import Any, Dict, Optional, Tuple

import psycopg
import pytest
from psycopg.rows import dict_row
from fastapi.testclient import TestClient
import random

from services.substitution_service.availability import get_db_conninfo
from services.substitution_service.data_loaders import product_data_df
from services.substitution_service.candidates import _normalize_id
from services.substitution_service.main import app


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


def _pick_three_same_category() -> Tuple[str, str, str]:
    df = product_data_df()
    assert "salesUnitGtin" in df.columns
    # Normalize gtin and drop null
    df = df.assign(salesUnitGtin=df["salesUnitGtin"].apply(_normalize_id)).dropna(subset=["salesUnitGtin"])
    # Find a category with at least 3 products
    grp = df.groupby(df["category"].astype(str))
    for cat, g in grp:
        if len(g) >= 3:
            g = g.head(3).reset_index(drop=True)
            a = str(g.loc[0, "salesUnitGtin"])
            b = str(g.loc[1, "salesUnitGtin"])
            c = str(g.loc[2, "salesUnitGtin"])
            return a, b, c
    # As a fallback, sample 3 arbitrary (test may be fragile)
    g = df.head(3).reset_index(drop=True)
    return str(g.loc[0, "salesUnitGtin"]), str(g.loc[1, "salesUnitGtin"]), str(g.loc[2, "salesUnitGtin"])


def _upsert_item(code: str, qty: float) -> None:
    # Deterministic line_id and clean previous rows to avoid leftovers
    try:
        line_id = int(str(code)[-9:])
    except Exception:
        line_id = abs(hash(code)) % 2_000_000_000
    with psycopg.connect(get_db_conninfo(), row_factory=dict_row) as conn:
        with conn.cursor() as cur:
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


def test_api_filters_by_db_availability():
    orig, cand_ok, cand_low = _pick_three_same_category()
    # Seed candidates in DB: cand_ok has enough qty, cand_low does not
    _upsert_item(cand_ok, 10.0)
    _upsert_item(cand_low, 2.0)
    client = TestClient(app)
    required_qty = 5.0
    resp = client.post(
        "/substitution/suggest",
        json={
            "sku": orig,
            "k": 10,
            "requiredQty": required_qty
        },
    )
    assert resp.status_code == 200, resp.text
    data = resp.json()
    recs = data.get("recommendations", [])
    rec_skus = [r["sku"] for r in recs]
    # cand_ok should be present; cand_low should be filtered out
    assert cand_ok in rec_skus
    assert cand_low not in rec_skus


