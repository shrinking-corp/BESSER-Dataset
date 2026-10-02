from python_code import Interieur

def test_Interieur___init__():
    assert Interieur.__init__(Interieur(0), 0) == None

from python_code import Observable

def test_Observable___init__():
    assert Observable.__init__(Observable(''), '') == None

from python_code import Position

def test_Position___init__():
    assert Position.__init__(Position(0), 0) == None

from python_code import Toit

def test_Toit___init__():
    assert Toit.__init__(Toit(0), 0) == None
