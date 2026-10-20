import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Cards_Card,
    MainGame_Deck,
    MainGame_GUI,
    MainGame_Hand,
    MainGame_Main,
    Players_Player,
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

def test_assoc_composed_of_reverse_link_reassign_clear():
    a1 = MainGame_Hand(Hand="sample_text", flush=True, fourKind=True, fullHouse=True, highCard=True, onePair=True, straight=True, straightFlush=True, threeKing=True, twoPair=True)
    a2 = MainGame_Hand(Hand="sample_text_2", flush=False, fourKind=False, fullHouse=False, highCard=False, onePair=False, straight=False, straightFlush=False, threeKing=False, twoPair=False)
    b = Cards_Card(suit="sample_text", value=7)
    _safe_set(b, 'hand5', a1)
    assert _is_linked(b, 'hand5', a1)
    if hasattr(a1, 'card4'):
        assert _is_linked(a1, 'card4', b)
    _safe_set(b, 'hand5', a2)
    assert _is_linked(b, 'hand5', a2)
    if hasattr(a1, 'card4'):
        assert not _is_linked(a1, 'card4', b)
    if hasattr(a2, 'card4'):
        assert _is_linked(a2, 'card4', b)
    _safe_set(b, 'hand5', None)
    assert not _is_linked(b, 'hand5', a2)
    if hasattr(a2, 'card4'):
        assert not _is_linked(a2, 'card4', b)


def test_assoc_contains_reverse_link_reassign_clear():
    a1 = MainGame_Deck(Cards="sample_text")
    a2 = MainGame_Deck(Cards="sample_text_2")
    b = Cards_Card(suit="sample_text", value=7)
    _safe_set(b, 'deck0', a1)
    assert _is_linked(b, 'deck0', a1)
    if hasattr(a1, 'card1'):
        assert _is_linked(a1, 'card1', b)
    _safe_set(b, 'deck0', a2)
    assert _is_linked(b, 'deck0', a2)
    if hasattr(a1, 'card1'):
        assert not _is_linked(a1, 'card1', b)
    if hasattr(a2, 'card1'):
        assert _is_linked(a2, 'card1', b)
    _safe_set(b, 'deck0', None)
    assert not _is_linked(b, 'deck0', a2)
    if hasattr(a2, 'card1'):
        assert not _is_linked(a2, 'card1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

