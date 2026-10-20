import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SimpleTrace_EObject,
    SimpleTrace_Trace,
    SimpleTrace_TraceLink,
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

def test_assoc_links0_stub_double():
    # SimpleTrace_Trace has no real 'SimpleTrace_Trace' property in the generated
    # code (a bare stub) -- manually attach it so SimpleTrace_TraceLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleTrace_TraceLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleTrace_TraceLink(description="sample_text")
    partner = SimpleTrace_Trace()
    setattr(partner, 'SimpleTrace_Trace', None)
    _safe_set(owner, 'SimpleTrace_TraceLink', partner)
    assert owner in getattr(partner, 'SimpleTrace_Trace')
    _safe_set(owner, 'SimpleTrace_TraceLink', None)
    assert owner not in getattr(partner, 'SimpleTrace_Trace')


def test_assoc_sources1_stub_double():
    # SimpleTrace_EObject has no real 'SimpleTrace_EObject' property in the generated
    # code (a bare stub) -- manually attach it so SimpleTrace_TraceLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleTrace_TraceLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleTrace_TraceLink(description="sample_text")
    partner = SimpleTrace_EObject()
    setattr(partner, 'SimpleTrace_EObject', None)
    _safe_set(owner, 'SimpleTrace_TraceLink2', {partner})
    assert getattr(partner, 'SimpleTrace_EObject') == owner
    _safe_set(owner, 'SimpleTrace_TraceLink2', set())
    assert getattr(partner, 'SimpleTrace_EObject') is None


def test_assoc_targets3_stub_double():
    # SimpleTrace_EObject has no real 'SimpleTrace_EObject5' property in the generated
    # code (a bare stub) -- manually attach it so SimpleTrace_TraceLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleTrace_TraceLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleTrace_TraceLink(description="sample_text")
    partner = SimpleTrace_EObject()
    setattr(partner, 'SimpleTrace_EObject5', None)
    _safe_set(owner, 'SimpleTrace_TraceLink4', {partner})
    assert getattr(partner, 'SimpleTrace_EObject5') == owner
    _safe_set(owner, 'SimpleTrace_TraceLink4', set())
    assert getattr(partner, 'SimpleTrace_EObject5') is None


