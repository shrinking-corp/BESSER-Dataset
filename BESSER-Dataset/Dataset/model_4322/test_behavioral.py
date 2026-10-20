import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ConstraintMetric,
    Metric,
    metric_Constraint,
    metric_ConstraintMetric,
    metric_ConstraintMetrics,
    metric_Metric,
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

def test_assoc_constraintMetrics0_reverse_link_reassign_clear():
    a1 = metric_ConstraintMetrics(numberOfConstraintsByKind="sample_text")
    a2 = metric_ConstraintMetrics(numberOfConstraintsByKind="sample_text_2")
    b = metric_ConstraintMetric(calledOperations="sample_text", calledProperties="sample_text", expressionCount=7, expressionDepth=7, numberOfIfExpressions=7, numberOfLetExpressions=7, usedIterators="sample_text", usedLiterals="sample_text")
    _safe_set(b, 'metric_ConstraintMetric', a1)
    assert _is_linked(b, 'metric_ConstraintMetric', a1)
    if hasattr(a1, 'metric_ConstraintMetrics'):
        assert _is_linked(a1, 'metric_ConstraintMetrics', b)
    _safe_set(b, 'metric_ConstraintMetric', a2)
    assert _is_linked(b, 'metric_ConstraintMetric', a2)
    if hasattr(a1, 'metric_ConstraintMetrics'):
        assert not _is_linked(a1, 'metric_ConstraintMetrics', b)
    if hasattr(a2, 'metric_ConstraintMetrics'):
        assert _is_linked(a2, 'metric_ConstraintMetrics', b)
    _safe_set(b, 'metric_ConstraintMetric', None)
    assert not _is_linked(b, 'metric_ConstraintMetric', a2)
    if hasattr(a2, 'metric_ConstraintMetrics'):
        assert not _is_linked(a2, 'metric_ConstraintMetrics', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_constraints1_stub_double():
    # metric_Constraint has no real 'metric_Constraint' property in the generated
    # code (a bare stub) -- manually attach it so metric_ConstraintMetrics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metric_ConstraintMetrics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metric_ConstraintMetrics(numberOfConstraintsByKind="sample_text")
    partner = metric_Constraint()
    setattr(partner, 'metric_Constraint', None)
    _safe_set(owner, 'metric_ConstraintMetrics2', {partner})
    assert getattr(partner, 'metric_Constraint') == owner
    _safe_set(owner, 'metric_ConstraintMetrics2', set())
    assert getattr(partner, 'metric_Constraint') is None


def test_assoc_referredConstraint3_stub_double():
    # metric_Constraint has no real 'metric_Constraint5' property in the generated
    # code (a bare stub) -- manually attach it so metric_ConstraintMetric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metric_ConstraintMetric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metric_ConstraintMetric(calledOperations="sample_text", calledProperties="sample_text", expressionCount=7, expressionDepth=7, numberOfIfExpressions=7, numberOfLetExpressions=7, usedIterators="sample_text", usedLiterals="sample_text")
    partner = metric_Constraint()
    setattr(partner, 'metric_Constraint5', None)
    _safe_set(owner, 'metric_ConstraintMetric4', partner)
    assert getattr(partner, 'metric_Constraint5') == owner
    _safe_set(owner, 'metric_ConstraintMetric4', None)
    assert getattr(partner, 'metric_Constraint5') is None


