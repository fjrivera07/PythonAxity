from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from orders_service.api.dependencies import get_auth_service, get_db
from orders_service.api.schemas.auth import (
    TokenResponse,
    UserLoginRequest,
    UserRegisterRequest,
)
from orders_service.application.use_cases.login_user import LoginUserUseCase
from orders_service.application.use_cases.register_user import RegisterUserUseCase
from orders_service.infrastructure.db.repositories.user_repository_sql import (
    UserRepositorySQL,
)
from orders_service.infrastructure.security.auth_service_impl import AuthServiceImpl

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register_user(
    request: UserRegisterRequest,
    db: Session = Depends(get_db),
    auth_service: AuthServiceImpl = Depends(get_auth_service),
) -> dict[str, str]:
    use_case = RegisterUserUseCase(
        user_repository=UserRepositorySQL(db),
        auth_service=auth_service,
    )

    try:
        use_case.execute(
            email=request.email,
            password=request.password,
        )
        return {"message": "User created successfully"}

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        ) from e


@router.post("/login", response_model=TokenResponse)
def login_user(
    request: UserLoginRequest,
    db: Session = Depends(get_db),
    auth_service: AuthServiceImpl = Depends(get_auth_service),
) -> TokenResponse:
    use_case = LoginUserUseCase(
        user_repository=UserRepositorySQL(db),
        auth_service=auth_service,
    )

    try:
        token = use_case.execute(
            email=request.email,
            password=request.password,
        )

        return TokenResponse(access_token=token)

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        ) from e
