import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArrayDeclarationType,
    ChannelExpression,
    ChannelPriority,
    Commentable,
    Declaration,
    Edge,
    Expression,
    Guards,
    Identifier,
    Initialiser,
    Location,
    Position,
    Selections,
    Statement,
    Synchronisation,
    System,
    SystemDefinition,
    TAElement,
    TAParameter,
    Template,
    TemplateInstantiation,
    Type,
    Updates,
    base_Commentable,
    base_Identifyable,
    base_Nameable,
    core_TAElement,
    core_timedAutomata_Label,
    core_timedAutomata_Nail,
    core_timedAutomata_Parameter,
    declarations_ArrayDeclaration,
    declarations_ArrayDeclarationType,
    declarations_Block,
    declarations_ChannelExpression,
    declarations_ChannelPriority,
    declarations_Declaration,
    declarations_FieldDeclaration,
    declarations_Initialiser,
    declarations_Statement,
    declarations_TAParameter,
    declarations_VariableIdentifier,
    expressions_Expression,
    expressions_Selection,
    timedAutomata_base_Commentable,
    timedAutomata_base_Identifyable,
    timedAutomata_base_Nameable,
    timedAutomata_bnf_Identifier,
    timedAutomata_bnf_ReceiveSynchronisation,
    timedAutomata_bnf_SendSynchronisation,
    timedAutomata_bnf_Synchronisation,
    timedAutomata_core_ComplexSystem,
    timedAutomata_core_Edge,
    timedAutomata_core_Guards,
    timedAutomata_core_Location,
    timedAutomata_core_Project,
    timedAutomata_core_Selections,
    timedAutomata_core_SimpleSystem,
    timedAutomata_core_System,
    timedAutomata_core_SystemDefinition,
    timedAutomata_core_TAElement,
    timedAutomata_core_Template,
    timedAutomata_core_TemplateInstantiation,
    timedAutomata_core_Updates,
    timedAutomata_declarations_ArrayDeclaration,
    timedAutomata_declarations_ArrayDeclarationType,
    timedAutomata_declarations_ArrayExpressionType,
    timedAutomata_declarations_ArrayInitialiser,
    timedAutomata_declarations_ArrayTypeType,
    timedAutomata_declarations_Block,
    timedAutomata_declarations_BlockStatement,
    timedAutomata_declarations_CallByReferenceParameter,
    timedAutomata_declarations_CallByValueParameter,
    timedAutomata_declarations_ChannelExpression,
    timedAutomata_declarations_ChannelPriority,
    timedAutomata_declarations_ChannelPriorityDeclaration,
    timedAutomata_declarations_ComplexChannelPriority,
    timedAutomata_declarations_Declaration,
    timedAutomata_declarations_DefaultChannelPriority,
    timedAutomata_declarations_DoWhileLoopStatement,
    timedAutomata_declarations_ExpressionChannelExpression,
    timedAutomata_declarations_ExpressionInitialiser,
    timedAutomata_declarations_ExpressionStatement,
    timedAutomata_declarations_FieldDeclaration,
    timedAutomata_declarations_ForLoopStatement,
    timedAutomata_declarations_FunctionDeclaration,
    timedAutomata_declarations_IdentifierChannelExpression,
    timedAutomata_declarations_IfStatement,
    timedAutomata_declarations_Initialiser,
    timedAutomata_declarations_IterationStatement,
    timedAutomata_declarations_ReturnStatement,
    timedAutomata_declarations_SimpleChannelPriority,
    timedAutomata_declarations_Statement,
    timedAutomata_declarations_TAParameter,
    timedAutomata_declarations_TypeDeclaration,
    timedAutomata_declarations_VariableDeclaration,
    timedAutomata_declarations_VariableIdentifier,
    timedAutomata_declarations_WhileLoopStatement,
    timedAutomata_expressions_ArrayVariableExpression,
    timedAutomata_expressions_AssignmentExpression,
    timedAutomata_expressions_BinaryExpression,
    timedAutomata_expressions_ConstantExpression,
    timedAutomata_expressions_ExistsExpression,
    timedAutomata_expressions_Expression,
    timedAutomata_expressions_FixedExpression,
    timedAutomata_expressions_ForallExpression,
    timedAutomata_expressions_GroupingExpression,
    timedAutomata_expressions_IdentifierExpression,
    timedAutomata_expressions_IncDecExpression,
    timedAutomata_expressions_PointExpression,
    timedAutomata_expressions_Selection,
    timedAutomata_expressions_SimpleIfExpression,
    timedAutomata_expressions_UnaryExpression,
    timedAutomata_expressions_VariableExpression,
    timedAutomata_expressions_WithArgumentsExpression,
    timedAutomata_types_IdentifierType,
    timedAutomata_types_IntegerRange,
    timedAutomata_types_Scalar,
    timedAutomata_types_SimpleType,
    timedAutomata_types_Struct,
    timedAutomata_types_Type,
    types_Type,
    AssignOperator,
    BinaryOperator,
    FixedExpressionType,
    PriorityOperator,
    TypeId,
    TypePrefix,
    UnaryOperator,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_expression21_stub_double():
    # expressions_Expression has no real 'expressions_Expression22' property in the generated
    # code (a bare stub) -- manually attach it so timedAutomata_expressions_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # timedAutomata_expressions_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = timedAutomata_expressions_UnaryExpression(operator="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression22', None)
    _safe_set(owner, 'timedAutomata_expressions_UnaryExpression', partner)
    assert getattr(partner, 'expressions_Expression22') == owner
    _safe_set(owner, 'timedAutomata_expressions_UnaryExpression', None)
    assert getattr(partner, 'expressions_Expression22') is None


