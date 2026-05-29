from sqlalchemy.orm import Session

from app.schemas.user_schema import UserCreate
from app.core.security import hash_password
from app.repositories.user_repository import create_user

from app.core.security import verify_password
from app.core.jwt import create_access_token
from app.repositories.user_repository import get_user_by_email

def register_user(
    db: Session,
    user_data: UserCreate
):
    hashed_password = hash_password(
        user_data.password
    )

    user = create_user(
        db=db,
        email=user_data.email,
        hashed_password=hashed_password
    )

    return user

def login_user(db, user_data):
    user = get_user_by_email(db, user_data.email)

    if not user:
        return None

    if not verify_password(user_data.password, user.hashed_password):
        return None

    token = create_access_token(
        data={"sub": str(user.id)}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }