from python_code import Excel_BooleanValue
from python_code import Excel_Data

def test_Excel_BooleanValue___init__():
    assert Excel_BooleanValue.__init__(Excel_BooleanValue('', ValueType=Excel_Data()), '', ValueType=Excel_Data()) == None


from python_code import Data
from python_code import Excel_Cell
from python_code import Row

def test_Excel_Cell___init__():
    assert Excel_Cell.__init__(Excel_Cell('', '', '', '', '', d_cell=Data(), r_cells=Row()), '', '', '', '', '', d_cell=Data(), r_cells=Row()) == None


from python_code import Excel_ColOrRowElement

def test_Excel_ColOrRowElement___init__():
    assert Excel_ColOrRowElement.__init__(Excel_ColOrRowElement('', '\x00'), '\x00\x00', '') == None


from python_code import Excel_Column
from python_code import Table

def test_Excel_Column___init__():
    assert Excel_Column.__init__(Excel_Column('', '\x00', t_cols=Table()), '\x00\x00', '', t_cols=Table()) == None


from python_code import Excel_DateTimeType

def test_Excel_DateTimeType___init__():
    assert Excel_DateTimeType.__init__(Excel_DateTimeType('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import Excel_Data
from python_code import Excel_NumberValue

def test_Excel_NumberValue___init__():
    assert Excel_NumberValue.__init__(Excel_NumberValue('', ValueType=Excel_Data()), '', ValueType=Excel_Data()) == None


from python_code import Excel_Row
from python_code import Table

def test_Excel_Row___init__():
    assert Excel_Row.__init__(Excel_Row('\x00\x00', '', t_rows=Table(), c_row=set()), '', '', t_rows=Table(), c_row=set()) == None


from python_code import Excel_Data
from python_code import Excel_StringValue

def test_Excel_StringValue___init__():
    assert Excel_StringValue.__init__(Excel_StringValue('', ValueType=Excel_Data()), '', ValueType=Excel_Data()) == None


from python_code import Excel_TableElement

def test_Excel_TableElement___init__():
    assert Excel_TableElement.__init__(Excel_TableElement(''), '') == None


from python_code import Excel_Worksheet
from python_code import Table
from python_code import Workbook

def test_Excel_Worksheet___init__():
    assert Excel_Worksheet.__init__(Excel_Worksheet('', wb_worksheets=Workbook(), t_worksheet=Table()), '', wb_worksheets=Workbook(), t_worksheet=Table()) == None

