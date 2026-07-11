from GUI.gui import main_gui
from archive_manager import data
from classes.data_base.expenses_and_income_data_base import ExpenseDataBase, IncomeDataBase
from transaction_types.transaction_types import expense_categories, income_categories

def main():
  expenses_list = ExpenseDataBase()
  income_list= IncomeDataBase()
  expenses_list.expense_data = data.load_transactions("transactions_expenses.csv")
  income_list.income_data = data.load_transactions("transactions_income.csv")
  expense_categories[:] = data.load_categories("categories_expenses.csv")
  income_categories[:] = data.load_categories("categories_income.csv")

  main_gui(expenses_list, income_list, expense_categories, income_categories)


if __name__ == "__main__":
  main()
