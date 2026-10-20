from python_code import Administrator

def test_Administrator___init__():
    assert Administrator.__init__(Administrator(0, '\x00', '', ''), 0, '', '', '') == None


from python_code import User

def test_User___init__():
    assert User.__init__(User(0, '', '', '', ''), 0, '', '', '', '') == None

