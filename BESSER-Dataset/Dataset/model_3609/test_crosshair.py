from python_code import pp2_AttributeOperation
from python_code import pp2_AttributeOperations
from python_code import pp2_Expression

def test_pp2_AttributeOperation___init__():
    assert pp2_AttributeOperation.__init__(pp2_AttributeOperation('', '\x00', pp2_AttributeOperation=pp2_Expression(), pp2_AttributeOperation7=pp2_AttributeOperations()), '\x00\x00', '', pp2_AttributeOperation=pp2_Expression(), pp2_AttributeOperation7=pp2_AttributeOperations()) == None


from python_code import pp2_BinaryOpExpression

def test_pp2_BinaryOpExpression___init__():
    assert pp2_BinaryOpExpression.__init__(pp2_BinaryOpExpression(''), '') == None


from python_code import pp2_Definition
from python_code import pp2_DefinitionArgumentList

def test_pp2_Definition___init__():
    assert pp2_Definition.__init__(pp2_Definition('', pp2_Definition=pp2_DefinitionArgumentList()), '', pp2_Definition=pp2_DefinitionArgumentList()) == None


from python_code import pp2_DefinitionArgument
from python_code import pp2_DefinitionArgumentList
from python_code import pp2_Expression

def test_pp2_DefinitionArgument___init__():
    assert pp2_DefinitionArgument.__init__(pp2_DefinitionArgument('', '\x00', pp2_DefinitionArgument=pp2_DefinitionArgumentList(), pp2_DefinitionArgument13=pp2_Expression(), pp2_DefinitionArgument16=pp2_Expression()), '\x00\x00', '', pp2_DefinitionArgument=pp2_DefinitionArgumentList(), pp2_DefinitionArgument13=pp2_Expression(), pp2_DefinitionArgument16=pp2_Expression()) == None


from python_code import pp2_InterpolatedVariable

def test_pp2_InterpolatedVariable___init__():
    assert pp2_InterpolatedVariable.__init__(pp2_InterpolatedVariable(''), '') == None


from python_code import pp2_JavaLambda

def test_pp2_JavaLambda___init__():
    assert pp2_JavaLambda.__init__(pp2_JavaLambda(True), False) == None


from python_code import pp2_LiteralBoolean

def test_pp2_LiteralBoolean___init__():
    assert pp2_LiteralBoolean.__init__(pp2_LiteralBoolean(True), False) == None


from python_code import pp2_LiteralName

def test_pp2_LiteralName___init__():
    assert pp2_LiteralName.__init__(pp2_LiteralName(''), '') == None


from python_code import pp2_LiteralNameOrReference

def test_pp2_LiteralNameOrReference___init__():
    assert pp2_LiteralNameOrReference.__init__(pp2_LiteralNameOrReference(''), '') == None


from python_code import pp2_LiteralRegex

def test_pp2_LiteralRegex___init__():
    assert pp2_LiteralRegex.__init__(pp2_LiteralRegex(''), '') == None


from python_code import pp2_Expression
from python_code import pp2_MethodCall

def test_pp2_MethodCall___init__():
    assert pp2_MethodCall.__init__(pp2_MethodCall(True, pp2_MethodCall=pp2_Expression()), False, pp2_MethodCall=pp2_Expression()) == None


from python_code import pp2_SingleQuotedString

def test_pp2_SingleQuotedString___init__():
    assert pp2_SingleQuotedString.__init__(pp2_SingleQuotedString(''), '') == None


from python_code import pp2_VariableExpression

def test_pp2_VariableExpression___init__():
    assert pp2_VariableExpression.__init__(pp2_VariableExpression(''), '') == None


from python_code import pp2_VariableTE

def test_pp2_VariableTE___init__():
    assert pp2_VariableTE.__init__(pp2_VariableTE(''), '') == None


from python_code import pp2_VerbatimTE

def test_pp2_VerbatimTE___init__():
    assert pp2_VerbatimTE.__init__(pp2_VerbatimTE(''), '') == None


from python_code import pp2_VirtualNameOrReference

def test_pp2_VirtualNameOrReference___init__():
    assert pp2_VirtualNameOrReference.__init__(pp2_VirtualNameOrReference('', False), '', False) == None

