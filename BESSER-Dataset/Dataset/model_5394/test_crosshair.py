from python_code import b_B

def test_b_B___init__():
    assert b_B.__init__(b_B('', '\x00'), '\x00\x00', '') == None

