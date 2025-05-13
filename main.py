from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models.user import  User
from schemas.user import UserCreate
from security.user import hash_password
from db.database import engine, get_db, Base
from api import auth

app = FastAPI()

# Создаем таблицы
Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth")