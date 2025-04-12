#Логика работы с БД
from sqlalchemy.orm import Session
from datetime import datetime
from app.db.models import Transaction
from app.schemas.transaction import TransactionCreate, TransactionResponse

#Получение всех транзакций
def get_transactions(db: Session):
    return db.query(Transaction)


#Создание новой транзакции
def create_transacton(db: Session, transaction: TransactionCreate, user_id: int):
    db_transaction = Transaction(
        name=transaction.name,
        type=transaction.type,
        amount=transaction.amount,
        date=transaction.date or datetime.utcnow(),
        user_id=user_id,
        category = transaction.category,
        description = transaction.description)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

#Получение всех транзакций
def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Transaction).offset(skip).limit(limit).all()

def get_transactions_by_id(db: Session, transaction_id: int):
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()
