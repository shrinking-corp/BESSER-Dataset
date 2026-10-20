from python_code import realop_IsNegative

def test_realop_IsNegative___init__():
    assert realop_IsNegative.__init__(realop_IsNegative(''), '') == None


from python_code import realop_IsPositive

def test_realop_IsPositive___init__():
    assert realop_IsPositive.__init__(realop_IsPositive(''), '') == None


from python_code import realop_IsRealised

def test_realop_IsRealised___init__():
    assert realop_IsRealised.__init__(realop_IsRealised(''), '') == None


from python_code import realop_Expression
from python_code import realop_Operator
from python_code import realop_Realop

def test_realop_Operator___init__():
    assert realop_Operator.__init__(realop_Operator('', realop_Operator=realop_Realop(), realop_Operator2=realop_Expression(), realop_Operator4=realop_Expression()), '', realop_Operator=realop_Realop(), realop_Operator2=realop_Expression(), realop_Operator4=realop_Expression()) == None

