from python_code import A
from python_code import R

def test_A___init__():
    assert A.__init__(A('', b0=set(), r5=R()), '', b0=set(), r5=R()) == None


from python_code import A1
from python_code import B1

def test_A1___init__():
    assert A1.__init__(A1(0, c6=B1()), 0, c6=B1()) == None


from python_code import A2

def test_A2___init__():
    assert A2.__init__(A2(True), False) == None


from python_code import E

def test_E___init__():
    assert E.__init__(E(''), '') == None


from python_code import F

def test_F___init__():
    assert F.__init__(F(''), '') == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

