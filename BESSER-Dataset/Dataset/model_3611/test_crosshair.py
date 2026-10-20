from python_code import pp_AttributeOperation
from python_code import pp_AttributeOperations
from python_code import pp_Expression

def test_pp_AttributeOperation___init__():
    assert pp_AttributeOperation.__init__(pp_AttributeOperation('', '\x00', pp_AttributeOperation=pp_Expression(), pp_AttributeOperation7=pp_AttributeOperations()), '\x00\x00', '', pp_AttributeOperation=pp_Expression(), pp_AttributeOperation7=pp_AttributeOperations()) == None


from python_code import pp_BinaryOpExpression

def test_pp_BinaryOpExpression___init__():
    assert pp_BinaryOpExpression.__init__(pp_BinaryOpExpression(''), '') == None


from python_code import pp_Definition
from python_code import pp_DefinitionArgumentList

def test_pp_Definition___init__():
    assert pp_Definition.__init__(pp_Definition('', pp_Definition=pp_DefinitionArgumentList(), pp_Definition11=set()), '', pp_Definition=pp_DefinitionArgumentList(), pp_Definition11=set()) == None


from python_code import pp_DefinitionArgument
from python_code import pp_DefinitionArgumentList
from python_code import pp_Expression

def test_pp_DefinitionArgument___init__():
    assert pp_DefinitionArgument.__init__(pp_DefinitionArgument('', '\x00', pp_DefinitionArgument=pp_DefinitionArgumentList(), pp_DefinitionArgument16=pp_Expression()), '\x00\x00', '', pp_DefinitionArgument=pp_DefinitionArgumentList(), pp_DefinitionArgument16=pp_Expression()) == None


from python_code import pp_InterpolatedVariable

def test_pp_InterpolatedVariable___init__():
    assert pp_InterpolatedVariable.__init__(pp_InterpolatedVariable(''), '') == None


from python_code import pp_JavaLambda

def test_pp_JavaLambda___init__():
    assert pp_JavaLambda.__init__(pp_JavaLambda(True), False) == None


from python_code import pp_LiteralBoolean

def test_pp_LiteralBoolean___init__():
    assert pp_LiteralBoolean.__init__(pp_LiteralBoolean(True), False) == None


from python_code import pp_LiteralName

def test_pp_LiteralName___init__():
    assert pp_LiteralName.__init__(pp_LiteralName(''), '') == None


from python_code import pp_LiteralNameOrReference

def test_pp_LiteralNameOrReference___init__():
    assert pp_LiteralNameOrReference.__init__(pp_LiteralNameOrReference(''), '') == None


from python_code import pp_LiteralRegex

def test_pp_LiteralRegex___init__():
    assert pp_LiteralRegex.__init__(pp_LiteralRegex(''), '') == None


from python_code import pp_Expression
from python_code import pp_MethodCall

def test_pp_MethodCall___init__():
    assert pp_MethodCall.__init__(pp_MethodCall(True, pp_MethodCall=pp_Expression()), False, pp_MethodCall=pp_Expression()) == None


from python_code import pp_SingleQuotedString

def test_pp_SingleQuotedString___init__():
    assert pp_SingleQuotedString.__init__(pp_SingleQuotedString(''), '') == None


from python_code import pp_VariableExpression

def test_pp_VariableExpression___init__():
    assert pp_VariableExpression.__init__(pp_VariableExpression(''), '') == None


from python_code import pp_VariableTE

def test_pp_VariableTE___init__():
    assert pp_VariableTE.__init__(pp_VariableTE(''), '') == None


from python_code import pp_VerbatimTE

def test_pp_VerbatimTE___init__():
    assert pp_VerbatimTE.__init__(pp_VerbatimTE(''), '') == None


from python_code import pp_VirtualNameOrReference

def test_pp_VirtualNameOrReference___init__():
    assert pp_VirtualNameOrReference.__init__(pp_VirtualNameOrReference('', False), '', False) == None

