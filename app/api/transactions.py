from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.crud import transaction
from app.schemas.transaction import Transaction, TransactionCreate

router = APIRouter()

#Получение сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Получение всех транзакций
@router.get("/transactions", response_model=list[Transaction])
def get_transactions(db: Session = Depends(get_db)):
    return transaction.get_transactions(db)

#Добавление новой транзакции
@router.post("/transactions", response_model=Transaction)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return transaction.create_transaction(db, transaction)
