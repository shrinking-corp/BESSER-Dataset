from python_code import cards_Deck

def test_cards_Deck___init__():
    assert cards_Deck.__init__(cards_Deck('', 0), '', 0) == None


from python_code import cards_PokerHand

def test_cards_PokerHand___init__():
    assert cards_PokerHand.__init__(cards_PokerHand('', 0), '', 0) == None


from python_code import cards_PokerHand
from python_code import game_Ranker

def test_game_Ranker___init__():
    assert game_Ranker.__init__(game_Ranker(cards_PokerHand('', 0), 0), cards_PokerHand('\x00', 0), 0) == None


from python_code import cards_CardsGUI
from python_code import game_GameBoardGUI
from python_code import main_Play
from python_code import players_PlayerVersionGUI

def test_main_Play___init__():
    assert main_Play.__init__(main_Play('', players_PlayerVersionGUI(), game_GameBoardGUI(), cards_CardsGUI()), '', players_PlayerVersionGUI(), game_GameBoardGUI(), cards_CardsGUI()) == None


from python_code import players_Person

def test_players_Person___init__():
    assert players_Person.__init__(players_Person('', '\x00'), '\x00\x00', '') == None


from python_code import cards_PokerHand
from python_code import players_Player

def test_players_Player___init__():
    assert players_Player.__init__(players_Player(cards_PokerHand('\x00\x00', 0), False, 0), cards_PokerHand('', 0), False, 0) == None

