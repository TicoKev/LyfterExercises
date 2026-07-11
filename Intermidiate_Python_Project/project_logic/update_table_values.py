from project_logic.get_category_properties import get_category_color

def update_table_values(transaction_data, categories):
  table_values = []
  for t in transaction_data:
    color = get_category_color(categories, t.category)
    table_values.append([t.title, t.category, t.amount, t.quantity, t.transaction_date, t.total, color])
  return table_values
