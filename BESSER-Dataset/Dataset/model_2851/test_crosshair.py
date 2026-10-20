from python_code import mitra_Assignment
from python_code import mitra_Expression

def test_mitra_Assignment___init__():
    assert mitra_Assignment.__init__(mitra_Assignment('', mitra_Assignment=set(), mitra_Assignment200=mitra_Expression()), '', mitra_Assignment=set(), mitra_Assignment200=mitra_Expression()) == None


from python_code import mitra_BooleanExpression
from python_code import mitra_Expression

def test_mitra_BooleanExpression___init__():
    assert mitra_BooleanExpression.__init__(mitra_BooleanExpression('', mitra_BooleanExpression=mitra_Expression(), mitra_BooleanExpression210=mitra_Expression()), '', mitra_BooleanExpression=mitra_Expression(), mitra_BooleanExpression210=mitra_Expression()) == None


from python_code import mitra_BooleanLiteral

def test_mitra_BooleanLiteral___init__():
    assert mitra_BooleanLiteral.__init__(mitra_BooleanLiteral(True), False) == None

def test_mitra_BooleanLiteral_toString():
    assert mitra_BooleanLiteral.toString(mitra_BooleanLiteral(False)) == None


from python_code import mitra_CollectionType
from python_code import mitra_Type

def test_mitra_CollectionType___init__():
    assert mitra_CollectionType.__init__(mitra_CollectionType('', mitra_CollectionType=mitra_Type()), '', mitra_CollectionType=mitra_Type()) == None

def test_mitra_CollectionType_toString():
    assert mitra_CollectionType.toString(mitra_CollectionType('', mitra_CollectionType=mitra_Type())) == None


from python_code import mitra_EqualityExpression
from python_code import mitra_Expression

def test_mitra_EqualityExpression___init__():
    assert mitra_EqualityExpression.__init__(mitra_EqualityExpression('', mitra_EqualityExpression=mitra_Expression(), mitra_EqualityExpression215=mitra_Expression()), '', mitra_EqualityExpression=mitra_Expression(), mitra_EqualityExpression215=mitra_Expression()) == None


from python_code import mitra_IntLiteral

def test_mitra_IntLiteral___init__():
    assert mitra_IntLiteral.__init__(mitra_IntLiteral(0), 0) == None

def test_mitra_IntLiteral_toString():
    assert mitra_IntLiteral.toString(mitra_IntLiteral(0)) == None


from python_code import mitra_Expression
from python_code import mitra_MathExpression

def test_mitra_MathExpression___init__():
    assert mitra_MathExpression.__init__(mitra_MathExpression('', mitra_MathExpression225=mitra_Expression(), mitra_MathExpression=mitra_Expression()), '', mitra_MathExpression225=mitra_Expression(), mitra_MathExpression=mitra_Expression()) == None


from python_code import mitra_Parameter
from python_code import mitra_TypedVarDeclaration

def test_mitra_Parameter___init__():
    assert mitra_Parameter.__init__(mitra_Parameter('', mitra_Parameter=set(), mitra_Parameter61=mitra_TypedVarDeclaration()), '', mitra_Parameter=set(), mitra_Parameter61=mitra_TypedVarDeclaration()) == None

