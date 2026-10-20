from python_code import extlibrary_Addressable

def test_extlibrary_Addressable___init__():
    assert extlibrary_Addressable.__init__(extlibrary_Addressable(''), '') == None


from python_code import extlibrary_AudioVisualItem

def test_extlibrary_AudioVisualItem___init__():
    assert extlibrary_AudioVisualItem.__init__(extlibrary_AudioVisualItem('', 0, False), '\x00', 0, False) == None


import datetime as _ch_datetime
from python_code import extlibrary_Item

def test_extlibrary_Item___init__():
    assert extlibrary_Item.__init__(extlibrary_Item(_ch_datetime.date(1, 1, 2)), _ch_datetime.date(1, 1, 1)) == None


from python_code import extlibrary_Borrower
from python_code import extlibrary_Lendable

def test_extlibrary_Lendable___init__():
    assert extlibrary_Lendable.__init__(extlibrary_Lendable(0, Lendable=extlibrary_Borrower(), borrowed=set()), 0, Lendable=extlibrary_Borrower(), borrowed=set()) == None


from python_code import extlibrary_Periodical

def test_extlibrary_Periodical___init__():
    assert extlibrary_Periodical.__init__(extlibrary_Periodical('', 0), '', 0) == None


from python_code import extlibrary_BookOnTape
from python_code import extlibrary_Person
from python_code import extlibrary_VideoCassette

def test_extlibrary_Person___init__():
    assert extlibrary_Person.__init__(extlibrary_Person('', '\x00', extlibrary_Person7=extlibrary_VideoCassette(), extlibrary_Person=extlibrary_BookOnTape()), '\x00\x00', '', extlibrary_Person7=extlibrary_VideoCassette(), extlibrary_Person=extlibrary_BookOnTape()) == None

