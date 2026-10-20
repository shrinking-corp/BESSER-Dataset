from python_code import Admin

def test_Admin___init__():
    assert Admin.__init__(Admin(0, '\x00', '', ''), 0, '', '', '') == None


from python_code import Banner

def test_Banner___init__():
    assert Banner.__init__(Banner('', 0, '', '', '', 0), '', 0, '', '', '\x00', 0) == None


from python_code import Color

def test_Color___init__():
    assert Color.__init__(Color('\x00\x00', '', inventory2=set()), '', '', inventory2=set()) == None


from python_code import Size

def test_Size___init__():
    assert Size.__init__(Size(0, '', inventory0=set()), 0, '', inventory0=set()) == None

