from python_code import Game

def test_Game___init__():
    assert Game.__init__(Game('', players6=set(), decks8=set()), '', players6=set(), decks8=set()) == None


from python_code import Avatar
from python_code import Player

def test_Player___init__():
    assert Player.__init__(Player('', cards10=set(), avatar4=Avatar(), games7=set()), '', cards10=set(), avatar4=Avatar(), games7=set()) == None

