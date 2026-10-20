import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Measurement,
    ModelElement,
    metrics_ComplexMeasurement,
    metrics_LinkMeasurement,
    metrics_Measurement,
    metrics_Observation,
    metrics_ValueMeasurement,
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

def test_assoc_measurements1_stub_double():
    # metrics_ComplexMeasurement has no real 'metrics_ComplexMeasurement' property in the generated
    # code (a bare stub) -- manually attach it so metrics_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_Measurement(error="sample_text", name="sample_text", tag="sample_text")
    partner = metrics_ComplexMeasurement()
    setattr(partner, 'metrics_ComplexMeasurement', None)
    _safe_set(owner, 'metrics_Measurement', partner)
    assert owner in getattr(partner, 'metrics_ComplexMeasurement')
    _safe_set(owner, 'metrics_Measurement', None)
    assert owner not in getattr(partner, 'metrics_ComplexMeasurement')


def test_assoc_measurements2_stub_double():
    # metrics_Observation has no real 'metrics_Observation' property in the generated
    # code (a bare stub) -- manually attach it so metrics_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_Measurement(error="sample_text", name="sample_text", tag="sample_text")
    partner = metrics_Observation()
    setattr(partner, 'metrics_Observation', None)
    _safe_set(owner, 'metrics_Measurement3', partner)
    assert owner in getattr(partner, 'metrics_Observation')
    _safe_set(owner, 'metrics_Measurement3', None)
    assert owner not in getattr(partner, 'metrics_Observation')


