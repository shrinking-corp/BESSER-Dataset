from python_code import simpleExpressions_BooleanLiteral

def test_simpleExpressions_BooleanLiteral___init__():
    assert simpleExpressions_BooleanLiteral.__init__(simpleExpressions_BooleanLiteral(True), False) == None


from python_code import simpleExpressions_Comparison
from python_code import simpleExpressions_Expression

def test_simpleExpressions_Comparison___init__():
    assert simpleExpressions_Comparison.__init__(simpleExpressions_Comparison('', simpleExpressions_Comparison=simpleExpressions_Expression(), simpleExpressions_Comparison14=simpleExpressions_Expression()), '', simpleExpressions_Comparison=simpleExpressions_Expression(), simpleExpressions_Comparison14=simpleExpressions_Expression()) == None


from python_code import simpleExpressions_Expression
from python_code import simpleExpressions_IfCondition

def test_simpleExpressions_IfCondition___init__():
    assert simpleExpressions_IfCondition.__init__(simpleExpressions_IfCondition(True, simpleExpressions_IfCondition=simpleExpressions_Expression()), False, simpleExpressions_IfCondition=simpleExpressions_Expression()) == None


from python_code import simpleExpressions_MethodCall

def test_simpleExpressions_MethodCall___init__():
    assert simpleExpressions_MethodCall.__init__(simpleExpressions_MethodCall(''), '') == None


from python_code import simpleExpressions_NumberLiteral

def test_simpleExpressions_NumberLiteral___init__():
    assert simpleExpressions_NumberLiteral.__init__(simpleExpressions_NumberLiteral(0), 0) == None

