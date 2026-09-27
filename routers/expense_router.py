from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from schemas import ExpenseFilter
from services.expense_service import log_expenses

router = APIRouter()


@router.post('/Categories')
async def log_expenses_route(raw_data: ExpenseFilter, db: Session = Depends(get_db)):
    final_calculation = log_expenses(raw_data, db)
    return {"final_calculation": final_calculation}