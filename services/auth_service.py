from schemas import UserRegistration,UserLogin
from sqlalchemy.orm import Session
from security import get_hashed_password,verify_hashed_password
from repositories.user_repository import user_check
from fastapi import HTTPException
from db.models import User

def user_registration(user:UserRegistration,db:Session):
    existing_user = user_check(user.username, db)
    if existing_user:
        raise HTTPException(status_code=400, detail="User with that username already exists")
    hashed_password = get_hashed_password(user.password)
    new_user = User(username=user.username, password=hashed_password, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def user_login(user:UserLogin, db:Session):
    existing_user = user_check(user.username, db)
    if not existing_user:
        raise HTTPException(status_code=400, detail="User does not exist")
    if not verify_hashed_password(user.password, existing_user.password):
        raise HTTPException(status_code=401, detail="Incorrect Password or Password")
    return existing_user