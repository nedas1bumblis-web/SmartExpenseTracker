import decimal

from pydantic import BaseModel,Field,EmailStr
from datetime import datetime

class UserRegistration(BaseModel):
    username: str = Field(max_length=10)
    password: str = Field(min_length=10)
    email: EmailStr

class UserLogin(BaseModel):
    username: str
    password: str

class AIQuery(BaseModel):
    account_id:int
    user_id:int
    budget:decimal.Decimal | None = Field(default=None,gt=0)
    user_prompt: str= Field(max_length=250)

class ExpenseCreate(BaseModel):
    account_id:int
    category:str
    amount: decimal.Decimal= Field(gt=0)

class ExpenseResponse(BaseModel):
    id:int
    amount:decimal.Decimal
    categories:str
    transaction_date:datetime

class ExpenseFilter(BaseModel):
    receipts:list[ExpenseCreate] = Field(min_length=1)

class AccountCreate(BaseModel):
    user_id:int
    balance:decimal.Decimal