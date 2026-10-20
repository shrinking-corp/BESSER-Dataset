from python_code import CustomDocumentPropertiesCollection
from python_code import SpreadsheetMLWorkbookProp_BooleanValue
from python_code import SpreadsheetMLWorkbookProp_CustomDocumentProperty
from python_code import SpreadsheetMLWorkbookProp_Data
from python_code import ValueType

def test_SpreadsheetMLWorkbookProp_BooleanValue___init__():
    assert SpreadsheetMLWorkbookProp_BooleanValue.__init__(SpreadsheetMLWorkbookProp_BooleanValue('', ValueType=SpreadsheetMLWorkbookProp_CustomDocumentProperty('', customDocumentProperties=CustomDocumentPropertiesCollection(), SpreadsheetMLWorkbookProp_CustomDocumentProperty=ValueType()), ValueType59=SpreadsheetMLWorkbookProp_Data()), '', ValueType=SpreadsheetMLWorkbookProp_CustomDocumentProperty('', customDocumentProperties=CustomDocumentPropertiesCollection(), SpreadsheetMLWorkbookProp_CustomDocumentProperty=ValueType()), ValueType59=SpreadsheetMLWorkbookProp_Data()) == None


from python_code import Comment
from python_code import Data
from python_code import Row
from python_code import SpreadsheetMLWorkbookProp_Cell

def test_SpreadsheetMLWorkbookProp_Cell___init__():
    assert SpreadsheetMLWorkbookProp_Cell.__init__(SpreadsheetMLWorkbookProp_Cell('', '', '', '', '', r_cells=Row(), st_cell=set(), d_cell=Data(), c_cell=Comment()), '', '', '', '\x00', '', r_cells=Row(), st_cell=set(), d_cell=Data(), c_cell=Comment()) == None


from python_code import SpreadsheetMLWorkbookProp_ColOrRowElement

def test_SpreadsheetMLWorkbookProp_ColOrRowElement___init__():
    assert SpreadsheetMLWorkbookProp_ColOrRowElement.__init__(SpreadsheetMLWorkbookProp_ColOrRowElement('', '\x00'), '\x00\x00', '') == None


from python_code import SpreadsheetMLWorkbookProp_Column
from python_code import Table

def test_SpreadsheetMLWorkbookProp_Column___init__():
    assert SpreadsheetMLWorkbookProp_Column.__init__(SpreadsheetMLWorkbookProp_Column('', '\x00', t_cols=Table()), '\x00\x00', '', t_cols=Table()) == None


from python_code import Cell
from python_code import Data
from python_code import SpreadsheetMLWorkbookProp_Comment

def test_SpreadsheetMLWorkbookProp_Comment___init__():
    assert SpreadsheetMLWorkbookProp_Comment.__init__(SpreadsheetMLWorkbookProp_Comment('', '\x00', d_comment=Data(), c_comment=Cell()), '\x00\x00', '', d_comment=Data(), c_comment=Cell()) == None


from python_code import CustomDocumentPropertiesCollection
from python_code import SpreadsheetMLWorkbookProp_CustomDocumentProperty
from python_code import ValueType

def test_SpreadsheetMLWorkbookProp_CustomDocumentProperty___init__():
    assert SpreadsheetMLWorkbookProp_CustomDocumentProperty.__init__(SpreadsheetMLWorkbookProp_CustomDocumentProperty('', customDocumentProperties=CustomDocumentPropertiesCollection(), SpreadsheetMLWorkbookProp_CustomDocumentProperty=ValueType()), '', customDocumentProperties=CustomDocumentPropertiesCollection(), SpreadsheetMLWorkbookProp_CustomDocumentProperty=ValueType()) == None


from python_code import SpreadsheetMLWorkbookProp_DateTimeType

