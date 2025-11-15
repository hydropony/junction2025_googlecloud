from __future__ import annotations

import joblib
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np

DEFAULT_MODEL_PATHS = [
    Path("models/substitution_rf.joblib"),
]


class ModelScorer:
    def __init__(self, artifact: Dict[str, Any]) -> None:
        self.model = artifact.get("model")
        self.feature_names: List[str] = list(artifact.get("feature_names", []))
        if not self.model or not self.feature_names:
            raise ValueError("Invalid model artifact")

    def score(self, feature_dict: Dict[str, float]) -> float:
        x = np.asarray([[float(feature_dict.get(fn, 0.0)) for fn in self.feature_names]], dtype=np.float32)
        proba = self.model.predict_proba(x)
        # Handle single-class models gracefully
        if proba.ndim == 2 and proba.shape[1] > 1:
            pos = proba[:, 1]
        else:
            # If only one class present in the trained model, fall back to a neutral score
            # (the caller should ideally avoid using single-class models)
            if hasattr(self.model, "classes_") and len(getattr(self.model, "classes_", [])) == 1:
                # If the single class is 1, use its probability; else use 1 - prob
                cls = self.model.classes_[0]
                base = proba.ravel()[0] if proba.size else 0.5
                pos = np.asarray([base if cls == 1 else 1.0 - base], dtype=np.float32)
            else:
                pos = proba.ravel() if proba.size else np.asarray([0.5], dtype=np.float32)
        return float(pos[0])


_SCORER: Optional[ModelScorer] = None


def load_default_model() -> Optional[ModelScorer]:
    global _SCORER
    if _SCORER is not None:
        return _SCORER
    for p in DEFAULT_MODEL_PATHS:
        if p.exists():
            artifact = joblib.load(p)
            # Avoid using single-class models; fall back to heuristic
            mdl = artifact.get("model")
            if hasattr(mdl, "classes_") and len(getattr(mdl, "classes_", [])) < 2:
                return None
            _SCORER = ModelScorer(artifact)
            return _SCORER
    return None


