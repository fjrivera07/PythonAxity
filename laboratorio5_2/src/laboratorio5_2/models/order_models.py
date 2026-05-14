from pydantic import BaseModel


class OrderIn(BaseModel):
    quantity: int
    unit_price: float


class OrderOut(BaseModel):
    quantity: int
    unit_price: float
    total: float
