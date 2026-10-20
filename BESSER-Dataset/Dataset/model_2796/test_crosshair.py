from python_code import Metamodelo_Cpp_CppAssignamentStatement

def test_Metamodelo_Cpp_CppAssignamentStatement___init__():
    assert Metamodelo_Cpp_CppAssignamentStatement.__init__(Metamodelo_Cpp_CppAssignamentStatement(''), '') == None


from python_code import Metamodelo_Cpp_CppBooleanLiteral

def test_Metamodelo_Cpp_CppBooleanLiteral___init__():
    assert Metamodelo_Cpp_CppBooleanLiteral.__init__(Metamodelo_Cpp_CppBooleanLiteral(True), False) == None


from python_code import Metamodelo_Cpp_CppCharacterLiteral

def test_Metamodelo_Cpp_CppCharacterLiteral___init__():
    assert Metamodelo_Cpp_CppCharacterLiteral.__init__(Metamodelo_Cpp_CppCharacterLiteral(''), '') == None


from python_code import Metamodelo_Cpp_CppComment

def test_Metamodelo_Cpp_CppComment___init__():
    assert Metamodelo_Cpp_CppComment.__init__(Metamodelo_Cpp_CppComment(False, False, '\x00\x00'), False, False, '') == None


from python_code import Metamodelo_Cpp_CppDestructor

def test_Metamodelo_Cpp_CppDestructor___init__():
    assert Metamodelo_Cpp_CppDestructor.__init__(Metamodelo_Cpp_CppDestructor(True), False) == None


from python_code import Metamodelo_Cpp_CppField
from python_code import Metamodelo_Cpp_CppFieldContainer

def test_Metamodelo_Cpp_CppField___init__():
    assert Metamodelo_Cpp_CppField.__init__(Metamodelo_Cpp_CppField('', CppField=Metamodelo_Cpp_CppFieldContainer(), cppFields=Metamodelo_Cpp_CppFieldContainer()), '', CppField=Metamodelo_Cpp_CppFieldContainer(), cppFields=Metamodelo_Cpp_CppFieldContainer()) == None


from python_code import Metamodelo_Cpp_CppBlock
from python_code import Metamodelo_Cpp_CppFunction

def test_Metamodelo_Cpp_CppFunction___init__():
    assert Metamodelo_Cpp_CppFunction.__init__(Metamodelo_Cpp_CppFunction(False, '', False, Metamodelo_Cpp_CppFunction=set(), Metamodelo_Cpp_CppFunction51=Metamodelo_Cpp_CppBlock()), False, '', True, Metamodelo_Cpp_CppFunction=set(), Metamodelo_Cpp_CppFunction51=Metamodelo_Cpp_CppBlock()) == None


from python_code import Metamodelo_Cpp_CppExpression
from python_code import Metamodelo_Cpp_CppIfElseStatement

def test_Metamodelo_Cpp_CppIfElseStatement___init__():
    assert Metamodelo_Cpp_CppIfElseStatement.__init__(Metamodelo_Cpp_CppIfElseStatement(True, Metamodelo_Cpp_CppIfElseStatement=Metamodelo_Cpp_CppExpression()), False, Metamodelo_Cpp_CppIfElseStatement=Metamodelo_Cpp_CppExpression()) == None


from python_code import Metamodelo_Cpp_CppInfixExpression

def test_Metamodelo_Cpp_CppInfixExpression___init__():
    assert Metamodelo_Cpp_CppInfixExpression.__init__(Metamodelo_Cpp_CppInfixExpression(''), '') == None


from python_code import Metamodelo_Cpp_CppMethod

def test_Metamodelo_Cpp_CppMethod___init__():
    assert Metamodelo_Cpp_CppMethod.__init__(Metamodelo_Cpp_CppMethod(False, False, False, False), False, False, False, True) == None


from python_code import Metamodelo_Cpp_CppNamedElement

def test_Metamodelo_Cpp_CppNamedElement___init__():
    assert Metamodelo_Cpp_CppNamedElement.__init__(Metamodelo_Cpp_CppNamedElement(''), '') == None


from python_code import Metamodelo_Cpp_CppNumberLiteral

def test_Metamodelo_Cpp_CppNumberLiteral___init__():
    assert Metamodelo_Cpp_CppNumberLiteral.__init__(Metamodelo_Cpp_CppNumberLiteral(''), '') == None


from python_code import Metamodelo_Cpp_CppPostfixExpression

def test_Metamodelo_Cpp_CppPostfixExpression___init__():
    assert Metamodelo_Cpp_CppPostfixExpression.__init__(Metamodelo_Cpp_CppPostfixExpression(''), '') == None


from python_code import Metamodelo_Cpp_CppPrefixExpression

def test_Metamodelo_Cpp_CppPrefixExpression___init__():
    assert Metamodelo_Cpp_CppPrefixExpression.__init__(Metamodelo_Cpp_CppPrefixExpression(''), '') == None


from python_code import Metamodelo_Cpp_CppRegexLiteral

def test_Metamodelo_Cpp_CppRegexLiteral___init__():
    assert Metamodelo_Cpp_CppRegexLiteral.__init__(Metamodelo_Cpp_CppRegexLiteral('', '\x00'), '\x00\x00', '') == None


from python_code import Metamodelo_Cpp_CppStringLiteral

def test_Metamodelo_Cpp_CppStringLiteral___init__():
    assert Metamodelo_Cpp_CppStringLiteral.__init__(Metamodelo_Cpp_CppStringLiteral(''), '') == None


from python_code import Metamodelo_Cpp_CppClassifier
from python_code import Metamodelo_Cpp_CppVariable

def test_Metamodelo_Cpp_CppVariable___init__():
    assert Metamodelo_Cpp_CppVariable.__init__(Metamodelo_Cpp_CppVariable(False, '\x00', Metamodelo_Cpp_CppVariable=Metamodelo_Cpp_CppClassifier()), False, '\x00', Metamodelo_Cpp_CppVariable=Metamodelo_Cpp_CppClassifier()) == None


from python_code import Metamodelo_Cpp_CppExpression
from python_code import Metamodelo_Cpp_CppVariableAccess
from python_code import Metamodelo_Cpp_CppVariableDeclaration

def test_Metamodelo_Cpp_CppVariableDeclaration___init__():
    assert Metamodelo_Cpp_CppVariableDeclaration.__init__(Metamodelo_Cpp_CppVariableDeclaration('', False, Metamodelo_Cpp_CppVariableDeclaration140=set(), CppVariableDeclaration=Metamodelo_Cpp_CppVariableAccess(), variable=set(), Metamodelo_Cpp_CppVariableDeclaration=Metamodelo_Cpp_CppExpression()), '', True, Metamodelo_Cpp_CppVariableDeclaration140=set(), CppVariableDeclaration=Metamodelo_Cpp_CppVariableAccess(), variable=set(), Metamodelo_Cpp_CppVariableDeclaration=Metamodelo_Cpp_CppExpression()) == None

