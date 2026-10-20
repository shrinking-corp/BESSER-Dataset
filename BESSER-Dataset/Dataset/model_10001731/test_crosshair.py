from python_code import Book

def test_Book___init__():
    assert Book.__init__(Book(0, '', '', 0, 0, bookBorrow28=set(), library32=set()), 0, '', '', 0, 0, bookBorrow28=set(), library32=set()) == None


from python_code import BookBorrow
from python_code import Enter__Username_UseCase

def test_BookBorrow___init__():
    assert BookBorrow.__init__(BookBorrow(0, '', '', 0, Enter__Username_UseCase(), book29=set(), user30=set()), 0, '', '', 0, Enter__Username_UseCase(), book29=set(), user30=set()) == None


from python_code import Guest

def test_Guest___init__():
    assert Guest.__init__(Guest(0), 0) == None


from python_code import Librarian

def test_Librarian___init__():
    assert Librarian.__init__(Librarian(0, '\x00'), 0, '\x00') == None


from python_code import Library

def test_Library___init__():
    assert Library.__init__(Library(0, '', book33=set(), person34=set()), 0, '', book33=set(), person34=set()) == None


from python_code import Person

def test_Person___init__():
    assert Person.__init__(Person(0, '', '', 0, library35=set()), 0, '', '', 0, library35=set()) == None


from python_code import User

def test_User___init__():
    assert User.__init__(User(0, '', False, '', '\x00', '', 0, bookBorrow31=set()), 0, '', False, '', '', '', 0, bookBorrow31=set()) == None

