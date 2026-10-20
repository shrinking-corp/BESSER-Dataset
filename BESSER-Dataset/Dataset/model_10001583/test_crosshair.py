from python_code import Card

def test_Card___init__():
    assert Card.__init__(Card('', '', 0), '\x00', '', 0) == None


from python_code import Deck

def test_Deck___init__():
    assert Deck.__init__(Deck(''), '') == None


from python_code import Player

def test_Player___init__():
    assert Player.__init__(Player('', '\x00'), '\x00\x00', '') == None


from python_code import Rules

def test_Rules___init__():
    assert Rules.__init__(Rules('', False), '', False) == None

