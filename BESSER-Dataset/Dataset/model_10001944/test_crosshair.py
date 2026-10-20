from python_code import Examen

def test_Examen___init__():
    assert Examen.__init__(Examen(0, '', '', '', ''), 0, '', '', '', '') == None


from python_code import Groupe

def test_Groupe___init__():
    assert Groupe.__init__(Groupe(0, 0, '', suivre8=set(), candidat3=set()), 0, 0, '', suivre8=set(), candidat3=set()) == None


from python_code import Personne

def test_Personne___init__():
    assert Personne.__init__(Personne(0, '', '', '', '\x00', '', '', '', 0), 0, '', '', '', '', '\x00', '', '', 0) == None


from python_code import Professeur

def test_Professeur___init__():
    assert Professeur.__init__(Professeur('', donner4=set(), dispenser6=set()), '', donner4=set(), dispenser6=set()) == None


from python_code import Utilisateur

def test_Utilisateur___init__():
    assert Utilisateur.__init__(Utilisateur('', '\x00'), '\x00\x00', '') == None


from python_code import Voiture

def test_Voiture___init__():
    assert Voiture.__init__(Voiture(0, '', '', '', coursConduite1=set()), 0, '', '', '', coursConduite1=set()) == None


from python_code import cours

def test_cours___init__():
    assert cours.__init__(cours(0, '\x00', '', ''), 0, '', '', '') == None

