import joblib
import pandas as pd

FEATURE_NAMES = ["Pclass", "Sex", "Age", "Fare"]


def load_model(path: str):
    return joblib.load(path)


def predict_sample(model, sample: list):
    sample_df = pd.DataFrame([sample], columns=FEATURE_NAMES)

    prediction = model.predict(sample_df)[0]

    if prediction == 1:
        return "SURVIVED"

    return "DID NOT SURVIVE"