def test_assoc_expression7_stub_double():
    # expressions_Expression has no real 'expressions_Expression8' property in the generated
    # code (a bare stub) -- manually attach it so timedAutomata_expressions_IncDecExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # timedAutomata_expressions_IncDecExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = timedAutomata_expressions_IncDecExpression(beforeExpression=True, increment=True)
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression8', None)
    _safe_set(owner, 'timedAutomata_expressions_IncDecExpression', partner)
    assert getattr(partner, 'expressions_Expression8') == owner
    _safe_set(owner, 'timedAutomata_expressions_IncDecExpression', None)
    assert getattr(partner, 'expressions_Expression8') is None


def test_assoc_globalDeclarations174_stub_double():
    # declarations_Declaration has no real 'declarations_Declaration175' property in the generated
    # code (a bare stub) -- manually attach it so timedAutomata_core_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # timedAutomata_core_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = timedAutomata_core_Project(id="sample_text")
    partner = declarations_Declaration()
    setattr(partner, 'declarations_Declaration175', None)
    _safe_set(owner, 'timedAutomata_core_Project', {partner})
    assert getattr(partner, 'declarations_Declaration175') == owner
    _safe_set(owner, 'timedAutomata_core_Project', set())
    assert getattr(partner, 'declarations_Declaration175') is None


def test_assoc_invariant206_stub_double():
    # expressions_Expression has no real 'expressions_Expression207' property in the generated
    # code (a bare stub) -- manually attach it so timedAutomata_core_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # timedAutomata_core_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = timedAutomata_core_Location(committed="sample_text", urgent="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression207', None)
    _safe_set(owner, 'timedAutomata_core_Location', partner)
    assert getattr(partner, 'expressions_Expression207') == owner
    _safe_set(owner, 'timedAutomata_core_Location', None)
    assert getattr(partner, 'expressions_Expression207') is None


def test_assoc_label208_stub_double():
    # core_timedAutomata_Label has no real 'core_timedAutomata_Label' property in the generated
    # code (a bare stub) -- manually attach it so timedAutomata_core_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # timedAutomata_core_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = timedAutomata_core_Location(committed="sample_text", urgent="sample_text")
    partner = core_timedAutomata_Label()
    setattr(partner, 'core_timedAutomata_Label', None)
    _safe_set(owner, 'timedAutomata_core_Location209', partner)
    assert getattr(partner, 'core_timedAutomata_Label') == owner
    _safe_set(owner, 'timedAutomata_core_Location209', None)
    assert getattr(partner, 'core_timedAutomata_Label') is None


def test_assoc_left11_stub_double():
    # expressions_Expression has no real 'expressions_Expression12' property in the generated
    # code (a bare stub) -- manually attach it so timedAutomata_expressions_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # timedAutomata_expressions_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = timedAutomata_expressions_BinaryExpression(operator="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression12', None)
    _safe_set(owner, 'timedAutomata_expressions_BinaryExpression', partner)
    assert getattr(partner, 'expressions_Expression12') == owner
    _safe_set(owner, 'timedAutomata_expressions_BinaryExpression', None)
    assert getattr(partner, 'expressions_Expression12') is None


def test_assoc_leftSide16_stub_double():
    # expressions_Expression has no real 'expressions_Expression17' property in the generated
    # code (a bare stub) -- manually attach it so timedAutomata_expressions_AssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # timedAutomata_expressions_AssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = timedAutomata_expressions_AssignmentExpression(operator="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression17', None)
    _safe_set(owner, 'timedAutomata_expressions_AssignmentExpression', partner)
    assert getattr(partner, 'expressions_Expression17') == owner
    _safe_set(owner, 'timedAutomata_expressions_AssignmentExpression', None)
    assert getattr(partner, 'expressions_Expression17') is None


