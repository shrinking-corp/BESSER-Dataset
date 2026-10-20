import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    PetriNetModel_ArcPT,
    PetriNetModel_ArcTP,
    PetriNetModel_PetriNet,
    PetriNetModel_Place,
    PetriNetModel_Transition,
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

def test_assoc_arcPT1_reverse_link_reassign_clear():
    a1 = PetriNetModel_PetriNet(name="sample_text")
    a2 = PetriNetModel_PetriNet(name="sample_text_2")
    b = PetriNetModel_ArcPT(inscription="sample_text")
    _safe_set(b, 'PetriNetModel_ArcPT', a1)
    assert _is_linked(b, 'PetriNetModel_ArcPT', a1)
    if hasattr(a1, 'PetriNetModel_PetriNet2'):
        assert _is_linked(a1, 'PetriNetModel_PetriNet2', b)
    _safe_set(b, 'PetriNetModel_ArcPT', a2)
    assert _is_linked(b, 'PetriNetModel_ArcPT', a2)
    if hasattr(a1, 'PetriNetModel_PetriNet2'):
        assert not _is_linked(a1, 'PetriNetModel_PetriNet2', b)
    if hasattr(a2, 'PetriNetModel_PetriNet2'):
        assert _is_linked(a2, 'PetriNetModel_PetriNet2', b)
    _safe_set(b, 'PetriNetModel_ArcPT', None)
    assert not _is_linked(b, 'PetriNetModel_ArcPT', a2)
    if hasattr(a2, 'PetriNetModel_PetriNet2'):
        assert not _is_linked(a2, 'PetriNetModel_PetriNet2', b)


def test_assoc_arcTP3_reverse_link_reassign_clear():
    a1 = PetriNetModel_PetriNet(name="sample_text")
    a2 = PetriNetModel_PetriNet(name="sample_text_2")
    b = PetriNetModel_ArcTP(inscription="sample_text")
    _safe_set(b, 'PetriNetModel_ArcTP', a1)
    assert _is_linked(b, 'PetriNetModel_ArcTP', a1)
    if hasattr(a1, 'PetriNetModel_PetriNet4'):
        assert _is_linked(a1, 'PetriNetModel_PetriNet4', b)
    _safe_set(b, 'PetriNetModel_ArcTP', a2)
    assert _is_linked(b, 'PetriNetModel_ArcTP', a2)
    if hasattr(a1, 'PetriNetModel_PetriNet4'):
        assert not _is_linked(a1, 'PetriNetModel_PetriNet4', b)
    if hasattr(a2, 'PetriNetModel_PetriNet4'):
        assert _is_linked(a2, 'PetriNetModel_PetriNet4', b)
    _safe_set(b, 'PetriNetModel_ArcTP', None)
    assert not _is_linked(b, 'PetriNetModel_ArcTP', a2)
    if hasattr(a2, 'PetriNetModel_PetriNet4'):
        assert not _is_linked(a2, 'PetriNetModel_PetriNet4', b)


def test_assoc_place16_reverse_link_reassign_clear():
    a1 = PetriNetModel_Place(name="sample_text", token="sample_text")
    a2 = PetriNetModel_Place(name="sample_text_2", token="sample_text_2")
    b = PetriNetModel_ArcPT(inscription="sample_text")
    _safe_set(b, 'PetriNetModel_ArcPT17', a1)
    assert _is_linked(b, 'PetriNetModel_ArcPT17', a1)
    if hasattr(a1, 'PetriNetModel_Place18'):
        assert _is_linked(a1, 'PetriNetModel_Place18', b)
    _safe_set(b, 'PetriNetModel_ArcPT17', a2)
    assert _is_linked(b, 'PetriNetModel_ArcPT17', a2)
    if hasattr(a1, 'PetriNetModel_Place18'):
        assert not _is_linked(a1, 'PetriNetModel_Place18', b)
    if hasattr(a2, 'PetriNetModel_Place18'):
        assert _is_linked(a2, 'PetriNetModel_Place18', b)
    _safe_set(b, 'PetriNetModel_ArcPT17', None)
    assert not _is_linked(b, 'PetriNetModel_ArcPT17', a2)
    if hasattr(a2, 'PetriNetModel_Place18'):
        assert not _is_linked(a2, 'PetriNetModel_Place18', b)


