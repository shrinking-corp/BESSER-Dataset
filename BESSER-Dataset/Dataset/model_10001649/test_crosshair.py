from python_code import A

def test_A___init__():
    assert A.__init__(A('', b0=set()), '', b0=set()) == None


from python_code import A1
from python_code import R

def test_A1___init__():
    assert A1.__init__(A1('', b6=set(), r9=R()), '', b6=set(), r9=R()) == None


from python_code import C1

def test_C1___init__():
    assert C1.__init__(C1(0, False, b5=set()), 0, False, b5=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

