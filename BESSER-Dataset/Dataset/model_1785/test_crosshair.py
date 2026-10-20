from python_code import Book_Book

def test_Book_Book___init__():
    assert Book_Book.__init__(Book_Book('\x00\x00', '', Book_Book=set()), '', '', Book_Book=set()) == None

