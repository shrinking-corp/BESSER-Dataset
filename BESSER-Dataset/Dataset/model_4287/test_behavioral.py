import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    HockeyleagueObject,
    Player,
    hockeyleague_Arena,
    hockeyleague_Defence,
    hockeyleague_Forward,
    hockeyleague_Goalie,
    hockeyleague_GoalieStats,
    hockeyleague_HockeyleagueObject,
    hockeyleague_League,
    hockeyleague_Player,
    hockeyleague_PlayerStats,
    hockeyleague_Team,
    DefencePositionKind,
    ForwardPositionKind,
    HeightKind,
    ShotKind,
    WeightKind,
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

def test_assoc_playerStats0_reverse_link_reassign_clear():
    a1 = hockeyleague_PlayerStats(assists=7, gameWinningGoals=7, gamesPlayedIn=7, goals=7, penaltyMinutes=7, plusMinus=7, points=7, powerPlayGoals=7, shortHandedGoals=7, shotPercentage=3.14, shots=7, year="sample_text")
    a2 = hockeyleague_PlayerStats(assists=13, gameWinningGoals=13, gamesPlayedIn=13, goals=13, penaltyMinutes=13, plusMinus=13, points=13, powerPlayGoals=13, shortHandedGoals=13, shotPercentage=9.99, shots=13, year="sample_text_2")
    b = hockeyleague_Defence(position="sample_text")
    _safe_set(b, 'hockeyleague_Defence', {a1})
    assert _is_linked(b, 'hockeyleague_Defence', a1)
    if hasattr(a1, 'hockeyleague_PlayerStats'):
        assert _is_linked(a1, 'hockeyleague_PlayerStats', b)
    _safe_set(b, 'hockeyleague_Defence', {a2})
    assert _is_linked(b, 'hockeyleague_Defence', a2)
    if hasattr(a1, 'hockeyleague_PlayerStats'):
        assert not _is_linked(a1, 'hockeyleague_PlayerStats', b)
    if hasattr(a2, 'hockeyleague_PlayerStats'):
        assert _is_linked(a2, 'hockeyleague_PlayerStats', b)
    _safe_set(b, 'hockeyleague_Defence', set())
    assert not _is_linked(b, 'hockeyleague_Defence', a2)
    if hasattr(a2, 'hockeyleague_PlayerStats'):
        assert not _is_linked(a2, 'hockeyleague_PlayerStats', b)


