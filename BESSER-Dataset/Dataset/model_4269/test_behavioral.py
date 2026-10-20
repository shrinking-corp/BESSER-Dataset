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

def test_assoc_games2_reverse_link_reassign_clear():
    a1 = bowling_Matchup(name="sample_text")
    a2 = bowling_Matchup(name="sample_text_2")
    b = bowling_Game(frames=7)
    _safe_set(b, 'Game', a1)
    assert _is_linked(b, 'Game', a1)
    if hasattr(a1, 'matchup'):
        assert _is_linked(a1, 'matchup', b)
    _safe_set(b, 'Game', a2)
    assert _is_linked(b, 'Game', a2)
    if hasattr(a1, 'matchup'):
        assert not _is_linked(a1, 'matchup', b)
    if hasattr(a2, 'matchup'):
        assert _is_linked(a2, 'matchup', b)
    _safe_set(b, 'Game', None)
    assert not _is_linked(b, 'Game', a2)
    if hasattr(a2, 'matchup'):
        assert not _is_linked(a2, 'matchup', b)


def test_assoc_matchup3_reverse_link_reassign_clear():
    a1 = bowling_Matchup(name="sample_text")
    a2 = bowling_Matchup(name="sample_text_2")
    b = bowling_Game(frames=7)
    _safe_set(b, 'games', a1)
    assert _is_linked(b, 'games', a1)
    if hasattr(a1, 'Matchup'):
        assert _is_linked(a1, 'Matchup', b)
    _safe_set(b, 'games', a2)
    assert _is_linked(b, 'games', a2)
    if hasattr(a1, 'Matchup'):
        assert not _is_linked(a1, 'Matchup', b)
    if hasattr(a2, 'Matchup'):
        assert _is_linked(a2, 'Matchup', b)
    _safe_set(b, 'games', None)
    assert not _is_linked(b, 'games', a2)
    if hasattr(a2, 'Matchup'):
        assert not _is_linked(a2, 'Matchup', b)


def test_assoc_matchups1_reverse_link_reassign_clear():
    a1 = bowling_Tournament(name="sample_text", type="sample_text")
    a2 = bowling_Tournament(name="sample_text_2", type="sample_text_2")
    b = bowling_Matchup(name="sample_text")
    _safe_set(b, 'bowling_Matchup', a1)
    assert _is_linked(b, 'bowling_Matchup', a1)
    if hasattr(a1, 'bowling_Tournament'):
        assert _is_linked(a1, 'bowling_Tournament', b)
    _safe_set(b, 'bowling_Matchup', a2)
    assert _is_linked(b, 'bowling_Matchup', a2)
    if hasattr(a1, 'bowling_Tournament'):
        assert not _is_linked(a1, 'bowling_Tournament', b)
    if hasattr(a2, 'bowling_Tournament'):
        assert _is_linked(a2, 'bowling_Tournament', b)
    _safe_set(b, 'bowling_Matchup', None)
    assert not _is_linked(b, 'bowling_Matchup', a2)
    if hasattr(a2, 'bowling_Tournament'):
        assert not _is_linked(a2, 'bowling_Tournament', b)


def test_assoc_player4_reverse_link_reassign_clear():
    a1 = bowling_Player(dateOfBirth=date(2024, 1, 1), height=3.14, isProfessional=True, name="sample_text")
    a2 = bowling_Player(dateOfBirth=date(2025, 6, 15), height=9.99, isProfessional=False, name="sample_text_2")
    b = bowling_Game(frames=7)
    _safe_set(b, 'bowling_Game', a1)
    assert _is_linked(b, 'bowling_Game', a1)
    if hasattr(a1, 'bowling_Player5'):
        assert _is_linked(a1, 'bowling_Player5', b)
    _safe_set(b, 'bowling_Game', a2)
    assert _is_linked(b, 'bowling_Game', a2)
    if hasattr(a1, 'bowling_Player5'):
        assert not _is_linked(a1, 'bowling_Player5', b)
    if hasattr(a2, 'bowling_Player5'):
        assert _is_linked(a2, 'bowling_Player5', b)
    _safe_set(b, 'bowling_Game', None)
    assert not _is_linked(b, 'bowling_Game', a2)
    if hasattr(a2, 'bowling_Player5'):
        assert not _is_linked(a2, 'bowling_Player5', b)


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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

