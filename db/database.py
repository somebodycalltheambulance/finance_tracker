from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from core.config import settings

DATABASE_URL = "postgresql+psycopg2://username:password@localhost:5432/finance_app"

#Создаем движок на основе адреса из .env
engine = create_engine(settings.database_url)

#Создаем сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Базовый класс для моделей
class Base(DeclarativeBase):
    pass