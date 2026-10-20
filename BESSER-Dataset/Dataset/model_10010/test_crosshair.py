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


from python_code import javaMM_NumberLiteral

def test_javaMM_NumberLiteral___init__():
    assert javaMM_NumberLiteral.__init__(javaMM_NumberLiteral(''), '') == None


from python_code import javaMM_Expression
from python_code import javaMM_PostfixExpression

def test_javaMM_PostfixExpression___init__():
    assert javaMM_PostfixExpression.__init__(javaMM_PostfixExpression('', javaMM_PostfixExpression=javaMM_Expression()), '', javaMM_PostfixExpression=javaMM_Expression()) == None


from python_code import javaMM_Expression
from python_code import javaMM_PrefixExpression

def test_javaMM_PrefixExpression___init__():
    assert javaMM_PrefixExpression.__init__(javaMM_PrefixExpression('', javaMM_PrefixExpression=javaMM_Expression()), '', javaMM_PrefixExpression=javaMM_Expression()) == None


from python_code import javaMM_StringLiteral

def test_javaMM_StringLiteral___init__():
    assert javaMM_StringLiteral.__init__(javaMM_StringLiteral(''), '') == None


from python_code import javaMM_Expression
from python_code import javaMM_SwitchCase

def test_javaMM_SwitchCase___init__():
    assert javaMM_SwitchCase.__init__(javaMM_SwitchCase(True, javaMM_SwitchCase=javaMM_Expression()), False, javaMM_SwitchCase=javaMM_Expression()) == None


from python_code import javaMM_Javadoc
from python_code import javaMM_TagElement

def test_javaMM_TagElement___init__():
    assert javaMM_TagElement.__init__(javaMM_TagElement('', javaMM_TagElement=javaMM_Javadoc(), javaMM_TagElement321=set()), '', javaMM_TagElement=javaMM_Javadoc(), javaMM_TagElement321=set()) == None


from python_code import javaMM_TextElement

def test_javaMM_TextElement___init__():
    assert javaMM_TextElement.__init__(javaMM_TextElement(''), '') == None


from python_code import javaMM_Expression
from python_code import javaMM_SingleVariableAccess
from python_code import javaMM_VariableDeclaration

def test_javaMM_VariableDeclaration___init__():
    assert javaMM_VariableDeclaration.__init__(javaMM_VariableDeclaration(0, VariableDeclaration=javaMM_SingleVariableAccess(), javaMM_VariableDeclaration=javaMM_Expression(), variable=set()), 0, VariableDeclaration=javaMM_SingleVariableAccess(), javaMM_VariableDeclaration=javaMM_Expression(), variable=set()) == None


from python_code import javaMM_TypeAccess
from python_code import javaMM_WildCardType

def test_javaMM_WildCardType___init__():
    assert javaMM_WildCardType.__init__(javaMM_WildCardType(True, javaMM_WildCardType=javaMM_TypeAccess()), False, javaMM_WildCardType=javaMM_TypeAccess()) == None

