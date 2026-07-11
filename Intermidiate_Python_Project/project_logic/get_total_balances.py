def handle_errors(func):
  def wrapper(*args,**kwargs):
    try:
      return func(*args, **kwargs)
    except (AttributeError, TypeError) as error:
      print(f"Invalid object structure in function {func.__name__}. {error}")
  return wrapper


@handle_errors
def get_total_expense(expenses):
  return sum(e.total for e in expenses.expense_data)


@handle_errors
def get_total_income(income_list): 
  return sum(i.total for i in income_list.income_data)
  

