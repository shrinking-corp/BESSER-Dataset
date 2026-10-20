from python_code import library_Addressable

def test_library_Addressable___init__():
    assert library_Addressable.__init__(library_Addressable(''), '') == None


from python_code import library_IncBook
from python_code import library_Writer

def test_library_IncBook___init__():
    assert library_IncBook.__init__(library_IncBook('\x00\x00', 0, books=set(), IncBook=library_Writer()), '', 0, books=set(), IncBook=library_Writer()) == None


from python_code import library_Borrower
from python_code import library_Lendable

def test_library_Lendable___init__():
    assert library_Lendable.__init__(library_Lendable(0, Lendable=library_Borrower(), borrowing=set()), 0, Lendable=library_Borrower(), borrowing=set()) == None


from python_code import library_Person

def test_library_Person___init__():
    assert library_Person.__init__(library_Person('', '\x00'), '\x00\x00', '') == None

