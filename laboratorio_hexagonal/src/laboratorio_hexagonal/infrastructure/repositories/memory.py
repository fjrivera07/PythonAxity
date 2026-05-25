from typing import List

from ...domain.entities import Order
from ...domain.ports import OrderRepository


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self._orders: List[Order] = []

    def save(self, order: Order) -> None:
        self._orders.append(order)

    def list_all(self) -> List[Order]:
        return self._orders
