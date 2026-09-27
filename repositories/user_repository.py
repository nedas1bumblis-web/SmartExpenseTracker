from sqlalchemy.orm import Session
from db.models import User

def user_check(username:str,db:Session):
    existing_user = db.query(User).filter(User.username == username).first()
    return existing_user

def user_lookup(user_id:int,db:Session):
    existing_user = db.query(User).filter(User.id == user_id).first()
    return existing_user