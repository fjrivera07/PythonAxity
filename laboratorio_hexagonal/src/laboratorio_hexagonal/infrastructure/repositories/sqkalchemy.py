from sqlalchemy import Column, Float, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from ...domain.entities import Order
from ...domain.ports import OrderRepository

Base = declarative_base()


class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(String, primary_key=True)
    customer = Column(String, nullable=False)
    amount = Column(Float, nullable=False)


class SqlAlchemyOrderRepository(OrderRepository):
    def __init__(self, db_url: str = "sqlite:///orders.db"):
        self.engine = create_engine(db_url, echo=False)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save(self, order: Order) -> None:
        session = self.Session()

        db_order = OrderModel(id=order.id, customer=order.customer, amount=order.amount)

        session.add(db_order)
        session.commit()
        session.close()
