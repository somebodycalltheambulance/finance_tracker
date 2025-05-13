from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserOut
from crud.user import get_user_by_email, create_user
from db.database import get_db
from security.user import hash_password, verify_password
from schemas.token import Token
from models.user import User
from security.auth import create_access_token


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


@router.post("/login", response_model=Token)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
