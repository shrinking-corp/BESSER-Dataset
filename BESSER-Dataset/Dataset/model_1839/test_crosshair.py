from python_code import book_Book
from python_code import book_BookCollection
from python_code import book_EObject

def test_book_Book___init__():
    assert book_Book.__init__(book_Book('', 0, book_Book=book_BookCollection(), book_Book2=book_EObject()), '', 0, book_Book=book_BookCollection(), book_Book2=book_EObject()) == None

