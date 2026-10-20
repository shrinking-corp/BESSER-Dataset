from python_code import AcePile

def test_AcePile___init__():
    assert AcePile.__init__(AcePile(''), '') == None


from python_code import Card

def test_Card___init__():
    assert Card.__init__(Card('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', False, False, '', '\x00', '', '', '', '', '', '', '', ''), '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', False, False, '', '', '', '\x00', '', '', '', '', '', '') == None


from python_code import CardStack

def test_CardStack___init__():
    assert CardStack.__init__(CardStack(''), '') == None


from python_code import ChangeAppearance

def test_ChangeAppearance___init__():
    assert ChangeAppearance.__init__(ChangeAppearance('', '', '', '', '', '', '', '', '', False, '\x00', ''), '', '', '', '', '', '', '', '', '', True, '', '') == None


from python_code import ChangeOptions

def test_ChangeOptions___init__():
    assert ChangeOptions.__init__(ChangeOptions('', '', False, '', '\x00', '', '', '', '', '', '', '', '', '', ''), '', '', False, '', '', '\x00', '', '', '', '', '', '', '', '', '') == None


from python_code import DealDeck

def test_DealDeck___init__():
    assert DealDeck.__init__(DealDeck('\x00', '', '', '', '', '', '', '', '', '', False), '', '', '', '', '', '', '', '', '', '', False) == None


from python_code import Deck

def test_Deck___init__():
    assert Deck.__init__(Deck('', '\x00'), '\x00\x00', '') == None


from python_code import DiscardPile

def test_DiscardPile___init__():
    assert DiscardPile.__init__(DiscardPile('', '\x00'), '\x00\x00', '') == None


from python_code import FireworksDisplay

def test_FireworksDisplay___init__():
    assert FireworksDisplay.__init__(FireworksDisplay('', '', '', '', '', '', '\x00', '', '', '', '', '', '', ''), '', '', '', '', '', '', '', '', '\x00', '', '', '', '', '') == None


from python_code import FourRowSolitaire

def test_FourRowSolitaire___init__():
    assert FourRowSolitaire.__init__(FourRowSolitaire('', '', '', '', '', '', '\x00', '', '', '', '', '', '', ''), '', '', '', '', '', '', '', '', '\x00', '', '', '', '', '') == None


from python_code import MyMouseListener

def test_MyMouseListener___init__():
    assert MyMouseListener.__init__(MyMouseListener(False, False, '', '', '', '', '\x00', False), False, False, '', '', '', '', '', False) == None


from python_code import DealDeck
from python_code import Deck
from python_code import SolitaireBoard

def test_SolitaireBoard___init__():
    assert SolitaireBoard.__init__(SolitaireBoard('', '', '\x00', True, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', Deck('', ''), '', '', DealDeck('', '', '', '', '', '', '', '', '', '', False), '', '\x00', '', '', '', '', ''), '', '', '', True, '', '', '', '', '', '', '', '', '\x00\x00', '', '\x00', '', '', '', '', Deck('', ''), '', '', DealDeck('', '', '', '', '', '', '', '', '\x01', '', False), '', '', '', '', '', '\x00', '') == None


from python_code import SolitaireLayout

def test_SolitaireLayout___init__():
    assert SolitaireLayout.__init__(SolitaireLayout('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''), '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '') == None


from python_code import SolitairePanel

def test_SolitairePanel___init__():
    assert SolitairePanel.__init__(SolitairePanel('', '\x00'), '\x00\x00', '') == None


from python_code import SoundThread

def test_SoundThread___init__():
    assert SoundThread.__init__(SoundThread(''), '') == None


from python_code import WinScreen

def test_WinScreen___init__():
    assert WinScreen.__init__(WinScreen(''), '') == None

