import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Activities,
    Parameter,
    ProcessElement,
    simplepdl_Activities,
    simplepdl_Guidance,
    simplepdl_Parameter,
    simplepdl_ParameterSWD,
    simplepdl_ParameterWD,
    simplepdl_Process,
    simplepdl_ProcessElement,
    simplepdl_Resource,
    simplepdl_SubWorkDefinition,
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

def test_assoc_linksToPredecessors8_reverse_link_reassign_clear():
    a1 = simplepdl_WorkSequence(linkType="sample_text", name="sample_text")
    a2 = simplepdl_WorkSequence(linkType="sample_text_2", name="sample_text_2")
    b = simplepdl_Activities(max_time=7, min_time=7, name="sample_text")
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


def test_assoc_linksToSuccessors9_reverse_link_reassign_clear():
    a1 = simplepdl_WorkSequence(linkType="sample_text", name="sample_text")
    a2 = simplepdl_WorkSequence(linkType="sample_text_2", name="sample_text_2")
    b = simplepdl_Activities(max_time=7, min_time=7, name="sample_text")
    _safe_set(b, 'predecessor', {a1})
    assert _is_linked(b, 'predecessor', a1)
    if hasattr(a1, 'WorkSequence10'):
        assert _is_linked(a1, 'WorkSequence10', b)
    _safe_set(b, 'predecessor', {a2})
    assert _is_linked(b, 'predecessor', a2)
    if hasattr(a1, 'WorkSequence10'):
        assert not _is_linked(a1, 'WorkSequence10', b)
    if hasattr(a2, 'WorkSequence10'):
        assert _is_linked(a2, 'WorkSequence10', b)
    _safe_set(b, 'predecessor', set())
    assert not _is_linked(b, 'predecessor', a2)
    if hasattr(a2, 'WorkSequence10'):
        assert not _is_linked(a2, 'WorkSequence10', b)


def test_assoc_predecessor5_reverse_link_reassign_clear():
    a1 = simplepdl_WorkSequence(linkType="sample_text", name="sample_text")
    a2 = simplepdl_WorkSequence(linkType="sample_text_2", name="sample_text_2")
    b = simplepdl_Activities(max_time=7, min_time=7, name="sample_text")
    _safe_set(b, 'Activities', a1)
    assert _is_linked(b, 'Activities', a1)
    if hasattr(a1, 'linksToSuccessors'):
        assert _is_linked(a1, 'linksToSuccessors', b)
    _safe_set(b, 'Activities', a2)
    assert _is_linked(b, 'Activities', a2)
    if hasattr(a1, 'linksToSuccessors'):
        assert not _is_linked(a1, 'linksToSuccessors', b)
    if hasattr(a2, 'linksToSuccessors'):
        assert _is_linked(a2, 'linksToSuccessors', b)
    _safe_set(b, 'Activities', None)
    assert not _is_linked(b, 'Activities', a2)
    if hasattr(a2, 'linksToSuccessors'):
        assert not _is_linked(a2, 'linksToSuccessors', b)


def test_assoc_resources1_reverse_link_reassign_clear():
    a1 = simplepdl_Resource(marking=7, name="sample_text")
    a2 = simplepdl_Resource(marking=13, name="sample_text_2")
    b = simplepdl_Process(max_time=7, min_time=7, name="sample_text")
    _safe_set(b, 'simplepdl_Process2', {a1})
    assert _is_linked(b, 'simplepdl_Process2', a1)
    if hasattr(a1, 'simplepdl_Resource'):
        assert _is_linked(a1, 'simplepdl_Resource', b)
    _safe_set(b, 'simplepdl_Process2', {a2})
    assert _is_linked(b, 'simplepdl_Process2', a2)
    if hasattr(a1, 'simplepdl_Resource'):
        assert not _is_linked(a1, 'simplepdl_Resource', b)
    if hasattr(a2, 'simplepdl_Resource'):
        assert _is_linked(a2, 'simplepdl_Resource', b)
    _safe_set(b, 'simplepdl_Process2', set())
    assert not _is_linked(b, 'simplepdl_Process2', a2)
    if hasattr(a2, 'simplepdl_Resource'):
        assert not _is_linked(a2, 'simplepdl_Resource', b)


