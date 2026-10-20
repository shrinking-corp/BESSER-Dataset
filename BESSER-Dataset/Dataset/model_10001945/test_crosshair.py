from python_code import Connect4_CirclePanel

def test_Connect4_CirclePanel___init__():
    assert Connect4_CirclePanel.__init__(Connect4_CirclePanel('\x00\x00', 0, connect4=set()), '', 0, connect4=set()) == None

