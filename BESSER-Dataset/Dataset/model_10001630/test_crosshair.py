from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y('', '\x00'), '\x00\x00', '') == None
