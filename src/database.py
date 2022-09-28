from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE = 'postgresql'
USER = 'postgres'
PASSWORD = 'Kesharitek1..'
HOST = 'localhost'
PORT = '5432'
DB_NAME = 'sponsoredby'
engine = create_engine(
    f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME }')
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
