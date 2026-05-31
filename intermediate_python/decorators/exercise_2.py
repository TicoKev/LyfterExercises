def is_number(func):
  def wrapper(*args):
    for arg in args:
      if not isinstance(arg, int):
        raise TypeError(f"{arg} is not a number")
    result = func(*args)
    return result
  return wrapper

@is_number
def is_number_function(*args):
  return args


is_number_function(2, 2, 5, "g", 6, 7, 10, 6, 10)