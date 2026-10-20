from python_code import relational_Column

def test_relational_Column___init__():
    assert relational_Column.__init__(relational_Column(''), '') == None


from python_code import relational_DataBase

def test_relational_DataBase___init__():
    assert relational_DataBase.__init__(relational_DataBase('\x00\x00', 0, relational_DataBase=set()), '', 0, relational_DataBase=set()) == None


from python_code import relational_PrimaryKey

def test_relational_PrimaryKey___init__():
    assert relational_PrimaryKey.__init__(relational_PrimaryKey(''), '') == None

