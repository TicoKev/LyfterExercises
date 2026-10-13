from datetime import date, datetime
from flask import Blueprint, request, jsonify
from sql_in_python.pg_manager.db import db_manager
from sql_in_python.repositories.user_repository import UserRepository

users_bp = Blueprint('users', __name__)

VALID_ACCOUNT_STATES = ['active', 'suspended', 'closed']
user_repo = UserRepository(db_manager)

@users_bp.route('/users')
def get_users():
  try:
    filter_items = request.args.to_dict()
    
    if filter_items:
      for key, value in filter_items.items():
        if not value:
          return jsonify({'error': f'Filter {key} is empty'}), 400

      if 'id' in filter_items:
        try:
          id_value = int(filter_items['id'])
          if id_value <= 0:
            return jsonify({'error': 'id must be a postive number higher than 0'}), 400
          filter_items['id'] = id_value
        except ValueError:
          return jsonify({'error': 'id must be a number'}), 400
      
      if 'account_state' in filter_items:
        filter_items['account_state'] = filter_items['account_state'].lower()
        if filter_items['account_state'] not in VALID_ACCOUNT_STATES:
          return jsonify({'error': f'Invalid state: {filter_items["account_state"]}', 'correct states': 'active, suspended or closed'}), 400
      
      if 'date_of_birth' in filter_items:
        try:
            datetime.fromisoformat(filter_items['date_of_birth'])
        except ValueError:
            return jsonify({'error': 'Date of birth must be in format YYYY-MM-DD'}), 400

      if 'name' in filter_items:
        filter_items['name'] = filter_items['name'].lower()
            
      if 'username' in filter_items:
        filter_items['username'] = filter_items['username'].lower()

      if 'email' in filter_items:
        filter_items['email'] = filter_items['email'].lower()

      users = user_repo.get_filtered(filter_items)
    
    else:
        users = user_repo.get_all()        
    
    if users == []:
      return jsonify({'data': users,
                      'message': 'No coincidences found',}), 200 

    if users == False:
      return jsonify({'error': 'Internal database error'}), 500
    
    return{'data' : users}, 200
  
  except Exception as e:
    return jsonify({'error': f'Unexpected error: {e}'}), 500

@users_bp.route('/users', methods=['POST'])
def create_user():
  try:
    data = request.get_json()

    required_fields = ["name", "username", "email", "user_password", "date_of_birth", "account_state"]

    missing_fields = [field for field in  required_fields if not data.get(field)]

    if missing_fields:
      return jsonify({'error': 'All field are required', 
                      'missing': missing_fields}), 400

    name = data.get('name')
    username = data.get('username')
    email = data.get('email')
    password = data.get('user_password')
    account_state = data.get('account_state')
    b_day = data.get('date_of_birth')
    
    if b_day:
      try:
        birth_date = datetime.fromisoformat(data.get('date_of_birth'))
        b_day = birth_date
      except (ValueError, TypeError) as e:
        return jsonify({'error': f'Incorrect format entered, {e}', 'correct format': 'YYYY-MM-DD'}), 400
  
    if not all(isinstance(s, str) for s in [name, username, email, account_state]):
      return jsonify({'error': 'name, username, email and account_state must be text'}), 400
    
    new_user = user_repo.create_user(name=name, username=username, email=email, user_password=password, date_of_birth=b_day, account_state=account_state)

    if not new_user:
      return jsonify({'error': 'Error while adding the new user'}), 400
        
    return jsonify({'message': 'User added succesfully', 'user': new_user }), 201

  except Exception as e:
    return jsonify({'error': f'Unexpected error {e}'}), 500

@users_bp.route('/users/<int:id>', methods=['PUT'])
def modify_user(id):
  try:
    data = request.get_json()
    user = user_repo.get_by_id(id)

    if not user:
      return jsonify({'error': 'User not found'}), 404

    if 'account_state' in data:
      state = data.get('account_state')

      if not state:
        return jsonify({'error': 'Account state must not be empty'}), 400
      if not isinstance(state, str):
        return jsonify({'error': 'Account state must be text'}), 400
      if state not in VALID_ACCOUNT_STATES:
        return jsonify({'error': 'Invalid state', 'correct states': 'active, suspended or closed'}), 400

      user['account_state'] = state
      result = user_repo.modify_account_state(state, id)
      if result is None:
        return jsonify({'error': 'Unable to modify user'}), 400
      if result == False:
        return jsonify({'error': 'Internal database error'}), 500
    
    if 'is_delinquent' in data:
      delinquency = data.get('is_delinquent')

      if delinquency is None:
        return jsonify({'error' : 'Is delinquent must not be empty'}), 400
      if not isinstance(delinquency, bool):
        return jsonify({'error': 'Is delinquent must be boolean (true or false)'}), 400
      
      user['is_delinquent'] = delinquency
      result = user_repo.modify_is_delinquent(delinquency, id)
      if result is None:
        return jsonify({'error': 'Unable to modify user'}), 400
      if result == False:
        return jsonify({'error': 'Internal database error'}), 500

    if 'account_state' not in data and 'is_delinquent' not in data:
      return jsonify({'error': 'Missing account_state and/or is_delinquent field'}), 400

    return jsonify({'message': 'User modified successfully', 'user': user}), 200
        
  except Exception as e:
    return jsonify({'error': f'Unexpected error ocurred, {e}'}), 500
