from uuid import UUID

from orders_service.domain.entities.order import Order
from orders_service.domain.ports.order_repository import OrderRepository


class ListOrdersUseCase:
    def __init__(self, order_repository: OrderRepository) -> None:
        self.order_repository = order_repository

    def execute(self, user_id: UUID) -> list[Order]:
        return self.order_repository.list_by_user(user_id)
