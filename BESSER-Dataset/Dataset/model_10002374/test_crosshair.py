from python_code import Clothes

def test_Clothes___init__():
    assert Clothes.__init__(Clothes('', '\x00'), '\x00\x00', '') == None


from python_code import Electronic

def test_Electronic___init__():
    assert Electronic.__init__(Electronic(''), '') == None


from python_code import Items
from python_code import OnlineShopping

def test_Items___init__():
    assert Items.__init__(Items(0, onlineShopping1=OnlineShopping()), 0, onlineShopping1=OnlineShopping()) == None

