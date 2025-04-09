from pydantic import BaseModel

class TransactionBase(BaseModel):
    name:str
    amount: int
    date: str
    category: str
    description: str

class TransactionCreate(BaseModel):
    pass

class Transaction(BaseModel):
    id: int

    class Config:
        orm_model = True
        