from python_code import e_X

def test_e_X___init__():
    assert e_X.__init__(e_X()) == None

def test_e_X_bar():
    assert e_X.bar(e_X(), '') == None


from python_code import e_Y

def test_e_Y___init__():
    assert e_Y.__init__(e_Y(''), '') == None

