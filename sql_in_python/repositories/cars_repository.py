class CarRepository():
  def __init__(self, db_manager):
    self.db_manager = db_manager

  def _format_cars(self, car_record):
    return {
      'id': car_record[0],
      'make': car_record[1],
      'model': car_record[2],
      'fabrication_year': car_record[3],
      'state': car_record[4]
    }

  def create_car(self, make, model, fabrication_year, state):
    try:
      
      result = self.db_manager.execute_query(
        '''
        INSERT INTO lyfter_car_rental.cars (make, model, fabrication_year, state)
        VALUES (%s, %s, %s, %s)
        RETURNING id, make, model, fabrication_year, state
        ''',
        make, model, fabrication_year, state
      )
      formatted_result = self._format_cars(result[0])
      return formatted_result if formatted_result else None
    except Exception as e:
      print('Error while inserting a car to the database', e)
      return False

  def get_all(self):
    try:
      results = self.db_manager.execute_query(
        'SELECT id, make, model, fabrication_year, state FROM lyfter_car_rental.cars;'
        )
      formatted_results = [self._format_cars(result) for result in results] 
      return formatted_results
    except Exception as e:
      print('Error while getting the cars information from database', e)
      return False

  def get_filtered(self, filters: dict):
    try:
      base_query ='''
        SELECT id, make, model, fabrication_year, state
        FROM lyfter_car_rental.cars
      '''
      conditions = []
      params = []

      if 'id' in  filters:
        conditions.append('id =  %s')
        params.append(filters['id'])
      
      if 'make' in filters:
        conditions.append('LOWER(make) = LOWER(%s)')
        params.append(filters['make'])

      if 'model' in filters:
        conditions.append('LOWER(model) = LOWER(%s)')
        params.append(filters['model'])

      if 'fabrication_year' in filters:
        conditions.append('fabrication_year = %s')
        params.append(filters['fabrication_year'])

      if 'state' in filters:
        conditions.append('state = %s')
        params.append(filters['state'])

      if conditions:
        base_query += ' WHERE ' + ' AND '.join(conditions)

      results = self.db_manager.execute_query(base_query, *params)
      return [self._format_cars(r) for r in results]
    
    except Exception as e:
      print('Error while getting filtered cars:', e)
      return False

  def modify_state(self, account_state, id):
      try:
        results = self.db_manager.execute_query(
          '''
          UPDATE lyfter_car_rental.cars
          SET state = %s 
          WHERE id = %s
          RETURNING id, make, model, fabrication_year, state
          ''',
          account_state, id
        )
        return self._format_cars(results[0]) if results else None

      except Exception  as e:
        print('Error while modifying the car information from database', e)
        return False 
  def get_by_id(self, id):
    try:
      result = self.db_manager.execute_query(
        '''
        SELECT id, make, model, fabrication_year, state
        FROM lyfter_car_rental.cars
        WHERE id = %s
        ''',
        id
      )
      return self._format_cars(result[0]) if result else None
    except Exception as e:
      print('Error while getting the id', e)
    