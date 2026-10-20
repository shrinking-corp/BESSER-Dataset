from python_code import database_DBModuleCommonProperty

def test_database_DBModuleCommonProperty___init__():
    assert database_DBModuleCommonProperty.__init__(database_DBModuleCommonProperty('', '\x00'), '\x00\x00', '') == None


from python_code import database_TableIndex
from python_code import database_TableResourceData

def test_database_TableIndex___init__():
    assert database_TableIndex.__init__(database_TableIndex('', False, False, '', database_TableIndex=database_TableResourceData(), database_TableIndex8=set()), '', False, False, '', database_TableIndex=database_TableResourceData(), database_TableIndex8=set()) == None


from python_code import database_TableKey
from python_code import database_TableResourceData

def test_database_TableKey___init__():
    assert database_TableKey.__init__(database_TableKey('', '', '', database_TableKey=database_TableResourceData(), database_TableKey10=set(), database_TableKey13=set()), '', '', '', database_TableKey=database_TableResourceData(), database_TableKey10=set(), database_TableKey13=set()) == None


from python_code import database_ViewResourceData

def test_database_ViewResourceData___init__():
    assert database_ViewResourceData.__init__(database_ViewResourceData('', False), '', False) == None

