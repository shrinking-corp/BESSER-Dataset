from python_code import adl203_Interface

def test_adl203_Interface___init__():
    assert adl203_Interface.__init__(adl203_Interface('', '\x00'), '\x00\x00', '') == None

