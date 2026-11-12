# -*- coding: utf-8 -*-
"""Flask web application for Hepatitis C (HCV) Disease Prediction (Latihan)."""

import os
from pathlib import Path
from typing import Optional

import joblib
import pandas as pd
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

MODEL_PATH = Path(__file__).resolve().parent / "dt_model.model"
LOADED_MODEL = joblib.load(MODEL_PATH)

COLUMNS_ORDER = [
    "Sex", "Age", "ALB", "ALP", "ALT", "AST",
    "BIL", "CHE", "CHOL", "CREA", "GGT", "PROT",
]

DIAGNOSIS_MAP = {
    0: "Suspect Blood Donor",
    1: "Hepatitis",
    2: "Fibrosis",
    3: "Cirrhosis",
}


def _to_float(value: Optional[str]) -> float:
    """Convert form string input to float, returning NaN when empty."""
    return float(value) if value is not None and value.strip() != "" else float("nan")


def _encode_sex(value: Optional[str]) -> int:
    """Encode sex string ('m'/'f'/'1'/'0') to match LabelEncoder order."""
    if value is None:
        return 0
    normalized = str(value).strip().lower()
    if normalized in ("m", "male", "1", "true"):
        return 1
    if normalized in ("f", "female", "0", "false"):
        return 0
    try:
        return int(float(normalized))
    except ValueError:
        return 0


@app.route("/")
def root_redirect():
    """Redirect root URL to the tabular form page."""
    return redirect(url_for("index"))


@app.route("/tabular/")
def index():
    """Render the disease prediction input form."""
    return render_template("index.html")


@app.route("/tabular/result/", methods=["POST"])
def prediction_result():
    """Receive form input, run model inference, and render prediction result."""
    age = request.form.get("age")
    sex = request.form.get("sex")
    alb = request.form.get("alb")
    alp = request.form.get("alp")
    alt = request.form.get("alt")
    ast = request.form.get("ast")
    bil = request.form.get("bil")
    che = request.form.get("che")
    chol = request.form.get("chol")
    crea = request.form.get("crea")
    ggt = request.form.get("ggt")
    prot = request.form.get("prot")

    df_input = pd.DataFrame(
        [[
            _encode_sex(sex), _to_float(age), _to_float(alb), _to_float(alp),
            _to_float(alt), _to_float(ast), _to_float(bil), _to_float(che),
            _to_float(chol), _to_float(crea), _to_float(ggt), _to_float(prot),
        ]],
        columns=COLUMNS_ORDER,
    )

    result = LOADED_MODEL.predict(df_input)
    int_result = int(result[0])
    decision = DIAGNOSIS_MAP.get(int_result, "Not defined")

    return render_template(
        "result.html",
        age=age, sex=sex, alb=alb, alp=alp, alt=alt, ast=ast,
        bil=bil, che=che, chol=chol, crea=crea, ggt=ggt, prot=prot,
        status=decision,
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="127.0.0.1", port=port, debug=True)
