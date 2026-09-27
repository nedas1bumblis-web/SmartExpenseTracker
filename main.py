from db.init_db import create_db_and_tables
from fastapi import FastAPI
import httpx
from contextlib import asynccontextmanager
from routers.auth_router import router as auth_router
from routers.account_router import router as account_router
from routers.expense_router import router as expense_router
from routers.ai_router import router as ai_router
@asynccontextmanager
async def lifespan(current_app :FastAPI):
    create_db_and_tables()
    current_app.state.client = httpx.AsyncClient()
    yield
    await current_app.state.client.aclose()
app = FastAPI(lifespan=lifespan)
app.include_router(auth_router)
app.include_router(account_router)
app.include_router(expense_router)

app.include_router(ai_router)
