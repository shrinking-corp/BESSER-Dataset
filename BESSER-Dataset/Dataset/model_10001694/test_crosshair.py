from python_code import Game_GUI
from python_code import Main_MainGame

def test_Main_MainGame___init__():
    assert Main_MainGame.__init__(Main_MainGame('', Game_GUI(), 0, 0, 0, 0, gUI3=Game_GUI()), '', Game_GUI(), 0, 0, 0, 0, gUI3=Game_GUI()) == None


from python_code import Players_Person

def test_Players_Person___init__():
    assert Players_Person.__init__(Players_Person('', '\x00'), '\x00\x00', '') == None

