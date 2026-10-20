from python_code import Korisnik_IS

def test_Korisnik_IS___init__():
    assert Korisnik_IS.__init__(Korisnik_IS(0, '', '', '', '', aran_man9=set()), 0, '', '', '\x00', '', aran_man9=set()) == None


from python_code import Osiguranje

def test_Osiguranje___init__():
    assert Osiguranje.__init__(Osiguranje(0, '', '', kupac4=set()), 0, '', '', kupac4=set()) == None


from python_code import Putovanje

def test_Putovanje___init__():
    assert Putovanje.__init__(Putovanje(0, '', '', sme_taj0=set(), aran_man3=set()), 0, '', '', sme_taj0=set(), aran_man3=set()) == None

