from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.session import get_db
from schemas import UserRegistration, UserLogin,Token
from services.auth_service import user_registration,user_login,authenticate_user,create_access_token,user_dependency
from datetime import timedelta
from repositories.user_repository import user_lookup

router = APIRouter()

@router.post('/Registration')
async def register_user_route(user: UserRegistration, db: Session = Depends(get_db)):
    new_user = user_registration(user, db)
    return {"user_id": new_user.id, "username": new_user.username}


@router.post('/Login')
async def login_route(user: UserLogin, db: Session = Depends(get_db)):
    existing_user = user_login(user, db)
    return {"message": f"User logged in {existing_user.username}"}

@router.post('/Token', response_model=Token)
async def login_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password,db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user")
    token = create_access_token(user.username,user.id,timedelta(minutes=60))
    return {"access_token":token,"token_type":"bearer"}
@router.get("/",status_code=status.HTTP_200_OK)
async def get_current_user(user:user_dependency,db:Session = Depends(get_db)):
    user_info = user_lookup(user["user_id"],db)
    if user_info is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Authentication failed")
    return {"User":user_info}


