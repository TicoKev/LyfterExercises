from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

DB_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'

engine = create_engine(DB_URI, echo=True)

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

def check_connection():
  with SessionLocal() as session:
    try:
      session.connection()
      print('Connection successful!')
      return True
    except SQLAlchemyError as e:
      print(f'Error while connecting to the database: {e}')
      return False