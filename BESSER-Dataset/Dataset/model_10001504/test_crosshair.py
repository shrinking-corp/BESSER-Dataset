from python_code import A
from python_code import R

def test_A___init__():
    assert A.__init__(A('', r5=R()), '', r5=R()) == None


from python_code import Union

def test_Union___init__():
    assert Union.__init__(Union(0, pers9=set(), personne11=set()), 0, pers9=set(), personne11=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y('', b2=set()), '', b2=set()) == None

