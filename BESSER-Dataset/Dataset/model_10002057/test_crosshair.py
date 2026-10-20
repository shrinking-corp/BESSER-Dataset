from python_code import Docter

def test_Docter___init__():
    assert Docter.__init__(Docter(0, '', '', '', '', '', patient0=set()), 0, '\x00', '', '', '', '', patient0=set()) == None


from python_code import Hospital

def test_Hospital___init__():
    assert Hospital.__init__(Hospital('', '', '\x00\x00'), '', '', '') == None