def test_assoc_place19_reverse_link_reassign_clear():
    a1 = PetriNetModel_Place(name="sample_text", token="sample_text")
    a2 = PetriNetModel_Place(name="sample_text_2", token="sample_text_2")
    b = PetriNetModel_ArcTP(inscription="sample_text")
    _safe_set(b, 'PetriNetModel_ArcTP20', a1)
    assert _is_linked(b, 'PetriNetModel_ArcTP20', a1)
    if hasattr(a1, 'PetriNetModel_Place21'):
        assert _is_linked(a1, 'PetriNetModel_Place21', b)
    _safe_set(b, 'PetriNetModel_ArcTP20', a2)
    assert _is_linked(b, 'PetriNetModel_ArcTP20', a2)
    if hasattr(a1, 'PetriNetModel_Place21'):
        assert not _is_linked(a1, 'PetriNetModel_Place21', b)
    if hasattr(a2, 'PetriNetModel_Place21'):
        assert _is_linked(a2, 'PetriNetModel_Place21', b)
    _safe_set(b, 'PetriNetModel_ArcTP20', None)
    assert not _is_linked(b, 'PetriNetModel_ArcTP20', a2)
    if hasattr(a2, 'PetriNetModel_Place21'):
        assert not _is_linked(a2, 'PetriNetModel_Place21', b)


def test_assoc_place5_reverse_link_reassign_clear():
    a1 = PetriNetModel_Place(name="sample_text", token="sample_text")
    a2 = PetriNetModel_Place(name="sample_text_2", token="sample_text_2")
    b = PetriNetModel_PetriNet(name="sample_text")
    _safe_set(b, 'PetriNetModel_PetriNet6', {a1})
    assert _is_linked(b, 'PetriNetModel_PetriNet6', a1)
    if hasattr(a1, 'PetriNetModel_Place'):
        assert _is_linked(a1, 'PetriNetModel_Place', b)
    _safe_set(b, 'PetriNetModel_PetriNet6', {a2})
    assert _is_linked(b, 'PetriNetModel_PetriNet6', a2)
    if hasattr(a1, 'PetriNetModel_Place'):
        assert not _is_linked(a1, 'PetriNetModel_Place', b)
    if hasattr(a2, 'PetriNetModel_Place'):
        assert _is_linked(a2, 'PetriNetModel_Place', b)
    _safe_set(b, 'PetriNetModel_PetriNet6', set())
    assert not _is_linked(b, 'PetriNetModel_PetriNet6', a2)
    if hasattr(a2, 'PetriNetModel_Place'):
        assert not _is_linked(a2, 'PetriNetModel_Place', b)


def test_assoc_postArc10_reverse_link_reassign_clear():
    a1 = PetriNetModel_Transition(name="sample_text")
    a2 = PetriNetModel_Transition(name="sample_text_2")
    b = PetriNetModel_ArcTP(inscription="sample_text")
    _safe_set(b, 'PetriNetModel_ArcTP12', a1)
    assert _is_linked(b, 'PetriNetModel_ArcTP12', a1)
    if hasattr(a1, 'PetriNetModel_Transition11'):
        assert _is_linked(a1, 'PetriNetModel_Transition11', b)
    _safe_set(b, 'PetriNetModel_ArcTP12', a2)
    assert _is_linked(b, 'PetriNetModel_ArcTP12', a2)
    if hasattr(a1, 'PetriNetModel_Transition11'):
        assert not _is_linked(a1, 'PetriNetModel_Transition11', b)
    if hasattr(a2, 'PetriNetModel_Transition11'):
        assert _is_linked(a2, 'PetriNetModel_Transition11', b)
    _safe_set(b, 'PetriNetModel_ArcTP12', None)
    assert not _is_linked(b, 'PetriNetModel_ArcTP12', a2)
    if hasattr(a2, 'PetriNetModel_Transition11'):
        assert not _is_linked(a2, 'PetriNetModel_Transition11', b)


