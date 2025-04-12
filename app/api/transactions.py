from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.crud import transaction
from app.crud.transaction import create_transacton, get_transactions, get_transactions_by_id
from app.schemas.transaction import Transaction, TransactionCreate, TransactionResponse


router = APIRouter()

#Получение сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Получение всех транзакций
@router.get("/transactions", response_model=list[TransactionResponse])
def get_transactions_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transactions = get_transactions(db=db, skip=skip, limit=limit)
    return transactions

#Добавление новой транзакции
@router.post("/transactions", response_model=TransactionResponse)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db), user_id: int = 1):
    db_transacton = create_transaction(db=db, transaction=transaction, user_id=user_id)
    return db_transacton

#Полуение транзакции по ID
@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction_by_id_route(transaction_id: int, db: Session = Depends(get_db)):
    db_transacton = get_transactions_by_id(db=db,transaction_id=transaction_id)
    if db_transacton is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transacton