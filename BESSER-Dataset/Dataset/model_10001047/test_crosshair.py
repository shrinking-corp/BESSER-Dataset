from python_code import Admin

def test_Admin___init__():
    assert Admin.__init__(Admin('', '\x00'), '\x00\x00', '') == None

from python_code import Login

def test_Login___init__():
    assert Login.__init__(Login('', '\x00'), '\x00\x00', '') == None
