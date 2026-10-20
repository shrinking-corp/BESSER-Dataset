from python_code import Analyse_Compte
from python_code import Analyse_Moderateurs
from python_code import Analyse_Utilisateur

def test_Analyse_Compte___init__():
    assert Analyse_Compte.__init__(Analyse_Compte('\x00\x00', '', est_associ_2=Analyse_Utilisateur(), poss_de4=set(), est_associ_9=Analyse_Moderateurs()), '', '', est_associ_2=Analyse_Utilisateur(), poss_de4=set(), est_associ_9=Analyse_Moderateurs()) == None


from python_code import Analyse_Criteres

def test_Analyse_Criteres___init__():
    assert Analyse_Criteres.__init__(Analyse_Criteres(0, 0, 0, 0, 0, sont_associ_s6=set()), 0, 0, 0, 0, 0, sont_associ_s6=set()) == None


from python_code import Analyse_Fast_Food

def test_Analyse_Fast_Food___init__():
    assert Analyse_Fast_Food.__init__(Analyse_Fast_Food('', '', 0, '', 0, 0, '', '', '\x00', '', '', poss_de1=set()), '', '', 0, '', 0, 0, '', '', '', '', '', poss_de1=set()) == None

