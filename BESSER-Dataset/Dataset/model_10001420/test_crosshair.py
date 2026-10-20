from python_code import Login_Process

def test_Login_Process___init__():
    assert Login_Process.__init__(Login_Process('', '\x00'), '\x00\x00', '') == None

