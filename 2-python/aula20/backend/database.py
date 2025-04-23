from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

POSTGRES_DATABASE_UEL = "postgresql://user:password@postgres/mydatabase"

engine = create_engine(POSTGRES_DATABASE_UEL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
