from collections.abc import Generator

from sqlalchemy.orm import Session

from orders_service.infrastructure.db.repositories.order_repository_sql import (
    OrderRepositorySQL,
)
from orders_service.infrastructure.db.repositories.user_repository_sql import (
    UserRepositorySQL,
)
from orders_service.infrastructure.db.session import SessionLocal
from orders_service.infrastructure.security.auth_service_impl import AuthServiceImpl


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_repository(db: Session) -> UserRepositorySQL:
    return UserRepositorySQL(db)


def get_order_repository(db: Session) -> OrderRepositorySQL:
    return OrderRepositorySQL(db)


def get_auth_service() -> AuthServiceImpl:
    return AuthServiceImpl()
