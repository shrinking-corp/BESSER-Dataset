from python_code import Admin

def test_Admin___init__():
    assert Admin.__init__(Admin('', '\x00'), '\x00\x00', '') == None


from python_code import User

def test_User___init__():
    assert User.__init__(User(0, 0, '\x00\x00'), 0, 0, '') == None

