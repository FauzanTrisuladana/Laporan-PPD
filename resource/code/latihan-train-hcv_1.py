# -*- coding: utf-8 -*-
"""Training and serialization script for the Hepatitis C Decision Tree model."""

from pathlib import Path
import joblib
import pandas as pd
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier


def train_and_save_decision_tree(
    features: pd.DataFrame, target: pd.Series, output_path: Path
) -> DecisionTreeClassifier:
    """Train DecisionTreeClassifier and serialize it via joblib."""
    model = DecisionTreeClassifier(random_state=0)
    model.fit(features, target)
    joblib.dump(model, output_path)
    print(f"Model berhasil disimpan ke: {output_path}")
    return model


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    dataset_path = base_dir / "hcvdat0.csv"
    model_path = base_dir / "dt_model.model"

    pd.options.display.max_columns = None
    df_ori = pd.read_csv(dataset_path)
    print(f"Dataset awal: {df_ori.shape[0]} baris, {df_ori.shape[1]} kolom")

    df_ori = df_ori.dropna().copy()
    print(f"Dataset setelah dropna(): {df_ori.shape[0]} baris")

    df_x = df_ori.drop(["Unnamed: 0", "Category"], axis=1)
    df_y = (
        df_ori["Category"]
        .replace(
            {
                "0=Blood Donor": 0,
                "0s=suspect Blood Donor": 0,
                "1=Hepatitis": 1,
                "2=Fibrosis": 2,
                "3=Cirrhosis": 3,
            }
        )
        .astype(int)
    )

    df_x_num = df_x.drop(["Sex"], axis=1)
    le = preprocessing.LabelEncoder()
    sex_encoded = pd.Series(
        le.fit_transform(df_x["Sex"]),
        index=df_x.index,
        name="Sex",
    )

    # Urutan kolom: ['Sex', 'Age', 'ALB', 'ALP', 'ALT', 'AST', 'BIL', 'CHE', 'CHOL', 'CREA', 'GGT', 'PROT']
    df_x_new = pd.concat([sex_encoded, df_x_num], axis=1)
    print("Urutan fitur:", list(df_x_new.columns))
    print("Mapping Sex LabelEncoder:", dict(zip(le.classes_, le.transform(le.classes_))))
    print("Generate Decision Tree Model")

    model = train_and_save_decision_tree(df_x_new, df_y, model_path)
    train_acc = model.score(df_x_new, df_y)
    print(f"Training accuracy (in-sample): {train_acc:.4f}")


if __name__ == "__main__":
    main()
