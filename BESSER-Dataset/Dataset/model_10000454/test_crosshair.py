from python_code import Administrator

def test_Administrator___init__():
    assert Administrator.__init__(Administrator('', '\x00'), '\x00\x00', '') == None


from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer('', '', '\x00', '', '', 0, shoppingCart0=set(), order2=set()), '', '', '', '', '', 0, shoppingCart0=set(), order2=set()) == None


from python_code import Shopping

def test_Shopping___init__():
    assert Shopping.__init__(Shopping('', '', 0), '\x00', '', 0) == None


from python_code import Users

def test_Users___init__():
    assert Users.__init__(Users('\x00\x00', '', '', 0), '', '', '', 0) == None

