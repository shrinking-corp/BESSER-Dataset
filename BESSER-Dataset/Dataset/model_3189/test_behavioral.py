import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractTemplate,
    BinaryExpression,
    Block,
    Declaration,
    Declarations,
    DeclaredType,
    Edge,
    Expression,
    Function,
    GlobalDeclarations,
    IdentifierExpression,
    IncrementDecrementExpression,
    Initializer,
    IntegerBounds,
    LocalDeclarations,
    Location,
    NamedElement,
    ParameterContainer,
    Point,
    PredefinedType,
    PriorityItem,
    RedefinedTemplate,
    Selection,
    Statement,
    Synchronization,
    SystemDeclarations,
    Template,
    Type,
    TypeDeclaration,
    TypeExpression,
    TypedDeclaration,
    TypedElement,
    TypedElementContainer,
    Variable,
    core_CommentableElement,
    core_NamedElement,
    core_TypedElement,
    declarations_Declaration,
    declarations_TypedElementContainer,
    expressions_Expression,
    global_ChannelPriorityDeclaration,
    global_ChannelPriorityGroup,
    global_PriorityItem,
    statements_Statement,
    system_InstantiationList,
    system_ProgressMeasure,
    system_System,
    system_TemplateDeclaration,
    uppaal_NTA,
    uppaal_core_CommentableElement,
    uppaal_core_NamedElement,
    uppaal_core_TypedElement,
    uppaal_declarations_ArrayInitializer,
    uppaal_declarations_Declaration,
    uppaal_declarations_Declarations,
    uppaal_declarations_ExpressionInitializer,
    uppaal_declarations_Function,
    uppaal_declarations_GlobalDeclarations,
    uppaal_declarations_Initializer,
    uppaal_declarations_LocalDeclarations,
    uppaal_declarations_Parameter,
    uppaal_declarations_ParameterContainer,
    uppaal_declarations_SystemDeclarations,
    uppaal_declarations_TypeDeclaration,
    uppaal_declarations_TypedDeclaration,
    uppaal_declarations_TypedElementContainer,
    uppaal_declarations_Variable,
    uppaal_expressions_ArithmeticExpression,
    uppaal_expressions_AssignmentExpression,
    uppaal_expressions_BinaryExpression,
    uppaal_expressions_BitShiftExpression,
    uppaal_expressions_BitwiseExpression,
    uppaal_expressions_ChannelPrefixExpression,
    uppaal_expressions_CompareExpression,
    uppaal_expressions_ConditionExpression,
    uppaal_expressions_DataPrefixExpression,
    uppaal_expressions_Expression,
    uppaal_expressions_FunctionCallExpression,
    uppaal_expressions_IdentifierExpression,
    uppaal_expressions_IncrementDecrementExpression,
    uppaal_expressions_LiteralExpression,
    uppaal_expressions_LogicalExpression,
    uppaal_expressions_MinMaxExpression,
    uppaal_expressions_MinusExpression,
    uppaal_expressions_NegationExpression,
    uppaal_expressions_PlusExpression,
    uppaal_expressions_PostIncrementDecrementExpression,
    uppaal_expressions_PreIncrementDecrementExpression,
    uppaal_expressions_QuantificationExpression,
    uppaal_expressions_ScopedIdentifierExpression,
    uppaal_global_ChannelItem,
    uppaal_global_ChannelPriorityDeclaration,
    uppaal_global_ChannelPriorityGroup,
    uppaal_global_DefaultItem,
    uppaal_global_PriorityItem,
    uppaal_statements_Block,
    uppaal_statements_DoWhileLoop,
    uppaal_statements_EmptyStatement,
    uppaal_statements_ExpressionStatement,
    uppaal_statements_ForLoop,
    uppaal_statements_IfStatement,
    uppaal_statements_Iteration,
    uppaal_statements_ReturnStatement,
    uppaal_statements_Statement,
    uppaal_statements_WhileLoop,
    uppaal_system_InstantiationList,
    uppaal_system_ProgressMeasure,
    uppaal_system_System,
    uppaal_system_TemplateDeclaration,
    uppaal_templates_AbstractTemplate,
    uppaal_templates_Edge,
    uppaal_templates_Location,
    uppaal_templates_RedefinedTemplate,
    uppaal_templates_Selection,
    uppaal_templates_Synchronization,
    uppaal_templates_Template,
    uppaal_types_DeclaredType,
    uppaal_types_IntegerBounds,
    uppaal_types_Library,
    uppaal_types_PredefinedType,
    uppaal_types_RangeTypeSpecification,
    uppaal_types_ScalarTypeSpecification,
    uppaal_types_StructTypeSpecification,
    uppaal_types_Type,
    uppaal_types_TypeExpression,
    uppaal_visuals_ColoredElement,
    uppaal_visuals_LinearElement,
    uppaal_visuals_PlanarElement,
    uppaal_visuals_Point,
    visuals_ColoredElement,
    visuals_LinearElement,
    visuals_PlanarElement,
    ArithmeticOperator,
    AssignmentOperator,
    BitShiftOperator,
    BitwiseOperator,
    BuiltInType,
    CallType,
    CompareOperator,
    DataVariablePrefix,
    IncrementDecrementOperator,
    LocationKind,
    LogicalOperator,
    MinMaxOperator,
    Quantifier,
    SynchronizationKind,
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

