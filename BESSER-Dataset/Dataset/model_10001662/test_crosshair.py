from python_code import A

def test_A___init__():
    assert A.__init__(A('', b0=set()), '', b0=set()) == None


from python_code import A1
from python_code import R

def test_A1___init__():
    assert A1.__init__(A1('\x00', b4=set(), r7=R()), '', b4=set(), r7=R()) == None


from python_code import C

def test_C___init__():
    assert C.__init__(C(0, False, b3=set()), 0, False, b3=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None


from python_code import c

def test_c___init__():
    assert c.__init__(c(0, False), 0, False) == None

