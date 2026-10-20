from python_code import sql_Database

def test_sql_Database___init__():
    assert sql_Database.__init__(sql_Database('\x00\x00', '', sql_Database=set()), '', '', sql_Database=set()) == None

