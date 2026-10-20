from python_code import Library_Book
from python_code import Library_Library

def test_Library_Book___init__():
    assert Library_Book.__init__(Library_Book('', Library_Book=Library_Library()), '', Library_Book=Library_Library()) == None

