import FreeSimpleGUI as sg
import datetime
from classes import transaction, category
from project_logic import date_handler
from archive_manager import generate_csv_report


def main_gui(manager, transaction_data_base):
  window = build_main_window(manager)
  window.maximize()

  while True:
    event, gui_values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    if event == "Add a new category":
        create_category_gui(event, manager)
    elif event == "Add a new Transaction":
        handle_add_transaction(window, manager)
    elif event in ("Export to CSV", "Generate CSV report"):
        handle_generate_csv(transaction_data_base)
    elif event == "Filter":
        handle_filter(window, gui_values, manager)
    elif event == "Clear Filter":
        handle_clear_filter(window, manager)

  window.close()


def add_transaction_gui(event, manager):
  if event != "Add a new Transaction":
    return None

  window = build_transaction_window()
  new_transaction = None

  while True:
    ev, values = window.read()
    if ev in (sg.WIN_CLOSED, "Cancel"):
        break

    if ev == "type":
      t_type = values["type"]
      categories = get_categories_by_type(manager, t_type)
      window["category"].update(values=categories)

    if ev == "Accept":
      try:
        title, category, t_type, amount, quantity, formatted_date, selected_obj = validate_transaction_inputs(values, manager)
        new_transaction = create_transaction_object(title, category, t_type, amount, quantity, formatted_date, selected_obj)
        break
      except ValueError as e:
        sg.popup_error(str(e))
        continue

  window.close()
  return new_transaction


def create_category_gui(event, manager):
  if event != "Add a new category":
    return None

  window = build_category_window()
  new_category = None

  while True:
    ev, values = window.read()
    if ev in (sg.WIN_CLOSED, "Cancel"):
      break
    if ev == "Accept":
      try:
        new_category, category_color, selection = validate_category_inputs(values)
        manager.add_category(new_category, category_color, selection)
        sg.popup(f"New {selection.lower()} category added")
        window["new_category"].update("")
        window["category_list"].update("")
        window["color_input"].update("")
      except ValueError as e:
        sg.popup_error(str(e))
        continue

  window.close()
  return new_category


def build_main_window(manager):
  layout = [
    [sg.Text("Welcome to your personal finance manager", font=("Helvetica", 20))],
    [sg.Button("Add a new category"), sg.Button("Add a new Transaction"),
     sg.Button("View Expenses"), sg.Button("View Incomes"),
     sg.Button("Generate CSV report"), sg.Button("Exit")],
    [sg.Text(f"Account balance: ${manager.calculate_balance()}",
             key="account_balance", font=("Helvetica", 18, "bold"))],
    [sg.Text("Insert start date"), sg.Input("", key="start_date"),
     sg.Text("Insert end date"), sg.Input("", key="end_date"),
     sg.Button("Filter"), sg.Button("Clear Filter")],
    [sg.Frame("Summary of transactions",
      [[sg.Table(values=manager.update_table_values_combined(),
                 headings=["Title", "Category", "Amount", "Quantity", "Date", "Total", "Type", "Color"],
                 expand_x=True, expand_y=True,
                 auto_size_columns=True, justification="center",
                 key="summary_transactions")]],
      expand_x=True, expand_y=True)]
  ]
  return sg.Window("Personal Finance Manager", layout, resizable=True, finalize=True)


def handle_add_transaction(window, manager):
  try:
    manager.validate_categories()
    transaction_obj = add_transaction_gui("Add a new Transaction", manager)
    if transaction_obj:
      updated_values = manager.add_transaction(
          transaction_obj.title, transaction_obj.category,
          transaction_obj.transaction_type, transaction_obj.amount,
          transaction_obj.quantity, transaction_obj.transaction_date
      )
      window["summary_transactions"].update(values=updated_values)
      window["account_balance"].update(f"Account balance ${manager.calculate_balance()}")
  except ValueError as e:
    sg.popup_error("Incorrect information entered.")


def handle_generate_csv(transaction_data_base):
  try:
    output_path = "report_all_transactions.csv"
    generate_csv_report.export_all_transactions_report(
        output_path,
        transaction_data_base.get_expense(),
        transaction_data_base.get_income()
    )
    sg.popup(f"CSV report exported to {output_path}")
  except ValueError as e:
    sg.popup_error(str(e))
  except Exception:
    sg.popup_error("Unexpected error occurred while exporting the report.")



