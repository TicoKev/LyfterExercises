from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, ForeignKey, insert, select, update, delete

DB_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'

engine = create_engine(DB_URI, echo=True)

try:
  connection = engine.connect()
  connection.close()
except Exception as e:
  print('Unexpected error, connection failed', e)
