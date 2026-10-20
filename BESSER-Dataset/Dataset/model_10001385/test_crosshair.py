from python_code import Personne

def test_Personne___init__():
    assert Personne.__init__(Personne('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import Test

def test_Test___init__():
    assert Test.__init__(Test(''), '') == None

