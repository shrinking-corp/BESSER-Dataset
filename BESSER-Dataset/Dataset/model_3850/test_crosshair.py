from python_code import SimpleRDBMS_Column

def test_SimpleRDBMS_Column___init__():
    assert SimpleRDBMS_Column.__init__(SimpleRDBMS_Column('', '\x00'), '\x00\x00', '') == None


from python_code import SimpleRDBMS_Table

def test_SimpleRDBMS_Table___init__():
    assert SimpleRDBMS_Table.__init__(SimpleRDBMS_Table('', '', SimpleRDBMS_Table=set(), SimpleRDBMS_Table2=set(), SimpleRDBMS_Table4=set()), '', '', SimpleRDBMS_Table=set(), SimpleRDBMS_Table2=set(), SimpleRDBMS_Table4=set()) == None

