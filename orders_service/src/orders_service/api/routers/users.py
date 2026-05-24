from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from orders_service.api.dependencies import get_db
from orders_service.api.schemas.user import UserResponse
from orders_service.infrastructure.db.models.user_model import UserModel

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    return users
