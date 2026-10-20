from python_code import library_Book
from python_code import library_Library

def test_library_Book___init__():
    assert library_Book.__init__(library_Book('\x00\x00', 0, library_Book=set(), library_Book2=library_Library()), '', 0, library_Book=set(), library_Book2=library_Library()) == None

