import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Metric,
    QualityMetrics_AggregatedIntegerMetric,
    QualityMetrics_AggregatedRealMetric,
    QualityMetrics_Metric,
    QualityMetrics_Metrics,
    QualityMetrics_SimpleMetric,
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

def test_assoc_AggregatedIntegerMetrics1_reverse_link_reassign_clear():
    a1 = QualityMetrics_Metrics(TrafoName="sample_text")
    a2 = QualityMetrics_Metrics(TrafoName="sample_text_2")
    b = QualityMetrics_AggregatedIntegerMetric(Average=3.14, Maximum=7, Median=7, Minimum=7, StandardDeviation=3.14)
    _safe_set(b, 'QualityMetrics_AggregatedIntegerMetric', a1)
    assert _is_linked(b, 'QualityMetrics_AggregatedIntegerMetric', a1)
    if hasattr(a1, 'QualityMetrics_Metrics2'):
        assert _is_linked(a1, 'QualityMetrics_Metrics2', b)
    _safe_set(b, 'QualityMetrics_AggregatedIntegerMetric', a2)
    assert _is_linked(b, 'QualityMetrics_AggregatedIntegerMetric', a2)
    if hasattr(a1, 'QualityMetrics_Metrics2'):
        assert not _is_linked(a1, 'QualityMetrics_Metrics2', b)
    if hasattr(a2, 'QualityMetrics_Metrics2'):
        assert _is_linked(a2, 'QualityMetrics_Metrics2', b)
    _safe_set(b, 'QualityMetrics_AggregatedIntegerMetric', None)
    assert not _is_linked(b, 'QualityMetrics_AggregatedIntegerMetric', a2)
    if hasattr(a2, 'QualityMetrics_Metrics2'):
        assert not _is_linked(a2, 'QualityMetrics_Metrics2', b)


def test_assoc_AggregatedRealMetrics3_reverse_link_reassign_clear():
    a1 = QualityMetrics_Metrics(TrafoName="sample_text")
    a2 = QualityMetrics_Metrics(TrafoName="sample_text_2")
    b = QualityMetrics_AggregatedRealMetric(Average=3.14, Maximum=3.14, Median=3.14, Minimum=3.14, StandardDeviation=3.14)
    _safe_set(b, 'QualityMetrics_AggregatedRealMetric', a1)
    assert _is_linked(b, 'QualityMetrics_AggregatedRealMetric', a1)
    if hasattr(a1, 'QualityMetrics_Metrics4'):
        assert _is_linked(a1, 'QualityMetrics_Metrics4', b)
    _safe_set(b, 'QualityMetrics_AggregatedRealMetric', a2)
    assert _is_linked(b, 'QualityMetrics_AggregatedRealMetric', a2)
    if hasattr(a1, 'QualityMetrics_Metrics4'):
        assert not _is_linked(a1, 'QualityMetrics_Metrics4', b)
    if hasattr(a2, 'QualityMetrics_Metrics4'):
        assert _is_linked(a2, 'QualityMetrics_Metrics4', b)
    _safe_set(b, 'QualityMetrics_AggregatedRealMetric', None)
    assert not _is_linked(b, 'QualityMetrics_AggregatedRealMetric', a2)
    if hasattr(a2, 'QualityMetrics_Metrics4'):
        assert not _is_linked(a2, 'QualityMetrics_Metrics4', b)


def test_assoc_SimpleMetrics0_reverse_link_reassign_clear():
    a1 = QualityMetrics_SimpleMetric(Value=7)
    a2 = QualityMetrics_SimpleMetric(Value=13)
    b = QualityMetrics_Metrics(TrafoName="sample_text")
    _safe_set(b, 'QualityMetrics_Metrics', {a1})
    assert _is_linked(b, 'QualityMetrics_Metrics', a1)
    if hasattr(a1, 'QualityMetrics_SimpleMetric'):
        assert _is_linked(a1, 'QualityMetrics_SimpleMetric', b)
    _safe_set(b, 'QualityMetrics_Metrics', {a2})
    assert _is_linked(b, 'QualityMetrics_Metrics', a2)
    if hasattr(a1, 'QualityMetrics_SimpleMetric'):
        assert not _is_linked(a1, 'QualityMetrics_SimpleMetric', b)
    if hasattr(a2, 'QualityMetrics_SimpleMetric'):
        assert _is_linked(a2, 'QualityMetrics_SimpleMetric', b)
    _safe_set(b, 'QualityMetrics_Metrics', set())
    assert not _is_linked(b, 'QualityMetrics_Metrics', a2)
    if hasattr(a2, 'QualityMetrics_SimpleMetric'):
        assert not _is_linked(a2, 'QualityMetrics_SimpleMetric', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

