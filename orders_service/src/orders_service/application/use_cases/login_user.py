from orders_service.domain.ports.auth_service import AuthService
from orders_service.domain.ports.user_repository import UserRepository


class LoginUserUseCase:
    def __init__(
        self,
        user_repository: UserRepository,
        auth_service: AuthService,
    ):
        self.user_repository = user_repository
        self.auth_service = auth_service

    def execute(self, email: str, password: str) -> str:
        user = self.user_repository.get_by_email(email)

        if not user:
            raise ValueError("Invalid credentials")

        if not self.auth_service.verify_password(
            password,
            user.hashed_password,
        ):
            raise ValueError("Invalid credentials")

        return self.auth_service.create_access_token(user)
