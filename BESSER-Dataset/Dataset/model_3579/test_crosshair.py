from python_code import TypeA_BlockA
from python_code import TypeA_PortA

def test_TypeA_PortA___init__():
    assert TypeA_PortA.__init__(TypeA_PortA('', TypeA_PortA=TypeA_BlockA(), TypeA_PortA3=TypeA_BlockA()), '', TypeA_PortA=TypeA_BlockA(), TypeA_PortA3=TypeA_BlockA()) == None

