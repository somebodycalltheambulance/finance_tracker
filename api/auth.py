from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserOut
from crud.user import get_user_by_email, create_user
from db.database import get_db
from security.user import hash_password  # вот это нужно
# не забудь импортировать UserOut с from_attributes=True если на Pydantic 2

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user_in.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email уже зарегистрирован")

    # хешируем пароль
    user_in.password = hash_password(user_in.password)

    user = create_user(db, user_in)
    return user
