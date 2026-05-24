from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from orders_service.domain.entities.order_item import OrderItem


@dataclass
class Order:
    id: UUID
    user_id: UUID
    items: list[OrderItem] = field(default_factory=list)
    status: str = "PENDING"
    created_at: datetime = field(default_factory=datetime.utcnow)

    @property
    def total(self) -> float:
        return sum(item.subtotal for item in self.items)
