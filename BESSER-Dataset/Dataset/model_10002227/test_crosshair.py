from python_code import A

def test_A___init__():
    assert A.__init__(A('\x00', b0=set()), '', b0=set()) == None


from python_code import C

def test_C___init__():
    assert C.__init__(C(0, False), 0, False) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None


from python_code import R
from python_code import a

def test_a___init__():
    assert a.__init__(a('', b2=set(), r5=R()), '', b2=set(), r5=R()) == None

