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
    
    make =  data['make']
    model = data['model']
    fabrication_year = data['fabrication_year']
    state = data['state']

    if not make or not model or not fabrication_year or not state:
      return jsonify({'error': 'All fields are required'})

    if not all(isinstance(s, str) for s in [make, model, state]):
      return jsonify({'error': 'make, model and state must be text'})

    if not isinstance(fabrication_year, int):
      return jsonify({'error': 'Fabrication year must be a number'})

    new_car = car_repo.create_car(make, model, fabrication_year, state)

    return jsonify({'message': 'Car added successfully', 'car': new_car}), 200

  except Exception as e:
    return jsonify({'error': f'Unexpected error, {e}'}), 500  


@cars_bp.route('/cars')
def get_cars():
  try:
    formatted_results = car_repo.get_all()
    filter_items = request.args.to_dict()
    cars = formatted_results

    if filter_items:
      for key, value in filter_items.items():
        if not value:
          return jsonify({'error': 'filter is empty'}), 400
        
        if key == 'state' and value not in VALID_CAR_STATES:
          return jsonify({'error': f'Invalid state {value}, correct states: available, rented, maintenance or disabled'})

        if key == 'fabrication_year':
          try:
              fabrication_year = value
              fabrication_year = int(fabrication_year)
          except (ValueError, TypeError):
              return jsonify({'error': 'Fabrication year is not correct'}), 400
        
        cars = [c for c in cars if str(c.get(key, "")).lower() == value.lower()]

    return jsonify({'data': cars}), 200

  except Exception as e:
    return jsonify({'error': f'Unexpected error, {e}'}), 500

@cars_bp.route('/cars/<int:id>', methods=['PUT'])
def modify_car(id):
  try:
    cars_list = car_repo.get_all()
    car = next((c for c in cars_list if c['id'] == id), None)

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
    
  except Exception as e:
    return  jsonify({'error': f'Unexpected error, {e}'}), 500
 