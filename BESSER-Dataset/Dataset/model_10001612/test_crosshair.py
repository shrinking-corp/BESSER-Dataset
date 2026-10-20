from python_code import Librarian
from python_code import log

def test_Librarian___init__():
    assert Librarian.__init__(Librarian(0, '', '\x00\x00', log3=log()), 0, '', '', log3=log()) == None

