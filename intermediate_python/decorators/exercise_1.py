def decorator_function(func):
  def wrapper(*args):
    print(f"Printing the args: {args}")
    result = func(*args)
    print(f"Function: {func.__name__}. Returned: {result}")

    return result
  return wrapper

@decorator_function
def numbers_sum(num_1, num_2):
  return num_1 + num_2

print(numbers_sum(10, 50))