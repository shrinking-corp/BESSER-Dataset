from python_code import droneDSLLib_DecollerAtterrir

def test_droneDSLLib_DecollerAtterrir___init__():
    assert droneDSLLib_DecollerAtterrir.__init__(droneDSLLib_DecollerAtterrir(''), '') == None


from python_code import droneDSLLib_FonctionCallInterne
from python_code import droneDSLLib_FonctionDecl
from python_code import droneDSLLib_Model

def test_droneDSLLib_FonctionDecl___init__():
    assert droneDSLLib_FonctionDecl.__init__(droneDSLLib_FonctionDecl('', droneDSLLib_FonctionDecl=droneDSLLib_Model(), droneDSLLib_FonctionDecl48=set(), droneDSLLib_FonctionDecl50=droneDSLLib_FonctionCallInterne()), '', droneDSLLib_FonctionDecl=droneDSLLib_Model(), droneDSLLib_FonctionDecl48=set(), droneDSLLib_FonctionDecl50=droneDSLLib_FonctionCallInterne()) == None


from python_code import droneDSLLib_PourcentConst
from python_code import droneDSLLib_PourcentDecl

def test_droneDSLLib_PourcentConst___init__():
    assert droneDSLLib_PourcentConst.__init__(droneDSLLib_PourcentConst('', droneDSLLib_PourcentConst=droneDSLLib_PourcentDecl()), '', droneDSLLib_PourcentConst=droneDSLLib_PourcentDecl()) == None


from python_code import droneDSLLib_SecondeConst
from python_code import droneDSLLib_SecondeDecl

def test_droneDSLLib_SecondeConst___init__():
    assert droneDSLLib_SecondeConst.__init__(droneDSLLib_SecondeConst('', droneDSLLib_SecondeConst=droneDSLLib_SecondeDecl()), '', droneDSLLib_SecondeConst=droneDSLLib_SecondeDecl()) == None


from python_code import droneDSLLib_VarDecl

def test_droneDSLLib_VarDecl___init__():
    assert droneDSLLib_VarDecl.__init__(droneDSLLib_VarDecl(''), '') == None

