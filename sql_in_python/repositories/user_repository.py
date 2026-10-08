class UserRepository():
  def __init__(self, db_manager):
    self.db_manager = db_manager

  def _format_users(self, user_record):
    return {
      'id': user_record[0],
      'name': user_record[1],
      'username': user_record[2],
      'email': user_record[3],
      'date_of_birth': user_record[4].strftime('%Y-%m-%d'),
      'account_state': user_record[5],
      'is_delinquent': user_record[6]
    }

  def create_user(self, name, username, email, user_password, date_of_birth, account_state):
    try:
      
      result = self.db_manager.execute_query(
        '''
        INSERT INTO lyfter_car_rental.users (name, username, email, user_password, date_of_birth, account_state)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id, name, username, email, date_of_birth, account_state, is_delinquent
        ''',
        name, username, email, user_password, date_of_birth, account_state
      )
      formatted_result = self._format_users(result[0])
      return formatted_result if formatted_result else None
    except Exception as e:
      print('Error while inserting an user to the database', e)
      return False

  def get_all(self):
    try:
      results = self.db_manager.execute_query(
        '''
          SELECT id, name, username, email, date_of_birth, account_state, is_delinquent
          FROM lyfter_car_rental.users;
        '''
        )
      formatted_results = [self._format_users(result) for result in results] 
      return formatted_results
    except Exception as e:
      print('Error while getting the users information from database', e)
      return False 

  def get_filtered(self, filters: dict):
    try:
      base_query ='''
        SELECT id, name, username, email, date_of_birth, account_state, is_delinquent
        FROM lyfter_car_rental.users
      '''
      conditions = []
      params = []

      if 'id' in  filters:
        conditions.append('id =  %s')
        params.append(filters['id'])
      
      if 'name' in filters:
        conditions.append('LOWER(name) = LOWER(%s)')
        params.append(filters['name'])

      if 'email' in filters:
        conditions.append('LOWER(email) = LOWER(%s)')
        params.append(filters['email'])

      if 'username' in filters:
        conditions.append('LOWER(username) = LOWER(%s)')
        params.append(filters['username'])

      if 'account_state' in filters:
        conditions.append('account_state = %s')
        params.append(filters['account_state'])

      if 'date_of_birth' in filters:
        conditions.append('date_of_birth = %s')
        params.append(filters['date_of_birth'])

      if 'is_delinquent' in filters:
        conditions.append('is_delinquent = %s')
        params.append(filters['is_delinquent'])

      if conditions:
        base_query += ' WHERE ' + ' AND '.join(conditions)

      results = self.db_manager.execute_query(base_query, *params)
      return [self._format_users(r) for r in results]
    
    except Exception as e:
      print('Error while getting filtered users:', e)
      return False

  def modify_account_state(self, account_state, id):
    try:
      results = self.db_manager.execute_query(
        '''
        UPDATE lyfter_car_rental.users
        SET account_state = %s 
        WHERE id = %s
        RETURNING id, name, username, email, date_of_birth, account_state, is_delinquent
        ''',
        account_state, id
      )
      return self._format_users(results[0]) if results else None
    
    except Exception  as e:
      print('Error while modifying the user information from database', e)
      return False 

  def modify_is_delinquent(self, is_delinquent, id):
    try:
      results = self.db_manager.execute_query(
        '''
        UPDATE lyfter_car_rental.users
        SET is_delinquent = %s 
        WHERE id = %s
        RETURNING id, name, username, email, date_of_birth, account_state, is_delinquent
        ''',
        is_delinquent, id
      )
      return self._format_users(results[0]) if results else None
    
    except Exception  as e:
      print('Error while modifying the user information from database', e)
      return False 

  def get_by_id(self, id):
    try:
      result = self.db_manager.execute_query(
        '''
        SELECT id, name, username, email, date_of_birth, account_state, is_delinquent
        FROM lyfter_car_rental.users
        WHERE id = %s
        ''',
        id
      )
      return self._format_users(result[0]) if result else None
    except Exception as e:
      print('Error while getting the id', e)
    