from python_code import Board

def test_Board___init__():
    assert Board.__init__(Board('', '\x00'), '\x00\x00', '') == None


from python_code import card_Card

def test_card_Card___init__():
    assert card_Card.__init__(card_Card(0, 0), 0, 0) == None


from python_code import player_Deck

def test_player_Deck___init__():
    assert player_Deck.__init__(player_Deck(0, 0, 0, 0), 0, 0, 0, 0) == None


from python_code import poker_Game

def test_poker_Game___init__():
    assert poker_Game.__init__(poker_Game(0, 0), 0, 0) == None

