from python_code import Library_Addressable

def test_Library_Addressable___init__():
    assert Library_Addressable.__init__(Library_Addressable(''), '') == None


from python_code import Library_AudioVisualItem

def test_Library_AudioVisualItem___init__():
    assert Library_AudioVisualItem.__init__(Library_AudioVisualItem('', 0, False), '\x00', 0, False) == None


from python_code import Library_Borrower
from python_code import Library_Lendable

def test_Library_Lendable___init__():
    assert Library_Lendable.__init__(Library_Lendable(0, borrowed=set(), Lendable=Library_Borrower()), 0, borrowed=set(), Lendable=Library_Borrower()) == None


from python_code import Library_Periodical

def test_Library_Periodical___init__():
    assert Library_Periodical.__init__(Library_Periodical('', 0), '', 0) == None


from python_code import Library_BookOnTape
from python_code import Library_Person
from python_code import Library_VideoCassette

def test_Library_Person___init__():
    assert Library_Person.__init__(Library_Person('', '\x00', Library_Person=Library_BookOnTape(), Library_Person22=Library_VideoCassette()), '\x00\x00', '', Library_Person=Library_BookOnTape(), Library_Person22=Library_VideoCassette()) == None

