from python_code import Authenticate_staff

def test_Authenticate_staff___init__():
    assert Authenticate_staff.__init__(Authenticate_staff('', '', '\x00\x00'), '', '', '') == None


from python_code import Login

def test_Login___init__():
    assert Login.__init__(Login('', '\x00'), '\x00\x00', '') == None

