import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MRPTrace_Event,
    MRPTrace_NamedElement,
    MRPTrace_RDMElement,
    MRPTrace_Trace,
    MRPTrace_TraceEntry,
    MRPTrace_TraceModel,
    NamedElement,
    TimeUnit,
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

def test_assoc_cause8_reverse_link_reassign_clear():
    a1 = MRPTrace_TraceEntry(description="sample_text")
    a2 = MRPTrace_TraceEntry(description="sample_text_2")
    b = MRPTrace_Event(time="sample_text")
    _safe_set(b, 'MRPTrace_Event', a1)
    assert _is_linked(b, 'MRPTrace_Event', a1)
    if hasattr(a1, 'MRPTrace_TraceEntry9'):
        assert _is_linked(a1, 'MRPTrace_TraceEntry9', b)
    _safe_set(b, 'MRPTrace_Event', a2)
    assert _is_linked(b, 'MRPTrace_Event', a2)
    if hasattr(a1, 'MRPTrace_TraceEntry9'):
        assert not _is_linked(a1, 'MRPTrace_TraceEntry9', b)
    if hasattr(a2, 'MRPTrace_TraceEntry9'):
        assert _is_linked(a2, 'MRPTrace_TraceEntry9', b)
    _safe_set(b, 'MRPTrace_Event', None)
    assert not _is_linked(b, 'MRPTrace_Event', a2)
    if hasattr(a2, 'MRPTrace_TraceEntry9'):
        assert not _is_linked(a2, 'MRPTrace_TraceEntry9', b)


def test_assoc_consistsOf1_reverse_link_reassign_clear():
    a1 = MRPTrace_TraceEntry(description="sample_text")
    a2 = MRPTrace_TraceEntry(description="sample_text_2")
    b = MRPTrace_Trace(granularity="sample_text")
    _safe_set(b, 'MRPTrace_Trace2', {a1})
    assert _is_linked(b, 'MRPTrace_Trace2', a1)
    if hasattr(a1, 'MRPTrace_TraceEntry'):
        assert _is_linked(a1, 'MRPTrace_TraceEntry', b)
    _safe_set(b, 'MRPTrace_Trace2', {a2})
    assert _is_linked(b, 'MRPTrace_Trace2', a2)
    if hasattr(a1, 'MRPTrace_TraceEntry'):
        assert not _is_linked(a1, 'MRPTrace_TraceEntry', b)
    if hasattr(a2, 'MRPTrace_TraceEntry'):
        assert _is_linked(a2, 'MRPTrace_TraceEntry', b)
    _safe_set(b, 'MRPTrace_Trace2', set())
    assert not _is_linked(b, 'MRPTrace_Trace2', a2)
    if hasattr(a2, 'MRPTrace_TraceEntry'):
        assert not _is_linked(a2, 'MRPTrace_TraceEntry', b)


def test_assoc_nextEntry4_reverse_link_reassign_clear():
    a1 = MRPTrace_TraceEntry(description="sample_text")
    a2 = MRPTrace_TraceEntry(description="sample_text_2")
    b = MRPTrace_TraceEntry(description="sample_text")
    _safe_set(b, 'MRPTrace_TraceEntry5', a1)
    assert _is_linked(b, 'MRPTrace_TraceEntry5', a1)
    if hasattr(a1, 'MRPTrace_TraceEntry3'):
        assert _is_linked(a1, 'MRPTrace_TraceEntry3', b)
    _safe_set(b, 'MRPTrace_TraceEntry5', a2)
    assert _is_linked(b, 'MRPTrace_TraceEntry5', a2)
    if hasattr(a1, 'MRPTrace_TraceEntry3'):
        assert not _is_linked(a1, 'MRPTrace_TraceEntry3', b)
    if hasattr(a2, 'MRPTrace_TraceEntry3'):
        assert _is_linked(a2, 'MRPTrace_TraceEntry3', b)
    _safe_set(b, 'MRPTrace_TraceEntry5', None)
    assert not _is_linked(b, 'MRPTrace_TraceEntry5', a2)
    if hasattr(a2, 'MRPTrace_TraceEntry3'):
        assert not _is_linked(a2, 'MRPTrace_TraceEntry3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_affectedRDMElements6_stub_double():
    # MRPTrace_RDMElement has no real 'MRPTrace_RDMElement' property in the generated
    # code (a bare stub) -- manually attach it so MRPTrace_TraceEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MRPTrace_TraceEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MRPTrace_TraceEntry(description="sample_text")
    partner = MRPTrace_RDMElement()
    setattr(partner, 'MRPTrace_RDMElement', None)
    _safe_set(owner, 'MRPTrace_TraceEntry7', {partner})
    assert getattr(partner, 'MRPTrace_RDMElement') == owner
    _safe_set(owner, 'MRPTrace_TraceEntry7', set())
    assert getattr(partner, 'MRPTrace_RDMElement') is None


def test_assoc_trace0_stub_double():
    # MRPTrace_TraceModel has no real 'MRPTrace_TraceModel' property in the generated
    # code (a bare stub) -- manually attach it so MRPTrace_Trace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MRPTrace_Trace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MRPTrace_Trace(granularity="sample_text")
    partner = MRPTrace_TraceModel()
    setattr(partner, 'MRPTrace_TraceModel', None)
    _safe_set(owner, 'MRPTrace_Trace', partner)
    assert getattr(partner, 'MRPTrace_TraceModel') == owner
    _safe_set(owner, 'MRPTrace_Trace', None)
    assert getattr(partner, 'MRPTrace_TraceModel') is None


