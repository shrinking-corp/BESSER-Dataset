from python_code import ast_Assignment
from python_code import ast_Expression

def test_ast_Assignment___init__():
    assert ast_Assignment.__init__(ast_Assignment('', ast_Assignment=ast_Expression(), ast_Assignment48=ast_Expression()), '', ast_Assignment=ast_Expression(), ast_Assignment48=ast_Expression()) == None


from python_code import ast_BooleanLiteral

def test_ast_BooleanLiteral___init__():
    assert ast_BooleanLiteral.__init__(ast_BooleanLiteral(True), False) == None


from python_code import ast_CharacterLiteral

def test_ast_CharacterLiteral___init__():
    assert ast_CharacterLiteral.__init__(ast_CharacterLiteral(''), '') == None


from python_code import ast_CompilationUnit
from python_code import ast_ImportDeclaration
from python_code import ast_Name

def test_ast_ImportDeclaration___init__():
    assert ast_ImportDeclaration.__init__(ast_ImportDeclaration(False, False, ast_ImportDeclaration=ast_CompilationUnit(), ast_ImportDeclaration136=ast_Name()), False, False, ast_ImportDeclaration=ast_CompilationUnit(), ast_ImportDeclaration136=ast_Name()) == None


from python_code import ast_Expression
from python_code import ast_InfixExpression

def test_ast_InfixExpression___init__():
    assert ast_InfixExpression.__init__(ast_InfixExpression('', ast_InfixExpression=ast_Expression(), ast_InfixExpression141=ast_Expression(), ast_InfixExpression144=set()), '', ast_InfixExpression=ast_Expression(), ast_InfixExpression141=ast_Expression(), ast_InfixExpression144=set()) == None


from python_code import ast_ASTNode
from python_code import ast_LambdaExpression

def test_ast_LambdaExpression___init__():
    assert ast_LambdaExpression.__init__(ast_LambdaExpression(False, ast_LambdaExpression=set(), ast_LambdaExpression470=ast_ASTNode()), False, ast_LambdaExpression=set(), ast_LambdaExpression470=ast_ASTNode()) == None


from python_code import ast_Modifier

def test_ast_Modifier___init__():
    assert ast_Modifier.__init__(ast_Modifier(''), '') == None


from python_code import ast_NumberLiteral

def test_ast_NumberLiteral___init__():
    assert ast_NumberLiteral.__init__(ast_NumberLiteral(''), '') == None


from python_code import ast_Expression
from python_code import ast_PostfixExpression

def test_ast_PostfixExpression___init__():
    assert ast_PostfixExpression.__init__(ast_PostfixExpression('', ast_PostfixExpression=ast_Expression()), '', ast_PostfixExpression=ast_Expression()) == None


from python_code import ast_Expression
from python_code import ast_PrefixExpression

def test_ast_PrefixExpression___init__():
    assert ast_PrefixExpression.__init__(ast_PrefixExpression('', ast_PrefixExpression=ast_Expression()), '', ast_PrefixExpression=ast_Expression()) == None


from python_code import ast_PrimitiveType

def test_ast_PrimitiveType___init__():
    assert ast_PrimitiveType.__init__(ast_PrimitiveType('', ast_PrimitiveType=set()), '', ast_PrimitiveType=set()) == None


from python_code import ast_StringLiteral

def test_ast_StringLiteral___init__():
    assert ast_StringLiteral.__init__(ast_StringLiteral(''), '') == None


from python_code import ast_Javadoc
from python_code import ast_TagElement

def test_ast_TagElement___init__():
    assert ast_TagElement.__init__(ast_TagElement('', ast_TagElement=set(), ast_TagElement156=ast_Javadoc()), '', ast_TagElement=set(), ast_TagElement156=ast_Javadoc()) == None


from python_code import ast_TextElement

def test_ast_TextElement___init__():
    assert ast_TextElement.__init__(ast_TextElement(''), '') == None


from python_code import ast_Type
from python_code import ast_WildcardType

def test_ast_WildcardType___init__():
    assert ast_WildcardType.__init__(ast_WildcardType(False, ast_WildcardType=set(), ast_WildcardType430=ast_Type()), False, ast_WildcardType=set(), ast_WildcardType430=ast_Type()) == None

