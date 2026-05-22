from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from laboratorio_fastapi.db.base import Base

if TYPE_CHECKING:
    from laboratorio_fastapi.db.models.user import User


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="orders")

    quantity: Mapped[int] = mapped_column(Integer)

    price: Mapped[int] = mapped_column(Integer)

    @property
    def total(self) -> int:
        return self.quantity * self.price
