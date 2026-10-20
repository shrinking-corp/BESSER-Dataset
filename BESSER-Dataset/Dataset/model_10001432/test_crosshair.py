from python_code import Login

def test_Login___init__():
    assert Login.__init__(Login('', '\x00'), '\x00\x00', '') == None


from python_code import RentalMobil

def test_RentalMobil___init__():
    assert RentalMobil.__init__(RentalMobil('\x00\x00', '', '', ''), '', '', '', '') == None

