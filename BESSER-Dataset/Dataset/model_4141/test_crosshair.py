from python_code import arithmetic_AbstractDefinition
from python_code import arithmetic_FunctionCall

def test_arithmetic_AbstractDefinition___init__():
    assert arithmetic_AbstractDefinition.__init__(arithmetic_AbstractDefinition('', arithmetic_AbstractDefinition=arithmetic_FunctionCall()), '', arithmetic_AbstractDefinition=arithmetic_FunctionCall()) == None


from python_code import arithmetic_Import
from python_code import arithmetic_Module

def test_arithmetic_Module___init__():
    assert arithmetic_Module.__init__(arithmetic_Module('', arithmetic_Module=set(), arithmetic_Module2=set(), arithmetic_Module5=arithmetic_Import()), '', arithmetic_Module=set(), arithmetic_Module2=set(), arithmetic_Module5=arithmetic_Import()) == None


from python_code import arithmetic_NumberLiteral

def test_arithmetic_NumberLiteral___init__():
    assert arithmetic_NumberLiteral.__init__(arithmetic_NumberLiteral(0), 0) == None


from python_code import arithmetic_DeclaredParameter
from python_code import arithmetic_Expression
from python_code import arithmetic_SumExpression

def test_arithmetic_SumExpression___init__():
    assert arithmetic_SumExpression.__init__(arithmetic_SumExpression(0, 0, arithmetic_SumExpression=arithmetic_DeclaredParameter(), arithmetic_SumExpression14=arithmetic_Expression()), 0, 0, arithmetic_SumExpression=arithmetic_DeclaredParameter(), arithmetic_SumExpression14=arithmetic_Expression()) == None

