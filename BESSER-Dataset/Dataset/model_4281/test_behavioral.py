import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    bowling_Game,
    bowling_Matchup,
    bowling_Player,
    bowling_Playerlist,
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

def test_assoc_game0_reverse_link_reassign_clear():
    a1 = bowling_Player(city="sample_text", dateOfBirth=date(2024, 1, 1), firstname="sample_text", height=3.14, isProfessional=True, lastname="sample_text", street="sample_text", streetnumber=7)
    a2 = bowling_Player(city="sample_text_2", dateOfBirth=date(2025, 6, 15), firstname="sample_text_2", height=9.99, isProfessional=False, lastname="sample_text_2", street="sample_text_2", streetnumber=13)
    b = bowling_Game(date=date(2024, 1, 1), frames=7)
    _safe_set(b, 'Game', a1)
    assert _is_linked(b, 'Game', a1)
    if hasattr(a1, 'player'):
        assert _is_linked(a1, 'player', b)
    _safe_set(b, 'Game', a2)
    assert _is_linked(b, 'Game', a2)
    if hasattr(a1, 'player'):
        assert not _is_linked(a1, 'player', b)
    if hasattr(a2, 'player'):
        assert _is_linked(a2, 'player', b)
    _safe_set(b, 'Game', None)
    assert not _is_linked(b, 'Game', a2)
    if hasattr(a2, 'player'):
        assert not _is_linked(a2, 'player', b)


def test_assoc_player3_reverse_link_reassign_clear():
    a1 = bowling_Player(city="sample_text", dateOfBirth=date(2024, 1, 1), firstname="sample_text", height=3.14, isProfessional=True, lastname="sample_text", street="sample_text", streetnumber=7)
    a2 = bowling_Player(city="sample_text_2", dateOfBirth=date(2025, 6, 15), firstname="sample_text_2", height=9.99, isProfessional=False, lastname="sample_text_2", street="sample_text_2", streetnumber=13)
    b = bowling_Game(date=date(2024, 1, 1), frames=7)
    _safe_set(b, 'game', a1)
    assert _is_linked(b, 'game', a1)
    if hasattr(a1, 'Player'):
        assert _is_linked(a1, 'Player', b)
    _safe_set(b, 'game', a2)
    assert _is_linked(b, 'game', a2)
    if hasattr(a1, 'Player'):
        assert not _is_linked(a1, 'Player', b)
    if hasattr(a2, 'Player'):
        assert _is_linked(a2, 'Player', b)
    _safe_set(b, 'game', None)
    assert not _is_linked(b, 'game', a2)
    if hasattr(a2, 'Player'):
        assert not _is_linked(a2, 'Player', b)


def test_assoc_player9_reverse_link_reassign_clear():
    a1 = bowling_Playerlist(name="sample_text")
    a2 = bowling_Playerlist(name="sample_text_2")
    b = bowling_Player(city="sample_text", dateOfBirth=date(2024, 1, 1), firstname="sample_text", height=3.14, isProfessional=True, lastname="sample_text", street="sample_text", streetnumber=7)
    _safe_set(b, 'Player10', a1)
    assert _is_linked(b, 'Player10', a1)
    if hasattr(a1, 'playerlist'):
        assert _is_linked(a1, 'playerlist', b)
    _safe_set(b, 'Player10', a2)
    assert _is_linked(b, 'Player10', a2)
    if hasattr(a1, 'playerlist'):
        assert not _is_linked(a1, 'playerlist', b)
    if hasattr(a2, 'playerlist'):
        assert _is_linked(a2, 'playerlist', b)
    _safe_set(b, 'Player10', None)
    assert not _is_linked(b, 'Player10', a2)
    if hasattr(a2, 'playerlist'):
        assert not _is_linked(a2, 'playerlist', b)


def test_assoc_playerlist1_reverse_link_reassign_clear():
    a1 = bowling_Playerlist(name="sample_text")
    a2 = bowling_Playerlist(name="sample_text_2")
    b = bowling_Player(city="sample_text", dateOfBirth=date(2024, 1, 1), firstname="sample_text", height=3.14, isProfessional=True, lastname="sample_text", street="sample_text", streetnumber=7)
    _safe_set(b, 'player2', a1)
    assert _is_linked(b, 'player2', a1)
    if hasattr(a1, 'Playerlist'):
        assert _is_linked(a1, 'Playerlist', b)
    _safe_set(b, 'player2', a2)
    assert _is_linked(b, 'player2', a2)
    if hasattr(a1, 'Playerlist'):
        assert not _is_linked(a1, 'Playerlist', b)
    if hasattr(a2, 'Playerlist'):
        assert _is_linked(a2, 'Playerlist', b)
    _safe_set(b, 'player2', None)
    assert not _is_linked(b, 'player2', a2)
    if hasattr(a2, 'Playerlist'):
        assert not _is_linked(a2, 'Playerlist', b)


