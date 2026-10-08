from main import add_expense, total, total_by_category, Expense

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
    assert expenses[0]==e
    