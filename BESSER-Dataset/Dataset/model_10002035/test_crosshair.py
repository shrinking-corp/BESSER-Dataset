from python_code import Login

def test_Login___init__():
    assert Login.__init__(Login('', '\x00'), '\x00\x00', '') == None


from python_code import public

def test_public___init__():
    assert public.__init__(public(''), '') == None


from python_code import secret

def test_secret___init__():
    assert secret.__init__(secret(''), '') == None

