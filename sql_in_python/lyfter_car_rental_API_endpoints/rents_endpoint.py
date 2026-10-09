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
    
    user =  data.get('user_id')
    car = data.get('car_id')
    rent_status = data.get('rent_status')

    if not user or not car or not rent_status:
      return jsonify({'error': 'All fields are required'}), 400

    if not all(isinstance(s, int) for s in [user, car]):
      return jsonify({'error': 'user and car must be a number.'}), 400

    if not isinstance(rent_status, str):
      return jsonify({'error': 'Rent status must be text'}), 400

    new_rent = rent_repo.create_rent(user, car, rent_status)

    print(new_rent)

    if not new_rent or new_rent is False:
      return jsonify({'error': 'Error while adding the new rent'}), 400
    
    return jsonify({'message': 'rent added successfully', 'rent': new_rent}), 201

  except Exception as e:
    return jsonify({'error': f'Unexpected error, {e}'}), 500  


@rents_bp.route('/rents')
def get_rents():
  try:
    filter_items = request.args.to_dict()

    if filter_items:
      for key, value in filter_items.items():
        if not value:
          return jsonify({'error': f'filter {key} is empty'}), 400
        
      if 'rent_status' in filter_items and filter_items['rent_status'] not in VALID_RENT_STATES:
        return jsonify({'error': f'Invalid state {value}, correct states: pending, active, completed, cancelled, overdue'}), 400
      
      if 'rent_date' in filter_items:
        rent_date = filter_items['rent_date']
        if not isinstance(rent_date, str):
          return jsonify({'error': 'Rent date must be a text format(YYYY-MM-DD)'}), 400
       
        try:
          rent_date = datetime.fromisoformat(filter_items['rent_date']).date()
        except ValueError:
          return jsonify({'error': f'The date entered is not correct'}), 400
        
      rents = rent_repo.get_filtered(filter_items)

    else:
      rents = rent_repo.get_all()

    if rents == []:
      return jsonify({'data': rents,
                      'message': 'Unable to get the rent, no coincidences found',}), 200 
    
    if rents is False:
      return jsonify({'error': 'Internal database error'}), 500
    
    return jsonify({'data': rents}), 200

  except Exception as e:
    return jsonify({'error': f'Unexpected error, {e}'}), 500

@rents_bp.route('/rents/<int:id>', methods=['PUT'])
def modify_rent(id):
  try:
    rent = rent_repo.get_by_id(id)

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
    else:
      return jsonify({'error': 'Missing rent status field'}), 400
    
  except Exception as e:
    return  jsonify({'error': f'Unexpected error, {e}'}), 500
 