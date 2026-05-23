from dataclasses import dataclass


@dataclass
class Order:
    id: int
    customer_type: str
    product_code: str
