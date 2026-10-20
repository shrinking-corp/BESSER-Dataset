from python_code import user

def test_user___init__():
    assert user.__init__(user('\x00\x00', '', '', ''), '', '', '', '') == None

