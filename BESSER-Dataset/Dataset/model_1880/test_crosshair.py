from python_code import budgeting_ActualAmountEntry

def test_budgeting_ActualAmountEntry___init__():
    assert budgeting_ActualAmountEntry.__init__(budgeting_ActualAmountEntry(''), '') == None


from python_code import budgeting_BudgetAmountEntry

def test_budgeting_BudgetAmountEntry___init__():
    assert budgeting_BudgetAmountEntry.__init__(budgeting_BudgetAmountEntry(''), '') == None


from python_code import budgeting_BudgetEntry
from python_code import budgeting_BudgetFactorEntry

def test_budgeting_BudgetFactorEntry___init__():
    assert budgeting_BudgetFactorEntry.__init__(budgeting_BudgetFactorEntry(0.0, budgeting_BudgetFactorEntry=budgeting_BudgetEntry()), 0.0, budgeting_BudgetFactorEntry=budgeting_BudgetEntry()) == None


from python_code import budgeting_CardTransaction

def test_budgeting_CardTransaction___init__():
    assert budgeting_CardTransaction.__init__(budgeting_CardTransaction(0, '\x00'), 0, '\x00') == None


from python_code import budgeting_CashTransaction

def test_budgeting_CashTransaction___init__():
    assert budgeting_CashTransaction.__init__(budgeting_CashTransaction(''), '') == None


from python_code import budgeting_ExpenseCategory

def test_budgeting_ExpenseCategory___init__():
    assert budgeting_ExpenseCategory.__init__(budgeting_ExpenseCategory(''), '') == None


from python_code import budgeting_ActualTransactionEntry
from python_code import budgeting_Transaction

def test_budgeting_Transaction___init__():
    assert budgeting_Transaction.__init__(budgeting_Transaction('', budgeting_Transaction=budgeting_ActualTransactionEntry()), '', budgeting_Transaction=budgeting_ActualTransactionEntry()) == None

