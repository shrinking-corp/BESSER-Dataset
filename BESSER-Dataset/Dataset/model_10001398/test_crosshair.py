from python_code import user

def test_user___init__():
    assert user.__init__(user(0, '\x00', '', ''), 0, '', '', '') == None

