from datetime import date, datetime
from flask import Blueprint, request, jsonify
from sql_in_python.pg_manager.db import db_manager 
from sql_in_python.repositories.rent_repository import RentRepository

rents_bp = Blueprint('rents', __name__)
VALID_RENT_STATES = ['pending','active','completed','cancelled','overdue']
rent_repo = RentRepository(db_manager)

@rents_bp.route('/rents', methods=['POST'])
def create_rent():
  try:
    data = request.get_json()
    
    user =  data['user_id']
    car = data['car_id']
    rent_date = data['rent_date']
    rent_status = data['rent_status']

    if not user or not car or not rent_date or not rent_status:
      return jsonify({'error': 'All fields are required'})

    if not all(isinstance(s, int) for s in [user, car]):
      return jsonify({'error': 'user and car must be a number.'})

    if not isinstance(rent_status, str):
      return jsonify({'error': 'Rent status must be a number'})

    new_rent = rent_repo.create_rent(user, car, rent_date, rent_status)

    return jsonify({'message': 'rent added successfully', 'rent': new_rent}), 200

  except Exception as e:
    return jsonify({'error': f'Unexpected error, {e}'}), 500  


@rents_bp.route('/rents')
def get_rents():
  try:
    formatted_results = rent_repo.get_all()
    filter_items = request.args.to_dict()
    rents = formatted_results

    if filter_items:
      for key, value in filter_items.items():
        if not value:
          return jsonify({'error': 'filter is empty'}), 400
        
        if key == 'rent_status' and value not in VALID_RENT_STATES:
          return jsonify({'error': f'Invalid state {value}, correct states: pending, active, completed, cancelled, overdue'})
        
        if key == 'rent_date':
          rent_date = value
          if not isinstance(rent_date, str):
            return jsonify({'error': 'Rent date must be a text format(YYYY-MM-DD)'}), 400
         
          try:
            rent_date = datetime.fromisoformat(value).date()
          except ValueError:
            return jsonify({'error': f'The date entered is not correct'})
        
        rents = [c for c in rents if str(c.get(key, "")).lower() == value.lower()]

    return jsonify({'data': rents}), 200

  except Exception as e:
    return jsonify({'error': f'Unexpected error, {e}'}), 500

@rents_bp.route('/rents/<int:id>', methods=['PUT', 'PATCH'])
def modify_rent(id):
  try:
    rents_list = rent_repo.get_all()
    rent = next((c for c in rents_list if c['id'] == id), None)

    if not rent:
      return jsonify({'error': 'rent not found'}), 404
    
    data = request.get_json()

    if 'rent_status' in data:
      if not data['rent_status']:
        return jsonify({'error': 'State must not be empty'}), 400
      
      if not isinstance(data['rent_status'], str):
        return jsonify({'error': 'The state must be text'}), 400
      
      if data['rent_status'] not in VALID_RENT_STATES:
        return jsonify({'error': f'Invalid state, correct states: pending, active, completed, cancelled, overdue'}), 400

      rent['rent_status'] = data.get('rent_status')
      rent_repo.modify_rent_status(rent['rent_status'], id)
      return jsonify({'message': 'rent status modified successfully', 'rent': rent}), 200
    
  except Exception as e:
    return  jsonify({'error': f'Unexpected error, {e}'}), 500
 