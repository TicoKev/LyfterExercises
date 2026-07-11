from datetime import datetime

def filter_transaction(start_date, end_date, transaction_data):
  if not start_date or not end_date:
    print("Both dates must be entered")
    
  filtered_data = [
    register for register in transaction_data
    if start_date <= datetime.strptime(register.transaction_date, "%d/%m/%Y") <= end_date
  ]

  if not filtered_data:
    raise ValueError("No data found in the date range")
    
  return filtered_data
  