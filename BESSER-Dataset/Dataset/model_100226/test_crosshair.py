from python_code import CustomDocumentPropertiesCollection
from python_code import SpreadsheetMLBasicDef_BooleanValue
from python_code import SpreadsheetMLBasicDef_CustomDocumentProperty
from python_code import SpreadsheetMLBasicDef_Data
from python_code import ValueType

def test_SpreadsheetMLBasicDef_BooleanValue___init__():
    assert SpreadsheetMLBasicDef_BooleanValue.__init__(SpreadsheetMLBasicDef_BooleanValue('', ValueType=SpreadsheetMLBasicDef_CustomDocumentProperty('', customDocumentProperties=CustomDocumentPropertiesCollection(), SpreadsheetMLBasicDef_CustomDocumentProperty=ValueType()), ValueType58=SpreadsheetMLBasicDef_Data()), '', ValueType=SpreadsheetMLBasicDef_CustomDocumentProperty('', customDocumentProperties=CustomDocumentPropertiesCollection(), SpreadsheetMLBasicDef_CustomDocumentProperty=ValueType()), ValueType58=SpreadsheetMLBasicDef_Data()) == None


from python_code import Comment
from python_code import Data
from python_code import Row
from python_code import SpreadsheetMLBasicDef_Cell

def test_SpreadsheetMLBasicDef_Cell___init__():
    assert SpreadsheetMLBasicDef_Cell.__init__(SpreadsheetMLBasicDef_Cell('', '', '', '', '', st_cell=set(), d_cell=Data(), c_cell=Comment(), r_cells=Row()), '', '', '', '\x00', '', st_cell=set(), d_cell=Data(), c_cell=Comment(), r_cells=Row()) == None


from python_code import SpreadsheetMLBasicDef_ColOrRowElement

def test_SpreadsheetMLBasicDef_ColOrRowElement___init__():
    assert SpreadsheetMLBasicDef_ColOrRowElement.__init__(SpreadsheetMLBasicDef_ColOrRowElement('', '\x00'), '\x00\x00', '') == None


from python_code import SpreadsheetMLBasicDef_Column
from python_code import Table

def test_SpreadsheetMLBasicDef_Column___init__():
    assert SpreadsheetMLBasicDef_Column.__init__(SpreadsheetMLBasicDef_Column('', '\x00', t_cols=Table()), '\x00\x00', '', t_cols=Table()) == None


from python_code import Cell
from python_code import Data
from python_code import SpreadsheetMLBasicDef_Comment

def test_SpreadsheetMLBasicDef_Comment___init__():
    assert SpreadsheetMLBasicDef_Comment.__init__(SpreadsheetMLBasicDef_Comment('', '\x00', c_comment=Cell(), d_comment=Data()), '\x00\x00', '', c_comment=Cell(), d_comment=Data()) == None


from python_code import CustomDocumentPropertiesCollection
from python_code import SpreadsheetMLBasicDef_CustomDocumentProperty
from python_code import ValueType

def test_SpreadsheetMLBasicDef_CustomDocumentProperty___init__():
    assert SpreadsheetMLBasicDef_CustomDocumentProperty.__init__(SpreadsheetMLBasicDef_CustomDocumentProperty('\x00', customDocumentProperties=CustomDocumentPropertiesCollection(), SpreadsheetMLBasicDef_CustomDocumentProperty=ValueType()), '', customDocumentProperties=CustomDocumentPropertiesCollection(), SpreadsheetMLBasicDef_CustomDocumentProperty=ValueType()) == None


from python_code import SpreadsheetMLBasicDef_DateTimeType

