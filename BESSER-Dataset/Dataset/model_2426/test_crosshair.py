from python_code import DB_Database
from python_code import DB_DatabaseElement

def test_DB_Database___init__():
    assert DB_Database.__init__(DB_Database('', database=set(), Database=DB_DatabaseElement()), '', database=set(), Database=DB_DatabaseElement()) == None


from python_code import DB_NamedElement

def test_DB_NamedElement___init__():
    assert DB_NamedElement.__init__(DB_NamedElement(''), '') == None

