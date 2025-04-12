from sqlalchemy import Column, Integer, Float, String, DateTime,  ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime, UTC


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text, nullable=False)
    type = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    date = Column(DateTime, default=lambda: datetime.now(UTC))
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    updated_at = Column(DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))

    user_id = Column(Integer,ForeignKey("users_id"), nullable=False)

    #user = relationship("User", back_populates="transactions")
