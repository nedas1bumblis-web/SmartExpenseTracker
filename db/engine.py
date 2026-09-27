from sqlalchemy import  create_engine
from sqlalchemy.engine import Engine
from db.config import get_db_settings

def get_engine()->Engine:
    settings = get_db_settings()
    url = (
        f"postgresql+psycopg2://{settings['pguser']}:{settings['pgpassword']}"
        f"@{settings['pghost']}:{settings['pgport']}/{settings['pgdb']}"
    )
    return create_engine(url,pool_recycle=50,echo=False)
