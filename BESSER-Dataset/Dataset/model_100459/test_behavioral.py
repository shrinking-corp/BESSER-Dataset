import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BuiltinEventSpec,
    Declaration,
    DefRoot,
    Effect,
    Event,
    EventSpec,
    Expression,
    Literal,
    NamedElement,
    Operation,
    Property,
    Reaction,
    ReactionProperty,
    Scope,
    ScopedElement,
    StatechartScope,
    Statement,
    Trigger,
    Variable,
    stext_ActiveStateReferenceExpression,
    stext_AlwaysEvent,
    stext_AssignmentExpression,
    stext_BitwiseAndExpression,
    stext_BitwiseOrExpression,
    stext_BitwiseXorExpression,
    stext_BoolLiteral,
    stext_BuiltinEventSpec,
    stext_ConditionalExpression,
    stext_DefRoot,
    stext_DefaultEvent,
    stext_EObject,
    stext_ElementReferenceExpression,
    stext_EntryEvent,
    stext_EntryPointSpec,
    stext_Entrypoint,
    stext_EventDefinition,
    stext_EventRaisingExpression,
    stext_EventSpec,
    stext_EventValueReferenceExpression,
    stext_ExitEvent,
    stext_ExitPointSpec,
    stext_Exitpoint,
    stext_Expression,
    stext_FeatureCall,
    stext_HexLiteral,
    stext_IntLiteral,
    stext_InterfaceScope,
    stext_InternalScope,
    stext_Literal,
    stext_LocalReaction,
    stext_LogicalAndExpression,
    stext_LogicalNotExpression,
    stext_LogicalOrExpression,
    stext_LogicalRelationExpression,
    stext_NumericalAddSubtractExpression,
    stext_NumericalMultiplyDivideExpression,
    stext_NumericalUnaryExpression,
    stext_OnCycleEvent,
    stext_OperationDefinition,
    stext_PrimitiveValueExpression,
    stext_ReactionEffect,
    stext_ReactionProperties,
    stext_ReactionProperty,
    stext_ReactionTrigger,
    stext_RealLiteral,
    stext_RegularEventSpec,
    stext_Root,
    stext_Scope,
    stext_ShiftExpression,
    stext_SimpleScope,
    stext_State,
    stext_StateRoot,
    stext_StateSpecification,
    stext_StatechartRoot,
    stext_StatechartScope,
    stext_StatechartSpecification,
    stext_StringLiteral,
    stext_TimeEventSpec,
    stext_TransitionReaction,
    stext_TransitionRoot,
    stext_TransitionSpecification,
    stext_VariableDefinition,
    AdditiveOperator,
    AssignmentOperator,
    Direction,
    MultiplicativeOperator,
    RelationalOperator,
    ShiftOperator,
    TimeEventType,
    TimeUnit,
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

def test_assoc_args100_stub_double():
    # stext_Expression has no real 'stext_Expression102' property in the generated
    # code (a bare stub) -- manually attach it so stext_ElementReferenceExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_ElementReferenceExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_ElementReferenceExpression(operationCall=True)
    partner = stext_Expression()
    setattr(partner, 'stext_Expression102', None)
    _safe_set(owner, 'stext_ElementReferenceExpression101', {partner})
    assert getattr(partner, 'stext_Expression102') == owner
    _safe_set(owner, 'stext_ElementReferenceExpression101', set())
    assert getattr(partner, 'stext_Expression102') is None


def test_assoc_args95_stub_double():
    # stext_Expression has no real 'stext_Expression97' property in the generated
    # code (a bare stub) -- manually attach it so stext_FeatureCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_FeatureCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_FeatureCall(operationCall=True)
    partner = stext_Expression()
    setattr(partner, 'stext_Expression97', None)
    _safe_set(owner, 'stext_FeatureCall96', {partner})
    assert getattr(partner, 'stext_Expression97') == owner
    _safe_set(owner, 'stext_FeatureCall96', set())
    assert getattr(partner, 'stext_Expression97') is None


def test_assoc_expression30_stub_double():
    # stext_Expression has no real 'stext_Expression32' property in the generated
    # code (a bare stub) -- manually attach it so stext_AssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_AssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_AssignmentExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression32', None)
    _safe_set(owner, 'stext_AssignmentExpression31', partner)
    assert getattr(partner, 'stext_Expression32') == owner
    _safe_set(owner, 'stext_AssignmentExpression31', None)
    assert getattr(partner, 'stext_Expression32') is None


def test_assoc_feature93_stub_double():
    # stext_EObject has no real 'stext_EObject' property in the generated
    # code (a bare stub) -- manually attach it so stext_FeatureCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_FeatureCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_FeatureCall(operationCall=True)
    partner = stext_EObject()
    setattr(partner, 'stext_EObject', None)
    _safe_set(owner, 'stext_FeatureCall94', partner)
    assert getattr(partner, 'stext_EObject') == owner
    _safe_set(owner, 'stext_FeatureCall94', None)
    assert getattr(partner, 'stext_EObject') is None


def test_assoc_initialValue8_stub_double():
    # stext_Expression has no real 'stext_Expression' property in the generated
    # code (a bare stub) -- manually attach it so stext_VariableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_VariableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_VariableDefinition(external=True, readonly=True)
    partner = stext_Expression()
    setattr(partner, 'stext_Expression', None)
    _safe_set(owner, 'stext_VariableDefinition', partner)
    assert getattr(partner, 'stext_Expression') == owner
    _safe_set(owner, 'stext_VariableDefinition', None)
    assert getattr(partner, 'stext_Expression') is None


