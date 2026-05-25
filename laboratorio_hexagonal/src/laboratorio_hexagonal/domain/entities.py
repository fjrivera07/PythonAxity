from dataclasses import dataclass
from uuid import uuid4


@dataclass
class Order:
    id: str
    customer: str
    amount: float

    @classmethod
    def create(cls, customer: str, amount: float) -> "Order":
        if not customer.strip():
            raise ValueError("Customer name cannot be empty")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        return cls(id=str(uuid4()), customer=customer, amount=amount)
