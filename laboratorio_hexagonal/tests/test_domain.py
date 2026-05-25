import pytest

from laboratorio_hexagonal.domain.entities import Order


def test_create_order_valid():
    order = Order.create("Juan", 100)

    assert order.customer == "Juan"
    assert order.amount == 100
    assert order.id is not None


def test_create_order_empty_customer():
    with pytest.raises(ValueError):
        Order.create("", 100)


def test_create_order_invalid_amount():
    with pytest.raises(ValueError):
        Order.create("Juan", 0)
