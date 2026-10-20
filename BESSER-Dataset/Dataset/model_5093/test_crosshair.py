from python_code import adl201_Interface

def test_adl201_Interface___init__():
    assert adl201_Interface.__init__(adl201_Interface('', '\x00'), '\x00\x00', '') == None

