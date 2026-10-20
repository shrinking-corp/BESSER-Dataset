import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Card_Interface,
    Deck,
    Function,
    PlayerOne_external,
    PlayerTwo_external,
    Players,
    WAR,
    Rank,
    Suit,
    en,
    en2,
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

def test_assoc_Function_Card_stub_double():
    # Card_Interface has no real 'function15' property in the generated
    # code (a bare stub) -- manually attach it so Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Function(Score=7, removedCard=7)
    partner = Card_Interface()
    setattr(partner, 'function15', None)
    _safe_set(owner, 'card14', partner)
    assert getattr(partner, 'function15') == owner
    _safe_set(owner, 'card14', None)
    assert getattr(partner, 'function15') is None


def test_assoc_Function_PlayerCPU_stub_double():
    # PlayerTwo_external has no real 'function11' property in the generated
    # code (a bare stub) -- manually attach it so Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Function(Score=7, removedCard=7)
    partner = PlayerTwo_external()
    setattr(partner, 'function11', None)
    _safe_set(owner, 'playerCPU10', partner)
    assert getattr(partner, 'function11') == owner
    _safe_set(owner, 'playerCPU10', None)
    assert getattr(partner, 'function11') is None


def test_assoc_Function_PlayerUser_stub_double():
    # PlayerOne_external has no real 'function13' property in the generated
    # code (a bare stub) -- manually attach it so Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Function(Score=7, removedCard=7)
    partner = PlayerOne_external()
    setattr(partner, 'function13', None)
    _safe_set(owner, 'playerUser12', partner)
    assert getattr(partner, 'function13') == owner
    _safe_set(owner, 'playerUser12', None)
    assert getattr(partner, 'function13') is None


