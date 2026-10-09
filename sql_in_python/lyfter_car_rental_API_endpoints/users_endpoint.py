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
      
      if 'account_state' in filter_items:
        filter_items['account_state'] = filter_items['account_state'].lower()
        if filter_items['account_state'] not in VALID_ACCOUNT_STATES:
          return jsonify({'error': f'Invalid state: {filter_items['account_state']}, correct states: active, suspended or closed'}), 400
      
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
    
    if not users:
      return jsonify({'error': 'Unable to get the users'}), 400 
    
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
    if not isinstance(data.get('date_of_birth'), (date, datetime)):
      return jsonify({'error': 'The date of birth is not a date'}), 400
    birth_date = datetime.fromisoformat(data.get('date_of_birth'))

    if not all(isinstance(s, str) for s in [name, username, email, account_state]):
      return jsonify({'error': 'name, username, email and account_state must be text'}), 400
    
    date_of_birth = birth_date

    new_user = user_repo.create_user(name=name, username=username, email=email, user_password=password, date_of_birth=date_of_birth, account_state=account_state)

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

    if 'account_state' in data:
      if not data['account_state']:
        return jsonify({'error': 'Account state must not be empty'}), 400
      
      if not isinstance(data['account_state'], str):
        return jsonify({'error': 'The state must be text'}), 400
      
      if data['account_state'] not in VALID_ACCOUNT_STATES:
        return jsonify({'error': 'Invalid account state, correct states: active, suspended or closed'}), 400
    else:
      jsonify({'error': 'Missing account state field'}), 400
      
      user['account_state'] = data.get('account_state')
      user_repo.modify_account_state(user['account_state'], id)
    
    if 'is_delinquent' in data:
      if data['is_delinquent'] is None:
        return jsonify({'error': 'Is delinquient must not be empty'}), 400
      
      if not isinstance(data['is_delinquent'], bool):
        return jsonify({'error': 'Is delinquent must be a boolen value (True or False)'}), 400

      user['is_delinquent'] = data.get('is_delinquent')
      user_repo.modify_is_delinquent(user['is_delinquent'], id)
    else:
      jsonify({'error': 'Missing is_delinquent field'}), 400

    return jsonify({'message': 'User state modified successfully', 'user': user}), 200
      
  except Exception as e:
    return jsonify({'error': f'Unexpected error {e}'}), 500
