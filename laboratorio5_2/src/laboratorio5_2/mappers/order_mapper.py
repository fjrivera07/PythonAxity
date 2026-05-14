from laboratorio5_2.domain.order import Order
from laboratorio5_2.models.order_models import OrderIn, OrderOut


def to_entity(order_in: OrderIn) -> Order:
    return Order(
        quantity=order_in.quantity,
        unit_price=order_in.unit_price,
    )


def to_output(order: Order) -> OrderOut:
    return OrderOut(
        quantity=order.quantity,
        unit_price=order.unit_price,
        total=order.total,
    )
