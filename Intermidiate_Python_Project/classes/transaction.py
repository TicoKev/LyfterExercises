from project_logic import date_handler
from datetime import date
class Transaction:
  def __init__(self, title, category, amount, quantity, transaction_date, transaction_type, color):
    if not title:
      raise ValueError("Transaction must have a title.")
    if transaction_type not in ["Income", "Expense"]:
      raise ValueError("Transaction type must be 'Income' or 'Expense'.")
        
    try:
      amount = float(amount)
    except ValueError:
      raise ValueError("Amount must be a number.")
        
    try:
      quantity = int(quantity)
    except ValueError:
      raise ValueError("Quantity must be an integer.")

    if amount < 0 and quantity < 0:
      raise ValueError("Amount and quantity cannot both be negative.")


    if not isinstance(transaction_date, date):
      raise ValueError("Date must be in DD/MM/YYYY format.")

    if not date_handler.date_check(transaction_date):
      raise ValueError("Transaction date cannot be in the future.")
        
    self.title = title.strip()
    self.category = category.strip()
    self.amount = amount
    self.quantity = quantity
    self.transaction_date = transaction_date
    self.transaction_type = transaction_type
    self.color = color.strip()
    self.total = amount * quantity
