from python_code import model_DatabaseVersions

def test_model_DatabaseVersions___init__():
    assert model_DatabaseVersions.__init__(model_DatabaseVersions('\x00\x00', '', model_DatabaseVersions=set()), '', '', model_DatabaseVersions=set()) == None

def test_model_DatabaseVersions_getLastVersion():
    assert model_DatabaseVersions.getLastVersion(model_DatabaseVersions('', '\x00', model_DatabaseVersions=set())) == None

def test_model_DatabaseVersions_createVersion():
    assert model_DatabaseVersions.createVersion(model_DatabaseVersions('', '\x00', model_DatabaseVersions=set())) == None

def test_model_DatabaseVersions_getFirstVersion():
    assert model_DatabaseVersions.getFirstVersion(model_DatabaseVersions('', '\x00', model_DatabaseVersions=set())) == None


from python_code import Table
from python_code import model_column_Column

def test_model_column_Column___init__():
    assert model_column_Column.__init__(model_column_Column('', columns=Table(), column=set()), '', columns=Table(), column=set()) == None


from python_code import Column
from python_code import model_column_ColumnConstraint

def test_model_column_ColumnConstraint___init__():
    assert model_column_ColumnConstraint.__init__(model_column_ColumnConstraint('', constraints51=Column()), '', constraints51=Column()) == None


from python_code import model_common_MappingEntry

def test_model_common_MappingEntry___init__():
    assert model_common_MappingEntry.__init__(model_common_MappingEntry('', '\x00'), '\x00\x00', '') == None


from python_code import model_common_NameProvider

def test_model_common_NameProvider___init__():
    assert model_common_NameProvider.__init__(model_common_NameProvider(''), '') == None


from python_code import model_common_StringToColumnMappingEntryMap

def test_model_common_StringToColumnMappingEntryMap___init__():
    assert model_common_StringToColumnMappingEntryMap.__init__(model_common_StringToColumnMappingEntryMap(''), '') == None


from python_code import model_common_StringToTableMappingEntryMap

def test_model_common_StringToTableMappingEntryMap___init__():
    assert model_common_StringToTableMappingEntryMap.__init__(model_common_StringToTableMappingEntryMap(''), '') == None


from python_code import Table
from python_code import model_table_TableConstraint

def test_model_table_TableConstraint___init__():
    assert model_table_TableConstraint.__init__(model_table_TableConstraint('', constraints=Table()), '', constraints=Table()) == None

