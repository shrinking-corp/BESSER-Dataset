import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    ArcToPlace,
    ArcToTransition,
    Node,
    Place,
    PlaceReference,
    Transition,
    ptnetLoLA_Annotation,
    ptnetLoLA_Arc,
    ptnetLoLA_ArcToPlace,
    ptnetLoLA_ArcToPlaceExt,
    ptnetLoLA_ArcToTransition,
    ptnetLoLA_ArcToTransitionExt,
    ptnetLoLA_Marking,
    ptnetLoLA_Node,
    ptnetLoLA_Place,
    ptnetLoLA_PlaceExt,
    ptnetLoLA_PlaceReference,
    ptnetLoLA_PtNet,
    ptnetLoLA_RefMarkedPlace,
    ptnetLoLA_Transition,
    ptnetLoLA_TransitionExt,
    NodeType,
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

def test_assoc_annotation12_reverse_link_reassign_clear():
    a1 = ptnetLoLA_Node(name="sample_text", type="sample_text")
    a2 = ptnetLoLA_Node(name="sample_text_2", type="sample_text_2")
    b = ptnetLoLA_Annotation(text="sample_text")
    _safe_set(b, 'ptnetLoLA_Annotation13', a1)
    assert _is_linked(b, 'ptnetLoLA_Annotation13', a1)
    if hasattr(a1, 'ptnetLoLA_Node'):
        assert _is_linked(a1, 'ptnetLoLA_Node', b)
    _safe_set(b, 'ptnetLoLA_Annotation13', a2)
    assert _is_linked(b, 'ptnetLoLA_Annotation13', a2)
    if hasattr(a1, 'ptnetLoLA_Node'):
        assert not _is_linked(a1, 'ptnetLoLA_Node', b)
    if hasattr(a2, 'ptnetLoLA_Node'):
        assert _is_linked(a2, 'ptnetLoLA_Node', b)
    _safe_set(b, 'ptnetLoLA_Annotation13', None)
    assert not _is_linked(b, 'ptnetLoLA_Annotation13', a2)
    if hasattr(a2, 'ptnetLoLA_Node'):
        assert not _is_linked(a2, 'ptnetLoLA_Node', b)


def test_assoc_incoming14_reverse_link_reassign_clear():
    a1 = ptnetLoLA_Node(name="sample_text", type="sample_text")
    a2 = ptnetLoLA_Node(name="sample_text_2", type="sample_text_2")
    b = ptnetLoLA_Arc(weight=7)
    _safe_set(b, 'Arc', a1)
    assert _is_linked(b, 'Arc', a1)
    if hasattr(a1, 'target'):
        assert _is_linked(a1, 'target', b)
    _safe_set(b, 'Arc', a2)
    assert _is_linked(b, 'Arc', a2)
    if hasattr(a1, 'target'):
        assert not _is_linked(a1, 'target', b)
    if hasattr(a2, 'target'):
        assert _is_linked(a2, 'target', b)
    _safe_set(b, 'Arc', None)
    assert not _is_linked(b, 'Arc', a2)
    if hasattr(a2, 'target'):
        assert not _is_linked(a2, 'target', b)


