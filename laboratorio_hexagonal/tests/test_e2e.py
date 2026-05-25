from fastapi.testclient import TestClient

from laboratorio_hexagonal.infrastructure.api.main import app

client = TestClient(app)


def test_create_order_e2e():
    response = client.post("/orders", json={"customer": "Juan", "amount": 300})

    assert response.status_code == 200

    data = response.json()

    assert data["customer"] == "Juan"
    assert data["amount"] == 300
    assert data["status"] == "created"
    assert "id" in data
