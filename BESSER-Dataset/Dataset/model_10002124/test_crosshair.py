from python_code import BlackJackApp
from python_code import BlackJack_Hra

def test_BlackJack_Hra___init__():
    assert BlackJack_Hra.__init__(BlackJack_Hra('', '', '', '', '', '', '', '', '\x00', '', '', '', '', blackJackApp1=BlackJackApp()), '', '', '', '', '', '', '', '', '', '', '', '\x00', '', blackJackApp1=BlackJackApp()) == None


from python_code import Card

def test_Card___init__():
    assert Card.__init__(Card(0, '', '\x00\x00'), 0, '', '') == None


from python_code import Deck

def test_Deck___init__():
    assert Deck.__init__(Deck('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None


from python_code import Hand

def test_Hand___init__():
    assert Hand.__init__(Hand(0, 0, '', '', False, '', '', False, ''), 0, 0, '', '', False, '', '', False, '') == None

