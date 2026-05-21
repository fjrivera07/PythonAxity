from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from laboratorio_fastapi.db.models.order import Order
from laboratorio_fastapi.dependencies.db import get_db
from laboratorio_fastapi.schemas.order import OrderCreate, OrderResponse

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=OrderResponse)
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):

    order = Order(user_id=order_data.user_id)

    db.add(order)
    db.commit()
    db.refresh(order)

    return order


@router.get("/", response_model=list[OrderResponse])
def get_orders(db: Session = Depends(get_db)):

    return db.query(Order).all()


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):

    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order
