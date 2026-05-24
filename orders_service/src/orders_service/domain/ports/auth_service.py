from typing import Protocol

from orders_service.domain.entities.user import User


class AuthService(Protocol):
    def hash_password(self, password: str) -> str: ...

    def verify_password(self, plain_password: str, hashed_password: str) -> bool: ...

    def create_access_token(self, user: User) -> str: ...
