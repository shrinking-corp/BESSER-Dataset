from python_code import Keluar

def test_Keluar___init__():
    assert Keluar.__init__(Keluar(''), '') == None


from python_code import Login

def test_Login___init__():
    assert Login.__init__(Login('', '\x00'), '\x00\x00', '') == None


from python_code import Login1

def test_Login1___init__():
    assert Login1.__init__(Login1('', '\x00'), '\x00\x00', '') == None

