def calculate_account_balance(income, expenses):
  try:
    return float(income) - float(expenses)
  except (ValueError, TypeError):
    print("Both parameters must be numeric")
    return 0.0

  