import csv
from types import SimpleNamespace
import pytest
from archive_manager import data as data_mod
from archive_manager import generate_csv_report as gen_mod
from classes.data_base.expenses_and_income_data_base import ExpenseDataBase, IncomeDataBase
from project_logic import filter_transaction
from datetime import datetime
from project_logic import calculate_account_balance
from project_logic import date_handler

def make_transactions(title="T", category="C", amount=10, quantity=1, date="01/01/2025", tx_type="Expense", color="#000000"):
    return SimpleNamespace(
        title=title,
        category=category,
        amount=str(amount),
        quantity=str(quantity),
        transaction_date=date,
        transaction_type=tx_type,
        color=color,
        total=float(amount) * int(quantity)
    )


def test_save_transactions_writes_color_header(tmp_path):
    transactions = [make_transactions("A", "Food", 5, 1, "01/01/2025", "Expense", "#ABCDEF")]
    out = tmp_path / "tx.csv"
    data_mod.save_transactions(str(out), transactions)
    with open(out, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
    assert "Color" in header


def test_load_transactions_returns_list_and_preserves_color(tmp_path):
    transactions = [
        make_transactions("A", "Food", 5, 1, "01/01/2025", "Expense", "#ABCDEF"),
        make_transactions("B", "Work", 10, 1, "02/01/2025", "Income", "#123456")
    ]
    out = tmp_path / "tx2.csv"
    data_mod.save_transactions(str(out), transactions)
    loaded = data_mod.load_transactions(str(out))
    assert isinstance(loaded, list)
    colors = [getattr(t, "color", None) for t in loaded]
    assert "#ABCDEF" in colors or "#123456" in colors


def test_export_writes_header_only(tmp_path):
    exporter = gen_mod if gen_mod is not None and hasattr(gen_mod, "export_all_transactions_report") else data_mod
    out = tmp_path / "report.csv"
    exporter.export_all_transactions_report(str(out), [], [])
    assert out.exists()
    content = out.read_text(encoding="utf-8")
    assert "Date,Title,Amount,Category,Type" in content


def test_filter_transaction_with_valid_dates_returns_list():
    transactions = [
        make_transactions("A", "C", 1, 1, "01/01/2025"),
        make_transactions("B", "C", 2, 1, "05/01/2025")
    ]

    start = datetime.strptime("01/01/2025", "%d/%m/%Y")
    end = datetime.strptime("31/12/2025", "%d/%m/%Y")
    result = filter_transaction.filter_transaction(start, end, transactions)
    assert isinstance(result, list)
    assert len(result) >= 1


def test_filter_transaction_no_data_raises_valueerror():
    transactions = [
        make_transactions("A", "C", 1, 1, "01/01/2025"),
        make_transactions("B", "C", 2, 1, "05/01/2025")
    ]

    start = datetime.strptime("01/01/2026", "%d/%m/%Y")
    end = datetime.strptime("31/12/2026", "%d/%m/%Y")
    with pytest.raises(ValueError):
        filter_transaction.filter_transaction(start, end, transactions)


def test_export_with_data_writes_rows(tmp_path):
    exporter = gen_mod if gen_mod is not None and hasattr(gen_mod, "export_all_transactions_report") else data_mod
    tx = make_transactions("Salary", "Work", 1000, 1, "01/07/2025", "Income")
    out = tmp_path / "report2.csv"
    exporter.export_all_transactions_report(str(out), [tx], [])
    content = out.read_text(encoding="utf-8")
    assert "Salary" in content or "1000" in content


def test_format_date_valid_and_invalid():
    valid = "01/07/2025"
    parsed = date_handler.format_date(valid)
    assert parsed is not None
    assert isinstance(parsed, datetime)
    invalid = "31/02/2025"
    assert date_handler.format_date(invalid) is None


def test_calculate_account_balance_numeric_and_non_numeric():
  assert float(calculate_account_balance.calculate_account_balance(150, 50)) == pytest.approx(100.0)
  bad = calculate_account_balance.calculate_account_balance("not-a-number", None)
  assert isinstance(bad, float)
  assert bad == pytest.approx(0.0)