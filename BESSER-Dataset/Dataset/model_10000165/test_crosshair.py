from python_code import Al_player

def test_Al_player___init__():
    assert Al_player.__init__(Al_player(0, 0), 0, 0) == None


from python_code import Deck1

def test_Deck1___init__():
    assert Deck1.__init__(Deck1(0), 0) == None


from python_code import Dealer_Type_Interface
from python_code import Pitch1

def test_Pitch1___init__():
    assert Pitch1.__init__(Pitch1(Dealer_Type_Interface()), Dealer_Type_Interface()) == None


from python_code import Player1

def test_Player1___init__():
    assert Player1.__init__(Player1('', 0, 0), '\x00', 0, 0) == None


from python_code import Rank1

def test_Rank1___init__():
    assert Rank1.__init__(Rank1(0), 0) == None

