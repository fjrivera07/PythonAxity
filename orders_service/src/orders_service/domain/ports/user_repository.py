from typing import Protocol
from uuid import UUID

from orders_service.domain.entities.user import User


class UserRepository(Protocol):
    def save(self, user: User) -> User: ...

    def get_by_id(self, user_id: UUID) -> User | None: ...

    def get_by_email(self, email: str) -> User | None: ...
