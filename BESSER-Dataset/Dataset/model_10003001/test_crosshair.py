from python_code import Conducteur
from python_code import Lieu
from python_code import Trajet1

def test_Trajet1___init__():
    assert Trajet1.__init__(Trajet1(Lieu(), Lieu(), '\x00\x00', '', passager2=set(), conducteur6=Conducteur()), Lieu(), Lieu(), '', '', passager2=set(), conducteur6=Conducteur()) == None


from python_code import Conducteur1
from python_code import Lieu
from python_code import Trajet2

def test_Trajet2___init__():
    assert Trajet2.__init__(Trajet2(Lieu(), Lieu(), '', '', 0, 0, '', conducteur17=Conducteur1(), passager19=set()), Lieu(), Lieu(), '', '', 0, 0, '', conducteur17=Conducteur1(), passager19=set()) == None


from python_code import Utilisateur

def test_Utilisateur___init__():
    assert Utilisateur.__init__(Utilisateur('', '', '\x00', 0, trajet8=set(), voiture10=set(), avis0=set()), '', '', '', 0, trajet8=set(), voiture10=set(), avis0=set()) == None


from python_code import Utilisateur1

def test_Utilisateur1___init__():
    assert Utilisateur1.__init__(Utilisateur1('', 0, '\x00\x00'), '', 0, '') == None


from python_code import Utilisateur2

def test_Utilisateur2___init__():
    assert Utilisateur2.__init__(Utilisateur2('', 0, '', '', 0, avis12=set()), '', 0, '', '\x00', 0, avis12=set()) == None


from python_code import Conducteur
from python_code import V_hicule

def test_V_hicule___init__():
    assert V_hicule.__init__(V_hicule('', '', '\x00\x00', Conducteur(), conducteur4=Conducteur()), '', '', '', Conducteur(), conducteur4=Conducteur()) == None


from python_code import Conducteur1
from python_code import V_hicule1

def test_V_hicule1___init__():
    assert V_hicule1.__init__(V_hicule1('\x00\x00', '', '', Conducteur1(), 0, conducteur15=Conducteur1()), '', '', '', Conducteur1(), 0, conducteur15=Conducteur1()) == None

