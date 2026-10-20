from python_code import Card

def test_Card___init__():
    assert Card.__init__(Card(False, 0, '', 0, deck0=set(), player3=set()), False, 0, '', 0, deck0=set(), player3=set()) == None


from python_code import Deck

def test_Deck___init__():
    assert Deck.__init__(Deck('\x00\x00', '', card1=set()), '', '', card1=set()) == None


from python_code import Player

def test_Player___init__():
    assert Player.__init__(Player('', '', '', card2=set()), '', '', '', card2=set()) == None

