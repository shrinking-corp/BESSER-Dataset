from python_code import relationaldb_Database

def test_relationaldb_Database___init__():
    assert relationaldb_Database.__init__(relationaldb_Database('', relationaldb_Database=set()), '', relationaldb_Database=set()) == None


from python_code import relationaldb_Named

def test_relationaldb_Named___init__():
    assert relationaldb_Named.__init__(relationaldb_Named(''), '') == None


from python_code import relationaldb_Varchar

def test_relationaldb_Varchar___init__():
    assert relationaldb_Varchar.__init__(relationaldb_Varchar(0), 0) == None

