from python_code import Admin

def test_Admin___init__():
    assert Admin.__init__(Admin('', '\x00'), '\x00\x00', '') == None


from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer('', '', '', 0, '', order8=set()), '', '', '', 0, '', order8=set()) == None


from python_code import Customer1

def test_Customer1___init__():
    assert Customer1.__init__(Customer1('', '\x00'), '\x00\x00', '') == None


from python_code import Manager

def test_Manager___init__():
    assert Manager.__init__(Manager('', '\x00'), '\x00\x00', '') == None


from python_code import Manager1

def test_Manager1___init__():
    assert Manager1.__init__(Manager1(0, '', '\x00\x00'), 0, '', '') == None


from python_code import Manager2

def test_Manager2___init__():
    assert Manager2.__init__(Manager2(0, '', '', employee15=set()), 0, '', '', employee15=set()) == None


from python_code import Users

def test_Users___init__():
    assert Users.__init__(Users('', '\x00'), '\x00\x00', '') == None


from python_code import Users1

def test_Users1___init__():
    assert Users1.__init__(Users1('', '\x00'), '\x00\x00', '') == None

