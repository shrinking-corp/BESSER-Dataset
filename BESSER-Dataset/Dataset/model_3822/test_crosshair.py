from python_code import expressions_AssignmentExpression
from python_code import expressions_Expression

def test_expressions_AssignmentExpression___init__():
    assert expressions_AssignmentExpression.__init__(expressions_AssignmentExpression('', expressions_AssignmentExpression=expressions_Expression(), expressions_AssignmentExpression11=expressions_Expression()), '', expressions_AssignmentExpression=expressions_Expression(), expressions_AssignmentExpression11=expressions_Expression()) == None


from python_code import expressions_BinaryExpression
from python_code import expressions_Expression

def test_expressions_BinaryExpression___init__():
    assert expressions_BinaryExpression.__init__(expressions_BinaryExpression(expressions_BinaryExpression=expressions_Expression(), expressions_BinaryExpression2=expressions_Expression()), expressions_BinaryExpression=expressions_Expression(), expressions_BinaryExpression2=expressions_Expression()) == None

def test_expressions_BinaryExpression_getOperator():
    assert expressions_BinaryExpression.getOperator(expressions_BinaryExpression(expressions_BinaryExpression=expressions_Expression(), expressions_BinaryExpression2=expressions_Expression())) == None


from python_code import expressions_BoolLiteral

def test_expressions_BoolLiteral___init__():
    assert expressions_BoolLiteral.__init__(expressions_BoolLiteral(True), False) == None


from python_code import expressions_DoubleLiteral

def test_expressions_DoubleLiteral___init__():
    assert expressions_DoubleLiteral.__init__(expressions_DoubleLiteral(0.0), 0.0) == None


from python_code import expressions_EObject
from python_code import expressions_ElementReferenceExpression

def test_expressions_ElementReferenceExpression___init__():
    assert expressions_ElementReferenceExpression.__init__(expressions_ElementReferenceExpression(False, False, expressions_ElementReferenceExpression=expressions_EObject(), expressions_ElementReferenceExpression32=set()), False, False, expressions_ElementReferenceExpression=expressions_EObject(), expressions_ElementReferenceExpression32=set()) == None


from python_code import expressions_EObject
from python_code import expressions_Expression
from python_code import expressions_FeatureCall

def test_expressions_FeatureCall___init__():
    assert expressions_FeatureCall.__init__(expressions_FeatureCall(False, False, expressions_FeatureCall=expressions_Expression(), expressions_FeatureCall25=expressions_EObject(), expressions_FeatureCall27=set()), False, False, expressions_FeatureCall=expressions_Expression(), expressions_FeatureCall25=expressions_EObject(), expressions_FeatureCall27=set()) == None


from python_code import expressions_FloatLiteral

def test_expressions_FloatLiteral___init__():
    assert expressions_FloatLiteral.__init__(expressions_FloatLiteral(0.0), 0.0) == None


from python_code import expressions_HexLiteral

def test_expressions_HexLiteral___init__():
    assert expressions_HexLiteral.__init__(expressions_HexLiteral(0), 0) == None


from python_code import expressions_IntLiteral

def test_expressions_IntLiteral___init__():
    assert expressions_IntLiteral.__init__(expressions_IntLiteral(0), 0) == None


from python_code import expressions_LogicalRelationExpression

def test_expressions_LogicalRelationExpression___init__():
    assert expressions_LogicalRelationExpression.__init__(expressions_LogicalRelationExpression(''), '') == None


from python_code import expressions_NumericalAddSubtractExpression

def test_expressions_NumericalAddSubtractExpression___init__():
    assert expressions_NumericalAddSubtractExpression.__init__(expressions_NumericalAddSubtractExpression(''), '') == None


from python_code import expressions_NumericalMultiplyDivideExpression

def test_expressions_NumericalMultiplyDivideExpression___init__():
    assert expressions_NumericalMultiplyDivideExpression.__init__(expressions_NumericalMultiplyDivideExpression(''), '') == None


from python_code import expressions_NumericalUnaryExpression

def test_expressions_NumericalUnaryExpression___init__():
    assert expressions_NumericalUnaryExpression.__init__(expressions_NumericalUnaryExpression(''), '') == None


from python_code import expressions_ShiftExpression

def test_expressions_ShiftExpression___init__():
    assert expressions_ShiftExpression.__init__(expressions_ShiftExpression(''), '') == None


from python_code import expressions_StringLiteral

def test_expressions_StringLiteral___init__():
    assert expressions_StringLiteral.__init__(expressions_StringLiteral(''), '') == None


from python_code import expressions_Expression
from python_code import expressions_UnaryExpression

def test_expressions_UnaryExpression___init__():
    assert expressions_UnaryExpression.__init__(expressions_UnaryExpression(expressions_UnaryExpression=expressions_Expression()), expressions_UnaryExpression=expressions_Expression()) == None

def test_expressions_UnaryExpression_getOperator():
    assert expressions_UnaryExpression.getOperator(expressions_UnaryExpression(expressions_UnaryExpression=expressions_Expression())) == None

