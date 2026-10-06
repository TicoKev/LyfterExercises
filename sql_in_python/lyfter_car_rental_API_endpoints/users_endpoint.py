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
  
    formatted_results = user_repo.get_all()
    filter_items = request.args.to_dict()
    users = formatted_results
    
    if filter_items:
      for key, value in filter_items.items():
        if not value:
          return jsonify({'error': 'filter is empty'}), 400
        
        if key == 'account_state' and value not in VALID_ACCOUNT_STATES:
          return jsonify({'error': f'Invalid state: {value}, correct states: active, suspended or closed'})

        if key == 'date_of_birth' and not isinstance(value, str):
          return jsonify({'error': 'Date of birth must be a text format(YYYY-MM-DD)'}), 400

        
        users = [u for u in users if str(u.get(key, "")).lower() == value.lower()]

    return{'data' : users}, 200
  
  except Exception as e:
    return jsonify({'error': f'Unexpected error: {e}'}), 500

@users_bp.route('/users', methods=['POST'])
def create_user():
  try:
    data = request.get_json()
    name = data['name']
    username = data['username']
    email = data['email']
    password = data['user_password']
    birth_date = datetime.fromisoformat(data['date_of_birth'])
    account_state = data['account_state']

    if not name or not username or not email or not password or not birth_date:
      return jsonify({'error': 'All fields are required'})

    if not all(isinstance(s, str) for s in [name, username, email, account_state]):
      return jsonify({'error': 'name, username, email and account_state must be text'})

    if not isinstance(birth_date, (date, datetime)):
      return jsonify({'error': 'The date of birth is not a date'})
    date_of_birth = birth_date

    new_user = user_repo.create_user(name=name, username=username, email=email, user_password=password, date_of_birth=date_of_birth, account_state=account_state)

    return jsonify({'message': 'User added succesfully', 'user': new_user }), 200

  except Exception as e:
    return jsonify({'error': f'Unexpected error {e}'}), 500

@users_bp.route('/users/<int:id>', methods=['PUT'])
def modify_user(id):
  try:
    users_list = user_repo.get_all()
    user =  next((u for u in users_list if u['id'] == id), None)

    if not user:
      return jsonify({'error': 'User not found'}), 404
    
    data = request.get_json()

    if 'account_state' in data:
      if not data['account_state']:
        return jsonify({'error': 'Account state must not be empty'}), 400
      
      if not isinstance(data['account_state'], str):
        return jsonify({'error': 'The state must be text'}), 400
      
      if  data['account_state'] not in VALID_ACCOUNT_STATES:
        return jsonify({'error': 'Invalid account state, correct states: active, suspended or closed'})
      
      user['account_state'] = data.get('account_state')
      user_repo.modify_account_state(user['account_state'], id)
    
    if 'is_delinquent' in data:
      if data['is_delinquent'] is None:
        return jsonify({'error': 'Is delinquient must not be empty'}), 400
      
      if not isinstance(data['is_delinquent'], bool):
        return jsonify({'error': 'Is delinquent must be a boolen value (True or False)'}), 400

      user['is_delinquent'] = data.get('is_delinquent')
      user_repo.modify_is_delinquent(user['is_delinquent'], id)
    return jsonify({'message': 'User state modified successfully', 'user': user}), 200
      
  except Exception as e:
    return jsonify({'error': f'Unexpected error {e}'}), 500
