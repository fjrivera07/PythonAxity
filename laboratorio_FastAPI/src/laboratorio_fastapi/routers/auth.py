from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from laboratorio_fastapi.auth.security import create_access_token, verify_password
from laboratorio_fastapi.db.models.user import User
from laboratorio_fastapi.dependencies.db import get_db
from laboratorio_fastapi.schemas.auth import LoginRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=TokenResponse)
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == login_data.email).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(login_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    print("plain:", login_data.password)
    print("hash:", user.password_hash)
    print("verify:", verify_password(login_data.password, user.password_hash))
    token = create_access_token(data={"sub": user.email})

    return {"access_token": token, "token_type": "bearer"}
