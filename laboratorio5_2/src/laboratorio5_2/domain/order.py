from dataclasses import dataclass


@dataclass
class Order:
    quantity: int
    unit_price: float

    @property
    def total(self):
        return self.quantity * self.unit_price
