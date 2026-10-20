from python_code import Card
from python_code import Deck

def test_Card___init__():
    assert Card.__init__(Card(0, 0, deck1=Deck()), 0, 0, deck1=Deck()) == None


from python_code import Deck
from python_code import GUI
from python_code import GameBoard

def test_GameBoard___init__():
    assert GameBoard.__init__(GameBoard('', '', '', deck2=Deck(), gUI6=GUI(), player9=set()), '', '', '', deck2=Deck(), gUI6=GUI(), player9=set()) == None

