from python_code import DB_Database

def test_DB_Database___init__():
    assert DB_Database.__init__(DB_Database('', DB_Database=set()), '', DB_Database=set()) == None

