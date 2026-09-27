from sqlalchemy.orm import Session
from db.models import Expense
from schemas import AIQuery


def create_expenses(receipts_list: list[dict], db: Session):
    new_expenses = []
    for receipt in receipts_list:
        new_expense = Expense(
            account_id=receipt["account_id"],
            category=receipt["category"],
            amount=receipt["amount"]
        )
        db.add(new_expense)
        new_expenses.append(new_expense)
    db.commit()
    return new_expenses

def expense_query(account_id:int,db:Session):
    user_expenses = db.query(Expense).filter(Expense.account_id == account_id ).all()
    return user_expenses