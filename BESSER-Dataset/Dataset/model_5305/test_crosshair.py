from python_code import typeB_ElementB
from python_code import typeB_RootB

def test_typeB_ElementB___init__():
    assert typeB_ElementB.__init__(typeB_ElementB('', typeB_ElementB=typeB_RootB()), '', typeB_ElementB=typeB_RootB()) == None

