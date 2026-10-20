from python_code import BomberMan

def test_BomberMan___init__():
    assert BomberMan.__init__(BomberMan(0, 0, '\x00\x00'), 0, 0, '') == None


from python_code import Game

def test_Game___init__():
    assert Game.__init__(Game(0), 0) == None


from python_code import GameMap

def test_GameMap___init__():
    assert GameMap.__init__(GameMap('', '', '\x00\x00'), '', '', '') == None


from python_code import Monster

def test_Monster___init__():
    assert Monster.__init__(Monster('\x00\x00', '', '', 0), '', '', '', 0) == None


from python_code import PowerUps

def test_PowerUps___init__():
    assert PowerUps.__init__(PowerUps('', '', 0), '\x00', '', 0) == None

