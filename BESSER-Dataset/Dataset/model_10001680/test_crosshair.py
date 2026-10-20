from python_code import Book

def test_Book___init__():
    assert Book.__init__(Book(0, '', 0), 0, '', 0) == None


from python_code import librarian

def test_librarian___init__():
    assert librarian.__init__(librarian('', 0), '', 0) == None


from python_code import library_data_base

def test_library_data_base___init__():
    assert library_data_base.__init__(library_data_base('', '', 0), '\x00', '', 0) == None


from python_code import patron

def test_patron___init__():
    assert patron.__init__(patron('', '', 0), '\x00', '', 0) == None

