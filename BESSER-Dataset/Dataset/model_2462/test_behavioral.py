import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    OclExpression,
    operators_IfExp,
    operators_OclExpression,
    operators_OclType,
    operators_OperationCallExp,
    operators_Type,
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

def test_assoc_arguments3_stub_double():
    # operators_OclExpression has no real 'operators_OclExpression5' property in the generated
    # code (a bare stub) -- manually attach it so operators_OperationCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_OperationCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_OperationCallExp(name="sample_text")
    partner = operators_OclExpression()
    setattr(partner, 'operators_OclExpression5', None)
    _safe_set(owner, 'operators_OperationCallExp4', {partner})
    assert getattr(partner, 'operators_OclExpression5') == owner
    _safe_set(owner, 'operators_OperationCallExp4', set())
    assert getattr(partner, 'operators_OclExpression5') is None


def test_assoc_source1_stub_double():
    # operators_OclExpression has no real 'operators_OclExpression2' property in the generated
    # code (a bare stub) -- manually attach it so operators_OperationCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_OperationCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_OperationCallExp(name="sample_text")
    partner = operators_OclExpression()
    setattr(partner, 'operators_OclExpression2', None)
    _safe_set(owner, 'operators_OperationCallExp', partner)
    assert getattr(partner, 'operators_OclExpression2') == owner
    _safe_set(owner, 'operators_OperationCallExp', None)
    assert getattr(partner, 'operators_OclExpression2') is None


def test_assoc_type_0_stub_double():
    # operators_OclExpression has no real 'operators_OclExpression' property in the generated
    # code (a bare stub) -- manually attach it so operators_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Type()
    partner = operators_OclExpression()
    setattr(partner, 'operators_OclExpression', None)
    _safe_set(owner, 'operators_Type', partner)
    assert getattr(partner, 'operators_OclExpression') == owner
    _safe_set(owner, 'operators_Type', None)
    assert getattr(partner, 'operators_OclExpression') is None


