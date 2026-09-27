from sqlalchemy import VARCHAR,TIMESTAMP, DECIMAL,ForeignKey,String,func
from sqlalchemy.orm import relationship,DeclarativeBase,Mapped,mapped_column
from datetime import datetime
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_info"
    id : Mapped[int] = mapped_column(primary_key=True)
    username : Mapped[str] = mapped_column(VARCHAR(80),unique=True)
    password : Mapped[str] = mapped_column(VARCHAR(255))
    email : Mapped[str]= mapped_column(String(120),unique=True)
    created_at :Mapped[datetime] = mapped_column(TIMESTAMP,server_default=func.now())

    accounts: Mapped[list["Account"]] = relationship(back_populates="user")
    ai_history:Mapped[list["AI"]] = relationship(back_populates="user")

class Account(Base):
    __tablename__ = "bank_account"
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey("user_info.id",ondelete="CASCADE"))
    balance : Mapped[float] = mapped_column(DECIMAL(9,2))

    user:Mapped["User"] = relationship(back_populates="accounts")
    expenses: Mapped[list["Expense"]] = relationship(back_populates="account")

class AI(Base):
    __tablename__ = "ai_history"
    id :Mapped[int] = mapped_column(primary_key=True)
    user_id :Mapped[int] = mapped_column(ForeignKey("user_info.id",ondelete="CASCADE"))
    user_prompt: Mapped[str] = mapped_column(VARCHAR(250))
    ai_response : Mapped[str] = mapped_column(String)
    created_at : Mapped[datetime] = mapped_column(TIMESTAMP,server_default=func.now())

    user:Mapped["User"] = relationship(back_populates="ai_history")

class Expense(Base):
    __tablename__ = "user_expenses"
    id : Mapped[int] = mapped_column(primary_key=True)
    account_id : Mapped[int] = mapped_column(ForeignKey("bank_account.id",ondelete="CASCADE"))
    amount:Mapped[float] = mapped_column(DECIMAL(9,2))
    category : Mapped[str] = mapped_column(VARCHAR(250))
    transaction_date : Mapped[datetime] = mapped_column(TIMESTAMP,server_default=func.now())

    account:Mapped["Account"] = relationship(back_populates="expenses")