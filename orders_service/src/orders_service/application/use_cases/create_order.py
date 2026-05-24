from datetime import datetime
from uuid import uuid4

from orders_service.domain.entities.order import Order
from orders_service.domain.entities.order_item import OrderItem
from orders_service.domain.ports.order_repository import OrderRepository


class CreateOrderUseCase:
    def __init__(self, order_repository: OrderRepository) -> None:
        self.order_repository = order_repository

    def execute(
        self,
        user_id,
        items_data: list[dict],
    ) -> Order:
        items = [
            OrderItem(
                id=uuid4(),
                product_name=item["product_name"],
                quantity=item["quantity"],
                unit_price=item["unit_price"],
            )
            for item in items_data
        ]

        order = Order(
            id=uuid4(),
            user_id=user_id,
            items=items,
            status="PENDING",
            created_at=datetime.utcnow(),
        )

        return self.order_repository.save(order)
