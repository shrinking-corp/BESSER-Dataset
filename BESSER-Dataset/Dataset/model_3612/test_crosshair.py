from python_code import pp1_AttributeOperation
from python_code import pp1_AttributeOperations
from python_code import pp1_Expression

def test_pp1_AttributeOperation___init__():
    assert pp1_AttributeOperation.__init__(pp1_AttributeOperation('', '\x00', pp1_AttributeOperation=pp1_Expression(), pp1_AttributeOperation7=pp1_AttributeOperations()), '\x00\x00', '', pp1_AttributeOperation=pp1_Expression(), pp1_AttributeOperation7=pp1_AttributeOperations()) == None


from python_code import pp1_BinaryOpExpression

def test_pp1_BinaryOpExpression___init__():
    assert pp1_BinaryOpExpression.__init__(pp1_BinaryOpExpression(''), '') == None


from python_code import pp1_Definition
from python_code import pp1_DefinitionArgumentList

def test_pp1_Definition___init__():
    assert pp1_Definition.__init__(pp1_Definition('', pp1_Definition=pp1_DefinitionArgumentList(), pp1_Definition11=set()), '', pp1_Definition=pp1_DefinitionArgumentList(), pp1_Definition11=set()) == None


from python_code import pp1_DefinitionArgument
from python_code import pp1_DefinitionArgumentList
from python_code import pp1_Expression

def test_pp1_DefinitionArgument___init__():
    assert pp1_DefinitionArgument.__init__(pp1_DefinitionArgument('', '\x00', pp1_DefinitionArgument=pp1_DefinitionArgumentList(), pp1_DefinitionArgument16=pp1_Expression()), '\x00\x00', '', pp1_DefinitionArgument=pp1_DefinitionArgumentList(), pp1_DefinitionArgument16=pp1_Expression()) == None


from python_code import pp1_InterpolatedVariable

def test_pp1_InterpolatedVariable___init__():
    assert pp1_InterpolatedVariable.__init__(pp1_InterpolatedVariable(''), '') == None


from python_code import pp1_JavaLambda

def test_pp1_JavaLambda___init__():
    assert pp1_JavaLambda.__init__(pp1_JavaLambda(True), False) == None


from python_code import pp1_LiteralBoolean

def test_pp1_LiteralBoolean___init__():
    assert pp1_LiteralBoolean.__init__(pp1_LiteralBoolean(True), False) == None


from python_code import pp1_LiteralName

def test_pp1_LiteralName___init__():
    assert pp1_LiteralName.__init__(pp1_LiteralName(''), '') == None


from python_code import pp1_LiteralNameOrReference

def test_pp1_LiteralNameOrReference___init__():
    assert pp1_LiteralNameOrReference.__init__(pp1_LiteralNameOrReference(''), '') == None


from python_code import pp1_LiteralRegex

def test_pp1_LiteralRegex___init__():
    assert pp1_LiteralRegex.__init__(pp1_LiteralRegex(''), '') == None


from python_code import pp1_Expression
from python_code import pp1_MethodCall

def test_pp1_MethodCall___init__():
    assert pp1_MethodCall.__init__(pp1_MethodCall(True, pp1_MethodCall=pp1_Expression()), False, pp1_MethodCall=pp1_Expression()) == None


from python_code import pp1_SingleQuotedString

def test_pp1_SingleQuotedString___init__():
    assert pp1_SingleQuotedString.__init__(pp1_SingleQuotedString(''), '') == None


from python_code import pp1_VariableExpression

def test_pp1_VariableExpression___init__():
    assert pp1_VariableExpression.__init__(pp1_VariableExpression(''), '') == None


from python_code import pp1_VariableTE

def test_pp1_VariableTE___init__():
    assert pp1_VariableTE.__init__(pp1_VariableTE(''), '') == None


from python_code import pp1_VerbatimTE

def test_pp1_VerbatimTE___init__():
    assert pp1_VerbatimTE.__init__(pp1_VerbatimTE(''), '') == None


from python_code import pp1_VirtualNameOrReference

def test_pp1_VirtualNameOrReference___init__():
    assert pp1_VirtualNameOrReference.__init__(pp1_VirtualNameOrReference('', False), '', False) == None

