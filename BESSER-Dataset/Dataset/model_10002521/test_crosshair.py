from python_code import administrator

def test_administrator___init__():
    assert administrator.__init__(administrator('', '\x00'), '\x00\x00', '') == None

