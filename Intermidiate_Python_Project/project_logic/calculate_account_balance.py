def calculate_account_balance(income, expenses):
  if not income and not expenses:
    return 0.0
  else:
    return float(income) - float(expenses)
  