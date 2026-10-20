from python_code import A
from python_code import R

def test_A___init__():
    assert A.__init__(A('', r1=R(), b2=set()), '', r1=R(), b2=set()) == None


from python_code import Union

def test_Union___init__():
    assert Union.__init__(Union('', pers9=set(), personnes11=set()), '', pers9=set(), personnes11=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

