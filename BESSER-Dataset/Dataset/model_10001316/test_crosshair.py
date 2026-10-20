from python_code import Hotel

def test_Hotel___init__():
    assert Hotel.__init__(Hotel('\x00', '', '', 0, 0, 0, '', room0=set(), service3=set()), '', '', '', 0, 0, 0, '', room0=set(), service3=set()) == None

