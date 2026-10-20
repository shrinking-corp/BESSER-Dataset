from python_code import droneDSL_DecollerAtterrir

def test_droneDSL_DecollerAtterrir___init__():
    assert droneDSL_DecollerAtterrir.__init__(droneDSL_DecollerAtterrir(''), '') == None


from python_code import droneDSL_FinDeMain
from python_code import droneDSL_Main

def test_droneDSL_FinDeMain___init__():
    assert droneDSL_FinDeMain.__init__(droneDSL_FinDeMain('', droneDSL_FinDeMain=droneDSL_Main()), '', droneDSL_FinDeMain=droneDSL_Main()) == None


from python_code import droneDSL_FonctionCallInterne
from python_code import droneDSL_FonctionDecl
from python_code import droneDSL_Model

def test_droneDSL_FonctionDecl___init__():
    assert droneDSL_FonctionDecl.__init__(droneDSL_FonctionDecl('', droneDSL_FonctionDecl=droneDSL_Model(), droneDSL_FonctionDecl79=set(), droneDSL_FonctionDecl81=droneDSL_FonctionCallInterne()), '', droneDSL_FonctionDecl=droneDSL_Model(), droneDSL_FonctionDecl79=set(), droneDSL_FonctionDecl81=droneDSL_FonctionCallInterne()) == None


from python_code import droneDSL_PourcentConst
from python_code import droneDSL_PourcentDecl
from python_code import droneDSL_Pourcent_vitesse_deplacement_max
from python_code import droneDSL_Pourcent_vitesse_hauteur_max
from python_code import droneDSL_Pourcent_vitesse_rotation_max

def test_droneDSL_PourcentConst___init__():
    assert droneDSL_PourcentConst.__init__(droneDSL_PourcentConst('', droneDSL_PourcentConst=droneDSL_Pourcent_vitesse_hauteur_max(), droneDSL_PourcentConst9=droneDSL_Pourcent_vitesse_deplacement_max(), droneDSL_PourcentConst11=droneDSL_Pourcent_vitesse_rotation_max(), droneDSL_PourcentConst33=droneDSL_PourcentDecl()), '', droneDSL_PourcentConst=droneDSL_Pourcent_vitesse_hauteur_max(), droneDSL_PourcentConst9=droneDSL_Pourcent_vitesse_deplacement_max(), droneDSL_PourcentConst11=droneDSL_Pourcent_vitesse_rotation_max(), droneDSL_PourcentConst33=droneDSL_PourcentDecl()) == None


from python_code import droneDSL_Eloignement_max
from python_code import droneDSL_Hauteur_max
from python_code import droneDSL_SecondeConst
from python_code import droneDSL_SecondeDecl

def test_droneDSL_SecondeConst___init__():
    assert droneDSL_SecondeConst.__init__(droneDSL_SecondeConst('', droneDSL_SecondeConst=droneDSL_Hauteur_max(), droneDSL_SecondeConst14=droneDSL_Eloignement_max(), droneDSL_SecondeConst31=droneDSL_SecondeDecl()), '', droneDSL_SecondeConst=droneDSL_Hauteur_max(), droneDSL_SecondeConst14=droneDSL_Eloignement_max(), droneDSL_SecondeConst31=droneDSL_SecondeDecl()) == None


from python_code import droneDSL_VarDecl

def test_droneDSL_VarDecl___init__():
    assert droneDSL_VarDecl.__init__(droneDSL_VarDecl(''), '') == None

