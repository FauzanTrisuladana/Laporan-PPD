# -*- coding: utf-8 -*-
"""Training, multi-model evaluation, and pipeline serialization for Room Occupancy Detection."""

import json
from pathlib import Path
from typing import Any

import joblib
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

FEATURE_COLUMNS = ["Temperature", "Humidity", "Light", "CO2", "HumidityRatio"]


def build_candidate_models() -> dict[str, Any]:
    """Return the five classifiers evaluated in UTS_PPD.ipynb."""
    return {
        "Logistic Regression": LogisticRegression(),
        "KNN (k=10)": KNeighborsClassifier(n_neighbors=10),
        "Decision Tree (Entropy)": DecisionTreeClassifier(
            criterion="entropy", random_state=8
        ),
        "Random Forest": RandomForestClassifier(random_state=8),
        "AdaBoost": AdaBoostClassifier(random_state=8),
    }


def evaluate_models(
    x_train: pd.DataFrame,
    x_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
) -> tuple[list[dict[str, Any]], str, Pipeline]:
    """Train and evaluate candidate pipelines, returning metrics and best pipeline."""
    results: list[dict[str, Any]] = []
    best_name = ""
    best_accuracy = -1.0
    best_pipeline: Pipeline | None = None

    for name, classifier in build_candidate_models().items():
        pipeline = Pipeline(
            [
                ("scaler", StandardScaler()),
                ("classifier", classifier),
            ]
        )
        pipeline.fit(x_train, y_train)
        y_pred = pipeline.predict(x_test)

        acc = float(accuracy_score(y_test, y_pred))
        prec = float(precision_score(y_test, y_pred, average="macro"))
        rec = float(recall_score(y_test, y_pred, average="macro"))
        f1 = float(f1_score(y_test, y_pred, average="macro"))
        cm = confusion_matrix(y_test, y_pred).tolist()

        results.append(
            {
                "name": name,
                "accuracy": round(acc, 6),
                "precision_macro": round(prec, 6),
                "recall_macro": round(rec, 6),
                "f1_macro": round(f1, 6),
                "confusion_matrix": cm,
            }
        )

        if acc > best_accuracy:
            best_accuracy = acc
            best_name = name
            best_pipeline = pipeline

    if best_pipeline is None:
        raise RuntimeError("No candidate models were evaluated.")

    return results, best_name, best_pipeline


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parents[1]
    dataset_path = repo_root / "docs" / "latihan" / "ocupancy_dataset.csv"
    local_model_path = script_dir / "occupancy_model.joblib"
    web_artifacts_dir = repo_root / "tugas" / "web" / "artifacts"
    web_artifacts_dir.mkdir(parents=True, exist_ok=True)
    web_model_path = web_artifacts_dir / "occupancy_model.joblib"
    summary_path = web_artifacts_dir / "analysis_summary.json"

    df = pd.read_csv(dataset_path)
    missing_total = int(df.isnull().sum().sum())
    class_counts = {str(k): int(v) for k, v in df["Occupancy"].value_counts().to_dict().items()}

    print("=== RINGKASAN DATASET OCCUPANCY ===")
    print(f"Path dataset   : {dataset_path}")
    print(f"Total baris    : {len(df)}")
    print(f"Total kolom    : {df.shape[1]} ({list(df.columns)})")
    print(f"Missing values : {missing_total}")
    print(f"Distribusi kelas (0=Kosong, 1=Terisi): {class_counts}")

    df_x = df[FEATURE_COLUMNS]
    df_y = df["Occupancy"]

    x_train, x_test, y_train, y_test = train_test_split(
        df_x, df_y, test_size=0.3, random_state=8
    )
    print(f"Split 70/30    : train={len(x_train)}, test={len(x_test)}")

    results, best_name, best_pipeline = evaluate_models(x_train, x_test, y_train, y_test)

    print("\n=== HASIL EVALUASI 5 MODEL (TEST SET) ===")
    header = f"{'Model':<26} {'Accuracy':>10} {'Precision':>10} {'Recall':>10} {'F1-Score':>10}"
    print(header)
    print("-" * len(header))
    for row in results:
        print(
            f"{row['name']:<26} "
            f"{row['accuracy']:>10.4f} "
            f"{row['precision_macro']:>10.4f} "
            f"{row['recall_macro']:>10.4f} "
            f"{row['f1_macro']:>10.4f}"
        )

    print(f"\nModel terbaik terpilih: {best_name}")
    joblib.dump(best_pipeline, local_model_path)
    joblib.dump(best_pipeline, web_model_path)
    print(f"Pipeline disimpan ke  : {local_model_path}")
    print(f"Pipeline disalin ke   : {web_model_path}")

    feature_stats = {
        col: {
            "min": round(float(df_x[col].min()), 6),
            "mean": round(float(df_x[col].mean()), 6),
            "max": round(float(df_x[col].max()), 6),
        }
        for col in FEATURE_COLUMNS
    }

    occupied_row = df[df["Occupancy"] == 1].iloc[0]
    empty_row = df[df["Occupancy"] == 0].iloc[0]

    summary_payload = {
        "dataset": {
            "source": "docs/latihan/ocupancy_dataset.csv",
            "total_rows": int(len(df)),
            "train_rows": int(len(x_train)),
            "test_rows": int(len(x_test)),
            "missing_values": missing_total,
            "class_counts": class_counts,
            "features": FEATURE_COLUMNS,
            "feature_stats": feature_stats,
        },
        "best_model_name": best_name,
        "models": results,
        "sample_cases": {
            "occupied": {col: float(occupied_row[col]) for col in FEATURE_COLUMNS},
            "not_occupied": {col: float(empty_row[col]) for col in FEATURE_COLUMNS},
        },
    }

    summary_path.write_text(json.dumps(summary_payload, indent=2), encoding="utf-8")
    print(f"Ringkasan analisis ke : {summary_path}")


if __name__ == "__main__":
    main()
