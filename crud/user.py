from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from typing import Optional
from security.user import hash_password

def create_user(db: Session, user_in: UserCreate):
    encrypted_password = hash_password(user_in.password)
    db_user = User(username=user_in.username,email=user_in.email, hashed_password=encrypted_password)
    existing_user = db.query(User).filter(User.username == user_in.username).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    existing_email = db.query(User).filter(User.email == user_in.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()
