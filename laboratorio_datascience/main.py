from src.laboratorio_datascience.features import split_features_target
from src.laboratorio_datascience.load_data import (
    clean_data,
    inspect_with_polars,
    load_csv,
    save_clean_data,
)
from src.laboratorio_datascience.predict import load_model, predict_sample
from src.laboratorio_datascience.train import save_model, train_model
from src.laboratorio_datascience.utils import print_banner

RAW_PATH = "data/raw/dataset.csv"
CLEAN_PATH = "data/processed/cleaned.csv"
MODEL_PATH = "models/classifier.joblib"


def main():
    print_banner("1. LOAD DATA")

    df = load_csv(RAW_PATH)
    print(df.head())

    print_banner("2. CLEAN DATA")

    cleaned_df = clean_data(df)
    save_clean_data(cleaned_df, CLEAN_PATH)

    print(cleaned_df.head())

    print_banner("3. POLARS INSPECTION")

    inspect_with_polars(CLEAN_PATH)

    print_banner("4. FEATURES")

    X, y = split_features_target(cleaned_df)

    print_banner("5. TRAIN MODEL")

    model = train_model(X, y)
    save_model(model, MODEL_PATH)

    print_banner("6. LOAD MODEL + INFERENCE")

    loaded_model = load_model(MODEL_PATH)

    # sample: [Pclass, Sex, Age, Fare]
    sample = [3, 0, 22, 7.25]

    result = predict_sample(loaded_model, sample)

    print(f"\nSample: {sample}")
    print(f"Prediction: {result}")


if __name__ == "__main__":
    main()
