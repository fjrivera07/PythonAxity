from uuid import UUID

from sqlalchemy.orm import Session

from orders_service.domain.entities.user import User
from orders_service.domain.ports.user_repository import UserRepository
from orders_service.infrastructure.db.models.user_model import UserModel


class UserRepositorySQL(UserRepository):
    def __init__(self, db: Session) -> None:
        self.db = db

    def _to_domain(self, model: UserModel) -> User:
        return User(
            id=UUID(model.id),
            email=model.email,
            hashed_password=model.hashed_password,
            created_at=model.created_at,
        )

    def _to_model(self, entity: User) -> UserModel:
        return UserModel(
            id=str(entity.id),
            email=entity.email,
            hashed_password=entity.hashed_password,
            created_at=entity.created_at,
        )

    def save(self, user: User) -> User:
        model = self._to_model(user)

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return self._to_domain(model)

    def get_by_id(self, user_id: UUID) -> User | None:
        model = self.db.query(UserModel).filter(UserModel.id == str(user_id)).first()

        if not model:
            return None

        return self._to_domain(model)

    def get_by_email(self, email: str) -> User | None:
        model = self.db.query(UserModel).filter(UserModel.email == email).first()

        if not model:
            return None

        return self._to_domain(model)
