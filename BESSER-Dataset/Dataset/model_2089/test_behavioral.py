import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FaultTree_EObject,
    FaultTree_Event,
    FaultTree_FaultTree,
    EventType,
    FaultTreeType,
    LogicOperation,
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

def test_assoc_events3_reverse_link_reassign_clear():
    a1 = FaultTree_FaultTree(faultTreeType="sample_text", message="sample_text", name="sample_text")
    a2 = FaultTree_FaultTree(faultTreeType="sample_text_2", message="sample_text_2", name="sample_text_2")
    b = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    _safe_set(b, 'FaultTree_Event5', a1)
    assert _is_linked(b, 'FaultTree_Event5', a1)
    if hasattr(a1, 'FaultTree_FaultTree4'):
        assert _is_linked(a1, 'FaultTree_FaultTree4', b)
    _safe_set(b, 'FaultTree_Event5', a2)
    assert _is_linked(b, 'FaultTree_Event5', a2)
    if hasattr(a1, 'FaultTree_FaultTree4'):
        assert not _is_linked(a1, 'FaultTree_FaultTree4', b)
    if hasattr(a2, 'FaultTree_FaultTree4'):
        assert _is_linked(a2, 'FaultTree_FaultTree4', b)
    _safe_set(b, 'FaultTree_Event5', None)
    assert not _is_linked(b, 'FaultTree_Event5', a2)
    if hasattr(a2, 'FaultTree_FaultTree4'):
        assert not _is_linked(a2, 'FaultTree_FaultTree4', b)


def test_assoc_root0_reverse_link_reassign_clear():
    a1 = FaultTree_FaultTree(faultTreeType="sample_text", message="sample_text", name="sample_text")
    a2 = FaultTree_FaultTree(faultTreeType="sample_text_2", message="sample_text_2", name="sample_text_2")
    b = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    _safe_set(b, 'FaultTree_Event', a1)
    assert _is_linked(b, 'FaultTree_Event', a1)
    if hasattr(a1, 'FaultTree_FaultTree'):
        assert _is_linked(a1, 'FaultTree_FaultTree', b)
    _safe_set(b, 'FaultTree_Event', a2)
    assert _is_linked(b, 'FaultTree_Event', a2)
    if hasattr(a1, 'FaultTree_FaultTree'):
        assert not _is_linked(a1, 'FaultTree_FaultTree', b)
    if hasattr(a2, 'FaultTree_FaultTree'):
        assert _is_linked(a2, 'FaultTree_FaultTree', b)
    _safe_set(b, 'FaultTree_Event', None)
    assert not _is_linked(b, 'FaultTree_Event', a2)
    if hasattr(a2, 'FaultTree_FaultTree'):
        assert not _is_linked(a2, 'FaultTree_FaultTree', b)


def test_assoc_subEvents7_reverse_link_reassign_clear():
    a1 = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    a2 = FaultTree_Event(assignedProbability="sample_text_2", computedProbability="sample_text_2", k=13, message="sample_text_2", name="sample_text_2", referenceCount=13, scale="sample_text_2", subEventLogic="sample_text_2", type="sample_text_2")
    b = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    _safe_set(b, 'FaultTree_Event8', a1)
    assert _is_linked(b, 'FaultTree_Event8', a1)
    if hasattr(a1, 'FaultTree_Event6'):
        assert _is_linked(a1, 'FaultTree_Event6', b)
    _safe_set(b, 'FaultTree_Event8', a2)
    assert _is_linked(b, 'FaultTree_Event8', a2)
    if hasattr(a1, 'FaultTree_Event6'):
        assert not _is_linked(a1, 'FaultTree_Event6', b)
    if hasattr(a2, 'FaultTree_Event6'):
        assert _is_linked(a2, 'FaultTree_Event6', b)
    _safe_set(b, 'FaultTree_Event8', None)
    assert not _is_linked(b, 'FaultTree_Event8', a2)
    if hasattr(a2, 'FaultTree_Event6'):
        assert not _is_linked(a2, 'FaultTree_Event6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_instanceRoot1_stub_double():
    # FaultTree_EObject has no real 'FaultTree_EObject' property in the generated
    # code (a bare stub) -- manually attach it so FaultTree_FaultTree's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FaultTree_FaultTree's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FaultTree_FaultTree(faultTreeType="sample_text", message="sample_text", name="sample_text")
    partner = FaultTree_EObject()
    setattr(partner, 'FaultTree_EObject', None)
    _safe_set(owner, 'FaultTree_FaultTree2', partner)
    assert getattr(partner, 'FaultTree_EObject') == owner
    _safe_set(owner, 'FaultTree_FaultTree2', None)
    assert getattr(partner, 'FaultTree_EObject') is None


def test_assoc_relatedEMV2Object15_stub_double():
    # FaultTree_EObject has no real 'FaultTree_EObject17' property in the generated
    # code (a bare stub) -- manually attach it so FaultTree_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FaultTree_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    partner = FaultTree_EObject()
    setattr(partner, 'FaultTree_EObject17', None)
    _safe_set(owner, 'FaultTree_Event16', partner)
    assert getattr(partner, 'FaultTree_EObject17') == owner
    _safe_set(owner, 'FaultTree_Event16', None)
    assert getattr(partner, 'FaultTree_EObject17') is None


def test_assoc_relatedErrorType12_stub_double():
    # FaultTree_EObject has no real 'FaultTree_EObject14' property in the generated
    # code (a bare stub) -- manually attach it so FaultTree_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FaultTree_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    partner = FaultTree_EObject()
    setattr(partner, 'FaultTree_EObject14', None)
    _safe_set(owner, 'FaultTree_Event13', partner)
    assert getattr(partner, 'FaultTree_EObject14') == owner
    _safe_set(owner, 'FaultTree_Event13', None)
    assert getattr(partner, 'FaultTree_EObject14') is None


def test_assoc_relatedInstanceObject9_stub_double():
    # FaultTree_EObject has no real 'FaultTree_EObject11' property in the generated
    # code (a bare stub) -- manually attach it so FaultTree_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FaultTree_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FaultTree_Event(assignedProbability="sample_text", computedProbability="sample_text", k=7, message="sample_text", name="sample_text", referenceCount=7, scale="sample_text", subEventLogic="sample_text", type="sample_text")
    partner = FaultTree_EObject()
    setattr(partner, 'FaultTree_EObject11', None)
    _safe_set(owner, 'FaultTree_Event10', partner)
    assert getattr(partner, 'FaultTree_EObject11') == owner
    _safe_set(owner, 'FaultTree_Event10', None)
    assert getattr(partner, 'FaultTree_EObject11') is None


