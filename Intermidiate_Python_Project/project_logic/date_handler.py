from datetime import datetime


def format_date(transaction_date):
  try:
    date_info = datetime.strptime(transaction_date, "%d/%m/%Y")
    return date_info
  except ValueError:
    return None


def date_check(transaction_date):
    current_date = datetime.today()
    if transaction_date > current_date:
      raise ValueError("The date must not be a future date")
    return transaction_date