from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DB_URL = "postgresql+psycopg2://postgres:voidpostgres@localhost:5432/mohirdev_db"


engine = create_engine(DB_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class BaseT(DeclarativeBase):
    pass