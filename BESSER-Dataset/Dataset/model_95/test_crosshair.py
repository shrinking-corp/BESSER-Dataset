from python_code import java_ArrayType
from python_code import java_TypeAccess

def test_java_ArrayType___init__():
    assert java_ArrayType.__init__(java_ArrayType(0, java_ArrayType=java_TypeAccess()), 0, java_ArrayType=java_TypeAccess()) == None


from python_code import java_Assignment
from python_code import java_Expression

def test_java_Assignment___init__():
    assert java_Assignment.__init__(java_Assignment('', java_Assignment=java_Expression(), java_Assignment46=java_Expression()), '', java_Assignment=java_Expression(), java_Assignment46=java_Expression()) == None


from python_code import java_BooleanLiteral

def test_java_BooleanLiteral___init__():
    assert java_BooleanLiteral.__init__(java_BooleanLiteral(True), False) == None


from python_code import java_CharacterLiteral

def test_java_CharacterLiteral___init__():
    assert java_CharacterLiteral.__init__(java_CharacterLiteral(''), '') == None


from python_code import java_ASTNode
from python_code import java_AbstractTypeDeclaration
from python_code import java_Comment

def test_java_Comment___init__():
    assert java_Comment.__init__(java_Comment('', java_Comment=java_AbstractTypeDeclaration(), java_Comment31=java_AbstractTypeDeclaration(), java_Comment67=java_ASTNode()), '', java_Comment=java_AbstractTypeDeclaration(), java_Comment31=java_AbstractTypeDeclaration(), java_Comment67=java_ASTNode()) == None


from python_code import java_Expression
from python_code import java_InfixExpression

def test_java_InfixExpression___init__():
    assert java_InfixExpression.__init__(java_InfixExpression('', java_InfixExpression=java_Expression(), java_InfixExpression114=java_Expression(), java_InfixExpression117=set()), '', java_InfixExpression=java_Expression(), java_InfixExpression114=java_Expression(), java_InfixExpression117=set()) == None


from python_code import java_Model

def test_java_Model___init__():
    assert java_Model.__init__(java_Model('', java_Model=set(), java_Model254=set(), java_Model257=set(), java_Model259=set()), '', java_Model=set(), java_Model254=set(), java_Model257=set(), java_Model259=set()) == None


from python_code import java_BodyDeclaration
from python_code import java_Modifier
from python_code import java_SingleVariableDeclaration

def test_java_Modifier___init__():
    assert java_Modifier.__init__(java_Modifier(False, '', '\x00\x00', java_Modifier=java_SingleVariableDeclaration(), java_Modifier156=java_BodyDeclaration()), False, '', '', java_Modifier=java_SingleVariableDeclaration(), java_Modifier156=java_BodyDeclaration()) == None


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

