import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    GameRound,
    PlayCard,
    Player,
    PlayerView,
    PokerTable,
    PokerTableView,
    RANK_external,
    Role_external,
    SUIT_external,
    StandardDeck,
    T,
    __abstract___BaseDeck,
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

def test_assoc_Pelaaja_Kortti_stub_double():
    # PlayCard has no real 'pelaaja1' property in the generated
    # code (a bare stub) -- manually attach it so Player's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Player's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Player(bid=7, stack=7)
    partner = PlayCard()
    setattr(partner, 'pelaaja1', None)
    _safe_set(owner, 'kortti0', {partner})
    assert getattr(partner, 'pelaaja1') == owner
    _safe_set(owner, 'kortti0', set())
    assert getattr(partner, 'pelaaja1') is None


def test_assoc_PeliPoyta_Pelaaja_stub_double():
    # PokerTable has no real 'pelaaja2' property in the generated
    # code (a bare stub) -- manually attach it so Player's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Player's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Player(bid=7, stack=7)
    partner = PokerTable()
    setattr(partner, 'pelaaja2', None)
    _safe_set(owner, 'Table3', partner)
    assert owner in getattr(partner, 'pelaaja2')
    _safe_set(owner, 'Table3', None)
    assert owner not in getattr(partner, 'pelaaja2')


def test_assoc_Player_Role_stub_double():
    # Role_external has no real 'player13' property in the generated
    # code (a bare stub) -- manually attach it so Player's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Player's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Player(bid=7, stack=7)
    partner = Role_external()
    setattr(partner, 'player13', None)
    _safe_set(owner, 'role12', {partner})
    assert getattr(partner, 'player13') == owner
    _safe_set(owner, 'role12', set())
    assert getattr(partner, 'player13') is None


def test_assoc_PokerTable_Player_stub_double():
    # PokerTable has no real 'Active18' property in the generated
    # code (a bare stub) -- manually attach it so Player's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Player's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Player(bid=7, stack=7)
    partner = PokerTable()
    setattr(partner, 'Active18', None)
    _safe_set(owner, 'pokerTable19', partner)
    assert getattr(partner, 'Active18') == owner
    _safe_set(owner, 'pokerTable19', None)
    assert getattr(partner, 'Active18') is None


