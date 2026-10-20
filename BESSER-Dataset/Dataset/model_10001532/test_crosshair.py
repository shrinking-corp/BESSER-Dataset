from python_code import C

def test_C___init__():
    assert C.__init__(C(0, False, b5=set()), 0, False, b5=set()) == None


from python_code import y

def test_y___init__():
    assert y.__init__(y(''), '') == None