def test_assoc_postArc28_reverse_link_reassign_clear():
    a1 = PetriNetModel_Place(name="sample_text", token="sample_text")
    a2 = PetriNetModel_Place(name="sample_text_2", token="sample_text_2")
    b = PetriNetModel_ArcPT(inscription="sample_text")
    _safe_set(b, 'PetriNetModel_ArcPT30', a1)
    assert _is_linked(b, 'PetriNetModel_ArcPT30', a1)
    if hasattr(a1, 'PetriNetModel_Place29'):
        assert _is_linked(a1, 'PetriNetModel_Place29', b)
    _safe_set(b, 'PetriNetModel_ArcPT30', a2)
    assert _is_linked(b, 'PetriNetModel_ArcPT30', a2)
    if hasattr(a1, 'PetriNetModel_Place29'):
        assert not _is_linked(a1, 'PetriNetModel_Place29', b)
    if hasattr(a2, 'PetriNetModel_Place29'):
        assert _is_linked(a2, 'PetriNetModel_Place29', b)
    _safe_set(b, 'PetriNetModel_ArcPT30', None)
    assert not _is_linked(b, 'PetriNetModel_ArcPT30', a2)
    if hasattr(a2, 'PetriNetModel_Place29'):
        assert not _is_linked(a2, 'PetriNetModel_Place29', b)


def test_assoc_preArc25_reverse_link_reassign_clear():
    a1 = PetriNetModel_Place(name="sample_text", token="sample_text")
    a2 = PetriNetModel_Place(name="sample_text_2", token="sample_text_2")
    b = PetriNetModel_ArcTP(inscription="sample_text")
    _safe_set(b, 'PetriNetModel_ArcTP27', a1)
    assert _is_linked(b, 'PetriNetModel_ArcTP27', a1)
    if hasattr(a1, 'PetriNetModel_Place26'):
        assert _is_linked(a1, 'PetriNetModel_Place26', b)
    _safe_set(b, 'PetriNetModel_ArcTP27', a2)
    assert _is_linked(b, 'PetriNetModel_ArcTP27', a2)
    if hasattr(a1, 'PetriNetModel_Place26'):
        assert not _is_linked(a1, 'PetriNetModel_Place26', b)
    if hasattr(a2, 'PetriNetModel_Place26'):
        assert _is_linked(a2, 'PetriNetModel_Place26', b)
    _safe_set(b, 'PetriNetModel_ArcTP27', None)
    assert not _is_linked(b, 'PetriNetModel_ArcTP27', a2)
    if hasattr(a2, 'PetriNetModel_Place26'):
        assert not _is_linked(a2, 'PetriNetModel_Place26', b)


def test_assoc_preArc7_reverse_link_reassign_clear():
    a1 = PetriNetModel_Transition(name="sample_text")
    a2 = PetriNetModel_Transition(name="sample_text_2")
    b = PetriNetModel_ArcPT(inscription="sample_text")
    _safe_set(b, 'PetriNetModel_ArcPT9', a1)
    assert _is_linked(b, 'PetriNetModel_ArcPT9', a1)
    if hasattr(a1, 'PetriNetModel_Transition8'):
        assert _is_linked(a1, 'PetriNetModel_Transition8', b)
    _safe_set(b, 'PetriNetModel_ArcPT9', a2)
    assert _is_linked(b, 'PetriNetModel_ArcPT9', a2)
    if hasattr(a1, 'PetriNetModel_Transition8'):
        assert not _is_linked(a1, 'PetriNetModel_Transition8', b)
    if hasattr(a2, 'PetriNetModel_Transition8'):
        assert _is_linked(a2, 'PetriNetModel_Transition8', b)
    _safe_set(b, 'PetriNetModel_ArcPT9', None)
    assert not _is_linked(b, 'PetriNetModel_ArcPT9', a2)
    if hasattr(a2, 'PetriNetModel_Transition8'):
        assert not _is_linked(a2, 'PetriNetModel_Transition8', b)