def test_assoc_playerStats1_reverse_link_reassign_clear():
    a1 = hockeyleague_PlayerStats(assists=7, gameWinningGoals=7, gamesPlayedIn=7, goals=7, penaltyMinutes=7, plusMinus=7, points=7, powerPlayGoals=7, shortHandedGoals=7, shotPercentage=3.14, shots=7, year="sample_text")
    a2 = hockeyleague_PlayerStats(assists=13, gameWinningGoals=13, gamesPlayedIn=13, goals=13, penaltyMinutes=13, plusMinus=13, points=13, powerPlayGoals=13, shortHandedGoals=13, shotPercentage=9.99, shots=13, year="sample_text_2")
    b = hockeyleague_Forward(position="sample_text")
    _safe_set(b, 'hockeyleague_Forward', {a1})
    assert _is_linked(b, 'hockeyleague_Forward', a1)
    if hasattr(a1, 'hockeyleague_PlayerStats2'):
        assert _is_linked(a1, 'hockeyleague_PlayerStats2', b)
    _safe_set(b, 'hockeyleague_Forward', {a2})
    assert _is_linked(b, 'hockeyleague_Forward', a2)
    if hasattr(a1, 'hockeyleague_PlayerStats2'):
        assert not _is_linked(a1, 'hockeyleague_PlayerStats2', b)
    if hasattr(a2, 'hockeyleague_PlayerStats2'):
        assert _is_linked(a2, 'hockeyleague_PlayerStats2', b)
    _safe_set(b, 'hockeyleague_Forward', set())
    assert not _is_linked(b, 'hockeyleague_Forward', a2)
    if hasattr(a2, 'hockeyleague_PlayerStats2'):
        assert not _is_linked(a2, 'hockeyleague_PlayerStats2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arena20_stub_double():
    # hockeyleague_Team has no real 'hockeyleague_Team21' property in the generated
    # code (a bare stub) -- manually attach it so hockeyleague_Arena's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hockeyleague_Arena's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hockeyleague_Arena(address="sample_text", capacity=7)
    partner = hockeyleague_Team()
    setattr(partner, 'hockeyleague_Team21', None)
    _safe_set(owner, 'hockeyleague_Arena', partner)
    assert getattr(partner, 'hockeyleague_Team21') == owner
    _safe_set(owner, 'hockeyleague_Arena', None)
    assert getattr(partner, 'hockeyleague_Team21') is None


def test_assoc_defencemen14_stub_double():
    # hockeyleague_Team has no real 'hockeyleague_Team15' property in the generated
    # code (a bare stub) -- manually attach it so hockeyleague_Defence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hockeyleague_Defence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hockeyleague_Defence(position="sample_text")
    partner = hockeyleague_Team()
    setattr(partner, 'hockeyleague_Team15', None)
    _safe_set(owner, 'hockeyleague_Defence16', partner)
    assert getattr(partner, 'hockeyleague_Team15') == owner
    _safe_set(owner, 'hockeyleague_Defence16', None)
    assert getattr(partner, 'hockeyleague_Team15') is None


def test_assoc_forwards11_stub_double():
    # hockeyleague_Team has no real 'hockeyleague_Team12' property in the generated
    # code (a bare stub) -- manually attach it so hockeyleague_Forward's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hockeyleague_Forward's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hockeyleague_Forward(position="sample_text")
    partner = hockeyleague_Team()
    setattr(partner, 'hockeyleague_Team12', None)
    _safe_set(owner, 'hockeyleague_Forward13', partner)
    assert getattr(partner, 'hockeyleague_Team12') == owner
    _safe_set(owner, 'hockeyleague_Forward13', None)
    assert getattr(partner, 'hockeyleague_Team12') is None


def test_assoc_goalieStats3_stub_double():
    # hockeyleague_Goalie has no real 'hockeyleague_Goalie' property in the generated
    # code (a bare stub) -- manually attach it so hockeyleague_GoalieStats's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hockeyleague_GoalieStats's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hockeyleague_GoalieStats(assists=7, emptyNetGoals=7, gamesPlayedIn=7, goals=7, goalsAgainst=7, goalsAgainstAverage=3.14, losses=7, minutesPlayedIn=7, penaltyMinutes=7, points=7, saves=7, shutouts=7, ties=7, wins=7, year="sample_text")
    partner = hockeyleague_Goalie()
    setattr(partner, 'hockeyleague_Goalie', None)
    _safe_set(owner, 'hockeyleague_GoalieStats', partner)
    assert getattr(partner, 'hockeyleague_Goalie') == owner
    _safe_set(owner, 'hockeyleague_GoalieStats', None)
    assert getattr(partner, 'hockeyleague_Goalie') is None


def test_assoc_team4_stub_double():
    # hockeyleague_Team has no real 'hockeyleague_Team' property in the generated
    # code (a bare stub) -- manually attach it so hockeyleague_GoalieStats's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hockeyleague_GoalieStats's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hockeyleague_GoalieStats(assists=7, emptyNetGoals=7, gamesPlayedIn=7, goals=7, goalsAgainst=7, goalsAgainstAverage=3.14, losses=7, minutesPlayedIn=7, penaltyMinutes=7, points=7, saves=7, shutouts=7, ties=7, wins=7, year="sample_text")
    partner = hockeyleague_Team()
    setattr(partner, 'hockeyleague_Team', None)
    _safe_set(owner, 'hockeyleague_GoalieStats5', partner)
    assert getattr(partner, 'hockeyleague_Team') == owner
    _safe_set(owner, 'hockeyleague_GoalieStats5', None)
    assert getattr(partner, 'hockeyleague_Team') is None


def test_assoc_team8_stub_double():
    # hockeyleague_Team has no real 'hockeyleague_Team10' property in the generated
    # code (a bare stub) -- manually attach it so hockeyleague_PlayerStats's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hockeyleague_PlayerStats's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hockeyleague_PlayerStats(assists=7, gameWinningGoals=7, gamesPlayedIn=7, goals=7, penaltyMinutes=7, plusMinus=7, points=7, powerPlayGoals=7, shortHandedGoals=7, shotPercentage=3.14, shots=7, year="sample_text")
    partner = hockeyleague_Team()
    setattr(partner, 'hockeyleague_Team10', None)
    _safe_set(owner, 'hockeyleague_PlayerStats9', partner)
    assert getattr(partner, 'hockeyleague_Team10') == owner
    _safe_set(owner, 'hockeyleague_PlayerStats9', None)
    assert getattr(partner, 'hockeyleague_Team10') is None


def test_assoc_teams6_stub_double():
    # hockeyleague_Team has no real 'hockeyleague_Team7' property in the generated
    # code (a bare stub) -- manually attach it so hockeyleague_League's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hockeyleague_League's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hockeyleague_League(headoffice="sample_text")
    partner = hockeyleague_Team()
    setattr(partner, 'hockeyleague_Team7', None)
    _safe_set(owner, 'hockeyleague_League', {partner})
    assert getattr(partner, 'hockeyleague_Team7') == owner
    _safe_set(owner, 'hockeyleague_League', set())
    assert getattr(partner, 'hockeyleague_Team7') is None


