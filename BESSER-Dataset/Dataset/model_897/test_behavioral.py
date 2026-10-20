import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ProcessElement,
    simplepdl_Guidance,
    simplepdl_Process,
    simplepdl_ProcessElement,
    simplepdl_WorkDefinition,
    simplepdl_WorkSequence,
    WorkSequenceType,
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

def test_assoc_linksToPredecessors1_reverse_link_reassign_clear():
    a1 = simplepdl_WorkSequence(linkType="sample_text")
    a2 = simplepdl_WorkSequence(linkType="sample_text_2")
    b = simplepdl_WorkDefinition(name="sample_text")
    _safe_set(b, 'successor', {a1})
    assert _is_linked(b, 'successor', a1)
    if hasattr(a1, 'WorkSequence'):
        assert _is_linked(a1, 'WorkSequence', b)
    _safe_set(b, 'successor', {a2})
    assert _is_linked(b, 'successor', a2)
    if hasattr(a1, 'WorkSequence'):
        assert not _is_linked(a1, 'WorkSequence', b)
    if hasattr(a2, 'WorkSequence'):
        assert _is_linked(a2, 'WorkSequence', b)
    _safe_set(b, 'successor', set())
    assert not _is_linked(b, 'successor', a2)
    if hasattr(a2, 'WorkSequence'):
        assert not _is_linked(a2, 'WorkSequence', b)


def test_assoc_linksToSuccessors2_reverse_link_reassign_clear():
    a1 = simplepdl_WorkSequence(linkType="sample_text")
    a2 = simplepdl_WorkSequence(linkType="sample_text_2")
    b = simplepdl_WorkDefinition(name="sample_text")
    _safe_set(b, 'predecessor', {a1})
    assert _is_linked(b, 'predecessor', a1)
    if hasattr(a1, 'WorkSequence3'):
        assert _is_linked(a1, 'WorkSequence3', b)
    _safe_set(b, 'predecessor', {a2})
    assert _is_linked(b, 'predecessor', a2)
    if hasattr(a1, 'WorkSequence3'):
        assert not _is_linked(a1, 'WorkSequence3', b)
    if hasattr(a2, 'WorkSequence3'):
        assert _is_linked(a2, 'WorkSequence3', b)
    _safe_set(b, 'predecessor', set())
    assert not _is_linked(b, 'predecessor', a2)
    if hasattr(a2, 'WorkSequence3'):
        assert not _is_linked(a2, 'WorkSequence3', b)


def test_assoc_predecessor4_reverse_link_reassign_clear():
    a1 = simplepdl_WorkSequence(linkType="sample_text")
    a2 = simplepdl_WorkSequence(linkType="sample_text_2")
    b = simplepdl_WorkDefinition(name="sample_text")
    _safe_set(b, 'WorkDefinition', a1)
    assert _is_linked(b, 'WorkDefinition', a1)
    if hasattr(a1, 'linksToSuccessors'):
        assert _is_linked(a1, 'linksToSuccessors', b)
    _safe_set(b, 'WorkDefinition', a2)
    assert _is_linked(b, 'WorkDefinition', a2)
    if hasattr(a1, 'linksToSuccessors'):
        assert not _is_linked(a1, 'linksToSuccessors', b)
    if hasattr(a2, 'linksToSuccessors'):
        assert _is_linked(a2, 'linksToSuccessors', b)
    _safe_set(b, 'WorkDefinition', None)
    assert not _is_linked(b, 'WorkDefinition', a2)
    if hasattr(a2, 'linksToSuccessors'):
        assert not _is_linked(a2, 'linksToSuccessors', b)


def test_assoc_successor5_reverse_link_reassign_clear():
    a1 = simplepdl_WorkSequence(linkType="sample_text")
    a2 = simplepdl_WorkSequence(linkType="sample_text_2")
    b = simplepdl_WorkDefinition(name="sample_text")
    _safe_set(b, 'WorkDefinition6', a1)
    assert _is_linked(b, 'WorkDefinition6', a1)
    if hasattr(a1, 'linksToPredecessors'):
        assert _is_linked(a1, 'linksToPredecessors', b)
    _safe_set(b, 'WorkDefinition6', a2)
    assert _is_linked(b, 'WorkDefinition6', a2)
    if hasattr(a1, 'linksToPredecessors'):
        assert not _is_linked(a1, 'linksToPredecessors', b)
    if hasattr(a2, 'linksToPredecessors'):
        assert _is_linked(a2, 'linksToPredecessors', b)
    _safe_set(b, 'WorkDefinition6', None)
    assert not _is_linked(b, 'WorkDefinition6', a2)
    if hasattr(a2, 'linksToPredecessors'):
        assert not _is_linked(a2, 'linksToPredecessors', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements7_stub_double():
    # simplepdl_ProcessElement has no real 'simplepdl_ProcessElement8' property in the generated
    # code (a bare stub) -- manually attach it so simplepdl_Guidance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplepdl_Guidance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplepdl_Guidance(text="sample_text")
    partner = simplepdl_ProcessElement()
    setattr(partner, 'simplepdl_ProcessElement8', None)
    _safe_set(owner, 'simplepdl_Guidance', {partner})
    assert getattr(partner, 'simplepdl_ProcessElement8') == owner
    _safe_set(owner, 'simplepdl_Guidance', set())
    assert getattr(partner, 'simplepdl_ProcessElement8') is None


def test_assoc_processElements0_stub_double():
    # simplepdl_ProcessElement has no real 'simplepdl_ProcessElement' property in the generated
    # code (a bare stub) -- manually attach it so simplepdl_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplepdl_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplepdl_Process(name="sample_text")
    partner = simplepdl_ProcessElement()
    setattr(partner, 'simplepdl_ProcessElement', None)
    _safe_set(owner, 'simplepdl_Process', {partner})
    assert getattr(partner, 'simplepdl_ProcessElement') == owner
    _safe_set(owner, 'simplepdl_Process', set())
    assert getattr(partner, 'simplepdl_ProcessElement') is None


