from python_code import Book_Book

def test_Book_Book___init__():
    assert Book_Book.__init__(Book_Book('', book=set()), '', book=set()) == None


from python_code import Book
from python_code import Book_Chapter

def test_Book_Chapter___init__():
    assert Book_Chapter.__init__(Book_Chapter('', '', '\x00\x00', chapters=Book()), '', '', '', chapters=Book()) == None

