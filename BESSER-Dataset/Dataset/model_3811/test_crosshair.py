from python_code import example_Player

def test_example_Player___init__():
    assert example_Player.__init__(example_Player(''), '') == None

def test_example_Player_setCompression():
    assert example_Player.setCompression(example_Player('')) == None

