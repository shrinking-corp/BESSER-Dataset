from python_code import uppaal_core_CommentableElement

def test_uppaal_core_CommentableElement___init__():
    assert uppaal_core_CommentableElement.__init__(uppaal_core_CommentableElement(''), '') == None


from python_code import uppaal_core_NamedElement

def test_uppaal_core_NamedElement___init__():
    assert uppaal_core_NamedElement.__init__(uppaal_core_NamedElement(''), '') == None


from python_code import VariableDeclaration
from python_code import uppaal_declarations_ChannelVariableDeclaration
from python_code import uppaal_declarations_Parameter

def test_uppaal_declarations_ChannelVariableDeclaration___init__():
    assert uppaal_declarations_ChannelVariableDeclaration.__init__(uppaal_declarations_ChannelVariableDeclaration(False, False, VariableDeclaration=uppaal_declarations_Parameter('', uppaal_declarations_Parameter=VariableDeclaration())), False, True, VariableDeclaration=uppaal_declarations_Parameter('', uppaal_declarations_Parameter=VariableDeclaration())) == None


from python_code import VariableDeclaration
from python_code import uppaal_declarations_DataVariableDeclaration
from python_code import uppaal_declarations_Parameter

def test_uppaal_declarations_DataVariableDeclaration___init__():
    assert uppaal_declarations_DataVariableDeclaration.__init__(uppaal_declarations_DataVariableDeclaration('', VariableDeclaration=uppaal_declarations_Parameter('', uppaal_declarations_Parameter=VariableDeclaration())), '', VariableDeclaration=uppaal_declarations_Parameter('', uppaal_declarations_Parameter=VariableDeclaration())) == None


from python_code import VariableDeclaration
from python_code import uppaal_declarations_Parameter

def test_uppaal_declarations_Parameter___init__():
    assert uppaal_declarations_Parameter.__init__(uppaal_declarations_Parameter('', uppaal_declarations_Parameter=VariableDeclaration()), '', uppaal_declarations_Parameter=VariableDeclaration()) == None


from python_code import uppaal_expressions_ArithmeticExpression

def test_uppaal_expressions_ArithmeticExpression___init__():
    assert uppaal_expressions_ArithmeticExpression.__init__(uppaal_expressions_ArithmeticExpression(''), '') == None


from python_code import uppaal_expressions_AssignmentExpression

def test_uppaal_expressions_AssignmentExpression___init__():
    assert uppaal_expressions_AssignmentExpression.__init__(uppaal_expressions_AssignmentExpression(''), '') == None


from python_code import uppaal_expressions_BitShiftExpression

def test_uppaal_expressions_BitShiftExpression___init__():
    assert uppaal_expressions_BitShiftExpression.__init__(uppaal_expressions_BitShiftExpression(''), '') == None


from python_code import uppaal_expressions_BitwiseExpression

def test_uppaal_expressions_BitwiseExpression___init__():
    assert uppaal_expressions_BitwiseExpression.__init__(uppaal_expressions_BitwiseExpression(''), '') == None


from python_code import uppaal_expressions_CompareExpression

def test_uppaal_expressions_CompareExpression___init__():
    assert uppaal_expressions_CompareExpression.__init__(uppaal_expressions_CompareExpression(''), '') == None


from python_code import uppaal_expressions_LogicalExpression

def test_uppaal_expressions_LogicalExpression___init__():
    assert uppaal_expressions_LogicalExpression.__init__(uppaal_expressions_LogicalExpression(''), '') == None


from python_code import uppaal_expressions_MinMaxExpression

def test_uppaal_expressions_MinMaxExpression___init__():
    assert uppaal_expressions_MinMaxExpression.__init__(uppaal_expressions_MinMaxExpression(''), '') == None


from python_code import IdentifierExpression
from python_code import uppaal_templates_Synchronization

def test_uppaal_templates_Synchronization___init__():
    assert uppaal_templates_Synchronization.__init__(uppaal_templates_Synchronization('', uppaal_templates_Synchronization=IdentifierExpression()), '', uppaal_templates_Synchronization=IdentifierExpression()) == None


from python_code import uppaal_types_PredefinedType
from python_code import uppaal_types_TypeReference

def test_uppaal_types_PredefinedType___init__():
    assert uppaal_types_PredefinedType.__init__(uppaal_types_PredefinedType('', Type=uppaal_types_TypeReference()), '', Type=uppaal_types_TypeReference()) == None


from python_code import TypeSpecification
from python_code import uppaal_expressions_IdentifierExpression
from python_code import uppaal_types_Type

def test_uppaal_types_Type___init__():
    assert uppaal_types_Type.__init__(uppaal_types_Type('\x00\x00', uppaal_types_Type=set(), uppaal_types_Type21=TypeSpecification(), NamedElement=uppaal_expressions_IdentifierExpression()), '', uppaal_types_Type=set(), uppaal_types_Type21=TypeSpecification(), NamedElement=uppaal_expressions_IdentifierExpression()) == None


from python_code import TypeSpecification
from python_code import uppaal_types_TypeDefinition

def test_uppaal_types_TypeDefinition___init__():
    assert uppaal_types_TypeDefinition.__init__(uppaal_types_TypeDefinition('', uppaal_types_TypeDefinition=TypeSpecification()), '', uppaal_types_TypeDefinition=TypeSpecification()) == None


from python_code import uppaal_visuals_ColoredElement

def test_uppaal_visuals_ColoredElement___init__():
    assert uppaal_visuals_ColoredElement.__init__(uppaal_visuals_ColoredElement('', '\x00'), '\x00\x00', '') == None


from python_code import uppaal_visuals_Point

def test_uppaal_visuals_Point___init__():
    assert uppaal_visuals_Point.__init__(uppaal_visuals_Point(0, 0), 0, 0) == None

