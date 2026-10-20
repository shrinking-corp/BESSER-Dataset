from python_code import SpreadsheetMLSimplified_BooleanValue
from python_code import SpreadsheetMLSimplified_Data

def test_SpreadsheetMLSimplified_BooleanValue___init__():
    assert SpreadsheetMLSimplified_BooleanValue.__init__(SpreadsheetMLSimplified_BooleanValue('', ValueType=SpreadsheetMLSimplified_Data()), '', ValueType=SpreadsheetMLSimplified_Data()) == None


from python_code import Data
from python_code import Row
from python_code import SpreadsheetMLSimplified_Cell

def test_SpreadsheetMLSimplified_Cell___init__():
    assert SpreadsheetMLSimplified_Cell.__init__(SpreadsheetMLSimplified_Cell('', '', '', '', '', d_cell=Data(), r_cells=Row()), '', '', '', '', '', d_cell=Data(), r_cells=Row()) == None


from python_code import SpreadsheetMLSimplified_ColOrRowElement

def test_SpreadsheetMLSimplified_ColOrRowElement___init__():
    assert SpreadsheetMLSimplified_ColOrRowElement.__init__(SpreadsheetMLSimplified_ColOrRowElement('', '\x00'), '\x00\x00', '') == None


from python_code import SpreadsheetMLSimplified_Column
from python_code import Table

def test_SpreadsheetMLSimplified_Column___init__():
    assert SpreadsheetMLSimplified_Column.__init__(SpreadsheetMLSimplified_Column('', '\x00', t_cols=Table()), '\x00\x00', '', t_cols=Table()) == None


from python_code import SpreadsheetMLSimplified_DateTimeType

def test_SpreadsheetMLSimplified_DateTimeType___init__():
    assert SpreadsheetMLSimplified_DateTimeType.__init__(SpreadsheetMLSimplified_DateTimeType('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import SpreadsheetMLSimplified_Data
from python_code import SpreadsheetMLSimplified_NumberValue

def test_SpreadsheetMLSimplified_NumberValue___init__():
    assert SpreadsheetMLSimplified_NumberValue.__init__(SpreadsheetMLSimplified_NumberValue('', ValueType=SpreadsheetMLSimplified_Data()), '', ValueType=SpreadsheetMLSimplified_Data()) == None


from python_code import SpreadsheetMLSimplified_Row
from python_code import Table

def test_SpreadsheetMLSimplified_Row___init__():
    assert SpreadsheetMLSimplified_Row.__init__(SpreadsheetMLSimplified_Row('\x00\x00', '', t_rows=Table(), c_row=set()), '', '', t_rows=Table(), c_row=set()) == None


from python_code import SpreadsheetMLSimplified_Data
from python_code import SpreadsheetMLSimplified_StringValue

def test_SpreadsheetMLSimplified_StringValue___init__():
    assert SpreadsheetMLSimplified_StringValue.__init__(SpreadsheetMLSimplified_StringValue('', ValueType=SpreadsheetMLSimplified_Data()), '', ValueType=SpreadsheetMLSimplified_Data()) == None


from python_code import SpreadsheetMLSimplified_TableElement

def test_SpreadsheetMLSimplified_TableElement___init__():
    assert SpreadsheetMLSimplified_TableElement.__init__(SpreadsheetMLSimplified_TableElement(''), '') == None


from python_code import SpreadsheetMLSimplified_Worksheet
from python_code import Table
from python_code import Workbook

def test_SpreadsheetMLSimplified_Worksheet___init__():
    assert SpreadsheetMLSimplified_Worksheet.__init__(SpreadsheetMLSimplified_Worksheet('', wb_worksheets=Workbook(), t_worksheet=Table()), '', wb_worksheets=Workbook(), t_worksheet=Table()) == None

