from python_code import myDsl_AffectVar
from python_code import myDsl_Commande
from python_code import myDsl_Commandes
from python_code import myDsl_For
from python_code import myDsl_Foreach
from python_code import myDsl_If
from python_code import myDsl_While

def test_myDsl_Commande___init__():
    assert myDsl_Commande.__init__(myDsl_Commande('', myDsl_Commande=myDsl_Commandes(), myDsl_Commande13=myDsl_Commandes(), myDsl_Commande15=myDsl_AffectVar(), myDsl_Commande17=myDsl_While(), myDsl_Commande19=myDsl_For(), myDsl_Commande21=myDsl_If(), myDsl_Commande23=myDsl_Foreach()), '', myDsl_Commande=myDsl_Commandes(), myDsl_Commande13=myDsl_Commandes(), myDsl_Commande15=myDsl_AffectVar(), myDsl_Commande17=myDsl_While(), myDsl_Commande19=myDsl_For(), myDsl_Commande21=myDsl_If(), myDsl_Commande23=myDsl_Foreach()) == None


from python_code import myDsl_AffectVar
from python_code import myDsl_Vars

def test_myDsl_Vars___init__():
    assert myDsl_Vars.__init__(myDsl_Vars('', '\x00', myDsl_Vars=myDsl_AffectVar()), '\x00\x00', '', myDsl_Vars=myDsl_AffectVar()) == None

