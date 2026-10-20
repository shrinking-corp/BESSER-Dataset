from python_code import adl202_Interface

def test_adl202_Interface___init__():
    assert adl202_Interface.__init__(adl202_Interface('', '\x00'), '\x00\x00', '') == None

