from python_code import A
from python_code import R

def test_A___init__():
    assert A.__init__(A('', r5=R(), b2=set()), '', r5=R(), b2=set()) == None


from python_code import A1
from python_code import B1

def test_A1___init__():
    assert A1.__init__(A1(False, 0, c6=B1()), False, 0, c6=B1()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