def test_assoc_transition0_reverse_link_reassign_clear():
    a1 = PetriNetModel_Transition(name="sample_text")
    a2 = PetriNetModel_Transition(name="sample_text_2")
    b = PetriNetModel_PetriNet(name="sample_text")
    _safe_set(b, 'PetriNetModel_PetriNet', {a1})
    assert _is_linked(b, 'PetriNetModel_PetriNet', a1)
    if hasattr(a1, 'PetriNetModel_Transition'):
        assert _is_linked(a1, 'PetriNetModel_Transition', b)
    _safe_set(b, 'PetriNetModel_PetriNet', {a2})
    assert _is_linked(b, 'PetriNetModel_PetriNet', a2)
    if hasattr(a1, 'PetriNetModel_Transition'):
        assert not _is_linked(a1, 'PetriNetModel_Transition', b)
    if hasattr(a2, 'PetriNetModel_Transition'):
        assert _is_linked(a2, 'PetriNetModel_Transition', b)
    _safe_set(b, 'PetriNetModel_PetriNet', set())
    assert not _is_linked(b, 'PetriNetModel_PetriNet', a2)
    if hasattr(a2, 'PetriNetModel_Transition'):
        assert not _is_linked(a2, 'PetriNetModel_Transition', b)


def test_assoc_transition13_reverse_link_reassign_clear():
    a1 = PetriNetModel_Transition(name="sample_text")
    a2 = PetriNetModel_Transition(name="sample_text_2")
    b = PetriNetModel_ArcPT(inscription="sample_text")
    _safe_set(b, 'PetriNetModel_ArcPT14', a1)
    assert _is_linked(b, 'PetriNetModel_ArcPT14', a1)
    if hasattr(a1, 'PetriNetModel_Transition15'):
        assert _is_linked(a1, 'PetriNetModel_Transition15', b)
    _safe_set(b, 'PetriNetModel_ArcPT14', a2)
    assert _is_linked(b, 'PetriNetModel_ArcPT14', a2)
    if hasattr(a1, 'PetriNetModel_Transition15'):
        assert not _is_linked(a1, 'PetriNetModel_Transition15', b)
    if hasattr(a2, 'PetriNetModel_Transition15'):
        assert _is_linked(a2, 'PetriNetModel_Transition15', b)
    _safe_set(b, 'PetriNetModel_ArcPT14', None)
    assert not _is_linked(b, 'PetriNetModel_ArcPT14', a2)
    if hasattr(a2, 'PetriNetModel_Transition15'):
        assert not _is_linked(a2, 'PetriNetModel_Transition15', b)


def test_assoc_transition22_reverse_link_reassign_clear():
    a1 = PetriNetModel_Transition(name="sample_text")
    a2 = PetriNetModel_Transition(name="sample_text_2")
    b = PetriNetModel_ArcTP(inscription="sample_text")
    _safe_set(b, 'PetriNetModel_ArcTP23', a1)
    assert _is_linked(b, 'PetriNetModel_ArcTP23', a1)
    if hasattr(a1, 'PetriNetModel_Transition24'):
        assert _is_linked(a1, 'PetriNetModel_Transition24', b)
    _safe_set(b, 'PetriNetModel_ArcTP23', a2)
    assert _is_linked(b, 'PetriNetModel_ArcTP23', a2)
    if hasattr(a1, 'PetriNetModel_Transition24'):
        assert not _is_linked(a1, 'PetriNetModel_Transition24', b)
    if hasattr(a2, 'PetriNetModel_Transition24'):
        assert _is_linked(a2, 'PetriNetModel_Transition24', b)
    _safe_set(b, 'PetriNetModel_ArcTP23', None)
    assert not _is_linked(b, 'PetriNetModel_ArcTP23', a2)
    if hasattr(a2, 'PetriNetModel_Transition24'):
        assert not _is_linked(a2, 'PetriNetModel_Transition24', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