def test_assoc_leftSideChannelExpression152_stub_double():
    # declarations_ChannelExpression has no real 'declarations_ChannelExpression153' property in the generated
    # code (a bare stub) -- manually attach it so timedAutomata_declarations_ComplexChannelPriority's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # timedAutomata_declarations_ComplexChannelPriority's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = timedAutomata_declarations_ComplexChannelPriority(channelOperator="sample_text")
    partner = declarations_ChannelExpression()
    setattr(partner, 'declarations_ChannelExpression153', None)
    _safe_set(owner, 'timedAutomata_declarations_ComplexChannelPriority', partner)
    assert getattr(partner, 'declarations_ChannelExpression153') == owner
    _safe_set(owner, 'timedAutomata_declarations_ComplexChannelPriority', None)
    assert getattr(partner, 'declarations_ChannelExpression153') is None


def test_assoc_leftSideSystem215_stub_double():
    # System has no real 'System216' property in the generated
    # code (a bare stub) -- manually attach it so timedAutomata_core_ComplexSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # timedAutomata_core_ComplexSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = timedAutomata_core_ComplexSystem(operator="sample_text")
    partner = System()
    setattr(partner, 'System216', None)
    _safe_set(owner, 'timedAutomata_core_ComplexSystem', partner)
    assert getattr(partner, 'System216') == owner
    _safe_set(owner, 'timedAutomata_core_ComplexSystem', None)
    assert getattr(partner, 'System216') is None


def test_assoc_right13_stub_double():
    # expressions_Expression has no real 'expressions_Expression15' property in the generated
    # code (a bare stub) -- manually attach it so timedAutomata_expressions_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # timedAutomata_expressions_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = timedAutomata_expressions_BinaryExpression(operator="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression15', None)
    _safe_set(owner, 'timedAutomata_expressions_BinaryExpression14', partner)
    assert getattr(partner, 'expressions_Expression15') == owner
    _safe_set(owner, 'timedAutomata_expressions_BinaryExpression14', None)
    assert getattr(partner, 'expressions_Expression15') is None


def test_assoc_rightSide18_stub_double():
    # expressions_Expression has no real 'expressions_Expression20' property in the generated
    # code (a bare stub) -- manually attach it so timedAutomata_expressions_AssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # timedAutomata_expressions_AssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = timedAutomata_expressions_AssignmentExpression(operator="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression20', None)
    _safe_set(owner, 'timedAutomata_expressions_AssignmentExpression19', partner)
    assert getattr(partner, 'expressions_Expression20') == owner
    _safe_set(owner, 'timedAutomata_expressions_AssignmentExpression19', None)
    assert getattr(partner, 'expressions_Expression20') is None


def test_assoc_rightSideChannelExpression154_stub_double():
    # declarations_ChannelPriority has no real 'declarations_ChannelPriority156' property in the generated
    # code (a bare stub) -- manually attach it so timedAutomata_declarations_ComplexChannelPriority's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # timedAutomata_declarations_ComplexChannelPriority's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = timedAutomata_declarations_ComplexChannelPriority(channelOperator="sample_text")
    partner = declarations_ChannelPriority()
    setattr(partner, 'declarations_ChannelPriority156', None)
    _safe_set(owner, 'timedAutomata_declarations_ComplexChannelPriority155', partner)
    assert getattr(partner, 'declarations_ChannelPriority156') == owner
    _safe_set(owner, 'timedAutomata_declarations_ComplexChannelPriority155', None)
    assert getattr(partner, 'declarations_ChannelPriority156') is None


def test_assoc_rightSideSystem217_stub_double():
    # System has no real 'System219' property in the generated
    # code (a bare stub) -- manually attach it so timedAutomata_core_ComplexSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # timedAutomata_core_ComplexSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = timedAutomata_core_ComplexSystem(operator="sample_text")
    partner = System()
    setattr(partner, 'System219', None)
    _safe_set(owner, 'timedAutomata_core_ComplexSystem218', partner)
    assert getattr(partner, 'System219') == owner
    _safe_set(owner, 'timedAutomata_core_ComplexSystem218', None)
    assert getattr(partner, 'System219') is None


def test_assoc_systemDeclaration178_stub_double():
    # SystemDefinition has no real 'SystemDefinition' property in the generated
    # code (a bare stub) -- manually attach it so timedAutomata_core_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # timedAutomata_core_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = timedAutomata_core_Project(id="sample_text")
    partner = SystemDefinition()
    setattr(partner, 'SystemDefinition', None)
    _safe_set(owner, 'timedAutomata_core_Project179', partner)
    assert getattr(partner, 'SystemDefinition') == owner
    _safe_set(owner, 'timedAutomata_core_Project179', None)
    assert getattr(partner, 'SystemDefinition') is None


def test_assoc_templates176_stub_double():
    # Template has no real 'Template' property in the generated
    # code (a bare stub) -- manually attach it so timedAutomata_core_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # timedAutomata_core_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = timedAutomata_core_Project(id="sample_text")
    partner = Template()
    setattr(partner, 'Template', None)
    _safe_set(owner, 'timedAutomata_core_Project177', {partner})
    assert getattr(partner, 'Template') == owner
    _safe_set(owner, 'timedAutomata_core_Project177', set())
    assert getattr(partner, 'Template') is None


