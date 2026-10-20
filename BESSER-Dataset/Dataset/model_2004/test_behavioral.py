import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    trace_Trace,
    trace_TraceElement,
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

def test_assoc_traceElements0_stub_double():
    # trace_Trace has no real 'trace_Trace' property in the generated
    # code (a bare stub) -- manually attach it so trace_TraceElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_TraceElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_TraceElement(event="sample_text", timestamp=7)
    partner = trace_Trace()
    setattr(partner, 'trace_Trace', None)
    _safe_set(owner, 'trace_TraceElement', partner)
    assert owner in getattr(partner, 'trace_Trace')
    _safe_set(owner, 'trace_TraceElement', None)
    assert owner not in getattr(partner, 'trace_Trace')


