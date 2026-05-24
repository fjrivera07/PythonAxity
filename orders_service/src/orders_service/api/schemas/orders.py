from uuid import UUID

from pydantic import BaseModel


class OrderItemRequest(BaseModel):
    product_name: str
    quantity: int
    unit_price: float


class CreateOrderRequest(BaseModel):
    user_id: UUID
    items: list[OrderItemRequest]


class OrderItemResponse(BaseModel):
    id: UUID
    product_name: str
    quantity: int
    unit_price: float
    subtotal: float


class OrderResponse(BaseModel):
    id: UUID
    user_id: UUID
    items: list[OrderItemResponse]
    status: str
    total: float
