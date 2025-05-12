from pydantic import BaseModel, EmailStr

# 👤 Что принимает API при создании пользователя
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# 👤 Что возвращает API
class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True  # это для работы с ORM-моделями
