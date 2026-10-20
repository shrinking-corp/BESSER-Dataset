from python_code import book_Fade

def test_book_Fade___init__():
    assert book_Fade.__init__(book_Fade(0.0, 0.0), 0.0, 0.0) == None


from python_code import book_JSAction

def test_book_JSAction___init__():
    assert book_JSAction.__init__(book_JSAction(''), '') == None


from python_code import book_Label

def test_book_Label___init__():
    assert book_Label.__init__(book_Label('', '\x00'), '\x00\x00', '') == None


from python_code import book_Media

def test_book_Media___init__():
    assert book_Media.__init__(book_Media('\x00\x00', False, 0, 0), '', False, 0, 0) == None


from python_code import book_Move

def test_book_Move___init__():
    assert book_Move.__init__(book_Move('', '\x00'), '\x00\x00', '') == None


from python_code import book_Group
from python_code import book_Node

def test_book_Node___init__():
    assert book_Node.__init__(book_Node(True, 0.0, '', '', '', book_Node=book_Group()), False, 0.0, '', '', '', book_Node=book_Group()) == None


from python_code import book_Rotation

def test_book_Rotation___init__():
    assert book_Rotation.__init__(book_Rotation(0.0, 0.0), 0.0, 0.0) == None


from python_code import book_Shape

def test_book_Shape___init__():
    assert book_Shape.__init__(book_Shape(0, '\x00'), 0, '\x00') == None

