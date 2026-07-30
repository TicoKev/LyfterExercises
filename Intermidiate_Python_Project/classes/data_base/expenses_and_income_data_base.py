class Transactions_Data_Base():

  def __init__(self):
    self._income_data_base = []
    self._expense_data_base = []


  def add_transaction(self, transaction):
    if transaction.transaction_type == "Income":
      self._income_data.append(transaction)
    elif transaction.transaction_type == "Expense":
      self._expense_data.append(transaction)
    else:
      raise ValueError("Unknown transaction type")
    return self.get_all_transactions()


  def set_expense(self, expenses):
    self._expense_data = expenses


  def set_income(self, incomes):
    self._income_data = incomes

  def get_income(self):
    return list(self._income_data)

  
  def get_expense(self):
    return list(self._expense_data)


  def get_all_transactions(self):
    return self._income_data + self._expense_data