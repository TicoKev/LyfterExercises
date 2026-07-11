import FreeSimpleGUI as sg
import datetime
from classes import transaction, category
from project_logic import calculate_account_balance, get_total_balances, date_handler, filter_transaction, update_table_values, traverse_category_list
from project_logic import get_category_properties
from archive_manager import data, generate_csv_report


def main_gui(expenses_list, income_list, expense_categories, income_categories):
  
  layout = [
    [sg.Text("Welcome to your personal finance manager", font=("Helvetica", 20))],
    [sg.Button("Expenses", pad=(15, 10)), sg.Button("Income", pad=(15, 10)), sg.Button("Generate CSV report", pad=(15, 10)), 
     sg.Button("Add a new category", pad=(15,10)), sg.Button("Exit", pad=(15, 10))],
    [sg.Text(f"Account balance: ${calculate_account_balance.calculate_account_balance(get_total_balances.get_total_income(income_list), get_total_balances.get_total_expense(expenses_list))}",
      key="account_balance",
      font=(18)
    )],
    [
      sg.Column([
        [sg.Frame("Summary of expenses", [[sg.Text(f"Total: ${get_total_balances.get_total_expense(expenses_list)}", font=(14), key="summary_expenses")]], size=(350, 250), expand_x=True, expand_y=True, font=(14))],
        [sg.Frame("Summary of income", [[sg.Text(f"Total: ${get_total_balances.get_total_income(income_list)}", font=(14), key="summary_income")]], size=(350, 250), expand_x=True, expand_y=True, font=(14))],
      ], justification="center")
    ],
  ]
  window = sg.Window("Personal Finance Manager", layout, resizable=True, finalize=True)
  window.maximize()
  
  while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
      break
    
    create_category_gui(event, expense_categories, income_categories)
    expense_amount = expense_gui(event,expenses_list, expense_categories)
    income_amount = income_gui(event, income_list, income_categories)
    total_balance = calculate_account_balance.calculate_account_balance(income_amount, expense_amount)
    
    window["account_balance"].update(f"Account balance ${total_balance}")
    window["summary_expenses"].update(f"Total: ${expense_amount}")
    window["summary_income"].update(f"Total: ${income_amount}")

    if event == "Export to CSV" or event == "Generate CSV report":
      try:
        output_path = "report_all_transactions.csv"
        generate_csv_report.export_all_transactions_report(
            output_path,
            expenses_list.expense_data,
            income_list.income_data
        )
        sg.popup(f"CSV report exported to {output_path}")
      except Exception as e:
        sg.popup_error(f"Error exporting CSV report: {e}")

  window.close()


def expense_gui(event, expenses_list, expense_categories):  
  if event == "Expenses":
    layout_expense = [
      [sg.Button("New Expense")],
      [sg.Text("Insert start date"), sg.Input("", key="start_date"), sg.Text("Insert end date"), sg.Input("", key="end_date"), sg.Button("Filter"), sg.Button("Clear Filter")],
      [
        sg.Frame("Expenses",
          [
            [sg.Table(
              values=update_table_values.update_table_values(expenses_list.expense_data, expense_categories),
              headings=["Title", "Category", "Amount", "Quantity", "Date", "Total", "Color"],
              key="expenses_table",
              expand_x=True,
              expand_y=True,
              auto_size_columns=True,
              justification="center"
            )],
            [sg.Text(f"Total spent: ${get_total_balances.get_total_expense(expenses_list)}", key="total_spent", font=("Helvetica", 14, "bold"))]
          ],
            expand_x=True,
            expand_y=True,
            font=(14),
            key="expense_frame"
        )
      ]
    ]
    window_expenses = sg.Window("Expenses", layout_expense, resizable=True, finalize=True)
    window_expenses.maximize()

    while True:
      expense_event, expense_values = window_expenses.read()
      if expense_event == sg.WIN_CLOSED:
        break
      
      if expense_event == "New Expense":
        try:
          expense = add_transaction_gui(expense_event, "New Expense", expense_categories, "expense")

          if expense:
            expenses_list.add_to_expense_data_base(expense)
            data.save_transactions("transactions_expenses.csv", expenses_list.expense_data)

            total_spent = get_total_balances.get_total_expense(expenses_list)
            table_values = update_table_values.update_table_values(expenses_list.expense_data, expense_categories)

            window_expenses["expenses_table"].update(values=table_values)
            window_expenses["total_spent"].update(f"Total spent: ${total_spent}")
        
        except Exception as error:
          sg.popup_error(f"Error ocurred while adding the expense, {error}")

      if expense_event == "Filter":
        if expense_values["start_date"] == "" or expense_values["end_date"] == "":
          sg.popup_error("Please enter both start and end date")
        else:
          if not window_expenses["expenses_table"].Values:
            sg.popup_error("The table is empty")   
          else:
            try:
              start_date = expense_values["start_date"].strip()
              end_date = expense_values["end_date"].strip()
              formatted_start_date = date_handler.format_date(start_date)
              formatted_end_date = date_handler.format_date(end_date)
              filtered_data = filter_transaction.filter_transaction(formatted_start_date, formatted_end_date, expenses_list.expense_data)
              
              table_values = update_table_values.update_table_values(filtered_data, expense_categories)
              window_expenses["expenses_table"].update(values=table_values)
            except ValueError as error:
              sg.popup_error(error)
      
      if expense_event == "Clear Filter":
        table_values = update_table_values.update_table_values(expenses_list.expense_data, expense_categories)
        window_expenses["expenses_table"].update(values=table_values)
        window_expenses["start_date"].update("")
        window_expenses["end_date"].update("")
    
    window_expenses.close()
  
  return get_total_balances.get_total_expense(expenses_list)


