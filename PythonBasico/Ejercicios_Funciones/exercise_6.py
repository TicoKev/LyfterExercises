def sort_string(string):
  string_list = string.split("-")
  string_list.sort()
  result = "-".join(string_list)

  return result


print(sort_string("python-variable-funcion-computadora-monitor"))