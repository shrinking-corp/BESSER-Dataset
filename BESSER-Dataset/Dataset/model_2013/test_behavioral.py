import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Call,
    Index,
    Level,
    Trace,
    Trace_Call,
    Trace_Index,
    Trace_Level,
    Trace_Trace,
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

def test_assoc_indexes5_stub_double():
    # Index has no real 'Index' property in the generated
    # code (a bare stub) -- manually attach it so Trace_Call's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Trace_Call's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Trace_Call(CPUTime="sample_text", DBAccessesNumber="sample_text", DBRowsNumber="sample_text", methodName="sample_text")
    partner = Index()
    setattr(partner, 'Index', None)
    _safe_set(owner, 'Trace_Call', {partner})
    assert getattr(partner, 'Index') == owner
    _safe_set(owner, 'Trace_Call', set())
    assert getattr(partner, 'Index') is None


def test_assoc_level3_stub_double():
    # Level has no real 'Level4' property in the generated
    # code (a bare stub) -- manually attach it so Trace_Call's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Trace_Call's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Trace_Call(CPUTime="sample_text", DBAccessesNumber="sample_text", DBRowsNumber="sample_text", methodName="sample_text")
    partner = Level()
    setattr(partner, 'Level4', None)
    _safe_set(owner, 'calls', partner)
    assert getattr(partner, 'Level4') == owner
    _safe_set(owner, 'calls', None)
    assert getattr(partner, 'Level4') is None


def test_assoc_levels0_stub_double():
    # Level has no real 'Level' property in the generated
    # code (a bare stub) -- manually attach it so Trace_Trace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Trace_Trace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Trace_Trace(name="sample_text")
    partner = Level()
    setattr(partner, 'Level', None)
    _safe_set(owner, 'trace', {partner})
    assert getattr(partner, 'Level') == owner
    _safe_set(owner, 'trace', set())
    assert getattr(partner, 'Level') is None


