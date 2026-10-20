from python_code import library_Book

def test_library_Book___init__():
    assert library_Book.__init__(library_Book('', 0, '', library_Book=set()), '', 0, '', library_Book=set()) == None


from python_code import library_Employee

def test_library_Employee___init__():
    assert library_Employee.__init__(library_Employee('', 0), '', 0) == None


from python_code import library_Library

def test_library_Library___init__():
    assert library_Library.__init__(library_Library('', '', library_Library2=set(), library_Library4=set(), library_Library=set()), '', '', library_Library2=set(), library_Library4=set(), library_Library=set()) == None


from python_code import library_Writer

def test_library_Writer___init__():
    assert library_Writer.__init__(library_Writer('', library_Writer=set()), '', library_Writer=set()) == None

