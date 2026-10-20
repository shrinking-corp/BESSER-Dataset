from python_code import Buch

def test_Buch___init__():
    assert Buch.__init__(Buch('', '\x00'), '\x00\x00', '') == None


from python_code import Videos_DVDS

def test_Videos_DVDS___init__():
    assert Videos_DVDS.__init__(Videos_DVDS(0, '\x00', '', 0), 0, '', '', 0) == None


from python_code import Zeitschrift

def test_Zeitschrift___init__():
    assert Zeitschrift.__init__(Zeitschrift('', 0), '', 0) == None

