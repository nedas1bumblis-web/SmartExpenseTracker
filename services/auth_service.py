from typing import Annotated
from schemas import UserRegistration,UserLogin
from sqlalchemy.orm import Session
from security import get_hashed_password,verify_hashed_password
from repositories.user_repository import user_check
from fastapi import HTTPException
from db.models import User
import jwt
from datetime import datetime,timedelta
from fastapi import status,Depends
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
import os
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

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

def authenticate_user(username:str, password:str,db:Session):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_hashed_password(password, user.password):
        return False
    return user

def create_access_token(username:str,user_id:int,expires_delta:timedelta):
    encode = {'sub':username,'id':user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="Token")

async def get_access_token(token:Annotated[str,Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        username:str=payload.get('sub')
        user_id:int=payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate user")
        return {"username":username,"user_id":user_id}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401,detail="Could not validate user")

user_dependency = Annotated[dict,Depends(get_access_token)]