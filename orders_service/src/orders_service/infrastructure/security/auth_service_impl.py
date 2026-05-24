from orders_service.domain.entities.user import User
from orders_service.domain.ports.auth_service import AuthService
from orders_service.infrastructure.security.jwt_service import create_access_token
from orders_service.infrastructure.security.password_hasher import (
    hash_password,
    verify_password,
)


class AuthServiceImpl(AuthService):
    def hash_password(self, password: str) -> str:
        return hash_password(password)

    def verify_password(
        self,
        plain_password: str,
        hashed_password: str,
    ) -> bool:
        return verify_password(
            plain_password,
            hashed_password,
        )

    def create_access_token(self, user: User) -> str:
        return create_access_token(str(user.id))
