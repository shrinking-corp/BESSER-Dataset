from python_code import rdb_Model

def test_rdb_Model___init__():
    assert rdb_Model.__init__(rdb_Model('', rdb_Model=set()), '', rdb_Model=set()) == None


from python_code import rdb_NamedElement

def test_rdb_NamedElement___init__():
    assert rdb_NamedElement.__init__(rdb_NamedElement(''), '') == None


from python_code import rdb_Schema
from python_code import rdb_SchemaElement

def test_rdb_SchemaElement___init__():
    assert rdb_SchemaElement.__init__(rdb_SchemaElement('', rdb_SchemaElement=rdb_Schema()), '', rdb_SchemaElement=rdb_Schema()) == None


from python_code import Domain
from python_code import PrimitiveDataType
from python_code import rdb_Table
from python_code import rdb_TableColumn

def test_rdb_TableColumn___init__():
    assert rdb_TableColumn.__init__(rdb_TableColumn('', '\x00', rdb_TableColumn17=Domain(), rdb_TableColumn19=PrimitiveDataType(), rdb_TableColumn=rdb_Table()), '\x00\x00', '', rdb_TableColumn17=Domain(), rdb_TableColumn19=PrimitiveDataType(), rdb_TableColumn=rdb_Table()) == None


from python_code import rdb_constraints_CheckConstraint

def test_rdb_constraints_CheckConstraint___init__():
    assert rdb_constraints_CheckConstraint.__init__(rdb_constraints_CheckConstraint(''), '') == None


from python_code import constraints_rdb_TableColumn
from python_code import rdb_constraints_IndexedColumn

def test_rdb_constraints_IndexedColumn___init__():
    assert rdb_constraints_IndexedColumn.__init__(rdb_constraints_IndexedColumn(True, rdb_constraints_IndexedColumn=constraints_rdb_TableColumn()), False, rdb_constraints_IndexedColumn=constraints_rdb_TableColumn()) == None


from python_code import rdb_datatypes_DataType

def test_rdb_datatypes_DataType___init__():
    assert rdb_datatypes_DataType.__init__(rdb_datatypes_DataType(0, 0, False, '', '', ''), 0, 0, False, '', '\x00', '') == None


from python_code import rdb_datatypes_PrimitiveDataType

def test_rdb_datatypes_PrimitiveDataType___init__():
    assert rdb_datatypes_PrimitiveDataType.__init__(rdb_datatypes_PrimitiveDataType(''), '') == None


from python_code import rdb_view_View

def test_rdb_view_View___init__():
    assert rdb_view_View.__init__(rdb_view_View('', rdb_view_View=set(), rdb_view_View30=set()), '', rdb_view_View=set(), rdb_view_View30=set()) == None


from python_code import rdb_view_View
from python_code import rdb_view_ViewExpressionColumn

def test_rdb_view_ViewExpressionColumn___init__():
    assert rdb_view_ViewExpressionColumn.__init__(rdb_view_ViewExpressionColumn('', ViewColumn=rdb_view_View('', rdb_view_View=set(), rdb_view_View30=set())), '', ViewColumn=rdb_view_View('', rdb_view_View=set(), rdb_view_View30=set())) == None

