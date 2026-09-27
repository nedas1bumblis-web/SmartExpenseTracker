from sqlalchemy.orm import Session
from schemas import ExpenseFilter
from calculations import expense_calculator
from repositories.expense_repository import create_expenses


def log_expenses(raw_data: ExpenseFilter, db: Session):
    receipts_list = []
    for items in raw_data.receipts:
        receipts_dict = items.model_dump()
        receipts_list.append(receipts_dict)

    create_expenses(receipts_list, db)
    final_calculation = expense_calculator(raw_data=receipts_list)
    return final_calculation