from GUI.gui import main_gui
from archive_manager import data
from classes import finance_manager
from classes.data_base.expenses_and_income_data_base import Transactions_Data_Base

def main():
  transaction_data_base = Transactions_Data_Base()
  transaction_data_base.set_expense(data.load_transactions("transactions_expenses.csv")) 
  transaction_data_base.set_income(data.load_transactions("transactions_income.csv"))
  manager = finance_manager.Finance_Manager(transaction_data_base)
  manager.expense_categories = data.load_categories("categories_expenses.csv")
  manager.income_categories = data.load_categories("categories_income.csv")
  main_gui(manager, transaction_data_base)


if __name__ == "__main__":
  main()
