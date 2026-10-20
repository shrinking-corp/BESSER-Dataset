from python_code import A

def test_A___init__():
    assert A.__init__(A('', b0=set()), '', b0=set()) == None


from python_code import A1
from python_code import R

def test_A1___init__():
    assert A1.__init__(A1('', r13=R(), b14=set(), b8=set()), '', r13=R(), b14=set(), b8=set()) == None


from python_code import A2

def test_A2___init__():
    assert A2.__init__(A2('', b4=set()), '', b4=set()) == None


from python_code import A5

def test_A5___init__():
    assert A5.__init__(A5('', b24=set()), '', b24=set()) == None


from python_code import Union1

def test_Union1___init__():
    assert Union1.__init__(Union1('', pers29=set(), personne31=set()), '', pers29=set(), personne31=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

