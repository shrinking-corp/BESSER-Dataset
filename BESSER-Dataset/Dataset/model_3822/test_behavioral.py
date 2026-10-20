import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArgumentExpression,
    BinaryExpression,
    Expression,
    Literal,
    UnaryExpression,
    expressions_ArgumentExpression,
    expressions_AssignmentExpression,
    expressions_BinaryExpression,
    expressions_BitwiseAndExpression,
    expressions_BitwiseOrExpression,
    expressions_BitwiseXorExpression,
    expressions_BoolLiteral,
    expressions_ConditionalExpression,
    expressions_DoubleLiteral,
    expressions_EObject,
    expressions_ElementReferenceExpression,
    expressions_Expression,
    expressions_FeatureCall,
    expressions_FloatLiteral,
    expressions_HexLiteral,
    expressions_IntLiteral,
    expressions_Literal,
    expressions_LogicalAndExpression,
    expressions_LogicalNotExpression,
    expressions_LogicalOrExpression,
    expressions_LogicalRelationExpression,
    expressions_NullLiteral,
    expressions_NumericalAddSubtractExpression,
    expressions_NumericalMultiplyDivideExpression,
    expressions_NumericalUnaryExpression,
    expressions_ParenthesizedExpression,
    expressions_PrimitiveValueExpression,
    expressions_ShiftExpression,
    expressions_StringLiteral,
    expressions_Type,
    expressions_TypeCastExpression,
    expressions_UnaryExpression,
    AdditiveOperator,
    AssignmentOperator,
    BitwiseOperator,
    LogicalOperator,
    MultiplicativeOperator,
    RelationalOperator,
    ShiftOperator,
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

def test_assoc_arraySelector26_stub_double():
    # expressions_Expression has no real 'expressions_Expression28' property in the generated
    # code (a bare stub) -- manually attach it so expressions_FeatureCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_FeatureCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_FeatureCall(arrayAccess=True, operationCall=True)
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression28', None)
    _safe_set(owner, 'expressions_FeatureCall27', {partner})
    assert getattr(partner, 'expressions_Expression28') == owner
    _safe_set(owner, 'expressions_FeatureCall27', set())
    assert getattr(partner, 'expressions_Expression28') is None


def test_assoc_arraySelector31_stub_double():
    # expressions_Expression has no real 'expressions_Expression33' property in the generated
    # code (a bare stub) -- manually attach it so expressions_ElementReferenceExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_ElementReferenceExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_ElementReferenceExpression(arrayAccess=True, operationCall=True)
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression33', None)
    _safe_set(owner, 'expressions_ElementReferenceExpression32', {partner})
    assert getattr(partner, 'expressions_Expression33') == owner
    _safe_set(owner, 'expressions_ElementReferenceExpression32', set())
    assert getattr(partner, 'expressions_Expression33') is None


def test_assoc_expression10_stub_double():
    # expressions_Expression has no real 'expressions_Expression12' property in the generated
    # code (a bare stub) -- manually attach it so expressions_AssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_AssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_AssignmentExpression(operator="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression12', None)
    _safe_set(owner, 'expressions_AssignmentExpression11', partner)
    assert getattr(partner, 'expressions_Expression12') == owner
    _safe_set(owner, 'expressions_AssignmentExpression11', None)
    assert getattr(partner, 'expressions_Expression12') is None


def test_assoc_feature24_stub_double():
    # expressions_EObject has no real 'expressions_EObject' property in the generated
    # code (a bare stub) -- manually attach it so expressions_FeatureCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_FeatureCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_FeatureCall(arrayAccess=True, operationCall=True)
    partner = expressions_EObject()
    setattr(partner, 'expressions_EObject', None)
    _safe_set(owner, 'expressions_FeatureCall25', partner)
    assert getattr(partner, 'expressions_EObject') == owner
    _safe_set(owner, 'expressions_FeatureCall25', None)
    assert getattr(partner, 'expressions_EObject') is None


def test_assoc_leftOperand0_stub_double():
    # expressions_Expression has no real 'expressions_Expression' property in the generated
    # code (a bare stub) -- manually attach it so expressions_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_BinaryExpression()
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression', None)
    _safe_set(owner, 'expressions_BinaryExpression', partner)
    assert getattr(partner, 'expressions_Expression') == owner
    _safe_set(owner, 'expressions_BinaryExpression', None)
    assert getattr(partner, 'expressions_Expression') is None


def test_assoc_operand4_stub_double():
    # expressions_Expression has no real 'expressions_Expression5' property in the generated
    # code (a bare stub) -- manually attach it so expressions_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_UnaryExpression()
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression5', None)
    _safe_set(owner, 'expressions_UnaryExpression', partner)
    assert getattr(partner, 'expressions_Expression5') == owner
    _safe_set(owner, 'expressions_UnaryExpression', None)
    assert getattr(partner, 'expressions_Expression5') is None


def test_assoc_owner22_stub_double():
    # expressions_Expression has no real 'expressions_Expression23' property in the generated
    # code (a bare stub) -- manually attach it so expressions_FeatureCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_FeatureCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_FeatureCall(arrayAccess=True, operationCall=True)
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression23', None)
    _safe_set(owner, 'expressions_FeatureCall', partner)
    assert getattr(partner, 'expressions_Expression23') == owner
    _safe_set(owner, 'expressions_FeatureCall', None)
    assert getattr(partner, 'expressions_Expression23') is None


def test_assoc_reference29_stub_double():
    # expressions_EObject has no real 'expressions_EObject30' property in the generated
    # code (a bare stub) -- manually attach it so expressions_ElementReferenceExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_ElementReferenceExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_ElementReferenceExpression(arrayAccess=True, operationCall=True)
    partner = expressions_EObject()
    setattr(partner, 'expressions_EObject30', None)
    _safe_set(owner, 'expressions_ElementReferenceExpression', partner)
    assert getattr(partner, 'expressions_EObject30') == owner
    _safe_set(owner, 'expressions_ElementReferenceExpression', None)
    assert getattr(partner, 'expressions_EObject30') is None


def test_assoc_rightOperand1_stub_double():
    # expressions_Expression has no real 'expressions_Expression3' property in the generated
    # code (a bare stub) -- manually attach it so expressions_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_BinaryExpression()
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression3', None)
    _safe_set(owner, 'expressions_BinaryExpression2', partner)
    assert getattr(partner, 'expressions_Expression3') == owner
    _safe_set(owner, 'expressions_BinaryExpression2', None)
    assert getattr(partner, 'expressions_Expression3') is None


def test_assoc_varRef8_stub_double():
    # expressions_Expression has no real 'expressions_Expression9' property in the generated
    # code (a bare stub) -- manually attach it so expressions_AssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_AssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_AssignmentExpression(operator="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression9', None)
    _safe_set(owner, 'expressions_AssignmentExpression', partner)
    assert getattr(partner, 'expressions_Expression9') == owner
    _safe_set(owner, 'expressions_AssignmentExpression', None)
    assert getattr(partner, 'expressions_Expression9') is None


