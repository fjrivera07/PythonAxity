from uuid import UUID

from sqlalchemy.orm import Session

from orders_service.domain.entities.order import Order
from orders_service.domain.entities.order_item import OrderItem
from orders_service.domain.ports.order_repository import OrderRepository
from orders_service.infrastructure.db.models.order_item_model import OrderItemModel
from orders_service.infrastructure.db.models.order_model import OrderModel


class OrderRepositorySQL(OrderRepository):
    def __init__(self, db: Session) -> None:
        self.db = db

    def _to_domain(self, model: OrderModel) -> Order:
        items = [
            OrderItem(
                id=UUID(item.id),
                product_name=item.product_name,
                quantity=item.quantity,
                unit_price=item.unit_price,
            )
            for item in model.items
        ]

        return Order(
            id=UUID(model.id),
            user_id=UUID(model.user_id),
            items=items,
            status=model.status,
            created_at=model.created_at,
        )

    def _to_model(self, entity: Order) -> OrderModel:
        order_model = OrderModel(
            id=str(entity.id),
            user_id=str(entity.user_id),
            status=entity.status,
            created_at=entity.created_at,
        )

        order_model.items = [
            OrderItemModel(
                id=str(item.id),
                product_name=item.product_name,
                quantity=item.quantity,
                unit_price=item.unit_price,
            )
            for item in entity.items
        ]

        return order_model

    def save(self, order: Order) -> Order:
        model = self._to_model(order)

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return self._to_domain(model)

    def get_by_id(self, order_id: UUID) -> Order | None:
        model = self.db.query(OrderModel).filter(OrderModel.id == str(order_id)).first()

        if not model:
            return None

        return self._to_domain(model)

    def list_by_user(self, user_id: UUID) -> list[Order]:
        models = (
            self.db.query(OrderModel).filter(OrderModel.user_id == str(user_id)).all()
        )

        return [self._to_domain(model) for model in models]

    def delete(self, order_id: UUID) -> None:
        model = self.db.query(OrderModel).filter(OrderModel.id == str(order_id)).first()

        if model:
            self.db.delete(model)
            self.db.commit()
