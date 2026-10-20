from python_code import core_BinaryExpression
from python_code import core_Conditional
from python_code import core_IntegerExpression
from python_code import core_Rule
from python_code import core_UnaryExpression

def test_core_IntegerExpression___init__():
    assert core_IntegerExpression.__init__(core_IntegerExpression(core_IntegerExpression=core_Rule(), core_IntegerExpression4=core_UnaryExpression(), core_IntegerExpression6=core_Conditional(), core_IntegerExpression9=core_Conditional(), core_IntegerExpression14=core_BinaryExpression(), core_IntegerExpression17=core_BinaryExpression(), core_IntegerExpression12=core_Conditional()), core_IntegerExpression=core_Rule(), core_IntegerExpression4=core_UnaryExpression(), core_IntegerExpression6=core_Conditional(), core_IntegerExpression9=core_Conditional(), core_IntegerExpression14=core_BinaryExpression(), core_IntegerExpression17=core_BinaryExpression(), core_IntegerExpression12=core_Conditional()) == None

def test_core_IntegerExpression_isBoolean():
    assert core_IntegerExpression.isBoolean(core_IntegerExpression(core_IntegerExpression=core_Rule(), core_IntegerExpression4=core_UnaryExpression(), core_IntegerExpression6=core_Conditional(), core_IntegerExpression9=core_Conditional(), core_IntegerExpression14=core_BinaryExpression(), core_IntegerExpression17=core_BinaryExpression(), core_IntegerExpression12=core_Conditional())) == None


from python_code import core_IntegerLiteral

def test_core_IntegerLiteral___init__():
    assert core_IntegerLiteral.__init__(core_IntegerLiteral(0), 0) == None

