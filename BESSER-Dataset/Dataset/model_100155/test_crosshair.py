from python_code import Table
from python_code import mm_rdb_AddColumn
from python_code import mm_rdb_ModelRoot

def test_mm_rdb_AddColumn___init__():
    assert mm_rdb_AddColumn.__init__(mm_rdb_AddColumn('', mm_rdb_AddColumn=Table(), mm_rdb_AddColumn59=set(), Operation=mm_rdb_ModelRoot()), '', mm_rdb_AddColumn=Table(), mm_rdb_AddColumn59=set(), Operation=mm_rdb_ModelRoot()) == None

def test_mm_rdb_AddColumn_addColumn():
    assert mm_rdb_AddColumn.addColumn(mm_rdb_AddColumn('\x00', mm_rdb_AddColumn=Table(), mm_rdb_AddColumn59=set(), Operation=mm_rdb_ModelRoot()), '', '', 0) == None


from python_code import mm_rdb_Column

def test_mm_rdb_Column___init__():
    assert mm_rdb_Column.__init__(mm_rdb_Column()) == None

def test_mm_rdb_Column_getOwningTable():
    assert mm_rdb_Column.getOwningTable(mm_rdb_Column()) == None


from python_code import PrimaryKey
from python_code import Sequence
from python_code import mm_rdb_CreateTable
from python_code import mm_rdb_ModelRoot

def test_mm_rdb_CreateTable___init__():
    assert mm_rdb_CreateTable.__init__(mm_rdb_CreateTable('', mm_rdb_CreateTable=set(), mm_rdb_CreateTable44=set(), mm_rdb_CreateTable47=PrimaryKey(), mm_rdb_CreateTable50=Sequence(), Operation=mm_rdb_ModelRoot()), '', mm_rdb_CreateTable=set(), mm_rdb_CreateTable44=set(), mm_rdb_CreateTable47=PrimaryKey(), mm_rdb_CreateTable50=Sequence(), Operation=mm_rdb_ModelRoot()) == None

def test_mm_rdb_CreateTable_createTable():
    assert mm_rdb_CreateTable.createTable(mm_rdb_CreateTable('\x00', mm_rdb_CreateTable=set(), mm_rdb_CreateTable44=set(), mm_rdb_CreateTable47=PrimaryKey(), mm_rdb_CreateTable50=Sequence(), Operation=mm_rdb_ModelRoot()), '', '', '', '', '') == None


from python_code import Table
from python_code import TableColumn
from python_code import mm_rdb_DeleteColumn
from python_code import mm_rdb_ModelRoot

def test_mm_rdb_DeleteColumn___init__():
    assert mm_rdb_DeleteColumn.__init__(mm_rdb_DeleteColumn(mm_rdb_DeleteColumn=Table(), mm_rdb_DeleteColumn74=TableColumn(), Operation=mm_rdb_ModelRoot()), mm_rdb_DeleteColumn=Table(), mm_rdb_DeleteColumn74=TableColumn(), Operation=mm_rdb_ModelRoot()) == None

def test_mm_rdb_DeleteColumn_deleteColumn():
    assert mm_rdb_DeleteColumn.deleteColumn(mm_rdb_DeleteColumn(mm_rdb_DeleteColumn=Table(), mm_rdb_DeleteColumn74=TableColumn(), Operation=mm_rdb_ModelRoot()), '', '') == None


from python_code import Table
from python_code import mm_rdb_DeleteTable
from python_code import mm_rdb_ModelRoot

def test_mm_rdb_DeleteTable___init__():
    assert mm_rdb_DeleteTable.__init__(mm_rdb_DeleteTable(mm_rdb_DeleteTable=Table(), Operation=mm_rdb_ModelRoot()), mm_rdb_DeleteTable=Table(), Operation=mm_rdb_ModelRoot()) == None

def test_mm_rdb_DeleteTable_deleteTable():
    assert mm_rdb_DeleteTable.deleteTable(mm_rdb_DeleteTable(mm_rdb_DeleteTable=Table(), Operation=mm_rdb_ModelRoot()), '') == None


from python_code import mm_rdb_NamedElement

def test_mm_rdb_NamedElement___init__():
    assert mm_rdb_NamedElement.__init__(mm_rdb_NamedElement(''), '') == None


from python_code import mm_rdb_Relation

def test_mm_rdb_Relation___init__():
    assert mm_rdb_Relation.__init__(mm_rdb_Relation()) == None

def test_mm_rdb_Relation_getColumns():
    assert mm_rdb_Relation.getColumns(mm_rdb_Relation()) == None


