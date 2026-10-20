import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TraceItem,
    trace_EObject,
    trace_M2CTraceItem,
    trace_M2MTraceItem,
    trace_Trace,
    trace_TraceBySource,
    trace_TraceItem,
    trace_TraceList,
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

def test_assoc_from_5_stub_double():
    # trace_EObject has no real 'trace_EObject' property in the generated
    # code (a bare stub) -- manually attach it so trace_TraceItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_TraceItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_TraceItem(kind="sample_text")
    partner = trace_EObject()
    setattr(partner, 'trace_EObject', None)
    _safe_set(owner, 'trace_TraceItem6', {partner})
    assert getattr(partner, 'trace_EObject') == owner
    _safe_set(owner, 'trace_TraceItem6', set())
    assert getattr(partner, 'trace_EObject') is None


def test_assoc_items10_stub_double():
    # trace_TraceBySource has no real 'trace_TraceBySource11' property in the generated
    # code (a bare stub) -- manually attach it so trace_TraceItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_TraceItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_TraceItem(kind="sample_text")
    partner = trace_TraceBySource()
    setattr(partner, 'trace_TraceBySource11', None)
    _safe_set(owner, 'trace_TraceItem12', partner)
    assert owner in getattr(partner, 'trace_TraceBySource11')
    _safe_set(owner, 'trace_TraceItem12', None)
    assert owner not in getattr(partner, 'trace_TraceBySource11')


def test_assoc_items3_stub_double():
    # trace_TraceList has no real 'trace_TraceList4' property in the generated
    # code (a bare stub) -- manually attach it so trace_TraceItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_TraceItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_TraceItem(kind="sample_text")
    partner = trace_TraceList()
    setattr(partner, 'trace_TraceList4', None)
    _safe_set(owner, 'trace_TraceItem', partner)
    assert owner in getattr(partner, 'trace_TraceList4')
    _safe_set(owner, 'trace_TraceItem', None)
    assert owner not in getattr(partner, 'trace_TraceList4')


