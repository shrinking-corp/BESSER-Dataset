from python_code import extralazy_Book

def test_extralazy_Book___init__():
    assert extralazy_Book.__init__(extralazy_Book('\x00\x00', '', extralazy_Book=set()), '', '', extralazy_Book=set()) == None

