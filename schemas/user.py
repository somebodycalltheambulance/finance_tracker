from pydantic import BaseModel, EmailStr
from typing import Optional


# 👤 Что принимает API при создании пользователя
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    username: str

# для ответа наружу (без пароля)
class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True 
