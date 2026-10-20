from python_code import gx10_False

def test_gx10_False___init__():
    assert gx10_False.__init__(gx10_False()) == None

def test_gx10_False_getCurrentValue():
    assert gx10_False.getCurrentValue(gx10_False()) == None


from python_code import gx10_IntConst

def test_gx10_IntConst___init__():
    assert gx10_IntConst.__init__(gx10_IntConst(True), False) == None

def test_gx10_IntConst_getCurrentValue():
    assert gx10_IntConst.getCurrentValue(gx10_IntConst(False)) == None


from python_code import gx10_Plus

def test_gx10_Plus___init__():
    assert gx10_Plus.__init__(gx10_Plus()) == None

def test_gx10_Plus_evaluate():
    assert gx10_Plus.evaluate(gx10_Plus()) == None

def test_gx10_Plus_getCurrentValue():
    assert gx10_Plus.getCurrentValue(gx10_Plus()) == None


from python_code import gx10_Expression
from python_code import gx10_Print

def test_gx10_Print___init__():
    assert gx10_Print.__init__(gx10_Print(gx10_Print=gx10_Expression()), gx10_Print=gx10_Expression()) == None

def test_gx10_Print_print():
    assert gx10_Print.print(gx10_Print(gx10_Print=gx10_Expression())) == None


from python_code import gx10_Time

def test_gx10_Time___init__():
    assert gx10_Time.__init__(gx10_Time()) == None

def test_gx10_Time_evaluate():
    assert gx10_Time.evaluate(gx10_Time()) == None

def test_gx10_Time_getCurrentValue():
    assert gx10_Time.getCurrentValue(gx10_Time()) == None


from python_code import gx10_True

def test_gx10_True___init__():
    assert gx10_True.__init__(gx10_True()) == None

def test_gx10_True_getCurrentValue():
    assert gx10_True.getCurrentValue(gx10_True()) == None

