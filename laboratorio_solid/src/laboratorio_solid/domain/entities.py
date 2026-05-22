from dataclasses import dataclass


@dataclass
class Order:
    id: int
    customer_name: str
    total: float
