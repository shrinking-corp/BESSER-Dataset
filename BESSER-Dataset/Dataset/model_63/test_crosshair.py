from python_code import Java_ArrayType
from python_code import Java_TypeAccess

def test_Java_ArrayType___init__():
    assert Java_ArrayType.__init__(Java_ArrayType(0, Java_ArrayType=Java_TypeAccess()), 0, Java_ArrayType=Java_TypeAccess()) == None


from python_code import Java_Assignment
from python_code import Java_Expression

def test_Java_Assignment___init__():
    assert Java_Assignment.__init__(Java_Assignment('', Java_Assignment=Java_Expression(), Java_Assignment83=Java_Expression()), '', Java_Assignment=Java_Expression(), Java_Assignment83=Java_Expression()) == None


from python_code import Java_BooleanLiteral

def test_Java_BooleanLiteral___init__():
    assert Java_BooleanLiteral.__init__(Java_BooleanLiteral(True), False) == None


from python_code import Java_CharacterLiteral

def test_Java_CharacterLiteral___init__():
    assert Java_CharacterLiteral.__init__(Java_CharacterLiteral(''), '') == None


from python_code import Java_Expression
from python_code import Java_InfixExpression

def test_Java_InfixExpression___init__():
    assert Java_InfixExpression.__init__(Java_InfixExpression('', Java_InfixExpression=Java_Expression(), Java_InfixExpression188=Java_Expression(), Java_InfixExpression191=set()), '', Java_InfixExpression=Java_Expression(), Java_InfixExpression188=Java_Expression(), Java_InfixExpression191=set()) == None


from python_code import Java_Manifest
from python_code import Java_ManifestEntry

def test_Java_ManifestEntry___init__():
    assert Java_ManifestEntry.__init__(Java_ManifestEntry('', Java_ManifestEntry=Java_Manifest(), Java_ManifestEntry211=set()), '', Java_ManifestEntry=Java_Manifest(), Java_ManifestEntry211=set()) == None


from python_code import Java_MethodRef
from python_code import Java_MethodRefParameter
from python_code import Java_TypeAccess

def test_Java_MethodRefParameter___init__():
    assert Java_MethodRefParameter.__init__(Java_MethodRefParameter('', False, Java_MethodRefParameter=Java_MethodRef(), Java_MethodRefParameter233=Java_TypeAccess()), '', False, Java_MethodRefParameter=Java_MethodRef(), Java_MethodRefParameter233=Java_TypeAccess()) == None


from python_code import Java_NumberLiteral

def test_Java_NumberLiteral___init__():
    assert Java_NumberLiteral.__init__(Java_NumberLiteral(''), '') == None


from python_code import Java_Expression
from python_code import Java_PostfixExpression

def test_Java_PostfixExpression___init__():
    assert Java_PostfixExpression.__init__(Java_PostfixExpression('', Java_PostfixExpression=Java_Expression()), '', Java_PostfixExpression=Java_Expression()) == None


from python_code import Java_Expression
from python_code import Java_PrefixExpression

def test_Java_PrefixExpression___init__():
    assert Java_PrefixExpression.__init__(Java_PrefixExpression('', Java_PrefixExpression=Java_Expression()), '', Java_PrefixExpression=Java_Expression()) == None

