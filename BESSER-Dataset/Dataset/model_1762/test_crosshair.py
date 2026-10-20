from python_code import Book_Book
from python_code import Book_Library

def test_Book_Book___init__():
    assert Book_Book.__init__(Book_Book('', '', 0, Book_Book=Book_Library(), Book_Book4=set(), Book_Book7=set()), '', '', 0, Book_Book=Book_Library(), Book_Book4=set(), Book_Book7=set()) == None


from python_code import Book_Paragraph

def test_Book_Paragraph___init__():
    assert Book_Paragraph.__init__(Book_Paragraph(''), '') == None


from python_code import Book_Section

def test_Book_Section___init__():
    assert Book_Section.__init__(Book_Section(''), '') == None

