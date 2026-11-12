# -*- coding: utf-8 -*-
"""Flask dashboard application for Room Occupancy Prediction & Model Analysis."""

import json
import os
from pathlib import Path
from typing import Any

import joblib
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"
MODEL_PATH = ARTIFACTS_DIR / "occupancy_model.joblib"
SUMMARY_PATH = ARTIFACTS_DIR / "analysis_summary.json"

LOADED_MODEL = joblib.load(MODEL_PATH)
ANALYSIS_SUMMARY: dict[str, Any] = json.loads(
    SUMMARY_PATH.read_text(encoding="utf-8")
)
FEATURE_COLUMNS: list[str] = ANALYSIS_SUMMARY["dataset"]["features"]

LABEL_MAP = {
    0: "Not Occupied (Kosong)",
    1: "Occupied (Terisi)",
}


def _parse_features(form_data: Any) -> tuple[dict[str, float], list[str]]:
    """Parse and validate 5 numeric sensor fields from POST form data."""
    parsed: dict[str, float] = {}
    errors: list[str] = []

    for col in FEATURE_COLUMNS:
        raw_val = (form_data.get(col) or "").strip()
        if raw_val == "":
            errors.append(f"Field '{col}' wajib diisi.")
            continue
        try:
            parsed[col] = float(raw_val)
        except ValueError:
            errors.append(
                f"Field '{col}' harus berupa angka yang valid (input: '{raw_val}')."
            )

    return parsed, errors


@app.route("/")
def index():
    """Render the Room Occupancy dashboard, model evaluation table, and input form."""
    default_values = ANALYSIS_SUMMARY["sample_cases"]["occupied"]
    return render_template(
        "index.html",
        summary=ANALYSIS_SUMMARY,
        default_values=default_values,
        error_messages=[],
    )


@app.route("/predict", methods=["POST"])
def predict():
    """Run inference on sensor inputs and render prediction result."""
    parsed, errors = _parse_features(request.form)
    if errors:
        return (
            render_template(
                "index.html",
                summary=ANALYSIS_SUMMARY,
                default_values=request.form,
                error_messages=errors,
            ),
            400,
        )

    df_input = pd.DataFrame(
        [[parsed[col] for col in FEATURE_COLUMNS]], columns=FEATURE_COLUMNS
    )
    pred_class = int(LOADED_MODEL.predict(df_input)[0])

    if hasattr(LOADED_MODEL, "predict_proba"):
        probs = LOADED_MODEL.predict_proba(df_input)[0]
        prob_not_occupied = round(float(probs[0]) * 100, 2)
        prob_occupied = round(float(probs[1]) * 100, 2)
        confidence = round(float(max(probs)) * 100, 2)
    else:
        prob_not_occupied = 100.0 if pred_class == 0 else 0.0
        prob_occupied = 100.0 if pred_class == 1 else 0.0
        confidence = 100.0

    return render_template(
        "result.html",
        summary=ANALYSIS_SUMMARY,
        inputs=parsed,
        pred_class=pred_class,
        status=LABEL_MAP.get(pred_class, "Unknown"),
        confidence=confidence,
        prob_not_occupied=prob_not_occupied,
        prob_occupied=prob_occupied,
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="127.0.0.1", port=port, debug=True)
