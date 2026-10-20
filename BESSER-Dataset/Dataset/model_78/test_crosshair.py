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
    assert java_MethodRefParameter.__init__(java_MethodRefParameter('', False, java_MethodRefParameter233=java_TypeAccess(), java_MethodRefParameter=java_MethodRef()), '', False, java_MethodRefParameter233=java_TypeAccess(), java_MethodRefParameter=java_MethodRef()) == None


from python_code import java_NumberLiteral

def test_java_NumberLiteral___init__():
    assert java_NumberLiteral.__init__(java_NumberLiteral(''), '') == None


from python_code import java_Expression
from python_code import java_PostfixExpression

def test_java_PostfixExpression___init__():
    assert java_PostfixExpression.__init__(java_PostfixExpression('', java_PostfixExpression=java_Expression()), '', java_PostfixExpression=java_Expression()) == None


from python_code import java_Expression
from python_code import java_PrefixExpression

def test_java_PrefixExpression___init__():
    assert java_PrefixExpression.__init__(java_PrefixExpression('', java_PrefixExpression=java_Expression()), '', java_PrefixExpression=java_Expression()) == None


from python_code import java_StringLiteral

def test_java_StringLiteral___init__():
    assert java_StringLiteral.__init__(java_StringLiteral(''), '') == None


from python_code import java_Expression
from python_code import java_SwitchCase

def test_java_SwitchCase___init__():
    assert java_SwitchCase.__init__(java_SwitchCase(True, java_SwitchCase=java_Expression()), False, java_SwitchCase=java_Expression()) == None


from python_code import java_Javadoc
from python_code import java_TagElement

def test_java_TagElement___init__():
    assert java_TagElement.__init__(java_TagElement('', java_TagElement=java_Javadoc(), java_TagElement321=set()), '', java_TagElement=java_Javadoc(), java_TagElement321=set()) == None


from python_code import java_TextElement

def test_java_TextElement___init__():
    assert java_TextElement.__init__(java_TextElement(''), '') == None

