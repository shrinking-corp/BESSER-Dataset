from python_code import expression_BinaryExpression
from python_code import expression_Expression
from python_code import expression_ExpressionStatement
from python_code import expression_UnaryExpression

def test_expression_Expression___init__():
    assert expression_Expression.__init__(expression_Expression(0.0, expression_Expression=expression_BinaryExpression(), expression_Expression3=expression_BinaryExpression(), expression_Expression5=expression_UnaryExpression(), expression_Expression7=expression_ExpressionStatement()), 0.0, expression_Expression=expression_BinaryExpression(), expression_Expression3=expression_BinaryExpression(), expression_Expression5=expression_UnaryExpression(), expression_Expression7=expression_ExpressionStatement()) == None


from python_code import expression_IntegerExpression

def test_expression_IntegerExpression___init__():
    assert expression_IntegerExpression.__init__(expression_IntegerExpression(0.0), 0.0) == None

