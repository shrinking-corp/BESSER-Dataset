from python_code import books_Book
from python_code import books_Catalog

def test_books_Book___init__():
    assert books_Book.__init__(books_Book('', '', 0, books_Book=books_Catalog(), books=set()), '', '', 0, books_Book=books_Catalog(), books=set()) == None

