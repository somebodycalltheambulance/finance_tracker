from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models.user import  User
from schemas.user import UserCreate
from security.user import hash_password
from db.database import engine, get_db, Base

app = FastAPI()

# Создаем таблицы
Base.metadata.create_all(bind=engine)

@app.post("/register/")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Проверяем, существует ли пользователь
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # Хешируем пароль и создаем пользователя
    hashed_password = hash_password(user.password)
    new_user = User(email=user.email, username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"username": new_user.username, "id": new_user.id}