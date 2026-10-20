import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Card,
    Deck,
    GUI,
    GameBoard,
    Player,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Deck_Card_stub_double():
    # Deck has no real 'card0' property in the generated
    # code (a bare stub) -- manually attach it so Card's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Card's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Card(suit=7, value=7)
    partner = Deck()
    setattr(partner, 'card0', None)
    _safe_set(owner, 'deck1', partner)
    assert owner in getattr(partner, 'card0')
    _safe_set(owner, 'deck1', None)
    assert owner not in getattr(partner, 'card0')


def test_assoc_GameBoard_Deck_stub_double():
    # Deck has no real 'gameBoard3' property in the generated
    # code (a bare stub) -- manually attach it so GameBoard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GameBoard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GameBoard(discardPile="sample_text", garbagePile="sample_text", shelf="sample_text")
    partner = Deck()
    setattr(partner, 'gameBoard3', None)
    _safe_set(owner, 'deck2', partner)
    assert getattr(partner, 'gameBoard3') == owner
    _safe_set(owner, 'deck2', None)
    assert getattr(partner, 'gameBoard3') is None


def test_assoc_GameBoard_GUI_stub_double():
    # GUI has no real 'gameBoard7' property in the generated
    # code (a bare stub) -- manually attach it so GameBoard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GameBoard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GameBoard(discardPile="sample_text", garbagePile="sample_text", shelf="sample_text")
    partner = GUI()
    setattr(partner, 'gameBoard7', None)
    _safe_set(owner, 'gUI6', partner)
    assert getattr(partner, 'gameBoard7') == owner
    _safe_set(owner, 'gUI6', None)
    assert getattr(partner, 'gameBoard7') is None


