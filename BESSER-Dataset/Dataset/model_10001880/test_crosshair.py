from python_code import Player

def test_Player___init__():
    assert Player.__init__(Player('\x00\x00', '', 0, 0), '', '', 0, 0) == None

