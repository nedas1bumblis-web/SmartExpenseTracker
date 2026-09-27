from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas import UserRegistration, UserLogin
from services.auth_service import user_registration,user_login


router = APIRouter()

@router.post('/Registration')
async def register_user_route(user: UserRegistration, db: Session = Depends(get_db)):
    new_user = user_registration(user, db)
    return {"user_id": new_user.id, "username": new_user.username}


@router.post('/Login')
async def login_route(user: UserLogin, db: Session = Depends(get_db)):
    existing_user = user_login(user, db)
    return {"message": f"User logged in {existing_user.username}"}

