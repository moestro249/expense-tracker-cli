from main import add_expense, total, total_by_category, Expense,save_expenses,load_expenses,delete_expense,filter_by_category,filter_by_period, is_valid_date

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

def test_delete_expense():
    e1 = Expense(101, "еда", "2026-10-07", "обед")
    e2= Expense(102, "еда", "2026-10-07", "обед")
    e3 = Expense(103, "еда", "2026-10-07", "обед")
    expenses=[e1,e2,e3]
    result = delete_expense(expenses,0)
    
    assert expenses == [e2,e3]
    assert result is True
    
def test_delete_out_index():
    e1 = Expense(101, "еда", "2026-10-07", "обед")
    e2= Expense(102, "еда", "2026-10-07", "обед")
    expenses=[e1,e2]
    
    result1 = delete_expense(expenses,-1)
    result2 = delete_expense(expenses, 5)
    
    assert result1 is False
    assert result2 is False
    assert expenses == [e1, e2]

    
    
    
def test_filter_by_category():
    a = Expense(100, "еда", "2026-10-07")
    b = Expense(80, "транспорт", "2026-10-07")
    c = Expense(50, "еда", "2026-10-08")
    expenses = [a,b,c]
    
    assert filter_by_category(expenses, 'еда') == [a,c]

def test_filter_by_category_missing():
    a = Expense(100, "еда", "2026-10-07")
    b = Expense(80, "транспорт", "2026-10-07")
    c = Expense(50, "еда", "2026-10-08")
    expenses = [a,b,c]
    
    assert filter_by_category(expenses,"кино") == []
    
def test_filter_by_period():
    e1 = Expense(101, "еда", "2026-10-07", "обед")
    e2= Expense(102, "еда", "2026-10-08", "обед")
    e3 = Expense(103, "еда", "2026-10-09", "обед")
    expenses=[e1,e2,e3]
    
    assert filter_by_period(expenses,"2026-10-07","2026-10-09") == [e1,e2,e3]
    assert filter_by_period(expenses,"2026-10-07","2026-10-08") == [e1,e2]
    assert filter_by_period(expenses,"2026-10-08","2026-10-09") == [e2,e3]
    assert e3 not in filter_by_period(expenses,"2026-10-07","2026-10-08")
    assert filter_by_period(expenses,"2026-10-10","2026-10-11") == []

def test_is_valid_date_ok():
    assert is_valid_date("2026-10-07") is True

def test_is_valid_date_no_leading_zero():
    assert is_valid_date("2026-10-7") is False

def test_is_valid_date_bad_month():
    assert is_valid_date("2026-13-01") is False

def test_is_valid_date_garbage():
    assert is_valid_date("abc") is False
    assert is_valid_date("") is False