from python_code import Chat

def test_Chat___init__():
    assert Chat.__init__(Chat('', '\x00'), '\x00\x00', '') == None

