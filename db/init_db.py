from db.engine import get_engine
from db.models import Base

def create_db_and_tables():
    engine = get_engine()
    Base.metadata.create_all(engine)
    print("Tables created")

if __name__ == "__main__":
    create_db_and_tables()