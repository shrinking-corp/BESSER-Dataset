from python_code import FACULTY

def test_FACULTY___init__():
    assert FACULTY.__init__(FACULTY('\x00\x00', '', sTUDENT40=set()), '', '', sTUDENT40=set()) == None


from python_code import STUDENT

def test_STUDENT___init__():
    assert STUDENT.__init__(STUDENT('\x00\x00', '', fACULTY41=set()), '', '', fACULTY41=set()) == None

