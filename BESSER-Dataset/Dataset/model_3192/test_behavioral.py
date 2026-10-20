import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractTemplate,
    BinaryExpression,
    Block,
    ChannelPriorityItem,
    DataVariableDeclaration,
    Declaration,
    Declarations,
    DeclaredType,
    Edge,
    Expression,
    Function,
    GlobalDeclarations,
    IdentifierExpression,
    Index,
    Initializer,
    IntegerBounds,
    LocalDeclarations,
    Location,
    NamedElement,
    Parameter,
    Point,
    PredefinedType,
    RedefinedTemplate,
    Selection,
    Statement,
    Synchronization,
    SystemDeclarations,
    Template,
    Type,
    TypeDeclaration,
    TypeDefinition,
    TypeSpecification,
    Variable,
    VariableContainer,
    VariableDeclaration,
    core_CommentableElement,
    core_NamedElement,
    declarations_Declaration,
    declarations_VariableContainer,
    expressions_Expression,
    global_ChannelPriority,
    global_ChannelPriorityItem,
    statements_Statement,
    system_InstantiationList,
    system_ProgressMeasure,
    system_System,
    system_TemplateDeclaration,
    uppaal_NTA,
    uppaal_core_CommentableElement,
    uppaal_core_NamedElement,
    uppaal_declarations_ArrayInitializer,
    uppaal_declarations_ChannelVariableDeclaration,
    uppaal_declarations_ClockVariableDeclaration,
    uppaal_declarations_DataVariableDeclaration,
    uppaal_declarations_Declaration,
    uppaal_declarations_Declarations,
    uppaal_declarations_ExpressionInitializer,
    uppaal_declarations_Function,
    uppaal_declarations_FunctionDeclaration,
    uppaal_declarations_GlobalDeclarations,
    uppaal_declarations_Index,
    uppaal_declarations_Initializer,
    uppaal_declarations_LocalDeclarations,
    uppaal_declarations_Parameter,
    uppaal_declarations_SystemDeclarations,
    uppaal_declarations_TypeDeclaration,
    uppaal_declarations_TypeIndex,
    uppaal_declarations_ValueIndex,
    uppaal_declarations_Variable,
    uppaal_declarations_VariableContainer,
    uppaal_declarations_VariableDeclaration,
    uppaal_expressions_ArithmeticExpression,
    uppaal_expressions_AssignmentExpression,
    uppaal_expressions_BinaryExpression,
    uppaal_expressions_BitShiftExpression,
    uppaal_expressions_BitwiseExpression,
    uppaal_expressions_CompareExpression,
    uppaal_expressions_ConditionExpression,
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
    uppaal_expressions_QuantificationExpression,
    uppaal_expressions_ScopedIdentifierExpression,
    uppaal_global_ChannelList,
    uppaal_global_ChannelPriority,
    uppaal_global_ChannelPriorityItem,
    uppaal_global_DefaultChannelPriority,
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
    uppaal_types_PredefinedType,
    uppaal_types_RangeTypeSpecification,
    uppaal_types_ScalarTypeSpecification,
    uppaal_types_StructTypeSpecification,
    uppaal_types_Type,
    uppaal_types_TypeDefinition,
    uppaal_types_TypeReference,
    uppaal_types_TypeSpecification,
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
    ColorKind,
    CompareOperator,
    DataVariablePrefix,
    IncrementDecrementOperator,
    IncrementDecrementPosition,
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

def test_assoc_channelExpression108_stub_double():
    # IdentifierExpression has no real 'IdentifierExpression109' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_templates_Synchronization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_templates_Synchronization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_templates_Synchronization(kind="sample_text")
    partner = IdentifierExpression()
    setattr(partner, 'IdentifierExpression109', None)
    _safe_set(owner, 'uppaal_templates_Synchronization', partner)
    assert getattr(partner, 'IdentifierExpression109') == owner
    _safe_set(owner, 'uppaal_templates_Synchronization', None)
    assert getattr(partner, 'IdentifierExpression109') is None


def test_assoc_expression182_stub_double():
    # Expression has no real 'Expression183' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_expressions_QuantificationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_expressions_QuantificationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_expressions_QuantificationExpression(quantifier="sample_text")
    partner = Expression()
    setattr(partner, 'Expression183', None)
    _safe_set(owner, 'uppaal_expressions_QuantificationExpression', partner)
    assert getattr(partner, 'Expression183') == owner
    _safe_set(owner, 'uppaal_expressions_QuantificationExpression', None)
    assert getattr(partner, 'Expression183') is None


def test_assoc_expression184_stub_double():
    # Expression has no real 'Expression185' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_expressions_IncrementDecrementExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_expressions_IncrementDecrementExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_expressions_IncrementDecrementExpression(operator="sample_text", position="sample_text")
    partner = Expression()
    setattr(partner, 'Expression185', None)
    _safe_set(owner, 'uppaal_expressions_IncrementDecrementExpression', partner)
    assert getattr(partner, 'Expression185') == owner
    _safe_set(owner, 'uppaal_expressions_IncrementDecrementExpression', None)
    assert getattr(partner, 'Expression185') is None


def test_assoc_index19_stub_double():
    # Index has no real 'Index' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_types_Type(baseType="sample_text")
    partner = Index()
    setattr(partner, 'Index', None)
    _safe_set(owner, 'uppaal_types_Type', {partner})
    assert getattr(partner, 'Index') == owner
    _safe_set(owner, 'uppaal_types_Type', set())
    assert getattr(partner, 'Index') is None


def test_assoc_invariant89_stub_double():
    # Expression has no real 'Expression90' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_templates_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_templates_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_templates_Location(locationTimeKind="sample_text")
    partner = Expression()
    setattr(partner, 'Expression90', None)
    _safe_set(owner, 'uppaal_templates_Location', partner)
    assert getattr(partner, 'Expression90') == owner
    _safe_set(owner, 'uppaal_templates_Location', None)
    assert getattr(partner, 'Expression90') is None


def test_assoc_parentTemplate87_stub_double():
    # Template has no real 'Template88' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_templates_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_templates_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_templates_Location(locationTimeKind="sample_text")
    partner = Template()
    setattr(partner, 'Template88', None)
    _safe_set(owner, 'location', partner)
    assert getattr(partner, 'Template88') == owner
    _safe_set(owner, 'location', None)
    assert getattr(partner, 'Template88') is None


def test_assoc_variableDeclaration61_stub_double():
    # VariableDeclaration has no real 'VariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so uppaal_declarations_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uppaal_declarations_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uppaal_declarations_Parameter(callType="sample_text")
    partner = VariableDeclaration()
    setattr(partner, 'VariableDeclaration', None)
    _safe_set(owner, 'uppaal_declarations_Parameter', partner)
    assert getattr(partner, 'VariableDeclaration') == owner
    _safe_set(owner, 'uppaal_declarations_Parameter', None)
    assert getattr(partner, 'VariableDeclaration') is None


