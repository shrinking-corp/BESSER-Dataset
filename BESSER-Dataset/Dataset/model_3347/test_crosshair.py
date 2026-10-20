from python_code import Map_Address
from python_code import Map_Map

def test_Map_Address___init__():
    assert Map_Address.__init__(Map_Address(0.0, 0.0, '', '', '', True, '', Map_Address=Map_Map()), 0.0, 0.0, '', '', '', False, '', Map_Address=Map_Map()) == None

