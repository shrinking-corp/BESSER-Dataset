from python_code import Admin

def test_Admin___init__():
    assert Admin.__init__(Admin('', '\x00'), '\x00\x00', '') == None

