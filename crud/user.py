from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from typing import Optional
from security.user import hash_password

def create_user(db: Session, user_in: UserCreate):
    encrypted_password = hash_password(user_in.password)
    db_user = User(username=user_in.username,email=user_in.email, password=encrypted_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()
