import pandas as pd
import polars as pl


def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df = df[["Survived", "Pclass", "Sex", "Age", "Fare"]]

    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())

    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

    return df


def save_clean_data(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)


def inspect_with_polars(path: str):
    df = pl.read_csv(path)

    print("\nPolars describe:")

    describe_df = df.describe()

    for row in describe_df.iter_rows():
        print(row)

    print("\nPolars group by Pclass:")

    grouped = df.group_by("Pclass").count()

    for row in grouped.iter_rows():
        print(row)
