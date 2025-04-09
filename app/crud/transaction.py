#Логика работы с БД
from sqlalchemy.orm import Session
from app.db.models import Transaction
from app.schemas.transaction import TransactionCreate

#Получение всех транзакций
def get_transactions(db: Session):
    return db.query(Transaction)


#Создание новой транзакции
def create_transacton(db: Session, transaction: TransactionCreate):
    db_transaction = Transaction(name=transaction.name, amount=transaction.amount, date=transaction.date, category = transaction.category, description = transaction.description)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction