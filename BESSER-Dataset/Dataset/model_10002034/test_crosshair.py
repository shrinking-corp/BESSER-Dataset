from python_code import AdvSearch

def test_AdvSearch___init__():
    assert AdvSearch.__init__(AdvSearch('', '', '', '', '', bookSet13=set()), '', '', '', '\x00', '', bookSet13=set()) == None


from python_code import BookSet

def test_BookSet___init__():
    assert BookSet.__init__(BookSet(0, '', search10=set(), advSearch12=set()), 0, '', search10=set(), advSearch12=set()) == None


from python_code import Search

def test_Search___init__():
    assert Search.__init__(Search('\x00\x00', '', bookSet11=set()), '', '', bookSet11=set()) == None


from python_code import ShoppingCart

def test_ShoppingCart___init__():
    assert ShoppingCart.__init__(ShoppingCart('', 0, 0, booksOrder18=set(), customer21=set()), '', 0, 0, booksOrder18=set(), customer21=set()) == None

