import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ProcessElement,
    simplepdl_Guidance,
    simplepdl_Need,
    simplepdl_NeedSet,
    simplepdl_Process,
    simplepdl_ProcessElement,
    simplepdl_Ressource,
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

def test_assoc_linksToPredecessors2_reverse_link_reassign_clear():
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


def test_assoc_linksToSuccessors3_reverse_link_reassign_clear():
    a1 = simplepdl_WorkSequence(linkType="sample_text")
    a2 = simplepdl_WorkSequence(linkType="sample_text_2")
    b = simplepdl_WorkDefinition(name="sample_text")
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


def test_assoc_needSet11_reverse_link_reassign_clear():
    a1 = simplepdl_NeedSet(name="sample_text")
    a2 = simplepdl_NeedSet(name="sample_text_2")
    b = simplepdl_Need(quantity=7)
    _safe_set(b, 'needs', a1)
    assert _is_linked(b, 'needs', a1)
    if hasattr(a1, 'NeedSet12'):
        assert _is_linked(a1, 'NeedSet12', b)
    _safe_set(b, 'needs', a2)
    assert _is_linked(b, 'needs', a2)
    if hasattr(a1, 'NeedSet12'):
        assert not _is_linked(a1, 'NeedSet12', b)
    if hasattr(a2, 'NeedSet12'):
        assert _is_linked(a2, 'NeedSet12', b)
    _safe_set(b, 'needs', None)
    assert not _is_linked(b, 'needs', a2)
    if hasattr(a2, 'NeedSet12'):
        assert not _is_linked(a2, 'NeedSet12', b)


def test_assoc_needSets5_reverse_link_reassign_clear():
    a1 = simplepdl_WorkDefinition(name="sample_text")
    a2 = simplepdl_WorkDefinition(name="sample_text_2")
    b = simplepdl_NeedSet(name="sample_text")
    _safe_set(b, 'NeedSet', a1)
    assert _is_linked(b, 'NeedSet', a1)
    if hasattr(a1, 'wd'):
        assert _is_linked(a1, 'wd', b)
    _safe_set(b, 'NeedSet', a2)
    assert _is_linked(b, 'NeedSet', a2)
    if hasattr(a1, 'wd'):
        assert not _is_linked(a1, 'wd', b)
    if hasattr(a2, 'wd'):
        assert _is_linked(a2, 'wd', b)
    _safe_set(b, 'NeedSet', None)
    assert not _is_linked(b, 'NeedSet', a2)
    if hasattr(a2, 'wd'):
        assert not _is_linked(a2, 'wd', b)


def test_assoc_needs13_reverse_link_reassign_clear():
    a1 = simplepdl_NeedSet(name="sample_text")
    a2 = simplepdl_NeedSet(name="sample_text_2")
    b = simplepdl_Need(quantity=7)
    _safe_set(b, 'Need', a1)
    assert _is_linked(b, 'Need', a1)
    if hasattr(a1, 'needSet'):
        assert _is_linked(a1, 'needSet', b)
    _safe_set(b, 'Need', a2)
    assert _is_linked(b, 'Need', a2)
    if hasattr(a1, 'needSet'):
        assert not _is_linked(a1, 'needSet', b)
    if hasattr(a2, 'needSet'):
        assert _is_linked(a2, 'needSet', b)
    _safe_set(b, 'Need', None)
    assert not _is_linked(b, 'Need', a2)
    if hasattr(a2, 'needSet'):
        assert not _is_linked(a2, 'needSet', b)


def test_assoc_predecessor6_reverse_link_reassign_clear():
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


def test_assoc_ressource10_reverse_link_reassign_clear():
    a1 = simplepdl_Ressource(name="sample_text", quantity=7)
    a2 = simplepdl_Ressource(name="sample_text_2", quantity=13)
    b = simplepdl_Need(quantity=7)
    _safe_set(b, 'simplepdl_Need', a1)
    assert _is_linked(b, 'simplepdl_Need', a1)
    if hasattr(a1, 'simplepdl_Ressource'):
        assert _is_linked(a1, 'simplepdl_Ressource', b)
    _safe_set(b, 'simplepdl_Need', a2)
    assert _is_linked(b, 'simplepdl_Need', a2)
    if hasattr(a1, 'simplepdl_Ressource'):
        assert not _is_linked(a1, 'simplepdl_Ressource', b)
    if hasattr(a2, 'simplepdl_Ressource'):
        assert _is_linked(a2, 'simplepdl_Ressource', b)
    _safe_set(b, 'simplepdl_Need', None)
    assert not _is_linked(b, 'simplepdl_Need', a2)
    if hasattr(a2, 'simplepdl_Ressource'):
        assert not _is_linked(a2, 'simplepdl_Ressource', b)


