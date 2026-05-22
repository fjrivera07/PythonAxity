from fastapi.testclient import TestClient

from laboratorio_fastapi.main import app

client = TestClient(app)


def test_create_order_should_return_total():

    payload = {"user_id": 1, "quantity": 2, "price": 50}

    response = client.post("/orders", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["quantity"] == 2
    assert data["price"] == 50
    assert data["total"] == 100
