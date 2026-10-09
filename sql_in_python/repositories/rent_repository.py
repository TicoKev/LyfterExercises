class RentRepository():
  def __init__(self, db_manager):
    self.db_manager = db_manager

  def _format_rents(self, rent_record):
    return {
      'id': rent_record[0],
      'user_id': rent_record[1],
      'car_id': rent_record[2],
      'rent_date': rent_record[3].strftime('%Y-%m-%d'),
      'rent_status': rent_record[4]
    }

  def create_rent(self, user_id: int, car_id: int, rent_status: str):
    try:
      user_check = self.db_manager.execute_query(
        '''
        SELECT account_state, is_delinquent
        FROM lyfter_car_rental.users
        WHERE id = %s
        ''',
        user_id
      )
      if not user_check:
        print ('error: User not found')
        return False
      
      account_state, is_delinquent = user_check[0]
      
      if account_state != 'active':
        print('error: User account is not active')
        return False
      
      if is_delinquent:
        print('error: User is delinquent')
        return False
      
      car_check = self.db_manager.execute_query(
          '''
          SELECT state
          FROM lyfter_car_rental.cars
          WHERE id = %s
          ''',
          car_id
      )
      if not car_check:
        print({'error: Car not found'})
        return False
      
      car_state = car_check[0][0]
      
      if car_state != 'available':
        print('Car is not available')
        return False
      
      result = self.db_manager.execute_query(
        '''
        INSERT INTO lyfter_car_rental.users_cars (user_id, car_id, rent_status)
        VALUES (%s, %s, %s)
        RETURNING id, user_id, car_id, rent_date, rent_status
        ''',
        user_id, car_id, rent_status
      )
    
      self.db_manager.execute_query(
        '''
        UPDATE lyfter_car_rental.cars
        SET state = 'rented'
        WHERE id = %s
        ''',
        car_id
      )
      print(result)

      formatted_result = self._format_rents(result[0])
      print(formatted_result)
     
      return formatted_result if formatted_result else None

    except Exception as e:
      print("Error while inserting a rent:", e)

  def get_all(self):
    try:
      results = self.db_manager.execute_query(
      'SELECT id, user_id, car_id, rent_date, rent_status FROM lyfter_car_rental.users_cars;'
        )
      formatted_results = [self._format_rents(result) for result in results] 
      return formatted_results
    except Exception as e:
      print('Error while getting the rents information from database', e)
      return False

  def get_filtered(self, filters: dict):
    try:
      base_query ='''
        SELECT id, user_id, car_id, rent_date, rent_status
        FROM lyfter_car_rental.users_cars
      '''
      conditions = []
      params = []

      if 'id' in  filters:
        conditions.append('id =  %s')
        params.append(filters['id'])
      
      if 'user_id' in filters:
        conditions.append('user_id = %s')
        params.append(filters['user_id'])

      if 'car_id' in filters:
        conditions.append('car_id = %s')
        params.append(filters['car_id'])

      if 'rent_date' in filters:
        conditions.append('rent_date = %s')
        params.append(filters['rent_date'])

      if 'rent_status' in filters:
        conditions.append('rent_status = %s')
        params.append(filters['rent_status'])

      if conditions:
        base_query += ' WHERE ' + ' AND '.join(conditions)

      results = self.db_manager.execute_query(base_query, *params)
      return [self._format_rents(r) for r in results]
    
    except Exception as e:
      print('Error while getting filtered cars:', e)
      return False

  def modify_rent_status(self, rent_status, id):
    try:
      car_id = self.db_manager.execute_query(
      '''
        SELECT car_id FROM lyfter_car_rental.users_cars
        WHERE id = %s
      ''', id
      )
      print(car_id)
      results = self.db_manager.execute_query(
        '''
        UPDATE lyfter_car_rental.users_cars
        SET rent_status = %s 
        WHERE id = %s
        RETURNING user_id, car_id, rent_date, rent_status;
        ''',
        rent_status, id
      )

      self.db_manager.execute_query(
        '''
        UPDATE lyfter_car_rental.cars
        SET state = 'available'
        WHERE id = %s
        ''', car_id[0]
      )
      return self._format_rents(results[0]) if results else None
    
    except Exception  as e:
      print('Error while modifying the rent information from database', e)
      return False 

  def get_by_id(self, id):
    try:
      result = self.db_manager.execute_query(
        '''
        SELECT id, user_id, car_id, rent_date, rent_status
        FROM lyfter_car_rental.users_cars
        WHERE id = %s
        ''',
        id
      )
      return self._format_rents(result[0]) if result else None
    except Exception as e:
      print('Error while getting the id', e)
    