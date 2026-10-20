from python_code import Room

def test_Room___init__():
    assert Room.__init__(Room(0, 0, reservation11=set()), 0, 0, reservation11=set()) == None

