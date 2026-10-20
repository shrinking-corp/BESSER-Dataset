from python_code import remember_KeyIdPair
from python_code import remember_KeyManager

def test_remember_KeyIdPair___init__():
    assert remember_KeyIdPair.__init__(remember_KeyIdPair('', '\x00', remember_KeyIdPair=remember_KeyManager()), '\x00\x00', '', remember_KeyIdPair=remember_KeyManager()) == None

