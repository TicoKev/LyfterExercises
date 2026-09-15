from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

VALID_STATES = ['pending', 'inprogress', 'completed']

STATE_ALIASES = {
    'porhacer': 'pending',
    'enprogreso': 'inprogress',
    'completada': 'completed'
}

@app.route('/tasks')
def get_tasks():
  try:
    filtered_tasks = read_json('tasks_list.json')
    state_filter = request.args.get('state')
    
    if state_filter:
      normalized_state = normalize_state(state_filter)
      state_error = check_valid_states(normalized_state)
      if state_error:
        return state_error
      
      filtered_tasks = list(filter(lambda task: task['state'] == normalized_state, filtered_tasks))
    return {'data': filtered_tasks}, 200
  
  except FileNotFoundError:
    return {'error': 'Tasks file not found, you must create a task first'}, 404
  except Exception as e:
    return {'error': f'Unexpected error: {str(e)}'}, 500

@app.route('/tasks', methods=['POST'])
def add_task():
  try:
    add_json_file()
    data = request.get_json()
    
    identifier =  data.get('identifier')
    title = data.get('title')
    description = data.get('description')
    state = data.get('state')

    field_error = is_field_empty(identifier, title, description, state)
    if field_error:
      return field_error

    if not isinstance(identifier, int) or identifier <= 0:
      return jsonify({'error': f'Identifier must be a positive number and can`t be 0.'}), 400

    values_error = check_string_values(identifier, title, description, state)
    if values_error:
      return values_error
    
    normalized_state = normalize_state(state)

    state_error = check_valid_states(normalized_state)
    if state_error:
      return state_error

    tasks = read_json('tasks_list.json')

    if (any(t['identifier'] == identifier for t in tasks)):
      return jsonify({'error': f'Task with identifier {identifier} already exists'}), 409

    new_task = {
      'identifier': identifier,
      'title': title,
      'description': description,
      'state': normalized_state
    }
    write_json('tasks_list.json', tasks, new_task)

    return jsonify({'message': 'Task added successfully', 'task': new_task}), 201
  except Exception as e:
    return jsonify( {'error': f'Unexpected error: {str(e)}'}), 500

@app.route('/tasks/<int:identifier>', methods=['PUT'])
def edit_task(identifier):
  try:
    tasks = read_json('tasks_list.json')
    task = get_task_info(tasks, identifier)

    no_task_error = no_task_found(task)
    if no_task_error:
      return no_task_error

    data = request.get_json()

    if 'title' in data:
      if not isinstance(data['title'], str):
        return jsonify({'error': 'title must be text'}), 400
      task['title'] = data['title']

    if 'description' in data:
      if not isinstance(data['description'], str):
        return jsonify({'error': 'description must be text'}), 400
      task['description'] = data['description']

    if 'state' in data:
      normalized_state = normalize_state(data['state'])
      state_error = check_valid_states(normalized_state)
      if state_error:
        return state_error
      task['state'] = normalized_state

    with open('tasks_list.json', 'w', encoding='utf-8') as file:
      json.dump(tasks, file, indent=2)

    return jsonify({'message': 'Task updated successfully', 'task': task}), 200

  except FileNotFoundError:
    return {'error': 'Tasks file not found, you must create a task first'}, 404
  except Exception as e:
    return jsonify({'error': f'Unexpected error: {str(e)}'}), 500


@app.route('/tasks/<int:identifier>', methods=['DELETE'])
def delete_task(identifier):
  try:
    tasks_list = read_json('tasks_list.json')
    task = get_task_info(tasks_list, identifier)

    no_task_error = no_task_found(task)
    if no_task_error:
      return no_task_error

    tasks_list.remove(task)
    delete_task_json('tasks_list.json', tasks_list)
    
    return {'message': 'Task deleted successfully'}, 200
  
  except FileNotFoundError:
    return {'error': 'Tasks file not found, you must create a task first'}, 404
  
  except Exception as e:
    return jsonify( {'error': f'Unexpected error: {str(e)}'}), 500


def read_json(path):
  with open(path, 'r', encoding='utf-8') as file:
    data = json.load(file)
    return data


def create_json(path):
  with open(path, 'w', encoding='utf-8') as file:
    json.dump([], file, indent=2)


def write_json(path, data, new_task):
  data.append(new_task)
  with open(path, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2)


def add_json_file():
  if not os.path.exists('tasks_list.json'):
    return create_json('tasks_list.json')


def delete_task_json(path, tasks_list):
  with open(path, 'w', encoding='utf-8') as file:
    json.dump(tasks_list, file, indent=2)


def normalize_state(state: str):
  normalized = state.lower().replace(' ', '')
  return STATE_ALIASES.get(normalized, normalized)


def get_task_info(tasks, identifier):
  return next((t for t in tasks if t['identifier'] == identifier), None)


def no_task_found(task):
  if not task:
    return jsonify({'error': 'Task not found'}), 404


def check_valid_states(state):
  if state not in VALID_STATES:
    return {'error': f'Invalid state: {state}'}, 400


def check_string_values(title='', description='', state=''):
  if not isinstance(title, str) or not isinstance(description, str) or not isinstance(state, str):
    return jsonify({'error': 'title, description and state must be text only'}), 400


def is_field_empty(identifier, title = '', description = '', state = ''):
  if identifier == None or not title or not description or not state:
    return jsonify({'error': 'All fields are required'}), 400

if __name__ == '__main__':
  app.run('localhost', debug=True)

  