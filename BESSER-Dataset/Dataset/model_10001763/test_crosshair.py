from python_code import Association

def test_Association___init__():
    assert Association.__init__(Association('', membre0=set(), service3=set()), '', membre0=set(), service3=set()) == None


from python_code import CompteDeLUtilisateur

def test_CompteDeLUtilisateur___init__():
    assert CompteDeLUtilisateur.__init__(CompteDeLUtilisateur('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import CompteDeLUtilisateur1

def test_CompteDeLUtilisateur1___init__():
    assert CompteDeLUtilisateur1.__init__(CompteDeLUtilisateur1('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import Contacter
from python_code import Utilisateur

def test_Contacter___init__():
    assert Contacter.__init__(Contacter(Utilisateur()), Utilisateur()) == None


from python_code import CritereDeRecherche

def test_CritereDeRecherche___init__():
    assert CritereDeRecherche.__init__(CritereDeRecherche(''), '') == None


from python_code import Membre

def test_Membre___init__():
    assert Membre.__init__(Membre('', association1=set(), service5=set()), '', association1=set(), service5=set()) == None


from python_code import RechercheDAssociations

def test_RechercheDAssociations___init__():
    assert RechercheDAssociations.__init__(RechercheDAssociations(''), '') == None


from python_code import RechercheDemandes

def test_RechercheDemandes___init__():
    assert RechercheDemandes.__init__(RechercheDemandes(''), '') == None


from python_code import RecherchePropositions

def test_RecherchePropositions___init__():
    assert RecherchePropositions.__init__(RecherchePropositions(''), '') == None


from python_code import RechercheRapide

def test_RechercheRapide___init__():
    assert RechercheRapide.__init__(RechercheRapide(''), '') == None


import datetime as _ch_datetime
from python_code import Association
from python_code import Recherche_Avanc_e

def test_Recherche_Avanc_e___init__():
    assert Recherche_Avanc_e.__init__(Recherche_Avanc_e('', Association('', membre0=set(), service3=set()), '', 0, _ch_datetime.date(1, 1, 1)), '', Association('\x00', membre0=set(), service3=set()), '', 0, _ch_datetime.date(1, 1, 1)) == None


from python_code import Recherche_Rapide

def test_Recherche_Rapide___init__():
    assert Recherche_Rapide.__init__(Recherche_Rapide(''), '') == None


from python_code import Resultat
from python_code import Resultat_Recherche

def test_Resultat___init__():
    assert Resultat.__init__(Resultat(Resultat_Recherche()), Resultat_Recherche()) == None


from python_code import __table___T_CompteDeLUtilisateur

def test___table___T_CompteDeLUtilisateur___init__():
    assert __table___T_CompteDeLUtilisateur.__init__(__table___T_CompteDeLUtilisateur(0, '', '', '', ''), 0, '', '', '', '') == None


import datetime as _ch_datetime
from python_code import __table___T_Services

def test___table___T_Services___init__():
    assert __table___T_Services.__init__(__table___T_Services(0, 0, '', '', '', 0, _ch_datetime.date(1, 1, 1)), 0, 0, '', '\x00', '', 0, _ch_datetime.date(1, 1, 1)) == None

