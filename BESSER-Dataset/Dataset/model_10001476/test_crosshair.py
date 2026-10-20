from python_code import User

def test_User___init__():
    assert User.__init__(User('\x00\x00', '', '', ''), '', '', '', '') == None

