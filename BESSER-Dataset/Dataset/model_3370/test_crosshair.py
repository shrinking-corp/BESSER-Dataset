from python_code import DDL_CreateCommentColumn

def test_DDL_CreateCommentColumn___init__():
    assert DDL_CreateCommentColumn.__init__(DDL_CreateCommentColumn('', '', '\x00\x00'), '', '', '') == None


from python_code import DDL_CreateCommentTable

def test_DDL_CreateCommentTable___init__():
    assert DDL_CreateCommentTable.__init__(DDL_CreateCommentTable('', '\x00'), '\x00\x00', '') == None


from python_code import DDL_CreateDatabase

def test_DDL_CreateDatabase___init__():
    assert DDL_CreateDatabase.__init__(DDL_CreateDatabase(''), '') == None

