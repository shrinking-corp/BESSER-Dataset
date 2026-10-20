from python_code import extlibrary_Addressable

def test_extlibrary_Addressable___init__():
    assert extlibrary_Addressable.__init__(extlibrary_Addressable(''), '') == None


from python_code import extlibrary_AudioVisualItem

def test_extlibrary_AudioVisualItem___init__():
    assert extlibrary_AudioVisualItem.__init__(extlibrary_AudioVisualItem('', 0, False), '\x00', 0, False) == None


from python_code import extlibrary_Borrower
from python_code import extlibrary_Lendable

def test_extlibrary_Lendable___init__():
    assert extlibrary_Lendable.__init__(extlibrary_Lendable(0, borrowed=set(), Lendable=extlibrary_Borrower()), 0, borrowed=set(), Lendable=extlibrary_Borrower()) == None


from python_code import extlibrary_Periodical

def test_extlibrary_Periodical___init__():
    assert extlibrary_Periodical.__init__(extlibrary_Periodical('', 0), '', 0) == None

