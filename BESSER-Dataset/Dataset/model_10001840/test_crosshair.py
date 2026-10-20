from python_code import Admin

def test_Admin___init__():
    assert Admin.__init__(Admin(0, '', '', '', '', reservasiKamar27=set()), 0, '', '', '\x00', '', reservasiKamar27=set()) == None


from python_code import Pemesan

def test_Pemesan___init__():
    assert Pemesan.__init__(Pemesan(0, '', '', '', '\x00', '', '', reservasiKamar24=set()), 0, '', '', '', '', '', '', reservasiKamar24=set()) == None

