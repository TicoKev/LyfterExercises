from datetime import datetime, date

def format_date(transaction_date: str) -> date | None:
  try:
    transaction_date = transaction_date.strip()

    try:
        return datetime.strptime(transaction_date, "%d/%m/%Y").date()
    except ValueError:
        pass

    try:
        return datetime.strptime(transaction_date, "%Y-%m-%d").date()
    except ValueError:
        pass
    return None
  except Exception:
    return None


def date_check(transaction_date: date) -> bool:
  current_date = date.today()
  return transaction_date <= current_date