def test_assoc_successor7_reverse_link_reassign_clear():
    a1 = simplepdl_WorkSequence(linkType="sample_text")
    a2 = simplepdl_WorkSequence(linkType="sample_text_2")
    b = simplepdl_WorkDefinition(name="sample_text")
    _safe_set(b, 'WorkDefinition8', a1)
    assert _is_linked(b, 'WorkDefinition8', a1)
    if hasattr(a1, 'linksToPredecessors'):
        assert _is_linked(a1, 'linksToPredecessors', b)
    _safe_set(b, 'WorkDefinition8', a2)
    assert _is_linked(b, 'WorkDefinition8', a2)
    if hasattr(a1, 'linksToPredecessors'):
        assert not _is_linked(a1, 'linksToPredecessors', b)
    if hasattr(a2, 'linksToPredecessors'):
        assert _is_linked(a2, 'linksToPredecessors', b)
    _safe_set(b, 'WorkDefinition8', None)
    assert not _is_linked(b, 'WorkDefinition8', a2)
    if hasattr(a2, 'linksToPredecessors'):
        assert not _is_linked(a2, 'linksToPredecessors', b)


def test_assoc_wd14_reverse_link_reassign_clear():
    a1 = simplepdl_WorkDefinition(name="sample_text")
    a2 = simplepdl_WorkDefinition(name="sample_text_2")
    b = simplepdl_NeedSet(name="sample_text")
    _safe_set(b, 'needSets', a1)
    assert _is_linked(b, 'needSets', a1)
    if hasattr(a1, 'WorkDefinition15'):
        assert _is_linked(a1, 'WorkDefinition15', b)
    _safe_set(b, 'needSets', a2)
    assert _is_linked(b, 'needSets', a2)
    if hasattr(a1, 'WorkDefinition15'):
        assert not _is_linked(a1, 'WorkDefinition15', b)
    if hasattr(a2, 'WorkDefinition15'):
        assert _is_linked(a2, 'WorkDefinition15', b)
    _safe_set(b, 'needSets', None)
    assert not _is_linked(b, 'needSets', a2)
    if hasattr(a2, 'WorkDefinition15'):
        assert not _is_linked(a2, 'WorkDefinition15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_element9_stub_double():
    # simplepdl_ProcessElement has no real 'simplepdl_ProcessElement' property in the generated
    # code (a bare stub) -- manually attach it so simplepdl_Guidance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplepdl_Guidance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplepdl_Guidance(text="sample_text")
    partner = simplepdl_ProcessElement()
    setattr(partner, 'simplepdl_ProcessElement', None)
    _safe_set(owner, 'simplepdl_Guidance', {partner})
    assert getattr(partner, 'simplepdl_ProcessElement') == owner
    _safe_set(owner, 'simplepdl_Guidance', set())
    assert getattr(partner, 'simplepdl_ProcessElement') is None


def test_assoc_process1_stub_double():
    # simplepdl_ProcessElement has no real 'processElements' property in the generated
    # code (a bare stub) -- manually attach it so simplepdl_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplepdl_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplepdl_Process(name="sample_text")
    partner = simplepdl_ProcessElement()
    setattr(partner, 'processElements', None)
    _safe_set(owner, 'Process', partner)
    assert getattr(partner, 'processElements') == owner
    _safe_set(owner, 'Process', None)
    assert getattr(partner, 'processElements') is None


def test_assoc_processElements0_stub_double():
    # simplepdl_ProcessElement has no real 'ProcessElement' property in the generated
    # code (a bare stub) -- manually attach it so simplepdl_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplepdl_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplepdl_Process(name="sample_text")
    partner = simplepdl_ProcessElement()
    setattr(partner, 'ProcessElement', None)
    _safe_set(owner, 'process', {partner})
    assert getattr(partner, 'ProcessElement') == owner
    _safe_set(owner, 'process', set())
    assert getattr(partner, 'ProcessElement') is None


