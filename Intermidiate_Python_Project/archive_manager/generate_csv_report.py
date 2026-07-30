import csv
import os
from datetime import datetime

def export_all_transactions_report(filename, expenses, incomes):
  all_transactions = []
  
  for t in incomes:
    all_transactions.append({
      "date": t.transaction_date,
      "title": t.title,
      "amount": float(t.amount),
      "category": getattr(t, "type", t.category),
      "type": "Income"
  })
  for t in expenses:
    all_transactions.append({
      "date": t.transaction_date,
      "title": t.title,
      "amount": float(t.amount),
      "category": getattr(t, "type", t.category),
      "type": "Expense"
    })

  def try_parse_date(s):
    for fmt in ("%d/%m/%Y", "%d/%m/%y", "%Y-%m-%d"):
      try:
        return datetime.strptime(s, fmt)
      except Exception:
        continue
    return None

  all_transactions_sorted = sorted(all_transactions, key=lambda x: (try_parse_date(x["date"]) or datetime.min))

  total_income = sum(x["amount"] for x in all_transactions_sorted if x["type"] == "Income")
  total_expenses = sum(abs(x["amount"]) for x in all_transactions_sorted if x["type"] == "Expense")
  net_balance = total_income - total_expenses

  os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)

  with open(filename, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "Title", "Amount", "Category", "Type"])
    for row in all_transactions_sorted:
      writer.writerow([row["date"], row["title"], row["amount"], row["category"], row["type"]])
      
    writer.writerow([])
    writer.writerow(["Totals:"])
    writer.writerow([f"Income: {total_income}"])
    writer.writerow([f"Expenses: {total_expenses}"])
    writer.writerow([f"Net Balance: {net_balance}"])

  return filename
