from python_code import java_ArrayType
from python_code import java_TypeAccess

def test_java_ArrayType___init__():
    assert java_ArrayType.__init__(java_ArrayType(0, java_ArrayType=java_TypeAccess()), 0, java_ArrayType=java_TypeAccess()) == None


from python_code import java_Assignment
from python_code import java_Expression

def test_java_Assignment___init__():
    assert java_Assignment.__init__(java_Assignment('', java_Assignment=java_Expression(), java_Assignment83=java_Expression()), '', java_Assignment=java_Expression(), java_Assignment83=java_Expression()) == None


from python_code import java_BooleanLiteral

def test_java_BooleanLiteral___init__():
    assert java_BooleanLiteral.__init__(java_BooleanLiteral(True), False) == None


from python_code import java_CharacterLiteral

def test_java_CharacterLiteral___init__():
    assert java_CharacterLiteral.__init__(java_CharacterLiteral(''), '') == None


from python_code import java_Expression
from python_code import java_InfixExpression

def test_java_InfixExpression___init__():
    assert java_InfixExpression.__init__(java_InfixExpression('', java_InfixExpression=java_Expression(), java_InfixExpression188=java_Expression(), java_InfixExpression191=set()), '', java_InfixExpression=java_Expression(), java_InfixExpression188=java_Expression(), java_InfixExpression191=set()) == None


from python_code import java_Manifest
from python_code import java_ManifestEntry

def test_java_ManifestEntry___init__():
    assert java_ManifestEntry.__init__(java_ManifestEntry('', java_ManifestEntry=java_Manifest(), java_ManifestEntry211=set()), '', java_ManifestEntry=java_Manifest(), java_ManifestEntry211=set()) == None


from python_code import java_MethodRef
from python_code import java_MethodRefParameter
from python_code import java_TypeAccess

def test_java_MethodRefParameter___init__():
    assert java_MethodRefParameter.__init__(java_MethodRefParameter('', False, java_MethodRefParameter=java_MethodRef(), java_MethodRefParameter233=java_TypeAccess()), '', False, java_MethodRefParameter=java_MethodRef(), java_MethodRefParameter233=java_TypeAccess()) == None

