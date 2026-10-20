from python_code import library_Addressable

def test_library_Addressable___init__():
    assert library_Addressable.__init__(library_Addressable(''), '') == None


from python_code import library_AudioVisualItem

def test_library_AudioVisualItem___init__():
    assert library_AudioVisualItem.__init__(library_AudioVisualItem('', 0, False), '\x00', 0, False) == None


from python_code import library_Borrower
from python_code import library_Lendable

def test_library_Lendable___init__():
    assert library_Lendable.__init__(library_Lendable(0, borrowed=set(), Lendable=library_Borrower()), 0, borrowed=set(), Lendable=library_Borrower()) == None


from python_code import library_Periodical

def test_library_Periodical___init__():
    assert library_Periodical.__init__(library_Periodical('', 0), '', 0) == None


from python_code import library_BookOnTape
from python_code import library_Person
from python_code import library_VideoCassette

def test_library_Person___init__():
    assert library_Person.__init__(library_Person('', '\x00', library_Person=library_BookOnTape(), library_Person22=library_VideoCassette()), '\x00\x00', '', library_Person=library_BookOnTape(), library_Person22=library_VideoCassette()) == None

