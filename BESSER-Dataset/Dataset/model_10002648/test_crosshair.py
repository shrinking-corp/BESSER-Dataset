from python_code import Connect4_Board

def test_Connect4_Board___init__():
    assert Connect4_Board.__init__(Connect4_Board(0, 0, '', token0=set(), player2=set()), 0, 0, '', token0=set(), player2=set()) == None


from python_code import Connect4_CirclePanel

def test_Connect4_CirclePanel___init__():
    assert Connect4_CirclePanel.__init__(Connect4_CirclePanel('', 0), '', 0) == None


from python_code import Connect4_connect

def test_Connect4_connect___init__():
    assert Connect4_connect.__init__(Connect4_connect(0, 0, 0, 0, 0, 0, '', '', '', '', '\x00', ''), 0, 0, 0, 0, 0, 0, '', '', '', '', '', '') == None

