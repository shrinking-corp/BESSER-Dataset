from python_code import Engine

def test_Engine___init__():
    assert Engine.__init__(Engine('', 0, 0), '\x00', 0, 0) == None


from python_code import Engine
from python_code import M6

def test_M6___init__():
    assert M6.__init__(M6('', '', Engine('', 0, 0)), '', '', Engine('', 0, 0)) == None


from python_code import Engine
from python_code import Tennis

def test_Tennis___init__():
    assert Tennis.__init__(Tennis('', '', Engine('', 0, 0)), '', '', Engine('', 0, 0)) == None


from python_code import Car
from python_code import TestStand

def test_TestStand___init__():
    assert TestStand.__init__(TestStand(Car()), Car()) == None

