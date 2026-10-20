from python_code import Gambler

def test_Gambler___init__():
    assert Gambler.__init__(Gambler(0, '', False, handDeck4=set()), 0, '', True, handDeck4=set()) == None


from python_code import JokerCard

def test_JokerCard___init__():
    assert JokerCard.__init__(JokerCard(True), False) == None


from python_code import Deck
from python_code import PlayingCard

def test_PlayingCard___init__():
    assert PlayingCard.__init__(PlayingCard(True, deck7=Deck()), False, deck7=Deck()) == None


from python_code import TEHandDeck

def test_TEHandDeck___init__():
    assert TEHandDeck.__init__(TEHandDeck(0), 0) == None

