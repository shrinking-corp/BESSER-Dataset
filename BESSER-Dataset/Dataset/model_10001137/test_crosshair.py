from python_code import Card

def test_Card___init__():
    assert Card.__init__(Card(0, 0, 0), 0, 0, 0) == None


from python_code import Card
from python_code import Dealer
from python_code import Deck

def test_Dealer___init__():
    assert Dealer.__init__(Dealer(Deck(Card(0, 0, 0))), Deck(Card(0, 0, 0))) == None


from python_code import Card
from python_code import Deck

def test_Deck___init__():
    assert Deck.__init__(Deck(Card(0, 0, 0)), Card(0, 0, 0)) == None


from python_code import Card
from python_code import Player

def test_Player___init__():
    assert Player.__init__(Player(Card(0, 0, 0), False), Card(0, 0, 0), True) == None

