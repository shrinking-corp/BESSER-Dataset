from python_code import gx10_IntConst

def test_gx10_IntConst___init__():
    assert gx10_IntConst.__init__(gx10_IntConst(0), 0) == None


from python_code import gx10_Expression
from python_code import gx10_Print

def test_gx10_Print___init__():
    assert gx10_Print.__init__(gx10_Print(gx10_Print=gx10_Expression()), gx10_Print=gx10_Expression()) == None

def test_gx10_Print_print():
    assert gx10_Print.print(gx10_Print(gx10_Print=gx10_Expression())) == None

