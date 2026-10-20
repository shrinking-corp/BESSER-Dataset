from python_code import A
from python_code import R

def test_A___init__():
    assert A.__init__(A('', r1=R(), b4=set()), '', r1=R(), b4=set()) == None


from python_code import E
from python_code import G

def test_E___init__():
    assert E.__init__(E('', g13=G()), '', g13=G()) == None


from python_code import F

def test_F___init__():
    assert F.__init__(F(''), '') == None


from python_code import Union

def test_Union___init__():
    assert Union.__init__(Union('', pers9=set(), personne11=set()), '', pers9=set(), personne11=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

