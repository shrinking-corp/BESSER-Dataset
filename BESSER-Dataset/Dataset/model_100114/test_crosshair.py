from python_code import database_Constraint
from python_code import database_Table

def test_database_Constraint___init__():
    assert database_Constraint.__init__(database_Constraint('', Constraint=database_Table(), constraints=database_Table()), '', Constraint=database_Table(), constraints=database_Table()) == None


from python_code import database_DataBase

def test_database_DataBase___init__():
    assert database_DataBase.__init__(database_DataBase('', database_DataBase=set(), database_DataBase2=set()), '', database_DataBase=set(), database_DataBase2=set()) == None


from python_code import database_DatabaseElement

def test_database_DatabaseElement___init__():
    assert database_DatabaseElement.__init__(database_DatabaseElement('', '\x00'), '\x00\x00', '') == None


from python_code import database_NamedElement

def test_database_NamedElement___init__():
    assert database_NamedElement.__init__(database_NamedElement(''), '') == None


from python_code import database_View

def test_database_View___init__():
    assert database_View.__init__(database_View(''), '') == None