def income_gui(event, income_list, income_categories):

  if event == "Income":
    layout_income = [
      [sg.Button("New Income")],
      [sg.Text("Insert start date"), sg.Input("", key="start_date"), sg.Text("Insert end date"), sg.Input("", key="end_date"), sg.Button("Filter"), sg.Button("Clear Filter")],
      [
        sg.Frame("Income",
          [
            [sg.Table(
              values=update_table_values.update_table_values(income_list.income_data, income_categories),
              headings=["Title","Category", "Amount", "Quantity", "Date", "Total", "Color"],
              key="income_table",
              expand_x=True,
              expand_y=True,
              auto_size_columns=True,
              justification="center"
            )],
            [sg.Text(f"Total Income: ${get_total_balances.get_total_income(income_list)}", key="total_income", font=("Helvetica", 14, "bold"))]
          ],
            expand_x=True,
            expand_y=True,
            font=(14),
            key="income_frame"
        )
      ]
    ]
    window_income = sg.Window("Income", layout_income, resizable=True, finalize=True)
    window_income.maximize()

    while True:
      income_event, income_values = window_income.read()
      
      if income_event == sg.WIN_CLOSED:
        break
      
      if income_event == "New Income":
        try:
          income = add_transaction_gui(income_event, "New Income", income_categories, "income")
          
          if income:
            income_list.add_to_income_data_base(income)
            data.save_transactions("transactions_income.csv", income_list.income_data)

            total_income = get_total_balances.get_total_income(income_list)
            table_values = update_table_values.update_table_values(income_list.income_data, income_categories)
            window_income["income_table"].update(values=table_values)
            window_income["total_income"].update(f"Total income: ${total_income}")
        except Exception as error:
          sg.popup_error(f"Error ocurred while adding the income, {error}")
      
      if income_event == "Filter":
        if income_values["start_date"] == "" or income_values["end_date"] == "":
          sg.popup_error("Please enter both start and end date")
        else:
          if not window_income["income_table"].Values:
            sg.popup_error("The table is empty")
          else:
            try:
              start_date = income_values["start_date"].strip()
              end_date = income_values["end_date"].strip()
              formatted_start_date = date_handler.format_date(start_date)
              formatted_end_date = date_handler.format_date(end_date)
              filtered_data = filter_transaction.filter_transaction(formatted_start_date, formatted_end_date, income_list.income_data)
              table_values = update_table_values.update_table_values(filtered_data, income_categories)
              window_income["income_table"].update(values=table_values)
            except ValueError as error:
              sg.popup_error(error)

      if income_event == "Clear Filter":
        table_values = update_table_values.update_table_values(income_list.income_data, income_categories)
        window_income["income_table"].update(values=table_values)
        window_income["start_date"].update("")
        window_income["end_date"].update("")
    
    window_income.close()

  return get_total_balances.get_total_income(income_list)


