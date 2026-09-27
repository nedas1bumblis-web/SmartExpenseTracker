from decimal import Decimal
from sqlalchemy.orm import Session
from db.models import Account


def create_account(user_id: int, balance: Decimal, db: Session):
    new_account = Account(user_id=user_id, balance=balance)
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account