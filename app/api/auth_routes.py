from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserCreate
from app.services.auth_service import register_user
from app.core.dependencies import get_db

from app.schemas.auth_schema import UserLogin
from app.services.auth_service import login_user

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    user = register_user(
        db=db,
        user_data=user_data
    )

    return {
        "id": user.id,
        "email": user.email
    }

@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):

    result = login_user(db, user_data)

    if not result:
        return {"error": "Invalid credentials"}

    return result