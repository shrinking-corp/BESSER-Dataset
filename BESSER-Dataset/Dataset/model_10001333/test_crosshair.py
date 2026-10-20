from python_code import library_management__Library

def test_library_management__Library___init__():
    assert library_management__Library.__init__(library_management__Library('', '', '', '', ''), '', '', '', '', '') == None


from python_code import library_management__librarian

def test_library_management__librarian___init__():
    assert library_management__librarian.__init__(library_management__librarian(0), 0) == None


from python_code import library_management__patron

def test_library_management__patron___init__():
    assert library_management__patron.__init__(library_management__patron(0), 0) == None

