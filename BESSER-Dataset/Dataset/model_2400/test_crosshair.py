from python_code import rdb_Schema

def test_rdb_Schema___init__():
    assert rdb_Schema.__init__(rdb_Schema('', rdb_Schema=set()), '', rdb_Schema=set()) == None

