from python_code import expressions_Feature
from python_code import expressions_Function
from python_code import expressions_QuantifyOperator

def test_expressions_Feature___init__():
    assert expressions_Feature.__init__(expressions_Feature('', expressions_Feature=expressions_Function(), expressions_Feature14=expressions_QuantifyOperator()), '', expressions_Feature=expressions_Function(), expressions_Feature14=expressions_QuantifyOperator()) == None


from python_code import expressions_Number

def test_expressions_Number___init__():
    assert expressions_Number.__init__(expressions_Number(0), 0) == None


from python_code import expressions_Quantity

def test_expressions_Quantity___init__():
    assert expressions_Quantity.__init__(expressions_Quantity(0), 0) == None

