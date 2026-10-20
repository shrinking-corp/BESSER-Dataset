from python_code import typeA_ElementA
from python_code import typeA_RootA

def test_typeA_ElementA___init__():
    assert typeA_ElementA.__init__(typeA_ElementA('', typeA_ElementA=typeA_RootA()), '', typeA_ElementA=typeA_RootA()) == None

