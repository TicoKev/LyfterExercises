from classes.transaction import Transaction

class ExpenseDataBase():
  def __init__(self):
    self.expense_data = []

  def add_to_expense_data_base(self, expense: Transaction):
    self.expense_data.append(expense)
    return self.expense_data

class IncomeDataBase():
  def __init__(self):
    self.income_data = []

  def add_to_income_data_base(self, income: Transaction):
    self.income_data.append(income)
    return self.income_data