"""
ORMs: SQLAlchemy, Django ORM, Tortoise ORM, SQLModel, Piccolo
Frameworks: Flask, Django, FastAPI, Pyramid, Starlette, Tornado


Django ORM: Django
SQLAlchemy: *


psycopg2_binary - driver

Drivers (postgres): psycopg2_binary (sinxron), asyncpg (asinxron), aiopg
Drivers (mysql): mysql-connector
Drivers (mongodb): motor, mongoengine

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DB_URL = "postgresql+psycopg2://postgres:voidpostgres@localhost:5432/mytest2_db"

engine = create_engine(DB_URL, echo=True) # conn

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # cursor


class Base(DeclarativeBase):
    pass