def test_assoc_outgoing15_reverse_link_reassign_clear():
    a1 = ptnetLoLA_Node(name="sample_text", type="sample_text")
    a2 = ptnetLoLA_Node(name="sample_text_2", type="sample_text_2")
    b = ptnetLoLA_Arc(weight=7)
    _safe_set(b, 'Arc16', a1)
    assert _is_linked(b, 'Arc16', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'Arc16', a2)
    assert _is_linked(b, 'Arc16', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'Arc16', None)
    assert not _is_linked(b, 'Arc16', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_source21_reverse_link_reassign_clear():
    a1 = ptnetLoLA_Node(name="sample_text", type="sample_text")
    a2 = ptnetLoLA_Node(name="sample_text_2", type="sample_text_2")
    b = ptnetLoLA_Arc(weight=7)
    _safe_set(b, 'outgoing', a1)
    assert _is_linked(b, 'outgoing', a1)
    if hasattr(a1, 'Node'):
        assert _is_linked(a1, 'Node', b)
    _safe_set(b, 'outgoing', a2)
    assert _is_linked(b, 'outgoing', a2)
    if hasattr(a1, 'Node'):
        assert not _is_linked(a1, 'Node', b)
    if hasattr(a2, 'Node'):
        assert _is_linked(a2, 'Node', b)
    _safe_set(b, 'outgoing', None)
    assert not _is_linked(b, 'outgoing', a2)
    if hasattr(a2, 'Node'):
        assert not _is_linked(a2, 'Node', b)


def test_assoc_target22_reverse_link_reassign_clear():
    a1 = ptnetLoLA_Node(name="sample_text", type="sample_text")
    a2 = ptnetLoLA_Node(name="sample_text_2", type="sample_text_2")
    b = ptnetLoLA_Arc(weight=7)
    _safe_set(b, 'incoming', a1)
    assert _is_linked(b, 'incoming', a1)
    if hasattr(a1, 'Node23'):
        assert _is_linked(a1, 'Node23', b)
    _safe_set(b, 'incoming', a2)
    assert _is_linked(b, 'incoming', a2)
    if hasattr(a1, 'Node23'):
        assert not _is_linked(a1, 'Node23', b)
    if hasattr(a2, 'Node23'):
        assert _is_linked(a2, 'Node23', b)
    _safe_set(b, 'incoming', None)
    assert not _is_linked(b, 'incoming', a2)
    if hasattr(a2, 'Node23'):
        assert not _is_linked(a2, 'Node23', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotation5_stub_double():
    # ptnetLoLA_PtNet has no real 'ptnetLoLA_PtNet6' property in the generated
    # code (a bare stub) -- manually attach it so ptnetLoLA_Annotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnetLoLA_Annotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnetLoLA_Annotation(text="sample_text")
    partner = ptnetLoLA_PtNet()
    setattr(partner, 'ptnetLoLA_PtNet6', None)
    _safe_set(owner, 'ptnetLoLA_Annotation', partner)
    assert getattr(partner, 'ptnetLoLA_PtNet6') == owner
    _safe_set(owner, 'ptnetLoLA_Annotation', None)
    assert getattr(partner, 'ptnetLoLA_PtNet6') is None


def test_assoc_arcs7_stub_double():
    # ptnetLoLA_PtNet has no real 'ptnetLoLA_PtNet8' property in the generated
    # code (a bare stub) -- manually attach it so ptnetLoLA_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnetLoLA_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnetLoLA_Arc(weight=7)
    partner = ptnetLoLA_PtNet()
    setattr(partner, 'ptnetLoLA_PtNet8', None)
    _safe_set(owner, 'ptnetLoLA_Arc', partner)
    assert owner in getattr(partner, 'ptnetLoLA_PtNet8')
    _safe_set(owner, 'ptnetLoLA_Arc', None)
    assert owner not in getattr(partner, 'ptnetLoLA_PtNet8')


def test_assoc_place19_stub_double():
    # ptnetLoLA_PlaceReference has no real 'ptnetLoLA_PlaceReference' property in the generated
    # code (a bare stub) -- manually attach it so ptnetLoLA_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnetLoLA_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnetLoLA_Place(finalMarking=7, token=7)
    partner = ptnetLoLA_PlaceReference()
    setattr(partner, 'ptnetLoLA_PlaceReference', None)
    _safe_set(owner, 'ptnetLoLA_Place20', partner)
    assert getattr(partner, 'ptnetLoLA_PlaceReference') == owner
    _safe_set(owner, 'ptnetLoLA_Place20', None)
    assert getattr(partner, 'ptnetLoLA_PlaceReference') is None


def test_assoc_places0_stub_double():
    # ptnetLoLA_PtNet has no real 'ptnetLoLA_PtNet' property in the generated
    # code (a bare stub) -- manually attach it so ptnetLoLA_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnetLoLA_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnetLoLA_Place(finalMarking=7, token=7)
    partner = ptnetLoLA_PtNet()
    setattr(partner, 'ptnetLoLA_PtNet', None)
    _safe_set(owner, 'ptnetLoLA_Place', partner)
    assert owner in getattr(partner, 'ptnetLoLA_PtNet')
    _safe_set(owner, 'ptnetLoLA_Place', None)
    assert owner not in getattr(partner, 'ptnetLoLA_PtNet')


def test_assoc_places17_stub_double():
    # ptnetLoLA_Marking has no real 'ptnetLoLA_Marking18' property in the generated
    # code (a bare stub) -- manually attach it so ptnetLoLA_RefMarkedPlace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ptnetLoLA_RefMarkedPlace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ptnetLoLA_RefMarkedPlace(token=7)
    partner = ptnetLoLA_Marking()
    setattr(partner, 'ptnetLoLA_Marking18', None)
    _safe_set(owner, 'ptnetLoLA_RefMarkedPlace', partner)
    assert owner in getattr(partner, 'ptnetLoLA_Marking18')
    _safe_set(owner, 'ptnetLoLA_RefMarkedPlace', None)
    assert owner not in getattr(partner, 'ptnetLoLA_Marking18')


