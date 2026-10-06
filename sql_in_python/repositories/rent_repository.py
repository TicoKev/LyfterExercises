class RentRepository():
  def __init__(self, db_manager):
    self.db_manager = db_manager

  def _format_rents(self, rent_record):
    return {
      'id': rent_record[0],
      'user_id': rent_record[1],
      'car_id': rent_record[2],
      'rent_date': rent_record[3].strftime("%Y-%m-%d"),
      'rent_status': rent_record[4]
    }

  def create_rent(self, user_id, car_id, rent_date, rent_status):
    try:
      
      result = self.db_manager.execute_query(
        '''
        INSERT INTO lyfter_car_rental.users_cars (user_id, car_id, rent_date, rent_status)
        VALUES (%s, %s, %s, %s)
        RETURNING id, user_id, car_id, rent_date, rent_status
        ''',
        user_id, car_id, rent_date, rent_status
      )
      formatted_result = self._format_rents(result[0])
      return formatted_result if formatted_result else None
    except Exception as e:
      print('Error while inserting a rent to the database', e)
      return False

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


  def modify_rent_status(self, rent_status, id):
    try:
      results = self.db_manager.execute_query(
        '''
        UPDATE lyfter_car_rental.users_cars
        SET rent_status = %s 
        WHERE id = %s
        RETURNING user_id, car_id, rent_date, rent_status;
        ''',
        rent_status, id
      )
      return self._format_rents(results[0]) if results else None
    
    except Exception  as e:
      print('Error while modifying the rent information from database', e)
      return False 