def test_SpreadsheetMLWorkbookProp_DateTimeType___init__():
    assert SpreadsheetMLWorkbookProp_DateTimeType.__init__(SpreadsheetMLWorkbookProp_DateTimeType('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import DateTimeType
from python_code import SpreadsheetMLWorkbookProp_DocumentPropertiesCollection
from python_code import VersionType
from python_code import Workbook

def test_SpreadsheetMLWorkbookProp_DocumentPropertiesCollection___init__():
    assert SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.__init__(SpreadsheetMLWorkbookProp_DocumentPropertiesCollection('', '', '', '', '', '', '', '', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', wb_docProperties=Workbook(), SpreadsheetMLWorkbookProp_DocumentPropertiesCollection5=DateTimeType(), SpreadsheetMLWorkbookProp_DocumentPropertiesCollection=VersionType(), SpreadsheetMLWorkbookProp_DocumentPropertiesCollection11=DateTimeType(), SpreadsheetMLWorkbookProp_DocumentPropertiesCollection8=DateTimeType()), '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\x00', '', '', '', '', '', wb_docProperties=Workbook(), SpreadsheetMLWorkbookProp_DocumentPropertiesCollection5=DateTimeType(), SpreadsheetMLWorkbookProp_DocumentPropertiesCollection=VersionType(), SpreadsheetMLWorkbookProp_DocumentPropertiesCollection11=DateTimeType(), SpreadsheetMLWorkbookProp_DocumentPropertiesCollection8=DateTimeType()) == None


from python_code import SpreadsheetMLWorkbookProp_ExcelWorkbook
from python_code import Workbook

def test_SpreadsheetMLWorkbookProp_ExcelWorkbook___init__():
    assert SpreadsheetMLWorkbookProp_ExcelWorkbook.__init__(SpreadsheetMLWorkbookProp_ExcelWorkbook('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', wb_excelWorkbook=Workbook()), '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\x00\x00', wb_excelWorkbook=Workbook()) == None


from python_code import CustomDocumentPropertiesCollection
from python_code import SpreadsheetMLWorkbookProp_CustomDocumentProperty
from python_code import SpreadsheetMLWorkbookProp_Data
from python_code import SpreadsheetMLWorkbookProp_NumberValue
from python_code import ValueType

def test_SpreadsheetMLWorkbookProp_NumberValue___init__():
    assert SpreadsheetMLWorkbookProp_NumberValue.__init__(SpreadsheetMLWorkbookProp_NumberValue('', ValueType=SpreadsheetMLWorkbookProp_CustomDocumentProperty('', customDocumentProperties=CustomDocumentPropertiesCollection(), SpreadsheetMLWorkbookProp_CustomDocumentProperty=ValueType()), ValueType59=SpreadsheetMLWorkbookProp_Data()), '', ValueType=SpreadsheetMLWorkbookProp_CustomDocumentProperty('', customDocumentProperties=CustomDocumentPropertiesCollection(), SpreadsheetMLWorkbookProp_CustomDocumentProperty=ValueType()), ValueType59=SpreadsheetMLWorkbookProp_Data()) == None


from python_code import SpreadsheetMLWorkbookProp_Row
from python_code import Table

def test_SpreadsheetMLWorkbookProp_Row___init__():
    assert SpreadsheetMLWorkbookProp_Row.__init__(SpreadsheetMLWorkbookProp_Row('\x00\x00', '', t_rows=Table(), c_row=set()), '', '', t_rows=Table(), c_row=set()) == None


from python_code import SmartTagsCollection
from python_code import SpreadsheetMLWorkbookProp_SmartTagType

def test_SpreadsheetMLWorkbookProp_SmartTagType___init__():
    assert SpreadsheetMLWorkbookProp_SmartTagType.__init__(SpreadsheetMLWorkbookProp_SmartTagType('', '', '\x00\x00', smartTagTypes=SmartTagsCollection()), '', '', '', smartTagTypes=SmartTagsCollection()) == None


from python_code import CustomDocumentPropertiesCollection
from python_code import SpreadsheetMLWorkbookProp_CustomDocumentProperty
from python_code import SpreadsheetMLWorkbookProp_Data
from python_code import SpreadsheetMLWorkbookProp_StringValue
from python_code import ValueType

def test_SpreadsheetMLWorkbookProp_StringValue___init__():
    assert SpreadsheetMLWorkbookProp_StringValue.__init__(SpreadsheetMLWorkbookProp_StringValue('', ValueType=SpreadsheetMLWorkbookProp_CustomDocumentProperty('', customDocumentProperties=CustomDocumentPropertiesCollection(), SpreadsheetMLWorkbookProp_CustomDocumentProperty=ValueType()), ValueType59=SpreadsheetMLWorkbookProp_Data()), '', ValueType=SpreadsheetMLWorkbookProp_CustomDocumentProperty('', customDocumentProperties=CustomDocumentPropertiesCollection(), SpreadsheetMLWorkbookProp_CustomDocumentProperty=ValueType()), ValueType59=SpreadsheetMLWorkbookProp_Data()) == None


from python_code import SpreadsheetMLWorkbookProp_Table
from python_code import Worksheet

def test_SpreadsheetMLWorkbookProp_Table___init__():
    assert SpreadsheetMLWorkbookProp_Table.__init__(SpreadsheetMLWorkbookProp_Table('', '', '', '', '', '', '', '', r_table=set(), ws_table=Worksheet(), c_table=set()), '', '', '\x00', '', '', '', '', '', r_table=set(), ws_table=Worksheet(), c_table=set()) == None


from python_code import SpreadsheetMLWorkbookProp_TableElement

def test_SpreadsheetMLWorkbookProp_TableElement___init__():
    assert SpreadsheetMLWorkbookProp_TableElement.__init__(SpreadsheetMLWorkbookProp_TableElement(''), '') == None


from python_code import SpreadsheetMLWorkbookProp_VersionType

def test_SpreadsheetMLWorkbookProp_VersionType___init__():
    assert SpreadsheetMLWorkbookProp_VersionType.__init__(SpreadsheetMLWorkbookProp_VersionType('', '\x00'), '\x00\x00', '') == None


from python_code import SpreadsheetMLWorkbookProp_Worksheet
from python_code import Table
from python_code import Workbook

def test_SpreadsheetMLWorkbookProp_Worksheet___init__():
    assert SpreadsheetMLWorkbookProp_Worksheet.__init__(SpreadsheetMLWorkbookProp_Worksheet('', wb_worksheets=Workbook(), t_worksheet=Table()), '', wb_worksheets=Workbook(), t_worksheet=Table()) == None

