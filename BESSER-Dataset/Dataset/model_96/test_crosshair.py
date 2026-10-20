from python_code import Java5_ArrayType
from python_code import Java5_NamedElementRef

def test_Java5_ArrayType___init__():
    assert Java5_ArrayType.__init__(Java5_ArrayType(0, '\x00', Java5_ArrayType=Java5_NamedElementRef()), 0, '\x00', Java5_ArrayType=Java5_NamedElementRef()) == None


from python_code import Java5_Assignment
from python_code import Java5_Expression

def test_Java5_Assignment___init__():
    assert Java5_Assignment.__init__(Java5_Assignment('', Java5_Assignment=Java5_Expression(), Java5_Assignment49=Java5_Expression()), '', Java5_Assignment=Java5_Expression(), Java5_Assignment49=Java5_Expression()) == None


from python_code import Java5_BooleanLiteral

def test_Java5_BooleanLiteral___init__():
    assert Java5_BooleanLiteral.__init__(Java5_BooleanLiteral(True), False) == None


from python_code import Java5_CharacterLiteral

def test_Java5_CharacterLiteral___init__():
    assert Java5_CharacterLiteral.__init__(Java5_CharacterLiteral('', '\x00'), '\x00\x00', '') == None


from python_code import Java5_Expression
from python_code import Java5_InfixExpression

def test_Java5_InfixExpression___init__():
    assert Java5_InfixExpression.__init__(Java5_InfixExpression('', Java5_InfixExpression=Java5_Expression(), Java5_InfixExpression159=Java5_Expression(), Java5_InfixExpression162=set()), '', Java5_InfixExpression=Java5_Expression(), Java5_InfixExpression159=Java5_Expression(), Java5_InfixExpression162=set()) == None


from python_code import Java5_MethodRef
from python_code import Java5_MethodRefParameter
from python_code import Java5_NamedElementRef

def test_Java5_MethodRefParameter___init__():
    assert Java5_MethodRefParameter.__init__(Java5_MethodRefParameter('', '\x00', Java5_MethodRefParameter=Java5_MethodRef(), Java5_MethodRefParameter211=Java5_NamedElementRef()), '\x00\x00', '', Java5_MethodRefParameter=Java5_MethodRef(), Java5_MethodRefParameter211=Java5_NamedElementRef()) == None


from python_code import Java5_NamedElement
from python_code import Java5_NamedElementRef

def test_Java5_NamedElement___init__():
    assert Java5_NamedElement.__init__(Java5_NamedElement('', False, Java5_NamedElement=Java5_NamedElementRef()), '', False, Java5_NamedElement=Java5_NamedElementRef()) == None


from python_code import Java5_NumberLiteral

def test_Java5_NumberLiteral___init__():
    assert Java5_NumberLiteral.__init__(Java5_NumberLiteral(''), '') == None


from python_code import Java5_Expression
from python_code import Java5_PostfixExpression

def test_Java5_PostfixExpression___init__():
    assert Java5_PostfixExpression.__init__(Java5_PostfixExpression('', Java5_PostfixExpression=Java5_Expression()), '', Java5_PostfixExpression=Java5_Expression()) == None


from python_code import Java5_Expression
from python_code import Java5_PrefixExpression

def test_Java5_PrefixExpression___init__():
    assert Java5_PrefixExpression.__init__(Java5_PrefixExpression('', Java5_PrefixExpression=Java5_Expression()), '', Java5_PrefixExpression=Java5_Expression()) == None


from python_code import Java5_StringLiteral

def test_Java5_StringLiteral___init__():
    assert Java5_StringLiteral.__init__(Java5_StringLiteral('', '\x00'), '\x00\x00', '') == None


from python_code import Java5_Expression
from python_code import Java5_SwitchCase

def test_Java5_SwitchCase___init__():
    assert Java5_SwitchCase.__init__(Java5_SwitchCase(True, Java5_SwitchCase=Java5_Expression()), False, Java5_SwitchCase=Java5_Expression()) == None


from python_code import Java5_TagElement

def test_Java5_TagElement___init__():
    assert Java5_TagElement.__init__(Java5_TagElement('', Java5_TagElement=set()), '', Java5_TagElement=set()) == None


from python_code import Java5_TextElement

def test_Java5_TextElement___init__():
    assert Java5_TextElement.__init__(Java5_TextElement(''), '') == None


from python_code import Java5_Expression
from python_code import Java5_VariableDeclaration

def test_Java5_VariableDeclaration___init__():
    assert Java5_VariableDeclaration.__init__(Java5_VariableDeclaration(0, Java5_VariableDeclaration=Java5_Expression()), 0, Java5_VariableDeclaration=Java5_Expression()) == None


from python_code import Java5_NamedElementRef
from python_code import Java5_WildCardType

def test_Java5_WildCardType___init__():
    assert Java5_WildCardType.__init__(Java5_WildCardType('', Java5_WildCardType=Java5_NamedElementRef()), '', Java5_WildCardType=Java5_NamedElementRef()) == None

