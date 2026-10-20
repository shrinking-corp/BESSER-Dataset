from python_code import Game

def test_Game___init__():
    assert Game.__init__(Game('', decks4=set(), players6=set()), '', decks4=set(), players6=set()) == None


from python_code import Game1

def test_Game1___init__():
    assert Game1.__init__(Game1('', decks28=set(), players30=set()), '', decks28=set(), players30=set()) == None


from python_code import Game2

def test_Game2___init__():
    assert Game2.__init__(Game2('', decks16=set(), players18=set()), '', decks16=set(), players18=set()) == None


from python_code import Avatar
from python_code import Player

def test_Player___init__():
    assert Player.__init__(Player('', games7=set(), cards8=set(), avatar10=Avatar()), '', games7=set(), cards8=set(), avatar10=Avatar()) == None


from python_code import Avatar1
from python_code import Player1

def test_Player1___init__():
    assert Player1.__init__(Player1('', '', games31=set(), cards32=set(), avatar34=Avatar1()), '', '', games31=set(), cards32=set(), avatar34=Avatar1()) == None


from python_code import Avatar2
from python_code import Player2

def test_Player2___init__():
    assert Player2.__init__(Player2('', games19=set(), cards20=set(), avatar22=Avatar2()), '', games19=set(), cards20=set(), avatar22=Avatar2()) == None