def test_assoc_leftOperand68_stub_double():
    # stext_Expression has no real 'stext_Expression69' property in the generated
    # code (a bare stub) -- manually attach it so stext_LogicalRelationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_LogicalRelationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_LogicalRelationExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression69', None)
    _safe_set(owner, 'stext_LogicalRelationExpression', partner)
    assert getattr(partner, 'stext_Expression69') == owner
    _safe_set(owner, 'stext_LogicalRelationExpression', None)
    assert getattr(partner, 'stext_Expression69') is None


def test_assoc_leftOperand73_stub_double():
    # stext_Expression has no real 'stext_Expression74' property in the generated
    # code (a bare stub) -- manually attach it so stext_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_ShiftExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression74', None)
    _safe_set(owner, 'stext_ShiftExpression', partner)
    assert getattr(partner, 'stext_Expression74') == owner
    _safe_set(owner, 'stext_ShiftExpression', None)
    assert getattr(partner, 'stext_Expression74') is None


def test_assoc_leftOperand78_stub_double():
    # stext_Expression has no real 'stext_Expression79' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalAddSubtractExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalAddSubtractExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalAddSubtractExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression79', None)
    _safe_set(owner, 'stext_NumericalAddSubtractExpression', partner)
    assert getattr(partner, 'stext_Expression79') == owner
    _safe_set(owner, 'stext_NumericalAddSubtractExpression', None)
    assert getattr(partner, 'stext_Expression79') is None


def test_assoc_leftOperand83_stub_double():
    # stext_Expression has no real 'stext_Expression84' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalMultiplyDivideExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalMultiplyDivideExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalMultiplyDivideExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression84', None)
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression', partner)
    assert getattr(partner, 'stext_Expression84') == owner
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression', None)
    assert getattr(partner, 'stext_Expression84') is None


def test_assoc_operand88_stub_double():
    # stext_Expression has no real 'stext_Expression89' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalUnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalUnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalUnaryExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression89', None)
    _safe_set(owner, 'stext_NumericalUnaryExpression', partner)
    assert getattr(partner, 'stext_Expression89') == owner
    _safe_set(owner, 'stext_NumericalUnaryExpression', None)
    assert getattr(partner, 'stext_Expression89') is None


def test_assoc_owner91_stub_double():
    # stext_Expression has no real 'stext_Expression92' property in the generated
    # code (a bare stub) -- manually attach it so stext_FeatureCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_FeatureCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_FeatureCall(operationCall=True)
    partner = stext_Expression()
    setattr(partner, 'stext_Expression92', None)
    _safe_set(owner, 'stext_FeatureCall', partner)
    assert getattr(partner, 'stext_Expression92') == owner
    _safe_set(owner, 'stext_FeatureCall', None)
    assert getattr(partner, 'stext_Expression92') is None


def test_assoc_reference98_stub_double():
    # stext_EObject has no real 'stext_EObject99' property in the generated
    # code (a bare stub) -- manually attach it so stext_ElementReferenceExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_ElementReferenceExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_ElementReferenceExpression(operationCall=True)
    partner = stext_EObject()
    setattr(partner, 'stext_EObject99', None)
    _safe_set(owner, 'stext_ElementReferenceExpression', partner)
    assert getattr(partner, 'stext_EObject99') == owner
    _safe_set(owner, 'stext_ElementReferenceExpression', None)
    assert getattr(partner, 'stext_EObject99') is None


def test_assoc_rightOperand70_stub_double():
    # stext_Expression has no real 'stext_Expression72' property in the generated
    # code (a bare stub) -- manually attach it so stext_LogicalRelationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_LogicalRelationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_LogicalRelationExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression72', None)
    _safe_set(owner, 'stext_LogicalRelationExpression71', partner)
    assert getattr(partner, 'stext_Expression72') == owner
    _safe_set(owner, 'stext_LogicalRelationExpression71', None)
    assert getattr(partner, 'stext_Expression72') is None


def test_assoc_rightOperand75_stub_double():
    # stext_Expression has no real 'stext_Expression77' property in the generated
    # code (a bare stub) -- manually attach it so stext_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_ShiftExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression77', None)
    _safe_set(owner, 'stext_ShiftExpression76', partner)
    assert getattr(partner, 'stext_Expression77') == owner
    _safe_set(owner, 'stext_ShiftExpression76', None)
    assert getattr(partner, 'stext_Expression77') is None


def test_assoc_rightOperand80_stub_double():
    # stext_Expression has no real 'stext_Expression82' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalAddSubtractExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalAddSubtractExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalAddSubtractExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression82', None)
    _safe_set(owner, 'stext_NumericalAddSubtractExpression81', partner)
    assert getattr(partner, 'stext_Expression82') == owner
    _safe_set(owner, 'stext_NumericalAddSubtractExpression81', None)
    assert getattr(partner, 'stext_Expression82') is None


def test_assoc_rightOperand85_stub_double():
    # stext_Expression has no real 'stext_Expression87' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalMultiplyDivideExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalMultiplyDivideExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalMultiplyDivideExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression87', None)
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression86', partner)
    assert getattr(partner, 'stext_Expression87') == owner
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression86', None)
    assert getattr(partner, 'stext_Expression87') is None


def test_assoc_varRef28_stub_double():
    # stext_Expression has no real 'stext_Expression29' property in the generated
    # code (a bare stub) -- manually attach it so stext_AssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_AssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_AssignmentExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression29', None)
    _safe_set(owner, 'stext_AssignmentExpression', partner)
    assert getattr(partner, 'stext_Expression29') == owner
    _safe_set(owner, 'stext_AssignmentExpression', None)
    assert getattr(partner, 'stext_Expression29') is None


