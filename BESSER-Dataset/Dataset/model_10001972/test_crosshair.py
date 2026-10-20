from python_code import Attempt

def test_Attempt___init__():
    assert Attempt.__init__(Attempt(0, 0), 0, 0) == None


from python_code import FileImporter

def test_FileImporter___init__():
    assert FileImporter.__init__(FileImporter(''), '') == None


from python_code import Game

def test_Game___init__():
    assert Game.__init__(Game(0, 0), 0, 0) == None


from python_code import InitialData

def test_InitialData___init__():
    assert InitialData.__init__(InitialData('', '\x00'), '\x00\x00', '') == None


from python_code import Match
from python_code import Result

def test_Match___init__():
    assert Match.__init__(Match('', '', '', Result('', 0)), '', '', '', Result('', 0)) == None


from python_code import Game
from python_code import Player

def test_Player___init__():
    assert Player.__init__(Player('\x00\x00', 0, Game(0, 0)), '', 0, Game(0, 0)) == None


from python_code import Result

def test_Result___init__():
    assert Result.__init__(Result('', 0), '', 0) == None

