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


from python_code import DDL_Decimal

def test_DDL_Decimal___init__():
    assert DDL_Decimal.__init__(DDL_Decimal(0, 0), 0, 0) == None


from python_code import DDL_Float

def test_DDL_Float___init__():
    assert DDL_Float.__init__(DDL_Float(0), 0) == None


from python_code import DDL_Number

def test_DDL_Number___init__():
    assert DDL_Number.__init__(DDL_Number(0, 0), 0, 0) == None


from python_code import DDL_Numeric

def test_DDL_Numeric___init__():
    assert DDL_Numeric.__init__(DDL_Numeric(0, 0), 0, 0) == None


from python_code import DDL_Timestamp

def test_DDL_Timestamp___init__():
    assert DDL_Timestamp.__init__(DDL_Timestamp(0), 0) == None

