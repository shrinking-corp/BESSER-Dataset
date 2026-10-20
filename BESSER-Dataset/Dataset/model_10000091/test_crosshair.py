from python_code import Destinacija

def test_Destinacija___init__():
    assert Destinacija.__init__(Destinacija(0, '', '', hotel0=set(), rezervisanje3=set()), 0, '', '', hotel0=set(), rezervisanje3=set()) == None


from python_code import Korisnik_IS

def test_Korisnik_IS___init__():
    assert Korisnik_IS.__init__(Korisnik_IS(0, '', '', '', '', rezervisanje9=set()), 0, '', '', '\x00', '', rezervisanje9=set()) == None


from python_code import Osiguranje

def test_Osiguranje___init__():
    assert Osiguranje.__init__(Osiguranje(0, '\x00', putnik4=set()), 0, '', putnik4=set()) == None

