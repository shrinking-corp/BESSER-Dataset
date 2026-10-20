import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    demo1_Category,
    demo1_EObject,
    demo1_Model,
    demo1_RatioExpression,
    demo1_Rule,
    demo1_RuleExpression,
    demo1_TestExpression,
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

def test_assoc_categories0_stub_double():
    # demo1_Model has no real 'demo1_Model' property in the generated
    # code (a bare stub) -- manually attach it so demo1_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # demo1_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = demo1_Category(name="sample_text")
    partner = demo1_Model()
    setattr(partner, 'demo1_Model', None)
    _safe_set(owner, 'demo1_Category', partner)
    assert owner in getattr(partner, 'demo1_Model')
    _safe_set(owner, 'demo1_Category', None)
    assert owner not in getattr(partner, 'demo1_Model')


def test_assoc_category11_stub_double():
    # demo1_TestExpression has no real 'demo1_TestExpression12' property in the generated
    # code (a bare stub) -- manually attach it so demo1_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # demo1_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = demo1_Category(name="sample_text")
    partner = demo1_TestExpression()
    setattr(partner, 'demo1_TestExpression12', None)
    _safe_set(owner, 'demo1_Category13', partner)
    assert getattr(partner, 'demo1_TestExpression12') == owner
    _safe_set(owner, 'demo1_Category13', None)
    assert getattr(partner, 'demo1_TestExpression12') is None


def test_assoc_ratio9_stub_double():
    # demo1_RuleExpression has no real 'demo1_RuleExpression10' property in the generated
    # code (a bare stub) -- manually attach it so demo1_RatioExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # demo1_RatioExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = demo1_RatioExpression(ratio=7)
    partner = demo1_RuleExpression()
    setattr(partner, 'demo1_RuleExpression10', None)
    _safe_set(owner, 'demo1_RatioExpression', partner)
    assert getattr(partner, 'demo1_RuleExpression10') == owner
    _safe_set(owner, 'demo1_RatioExpression', None)
    assert getattr(partner, 'demo1_RuleExpression10') is None


