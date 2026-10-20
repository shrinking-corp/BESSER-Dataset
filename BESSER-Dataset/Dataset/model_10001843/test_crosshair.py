from python_code import A

def test_A___init__():
    assert A.__init__(A('', b1=set()), '', b1=set()) == None


from python_code import Abis
from python_code import R

def test_Abis___init__():
    assert Abis.__init__(Abis('', b4=set(), r9=R()), '', b4=set(), r9=R()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

