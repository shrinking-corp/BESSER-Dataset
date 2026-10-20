from python_code import adl200_Interface

def test_adl200_Interface___init__():
    assert adl200_Interface.__init__(adl200_Interface('', '\x00'), '\x00\x00', '') == None

