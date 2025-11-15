from __future__ import annotations

from typing import Dict, Any

import pytest

from services.substitution_service.features import compute_pair_features
from services.substitution_service.candidates import heuristic_score


def _base_product() -> Dict[str, Any]:
    return {
        "salesUnitGtin": "0000000000001",
        "salesUnit": "ST",
        "category": "TEST",
        "vendorName": "Test Vendor",
        "brand": "Test Brand",
        "allowedLotSize": 1.0,
        "temperatureCondition": 4.0,
    }


def test_allergen_conflict_reduces_score():
    orig = _base_product()
    # Original explicitly FREE_FROM lactose via nonAllergen and nutritionalClaim
    orig["classifications"] = [
        {
            "type": "ENUM",
            "name": "nonAllergen",
            "values": [
                {"id": "LACTOSE", "unit": "FREE_FROM"},
            ],
        },
        {
            "type": "ENUM",
            "name": "nutritionalClaim",
            "values": [
                {"id": "FREE_FROM_LACTOSE", "synkkaId": "LACTOSE", "unit": "FREE_FROM"},
            ],
        },
    ]

    # Candidate A: respects lactose-free (no allergen entry)
    cand_ok = _base_product()

    # Candidate B: contains lactose allergen -> should trigger conflict
    cand_conflict = _base_product()
    cand_conflict["classifications"] = [
        {
            "type": "ENUM",
            "name": "allergen",
            "values": [
                {"id": "LACTOSE", "unit": "CONTAINS"},
            ],
        },
    ]

    feats_ok = compute_pair_features(orig, cand_ok)
    feats_conflict = compute_pair_features(orig, cand_conflict)

    assert feats_ok["allergen_conflict"] == 0.0
    assert feats_conflict["allergen_conflict"] == 1.0

    score_ok = heuristic_score(feats_ok)
    score_conflict = heuristic_score(feats_conflict)

    assert score_ok > score_conflict
    # Penalty should be at least ~1 point (given coefficient -1.0)
    assert (score_ok - score_conflict) >= 0.9


