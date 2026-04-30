employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

employee_department_dictionary = {}

for employee in employees:
  employee_department = employee["department"]
  employee_name = employee["name"]
  
  if not employee_department in employee_department_dictionary:
    employee_department_dictionary[employee_department] = []
    employee_department_dictionary[employee_department].append(employee_name)
  else:
    employee_department_dictionary[employee_department].append(employee_name)


print(employee_department_dictionary)