def test_SpreadsheetMLBasicDef_DateTimeType___init__():
    assert SpreadsheetMLBasicDef_DateTimeType.__init__(SpreadsheetMLBasicDef_DateTimeType('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import DateTimeType
from python_code import SpreadsheetMLBasicDef_DocumentPropertiesCollection
from python_code import VersionType
from python_code import Workbook

def test_SpreadsheetMLBasicDef_DocumentPropertiesCollection___init__():
    assert SpreadsheetMLBasicDef_DocumentPropertiesCollection.__init__(SpreadsheetMLBasicDef_DocumentPropertiesCollection('', '', '', '', '', '', '', '', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', wb_docProperties=Workbook(), SpreadsheetMLBasicDef_DocumentPropertiesCollection5=DateTimeType(), SpreadsheetMLBasicDef_DocumentPropertiesCollection8=DateTimeType(), SpreadsheetMLBasicDef_DocumentPropertiesCollection11=DateTimeType(), SpreadsheetMLBasicDef_DocumentPropertiesCollection=VersionType()), '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\x00', '', '', '', '', '', wb_docProperties=Workbook(), SpreadsheetMLBasicDef_DocumentPropertiesCollection5=DateTimeType(), SpreadsheetMLBasicDef_DocumentPropertiesCollection8=DateTimeType(), SpreadsheetMLBasicDef_DocumentPropertiesCollection11=DateTimeType(), SpreadsheetMLBasicDef_DocumentPropertiesCollection=VersionType()) == None


from python_code import CustomDocumentPropertiesCollection
from python_code import SpreadsheetMLBasicDef_CustomDocumentProperty
from python_code import SpreadsheetMLBasicDef_Data
from python_code import SpreadsheetMLBasicDef_NumberValue
from python_code import ValueType

def test_SpreadsheetMLBasicDef_NumberValue___init__():
    assert SpreadsheetMLBasicDef_NumberValue.__init__(SpreadsheetMLBasicDef_NumberValue('', ValueType=SpreadsheetMLBasicDef_CustomDocumentProperty('', customDocumentProperties=CustomDocumentPropertiesCollection(), SpreadsheetMLBasicDef_CustomDocumentProperty=ValueType()), ValueType58=SpreadsheetMLBasicDef_Data()), '', ValueType=SpreadsheetMLBasicDef_CustomDocumentProperty('', customDocumentProperties=CustomDocumentPropertiesCollection(), SpreadsheetMLBasicDef_CustomDocumentProperty=ValueType()), ValueType58=SpreadsheetMLBasicDef_Data()) == None


from python_code import SpreadsheetMLBasicDef_Row
from python_code import Table

def test_SpreadsheetMLBasicDef_Row___init__():
    assert SpreadsheetMLBasicDef_Row.__init__(SpreadsheetMLBasicDef_Row('\x00\x00', '', t_rows=Table(), c_row=set()), '', '', t_rows=Table(), c_row=set()) == None


from python_code import SmartTagsCollection
from python_code import SpreadsheetMLBasicDef_SmartTagType

def test_SpreadsheetMLBasicDef_SmartTagType___init__():
    assert SpreadsheetMLBasicDef_SmartTagType.__init__(SpreadsheetMLBasicDef_SmartTagType('', '', '\x00\x00', smartTagTypes=SmartTagsCollection()), '', '', '', smartTagTypes=SmartTagsCollection()) == None


from python_code import CustomDocumentPropertiesCollection
from python_code import SpreadsheetMLBasicDef_CustomDocumentProperty
from python_code import SpreadsheetMLBasicDef_Data
from python_code import SpreadsheetMLBasicDef_StringValue
from python_code import ValueType

def test_SpreadsheetMLBasicDef_StringValue___init__():
    assert SpreadsheetMLBasicDef_StringValue.__init__(SpreadsheetMLBasicDef_StringValue('', ValueType=SpreadsheetMLBasicDef_CustomDocumentProperty('', customDocumentProperties=CustomDocumentPropertiesCollection(), SpreadsheetMLBasicDef_CustomDocumentProperty=ValueType()), ValueType58=SpreadsheetMLBasicDef_Data()), '', ValueType=SpreadsheetMLBasicDef_CustomDocumentProperty('', customDocumentProperties=CustomDocumentPropertiesCollection(), SpreadsheetMLBasicDef_CustomDocumentProperty=ValueType()), ValueType58=SpreadsheetMLBasicDef_Data()) == None


from python_code import SpreadsheetMLBasicDef_Table
from python_code import Worksheet

def test_SpreadsheetMLBasicDef_Table___init__():
    assert SpreadsheetMLBasicDef_Table.__init__(SpreadsheetMLBasicDef_Table('', '', '', '', '', '', '', '', ws_table=Worksheet(), c_table=set(), r_table=set()), '', '', '\x00', '', '', '', '', '', ws_table=Worksheet(), c_table=set(), r_table=set()) == None


from python_code import SpreadsheetMLBasicDef_TableElement

def test_SpreadsheetMLBasicDef_TableElement___init__():
    assert SpreadsheetMLBasicDef_TableElement.__init__(SpreadsheetMLBasicDef_TableElement(''), '') == None


from python_code import SpreadsheetMLBasicDef_VersionType

def test_SpreadsheetMLBasicDef_VersionType___init__():
    assert SpreadsheetMLBasicDef_VersionType.__init__(SpreadsheetMLBasicDef_VersionType('', '\x00'), '\x00\x00', '') == None


from python_code import SpreadsheetMLBasicDef_Worksheet
from python_code import Table
from python_code import Workbook

def test_SpreadsheetMLBasicDef_Worksheet___init__():
    assert SpreadsheetMLBasicDef_Worksheet.__init__(SpreadsheetMLBasicDef_Worksheet('', wb_worksheets=Workbook(), t_worksheet=Table()), '', wb_worksheets=Workbook(), t_worksheet=Table()) == None

