from datetime import datetime

from pydantic import BaseModel, ConfigDict, computed_field


class OrderCreate(BaseModel):
    user_id: int
    quantity: int
    price: int


class OrderResponse(BaseModel):
    id: int
    user_id: int
    created_at: datetime
    quantity: int
    price: int

    model_config = ConfigDict(from_attributes=True)

    @computed_field
    @property
    def total(self) -> int:
        return self.quantity * self.price
