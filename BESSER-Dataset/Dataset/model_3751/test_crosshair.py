from python_code import rdb_ERDInfo

def test_rdb_ERDInfo___init__():
    assert rdb_ERDInfo.__init__(rdb_ERDInfo(False, '\x00'), False, '\x00') == None

