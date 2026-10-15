from  storage import save_expenses, load_expenses
from models import Expense

def test_missing_load_expenses(tmp_path):
    assert load_expenses(tmp_path / 'no.json')==[]

def test_save_expenses(tmp_path):
    file = tmp_path / 'test.json'
    expenses = [Expense(100, "еда", "2026-10-07", "обед")]
    save_expenses(expenses,file)
    
    assert load_expenses(file)==expenses
    
def test_load_expenses(tmp_path):
    file = tmp_path / 'test.json'
    file.write_text(
        '[{"amount": 100, "category": "еда", "date": "2026-10-07", "comment": "обед"}]',
        encoding='utf-8'
    )
    
    assert load_expenses(file)==[Expense(100, "еда", "2026-10-07", "обед")]