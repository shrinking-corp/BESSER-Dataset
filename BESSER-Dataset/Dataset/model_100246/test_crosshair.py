from python_code import SpreadsheetMLSimplified_BooleanValue

def test_SpreadsheetMLSimplified_BooleanValue___init__():
    assert SpreadsheetMLSimplified_BooleanValue.__init__(SpreadsheetMLSimplified_BooleanValue(True), False) == None


from python_code import SpreadsheetMLSimplified_ColOrRowElement

def test_SpreadsheetMLSimplified_ColOrRowElement___init__():
    assert SpreadsheetMLSimplified_ColOrRowElement.__init__(SpreadsheetMLSimplified_ColOrRowElement(False, 0), False, 0) == None


from python_code import SpreadsheetMLSimplified_Column
from python_code import SpreadsheetMLSimplified_Table

def test_SpreadsheetMLSimplified_Column___init__():
    assert SpreadsheetMLSimplified_Column.__init__(SpreadsheetMLSimplified_Column(False, 0.0, Column=SpreadsheetMLSimplified_Table(), t_cols=SpreadsheetMLSimplified_Table()), False, 0.0, Column=SpreadsheetMLSimplified_Table(), t_cols=SpreadsheetMLSimplified_Table()) == None


from python_code import SpreadsheetMLSimplified_DateTimeType
from python_code import SpreadsheetMLSimplified_DateTimeTypeValue

def test_SpreadsheetMLSimplified_DateTimeType___init__():
    assert SpreadsheetMLSimplified_DateTimeType.__init__(SpreadsheetMLSimplified_DateTimeType(0, 0, 0, 0, 0, 0, SpreadsheetMLSimplified_DateTimeType=SpreadsheetMLSimplified_DateTimeTypeValue()), 0, 0, 0, 0, 0, 0, SpreadsheetMLSimplified_DateTimeType=SpreadsheetMLSimplified_DateTimeTypeValue()) == None


from python_code import SpreadsheetMLSimplified_NumberValue

def test_SpreadsheetMLSimplified_NumberValue___init__():
    assert SpreadsheetMLSimplified_NumberValue.__init__(SpreadsheetMLSimplified_NumberValue(0.0), 0.0) == None


from python_code import SpreadsheetMLSimplified_StringValue

def test_SpreadsheetMLSimplified_StringValue___init__():
    assert SpreadsheetMLSimplified_StringValue.__init__(SpreadsheetMLSimplified_StringValue(''), '') == None


from python_code import SpreadsheetMLSimplified_TableElement

def test_SpreadsheetMLSimplified_TableElement___init__():
    assert SpreadsheetMLSimplified_TableElement.__init__(SpreadsheetMLSimplified_TableElement(0), 0) == None


from python_code import SpreadsheetMLSimplified_Table
from python_code import SpreadsheetMLSimplified_Workbook
from python_code import SpreadsheetMLSimplified_Worksheet

def test_SpreadsheetMLSimplified_Worksheet___init__():
    assert SpreadsheetMLSimplified_Worksheet.__init__(SpreadsheetMLSimplified_Worksheet('', Worksheet=SpreadsheetMLSimplified_Workbook(), Worksheet6=SpreadsheetMLSimplified_Table(), wb_worksheets=SpreadsheetMLSimplified_Workbook(), t_worksheet=SpreadsheetMLSimplified_Table()), '', Worksheet=SpreadsheetMLSimplified_Workbook(), Worksheet6=SpreadsheetMLSimplified_Table(), wb_worksheets=SpreadsheetMLSimplified_Workbook(), t_worksheet=SpreadsheetMLSimplified_Table()) == None

