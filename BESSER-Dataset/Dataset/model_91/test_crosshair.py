from python_code import javaMM_ArrayType
from python_code import javaMM_TypeAccess

def test_javaMM_ArrayType___init__():
    assert javaMM_ArrayType.__init__(javaMM_ArrayType(0, javaMM_ArrayType=javaMM_TypeAccess()), 0, javaMM_ArrayType=javaMM_TypeAccess()) == None


from python_code import javaMM_Assignment
from python_code import javaMM_Expression

def test_javaMM_Assignment___init__():
    assert javaMM_Assignment.__init__(javaMM_Assignment('', javaMM_Assignment=javaMM_Expression(), javaMM_Assignment83=javaMM_Expression()), '', javaMM_Assignment=javaMM_Expression(), javaMM_Assignment83=javaMM_Expression()) == None


from python_code import javaMM_BooleanLiteral

def test_javaMM_BooleanLiteral___init__():
    assert javaMM_BooleanLiteral.__init__(javaMM_BooleanLiteral(True), False) == None


from python_code import javaMM_CharacterLiteral

def test_javaMM_CharacterLiteral___init__():
    assert javaMM_CharacterLiteral.__init__(javaMM_CharacterLiteral(''), '') == None


from python_code import javaMM_ClassDeclaration
from python_code import javaMM_TypeAccess

def test_javaMM_ClassDeclaration___init__():
    assert javaMM_ClassDeclaration.__init__(javaMM_ClassDeclaration(javaMM_ClassDeclaration=javaMM_TypeAccess()), javaMM_ClassDeclaration=javaMM_TypeAccess()) == None

def test_javaMM_ClassDeclaration_getMethods():
    assert javaMM_ClassDeclaration.getMethods(javaMM_ClassDeclaration(javaMM_ClassDeclaration=javaMM_TypeAccess())) == None


from python_code import javaMM_Expression
from python_code import javaMM_InfixExpression

def test_javaMM_InfixExpression___init__():
    assert javaMM_InfixExpression.__init__(javaMM_InfixExpression('', javaMM_InfixExpression=javaMM_Expression(), javaMM_InfixExpression188=javaMM_Expression(), javaMM_InfixExpression191=set()), '', javaMM_InfixExpression=javaMM_Expression(), javaMM_InfixExpression188=javaMM_Expression(), javaMM_InfixExpression191=set()) == None

def test_javaMM_InfixExpression_operatorIsEquality():
    assert javaMM_InfixExpression.operatorIsEquality(javaMM_InfixExpression('', javaMM_InfixExpression=javaMM_Expression(), javaMM_InfixExpression188=javaMM_Expression(), javaMM_InfixExpression191=set())) == None


from python_code import javaMM_Manifest
from python_code import javaMM_ManifestEntry

def test_javaMM_ManifestEntry___init__():
    assert javaMM_ManifestEntry.__init__(javaMM_ManifestEntry('', javaMM_ManifestEntry=javaMM_Manifest(), javaMM_ManifestEntry211=set()), '', javaMM_ManifestEntry=javaMM_Manifest(), javaMM_ManifestEntry211=set()) == None


from python_code import javaMM_MethodRef
from python_code import javaMM_MethodRefParameter
from python_code import javaMM_TypeAccess

def test_javaMM_MethodRefParameter___init__():
    assert javaMM_MethodRefParameter.__init__(javaMM_MethodRefParameter('', False, javaMM_MethodRefParameter=javaMM_MethodRef(), javaMM_MethodRefParameter233=javaMM_TypeAccess()), '', False, javaMM_MethodRefParameter=javaMM_MethodRef(), javaMM_MethodRefParameter233=javaMM_TypeAccess()) == None

