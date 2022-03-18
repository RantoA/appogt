from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:idea22@localhost/ogt"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, bind=engine, autoflush=False)

Base = declarative_base()

def get_db():   
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()