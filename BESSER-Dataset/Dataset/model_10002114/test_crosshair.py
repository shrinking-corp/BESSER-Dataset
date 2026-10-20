from python_code import Colonist
from python_code import Game_Building
from python_code import Game_ColonistZone

def test_Game_Building___init__():
    assert Game_Building.__init__(Game_Building('', 0, 0, 0, Game_ColonistZone(False, Colonist(), 0), 0, False), '', 0, 0, 0, Game_ColonistZone(False, Colonist(), 0), 0, False) == None


from python_code import Colonist
from python_code import Game_ColonistShip
from python_code import Game_ColonistZone

def test_Game_ColonistShip___init__():
    assert Game_ColonistShip.__init__(Game_ColonistShip(Game_ColonistZone(False, Colonist(), 0), 0), Game_ColonistZone(False, Colonist(), 0), 0) == None


from python_code import Colonist
from python_code import Game_ColonistZone

def test_Game_ColonistZone___init__():
    assert Game_ColonistZone.__init__(Game_ColonistZone(False, Colonist(), 0), False, Colonist(), 0) == None


from python_code import Game_GoodZone
from python_code import Good

def test_Game_GoodZone___init__():
    assert Game_GoodZone.__init__(Game_GoodZone(True, Good()), False, Good()) == None


from python_code import Colonist
from python_code import Game_ColonistZone
from python_code import Game_PlayerBoard

def test_Game_PlayerBoard___init__():
    assert Game_PlayerBoard.__init__(Game_PlayerBoard(0, Game_ColonistZone(False, Colonist(), 0)), 0, Game_ColonistZone(False, Colonist(), 0)) == None


from python_code import Game_ShippingShip

def test_Game_ShippingShip___init__():
    assert Game_ShippingShip.__init__(Game_ShippingShip(0), 0) == None

