from typing import Protocol
from uuid import UUID

from orders_service.domain.entities.order import Order


class OrderRepository(Protocol):
    def save(self, order: Order) -> Order: ...

    def get_by_id(self, order_id: UUID) -> Order | None: ...

    def list_by_user(self, user_id: UUID) -> list[Order]: ...

    def delete(self, order_id: UUID) -> None: ...
