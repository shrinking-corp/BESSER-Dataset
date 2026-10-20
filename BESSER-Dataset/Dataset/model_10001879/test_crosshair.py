from python_code import C3

def test_C3___init__():
    assert C3.__init__(C3(0, '\x00'), 0, '\x00') == None


from python_code import S1

def test_S1___init__():
    assert S1.__init__(S1('', '\x00'), '\x00\x00', '') == None

