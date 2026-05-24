import uuid


def test_e2e_auth_users_orders(client):
    email = f"test_{uuid.uuid4()}@mail.com"

    # 1. Register
    register_response = client.post(
        "/auth/register", json={"email": email, "password": "1234"}
    )

    assert register_response.status_code in [200, 201]

    # 2. Login
    login_response = client.post(
        "/auth/login", json={"email": email, "password": "1234"}
    )

    assert login_response.status_code == 200

    login_data = login_response.json()

    assert "access_token" in login_data
    assert login_data["token_type"] == "bearer"

    # 3. Get users
    users_response = client.get("/users/")

    assert users_response.status_code == 200

    users = users_response.json()

    test_user = next((u for u in users if u["email"] == email), None)

    print(users_response.status_code)
    print(users_response.json())

    assert test_user is not None

    user_id = test_user["id"]

    # 4. Create order
    order_response = client.post(
        "/orders/",
        json={
            "user_id": user_id,
            "items": [{"product_name": "Laptop", "quantity": 1, "unit_price": 1000.0}],
        },
    )

    assert order_response.status_code in [200, 201]

    order_data = order_response.json()

    assert "id" in order_data
