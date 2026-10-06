import psycopg2

class PgManager():
  def __init__(self, db_name, user, password, host, port=5432):
    self.db_name = db_name
    self.user = user
    self.password = password
    self.host = host
    self.port = port

    self.connection = self.create_connection()
    if self.connection:
      self.cursor = self.connection.cursor()

  def create_connection(self):
    try:
      connection = psycopg2.connect(
        dbname = self.db_name,
        user = self.user,
        password = self.password,
        host = self.host,
        port = self.port
      )
      return connection
    except Exception as e:
      return None

  def close_connection(self):
    if self.cursor:
      self.cursor.close()
    if self.connection:
      self.connection.close()

  def execute_query(self, query, *args):
    
    self.cursor.execute(query, args)
    self.connection.commit()
    if self.cursor.description:
      results = self.cursor.fetchall()
      return results