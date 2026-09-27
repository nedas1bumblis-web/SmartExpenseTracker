from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from schemas import AccountCreate
from services.account_service import account_registration

router = APIRouter()

@router.post('/Accounts')
async def create_account_route(account: AccountCreate, db: Session = Depends(get_db)):
    new_account = account_registration(account, db)
    return {"account_id": new_account.id}