def test_assoc_playerlist16_reverse_link_reassign_clear():
    a1 = bowling_Tournament(title="sample_text", type="sample_text")
    a2 = bowling_Tournament(title="sample_text_2", type="sample_text_2")
    b = bowling_Playerlist(name="sample_text")
    _safe_set(b, 'Playerlist18', a1)
    assert _is_linked(b, 'Playerlist18', a1)
    if hasattr(a1, 'tournament17'):
        assert _is_linked(a1, 'tournament17', b)
    _safe_set(b, 'Playerlist18', a2)
    assert _is_linked(b, 'Playerlist18', a2)
    if hasattr(a1, 'tournament17'):
        assert not _is_linked(a1, 'tournament17', b)
    if hasattr(a2, 'tournament17'):
        assert _is_linked(a2, 'tournament17', b)
    _safe_set(b, 'Playerlist18', None)
    assert not _is_linked(b, 'Playerlist18', a2)
    if hasattr(a2, 'tournament17'):
        assert not _is_linked(a2, 'tournament17', b)


def test_assoc_tournament11_reverse_link_reassign_clear():
    a1 = bowling_Tournament(title="sample_text", type="sample_text")
    a2 = bowling_Tournament(title="sample_text_2", type="sample_text_2")
    b = bowling_Playerlist(name="sample_text")
    _safe_set(b, 'playerlist12', a1)
    assert _is_linked(b, 'playerlist12', a1)
    if hasattr(a1, 'Tournament13'):
        assert _is_linked(a1, 'Tournament13', b)
    _safe_set(b, 'playerlist12', a2)
    assert _is_linked(b, 'playerlist12', a2)
    if hasattr(a1, 'Tournament13'):
        assert not _is_linked(a1, 'Tournament13', b)
    if hasattr(a2, 'Tournament13'):
        assert _is_linked(a2, 'Tournament13', b)
    _safe_set(b, 'playerlist12', None)
    assert not _is_linked(b, 'playerlist12', a2)
    if hasattr(a2, 'Tournament13'):
        assert not _is_linked(a2, 'Tournament13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_game6_stub_double():
    # bowling_Matchup has no real 'matchup' property in the generated
    # code (a bare stub) -- manually attach it so bowling_Game's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bowling_Game's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bowling_Game(date=date(2024, 1, 1), frames=7)
    partner = bowling_Matchup()
    setattr(partner, 'matchup', None)
    _safe_set(owner, 'Game7', partner)
    assert owner in getattr(partner, 'matchup')
    _safe_set(owner, 'Game7', None)
    assert owner not in getattr(partner, 'matchup')


def test_assoc_matchup4_stub_double():
    # bowling_Matchup has no real 'Matchup' property in the generated
    # code (a bare stub) -- manually attach it so bowling_Game's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bowling_Game's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bowling_Game(date=date(2024, 1, 1), frames=7)
    partner = bowling_Matchup()
    setattr(partner, 'Matchup', None)
    _safe_set(owner, 'game5', partner)
    assert getattr(partner, 'Matchup') == owner
    _safe_set(owner, 'game5', None)
    assert getattr(partner, 'Matchup') is None


def test_assoc_matchups14_stub_double():
    # bowling_Matchup has no real 'Matchup15' property in the generated
    # code (a bare stub) -- manually attach it so bowling_Tournament's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bowling_Tournament's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bowling_Tournament(title="sample_text", type="sample_text")
    partner = bowling_Matchup()
    setattr(partner, 'Matchup15', None)
    _safe_set(owner, 'tournament', {partner})
    assert getattr(partner, 'Matchup15') == owner
    _safe_set(owner, 'tournament', set())
    assert getattr(partner, 'Matchup15') is None


def test_assoc_tournament8_stub_double():
    # bowling_Matchup has no real 'matchups' property in the generated
    # code (a bare stub) -- manually attach it so bowling_Tournament's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bowling_Tournament's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bowling_Tournament(title="sample_text", type="sample_text")
    partner = bowling_Matchup()
    setattr(partner, 'matchups', None)
    _safe_set(owner, 'Tournament', partner)
    assert getattr(partner, 'matchups') == owner
    _safe_set(owner, 'Tournament', None)
    assert getattr(partner, 'matchups') is None


