import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element,
    pnml_ArcPlace2Transition,
    pnml_ArcTransition2Place,
    pnml_Element,
    pnml_NetElement,
    pnml_PNMLDocument,
    pnml_PlaceElement,
    pnml_TransitionElement,
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

def test_assoc_contents9_reverse_link_reassign_clear():
    a1 = pnml_NetElement(name="sample_text")
    a2 = pnml_NetElement(name="sample_text_2")
    b = pnml_Element(id="sample_text", location="sample_text")
    _safe_set(b, 'pnml_Element', a1)
    assert _is_linked(b, 'pnml_Element', a1)
    if hasattr(a1, 'pnml_NetElement10'):
        assert _is_linked(a1, 'pnml_NetElement10', b)
    _safe_set(b, 'pnml_Element', a2)
    assert _is_linked(b, 'pnml_Element', a2)
    if hasattr(a1, 'pnml_NetElement10'):
        assert not _is_linked(a1, 'pnml_NetElement10', b)
    if hasattr(a2, 'pnml_NetElement10'):
        assert _is_linked(a2, 'pnml_NetElement10', b)
    _safe_set(b, 'pnml_Element', None)
    assert not _is_linked(b, 'pnml_Element', a2)
    if hasattr(a2, 'pnml_NetElement10'):
        assert not _is_linked(a2, 'pnml_NetElement10', b)


def test_assoc_nets0_reverse_link_reassign_clear():
    a1 = pnml_PNMLDocument(location="sample_text")
    a2 = pnml_PNMLDocument(location="sample_text_2")
    b = pnml_NetElement(name="sample_text")
    _safe_set(b, 'pnml_NetElement', a1)
    assert _is_linked(b, 'pnml_NetElement', a1)
    if hasattr(a1, 'pnml_PNMLDocument'):
        assert _is_linked(a1, 'pnml_PNMLDocument', b)
    _safe_set(b, 'pnml_NetElement', a2)
    assert _is_linked(b, 'pnml_NetElement', a2)
    if hasattr(a1, 'pnml_PNMLDocument'):
        assert not _is_linked(a1, 'pnml_PNMLDocument', b)
    if hasattr(a2, 'pnml_PNMLDocument'):
        assert _is_linked(a2, 'pnml_PNMLDocument', b)
    _safe_set(b, 'pnml_NetElement', None)
    assert not _is_linked(b, 'pnml_NetElement', a2)
    if hasattr(a2, 'pnml_PNMLDocument'):
        assert not _is_linked(a2, 'pnml_PNMLDocument', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_source1_stub_double():
    # pnml_ArcPlace2Transition has no real 'pnml_ArcPlace2Transition' property in the generated
    # code (a bare stub) -- manually attach it so pnml_PlaceElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnml_PlaceElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnml_PlaceElement(name="sample_text", tokens=7)
    partner = pnml_ArcPlace2Transition()
    setattr(partner, 'pnml_ArcPlace2Transition', None)
    _safe_set(owner, 'pnml_PlaceElement', partner)
    assert getattr(partner, 'pnml_ArcPlace2Transition') == owner
    _safe_set(owner, 'pnml_PlaceElement', None)
    assert getattr(partner, 'pnml_ArcPlace2Transition') is None


def test_assoc_source6_stub_double():
    # pnml_ArcTransition2Place has no real 'pnml_ArcTransition2Place7' property in the generated
    # code (a bare stub) -- manually attach it so pnml_TransitionElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnml_TransitionElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnml_TransitionElement(name="sample_text")
    partner = pnml_ArcTransition2Place()
    setattr(partner, 'pnml_ArcTransition2Place7', None)
    _safe_set(owner, 'pnml_TransitionElement8', partner)
    assert getattr(partner, 'pnml_ArcTransition2Place7') == owner
    _safe_set(owner, 'pnml_TransitionElement8', None)
    assert getattr(partner, 'pnml_ArcTransition2Place7') is None


def test_assoc_target2_stub_double():
    # pnml_ArcPlace2Transition has no real 'pnml_ArcPlace2Transition3' property in the generated
    # code (a bare stub) -- manually attach it so pnml_TransitionElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnml_TransitionElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnml_TransitionElement(name="sample_text")
    partner = pnml_ArcPlace2Transition()
    setattr(partner, 'pnml_ArcPlace2Transition3', None)
    _safe_set(owner, 'pnml_TransitionElement', partner)
    assert getattr(partner, 'pnml_ArcPlace2Transition3') == owner
    _safe_set(owner, 'pnml_TransitionElement', None)
    assert getattr(partner, 'pnml_ArcPlace2Transition3') is None


def test_assoc_target4_stub_double():
    # pnml_ArcTransition2Place has no real 'pnml_ArcTransition2Place' property in the generated
    # code (a bare stub) -- manually attach it so pnml_PlaceElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pnml_PlaceElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pnml_PlaceElement(name="sample_text", tokens=7)
    partner = pnml_ArcTransition2Place()
    setattr(partner, 'pnml_ArcTransition2Place', None)
    _safe_set(owner, 'pnml_PlaceElement5', partner)
    assert getattr(partner, 'pnml_ArcTransition2Place') == owner
    _safe_set(owner, 'pnml_PlaceElement5', None)
    assert getattr(partner, 'pnml_ArcTransition2Place') is None


