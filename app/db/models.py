from sqlalchemy import Column, Integer, Float, String, DateTime, func
from app.db.database import Base
from datetime import datetime, UTC


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(UTC))