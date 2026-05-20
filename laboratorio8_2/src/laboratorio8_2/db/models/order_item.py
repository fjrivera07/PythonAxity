from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from laboratorio8_2.db.base import Base

if TYPE_CHECKING:
    from laboratorio8_2.db.models.order import Order


class OrderItem(Base):

    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True)

    product_name: Mapped[str] = mapped_column(String(100))

    quantity: Mapped[int]

    unit_price: Mapped[float]

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))

    order: Mapped["Order"] = relationship(back_populates="items")
