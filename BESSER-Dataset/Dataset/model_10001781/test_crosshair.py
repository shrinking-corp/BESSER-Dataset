from python_code import Card

def test_Card___init__():
    assert Card.__init__(Card(0, '\x00'), 0, '\x00') == None


from python_code import CasinoManager
from python_code import Deck
from python_code import Table

def test_CasinoManager___init__():
    assert CasinoManager.__init__(CasinoManager(Table(Deck(''), ''), '\x00\x00'), Table(Deck(''), ''), '') == None


from python_code import Deck

def test_Deck___init__():
    assert Deck.__init__(Deck(''), '') == None


from python_code import Deck
from python_code import Table

def test_Table___init__():
    assert Table.__init__(Table(Deck(''), '\x00'), Deck('\x00\x00'), '') == None

