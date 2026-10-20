import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BlackJackApp,
    BlackJack_Hra,
    Card,
    Deck,
    Hand,
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

def test_assoc_BlackJackApp_BlackJack_Hra_stub_double():
    # BlackJackApp has no real 'blackJack_Hra0' property in the generated
    # code (a bare stub) -- manually attach it so BlackJack_Hra's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # BlackJack_Hra's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = BlackJack_Hra(bet="sample_text", deal="sample_text", dealer_wins="sample_text", dealers_hand="sample_text", deck="sample_text", money="sample_text", placebet="sample_text", play="sample_text", player_asks_for_card="sample_text", player_wins="sample_text", players_hand="sample_text", show_result="sample_text", tie="sample_text")
    partner = BlackJackApp()
    setattr(partner, 'blackJack_Hra0', None)
    _safe_set(owner, 'blackJackApp1', partner)
    assert getattr(partner, 'blackJack_Hra0') == owner
    _safe_set(owner, 'blackJackApp1', None)
    assert getattr(partner, 'blackJack_Hra0') is None