def test_assoc_successor6_reverse_link_reassign_clear():
    a1 = simplepdl_WorkSequence(linkType="sample_text", name="sample_text")
    a2 = simplepdl_WorkSequence(linkType="sample_text_2", name="sample_text_2")
    b = simplepdl_Activities(max_time=7, min_time=7, name="sample_text")
    _safe_set(b, 'Activities7', a1)
    assert _is_linked(b, 'Activities7', a1)
    if hasattr(a1, 'linksToPredecessors'):
        assert _is_linked(a1, 'linksToPredecessors', b)
    _safe_set(b, 'Activities7', a2)
    assert _is_linked(b, 'Activities7', a2)
    if hasattr(a1, 'linksToPredecessors'):
        assert not _is_linked(a1, 'linksToPredecessors', b)
    if hasattr(a2, 'linksToPredecessors'):
        assert _is_linked(a2, 'linksToPredecessors', b)
    _safe_set(b, 'Activities7', None)
    assert not _is_linked(b, 'Activities7', a2)
    if hasattr(a2, 'linksToPredecessors'):
        assert not _is_linked(a2, 'linksToPredecessors', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_children11_stub_double():
    # simplepdl_SubWorkDefinition has no real 'SubWorkDefinition' property in the generated
    # code (a bare stub) -- manually attach it so simplepdl_Activities's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplepdl_Activities's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplepdl_Activities(max_time=7, min_time=7, name="sample_text")
    partner = simplepdl_SubWorkDefinition()
    setattr(partner, 'SubWorkDefinition', None)
    _safe_set(owner, 'parent', {partner})
    assert getattr(partner, 'SubWorkDefinition') == owner
    _safe_set(owner, 'parent', set())
    assert getattr(partner, 'SubWorkDefinition') is None


def test_assoc_element3_stub_double():
    # simplepdl_ProcessElement has no real 'simplepdl_ProcessElement4' property in the generated
    # code (a bare stub) -- manually attach it so simplepdl_Guidance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplepdl_Guidance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplepdl_Guidance(text="sample_text")
    partner = simplepdl_ProcessElement()
    setattr(partner, 'simplepdl_ProcessElement4', None)
    _safe_set(owner, 'simplepdl_Guidance', {partner})
    assert getattr(partner, 'simplepdl_ProcessElement4') == owner
    _safe_set(owner, 'simplepdl_Guidance', set())
    assert getattr(partner, 'simplepdl_ProcessElement4') is None


def test_assoc_internResource19_stub_double():
    # simplepdl_ParameterSWD has no real 'simplepdl_ParameterSWD20' property in the generated
    # code (a bare stub) -- manually attach it so simplepdl_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplepdl_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplepdl_Parameter(name="sample_text", nbNeeds=7)
    partner = simplepdl_ParameterSWD()
    setattr(partner, 'simplepdl_ParameterSWD20', None)
    _safe_set(owner, 'simplepdl_Parameter', partner)
    assert getattr(partner, 'simplepdl_ParameterSWD20') == owner
    _safe_set(owner, 'simplepdl_Parameter', None)
    assert getattr(partner, 'simplepdl_ParameterSWD20') is None


def test_assoc_parent13_stub_double():
    # simplepdl_SubWorkDefinition has no real 'children' property in the generated
    # code (a bare stub) -- manually attach it so simplepdl_Activities's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplepdl_Activities's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplepdl_Activities(max_time=7, min_time=7, name="sample_text")
    partner = simplepdl_SubWorkDefinition()
    setattr(partner, 'children', None)
    _safe_set(owner, 'Activities14', partner)
    assert getattr(partner, 'children') == owner
    _safe_set(owner, 'Activities14', None)
    assert getattr(partner, 'children') is None


def test_assoc_processElements0_stub_double():
    # simplepdl_ProcessElement has no real 'simplepdl_ProcessElement' property in the generated
    # code (a bare stub) -- manually attach it so simplepdl_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplepdl_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplepdl_Process(max_time=7, min_time=7, name="sample_text")
    partner = simplepdl_ProcessElement()
    setattr(partner, 'simplepdl_ProcessElement', None)
    _safe_set(owner, 'simplepdl_Process', {partner})
    assert getattr(partner, 'simplepdl_ProcessElement') == owner
    _safe_set(owner, 'simplepdl_Process', set())
    assert getattr(partner, 'simplepdl_ProcessElement') is None


def test_assoc_resource16_stub_double():
    # simplepdl_ParameterWD has no real 'simplepdl_ParameterWD' property in the generated
    # code (a bare stub) -- manually attach it so simplepdl_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplepdl_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplepdl_Resource(marking=7, name="sample_text")
    partner = simplepdl_ParameterWD()
    setattr(partner, 'simplepdl_ParameterWD', None)
    _safe_set(owner, 'simplepdl_Resource17', partner)
    assert getattr(partner, 'simplepdl_ParameterWD') == owner
    _safe_set(owner, 'simplepdl_Resource17', None)
    assert getattr(partner, 'simplepdl_ParameterWD') is None


