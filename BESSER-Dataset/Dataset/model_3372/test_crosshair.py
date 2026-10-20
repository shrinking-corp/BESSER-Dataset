from python_code import DDL_Bits

def test_DDL_Bits___init__():
    assert DDL_Bits.__init__(DDL_Bits(''), '') == None


from python_code import DDL_Characters

def test_DDL_Characters___init__():
    assert DDL_Characters.__init__(DDL_Characters(''), '') == None


from python_code import DDL_CommentColumn

def test_DDL_CommentColumn___init__():
    assert DDL_CommentColumn.__init__(DDL_CommentColumn('', '', '\x00\x00'), '', '', '') == None


from python_code import DDL_CommentTable

def test_DDL_CommentTable___init__():
    assert DDL_CommentTable.__init__(DDL_CommentTable('', '\x00'), '\x00\x00', '') == None


from python_code import DDL_Database

def test_DDL_Database___init__():
    assert DDL_Database.__init__(DDL_Database(''), '') == None

