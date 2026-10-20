from python_code import Class4
from python_code import Room

def test_Room___init__():
    assert Room.__init__(Room('\x00', teacher1=set(), class42=Class4()), '', teacher1=set(), class42=Class4()) == None

