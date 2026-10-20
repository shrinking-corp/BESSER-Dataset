from python_code import RelationalDBSchema_Column
from python_code import Table

def test_RelationalDBSchema_Column___init__():
    assert RelationalDBSchema_Column.__init__(RelationalDBSchema_Column('', '', '\x00\x00', columns=Table(), key=Table()), '', '', '', columns=Table(), key=Table()) == None


from python_code import RelationalDBSchema_DataBase

def test_RelationalDBSchema_DataBase___init__():
    assert RelationalDBSchema_DataBase.__init__(RelationalDBSchema_DataBase('', database=set()), '', database=set()) == None


from python_code import RelationalDBSchema_NamedElement

def test_RelationalDBSchema_NamedElement___init__():
    assert RelationalDBSchema_NamedElement.__init__(RelationalDBSchema_NamedElement(''), '') == None

