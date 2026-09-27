from sqlalchemy.orm import Session
from fastapi import HTTPException
from schemas import AccountCreate
from repositories.user_repository import user_lookup
from repositories.account_repository import create_account


def account_registration(account: AccountCreate, db: Session):
    existing_user = user_lookup(account.user_id, db)
    if not existing_user:
        raise HTTPException(status_code=400, detail="User does not exist")

    new_account = create_account(account.user_id, account.balance, db)
    return new_account