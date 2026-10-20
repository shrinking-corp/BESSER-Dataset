from python_code import dSDL_AutoIncrement

def test_dSDL_AutoIncrement___init__():
    assert dSDL_AutoIncrement.__init__(dSDL_AutoIncrement(True), False) == None


from python_code import dSDL_Database

def test_dSDL_Database___init__():
    assert dSDL_Database.__init__(dSDL_Database('', dSDL_Database=set()), '', dSDL_Database=set()) == None


from python_code import dSDL_DateTime

def test_dSDL_DateTime___init__():
    assert dSDL_DateTime.__init__(dSDL_DateTime(''), '') == None


from python_code import dSDL_ForeignKey

def test_dSDL_ForeignKey___init__():
    assert dSDL_ForeignKey.__init__(dSDL_ForeignKey('', '\x00'), '\x00\x00', '') == None


from python_code import dSDL_Integer

def test_dSDL_Integer___init__():
    assert dSDL_Integer.__init__(dSDL_Integer('', 0), '', 0) == None


from python_code import dSDL_Nullable

def test_dSDL_Nullable___init__():
    assert dSDL_Nullable.__init__(dSDL_Nullable(True), False) == None


from python_code import dSDL_PrimaryKey

def test_dSDL_PrimaryKey___init__():
    assert dSDL_PrimaryKey.__init__(dSDL_PrimaryKey(True), False) == None


from python_code import dSDL_Text

def test_dSDL_Text___init__():
    assert dSDL_Text.__init__(dSDL_Text(''), '') == None


from python_code import dSDL_Varchar

def test_dSDL_Varchar___init__():
    assert dSDL_Varchar.__init__(dSDL_Varchar('', 0), '', 0) == None