from python_code import Table
from python_code import TableColumn
from python_code import mm_rdb_ModelRoot
from python_code import mm_rdb_RenameColumn

def test_mm_rdb_RenameColumn___init__():
    assert mm_rdb_RenameColumn.__init__(mm_rdb_RenameColumn('', mm_rdb_RenameColumn=Table(), mm_rdb_RenameColumn64=TableColumn(), Operation=mm_rdb_ModelRoot()), '', mm_rdb_RenameColumn=Table(), mm_rdb_RenameColumn64=TableColumn(), Operation=mm_rdb_ModelRoot()) == None

def test_mm_rdb_RenameColumn_renameColumn():
    assert mm_rdb_RenameColumn.renameColumn(mm_rdb_RenameColumn('', mm_rdb_RenameColumn=Table(), mm_rdb_RenameColumn64=TableColumn(), Operation=mm_rdb_ModelRoot()), 0, '\x00\x00', '') == None


from python_code import Table
from python_code import mm_rdb_ModelRoot
from python_code import mm_rdb_RenameTable

def test_mm_rdb_RenameTable___init__():
    assert mm_rdb_RenameTable.__init__(mm_rdb_RenameTable('', mm_rdb_RenameTable=Table(), Operation=mm_rdb_ModelRoot()), '', mm_rdb_RenameTable=Table(), Operation=mm_rdb_ModelRoot()) == None

def test_mm_rdb_RenameTable_renameTable():
    assert mm_rdb_RenameTable.renameTable(mm_rdb_RenameTable('', mm_rdb_RenameTable=Table(), Operation=mm_rdb_ModelRoot()), 0, '\x00\x00') == None


from python_code import Schema
from python_code import mm_rdb_Sequence

def test_mm_rdb_Sequence___init__():
    assert mm_rdb_Sequence.__init__(mm_rdb_Sequence(0, sequences=Schema()), 0, sequences=Schema()) == None


from python_code import PrimaryKey
from python_code import Schema
from python_code import mm_rdb_Table

def test_mm_rdb_Table___init__():
    assert mm_rdb_Table.__init__(mm_rdb_Table(owningTable=set(), tables=Schema(), mm_rdb_Table=PrimaryKey(), _owningTable=set()), owningTable=set(), tables=Schema(), mm_rdb_Table=PrimaryKey(), _owningTable=set()) == None

def test_mm_rdb_Table_getColumns():
    assert mm_rdb_Table.getColumns(mm_rdb_Table(owningTable=set(), tables=Schema(), mm_rdb_Table=PrimaryKey(), _owningTable=set())) == None

def test_mm_rdb_Table_getPrimaryColumn():
    assert mm_rdb_Table.getPrimaryColumn(mm_rdb_Table(owningTable=set(), tables=Schema(), mm_rdb_Table=PrimaryKey(), _owningTable=set())) == None


from python_code import Table
from python_code import mm_dml_ColumnReference
from python_code import mm_rdb_TableColumn

def test_mm_rdb_TableColumn___init__():
    assert mm_rdb_TableColumn.__init__(mm_rdb_TableColumn('', ownedColumns=Table(), owningColumn=set(), Column=mm_dml_ColumnReference()), '', ownedColumns=Table(), owningColumn=set(), Column=mm_dml_ColumnReference()) == None

def test_mm_rdb_TableColumn_getOwningTable():
    assert mm_rdb_TableColumn.getOwningTable(mm_rdb_TableColumn('', ownedColumns=Table(), owningColumn=set(), Column=mm_dml_ColumnReference())) == None


from python_code import Table
from python_code import TableColumn
from python_code import mm_rdb_ModelRoot
from python_code import mm_rdb_TypeChangeToColumn

def test_mm_rdb_TypeChangeToColumn___init__():
    assert mm_rdb_TypeChangeToColumn.__init__(mm_rdb_TypeChangeToColumn('', mm_rdb_TypeChangeToColumn69=TableColumn(), mm_rdb_TypeChangeToColumn=Table(), Operation=mm_rdb_ModelRoot()), '', mm_rdb_TypeChangeToColumn69=TableColumn(), mm_rdb_TypeChangeToColumn=Table(), Operation=mm_rdb_ModelRoot()) == None

def test_mm_rdb_TypeChangeToColumn_typeChangeToColumn():
    assert mm_rdb_TypeChangeToColumn.typeChangeToColumn(mm_rdb_TypeChangeToColumn('', mm_rdb_TypeChangeToColumn69=TableColumn(), mm_rdb_TypeChangeToColumn=Table(), Operation=mm_rdb_ModelRoot()), 0, '\x00\x00', '') == None

