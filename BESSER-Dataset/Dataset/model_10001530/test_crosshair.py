from python_code import Card

def test_Card___init__():
    assert Card.__init__(Card(0), 0) == None


from python_code import Card
from python_code import Deck

def test_Deck___init__():
    assert Deck.__init__(Deck(Card(0)), Card(0)) == None


from python_code import Card
from python_code import Deck
from python_code import Game

def test_Game___init__():
    assert Game.__init__(Game(Deck(Card(0)), Deck(Card(0)), Card(0)), Deck(Card(0)), Deck(Card(0)), Card(0)) == None

