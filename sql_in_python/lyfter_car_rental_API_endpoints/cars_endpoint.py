from flask import Blueprint, request, jsonify
from sql_in_python.pg_manager.db import db_manager 
from sql_in_python.repositories.cars_repository import CarRepository

cars_bp = Blueprint('cars', __name__)
VALID_CAR_STATES = ['available', 'rented', 'maintenance', 'disabled']
car_repo = CarRepository(db_manager)

@cars_bp.route('/cars', methods=['POST'])
def create_car():
  try:
    data = request.get_json()
    
    make =  data.get('make')
    model = data.get('model')
    fabrication_year = data.get('fabrication_year')
    state = data.get('state')

    if not make or not model or not fabrication_year or not state:
      return jsonify({'error': 'All fields are required'}), 400

    if not all(isinstance(s, str) for s in [make, model, state]):
      return jsonify({'error': 'make, model and state must be text'}), 400

    if not isinstance(fabrication_year, int):
      return jsonify({'error': 'Fabrication year must be a number'}), 400

    new_car = car_repo.create_car(make, model, fabrication_year, state)

    if not new_car:
      return jsonify({'error': 'Error while adding the new user'}), 400
        
    return jsonify({'message': 'Car added successfully', 'car': new_car}), 201

  except Exception as e:
    return jsonify({'error': f'Unexpected error, {e}'}), 500  


@cars_bp.route('/cars')
def get_cars():
  try:
    filter_items = request.args.to_dict()

    if filter_items:
      for key, value in filter_items.items():
        if not value:
          return jsonify({'error': f'filter {key} is empty'}), 400

      if 'id' in filter_items:
        try:
          id_value = int(filter_items['id'])
          if id_value < 0:
            return jsonify({'error': 'id must be a postive number'}), 400
          filter_items['id'] = id_value
        except ValueError:
          return jsonify({'error': 'id must be a number'}), 400

      if 'make' in filter_items:
        filter_items['make'] = filter_items['make'].lower()

      if 'model' in filter_items:
       filter_items['model'] = filter_items['model'].lower()  

      if 'state' in filter_items and filter_items['state'] not in VALID_CAR_STATES:
        return jsonify({'error': f'Invalid state {value}, correct states: available, rented, maintenance or disabled'}), 400

      if 'fabrication_year' in filter_items:
        try:
          year_value = int(filter_items['fabrication_year'])
          filter_items['fabrication_year'] = year_value
        except (ValueError, TypeError):
          return jsonify({'error': 'Fabrication year is not correct'}), 400
          
      cars = car_repo.get_filtered(filter_items)    
    
    else:
      cars = car_repo.get_all()

    if not cars:
      return jsonify({'error': 'Unable to get the car'}), 400 
    
    return jsonify({'data': cars}), 200

  except Exception as e:
    return jsonify({'error': f'Unexpected error, {e}'}), 500

@cars_bp.route('/cars/<int:id>', methods=['PUT'])
def modify_car(id):
  try:
    car = car_repo.get_by_id(id)
    
    if not car:
      return jsonify({'error': 'Car not found'}), 404
    
    data = request.get_json()

    if 'state' in data:
      if not data['state']:
        return jsonify({'error': 'State must not be empty'}), 400
      
      if not isinstance(data['state'], str):
        return jsonify({'error': 'The state must be text'}), 400
      
      if data['state'] not in VALID_CAR_STATES:
        return jsonify({'error': f'Invalid state, correct states: available, rented, maintenance or disabled'}), 400

      car['state'] = data.get('state')
      car_repo.modify_state(car['state'], id)
      return jsonify({'message': 'car state modified successfully', 'car': car}), 200
    else:
      return jsonify({'error': 'Missing state field'}), 400
    
  except Exception as e:
    return jsonify({'error': f'Unexpected error, {e}'}), 500
 