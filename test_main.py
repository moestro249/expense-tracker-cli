from main import add_expense, total, total_by_category, Expense,save_expenses,load_expenses

def test_total():
    expenses = [
        Expense(250, "еда", "2026-10-07"),
        Expense(80, "транспорт", "2026-10-07"),
    ]
    assert total(expenses)==330
    
def test_total_empty():
    expenses=[]
    assert total(expenses)==0
    
def test_total_by_category():
    expenses = [
                Expense(250, "еда", "2026-10-07"),
                Expense(80, "транспорт", "2026-10-07"),
                Expense(80, "еда", "2026-10-07")
            ]
    
    assert total_by_category(expenses)=={"еда": 330, "транспорт": 80}
        
def test_total_by_category_empty():
    expenses=[]
    
    assert total_by_category(expenses)=={}
    
def test_add_expense():
    e = Expense(100, "еда", "2026-10-07")
    expenses=[]
    add_expense(expenses, e)
    
    assert len(expenses)==1
    assert expenses[0] is e
    
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
    
def test_missing_load_expenses(tmp_path):
    assert load_expenses(tmp_path / 'no.json')==[]
    