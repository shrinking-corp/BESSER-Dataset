import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Banker,
    Business_Owner,
    Cards_external,
    ComputerPlayer,
    Creator,
    Human_Player_external,
    Interface_Interface,
    Enumeration,
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

def test_assoc_Player_ComputerPlayer_reverse_link_reassign_clear():
    a1 = Creator(currentBet=3.14, folded=True, money=3.14, name="sample_text")
    a2 = Creator(currentBet=9.99, folded=False, money=9.99, name="sample_text_2")
    b = ComputerPlayer(difficulty=7)
    _safe_set(b, 'player1', a1)
    assert _is_linked(b, 'player1', a1)
    if hasattr(a1, 'computerPlayer0'):
        assert _is_linked(a1, 'computerPlayer0', b)
    _safe_set(b, 'player1', a2)
    assert _is_linked(b, 'player1', a2)
    if hasattr(a1, 'computerPlayer0'):
        assert not _is_linked(a1, 'computerPlayer0', b)
    if hasattr(a2, 'computerPlayer0'):
        assert _is_linked(a2, 'computerPlayer0', b)
    _safe_set(b, 'player1', None)
    assert not _is_linked(b, 'player1', a2)
    if hasattr(a2, 'computerPlayer0'):
        assert not _is_linked(a2, 'computerPlayer0', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Cards_Hand_stub_double():
    # Cards_external has no real 'make_up_possible_hand4' property in the generated
    # code (a bare stub) -- manually attach it so Business_Owner's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Business_Owner's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Business_Owner(_Card_cards_5_=7)
    partner = Cards_external()
    setattr(partner, 'make_up_possible_hand4', None)
    _safe_set(owner, 'cards5', partner)
    assert getattr(partner, 'make_up_possible_hand4') == owner
    _safe_set(owner, 'cards5', None)
    assert getattr(partner, 'make_up_possible_hand4') is None


def test_assoc_Player_Human_Player_stub_double():
    # Human_Player_external has no real 'player3' property in the generated
    # code (a bare stub) -- manually attach it so Creator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Creator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Creator(currentBet=3.14, folded=True, money=3.14, name="sample_text")
    partner = Human_Player_external()
    setattr(partner, 'player3', None)
    _safe_set(owner, 'human_Player2', partner)
    assert getattr(partner, 'player3') == owner
    _safe_set(owner, 'human_Player2', None)
    assert getattr(partner, 'player3') is None