def handle_filter(window, gui_values, manager):
  try:
      if not gui_values["start_date"] or not gui_values["end_date"]:
          sg.popup_error("Please enter both start and end date")
          return
      if not window["summary_transactions"].Values:
          sg.popup_error("The table is empty")
          return
      start_date = gui_values["start_date"].strip()
      end_date = gui_values["end_date"].strip()
      formatted_start, formatted_end = manager.check_correct_filtered_dates(start_date, end_date)
      if not formatted_start or not formatted_end:
          sg.popup_error("Invalid date format. Please use DD/MM/YYYY.")
          return
      filtered_data = manager.filter_transactions(start_date, end_date)
      table_values = manager.update_table_values_combined(filtered_data)
      window["summary_transactions"].update(values=table_values)
  except (ValueError, TypeError):
      sg.popup_error("Error: the dates entered are invalid. Please use DD/MM/YYYY.")
  except Exception:
        sg.popup_error("An unexpected error occurred while filtering. Please try again.")


def handle_clear_filter(window, manager):
  table_values = manager.update_table_values_combined()
  window["summary_transactions"].update(values=table_values)
  window["start_date"].update("")
  window["end_date"].update("")


def build_transaction_window():
  layout_transaction = [
      [sg.Text("Add new transaction", font=("Helvetica", 20, "bold"))],
      [sg.Text("Title:"), sg.Input("", key="title")],
      [sg.Text("Type:"), sg.Combo(values=["Income", "Expense"], key="type", enable_events=True, readonly=True)],
      [sg.Text("Category:"), sg.Combo(values=[], key="category", readonly=True)],
      [sg.Text("Amount:"), sg.Input("", key="amount")],
      [sg.Text("Quantity:"), sg.Input("", key="quantity")],
      [sg.Text("Date:"), sg.Input("", key="date")],
      [sg.Button("Cancel"), sg.Button("Accept")]
  ]
  return sg.Window("New Transaction", layout_transaction)

def validate_transaction_inputs(values, manager):
  title = values["title"].strip()
  category = values["category"].strip()
  t_type = values["type"].strip()
  amount = values["amount"].strip()
  quantity = values["quantity"].strip()
  date_str = values["date"].strip()

  if not all([title, category, amount, quantity, date_str]):
      raise ValueError("All fields are obligatory")
  
  if float(amount) < 0 and int(quantity) < 0:
      raise ValueError("Amount and quantity cannot both be negative")
  
  formatted_date = date_handler.format_date(date_str)
  if not formatted_date:
      raise ValueError("Date format is incorrect or invalid")
  
  if not date_handler.date_check(formatted_date):
      raise ValueError("Date cannot be in the future")
  
  selected_obj = manager.get_category_name(category)
  if not selected_obj:
      raise ValueError("Category not found")
  
  return title, category, t_type, amount, quantity, formatted_date, selected_obj


def create_transaction_object(title, category, t_type, amount, quantity, formatted_date, selected_obj):
  return transaction.Transaction(
      title,
      selected_obj.category_type,
      amount,
      quantity,
      formatted_date,
      t_type,
      getattr(selected_obj, "color", "")
  )


def get_categories_by_type(manager, t_type):
  categories = [c.category_type for c in manager.get_categories(t_type)]
  if not categories:
    sg.popup_error(f"No {t_type.lower()} categories available, please create one first.")
  return categories



def build_category_window():
  layout = [
    [sg.Text("Select transaction type:"), sg.Combo(values=["Income", "Expense"], key="category_list", readonly=True)],
    [sg.Text("Enter the new category"), sg.Input("", key="new_category")],
    [sg.Text("Color:"), sg.ColorChooserButton("Select a color", target="color_input")],
    [sg.Text("Selected:"), sg.Input("", key="color_input", readonly=True, text_color="black")],
    [sg.Button("Cancel"), sg.Button("Accept")]
  ]
  return sg.Window("New Category", layout)


def validate_category_inputs(values):
  new_category = values["new_category"].strip()
  category_color = values["color_input"]
  selection = values["category_list"]

  if not new_category:
    raise ValueError("New category field is obligatory")
  if not selection:
    raise ValueError("You must select Income or Expense")

  return new_category, category_color, selection
