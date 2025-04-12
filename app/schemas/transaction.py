from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TransactionBase(BaseModel):
    name:str
    amount: int
    date: str
    category: str
    description: str

class TransactionCreate(BaseModel):
    amount: float
    type: str
    category: str
    description: Optional[str] = None
    date: Optional[datetime] = None

    class Config:
        orm_mode = True


class Transaction(BaseModel):
    id: int

    class Config:
        orm_model = True



class TransactionResponse(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    description: Optional[str] = None
    date: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True     