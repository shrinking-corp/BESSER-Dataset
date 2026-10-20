from python_code import ADMIN

def test_ADMIN___init__():
    assert ADMIN.__init__(ADMIN('', '', eMPLOYEE2=set(), sTUDENT4=set()), '', '', eMPLOYEE2=set(), sTUDENT4=set()) == None


from python_code import VALIDATE

def test_VALIDATE___init__():
    assert VALIDATE.__init__(VALIDATE('', '\x00'), '\x00\x00', '') == None

