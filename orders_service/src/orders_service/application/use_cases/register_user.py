from datetime import datetime
from uuid import uuid4

from orders_service.domain.entities.user import User
from orders_service.domain.ports.auth_service import AuthService
from orders_service.domain.ports.user_repository import UserRepository


class RegisterUserUseCase:
    def __init__(
        self,
        user_repository: UserRepository,
        auth_service: AuthService,
    ) -> None:
        self.user_repository = user_repository
        self.auth_service = auth_service

    def execute(self, email: str, password: str) -> User:
        existing_user = self.user_repository.get_by_email(email)

        if existing_user:
            raise ValueError("User already exists")

        hashed_password = self.auth_service.hash_password(password)

        user = User(
            id=uuid4(),
            email=email,
            hashed_password=hashed_password,
            created_at=datetime.utcnow(),
        )

        return self.user_repository.save(user)
