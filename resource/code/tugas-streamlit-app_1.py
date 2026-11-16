# -*- coding: utf-8 -*-
"""Streamlit dashboard application for Room Occupancy Detection & Model Analysis (Tugas)."""

import json
from pathlib import Path
from typing import Any

import joblib
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Room Occupancy Predictor",
    page_icon="[App]",
    layout="wide",
)

BASE_DIR = Path(__file__).resolve().parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"
MODEL_PATH = ARTIFACTS_DIR / "occupancy_model.joblib"
SUMMARY_PATH = ARTIFACTS_DIR / "analysis_summary.json"

LABEL_MAP = {
    0: "Not Occupied (Kosong)",
    1: "Occupied (Terisi)",
}

FEATURE_META = {
    "Temperature": {"label": "Temperature (C)", "step": 0.1, "format": "%.4f"},
    "Humidity": {"label": "Humidity (%)", "step": 0.1, "format": "%.4f"},
    "Light": {"label": "Light (Lux)", "step": 1.0, "format": "%.4f"},
    "CO2": {"label": "CO2 (ppm)", "step": 1.0, "format": "%.4f"},
    "HumidityRatio": {"label": "HumidityRatio (kg/kg)", "step": 0.0001, "format": "%.6f"},
}


@st.cache_resource(show_spinner=True)
def load_model(path: str = str(MODEL_PATH)):
    """Load and cache the serialized scikit-learn pipeline."""
    return joblib.load(path)


@st.cache_data
def load_summary(path: str = str(SUMMARY_PATH)) -> dict[str, Any]:
    """Load and cache dataset summary and 5-model evaluation metrics."""
    return json.loads(Path(path).read_text(encoding="utf-8"))


summary = load_summary(str(SUMMARY_PATH))
FEATURE_COLUMNS: list[str] = summary["dataset"]["features"]
sample_occupied: dict[str, float] = summary["sample_cases"]["occupied"]
sample_not_occupied: dict[str, float] = summary["sample_cases"]["not_occupied"]
feature_stats: dict[str, dict[str, float]] = summary["dataset"]["feature_stats"]

# Initialize session state with Occupied sample values if missing
for col in FEATURE_COLUMNS:
    if col not in st.session_state:
        st.session_state[col] = float(sample_occupied[col])

# Sidebar information
with st.sidebar:
    st.header("Informasi Proyek")
    st.write(
        "Dashboard ini memprediksi status keterisian ruangan (**Room Occupancy**) "
        "berdasarkan 5 sensor lingkungan menggunakan model terbaik dari evaluasi "
        "5 algoritma pada `UTS_PPD.ipynb`."
    )
    st.subheader("Ringkasan Dataset")
    st.caption(f"Sumber: `{summary['dataset']['source']}`")
    st.write(f"- Total Baris: **{summary['dataset']['total_rows']:,}**")
    st.write(
        f"- Split 70/30: **{summary['dataset']['train_rows']:,}** train / "
        f"**{summary['dataset']['test_rows']:,}** test"
    )
    st.write(f"- Missing Values: **{summary['dataset']['missing_values']}**")
    st.write(
        f"- Kelas 0 (Kosong): **{summary['dataset']['class_counts']['0']:,}**\n"
        f"- Kelas 1 (Terisi): **{summary['dataset']['class_counts']['1']:,}**"
    )
    st.subheader("Model Aktif")
    st.info(f"**{summary['best_model_name']}**\n\nPipeline: `StandardScaler` + Classifier")

st.title("Room Occupancy Detection & Model Analysis")
st.caption(
    "Aplikasi prediksi okupansi ruangan dan perbandingan performa 5 model klasifikasi "
    "(Logistic Regression, KNN, Decision Tree, Random Forest, AdaBoost)."
)

# Preset & Reset buttons must run before form widgets are instantiated
preset_col1, preset_col2, preset_col3 = st.columns(3)
with preset_col1:
    if st.button("Preset Occupied (Terisi)", type="secondary"):
        for col in FEATURE_COLUMNS:
            st.session_state[col] = float(sample_occupied[col])
        st.rerun()
with preset_col2:
    if st.button("Preset Not Occupied (Kosong)", type="secondary"):
        for col in FEATURE_COLUMNS:
            st.session_state[col] = float(sample_not_occupied[col])
        st.rerun()
with preset_col3:
    if st.button("Reset ke Rata-rata (Mean)", type="secondary"):
        for col in FEATURE_COLUMNS:
            st.session_state[col] = float(feature_stats[col]["mean"])
        st.rerun()

tab_pred, tab_eval = st.tabs(["Prediksi Okupansi", "Analisis & Evaluasi 5 Model"])

