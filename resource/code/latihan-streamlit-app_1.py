# -*- coding: utf-8 -*-
"""Streamlit web application for Hepatitis C (HCV) Disease Prediction (Latihan)."""

from pathlib import Path
from typing import Optional

import joblib
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="HCV Tabular Predictor",
    page_icon="[HCV]",
    layout="centered",
)

st.title("Hepatitis (HCV) Tabular Predictor")
st.caption("Prediction app using the trained Decision Tree model")

MODEL_PATH = Path(__file__).resolve().parent / "dt_model.model"

COLUMNS_ORDER = [
    "Sex",
    "Age",
    "ALB",
    "ALP",
    "ALT",
    "AST",
    "BIL",
    "CHE",
    "CHOL",
    "CREA",
    "GGT",
    "PROT",
]

DIAGNOSIS_MAP = {
    0: "Suspect Blood Donor",
    1: "Hepatitis",
    2: "Fibrosis",
    3: "Cirrhosis",
}

# Default input values
DEFAULTS = {
    "age": 30,
    "sex": "Male",
    "alb": 39.0,
    "alp": 100.0,
    "alt": 28.0,
    "ast": 143.0,
    "bil": 15.0,
    "che": 5.0,
    "chol": 4.0,
    "crea": 72.0,
    "ggt": 400.0,
    "prot": 70.0,
}

# Initialize session state with defaults if missing
for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v


@st.cache_resource(show_spinner=True)
def load_model(path: str = str(MODEL_PATH)):
    """Load and cache the trained Decision Tree model from disk."""
    return joblib.load(path)


def _to_float(x: Optional[float]) -> float:
    """Convert numeric input to float, returning NaN when invalid or missing."""
    try:
        return float(x) if x is not None else float("nan")
    except Exception:
        return float("nan")


def _encode_sex(x: Optional[str]) -> int:
    """Encode sex string ('Male'/'Female'/'m'/'f'/'1'/'0') to match LabelEncoder order."""
    if x is None:
        return 0
    s = str(x).strip().lower()
    if s in ("m", "male", "1", "true"):
        return 1
    if s in ("f", "female", "0", "false"):
        return 0
    try:
        return int(float(s))
    except Exception:
        return 0


# Top-level Reset button must run before widgets are created
top_col1, top_col2 = st.columns([1, 1])
with top_col2:
    if st.button("Reset to defaults", type="secondary"):
        for k, v in DEFAULTS.items():
            st.session_state[k] = v
        st.rerun()

# Input form with 2 columns
with st.form("input-form"):
    st.subheader("Enter Patient Lab Values")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=0, max_value=120, step=1, key="age")
        sex = st.selectbox("Sex", options=["Male", "Female"], key="sex")
        alb = st.number_input("ALB (Albumin)", min_value=0.0, step=0.1, key="alb")
        alp = st.number_input("ALP (Alkaline Phosphatase)", min_value=0.0, step=0.1, key="alp")
        alt = st.number_input("ALT (Alanine Transaminase)", min_value=0.0, step=0.1, key="alt")
        ast = st.number_input("AST (Aspartate Transaminase)", min_value=0.0, step=0.1, key="ast")
    with col2:
        bil = st.number_input("BIL (Bilirubin)", min_value=0.0, step=0.1, key="bil")
        che = st.number_input("CHE (Cholinesterase)", min_value=0.0, step=0.1, key="che")
        chol = st.number_input("CHOL (Cholesterol)", min_value=0.0, step=0.1, key="chol")
        crea = st.number_input("CREA (Creatinine)", min_value=0.0, step=0.1, key="crea")
        ggt = st.number_input("GGT (Gamma-Glutamyl Transferase)", min_value=0.0, step=0.1, key="ggt")
        prot = st.number_input("PROT (Total Protein)", min_value=0.0, step=0.1, key="prot")

    submitted = st.form_submit_button("Predict")

# Prediction and result display
if submitted:
    with st.spinner("Loading model and predicting..."):
        model = load_model(str(MODEL_PATH))
        sex_enc = _encode_sex(sex)

        df_input = pd.DataFrame(
            [
                [
                    sex_enc,
                    _to_float(age),
                    _to_float(alb),
                    _to_float(alp),
                    _to_float(alt),
                    _to_float(ast),
                    _to_float(bil),
                    _to_float(che),
                    _to_float(chol),
                    _to_float(crea),
                    _to_float(ggt),
                    _to_float(prot),
                ]
            ],
            columns=COLUMNS_ORDER,
        )

        result = model.predict(df_input)
        int_result = int(result[0])
        decision = DIAGNOSIS_MAP.get(int_result, "Not defined")

    st.success("Prediction complete")
    st.metric(label="Predicted Status", value=decision)

    with st.expander("Input Summary"):
        st.write(
            {
                "age": age,
                "sex": sex,
                "alb": alb,
                "alp": alp,
                "alt": alt,
                "ast": ast,
                "bil": bil,
                "che": che,
                "chol": chol,
                "crea": crea,
                "ggt": ggt,
                "prot": prot,
            }
        )
