from python_code import BlackJack_Card

def test_BlackJack_Card___init__():
    assert BlackJack_Card.__init__(BlackJack_Card(0, '', 0, hand6=set()), 0, '', 0, hand6=set()) == None


from python_code import BlackJack_Deck
from python_code import BlackJack_House

def test_BlackJack_Deck___init__():
    assert BlackJack_Deck.__init__(BlackJack_Deck(0, game4=BlackJack_House()), 0, game4=BlackJack_House()) == None


from python_code import BlackJack_Game
from python_code import BlackJack_House

def test_BlackJack_Game___init__():
    assert BlackJack_Game.__init__(BlackJack_Game(False, house0=BlackJack_House(), player2=set()), False, house0=BlackJack_House(), player2=set()) == None


from python_code import BlackJack_Generic_Player

def test_BlackJack_Generic_Player___init__():
    assert BlackJack_Generic_Player.__init__(BlackJack_Generic_Player(0), 0) == None


from python_code import BlackJack_Card
from python_code import BlackJack_Hand

def test_BlackJack_Hand___init__():
    assert BlackJack_Hand.__init__(BlackJack_Hand(BlackJack_Card(0, '', 0, hand6=set()), card7=set()), BlackJack_Card(0, '', 0, hand6=set()), card7=set()) == None

