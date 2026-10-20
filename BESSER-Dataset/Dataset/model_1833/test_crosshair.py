from python_code import edatatypeColumn_Book

def test_edatatypeColumn_Book___init__():
    assert edatatypeColumn_Book.__init__(edatatypeColumn_Book('\x00\x00', '', '', ''), '', '', '', '') == None

