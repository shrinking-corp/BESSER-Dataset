from python_code import A

def test_A___init__():
    assert A.__init__(A('', b0=set()), '', b0=set()) == None


from python_code import A2
from python_code import R

def test_A2___init__():
    assert A2.__init__(A2('', r5=R(), b6=set()), '', r5=R(), b6=set()) == None


from python_code import E
from python_code import G

def test_E___init__():
    assert E.__init__(E('', g17=G()), '', g17=G()) == None


from python_code import F

def test_F___init__():
    assert F.__init__(F(''), '') == None


from python_code import Union

def test_Union___init__():
    assert Union.__init__(Union('', pers13=set(), personnes15=set()), '', pers13=set(), personnes15=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

