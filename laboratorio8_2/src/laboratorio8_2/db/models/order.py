from __future__ import annotations

from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from laboratorio8_2.db.base import Base

if TYPE_CHECKING:
    from laboratorio8_2.db.models.order_item import OrderItem
    from laboratorio8_2.db.models.user import User


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)

    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped[User] = relationship(back_populates="orders")

    items: Mapped[list[OrderItem]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan",
    )
