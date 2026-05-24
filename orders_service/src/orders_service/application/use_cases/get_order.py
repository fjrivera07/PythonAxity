from uuid import UUID

from orders_service.domain.entities.order import Order
from orders_service.domain.ports.order_repository import OrderRepository


class GetOrderUseCase:
    def __init__(self, order_repository: OrderRepository) -> None:
        self.order_repository = order_repository

    def execute(self, order_id: UUID) -> Order | None:
        return self.order_repository.get_by_id(order_id)
