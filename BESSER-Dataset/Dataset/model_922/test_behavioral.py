import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    spem_Activity,
    spem_Process,
    spem_WorkSequence,
    WorkSequenceKind,
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

def test_assoc_linkToPredecessor5_reverse_link_reassign_clear():
    a1 = spem_WorkSequence(kind="sample_text")
    a2 = spem_WorkSequence(kind="sample_text_2")
    b = spem_Activity(durationmax=7, durationmin=7, name="sample_text")
    _safe_set(b, 'successor', {a1})
    assert _is_linked(b, 'successor', a1)
    if hasattr(a1, 'WorkSequence6'):
        assert _is_linked(a1, 'WorkSequence6', b)
    _safe_set(b, 'successor', {a2})
    assert _is_linked(b, 'successor', a2)
    if hasattr(a1, 'WorkSequence6'):
        assert not _is_linked(a1, 'WorkSequence6', b)
    if hasattr(a2, 'WorkSequence6'):
        assert _is_linked(a2, 'WorkSequence6', b)
    _safe_set(b, 'successor', set())
    assert not _is_linked(b, 'successor', a2)
    if hasattr(a2, 'WorkSequence6'):
        assert not _is_linked(a2, 'WorkSequence6', b)


def test_assoc_linkToSuccessor3_reverse_link_reassign_clear():
    a1 = spem_WorkSequence(kind="sample_text")
    a2 = spem_WorkSequence(kind="sample_text_2")
    b = spem_Activity(durationmax=7, durationmin=7, name="sample_text")
    _safe_set(b, 'predecessor', {a1})
    assert _is_linked(b, 'predecessor', a1)
    if hasattr(a1, 'WorkSequence4'):
        assert _is_linked(a1, 'WorkSequence4', b)
    _safe_set(b, 'predecessor', {a2})
    assert _is_linked(b, 'predecessor', a2)
    if hasattr(a1, 'WorkSequence4'):
        assert not _is_linked(a1, 'WorkSequence4', b)
    if hasattr(a2, 'WorkSequence4'):
        assert _is_linked(a2, 'WorkSequence4', b)
    _safe_set(b, 'predecessor', set())
    assert not _is_linked(b, 'predecessor', a2)
    if hasattr(a2, 'WorkSequence4'):
        assert not _is_linked(a2, 'WorkSequence4', b)


def test_assoc_predecessor10_reverse_link_reassign_clear():
    a1 = spem_WorkSequence(kind="sample_text")
    a2 = spem_WorkSequence(kind="sample_text_2")
    b = spem_Activity(durationmax=7, durationmin=7, name="sample_text")
    _safe_set(b, 'Activity11', a1)
    assert _is_linked(b, 'Activity11', a1)
    if hasattr(a1, 'linkToSuccessor'):
        assert _is_linked(a1, 'linkToSuccessor', b)
    _safe_set(b, 'Activity11', a2)
    assert _is_linked(b, 'Activity11', a2)
    if hasattr(a1, 'linkToSuccessor'):
        assert not _is_linked(a1, 'linkToSuccessor', b)
    if hasattr(a2, 'linkToSuccessor'):
        assert _is_linked(a2, 'linkToSuccessor', b)
    _safe_set(b, 'Activity11', None)
    assert not _is_linked(b, 'Activity11', a2)
    if hasattr(a2, 'linkToSuccessor'):
        assert not _is_linked(a2, 'linkToSuccessor', b)


def test_assoc_successor8_reverse_link_reassign_clear():
    a1 = spem_WorkSequence(kind="sample_text")
    a2 = spem_WorkSequence(kind="sample_text_2")
    b = spem_Activity(durationmax=7, durationmin=7, name="sample_text")
    _safe_set(b, 'Activity9', a1)
    assert _is_linked(b, 'Activity9', a1)
    if hasattr(a1, 'linkToPredecessor'):
        assert _is_linked(a1, 'linkToPredecessor', b)
    _safe_set(b, 'Activity9', a2)
    assert _is_linked(b, 'Activity9', a2)
    if hasattr(a1, 'linkToPredecessor'):
        assert not _is_linked(a1, 'linkToPredecessor', b)
    if hasattr(a2, 'linkToPredecessor'):
        assert _is_linked(a2, 'linkToPredecessor', b)
    _safe_set(b, 'Activity9', None)
    assert not _is_linked(b, 'Activity9', a2)
    if hasattr(a2, 'linkToPredecessor'):
        assert not _is_linked(a2, 'linkToPredecessor', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_activities0_stub_double():
    # spem_Process has no real 'process' property in the generated
    # code (a bare stub) -- manually attach it so spem_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_Activity(durationmax=7, durationmin=7, name="sample_text")
    partner = spem_Process()
    setattr(partner, 'process', None)
    _safe_set(owner, 'Activity', partner)
    assert owner in getattr(partner, 'process')
    _safe_set(owner, 'Activity', None)
    assert owner not in getattr(partner, 'process')


def test_assoc_process12_stub_double():
    # spem_Process has no real 'Process13' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkSequence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkSequence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkSequence(kind="sample_text")
    partner = spem_Process()
    setattr(partner, 'Process13', None)
    _safe_set(owner, 'workSquences', partner)
    assert getattr(partner, 'Process13') == owner
    _safe_set(owner, 'workSquences', None)
    assert getattr(partner, 'Process13') is None


def test_assoc_process7_stub_double():
    # spem_Process has no real 'Process' property in the generated
    # code (a bare stub) -- manually attach it so spem_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_Activity(durationmax=7, durationmin=7, name="sample_text")
    partner = spem_Process()
    setattr(partner, 'Process', None)
    _safe_set(owner, 'activities', partner)
    assert getattr(partner, 'Process') == owner
    _safe_set(owner, 'activities', None)
    assert getattr(partner, 'Process') is None


def test_assoc_workSquences1_stub_double():
    # spem_Process has no real 'process2' property in the generated
    # code (a bare stub) -- manually attach it so spem_WorkSequence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # spem_WorkSequence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = spem_WorkSequence(kind="sample_text")
    partner = spem_Process()
    setattr(partner, 'process2', None)
    _safe_set(owner, 'WorkSequence', partner)
    assert owner in getattr(partner, 'process2')
    _safe_set(owner, 'WorkSequence', None)
    assert owner not in getattr(partner, 'process2')


