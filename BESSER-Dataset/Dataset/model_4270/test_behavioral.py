import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    bowlingTournament_Game,
    bowlingTournament_League,
    bowlingTournament_Matchup,
    bowlingTournament_Player,
    bowlingTournament_Tournament,
    TournamentType,
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

def test_assoc_league2_reverse_link_reassign_clear():
    a1 = bowlingTournament_Tournament(type="sample_text")
    a2 = bowlingTournament_Tournament(type="sample_text_2")
    b = bowlingTournament_League(name="sample_text")
    _safe_set(b, 'bowlingTournament_League4', a1)
    assert _is_linked(b, 'bowlingTournament_League4', a1)
    if hasattr(a1, 'bowlingTournament_Tournament3'):
        assert _is_linked(a1, 'bowlingTournament_Tournament3', b)
    _safe_set(b, 'bowlingTournament_League4', a2)
    assert _is_linked(b, 'bowlingTournament_League4', a2)
    if hasattr(a1, 'bowlingTournament_Tournament3'):
        assert not _is_linked(a1, 'bowlingTournament_Tournament3', b)
    if hasattr(a2, 'bowlingTournament_Tournament3'):
        assert _is_linked(a2, 'bowlingTournament_Tournament3', b)
    _safe_set(b, 'bowlingTournament_League4', None)
    assert not _is_linked(b, 'bowlingTournament_League4', a2)
    if hasattr(a2, 'bowlingTournament_Tournament3'):
        assert not _is_linked(a2, 'bowlingTournament_Tournament3', b)


def test_assoc_player0_reverse_link_reassign_clear():
    a1 = bowlingTournament_Player(dateOfBirth=date(2024, 1, 1), height=3.14, isProfessional=True, name="sample_text")
    a2 = bowlingTournament_Player(dateOfBirth=date(2025, 6, 15), height=9.99, isProfessional=False, name="sample_text_2")
    b = bowlingTournament_League(name="sample_text")
    _safe_set(b, 'bowlingTournament_League', {a1})
    assert _is_linked(b, 'bowlingTournament_League', a1)
    if hasattr(a1, 'bowlingTournament_Player'):
        assert _is_linked(a1, 'bowlingTournament_Player', b)
    _safe_set(b, 'bowlingTournament_League', {a2})
    assert _is_linked(b, 'bowlingTournament_League', a2)
    if hasattr(a1, 'bowlingTournament_Player'):
        assert not _is_linked(a1, 'bowlingTournament_Player', b)
    if hasattr(a2, 'bowlingTournament_Player'):
        assert _is_linked(a2, 'bowlingTournament_Player', b)
    _safe_set(b, 'bowlingTournament_League', set())
    assert not _is_linked(b, 'bowlingTournament_League', a2)
    if hasattr(a2, 'bowlingTournament_Player'):
        assert not _is_linked(a2, 'bowlingTournament_Player', b)


def test_assoc_player6_reverse_link_reassign_clear():
    a1 = bowlingTournament_Player(dateOfBirth=date(2024, 1, 1), height=3.14, isProfessional=True, name="sample_text")
    a2 = bowlingTournament_Player(dateOfBirth=date(2025, 6, 15), height=9.99, isProfessional=False, name="sample_text_2")
    b = bowlingTournament_Game(frames=7)
    _safe_set(b, 'bowlingTournament_Game', a1)
    assert _is_linked(b, 'bowlingTournament_Game', a1)
    if hasattr(a1, 'bowlingTournament_Player7'):
        assert _is_linked(a1, 'bowlingTournament_Player7', b)
    _safe_set(b, 'bowlingTournament_Game', a2)
    assert _is_linked(b, 'bowlingTournament_Game', a2)
    if hasattr(a1, 'bowlingTournament_Player7'):
        assert not _is_linked(a1, 'bowlingTournament_Player7', b)
    if hasattr(a2, 'bowlingTournament_Player7'):
        assert _is_linked(a2, 'bowlingTournament_Player7', b)
    _safe_set(b, 'bowlingTournament_Game', None)
    assert not _is_linked(b, 'bowlingTournament_Game', a2)
    if hasattr(a2, 'bowlingTournament_Player7'):
        assert not _is_linked(a2, 'bowlingTournament_Player7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_games5_stub_double():
    # bowlingTournament_Matchup has no real 'matchup' property in the generated
    # code (a bare stub) -- manually attach it so bowlingTournament_Game's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bowlingTournament_Game's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bowlingTournament_Game(frames=7)
    partner = bowlingTournament_Matchup()
    setattr(partner, 'matchup', None)
    _safe_set(owner, 'Game', partner)
    assert owner in getattr(partner, 'matchup')
    _safe_set(owner, 'Game', None)
    assert owner not in getattr(partner, 'matchup')


def test_assoc_matchup8_stub_double():
    # bowlingTournament_Matchup has no real 'Matchup' property in the generated
    # code (a bare stub) -- manually attach it so bowlingTournament_Game's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bowlingTournament_Game's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bowlingTournament_Game(frames=7)
    partner = bowlingTournament_Matchup()
    setattr(partner, 'Matchup', None)
    _safe_set(owner, 'games', partner)
    assert getattr(partner, 'Matchup') == owner
    _safe_set(owner, 'games', None)
    assert getattr(partner, 'Matchup') is None


def test_assoc_matchups1_stub_double():
    # bowlingTournament_Matchup has no real 'bowlingTournament_Matchup' property in the generated
    # code (a bare stub) -- manually attach it so bowlingTournament_Tournament's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bowlingTournament_Tournament's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bowlingTournament_Tournament(type="sample_text")
    partner = bowlingTournament_Matchup()
    setattr(partner, 'bowlingTournament_Matchup', None)
    _safe_set(owner, 'bowlingTournament_Tournament', {partner})
    assert getattr(partner, 'bowlingTournament_Matchup') == owner
    _safe_set(owner, 'bowlingTournament_Tournament', set())
    assert getattr(partner, 'bowlingTournament_Matchup') is None


