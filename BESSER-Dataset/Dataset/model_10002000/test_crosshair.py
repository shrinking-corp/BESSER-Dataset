from python_code import ActionCard

def test_ActionCard___init__():
    assert ActionCard.__init__(ActionCard('', '', '\x00\x00'), '', '', '') == None


from python_code import Card
from python_code import Color

def test_Card___init__():
    assert Card.__init__(Card('', '', '', Color(), '', ''), '', '', '', Color(), '', '') == None


from python_code import Dealer

def test_Dealer___init__():
    assert Dealer.__init__(Dealer('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import DiscardPile

def test_DiscardPile___init__():
    assert DiscardPile.__init__(DiscardPile('', '', '\x00\x00'), '', '', '') == None


from python_code import DrawPile

def test_DrawPile___init__():
    assert DrawPile.__init__(DrawPile('', '', '\x00\x00'), '', '', '') == None


from python_code import Game

def test_Game___init__():
    assert Game.__init__(Game('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import GameElements
from python_code import int___1

def test_GameElements___init__():
    assert GameElements.__init__(GameElements('', '', '', '', '\x00', '', int___1(), '', '', ''), '', '', '', '', '', '\x00', int___1(), '', '', '') == None


from python_code import GameSession

def test_GameSession___init__():
    assert GameSession.__init__(GameSession('', '', '\x00\x00'), '', '', '') == None


from python_code import Main

def test_Main___init__():
    assert Main.__init__(Main('', '\x00'), '\x00\x00', '') == None


from python_code import NumberCard

def test_NumberCard___init__():
    assert NumberCard.__init__(NumberCard('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import Players

def test_Players___init__():
    assert Players.__init__(Players('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None


from python_code import WildCard

def test_WildCard___init__():
    assert WildCard.__init__(WildCard('', '\x00'), '\x00\x00', '') == None

