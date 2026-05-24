from dataclasses import dataclass
from uuid import UUID


@dataclass
class OrderItem:
    id: UUID
    product_name: str
    quantity: int
    unit_price: float

    @property
    def subtotal(self) -> float:
        return self.quantity * self.unit_price
