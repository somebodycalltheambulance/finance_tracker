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
from api.dependencies import get_current_user
from models import user


router = APIRouter()

@router.post("/register", response_model=Token)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    #Проверяем что наш емейл не занят
    db_user = get_user_by_email(db, user_in.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email уже зарегистрирован")
    
    # Проверяем, что пользователь с таким username не существует
    existing_username = db.query(User).filter(User.username == user_in.username).first()
    if existing_username:
        raise HTTPException(status_code=400, detail="Username уже занят")

    # Хешируем пароль
    hashed_password = hash_password(user_in.password)

    # Создаём пользователя
    new_user = User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Генерим токен
    token = create_access_token(data={"sub": str(new_user.id)})

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.post("/login", response_model=Token)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user:
        print("❌ Пользователь не найден")
    else:
        print(f"🔐 Из БД: {user.username}, {user.hashed_password}")
        print("✅ Проверка пароля:", verify_password(form_data.password, user.hashed_password))


    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me", tags=["users"])
def read_current_user(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "username": current_user.username
    }
