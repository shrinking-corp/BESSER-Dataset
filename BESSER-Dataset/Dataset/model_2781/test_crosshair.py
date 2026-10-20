from python_code import p_A
from python_code import p_B
from python_code import p_C

def test_p_A___init__():
    assert p_A.__init__(p_A(True, p_A=p_B(), p_A5=p_C()), False, p_A=p_B(), p_A5=p_C()) == None

