from python_code import timedAutomata_base_Commentable

def test_timedAutomata_base_Commentable___init__():
    assert timedAutomata_base_Commentable.__init__(timedAutomata_base_Commentable(''), '') == None


from python_code import timedAutomata_base_Identifyable

def test_timedAutomata_base_Identifyable___init__():
    assert timedAutomata_base_Identifyable.__init__(timedAutomata_base_Identifyable(0), 0) == None


from python_code import timedAutomata_base_Nameable

def test_timedAutomata_base_Nameable___init__():
    assert timedAutomata_base_Nameable.__init__(timedAutomata_base_Nameable(''), '') == None


from python_code import timedAutomata_bnf_Identifier

def test_timedAutomata_bnf_Identifier___init__():
    assert timedAutomata_bnf_Identifier.__init__(timedAutomata_bnf_Identifier(''), '') == None


from python_code import core_timedAutomata_Label
from python_code import expressions_Expression
from python_code import timedAutomata_core_Location

def test_timedAutomata_core_Location___init__():
    assert timedAutomata_core_Location.__init__(timedAutomata_core_Location('', '\x00', timedAutomata_core_Location209=core_timedAutomata_Label(), timedAutomata_core_Location=expressions_Expression()), '\x00\x00', '', timedAutomata_core_Location209=core_timedAutomata_Label(), timedAutomata_core_Location=expressions_Expression()) == None


from python_code import SystemDefinition
from python_code import timedAutomata_core_Project

def test_timedAutomata_core_Project___init__():
    assert timedAutomata_core_Project.__init__(timedAutomata_core_Project('', timedAutomata_core_Project=set(), timedAutomata_core_Project177=set(), timedAutomata_core_Project179=SystemDefinition()), '', timedAutomata_core_Project=set(), timedAutomata_core_Project177=set(), timedAutomata_core_Project179=SystemDefinition()) == None


from python_code import declarations_ChannelExpression
from python_code import declarations_ChannelPriority
from python_code import timedAutomata_declarations_ComplexChannelPriority

def test_timedAutomata_declarations_ComplexChannelPriority___init__():
    assert timedAutomata_declarations_ComplexChannelPriority.__init__(timedAutomata_declarations_ComplexChannelPriority('', timedAutomata_declarations_ComplexChannelPriority=declarations_ChannelExpression(), timedAutomata_declarations_ComplexChannelPriority155=declarations_ChannelPriority()), '', timedAutomata_declarations_ComplexChannelPriority=declarations_ChannelExpression(), timedAutomata_declarations_ComplexChannelPriority155=declarations_ChannelPriority()) == None


from python_code import expressions_Expression
from python_code import timedAutomata_expressions_AssignmentExpression

def test_timedAutomata_expressions_AssignmentExpression___init__():
    assert timedAutomata_expressions_AssignmentExpression.__init__(timedAutomata_expressions_AssignmentExpression('', timedAutomata_expressions_AssignmentExpression=expressions_Expression(), timedAutomata_expressions_AssignmentExpression19=expressions_Expression()), '', timedAutomata_expressions_AssignmentExpression=expressions_Expression(), timedAutomata_expressions_AssignmentExpression19=expressions_Expression()) == None


from python_code import expressions_Expression
from python_code import timedAutomata_expressions_BinaryExpression

def test_timedAutomata_expressions_BinaryExpression___init__():
    assert timedAutomata_expressions_BinaryExpression.__init__(timedAutomata_expressions_BinaryExpression('', timedAutomata_expressions_BinaryExpression=expressions_Expression(), timedAutomata_expressions_BinaryExpression14=expressions_Expression()), '', timedAutomata_expressions_BinaryExpression=expressions_Expression(), timedAutomata_expressions_BinaryExpression14=expressions_Expression()) == None


from python_code import timedAutomata_expressions_ConstantExpression

def test_timedAutomata_expressions_ConstantExpression___init__():
    assert timedAutomata_expressions_ConstantExpression.__init__(timedAutomata_expressions_ConstantExpression(0), 0) == None


from python_code import timedAutomata_expressions_FixedExpression

def test_timedAutomata_expressions_FixedExpression___init__():
    assert timedAutomata_expressions_FixedExpression.__init__(timedAutomata_expressions_FixedExpression(''), '') == None


from python_code import expressions_Expression
from python_code import timedAutomata_expressions_IncDecExpression

def test_timedAutomata_expressions_IncDecExpression___init__():
    assert timedAutomata_expressions_IncDecExpression.__init__(timedAutomata_expressions_IncDecExpression(False, False, timedAutomata_expressions_IncDecExpression=expressions_Expression()), False, False, timedAutomata_expressions_IncDecExpression=expressions_Expression()) == None


from python_code import expressions_Expression
from python_code import timedAutomata_expressions_UnaryExpression

def test_timedAutomata_expressions_UnaryExpression___init__():
    assert timedAutomata_expressions_UnaryExpression.__init__(timedAutomata_expressions_UnaryExpression('', timedAutomata_expressions_UnaryExpression=expressions_Expression()), '', timedAutomata_expressions_UnaryExpression=expressions_Expression()) == None


from python_code import timedAutomata_types_SimpleType

def test_timedAutomata_types_SimpleType___init__():
    assert timedAutomata_types_SimpleType.__init__(timedAutomata_types_SimpleType(''), '') == None


from python_code import timedAutomata_types_Type

def test_timedAutomata_types_Type___init__():
    assert timedAutomata_types_Type.__init__(timedAutomata_types_Type(''), '') == None

