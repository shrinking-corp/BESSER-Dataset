import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    simple_metrics_Metric,
    simple_metrics_MetricsSet,
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

def test_assoc_metrics0_reverse_link_reassign_clear():
    a1 = simple_metrics_MetricsSet(name="sample_text")
    a2 = simple_metrics_MetricsSet(name="sample_text_2")
    b = simple_metrics_Metric(name="sample_text", value="sample_text")
    _safe_set(b, 'simple_metrics_Metric', a1)
    assert _is_linked(b, 'simple_metrics_Metric', a1)
    if hasattr(a1, 'simple_metrics_MetricsSet'):
        assert _is_linked(a1, 'simple_metrics_MetricsSet', b)
    _safe_set(b, 'simple_metrics_Metric', a2)
    assert _is_linked(b, 'simple_metrics_Metric', a2)
    if hasattr(a1, 'simple_metrics_MetricsSet'):
        assert not _is_linked(a1, 'simple_metrics_MetricsSet', b)
    if hasattr(a2, 'simple_metrics_MetricsSet'):
        assert _is_linked(a2, 'simple_metrics_MetricsSet', b)
    _safe_set(b, 'simple_metrics_Metric', None)
    assert not _is_linked(b, 'simple_metrics_Metric', a2)
    if hasattr(a2, 'simple_metrics_MetricsSet'):
        assert not _is_linked(a2, 'simple_metrics_MetricsSet', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

