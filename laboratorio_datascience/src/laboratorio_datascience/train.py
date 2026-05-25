import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split


def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print("\nAccuracy:", accuracy)
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    return model


def save_model(model, path: str):
    joblib.dump(model, path)
    print(f"\nModelo guardado en: {path}")
