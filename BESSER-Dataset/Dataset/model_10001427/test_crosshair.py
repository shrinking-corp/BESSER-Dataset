from python_code import Login

def test_Login___init__():
    assert Login.__init__(Login('', '', '\x00\x00'), '', '', '') == None

