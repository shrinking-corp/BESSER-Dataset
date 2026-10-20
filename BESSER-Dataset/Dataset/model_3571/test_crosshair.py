from python_code import expression_BooleanLiteral

def test_expression_BooleanLiteral___init__():
    assert expression_BooleanLiteral.__init__(expression_BooleanLiteral(''), '') == None


from python_code import expression_BooleanOperation
from python_code import expression_Expression

def test_expression_BooleanOperation___init__():
    assert expression_BooleanOperation.__init__(expression_BooleanOperation('', expression_BooleanOperation=expression_Expression(), expression_BooleanOperation53=expression_Expression()), '', expression_BooleanOperation=expression_Expression(), expression_BooleanOperation53=expression_Expression()) == None


from python_code import expression_CollectionExpression
from python_code import expression_Expression

def test_expression_CollectionExpression___init__():
    assert expression_CollectionExpression.__init__(expression_CollectionExpression('', expression_CollectionExpression=expression_Expression()), '', expression_CollectionExpression=expression_Expression()) == None


from python_code import expression_GlobalVarExpression

def test_expression_GlobalVarExpression___init__():
    assert expression_GlobalVarExpression.__init__(expression_GlobalVarExpression(''), '') == None


from python_code import expression_IntegerLiteral

def test_expression_IntegerLiteral___init__():
    assert expression_IntegerLiteral.__init__(expression_IntegerLiteral(0), 0) == None


from python_code import expression_Expression
from python_code import expression_LetExpression

def test_expression_LetExpression___init__():
    assert expression_LetExpression.__init__(expression_LetExpression('', expression_LetExpression=expression_Expression(), expression_LetExpression2=expression_Expression()), '', expression_LetExpression=expression_Expression(), expression_LetExpression2=expression_Expression()) == None


from python_code import expression_NullLiteral

def test_expression_NullLiteral___init__():
    assert expression_NullLiteral.__init__(expression_NullLiteral(''), '') == None


from python_code import expression_RealLiteral

def test_expression_RealLiteral___init__():
    assert expression_RealLiteral.__init__(expression_RealLiteral(''), '') == None


from python_code import expression_StringLiteral

def test_expression_StringLiteral___init__():
    assert expression_StringLiteral.__init__(expression_StringLiteral(''), '') == None

