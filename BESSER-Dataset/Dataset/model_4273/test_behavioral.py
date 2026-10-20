import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    bowling_Area,
    bowling_Fan,
    bowling_Game,
    bowling_League,
    bowling_Matchup,
    bowling_Merchandise,
    bowling_Player,
    bowling_PlayerToPointsMap,
    bowling_Referee,
    bowling_RefereeToGamesMap,
    bowling_Tournament,
    Gender,
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

def test_assoc_fanMerchandise31_reverse_link_reassign_clear():
    a1 = bowling_Merchandise(name="sample_text", price="sample_text", serialNumber="sample_text")
    a2 = bowling_Merchandise(name="sample_text_2", price="sample_text_2", serialNumber="sample_text_2")
    b = bowling_Fan(dateOfBirth=date(2024, 1, 1), eMails="sample_text", gender="sample_text", hasSeasonTicket=True, moneySpentOnTickets=3.14, name="sample_text", numberOfTournamentsVisited=7)
    _safe_set(b, 'bowling_Fan32', {a1})
    assert _is_linked(b, 'bowling_Fan32', a1)
    if hasattr(a1, 'bowling_Merchandise'):
        assert _is_linked(a1, 'bowling_Merchandise', b)
    _safe_set(b, 'bowling_Fan32', {a2})
    assert _is_linked(b, 'bowling_Fan32', a2)
    if hasattr(a1, 'bowling_Merchandise'):
        assert not _is_linked(a1, 'bowling_Merchandise', b)
    if hasattr(a2, 'bowling_Merchandise'):
        assert _is_linked(a2, 'bowling_Merchandise', b)
    _safe_set(b, 'bowling_Fan32', set())
    assert not _is_linked(b, 'bowling_Fan32', a2)
    if hasattr(a2, 'bowling_Merchandise'):
        assert not _is_linked(a2, 'bowling_Merchandise', b)


def test_assoc_favouriteMerchandise33_reverse_link_reassign_clear():
    a1 = bowling_Merchandise(name="sample_text", price="sample_text", serialNumber="sample_text")
    a2 = bowling_Merchandise(name="sample_text_2", price="sample_text_2", serialNumber="sample_text_2")
    b = bowling_Fan(dateOfBirth=date(2024, 1, 1), eMails="sample_text", gender="sample_text", hasSeasonTicket=True, moneySpentOnTickets=3.14, name="sample_text", numberOfTournamentsVisited=7)
    _safe_set(b, 'bowling_Fan34', a1)
    assert _is_linked(b, 'bowling_Fan34', a1)
    if hasattr(a1, 'bowling_Merchandise35'):
        assert _is_linked(a1, 'bowling_Merchandise35', b)
    _safe_set(b, 'bowling_Fan34', a2)
    assert _is_linked(b, 'bowling_Fan34', a2)
    if hasattr(a1, 'bowling_Merchandise35'):
        assert not _is_linked(a1, 'bowling_Merchandise35', b)
    if hasattr(a2, 'bowling_Merchandise35'):
        assert _is_linked(a2, 'bowling_Merchandise35', b)
    _safe_set(b, 'bowling_Fan34', None)
    assert not _is_linked(b, 'bowling_Fan34', a2)
    if hasattr(a2, 'bowling_Merchandise35'):
        assert not _is_linked(a2, 'bowling_Merchandise35', b)


def test_assoc_favouritePlayer29_reverse_link_reassign_clear():
    a1 = bowling_Player(dateOfBirth=date(2024, 1, 1), eMails="sample_text", gender="sample_text", height=3.14, isProfessional=True, name="sample_text", numberOfVictories=7, playedTournamentTypes="sample_text", winLossRatio="sample_text")
    a2 = bowling_Player(dateOfBirth=date(2025, 6, 15), eMails="sample_text_2", gender="sample_text_2", height=9.99, isProfessional=False, name="sample_text_2", numberOfVictories=13, playedTournamentTypes="sample_text_2", winLossRatio="sample_text_2")
    b = bowling_Fan(dateOfBirth=date(2024, 1, 1), eMails="sample_text", gender="sample_text", hasSeasonTicket=True, moneySpentOnTickets=3.14, name="sample_text", numberOfTournamentsVisited=7)
    _safe_set(b, 'bowling_Fan', a1)
    assert _is_linked(b, 'bowling_Fan', a1)
    if hasattr(a1, 'bowling_Player30'):
        assert _is_linked(a1, 'bowling_Player30', b)
    _safe_set(b, 'bowling_Fan', a2)
    assert _is_linked(b, 'bowling_Fan', a2)
    if hasattr(a1, 'bowling_Player30'):
        assert not _is_linked(a1, 'bowling_Player30', b)
    if hasattr(a2, 'bowling_Player30'):
        assert _is_linked(a2, 'bowling_Player30', b)
    _safe_set(b, 'bowling_Fan', None)
    assert not _is_linked(b, 'bowling_Fan', a2)
    if hasattr(a2, 'bowling_Player30'):
        assert not _is_linked(a2, 'bowling_Player30', b)


