from pydantic import BaseModel


class CreateOrderRequest(BaseModel):
    customer: str
    amount: float


class CreateOrderResponse(BaseModel):
    id: str
    customer: str
    amount: float
    status: str = "created"
