from python_code import DML_DDL_Bits

def test_DML_DDL_Bits___init__():
    assert DML_DDL_Bits.__init__(DML_DDL_Bits(''), '') == None


from python_code import DML_DDL_Characters

def test_DML_DDL_Characters___init__():
    assert DML_DDL_Characters.__init__(DML_DDL_Characters(''), '') == None


from python_code import DML_DDL_CommentColumn

def test_DML_DDL_CommentColumn___init__():
    assert DML_DDL_CommentColumn.__init__(DML_DDL_CommentColumn('', '', '\x00\x00'), '', '', '') == None


from python_code import DML_DDL_CommentTable

def test_DML_DDL_CommentTable___init__():
    assert DML_DDL_CommentTable.__init__(DML_DDL_CommentTable('', '\x00'), '\x00\x00', '') == None


from python_code import DML_DDL_Database

def test_DML_DDL_Database___init__():
    assert DML_DDL_Database.__init__(DML_DDL_Database(''), '') == None

