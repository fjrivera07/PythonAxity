from laboratorio_solid.domain.entities import Order
from laboratorio_solid.domain.ports import OrderRepository


class OrderService:

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def create_order(self, order_id: int, customer_name: str, total: float) -> Order:

        order = Order(id=order_id, customer_name=customer_name, total=total)

        self.repository.save(order)

        return order

    def get_order(self, order_id: int) -> Order | None:
        return self.repository.get_by_id(order_id)

    def list_orders(self) -> list[Order]:
        return self.repository.list_all()
