import pytest

from laboratorio_fastapi.db.models.order import Order


@pytest.mark.parametrize(
    "quantity, price, expected",
    [
        (1, 10, 10),
        (2, 50, 100),
        (3, 20, 60),
    ],
)
def test_order_total(quantity, price, expected):

    order = Order(quantity=quantity, price=price)

    assert order.total == expected
