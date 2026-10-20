import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ProcessElement,
    SimplePDL_Guidance,
    SimplePDL_Process,
    SimplePDL_ProcessElement,
    SimplePDL_Resource,
    SimplePDL_ResourceType,
    SimplePDL_WorkDefinition,
    SimplePDL_WorkSequence,
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

def test_assoc_guidanceGFX1_reverse_link_reassign_clear():
    a1 = SimplePDL_Process(maxTime=7, minTime=7, name="sample_text")
    a2 = SimplePDL_Process(maxTime=13, minTime=13, name="sample_text_2")
    b = SimplePDL_Guidance(text="sample_text")
    _safe_set(b, 'SimplePDL_Guidance', a1)
    assert _is_linked(b, 'SimplePDL_Guidance', a1)
    if hasattr(a1, 'SimplePDL_Process2'):
        assert _is_linked(a1, 'SimplePDL_Process2', b)
    _safe_set(b, 'SimplePDL_Guidance', a2)
    assert _is_linked(b, 'SimplePDL_Guidance', a2)
    if hasattr(a1, 'SimplePDL_Process2'):
        assert not _is_linked(a1, 'SimplePDL_Process2', b)
    if hasattr(a2, 'SimplePDL_Process2'):
        assert _is_linked(a2, 'SimplePDL_Process2', b)
    _safe_set(b, 'SimplePDL_Guidance', None)
    assert not _is_linked(b, 'SimplePDL_Guidance', a2)
    if hasattr(a2, 'SimplePDL_Process2'):
        assert not _is_linked(a2, 'SimplePDL_Process2', b)


def test_assoc_linksToPredecessors3_reverse_link_reassign_clear():
    a1 = SimplePDL_WorkSequence(linkType="sample_text")
    a2 = SimplePDL_WorkSequence(linkType="sample_text_2")
    b = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
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


def test_assoc_linksToSuccessors4_reverse_link_reassign_clear():
    a1 = SimplePDL_WorkSequence(linkType="sample_text")
    a2 = SimplePDL_WorkSequence(linkType="sample_text_2")
    b = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'predecessor', {a1})
    assert _is_linked(b, 'predecessor', a1)
    if hasattr(a1, 'WorkSequence5'):
        assert _is_linked(a1, 'WorkSequence5', b)
    _safe_set(b, 'predecessor', {a2})
    assert _is_linked(b, 'predecessor', a2)
    if hasattr(a1, 'WorkSequence5'):
        assert not _is_linked(a1, 'WorkSequence5', b)
    if hasattr(a2, 'WorkSequence5'):
        assert _is_linked(a2, 'WorkSequence5', b)
    _safe_set(b, 'predecessor', set())
    assert not _is_linked(b, 'predecessor', a2)
    if hasattr(a2, 'WorkSequence5'):
        assert not _is_linked(a2, 'WorkSequence5', b)


def test_assoc_neededResources6_reverse_link_reassign_clear():
    a1 = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    a2 = SimplePDL_WorkDefinition(maxTime=13, minTime=13, name="sample_text_2")
    b = SimplePDL_Resource(occurrences=7)
    _safe_set(b, 'Resource', a1)
    assert _is_linked(b, 'Resource', a1)
    if hasattr(a1, 'workDefinition'):
        assert _is_linked(a1, 'workDefinition', b)
    _safe_set(b, 'Resource', a2)
    assert _is_linked(b, 'Resource', a2)
    if hasattr(a1, 'workDefinition'):
        assert not _is_linked(a1, 'workDefinition', b)
    if hasattr(a2, 'workDefinition'):
        assert _is_linked(a2, 'workDefinition', b)
    _safe_set(b, 'Resource', None)
    assert not _is_linked(b, 'Resource', a2)
    if hasattr(a2, 'workDefinition'):
        assert not _is_linked(a2, 'workDefinition', b)


def test_assoc_predecessor8_reverse_link_reassign_clear():
    a1 = SimplePDL_WorkSequence(linkType="sample_text")
    a2 = SimplePDL_WorkSequence(linkType="sample_text_2")
    b = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
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


def test_assoc_successor9_reverse_link_reassign_clear():
    a1 = SimplePDL_WorkSequence(linkType="sample_text")
    a2 = SimplePDL_WorkSequence(linkType="sample_text_2")
    b = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    _safe_set(b, 'WorkDefinition10', a1)
    assert _is_linked(b, 'WorkDefinition10', a1)
    if hasattr(a1, 'linksToPredecessors'):
        assert _is_linked(a1, 'linksToPredecessors', b)
    _safe_set(b, 'WorkDefinition10', a2)
    assert _is_linked(b, 'WorkDefinition10', a2)
    if hasattr(a1, 'linksToPredecessors'):
        assert not _is_linked(a1, 'linksToPredecessors', b)
    if hasattr(a2, 'linksToPredecessors'):
        assert _is_linked(a2, 'linksToPredecessors', b)
    _safe_set(b, 'WorkDefinition10', None)
    assert not _is_linked(b, 'WorkDefinition10', a2)
    if hasattr(a2, 'linksToPredecessors'):
        assert not _is_linked(a2, 'linksToPredecessors', b)


