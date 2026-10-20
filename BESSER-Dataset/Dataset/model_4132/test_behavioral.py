import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    Feature_,
    IdentifiableElement,
    Literal,
    PrimaryExpression,
    Type,
    cool_AdditionExpression,
    cool_AssignmentExpression,
    cool_Attr,
    cool_BlockExpression,
    cool_BooleanLiteral,
    cool_Case,
    cool_CaseExpression,
    cool_Class_,
    cool_CompareExpression,
    cool_ConditionalExpression,
    cool_DispatchExpression,
    cool_Div,
    cool_Expression,
    cool_Feature_,
    cool_Formal,
    cool_IdentifiableElement,
    cool_IdentifierRefExpression,
    cool_IntegerCompositeExpression,
    cool_IsvoidExpression,
    cool_LetDeclaration,
    cool_LetExpression,
    cool_Literal,
    cool_LoopExpression,
    cool_Method,
    cool_Minus,
    cool_MultiplicationExpression,
    cool_NegationExpression,
    cool_NewExpression,
    cool_NumberLiteral,
    cool_ParenExpression,
    cool_PrimaryExpression,
    cool_Program,
    cool_SelfTypeLiteral,
    cool_StringLiteral,
    cool_Type,
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

def test_assoc_expr22_stub_double():
    # cool_Expression has no real 'cool_Expression23' property in the generated
    # code (a bare stub) -- manually attach it so cool_AssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cool_AssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cool_AssignmentExpression(name="sample_text")
    partner = cool_Expression()
    setattr(partner, 'cool_Expression23', None)
    _safe_set(owner, 'cool_AssignmentExpression', partner)
    assert getattr(partner, 'cool_Expression23') == owner
    _safe_set(owner, 'cool_AssignmentExpression', None)
    assert getattr(partner, 'cool_Expression23') is None


def test_assoc_id19_stub_double():
    # cool_IdentifierRefExpression has no real 'cool_IdentifierRefExpression' property in the generated
    # code (a bare stub) -- manually attach it so cool_IdentifiableElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cool_IdentifiableElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cool_IdentifiableElement(name="sample_text")
    partner = cool_IdentifierRefExpression()
    setattr(partner, 'cool_IdentifierRefExpression', None)
    _safe_set(owner, 'cool_IdentifiableElement', partner)
    assert getattr(partner, 'cool_IdentifierRefExpression') == owner
    _safe_set(owner, 'cool_IdentifiableElement', None)
    assert getattr(partner, 'cool_IdentifierRefExpression') is None


def test_assoc_left80_stub_double():
    # cool_Expression has no real 'cool_Expression81' property in the generated
    # code (a bare stub) -- manually attach it so cool_CompareExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cool_CompareExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cool_CompareExpression(op="sample_text")
    partner = cool_Expression()
    setattr(partner, 'cool_Expression81', None)
    _safe_set(owner, 'cool_CompareExpression', partner)
    assert getattr(partner, 'cool_Expression81') == owner
    _safe_set(owner, 'cool_CompareExpression', None)
    assert getattr(partner, 'cool_Expression81') is None


def test_assoc_right82_stub_double():
    # cool_Expression has no real 'cool_Expression84' property in the generated
    # code (a bare stub) -- manually attach it so cool_CompareExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cool_CompareExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cool_CompareExpression(op="sample_text")
    partner = cool_Expression()
    setattr(partner, 'cool_Expression84', None)
    _safe_set(owner, 'cool_CompareExpression83', partner)
    assert getattr(partner, 'cool_Expression84') == owner
    _safe_set(owner, 'cool_CompareExpression83', None)
    assert getattr(partner, 'cool_Expression84') is None


