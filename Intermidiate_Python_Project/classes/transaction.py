class Transaction:
  total = 0
  def __init__(self, title, category, amount, quantity, transaction_date, transaction_type, color):
    self.title = title
    self.category = category
    self.amount = amount
    self.quantity = quantity
    self.transaction_date = transaction_date
    self.transaction_type = transaction_type
    self.color = color
    self.total = int(amount) * int(quantity)

    