with tab_pred:
    with st.form("occupancy-form"):
        st.subheader("Input Nilai Sensor Lingkungan")
        col1, col2 = st.columns(2)
        inputs: dict[str, float] = {}

        with col1:
            for col in FEATURE_COLUMNS[:3]:
                meta = FEATURE_META[col]
                inputs[col] = st.number_input(
                    meta["label"],
                    min_value=0.0,
                    step=meta["step"],
                    format=meta["format"],
                    key=col,
                )
        with col2:
            for col in FEATURE_COLUMNS[3:]:
                meta = FEATURE_META[col]
                inputs[col] = st.number_input(
                    meta["label"],
                    min_value=0.0,
                    step=meta["step"],
                    format=meta["format"],
                    key=col,
                )

        submitted = st.form_submit_button("Predict Occupancy")

    if submitted:
        with st.spinner("Loading pipeline and running inference..."):
            model = load_model(str(MODEL_PATH))
            df_input = pd.DataFrame(
                [[float(inputs[col]) for col in FEATURE_COLUMNS]],
                columns=FEATURE_COLUMNS,
            )
            pred_class = int(model.predict(df_input)[0])
            status = LABEL_MAP.get(pred_class, "Unknown")

            if hasattr(model, "predict_proba"):
                probs = model.predict_proba(df_input)[0]
                prob_not_occupied = round(float(probs[0]) * 100, 2)
                prob_occupied = round(float(probs[1]) * 100, 2)
                confidence = round(float(max(probs)) * 100, 1)
            else:
                prob_not_occupied = 100.0 if pred_class == 0 else 0.0
                prob_occupied = 100.0 if pred_class == 1 else 0.0
                confidence = 100.0

        st.success("Prediction complete")
        m_col1, m_col2, m_col3 = st.columns(3)
        m_col1.metric(label="Predicted Occupancy", value=status)
        m_col2.metric(label="Confidence", value=f"{confidence:.1f}%")
        m_col3.metric(label="Active Model", value=summary["best_model_name"])

        st.write(
            f"**Distribusi Probabilitas:** Not Occupied = `{prob_not_occupied:.2f}%` | "
            f"Occupied = `{prob_occupied:.2f}%`"
        )

        with st.expander("Input Sensor Summary"):
            st.write(
                {
                    "inputs": inputs,
                    "predicted_class": pred_class,
                    "status": status,
                    "probabilities_percent": {
                        "not_occupied": prob_not_occupied,
                        "occupied": prob_occupied,
                    },
                }
            )

with tab_eval:
    st.subheader("Ringkasan Dataset & Evaluasi 5 Model Klasifikasi")
    ds = summary["dataset"]
    d_col1, d_col2, d_col3, d_col4 = st.columns(4)
    d_col1.metric(label="Total Rows", value=f"{ds['total_rows']:,}")
    d_col2.metric(label="Train Split (70%)", value=f"{ds['train_rows']:,}")
    d_col3.metric(label="Test Split (30%)", value=f"{ds['test_rows']:,}")
    d_col4.metric(label="Best Model", value=summary["best_model_name"])

    st.markdown("#### Perbandingan Metrik Evaluasi (Test Set)")
    df_models = pd.DataFrame(
        [
            {
                "Model": row["name"],
                "Accuracy": row["accuracy"],
                "Precision (Macro)": row["precision_macro"],
                "Recall (Macro)": row["recall_macro"],
                "F1-Score (Macro)": row["f1_macro"],
            }
            for row in summary["models"]
        ]
    )
    st.dataframe(df_models, hide_index=True)

    st.markdown("#### Grafik Perbandingan Akurasi & F1-Score")
    df_chart = df_models.set_index("Model")[["Accuracy", "F1-Score (Macro)"]]
    st.bar_chart(df_chart)

    best_row = next(
        row for row in summary["models"] if row["name"] == summary["best_model_name"]
    )
    cm = best_row["confusion_matrix"]
    st.markdown(f"#### Confusion Matrix Model Terbaik ({summary['best_model_name']})")
    df_cm = pd.DataFrame(
        cm,
        index=["Actual: Not Occupied (0)", "Actual: Occupied (1)"],
        columns=["Predicted: Not Occupied (0)", "Predicted: Occupied (1)"],
    )
    st.dataframe(df_cm)

    st.markdown("#### Statistik Deskriptif Fitur Sensor")
    df_stats = pd.DataFrame.from_dict(feature_stats, orient="index")
    df_stats.index.name = "Feature"
    df_stats = df_stats.rename(columns={"min": "Min", "mean": "Mean", "max": "Max"})
    st.dataframe(df_stats)
