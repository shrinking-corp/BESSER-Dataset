from python_code import rdbmdl_Model

def test_rdbmdl_Model___init__():
    assert rdbmdl_Model.__init__(rdbmdl_Model('', rdbmdl_Model=set()), '', rdbmdl_Model=set()) == None


from python_code import rdbmdl_NamedElement

def test_rdbmdl_NamedElement___init__():
    assert rdbmdl_NamedElement.__init__(rdbmdl_NamedElement('', '\x00'), '\x00\x00', '') == None


from python_code import rdbmdl_Schema
from python_code import rdbmdl_SchemaElement

def test_rdbmdl_SchemaElement___init__():
    assert rdbmdl_SchemaElement.__init__(rdbmdl_SchemaElement('', rdbmdl_SchemaElement=rdbmdl_Schema()), '', rdbmdl_SchemaElement=rdbmdl_Schema()) == None


from python_code import Domain
from python_code import PrimitiveDataType
from python_code import rdbmdl_Table
from python_code import rdbmdl_TableColumn

def test_rdbmdl_TableColumn___init__():
    assert rdbmdl_TableColumn.__init__(rdbmdl_TableColumn('', '\x00', rdbmdl_TableColumn17=Domain(), rdbmdl_TableColumn19=PrimitiveDataType(), rdbmdl_TableColumn=rdbmdl_Table()), '\x00\x00', '', rdbmdl_TableColumn17=Domain(), rdbmdl_TableColumn19=PrimitiveDataType(), rdbmdl_TableColumn=rdbmdl_Table()) == None


from python_code import rdbmdl_constraints_CheckConstraint

def test_rdbmdl_constraints_CheckConstraint___init__():
    assert rdbmdl_constraints_CheckConstraint.__init__(rdbmdl_constraints_CheckConstraint(''), '') == None


from python_code import constraints_rdbmdl_TableColumn
from python_code import rdbmdl_constraints_IndexedColumn

def test_rdbmdl_constraints_IndexedColumn___init__():
    assert rdbmdl_constraints_IndexedColumn.__init__(rdbmdl_constraints_IndexedColumn(True, rdbmdl_constraints_IndexedColumn=constraints_rdbmdl_TableColumn()), False, rdbmdl_constraints_IndexedColumn=constraints_rdbmdl_TableColumn()) == None


from python_code import rdbmdl_datatypes_DataType

def test_rdbmdl_datatypes_DataType___init__():
    assert rdbmdl_datatypes_DataType.__init__(rdbmdl_datatypes_DataType(0, False, '', '', '', 0), 0, False, '', '', '\x00', 0) == None


from python_code import rdbmdl_datatypes_PrimitiveDataType

def test_rdbmdl_datatypes_PrimitiveDataType___init__():
    assert rdbmdl_datatypes_PrimitiveDataType.__init__(rdbmdl_datatypes_PrimitiveDataType(''), '') == None


from python_code import rdbmdl_view_View

def test_rdbmdl_view_View___init__():
    assert rdbmdl_view_View.__init__(rdbmdl_view_View('', rdbmdl_view_View=set(), rdbmdl_view_View30=set()), '', rdbmdl_view_View=set(), rdbmdl_view_View30=set()) == None


from python_code import rdbmdl_view_View
from python_code import rdbmdl_view_ViewExpressionColumn

def test_rdbmdl_view_ViewExpressionColumn___init__():
    assert rdbmdl_view_ViewExpressionColumn.__init__(rdbmdl_view_ViewExpressionColumn('', ViewColumn=rdbmdl_view_View('', rdbmdl_view_View=set(), rdbmdl_view_View30=set())), '', ViewColumn=rdbmdl_view_View('', rdbmdl_view_View=set(), rdbmdl_view_View30=set())) == None