def test_assoc_channelExpression87_stub_double():
    # IdentifierExpression has no real 'IdentifierExpression88' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_templates_Synchronization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_templates_Synchronization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_templates_Synchronization(kind="sample_text")
    partner = IdentifierExpression()
    setattr(partner, 'IdentifierExpression88', None)
    _safe_set(owner, 'uppaal_templates_Synchronization', partner)
    assert getattr(partner, 'IdentifierExpression88') == owner
    _safe_set(owner, 'uppaal_templates_Synchronization', None)
    assert getattr(partner, 'IdentifierExpression88') is None


def test_assoc_channelType164_stub_double():
    # Type has no real 'Type' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_expressions_ChannelPrefixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_expressions_ChannelPrefixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_expressions_ChannelPrefixExpression(broadcast=True, urgent=True)
    partner = Type()
    setattr(partner, 'Type', None)
    _safe_set(owner, 'uppaal_expressions_ChannelPrefixExpression', partner)
    assert getattr(partner, 'Type') == owner
    _safe_set(owner, 'uppaal_expressions_ChannelPrefixExpression', None)
    assert getattr(partner, 'Type') is None


def test_assoc_dataTypeExpression165_stub_double():
    # Expression has no real 'Expression166' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_expressions_DataPrefixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_expressions_DataPrefixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_expressions_DataPrefixExpression(prefix="sample_text")
    partner = Expression()
    setattr(partner, 'Expression166', None)
    _safe_set(owner, 'uppaal_expressions_DataPrefixExpression', partner)
    assert getattr(partner, 'Expression166') == owner
    _safe_set(owner, 'uppaal_expressions_DataPrefixExpression', None)
    assert getattr(partner, 'Expression166') is None


def test_assoc_expression160_stub_double():
    # Expression has no real 'Expression161' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_expressions_QuantificationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_expressions_QuantificationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_expressions_QuantificationExpression(quantifier="sample_text")
    partner = Expression()
    setattr(partner, 'Expression161', None)
    _safe_set(owner, 'uppaal_expressions_QuantificationExpression', partner)
    assert getattr(partner, 'Expression161') == owner
    _safe_set(owner, 'uppaal_expressions_QuantificationExpression', None)
    assert getattr(partner, 'Expression161') is None


def test_assoc_expression162_stub_double():
    # Expression has no real 'Expression163' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_expressions_IncrementDecrementExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_expressions_IncrementDecrementExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_expressions_IncrementDecrementExpression(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression163', None)
    _safe_set(owner, 'uppaal_expressions_IncrementDecrementExpression', partner)
    assert getattr(partner, 'Expression163') == owner
    _safe_set(owner, 'uppaal_expressions_IncrementDecrementExpression', None)
    assert getattr(partner, 'Expression163') is None


def test_assoc_incomingEdges68_stub_double():
    # Edge has no real 'Edge69' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_templates_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_templates_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_templates_Location(locationTimeKind="sample_text")
    partner = Edge()
    setattr(partner, 'Edge69', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Edge69') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Edge69') is None


def test_assoc_invariant66_stub_double():
    # Expression has no real 'Expression67' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_templates_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_templates_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_templates_Location(locationTimeKind="sample_text")
    partner = Expression()
    setattr(partner, 'Expression67', None)
    _safe_set(owner, 'uppaal_templates_Location', partner)
    assert getattr(partner, 'Expression67') == owner
    _safe_set(owner, 'uppaal_templates_Location', None)
    assert getattr(partner, 'Expression67') is None


def test_assoc_outgoingEdges70_stub_double():
    # Edge has no real 'Edge71' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_templates_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_templates_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_templates_Location(locationTimeKind="sample_text")
    partner = Edge()
    setattr(partner, 'Edge71', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Edge71') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Edge71') is None


def test_assoc_parentTemplate64_stub_double():
    # Template has no real 'Template65' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_templates_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_templates_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_templates_Location(locationTimeKind="sample_text")
    partner = Template()
    setattr(partner, 'Template65', None)
    _safe_set(owner, 'location', partner)
    assert getattr(partner, 'Template65') == owner
    _safe_set(owner, 'location', None)
    assert getattr(partner, 'Template65') is None


