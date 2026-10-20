from python_code import Convention

def test_Convention___init__():
    assert Convention.__init__(Convention('', 0), '', 0) == None


from python_code import Facture

def test_Facture___init__():
    assert Facture.__init__(Facture('', 0, False), '\x00', 0, False) == None


from python_code import Participant

def test_Participant___init__():
    assert Participant.__init__(Participant(0, '', '', '', sessions1=set()), 0, '', '', '', sessions1=set()) == None

