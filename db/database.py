from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from core.config import settings

#Создаем движок на основе адреса из .env
engine = create_engine(settings.database_url, connect_args={"check_same_thread": False})


#Создаем сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Базовый класс для моделей
class Base(DeclarativeBase):
    pass