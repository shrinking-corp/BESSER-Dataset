from python_code import be_jebouquine_bo_LivreBO

def test_be_jebouquine_bo_LivreBO___init__():
    assert be_jebouquine_bo_LivreBO.__init__(be_jebouquine_bo_LivreBO(0), 0) == None


import datetime as _ch_datetime
from python_code import Collection_Livre_
from python_code import be_jebouquine_bo_PanierBO

def test_be_jebouquine_bo_PanierBO___init__():
    assert be_jebouquine_bo_PanierBO.__init__(be_jebouquine_bo_PanierBO(0, 0, _ch_datetime.date(1, 1, 1), Collection_Livre_()), 0, 0, _ch_datetime.date(1, 1, 2), Collection_Livre_()) == None


from python_code import be_jebouquine_entities_Administrateur

def test_be_jebouquine_entities_Administrateur___init__():
    assert be_jebouquine_entities_Administrateur.__init__(be_jebouquine_entities_Administrateur(0, '', '', '', ''), 0, '', '', '', '') == None


from python_code import be_jebouquine_entities_Client

def test_be_jebouquine_entities_Client___init__():
    assert be_jebouquine_entities_Client.__init__(be_jebouquine_entities_Client(0, '', '', '', '', '', '', commande12=set(), commentaire22=set()), 0, '', '', '', '', '\x00', '', commande12=set(), commentaire22=set()) == None


from python_code import be_jebouquine_entities_EtatCommande

def test_be_jebouquine_entities_EtatCommande___init__():
    assert be_jebouquine_entities_EtatCommande.__init__(be_jebouquine_entities_EtatCommande(0, '\x00', commande25=set()), 0, '', commande25=set()) == None


from python_code import be_jebouquine_entities_LivraisonType

def test_be_jebouquine_entities_LivraisonType___init__():
    assert be_jebouquine_entities_LivraisonType.__init__(be_jebouquine_entities_LivraisonType(0, '', 0.0, commande35=set()), 0, '', 0.0, commande35=set()) == None