def add_transaction_gui(event, title, categories, transaction_type):
  new_transaction = None

  if event == f"New {transaction_type.capitalize()}":
    layout_new_expense = [
      [sg.Column([
        [sg.Text(f"Add {transaction_type.capitalize()} ", font=("Helvetica", 20, "bold"))],
        [sg.Text("Title:", size=(10, 1)), sg.Input("", size=(20, 1), key="title")],
        [sg.Text("Category:", size=(10, 1)), sg.Combo(traverse_category_list.traverse_category_list(categories),size=(18, 1), readonly=True, key="category")],
        [sg.Text("Amount:", size=(10,1)), sg.Input("", size=(20, 1), key="amount")],
        [sg.Text("Quantity:", size=(10,1)), sg.Input("", size=(20, 1), key="quantity")],
        [sg.Text("Date:", size=(10,1)), sg.Input("", size=(20, 1), key="date")],
        [sg.Button("Cancel", size=(10,1)), sg.Button("Accept", size=(10,1))],
        ], element_justification="center")]
    ]
    window_new_expense = sg.Window(title, layout_new_expense)

    while True:
      new_expense_event, new_expense_values = window_new_expense.read()
      if new_expense_event == sg.WIN_CLOSED or new_expense_event == "Cancel":
        break

      if new_expense_event == "Accept":
        transaction_title = new_expense_values["title"].strip()
        category = new_expense_values["category"].strip()
        amount = new_expense_values["amount"].strip()
        quantity = new_expense_values["quantity"].strip()
        transaction_date = new_expense_values["date"].strip()
        
        formatted_date = date_handler.format_date(transaction_date)
        if formatted_date is None:
          sg.popup_error("Error, date format is incorrect or the date is invalid")
          continue

        if not all ([transaction_title, category, amount, quantity, transaction_date]):
          sg.popup_error("Error, all fields are obligatory")
      
        try:
          formatted_date = date_handler.format_date(transaction_date)

          if not isinstance(formatted_date, datetime.datetime):
            sg.popup_error("Error, date format is incorrect or the date is invalid")
            continue
          
          selected_obj = get_category_properties.get_category_by_name(categories, category)
          new_transaction = transaction.Transaction(transaction_title, selected_obj.category_type, amount, quantity, transaction_date, transaction_type, getattr(selected_obj, "color", ""))
          new_transaction.type = category

          break
        
        except ValueError as error:
          sg.popup_error(error)
    window_new_expense.close()

  return new_transaction


def create_category_gui(event, expense_categories, income_categories):
  new_category = None

  if event == "Add a new category":
    layout = [
      [sg.Text("Select transaction type:"), sg.Combo(values=["Income", "Expense"], key="category_list")],
      [sg.Text("Enter the new category"), sg.Input("", key="new_category")],
      [sg.Text("Color:", size=(10,1)), sg.ColorChooserButton("Select a color", target="color_input", size=(17, 1))],
      [sg.Text("Selected:", size=(10,1)), sg.Input("", key="color_input", readonly=True, size=(20,1), text_color="black")],
      [sg.Button("Cancel"), sg.Button("Accept")]
    ]
    category_window = sg.Window("New Category", layout)

    while True:
      event_category, values = category_window.read()

      if event_category == sg.WIN_CLOSED or event_category == "Cancel":
        break

      if event_category == "Accept":
        new_category = values["new_category"].strip()
        category_color = values["color_input"]
        selection = values["category_list"]

        if not new_category:
          sg.popup_error("Error, new category field is obligatory")
          continue
        if not selection:
          sg.popup_error("Error, you must select Income or Expense")
          continue
        
        if selection == "Income":
          new_category_option = category.Category(new_category, category_color)
          income_categories.append(new_category_option)
          data.save_categories("categories_income.csv", income_categories)
          category_window["new_category"].update("")
          sg.popup("New income category added")
          
        elif selection == "Expense":
          new_category_option = category.Category(new_category, category_color)
          expense_categories.append(new_category_option)  
          data.save_categories("categories_expenses.csv", expense_categories) 
          category_window["new_category"].update("")
          sg.popup("New expense category added")

    category_window.close()
  return new_category

