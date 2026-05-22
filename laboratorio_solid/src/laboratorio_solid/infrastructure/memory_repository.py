from laboratorio_solid.domain.entities import Order


class MemoryOrderRepository:

    def __init__(self):
        self.orders: dict[int, Order] = {}

    def save(self, order: Order) -> None:
        self.orders[order.id] = order

    def get_by_id(self, order_id: int) -> Order | None:
        return self.orders.get(order_id)

    def list_all(self) -> list[Order]:
        return list(self.orders.values())
