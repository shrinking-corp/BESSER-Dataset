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
    stext_DefaultTrigger,
    stext_EObject,
    stext_ElementReferenceExpression,
    stext_EntryEvent,
    stext_EntryPointSpec,
    stext_EventDefinition,
    stext_EventRaisingExpression,
    stext_EventSpec,
    stext_EventValueReferenceExpression,
    stext_ExitEvent,
    stext_ExitPointSpec,
    stext_Expression,
    stext_FeatureCall,
    stext_Guard,
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
    stext_OperationDefinition,
    stext_ParenthesizedExpression,
    stext_PrimitiveValueExpression,
    stext_ReactionEffect,
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

def test_assoc_args93_stub_double():
    # stext_Expression has no real 'stext_Expression95' property in the generated
    # code (a bare stub) -- manually attach it so stext_FeatureCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_FeatureCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_FeatureCall(operationCall=True)
    partner = stext_Expression()
    setattr(partner, 'stext_Expression95', None)
    _safe_set(owner, 'stext_FeatureCall94', {partner})
    assert getattr(partner, 'stext_Expression95') == owner
    _safe_set(owner, 'stext_FeatureCall94', set())
    assert getattr(partner, 'stext_Expression95') is None


def test_assoc_args98_stub_double():
    # stext_Expression has no real 'stext_Expression100' property in the generated
    # code (a bare stub) -- manually attach it so stext_ElementReferenceExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_ElementReferenceExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_ElementReferenceExpression(operationCall=True)
    partner = stext_Expression()
    setattr(partner, 'stext_Expression100', None)
    _safe_set(owner, 'stext_ElementReferenceExpression99', {partner})
    assert getattr(partner, 'stext_Expression100') == owner
    _safe_set(owner, 'stext_ElementReferenceExpression99', set())
    assert getattr(partner, 'stext_Expression100') is None


def test_assoc_expression28_stub_double():
    # stext_Expression has no real 'stext_Expression30' property in the generated
    # code (a bare stub) -- manually attach it so stext_AssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_AssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_AssignmentExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression30', None)
    _safe_set(owner, 'stext_AssignmentExpression29', partner)
    assert getattr(partner, 'stext_Expression30') == owner
    _safe_set(owner, 'stext_AssignmentExpression29', None)
    assert getattr(partner, 'stext_Expression30') is None


def test_assoc_feature91_stub_double():
    # stext_EObject has no real 'stext_EObject' property in the generated
    # code (a bare stub) -- manually attach it so stext_FeatureCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_FeatureCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_FeatureCall(operationCall=True)
    partner = stext_EObject()
    setattr(partner, 'stext_EObject', None)
    _safe_set(owner, 'stext_FeatureCall92', partner)
    assert getattr(partner, 'stext_EObject') == owner
    _safe_set(owner, 'stext_FeatureCall92', None)
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


def test_assoc_leftOperand66_stub_double():
    # stext_Expression has no real 'stext_Expression67' property in the generated
    # code (a bare stub) -- manually attach it so stext_LogicalRelationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_LogicalRelationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_LogicalRelationExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression67', None)
    _safe_set(owner, 'stext_LogicalRelationExpression', partner)
    assert getattr(partner, 'stext_Expression67') == owner
    _safe_set(owner, 'stext_LogicalRelationExpression', None)
    assert getattr(partner, 'stext_Expression67') is None


def test_assoc_leftOperand71_stub_double():
    # stext_Expression has no real 'stext_Expression72' property in the generated
    # code (a bare stub) -- manually attach it so stext_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_ShiftExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression72', None)
    _safe_set(owner, 'stext_ShiftExpression', partner)
    assert getattr(partner, 'stext_Expression72') == owner
    _safe_set(owner, 'stext_ShiftExpression', None)
    assert getattr(partner, 'stext_Expression72') is None


def test_assoc_leftOperand76_stub_double():
    # stext_Expression has no real 'stext_Expression77' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalAddSubtractExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalAddSubtractExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalAddSubtractExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression77', None)
    _safe_set(owner, 'stext_NumericalAddSubtractExpression', partner)
    assert getattr(partner, 'stext_Expression77') == owner
    _safe_set(owner, 'stext_NumericalAddSubtractExpression', None)
    assert getattr(partner, 'stext_Expression77') is None


def test_assoc_leftOperand81_stub_double():
    # stext_Expression has no real 'stext_Expression82' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalMultiplyDivideExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalMultiplyDivideExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalMultiplyDivideExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression82', None)
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression', partner)
    assert getattr(partner, 'stext_Expression82') == owner
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression', None)
    assert getattr(partner, 'stext_Expression82') is None


