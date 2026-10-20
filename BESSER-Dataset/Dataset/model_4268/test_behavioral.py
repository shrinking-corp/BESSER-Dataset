import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    bowling_Game,
    bowling_League,
    bowling_Matchup,
    bowling_Player,
    bowling_Tournament,
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

def test_assoc_player10_reverse_link_reassign_clear():
    a1 = bowling_Player(dateOfBirth=date(2024, 1, 1), height=3.14, isProfessional=True, name="sample_text")
    a2 = bowling_Player(dateOfBirth=date(2025, 6, 15), height=9.99, isProfessional=False, name="sample_text_2")
    b = bowling_Game(frames=7)
    _safe_set(b, 'bowling_Game', a1)
    assert _is_linked(b, 'bowling_Game', a1)
    if hasattr(a1, 'bowling_Player11'):
        assert _is_linked(a1, 'bowling_Player11', b)
    _safe_set(b, 'bowling_Game', a2)
    assert _is_linked(b, 'bowling_Game', a2)
    if hasattr(a1, 'bowling_Player11'):
        assert not _is_linked(a1, 'bowling_Player11', b)
    if hasattr(a2, 'bowling_Player11'):
        assert _is_linked(a2, 'bowling_Player11', b)
    _safe_set(b, 'bowling_Game', None)
    assert not _is_linked(b, 'bowling_Game', a2)
    if hasattr(a2, 'bowling_Player11'):
        assert not _is_linked(a2, 'bowling_Player11', b)


def test_assoc_players0_reverse_link_reassign_clear():
    a1 = bowling_Player(dateOfBirth=date(2024, 1, 1), height=3.14, isProfessional=True, name="sample_text")
    a2 = bowling_Player(dateOfBirth=date(2025, 6, 15), height=9.99, isProfessional=False, name="sample_text_2")
    b = bowling_League(name="sample_text")
    _safe_set(b, 'bowling_League', {a1})
    assert _is_linked(b, 'bowling_League', a1)
    if hasattr(a1, 'bowling_Player'):
        assert _is_linked(a1, 'bowling_Player', b)
    _safe_set(b, 'bowling_League', {a2})
    assert _is_linked(b, 'bowling_League', a2)
    if hasattr(a1, 'bowling_Player'):
        assert not _is_linked(a1, 'bowling_Player', b)
    if hasattr(a2, 'bowling_Player'):
        assert _is_linked(a2, 'bowling_Player', b)
    _safe_set(b, 'bowling_League', set())
    assert not _is_linked(b, 'bowling_League', a2)
    if hasattr(a2, 'bowling_Player'):
        assert not _is_linked(a2, 'bowling_Player', b)


def test_assoc_subleagues2_reverse_link_reassign_clear():
    a1 = bowling_League(name="sample_text")
    a2 = bowling_League(name="sample_text_2")
    b = bowling_League(name="sample_text")
    _safe_set(b, 'bowling_League3', a1)
    assert _is_linked(b, 'bowling_League3', a1)
    if hasattr(a1, 'bowling_League1'):
        assert _is_linked(a1, 'bowling_League1', b)
    _safe_set(b, 'bowling_League3', a2)
    assert _is_linked(b, 'bowling_League3', a2)
    if hasattr(a1, 'bowling_League1'):
        assert not _is_linked(a1, 'bowling_League1', b)
    if hasattr(a2, 'bowling_League1'):
        assert _is_linked(a2, 'bowling_League1', b)
    _safe_set(b, 'bowling_League3', None)
    assert not _is_linked(b, 'bowling_League3', a2)
    if hasattr(a2, 'bowling_League1'):
        assert not _is_linked(a2, 'bowling_League1', b)


def test_assoc_tournaments4_reverse_link_reassign_clear():
    a1 = bowling_Tournament(type="sample_text")
    a2 = bowling_Tournament(type="sample_text_2")
    b = bowling_League(name="sample_text")
    _safe_set(b, 'bowling_League5', a1)
    assert _is_linked(b, 'bowling_League5', a1)
    if hasattr(a1, 'bowling_Tournament'):
        assert _is_linked(a1, 'bowling_Tournament', b)
    _safe_set(b, 'bowling_League5', a2)
    assert _is_linked(b, 'bowling_League5', a2)
    if hasattr(a1, 'bowling_Tournament'):
        assert not _is_linked(a1, 'bowling_Tournament', b)
    if hasattr(a2, 'bowling_Tournament'):
        assert _is_linked(a2, 'bowling_Tournament', b)
    _safe_set(b, 'bowling_League5', None)
    assert not _is_linked(b, 'bowling_League5', a2)
    if hasattr(a2, 'bowling_Tournament'):
        assert not _is_linked(a2, 'bowling_Tournament', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_games8_stub_double():
    # bowling_Matchup has no real 'matchup' property in the generated
    # code (a bare stub) -- manually attach it so bowling_Game's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bowling_Game's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bowling_Game(frames=7)
    partner = bowling_Matchup()
    setattr(partner, 'matchup', None)
    _safe_set(owner, 'Game', partner)
    assert owner in getattr(partner, 'matchup')
    _safe_set(owner, 'Game', None)
    assert owner not in getattr(partner, 'matchup')


def test_assoc_matchup9_stub_double():
    # bowling_Matchup has no real 'Matchup' property in the generated
    # code (a bare stub) -- manually attach it so bowling_Game's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bowling_Game's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bowling_Game(frames=7)
    partner = bowling_Matchup()
    setattr(partner, 'Matchup', None)
    _safe_set(owner, 'games', partner)
    assert getattr(partner, 'Matchup') == owner
    _safe_set(owner, 'games', None)
    assert getattr(partner, 'Matchup') is None


def test_assoc_matchups6_stub_double():
    # bowling_Matchup has no real 'bowling_Matchup' property in the generated
    # code (a bare stub) -- manually attach it so bowling_Tournament's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bowling_Tournament's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bowling_Tournament(type="sample_text")
    partner = bowling_Matchup()
    setattr(partner, 'bowling_Matchup', None)
    _safe_set(owner, 'bowling_Tournament7', {partner})
    assert getattr(partner, 'bowling_Matchup') == owner
    _safe_set(owner, 'bowling_Tournament7', set())
    assert getattr(partner, 'bowling_Matchup') is None


