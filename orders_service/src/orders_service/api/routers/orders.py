from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from orders_service.api.dependencies import get_db
from orders_service.api.schemas.orders import (
    CreateOrderRequest,
    OrderItemResponse,
    OrderResponse,
)
from orders_service.application.use_cases.create_order import CreateOrderUseCase
from orders_service.application.use_cases.get_order import GetOrderUseCase
from orders_service.application.use_cases.list_orders import ListOrdersUseCase
from orders_service.infrastructure.db.repositories.order_repository_sql import (
    OrderRepositorySQL,
)

router = APIRouter(prefix="/orders", tags=["Orders"])


def map_order_response(order) -> OrderResponse:
    return OrderResponse(
        id=order.id,
        user_id=order.user_id,
        items=[
            OrderItemResponse(
                id=item.id,
                product_name=item.product_name,
                quantity=item.quantity,
                unit_price=item.unit_price,
                subtotal=item.subtotal,
            )
            for item in order.items
        ],
        status=order.status,
        total=order.total,
    )


@router.post("/", response_model=OrderResponse)
def create_order(
    request: CreateOrderRequest,
    db: Session = Depends(get_db),
) -> OrderResponse:
    use_case = CreateOrderUseCase(order_repository=OrderRepositorySQL(db))

    order = use_case.execute(
        user_id=request.user_id,
        items_data=[item.model_dump() for item in request.items],
    )

    return map_order_response(order)


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: UUID,
    db: Session = Depends(get_db),
) -> OrderResponse:
    use_case = GetOrderUseCase(order_repository=OrderRepositorySQL(db))

    order = use_case.execute(order_id)

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    return map_order_response(order)


@router.get("/user/{user_id}", response_model=list[OrderResponse])
def list_orders(
    user_id: UUID,
    db: Session = Depends(get_db),
) -> list[OrderResponse]:
    use_case = ListOrdersUseCase(order_repository=OrderRepositorySQL(db))

    orders = use_case.execute(user_id)

    return [map_order_response(order) for order in orders]