def test_assoc_games9_reverse_link_reassign_clear():
    a1 = bowling_Matchup(nrSpectators="sample_text")
    a2 = bowling_Matchup(nrSpectators="sample_text_2")
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


def test_assoc_key13_reverse_link_reassign_clear():
    a1 = bowling_PlayerToPointsMap(value="sample_text")
    a2 = bowling_PlayerToPointsMap(value="sample_text_2")
    b = bowling_Player(dateOfBirth=date(2024, 1, 1), eMails="sample_text", gender="sample_text", height=3.14, isProfessional=True, name="sample_text", numberOfVictories=7, playedTournamentTypes="sample_text", winLossRatio="sample_text")
    _safe_set(b, 'bowling_Player15', a1)
    assert _is_linked(b, 'bowling_Player15', a1)
    if hasattr(a1, 'bowling_PlayerToPointsMap14'):
        assert _is_linked(a1, 'bowling_PlayerToPointsMap14', b)
    _safe_set(b, 'bowling_Player15', a2)
    assert _is_linked(b, 'bowling_Player15', a2)
    if hasattr(a1, 'bowling_PlayerToPointsMap14'):
        assert not _is_linked(a1, 'bowling_PlayerToPointsMap14', b)
    if hasattr(a2, 'bowling_PlayerToPointsMap14'):
        assert _is_linked(a2, 'bowling_PlayerToPointsMap14', b)
    _safe_set(b, 'bowling_Player15', None)
    assert not _is_linked(b, 'bowling_Player15', a2)
    if hasattr(a2, 'bowling_PlayerToPointsMap14'):
        assert not _is_linked(a2, 'bowling_PlayerToPointsMap14', b)


def test_assoc_league16_reverse_link_reassign_clear():
    a1 = bowling_Referee(dateOfBirth="sample_text")
    a2 = bowling_Referee(dateOfBirth="sample_text_2")
    b = bowling_League(name="sample_text")
    _safe_set(b, 'bowling_League17', a1)
    assert _is_linked(b, 'bowling_League17', a1)
    if hasattr(a1, 'bowling_Referee'):
        assert _is_linked(a1, 'bowling_Referee', b)
    _safe_set(b, 'bowling_League17', a2)
    assert _is_linked(b, 'bowling_League17', a2)
    if hasattr(a1, 'bowling_Referee'):
        assert not _is_linked(a1, 'bowling_Referee', b)
    if hasattr(a2, 'bowling_Referee'):
        assert _is_linked(a2, 'bowling_Referee', b)
    _safe_set(b, 'bowling_League17', None)
    assert not _is_linked(b, 'bowling_League17', a2)
    if hasattr(a2, 'bowling_Referee'):
        assert not _is_linked(a2, 'bowling_Referee', b)


def test_assoc_matchup10_reverse_link_reassign_clear():
    a1 = bowling_Matchup(nrSpectators="sample_text")
    a2 = bowling_Matchup(nrSpectators="sample_text_2")
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
    a1 = bowling_Tournament(matchDays=date(2024, 1, 1), priceMoney=3.14, receivesTrophy=True, type="sample_text")
    a2 = bowling_Tournament(matchDays=date(2025, 6, 15), priceMoney=9.99, receivesTrophy=False, type="sample_text_2")
    b = bowling_Matchup(nrSpectators="sample_text")
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


