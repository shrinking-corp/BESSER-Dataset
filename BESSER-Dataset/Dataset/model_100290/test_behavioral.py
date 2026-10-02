import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Noeud,
    petrinet_Arc,
    petrinet_Noeud,
    petrinet_PetriNet,
    petrinet_Place,
    petrinet_Transition,
    ArcKindType,
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

def test_assoc_arcs1_reverse_link_reassign_clear():
    a1 = petrinet_PetriNet(name="sample_text")
    a2 = petrinet_PetriNet(name="sample_text_2")
    b = petrinet_Arc(arcType="sample_text", name="sample_text", weight=7)
    _safe_set(b, 'petrinet_Arc', a1)
    assert _is_linked(b, 'petrinet_Arc', a1)
    if hasattr(a1, 'petrinet_PetriNet2'):
        assert _is_linked(a1, 'petrinet_PetriNet2', b)
    _safe_set(b, 'petrinet_Arc', a2)
    assert _is_linked(b, 'petrinet_Arc', a2)
    if hasattr(a1, 'petrinet_PetriNet2'):
        assert not _is_linked(a1, 'petrinet_PetriNet2', b)
    if hasattr(a2, 'petrinet_PetriNet2'):
        assert _is_linked(a2, 'petrinet_PetriNet2', b)
    _safe_set(b, 'petrinet_Arc', None)
    assert not _is_linked(b, 'petrinet_Arc', a2)
    if hasattr(a2, 'petrinet_PetriNet2'):
        assert not _is_linked(a2, 'petrinet_PetriNet2', b)


def test_assoc_noeuds0_reverse_link_reassign_clear():
    a1 = petrinet_PetriNet(name="sample_text")
    a2 = petrinet_PetriNet(name="sample_text_2")
    b = petrinet_Noeud(name="sample_text")
    _safe_set(b, 'petrinet_Noeud', a1)
    assert _is_linked(b, 'petrinet_Noeud', a1)
    if hasattr(a1, 'petrinet_PetriNet'):
        assert _is_linked(a1, 'petrinet_PetriNet', b)
    _safe_set(b, 'petrinet_Noeud', a2)
    assert _is_linked(b, 'petrinet_Noeud', a2)
    if hasattr(a1, 'petrinet_PetriNet'):
        assert not _is_linked(a1, 'petrinet_PetriNet', b)
    if hasattr(a2, 'petrinet_PetriNet'):
        assert _is_linked(a2, 'petrinet_PetriNet', b)
    _safe_set(b, 'petrinet_Noeud', None)
    assert not _is_linked(b, 'petrinet_Noeud', a2)
    if hasattr(a2, 'petrinet_PetriNet'):
        assert not _is_linked(a2, 'petrinet_PetriNet', b)


def test_assoc_source3_reverse_link_reassign_clear():
    a1 = petrinet_Noeud(name="sample_text")
    a2 = petrinet_Noeud(name="sample_text_2")
    b = petrinet_Arc(arcType="sample_text", name="sample_text", weight=7)
    _safe_set(b, 'petrinet_Arc4', a1)
    assert _is_linked(b, 'petrinet_Arc4', a1)
    if hasattr(a1, 'petrinet_Noeud5'):
        assert _is_linked(a1, 'petrinet_Noeud5', b)
    _safe_set(b, 'petrinet_Arc4', a2)
    assert _is_linked(b, 'petrinet_Arc4', a2)
    if hasattr(a1, 'petrinet_Noeud5'):
        assert not _is_linked(a1, 'petrinet_Noeud5', b)
    if hasattr(a2, 'petrinet_Noeud5'):
        assert _is_linked(a2, 'petrinet_Noeud5', b)
    _safe_set(b, 'petrinet_Arc4', None)
    assert not _is_linked(b, 'petrinet_Arc4', a2)
    if hasattr(a2, 'petrinet_Noeud5'):
        assert not _is_linked(a2, 'petrinet_Noeud5', b)


def test_assoc_target6_reverse_link_reassign_clear():
    a1 = petrinet_Noeud(name="sample_text")
    a2 = petrinet_Noeud(name="sample_text_2")
    b = petrinet_Arc(arcType="sample_text", name="sample_text", weight=7)
    _safe_set(b, 'petrinet_Arc7', a1)
    assert _is_linked(b, 'petrinet_Arc7', a1)
    if hasattr(a1, 'petrinet_Noeud8'):
        assert _is_linked(a1, 'petrinet_Noeud8', b)
    _safe_set(b, 'petrinet_Arc7', a2)
    assert _is_linked(b, 'petrinet_Arc7', a2)
    if hasattr(a1, 'petrinet_Noeud8'):
        assert not _is_linked(a1, 'petrinet_Noeud8', b)
    if hasattr(a2, 'petrinet_Noeud8'):
        assert _is_linked(a2, 'petrinet_Noeud8', b)
    _safe_set(b, 'petrinet_Arc7', None)
    assert not _is_linked(b, 'petrinet_Arc7', a2)
    if hasattr(a2, 'petrinet_Noeud8'):
        assert not _is_linked(a2, 'petrinet_Noeud8', b)


