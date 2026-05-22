from laboratorio_solid.domain.entities import Order


class SqlOrderRepository:

    def __init__(self):
        self.storage: dict[int, Order] = {}

    def save(self, order: Order) -> None:
        print(f"INSERT INTO orders VALUES ({order.id})")
        self.storage[order.id] = order

    def get_by_id(self, order_id: int) -> Order | None:
        return self.storage.get(order_id)

    def list_all(self) -> list[Order]:
        return list(self.storage.values())
