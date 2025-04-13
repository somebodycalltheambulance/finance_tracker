from sqlalchemy.orm import Session
from app.db.models import User
from app.schemas.user import UserCreate
from utils.hashing import get_password_hash, verify_password

def create_user(db:Session, user: UserCreate):
    hashed_pw = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password. user.hashed_password):
        return None
    return User

def get_user_by_id(db:Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()