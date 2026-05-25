import numpy as np
import pandas as pd


def split_features_target(df: pd.DataFrame):
    X = df.drop(columns=["Survived"])
    y = df["Survived"]

    return X, y


def to_numpy(X: pd.DataFrame):
    """Conversión Pandas -> NumPy."""
    return np.array(X)
