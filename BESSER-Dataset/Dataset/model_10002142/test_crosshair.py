from python_code import PASSENGER

def test_PASSENGER___init__():
    assert PASSENGER.__init__(PASSENGER('', 0, '\x00\x00'), '', 0, '') == None

