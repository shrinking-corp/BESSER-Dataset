from python_code import Book_Book

def test_Book_Book___init__():
    assert Book_Book.__init__(Book_Book('', 0, False, True, Book_Book=set()), '', 0, False, False, Book_Book=set()) == None

