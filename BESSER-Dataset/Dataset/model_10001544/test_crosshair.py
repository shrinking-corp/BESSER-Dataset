from python_code import Cards

def test_Cards___init__():
    assert Cards.__init__(Cards('', 0), '', 0) == None


from python_code import BlackjackGame
from python_code import Dealer
from python_code import Integer_external

def test_Dealer___init__():
    assert Dealer.__init__(Dealer(0, 0, hand1=Integer_external(), blackjackGame5=BlackjackGame()), 0, 0, hand1=Integer_external(), blackjackGame5=BlackjackGame()) == None


from python_code import Deck
from python_code import _Interface

def test_Deck___init__():
    assert Deck.__init__(Deck(0, 0, association2_111=_Interface()), 0, 0, association2_111=_Interface()) == None


from python_code import Hand

def test_Hand___init__():
    assert Hand.__init__(Hand(0, player7=set()), 0, player7=set()) == None

