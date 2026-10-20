from python_code import Conducteur
from python_code import Lieu
from python_code import Trajet1

def test_Trajet1___init__():
    assert Trajet1.__init__(Trajet1(Lieu(), Lieu(), '\x00\x00', '', passager2=set(), conducteur6=Conducteur()), Lieu(), Lieu(), '', '', passager2=set(), conducteur6=Conducteur()) == None


from python_code import Utilisateur1

def test_Utilisateur1___init__():
    assert Utilisateur1.__init__(Utilisateur1('', 0, '\x00\x00'), '', 0, '') == None


from python_code import Conducteur
from python_code import V_hicule

def test_V_hicule___init__():
    assert V_hicule.__init__(V_hicule('', '', '\x00\x00', Conducteur(), conducteur4=Conducteur()), '', '', '', Conducteur(), conducteur4=Conducteur()) == None

