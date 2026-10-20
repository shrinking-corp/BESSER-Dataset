from python_code import RDBMS_Column

def test_RDBMS_Column___init__():
    assert RDBMS_Column.__init__(RDBMS_Column('', '\x00'), '\x00\x00', '') == None


from python_code import RDBMS_Schema

def test_RDBMS_Schema___init__():
    assert RDBMS_Schema.__init__(RDBMS_Schema('', RDBMS_Schema=set()), '', RDBMS_Schema=set()) == None


from python_code import RDBMS_Table

def test_RDBMS_Table___init__():
    assert RDBMS_Table.__init__(RDBMS_Table('', '', RDBMS_Table2=set(), RDBMS_Table4=set(), RDBMS_Table=set()), '', '', RDBMS_Table2=set(), RDBMS_Table4=set(), RDBMS_Table=set()) == None

