import datetime
from classes import transaction, category
from project_logic import date_handler, filter_transaction, get_category_properties, get_total_balances, update_table_values 
from archive_manager import data, generate_csv_report

class Finance_Manager:
  def __init__(self, transaction_data_base):
    self.transaction_data_base = transaction_data_base
    self.expense_categories = []
    self.income_categories = []

  def validate_categories(self):
    if len(self.income_categories) == 0 and len(self.expense_categories) == 0:
      raise ValueError("No categories available, please add a category first.")

  
  def add_transaction(self, title, category_name, type, amount, quantity, formatted_date):
    formatted_date
    if not formatted_date:
      raise ValueError("Invlid format.")
    if not date_handler.date_check(formatted_date):
      raise ValueError("The date cannot be future.")
    if float(amount) < 0 and int(quantity) < 0:
      raise ValueError("Amount and quantity cannot be negative.")


    self.validate_categories()
    selected_obj = get_category_properties.get_category_by_name(
        self.expense_categories + self.income_categories, category_name
      )
    if not selected_obj:
      raise ValueError(f"Category '{category_name}' not found.")

    new_transaction = transaction.Transaction(
        title,
        selected_obj.category_type,
        amount,
        quantity,
        formatted_date,
        type,
        getattr(selected_obj, "color", "")
    )

    if type == "Expense":
      self.transaction_data_base.add_transaction(new_transaction)
      data.save_transactions("transactions_expenses.csv", self.transaction_data_base.get_expense())
    else:
      self.transaction_data_base.add_transaction(new_transaction)
      data.save_transactions("transactions_income.csv", self.transaction_data_base.get_income())

    return update_table_values.update_table_values_combined(
      self.transaction_data_base.get_expense(), 
      self.transaction_data_base.get_income(), 
      self.expense_categories + self.income_categories)


  def calculate_balance(self):
    total_income = get_total_balances.get_total_income(self.transaction_data_base.get_income())
    total_expense = get_total_balances.get_total_expense(self.transaction_data_base.get_expense())
    return total_income - total_expense


  def update_table_values(self):
    get_new_values = update_table_values.update_table_values(
      self.transaction_data_base.get_income() + self.transaction_data_base.get_expense(), 
      self.income_categories + self.expense_categories)
    return get_new_values


  def update_table_values_combined(self, expenses=None, incomes=None, categories=None):
    expenses = expenses if expenses is not None else self.transaction_data_base.get_expense()
    incomes = incomes if incomes is not None else self.transaction_data_base.get_income()
    categories = categories if categories is not None else (self.income_categories + self.expense_categories)

    return update_table_values.update_table_values_combined(expenses, incomes, categories)



  def check_correct_filtered_dates(self, start_date, end_date):
    formatted_start = date_handler.format_date(start_date)
    formatted_end = date_handler.format_date(end_date)

    return formatted_start, formatted_end


  def check_correct_date_format(self):
    return date_handler.format_date()

  def filter_transactions(self, start_date, end_date):
    formatted_start = date_handler.format_date(start_date)
    formatted_end = date_handler.format_date(end_date)
    return filter_transaction.filter_transaction(formatted_start, formatted_end, self.transaction_data_base.get_expense() + self.transaction_data_base.get_income())


  def save_categories(self, category_type):
    if category_type == "Income":
      data.save_categories("categories_income.csv", self.income_categories)
    elif category_type == "Expense":
      data.save_categories("categories_expenses.csv", self.expense_categories)
    else:
      raise ValueError("Uknown category type")


  def export_reports(self, filename="report_all_transactions.csv"):
    generate_csv_report.export_all_transactions_report(
      filename,
      self.transaction_data_base.get_expense(),
      self.transaction_data_base.get_income()
    )
    return filename


  def get_category_name(self, category_type):
    return get_category_properties.get_category_by_name(
        self.income_categories + self.expense_categories, category_type
    )

  def add_category(self, name, color, category_type):
    if category_type == "Income":
        if any(c.category_type == name for c in self.income_categories):
            raise ValueError("Income category already exists.")
        self.income_categories.append(category.Category(name, color))
        self.save_categories("Income")
    elif category_type == "Expense":
        if any(c.category_type == name for c in self.expense_categories):
            raise ValueError("Expense category already exists.")
        self.expense_categories.append(category.Category(name, color))
        self.save_categories("Expense")
    else:
        raise ValueError("Unknown category type")


def get_categories(self, category_type=None):
    if category_type == "Income":
        return self.income_categories
    elif category_type == "Expense":
        return self.expense_categories
    return self.income_categories + self.expense_categories
