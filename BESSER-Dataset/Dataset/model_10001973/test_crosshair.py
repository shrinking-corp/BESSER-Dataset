from python_code import AIplayer

def test_AIplayer___init__():
    assert AIplayer.__init__(AIplayer('', '\x00'), '\x00\x00', '') == None


from python_code import ConsolePlayer

def test_ConsolePlayer___init__():
    assert ConsolePlayer.__init__(ConsolePlayer('', '\x00'), '\x00\x00', '') == None


from python_code import RandomPlayer

def test_RandomPlayer___init__():
    assert RandomPlayer.__init__(RandomPlayer('', '\x00'), '\x00\x00', '') == None


from python_code import MainMenuGUI
from python_code import ScoreBoardGUI

def test_ScoreBoardGUI___init__():
    assert ScoreBoardGUI.__init__(ScoreBoardGUI('', player2=set(), mainMenuGUI12=MainMenuGUI()), '', player2=set(), mainMenuGUI12=MainMenuGUI()) == None

