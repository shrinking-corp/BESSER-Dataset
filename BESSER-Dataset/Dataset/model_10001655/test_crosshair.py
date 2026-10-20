from python_code import A

def test_A___init__():
    assert A.__init__(A('', b0=set()), '', b0=set()) == None


from python_code import A1
from python_code import R

def test_A1___init__():
    assert A1.__init__(A1('', b4=set(), r9=R()), '', b4=set(), r9=R()) == None


from python_code import E

def test_E___init__():
    assert E.__init__(E(''), '') == None


from python_code import F

def test_F___init__():
    assert F.__init__(F(''), '') == None


from python_code import Union

def test_Union___init__():
    assert Union.__init__(Union('', pers11=set(), personnes13=set()), '', pers11=set(), personnes13=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

