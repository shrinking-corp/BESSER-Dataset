from python_code import project_CellText
from python_code import project_LogicalExpression

def test_project_CellText___init__():
    assert project_CellText.__init__(project_CellText('', project_CellText=project_LogicalExpression()), '', project_CellText=project_LogicalExpression()) == None


from python_code import project_Charge

def test_project_Charge___init__():
    assert project_Charge.__init__(project_Charge(0.0, '\x00\x00'), 0.0, '') == None


from python_code import project_Column
from python_code import project_ColumnAttribute
from python_code import project_Columns

def test_project_Column___init__():
    assert project_Column.__init__(project_Column('', project_Column=project_Columns(), project_Column228=project_ColumnAttribute()), '', project_Column=project_Columns(), project_Column228=project_ColumnAttribute()) == None


from python_code import project_Complete

def test_project_Complete___init__():
    assert project_Complete.__init__(project_Complete(0.0), 0.0) == None


from python_code import project_Copyright

def test_project_Copyright___init__():
    assert project_Copyright.__init__(project_Copyright(''), '') == None


from python_code import project_Credit

def test_project_Credit___init__():
    assert project_Credit.__init__(project_Credit('', '', 0.0), '', '', 0.0) == None


from python_code import project_Currency

def test_project_Currency___init__():
    assert project_Currency.__init__(project_Currency(''), '') == None


from python_code import project_DailyWorkingHours

def test_project_DailyWorkingHours___init__():
    assert project_DailyWorkingHours.__init__(project_DailyWorkingHours(0.0), 0.0) == None


from python_code import project_Definitions

def test_project_Definitions___init__():
    assert project_Definitions.__init__(project_Definitions(False, False), False, False) == None


from python_code import project_Defintions

def test_project_Defintions___init__():
    assert project_Defintions.__init__(project_Defintions(False, False, False, False, False), True, False, False, False, False) == None


from python_code import project_Efficiency

def test_project_Efficiency___init__():
    assert project_Efficiency.__init__(project_Efficiency(0.0), 0.0) == None


from python_code import project_Email

def test_project_Email___init__():
    assert project_Email.__init__(project_Email(''), '') == None


from python_code import project_End

def test_project_End___init__():
    assert project_End.__init__(project_End(''), '') == None


from python_code import project_EndCredit

def test_project_EndCredit___init__():
    assert project_EndCredit.__init__(project_EndCredit(0.0), 0.0) == None


from python_code import project_Export

def test_project_Export___init__():
    assert project_Export.__init__(project_Export('\x00\x00', '', project_Export=set()), '', '', project_Export=set()) == None

