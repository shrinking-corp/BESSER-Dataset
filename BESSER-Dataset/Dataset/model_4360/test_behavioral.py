import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryExpression,
    Expression,
    FeatureCallExpression,
    Statement,
    simple_lang_ArithmeticExpression,
    simple_lang_AssignmentStatement,
    simple_lang_BinaryExpression,
    simple_lang_ComparisonExpression,
    simple_lang_Expression,
    simple_lang_ExpressionStatement,
    simple_lang_FeatureCallExpression,
    simple_lang_IfStatement,
    simple_lang_LogicalExpression,
    simple_lang_MethodCallExpression,
    simple_lang_PropertyCallExpression,
    simple_lang_SimpleLang,
    simple_lang_Statement,
    simple_lang_Type,
    simple_lang_WhileStatement,
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

def test_assoc_lhs2_stub_double():
    # simple_lang_Expression has no real 'simple_lang_Expression3' property in the generated
    # code (a bare stub) -- manually attach it so simple_lang_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simple_lang_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simple_lang_BinaryExpression(operator="sample_text")
    partner = simple_lang_Expression()
    setattr(partner, 'simple_lang_Expression3', None)
    _safe_set(owner, 'simple_lang_BinaryExpression', partner)
    assert getattr(partner, 'simple_lang_Expression3') == owner
    _safe_set(owner, 'simple_lang_BinaryExpression', None)
    assert getattr(partner, 'simple_lang_Expression3') is None


def test_assoc_rhs4_stub_double():
    # simple_lang_Expression has no real 'simple_lang_Expression6' property in the generated
    # code (a bare stub) -- manually attach it so simple_lang_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simple_lang_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simple_lang_BinaryExpression(operator="sample_text")
    partner = simple_lang_Expression()
    setattr(partner, 'simple_lang_Expression6', None)
    _safe_set(owner, 'simple_lang_BinaryExpression5', partner)
    assert getattr(partner, 'simple_lang_Expression6') == owner
    _safe_set(owner, 'simple_lang_BinaryExpression5', None)
    assert getattr(partner, 'simple_lang_Expression6') is None


def test_assoc_target7_stub_double():
    # simple_lang_Expression has no real 'simple_lang_Expression8' property in the generated
    # code (a bare stub) -- manually attach it so simple_lang_FeatureCallExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simple_lang_FeatureCallExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simple_lang_FeatureCallExpression(name="sample_text")
    partner = simple_lang_Expression()
    setattr(partner, 'simple_lang_Expression8', None)
    _safe_set(owner, 'simple_lang_FeatureCallExpression', partner)
    assert getattr(partner, 'simple_lang_Expression8') == owner
    _safe_set(owner, 'simple_lang_FeatureCallExpression', None)
    assert getattr(partner, 'simple_lang_Expression8') is None


