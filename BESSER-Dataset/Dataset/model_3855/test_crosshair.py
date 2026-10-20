from python_code import SimpleRDBMS_Database

def test_SimpleRDBMS_Database___init__():
    assert SimpleRDBMS_Database.__init__(SimpleRDBMS_Database('', '', '\x00\x00'), '', '', '') == None


from python_code import SimpleRDBMS_FKey
from python_code import SimpleRDBMS_Table

def test_SimpleRDBMS_Table___init__():
    assert SimpleRDBMS_Table.__init__(SimpleRDBMS_Table('', 0, SimpleRDBMS_Table=set(), SimpleRDBMS_Table2=set(), SimpleRDBMS_Table4=set(), SimpleRDBMS_Table8=SimpleRDBMS_FKey()), '', 0, SimpleRDBMS_Table=set(), SimpleRDBMS_Table2=set(), SimpleRDBMS_Table4=set(), SimpleRDBMS_Table8=SimpleRDBMS_FKey()) == None

