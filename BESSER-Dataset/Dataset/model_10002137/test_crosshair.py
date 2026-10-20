from python_code import Cards_Card

def test_Cards_Card___init__():
    assert Cards_Card.__init__(Cards_Card(0), 0) == None


from python_code import Cards_Deck

def test_Cards_Deck___init__():
    assert Cards_Deck.__init__(Cards_Deck(''), '') == None


from python_code import Poker_Hand
from python_code import Poker_HandIterator

def test_Poker_Hand___init__():
    assert Poker_Hand.__init__(Poker_Hand(0, '', False, Poker_HandIterator(), Hand_HandIterator_00=Poker_HandIterator()), 0, '', False, Poker_HandIterator(), Hand_HandIterator_00=Poker_HandIterator()) == None


from python_code import Poker_Hand
from python_code import Poker_HandIterator
from python_code import Poker_Player

def test_Poker_Player___init__():
    assert Poker_Player.__init__(Poker_Player(0, 0, Poker_Hand(0, '', False, Poker_HandIterator(), Hand_HandIterator_00=Poker_HandIterator())), 0, 0, Poker_Hand(0, '', False, Poker_HandIterator(), Hand_HandIterator_00=Poker_HandIterator())) == None


from python_code import Poker_PokerGame

def test_Poker_PokerGame___init__():
    assert Poker_PokerGame.__init__(Poker_PokerGame(0, 0), 0, 0) == None

