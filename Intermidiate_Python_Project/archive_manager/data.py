import csv
import os
from classes.category import Category
from classes.transaction import Transaction

def save_transactions(filename, transactions):
  os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
  with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Category", "Amount", "Quantity", "Date", "Total", "Type", "Color"])
    for t in transactions:
      writer.writerow([
        getattr(t, "title", ""),
        getattr(t, "category", ""),
        getattr(t, "amount", ""),
        getattr(t, "quantity", ""),
        getattr(t, "transaction_date", ""),
        getattr(t, "total", ""),
        getattr(t, "transaction_type", ""),
        getattr(t, "color", "")
      ])


def load_transactions(filename):
  if not os.path.exists(filename):
    return []
  transactions = []
  with open(filename, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
      title = row.get("Title", "")
      category = row.get("Category", "")
      amount = row.get("Amount", "")
      quantity = row.get("Quantity", "")
      date = row.get("Date", "")
      tx_type = row.get("Type", "")
      color = row.get("Color", "")
      try:
        t = Transaction(title, category, amount, quantity, date, tx_type, color)
      except TypeError:
        from types import SimpleNamespace
        t = SimpleNamespace(
            title=title,
            category=category,
            amount=amount,
            quantity=quantity,
            transaction_date=date,
            transaction_type=tx_type,
            color=color,
            total=(float(amount) * int(quantity)) if amount and quantity else 0.0
        )
            
      if not hasattr(t, "transaction_date"):
        setattr(t, "transaction_date", date)
      if not hasattr(t, "color"):
        setattr(t, "color", color)
      transactions.append(t)
  return transactions


def save_categories(filename, categories):
  with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Color"])
    for c in categories:
      writer.writerow([c.category_type, c.color])



def load_categories(filename):
  if not os.path.exists(filename):
    return []
  categories = []
  with open(filename, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
      categories.append(Category(row["Category"], row["Color"]))
  return categories
