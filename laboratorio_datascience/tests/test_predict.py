from src.laboratorio_datascience.predict import predict_sample


class DummyModel:
    def predict(self, X):
        return [1]


def test_predict_sample():
    model = DummyModel()

    result = predict_sample(model, [3, 0, 22, 7.25])

    assert result == "SURVIVED"
