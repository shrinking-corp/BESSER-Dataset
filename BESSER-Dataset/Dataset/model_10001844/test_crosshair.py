from python_code import A
from python_code import R

def test_A___init__():
    assert A.__init__(A('', r1=R(), b2=set()), '', r1=R(), b2=set()) == None


from python_code import A1
from python_code import B1

def test_A1___init__():
    assert A1.__init__(A1(False, B1(), 0, b16=set()), False, B1(), 0, b16=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

