from python_code import dummy_F

def test_dummy_F___init__():
    assert dummy_F.__init__(dummy_F('\x00', 0.0), '', 0.0) == None


from python_code import dummy_G

def test_dummy_G___init__():
    assert dummy_G.__init__(dummy_G(''), '') == None

