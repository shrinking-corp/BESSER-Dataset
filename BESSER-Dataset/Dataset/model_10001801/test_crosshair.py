from python_code import Deck

def test_Deck___init__():
    assert Deck.__init__(Deck('\x00\x00', 0, card1=set()), '', 0, card1=set()) == None


from python_code import Player

def test_Player___init__():
    assert Player.__init__(Player('', '\x00'), '\x00\x00', '') == None

