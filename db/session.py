from sqlalchemy.orm import sessionmaker,Session
from db.engine import get_engine

_engine = get_engine()
SessionLocal = sessionmaker(bind=_engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()