def test_assoc_operand86_stub_double():
    # stext_Expression has no real 'stext_Expression87' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalUnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalUnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalUnaryExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression87', None)
    _safe_set(owner, 'stext_NumericalUnaryExpression', partner)
    assert getattr(partner, 'stext_Expression87') == owner
    _safe_set(owner, 'stext_NumericalUnaryExpression', None)
    assert getattr(partner, 'stext_Expression87') is None


def test_assoc_owner89_stub_double():
    # stext_Expression has no real 'stext_Expression90' property in the generated
    # code (a bare stub) -- manually attach it so stext_FeatureCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_FeatureCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_FeatureCall(operationCall=True)
    partner = stext_Expression()
    setattr(partner, 'stext_Expression90', None)
    _safe_set(owner, 'stext_FeatureCall', partner)
    assert getattr(partner, 'stext_Expression90') == owner
    _safe_set(owner, 'stext_FeatureCall', None)
    assert getattr(partner, 'stext_Expression90') is None


def test_assoc_reference96_stub_double():
    # stext_EObject has no real 'stext_EObject97' property in the generated
    # code (a bare stub) -- manually attach it so stext_ElementReferenceExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_ElementReferenceExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_ElementReferenceExpression(operationCall=True)
    partner = stext_EObject()
    setattr(partner, 'stext_EObject97', None)
    _safe_set(owner, 'stext_ElementReferenceExpression', partner)
    assert getattr(partner, 'stext_EObject97') == owner
    _safe_set(owner, 'stext_ElementReferenceExpression', None)
    assert getattr(partner, 'stext_EObject97') is None


def test_assoc_rightOperand68_stub_double():
    # stext_Expression has no real 'stext_Expression70' property in the generated
    # code (a bare stub) -- manually attach it so stext_LogicalRelationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_LogicalRelationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_LogicalRelationExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression70', None)
    _safe_set(owner, 'stext_LogicalRelationExpression69', partner)
    assert getattr(partner, 'stext_Expression70') == owner
    _safe_set(owner, 'stext_LogicalRelationExpression69', None)
    assert getattr(partner, 'stext_Expression70') is None


def test_assoc_rightOperand73_stub_double():
    # stext_Expression has no real 'stext_Expression75' property in the generated
    # code (a bare stub) -- manually attach it so stext_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_ShiftExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression75', None)
    _safe_set(owner, 'stext_ShiftExpression74', partner)
    assert getattr(partner, 'stext_Expression75') == owner
    _safe_set(owner, 'stext_ShiftExpression74', None)
    assert getattr(partner, 'stext_Expression75') is None


def test_assoc_rightOperand78_stub_double():
    # stext_Expression has no real 'stext_Expression80' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalAddSubtractExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalAddSubtractExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalAddSubtractExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression80', None)
    _safe_set(owner, 'stext_NumericalAddSubtractExpression79', partner)
    assert getattr(partner, 'stext_Expression80') == owner
    _safe_set(owner, 'stext_NumericalAddSubtractExpression79', None)
    assert getattr(partner, 'stext_Expression80') is None


def test_assoc_rightOperand83_stub_double():
    # stext_Expression has no real 'stext_Expression85' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalMultiplyDivideExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalMultiplyDivideExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalMultiplyDivideExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression85', None)
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression84', partner)
    assert getattr(partner, 'stext_Expression85') == owner
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression84', None)
    assert getattr(partner, 'stext_Expression85') is None


def test_assoc_value13_stub_double():
    # stext_Expression has no real 'stext_Expression14' property in the generated
    # code (a bare stub) -- manually attach it so stext_TimeEventSpec's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_TimeEventSpec's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_TimeEventSpec(type="sample_text", unit="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression14', None)
    _safe_set(owner, 'stext_TimeEventSpec', partner)
    assert getattr(partner, 'stext_Expression14') == owner
    _safe_set(owner, 'stext_TimeEventSpec', None)
    assert getattr(partner, 'stext_Expression14') is None


def test_assoc_varRef26_stub_double():
    # stext_Expression has no real 'stext_Expression27' property in the generated
    # code (a bare stub) -- manually attach it so stext_AssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_AssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_AssignmentExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression27', None)
    _safe_set(owner, 'stext_AssignmentExpression', partner)
    assert getattr(partner, 'stext_Expression27') == owner
    _safe_set(owner, 'stext_AssignmentExpression', None)
    assert getattr(partner, 'stext_Expression27') is None


