from python_code import Date_trajet

def test_Date_trajet___init__():
    assert Date_trajet.__init__(Date_trajet(0, '\x00', '', ''), 0, '', '', '') == None


from python_code import Utilisateur

def test_Utilisateur___init__():
    assert Utilisateur.__init__(Utilisateur(0, '', '', '', '', '', ''), 0, '\x00', '', '', '', '', '') == None