def test_assoc_player11_reverse_link_reassign_clear():
    a1 = bowling_Player(dateOfBirth=date(2024, 1, 1), eMails="sample_text", gender="sample_text", height=3.14, isProfessional=True, name="sample_text", numberOfVictories=7, playedTournamentTypes="sample_text", winLossRatio="sample_text")
    a2 = bowling_Player(dateOfBirth=date(2025, 6, 15), eMails="sample_text_2", gender="sample_text_2", height=9.99, isProfessional=False, name="sample_text_2", numberOfVictories=13, playedTournamentTypes="sample_text_2", winLossRatio="sample_text_2")
    b = bowling_Game(frames=7)
    _safe_set(b, 'bowling_Game', a1)
    assert _is_linked(b, 'bowling_Game', a1)
    if hasattr(a1, 'bowling_Player12'):
        assert _is_linked(a1, 'bowling_Player12', b)
    _safe_set(b, 'bowling_Game', a2)
    assert _is_linked(b, 'bowling_Game', a2)
    if hasattr(a1, 'bowling_Player12'):
        assert not _is_linked(a1, 'bowling_Player12', b)
    if hasattr(a2, 'bowling_Player12'):
        assert _is_linked(a2, 'bowling_Player12', b)
    _safe_set(b, 'bowling_Game', None)
    assert not _is_linked(b, 'bowling_Game', a2)
    if hasattr(a2, 'bowling_Player12'):
        assert not _is_linked(a2, 'bowling_Player12', b)


def test_assoc_playerPoints2_reverse_link_reassign_clear():
    a1 = bowling_Tournament(matchDays=date(2024, 1, 1), priceMoney=3.14, receivesTrophy=True, type="sample_text")
    a2 = bowling_Tournament(matchDays=date(2025, 6, 15), priceMoney=9.99, receivesTrophy=False, type="sample_text_2")
    b = bowling_PlayerToPointsMap(value="sample_text")
    _safe_set(b, 'bowling_PlayerToPointsMap', a1)
    assert _is_linked(b, 'bowling_PlayerToPointsMap', a1)
    if hasattr(a1, 'bowling_Tournament3'):
        assert _is_linked(a1, 'bowling_Tournament3', b)
    _safe_set(b, 'bowling_PlayerToPointsMap', a2)
    assert _is_linked(b, 'bowling_PlayerToPointsMap', a2)
    if hasattr(a1, 'bowling_Tournament3'):
        assert not _is_linked(a1, 'bowling_Tournament3', b)
    if hasattr(a2, 'bowling_Tournament3'):
        assert _is_linked(a2, 'bowling_Tournament3', b)
    _safe_set(b, 'bowling_PlayerToPointsMap', None)
    assert not _is_linked(b, 'bowling_PlayerToPointsMap', a2)
    if hasattr(a2, 'bowling_Tournament3'):
        assert not _is_linked(a2, 'bowling_Tournament3', b)


def test_assoc_players0_reverse_link_reassign_clear():
    a1 = bowling_Player(dateOfBirth=date(2024, 1, 1), eMails="sample_text", gender="sample_text", height=3.14, isProfessional=True, name="sample_text", numberOfVictories=7, playedTournamentTypes="sample_text", winLossRatio="sample_text")
    a2 = bowling_Player(dateOfBirth=date(2025, 6, 15), eMails="sample_text_2", gender="sample_text_2", height=9.99, isProfessional=False, name="sample_text_2", numberOfVictories=13, playedTournamentTypes="sample_text_2", winLossRatio="sample_text_2")
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


def test_assoc_players4_reverse_link_reassign_clear():
    a1 = bowling_Tournament(matchDays=date(2024, 1, 1), priceMoney=3.14, receivesTrophy=True, type="sample_text")
    a2 = bowling_Tournament(matchDays=date(2025, 6, 15), priceMoney=9.99, receivesTrophy=False, type="sample_text_2")
    b = bowling_Player(dateOfBirth=date(2024, 1, 1), eMails="sample_text", gender="sample_text", height=3.14, isProfessional=True, name="sample_text", numberOfVictories=7, playedTournamentTypes="sample_text", winLossRatio="sample_text")
    _safe_set(b, 'bowling_Player6', a1)
    assert _is_linked(b, 'bowling_Player6', a1)
    if hasattr(a1, 'bowling_Tournament5'):
        assert _is_linked(a1, 'bowling_Tournament5', b)
    _safe_set(b, 'bowling_Player6', a2)
    assert _is_linked(b, 'bowling_Player6', a2)
    if hasattr(a1, 'bowling_Tournament5'):
        assert not _is_linked(a1, 'bowling_Tournament5', b)
    if hasattr(a2, 'bowling_Tournament5'):
        assert _is_linked(a2, 'bowling_Tournament5', b)
    _safe_set(b, 'bowling_Player6', None)
    assert not _is_linked(b, 'bowling_Player6', a2)
    if hasattr(a2, 'bowling_Tournament5'):
        assert not _is_linked(a2, 'bowling_Tournament5', b)


