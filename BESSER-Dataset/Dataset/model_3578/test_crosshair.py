from python_code import typeA_BlockA
from python_code import typeA_PortA

def test_typeA_PortA___init__():
    assert typeA_PortA.__init__(typeA_PortA('', typeA_PortA=typeA_BlockA(), typeA_PortA3=typeA_BlockA()), '', typeA_PortA=typeA_BlockA(), typeA_PortA3=typeA_BlockA()) == None

