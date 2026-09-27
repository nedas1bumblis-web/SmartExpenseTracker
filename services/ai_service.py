from ai_logic import formatting_expenses, build_budget_text, build_prompt, get_ai_response
from schemas import AIQuery
from sqlalchemy.orm import Session
from repositories.expense_repository import expense_query
from repositories.ai_repository import create_prompt

async def ai_creation(ai:AIQuery,client,db:Session):
    user_expenses = expense_query(ai.account_id,db)
    formatted_expenses = formatting_expenses(user_expenses)
    budget_text = build_budget_text(budget=ai.budget)
    full_prompt = build_prompt(
        formatted_expenses=formatted_expenses,
        budget_text=budget_text,
        user_prompt=ai.user_prompt
    )
    ai_response = await get_ai_response(client,full_prompt)
    create_prompt(ai.user_id,ai.user_prompt,ai_response,db)
    return ai_response