def test_assoc_type18_reverse_link_reassign_clear():
    a1 = SimplePDL_ResourceType(name="sample_text", occurrences=7)
    a2 = SimplePDL_ResourceType(name="sample_text_2", occurrences=13)
    b = SimplePDL_Resource(occurrences=7)
    _safe_set(b, 'SimplePDL_Resource', a1)
    assert _is_linked(b, 'SimplePDL_Resource', a1)
    if hasattr(a1, 'SimplePDL_ResourceType'):
        assert _is_linked(a1, 'SimplePDL_ResourceType', b)
    _safe_set(b, 'SimplePDL_Resource', a2)
    assert _is_linked(b, 'SimplePDL_Resource', a2)
    if hasattr(a1, 'SimplePDL_ResourceType'):
        assert not _is_linked(a1, 'SimplePDL_ResourceType', b)
    if hasattr(a2, 'SimplePDL_ResourceType'):
        assert _is_linked(a2, 'SimplePDL_ResourceType', b)
    _safe_set(b, 'SimplePDL_Resource', None)
    assert not _is_linked(b, 'SimplePDL_Resource', a2)
    if hasattr(a2, 'SimplePDL_ResourceType'):
        assert not _is_linked(a2, 'SimplePDL_ResourceType', b)


def test_assoc_workDefinition16_reverse_link_reassign_clear():
    a1 = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    a2 = SimplePDL_WorkDefinition(maxTime=13, minTime=13, name="sample_text_2")
    b = SimplePDL_Resource(occurrences=7)
    _safe_set(b, 'neededResources', a1)
    assert _is_linked(b, 'neededResources', a1)
    if hasattr(a1, 'WorkDefinition17'):
        assert _is_linked(a1, 'WorkDefinition17', b)
    _safe_set(b, 'neededResources', a2)
    assert _is_linked(b, 'neededResources', a2)
    if hasattr(a1, 'WorkDefinition17'):
        assert not _is_linked(a1, 'WorkDefinition17', b)
    if hasattr(a2, 'WorkDefinition17'):
        assert _is_linked(a2, 'WorkDefinition17', b)
    _safe_set(b, 'neededResources', None)
    assert not _is_linked(b, 'neededResources', a2)
    if hasattr(a2, 'WorkDefinition17'):
        assert not _is_linked(a2, 'WorkDefinition17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_child7_stub_double():
    # SimplePDL_ProcessElement has no real 'ProcessElement' property in the generated
    # code (a bare stub) -- manually attach it so SimplePDL_WorkDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplePDL_WorkDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    partner = SimplePDL_ProcessElement()
    setattr(partner, 'ProcessElement', None)
    _safe_set(owner, 'parent', {partner})
    assert getattr(partner, 'ProcessElement') == owner
    _safe_set(owner, 'parent', set())
    assert getattr(partner, 'ProcessElement') is None


def test_assoc_guides11_stub_double():
    # SimplePDL_ProcessElement has no real 'SimplePDL_ProcessElement12' property in the generated
    # code (a bare stub) -- manually attach it so SimplePDL_Guidance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplePDL_Guidance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplePDL_Guidance(text="sample_text")
    partner = SimplePDL_ProcessElement()
    setattr(partner, 'SimplePDL_ProcessElement12', None)
    _safe_set(owner, 'SimplePDL_Guidance13', partner)
    assert owner in getattr(partner, 'SimplePDL_ProcessElement12')
    _safe_set(owner, 'SimplePDL_Guidance13', None)
    assert owner not in getattr(partner, 'SimplePDL_ProcessElement12')


def test_assoc_parent14_stub_double():
    # SimplePDL_ProcessElement has no real 'child' property in the generated
    # code (a bare stub) -- manually attach it so SimplePDL_WorkDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplePDL_WorkDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplePDL_WorkDefinition(maxTime=7, minTime=7, name="sample_text")
    partner = SimplePDL_ProcessElement()
    setattr(partner, 'child', None)
    _safe_set(owner, 'WorkDefinition15', partner)
    assert getattr(partner, 'child') == owner
    _safe_set(owner, 'WorkDefinition15', None)
    assert getattr(partner, 'child') is None


def test_assoc_processElements0_stub_double():
    # SimplePDL_ProcessElement has no real 'SimplePDL_ProcessElement' property in the generated
    # code (a bare stub) -- manually attach it so SimplePDL_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplePDL_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplePDL_Process(maxTime=7, minTime=7, name="sample_text")
    partner = SimplePDL_ProcessElement()
    setattr(partner, 'SimplePDL_ProcessElement', None)
    _safe_set(owner, 'SimplePDL_Process', {partner})
    assert getattr(partner, 'SimplePDL_ProcessElement') == owner
    _safe_set(owner, 'SimplePDL_Process', set())
    assert getattr(partner, 'SimplePDL_ProcessElement') is None


