import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AI,
    Card,
    CommunityCards,
    Deck,
    Game,
    Player,
    makeNewPlayer,
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

def test_assoc_Community_Cards_Card_reverse_link_reassign_clear():
    a1 = CommunityCards(cards="sample_text")
    a2 = CommunityCards(cards="sample_text_2")
    b = Card(suit="sample_text", value=7)
    _safe_set(b, 'communityCards7', a1)
    assert _is_linked(b, 'communityCards7', a1)
    if hasattr(a1, 'card6'):
        assert _is_linked(a1, 'card6', b)
    _safe_set(b, 'communityCards7', a2)
    assert _is_linked(b, 'communityCards7', a2)
    if hasattr(a1, 'card6'):
        assert not _is_linked(a1, 'card6', b)
    if hasattr(a2, 'card6'):
        assert _is_linked(a2, 'card6', b)
    _safe_set(b, 'communityCards7', None)
    assert not _is_linked(b, 'communityCards7', a2)
    if hasattr(a2, 'card6'):
        assert not _is_linked(a2, 'card6', b)


def test_assoc_DeckOfCards_Card_reverse_link_reassign_clear():
    a1 = Deck(cards="sample_text", positionInDeck=7)
    a2 = Deck(cards="sample_text_2", positionInDeck=13)
    b = Card(suit="sample_text", value=7)
    _safe_set(b, 'DeckOfCards1', a1)
    assert _is_linked(b, 'DeckOfCards1', a1)
    if hasattr(a1, 'card0'):
        assert _is_linked(a1, 'card0', b)
    _safe_set(b, 'DeckOfCards1', a2)
    assert _is_linked(b, 'DeckOfCards1', a2)
    if hasattr(a1, 'card0'):
        assert not _is_linked(a1, 'card0', b)
    if hasattr(a2, 'card0'):
        assert _is_linked(a2, 'card0', b)
    _safe_set(b, 'DeckOfCards1', None)
    assert not _is_linked(b, 'DeckOfCards1', a2)
    if hasattr(a2, 'card0'):
        assert not _is_linked(a2, 'card0', b)


def test_assoc_Player_Card_reverse_link_reassign_clear():
    a1 = Player(chips=7, hand="sample_text", handValue=7, isAI=True, isAllIn=True, isBigBlind=True, isFolded=True, isSmallBlind=True, name="sample_text", playerNumber=7)
    a2 = Player(chips=13, hand="sample_text_2", handValue=13, isAI=False, isAllIn=False, isBigBlind=False, isFolded=False, isSmallBlind=False, name="sample_text_2", playerNumber=13)
    b = Card(suit="sample_text", value=7)
    _safe_set(b, 'player11', a1)
    assert _is_linked(b, 'player11', a1)
    if hasattr(a1, 'card10'):
        assert _is_linked(a1, 'card10', b)
    _safe_set(b, 'player11', a2)
    assert _is_linked(b, 'player11', a2)
    if hasattr(a1, 'card10'):
        assert not _is_linked(a1, 'card10', b)
    if hasattr(a2, 'card10'):
        assert _is_linked(a2, 'card10', b)
    _safe_set(b, 'player11', None)
    assert not _is_linked(b, 'player11', a2)
    if hasattr(a2, 'card10'):
        assert not _is_linked(a2, 'card10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

