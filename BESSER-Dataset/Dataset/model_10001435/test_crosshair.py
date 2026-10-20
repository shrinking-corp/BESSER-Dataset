from python_code import User

def test_User___init__():
    assert User.__init__(User(0, '\x00'), 0, '\x00') == None

