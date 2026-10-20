from python_code import A
from python_code import R

def test_A___init__():
    assert A.__init__(A('\x00', r1=R(), b2=set()), '', r1=R(), b2=set()) == None


from python_code import C

def test_C___init__():
    assert C.__init__(C(0, False), 0, False) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

