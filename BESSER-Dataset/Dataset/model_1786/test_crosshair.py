from python_code import column_Book

def test_column_Book___init__():
    assert column_Book.__init__(column_Book('\x00\x00', '', '', ''), '', '', '', '') == None

