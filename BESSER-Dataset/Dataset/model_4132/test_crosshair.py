from python_code import cool_AssignmentExpression
from python_code import cool_Expression

def test_cool_AssignmentExpression___init__():
    assert cool_AssignmentExpression.__init__(cool_AssignmentExpression('', cool_AssignmentExpression=cool_Expression()), '', cool_AssignmentExpression=cool_Expression()) == None


from python_code import cool_BooleanLiteral

def test_cool_BooleanLiteral___init__():
    assert cool_BooleanLiteral.__init__(cool_BooleanLiteral(''), '') == None


from python_code import cool_CompareExpression
from python_code import cool_Expression

def test_cool_CompareExpression___init__():
    assert cool_CompareExpression.__init__(cool_CompareExpression('', cool_CompareExpression=cool_Expression(), cool_CompareExpression83=cool_Expression()), '', cool_CompareExpression=cool_Expression(), cool_CompareExpression83=cool_Expression()) == None


from python_code import cool_IdentifiableElement
from python_code import cool_IdentifierRefExpression

def test_cool_IdentifiableElement___init__():
    assert cool_IdentifiableElement.__init__(cool_IdentifiableElement('', cool_IdentifiableElement=cool_IdentifierRefExpression()), '', cool_IdentifiableElement=cool_IdentifierRefExpression()) == None


from python_code import cool_NumberLiteral

def test_cool_NumberLiteral___init__():
    assert cool_NumberLiteral.__init__(cool_NumberLiteral(0), 0) == None


from python_code import cool_StringLiteral

def test_cool_StringLiteral___init__():
    assert cool_StringLiteral.__init__(cool_StringLiteral(''), '') == None