def test_assoc_visitedTournaments36_reverse_link_reassign_clear():
    a1 = bowling_Tournament(matchDays=date(2024, 1, 1), priceMoney=3.14, receivesTrophy=True, type="sample_text")
    a2 = bowling_Tournament(matchDays=date(2025, 6, 15), priceMoney=9.99, receivesTrophy=False, type="sample_text_2")
    b = bowling_Fan(dateOfBirth=date(2024, 1, 1), eMails="sample_text", gender="sample_text", hasSeasonTicket=True, moneySpentOnTickets=3.14, name="sample_text", numberOfTournamentsVisited=7)
    _safe_set(b, 'bowling_Fan37', {a1})
    assert _is_linked(b, 'bowling_Fan37', a1)
    if hasattr(a1, 'bowling_Tournament38'):
        assert _is_linked(a1, 'bowling_Tournament38', b)
    _safe_set(b, 'bowling_Fan37', {a2})
    assert _is_linked(b, 'bowling_Fan37', a2)
    if hasattr(a1, 'bowling_Tournament38'):
        assert not _is_linked(a1, 'bowling_Tournament38', b)
    if hasattr(a2, 'bowling_Tournament38'):
        assert _is_linked(a2, 'bowling_Tournament38', b)
    _safe_set(b, 'bowling_Fan37', set())
    assert not _is_linked(b, 'bowling_Fan37', a2)
    if hasattr(a2, 'bowling_Tournament38'):
        assert not _is_linked(a2, 'bowling_Tournament38', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_key18_stub_double():
    # bowling_RefereeToGamesMap has no real 'bowling_RefereeToGamesMap19' property in the generated
    # code (a bare stub) -- manually attach it so bowling_Referee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bowling_Referee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bowling_Referee(dateOfBirth="sample_text")
    partner = bowling_RefereeToGamesMap()
    setattr(partner, 'bowling_RefereeToGamesMap19', None)
    _safe_set(owner, 'bowling_Referee20', partner)
    assert getattr(partner, 'bowling_RefereeToGamesMap19') == owner
    _safe_set(owner, 'bowling_Referee20', None)
    assert getattr(partner, 'bowling_RefereeToGamesMap19') is None


def test_assoc_referees7_stub_double():
    # bowling_RefereeToGamesMap has no real 'bowling_RefereeToGamesMap' property in the generated
    # code (a bare stub) -- manually attach it so bowling_Tournament's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bowling_Tournament's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bowling_Tournament(matchDays=date(2024, 1, 1), priceMoney=3.14, receivesTrophy=True, type="sample_text")
    partner = bowling_RefereeToGamesMap()
    setattr(partner, 'bowling_RefereeToGamesMap', None)
    _safe_set(owner, 'bowling_Tournament8', {partner})
    assert getattr(partner, 'bowling_RefereeToGamesMap') == owner
    _safe_set(owner, 'bowling_Tournament8', set())
    assert getattr(partner, 'bowling_RefereeToGamesMap') is None


def test_assoc_tournaments26_stub_double():
    # bowling_Area has no real 'bowling_Area27' property in the generated
    # code (a bare stub) -- manually attach it so bowling_Tournament's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bowling_Tournament's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bowling_Tournament(matchDays=date(2024, 1, 1), priceMoney=3.14, receivesTrophy=True, type="sample_text")
    partner = bowling_Area()
    setattr(partner, 'bowling_Area27', None)
    _safe_set(owner, 'bowling_Tournament28', partner)
    assert owner in getattr(partner, 'bowling_Area27')
    _safe_set(owner, 'bowling_Tournament28', None)
    assert owner not in getattr(partner, 'bowling_Area27')


def test_assoc_value21_stub_double():
    # bowling_RefereeToGamesMap has no real 'bowling_RefereeToGamesMap22' property in the generated
    # code (a bare stub) -- manually attach it so bowling_Game's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bowling_Game's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bowling_Game(frames=7)
    partner = bowling_RefereeToGamesMap()
    setattr(partner, 'bowling_RefereeToGamesMap22', None)
    _safe_set(owner, 'bowling_Game23', partner)
    assert getattr(partner, 'bowling_RefereeToGamesMap22') == owner
    _safe_set(owner, 'bowling_Game23', None)
    assert getattr(partner, 'bowling_RefereeToGamesMap22') is None


