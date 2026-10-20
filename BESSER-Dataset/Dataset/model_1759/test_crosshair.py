from python_code import library_book

def test_library_book___init__():
    assert library_book.__init__(library_book('\x00\x00', '', '', ''), '', '', '', '') == None

