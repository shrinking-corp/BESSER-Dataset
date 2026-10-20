from python_code import mm_ops_AddColumn

def test_mm_ops_AddColumn___init__():
    assert mm_ops_AddColumn.__init__(mm_ops_AddColumn('', '', '', '', ''), '', '', '', '', '') == None


from python_code import mm_ops_AddForeignKey

def test_mm_ops_AddForeignKey___init__():
    assert mm_ops_AddForeignKey.__init__(mm_ops_AddForeignKey('', '', '', '', ''), '', '', '', '', '') == None


from python_code import mm_ops_AddIndex

def test_mm_ops_AddIndex___init__():
    assert mm_ops_AddIndex.__init__(mm_ops_AddIndex('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import mm_ops_AddNotNull

def test_mm_ops_AddNotNull___init__():
    assert mm_ops_AddNotNull.__init__(mm_ops_AddNotNull('', '', '\x00\x00'), '', '', '') == None


from python_code import mm_ops_AddPrimaryKey

def test_mm_ops_AddPrimaryKey___init__():
    assert mm_ops_AddPrimaryKey.__init__(mm_ops_AddPrimaryKey('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import mm_ops_AddSchema

def test_mm_ops_AddSchema___init__():
    assert mm_ops_AddSchema.__init__(mm_ops_AddSchema(''), '') == None


from python_code import mm_ops_AddSequence

def test_mm_ops_AddSequence___init__():
    assert mm_ops_AddSequence.__init__(mm_ops_AddSequence('', '', 0), '\x00', '', 0) == None


from python_code import mm_ops_AddTable

def test_mm_ops_AddTable___init__():
    assert mm_ops_AddTable.__init__(mm_ops_AddTable('', '\x00'), '\x00\x00', '') == None


from python_code import mm_ops_AddUnique

def test_mm_ops_AddUnique___init__():
    assert mm_ops_AddUnique.__init__(mm_ops_AddUnique('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import mm_ops_DeleteRows

def test_mm_ops_DeleteRows___init__():
    assert mm_ops_DeleteRows.__init__(mm_ops_DeleteRows('', '', '\x00\x00'), '', '', '') == None


from python_code import mm_ops_GenerateSequenceNumbers

def test_mm_ops_GenerateSequenceNumbers___init__():
    assert mm_ops_GenerateSequenceNumbers.__init__(mm_ops_GenerateSequenceNumbers('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import mm_ops_HasNoInstances

def test_mm_ops_HasNoInstances___init__():
    assert mm_ops_HasNoInstances.__init__(mm_ops_HasNoInstances('', '\x00'), '\x00\x00', '') == None


from python_code import mm_ops_HasNoOwnInstances

def test_mm_ops_HasNoOwnInstances___init__():
    assert mm_ops_HasNoOwnInstances.__init__(mm_ops_HasNoOwnInstances('', '', '\x00\x00'), '', '', '') == None


from python_code import mm_ops_InsertRows

def test_mm_ops_InsertRows___init__():
    assert mm_ops_InsertRows.__init__(mm_ops_InsertRows('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import mm_ops_NillRows

def test_mm_ops_NillRows___init__():
    assert mm_ops_NillRows.__init__(mm_ops_NillRows('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import mm_ops_RemoveColumn

def test_mm_ops_RemoveColumn___init__():
    assert mm_ops_RemoveColumn.__init__(mm_ops_RemoveColumn('', '', '\x00\x00'), '', '', '') == None


from python_code import mm_ops_RemoveConstraint

def test_mm_ops_RemoveConstraint___init__():
    assert mm_ops_RemoveConstraint.__init__(mm_ops_RemoveConstraint('', '', '\x00\x00'), '', '', '') == None


from python_code import mm_ops_RemoveDefaultValue

def test_mm_ops_RemoveDefaultValue___init__():
    assert mm_ops_RemoveDefaultValue.__init__(mm_ops_RemoveDefaultValue('', '', '\x00\x00'), '', '', '') == None


from python_code import mm_ops_RemoveIndex

def test_mm_ops_RemoveIndex___init__():
    assert mm_ops_RemoveIndex.__init__(mm_ops_RemoveIndex('', '\x00'), '\x00\x00', '') == None


from python_code import mm_ops_RemoveNotNull

def test_mm_ops_RemoveNotNull___init__():
    assert mm_ops_RemoveNotNull.__init__(mm_ops_RemoveNotNull('', '', '\x00\x00'), '', '', '') == None


from python_code import mm_ops_RemoveSequence

def test_mm_ops_RemoveSequence___init__():
    assert mm_ops_RemoveSequence.__init__(mm_ops_RemoveSequence('', '\x00'), '\x00\x00', '') == None


from python_code import mm_ops_RemoveTable

def test_mm_ops_RemoveTable___init__():
    assert mm_ops_RemoveTable.__init__(mm_ops_RemoveTable('', '\x00'), '\x00\x00', '') == None


from python_code import mm_ops_RenameColumn

def test_mm_ops_RenameColumn___init__():
    assert mm_ops_RenameColumn.__init__(mm_ops_RenameColumn('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import mm_ops_RenameTable

def test_mm_ops_RenameTable___init__():
    assert mm_ops_RenameTable.__init__(mm_ops_RenameTable('', '', '\x00\x00'), '', '', '') == None


from python_code import mm_ops_SetColumnType

def test_mm_ops_SetColumnType___init__():
    assert mm_ops_SetColumnType.__init__(mm_ops_SetColumnType('', '', '', '', ''), '', '', '', '', '') == None


from python_code import mm_ops_SetDefaultValue

def test_mm_ops_SetDefaultValue___init__():
    assert mm_ops_SetDefaultValue.__init__(mm_ops_SetDefaultValue('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import mm_ops_UpdateRows

def test_mm_ops_UpdateRows___init__():
    assert mm_ops_UpdateRows.__init__(mm_ops_UpdateRows('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import Table
from python_code import mm_rdb_Column

def test_mm_rdb_Column___init__():
    assert mm_rdb_Column.__init__(mm_rdb_Column('\x00\x00', '', '', '', columns=Table()), '', '', '', '', columns=Table()) == None


from python_code import Schema
from python_code import mm_rdb_Index

def test_mm_rdb_Index___init__():
    assert mm_rdb_Index.__init__(mm_rdb_Index('', indexes=Schema(), mm_rdb_Index=set()), '', indexes=Schema(), mm_rdb_Index=set()) == None


from python_code import Sequence
from python_code import Structure
from python_code import mm_rdb_Schema

def test_mm_rdb_Schema___init__():
    assert mm_rdb_Schema.__init__(mm_rdb_Schema('', owningSchema5=Sequence(), owningSchema7=set(), schemas=Structure(), owningSchema=set()), '', owningSchema5=Sequence(), owningSchema7=set(), schemas=Structure(), owningSchema=set()) == None


from python_code import Schema
from python_code import mm_rdb_Sequence

def test_mm_rdb_Sequence___init__():
    assert mm_rdb_Sequence.__init__(mm_rdb_Sequence('', 0, sequence=Schema()), '', 0, sequence=Schema()) == None


from python_code import Schema
from python_code import mm_rdb_Table

def test_mm_rdb_Table___init__():
    assert mm_rdb_Table.__init__(mm_rdb_Table('', tables=Schema(), owningTable=set(), owningTable18=set()), '', tables=Schema(), owningTable=set(), owningTable18=set()) == None


from python_code import Table
from python_code import mm_rdb_TableConstraint

def test_mm_rdb_TableConstraint___init__():
    assert mm_rdb_TableConstraint.__init__(mm_rdb_TableConstraint('', constraints=Table()), '', constraints=Table()) == None

