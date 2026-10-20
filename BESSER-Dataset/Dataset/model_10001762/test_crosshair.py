from python_code import Card

def test_Card___init__():
    assert Card.__init__(Card('', '\x00'), '\x00\x00', '') == None


from python_code import Deck

def test_Deck___init__():
    assert Deck.__init__(Deck(''), '') == None

