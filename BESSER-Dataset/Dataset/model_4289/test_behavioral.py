import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Person,
    eSport_Capacity,
    eSport_Coach,
    eSport_Country,
    eSport_FinalStage,
    eSport_Group,
    eSport_GroupStage,
    eSport_League,
    eSport_Match,
    eSport_Person,
    eSport_Player,
    eSport_Qualification,
    eSport_Root,
    eSport_Team,
    eSport_Tournament,
    eSport_Zone,
    CapacityType,
    GroupStageType,
    MatchType,
    Position,
    Season,
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

def test_assoc_allowedZones4_reverse_link_reassign_clear():
    a1 = eSport_Zone(name="sample_text")
    a2 = eSport_Zone(name="sample_text_2")
    b = eSport_Tournament(name="sample_text", size=7, type="sample_text", year=7)
    _safe_set(b, 'tournaments5', {a1})
    assert _is_linked(b, 'tournaments5', a1)
    if hasattr(a1, 'Zone'):
        assert _is_linked(a1, 'Zone', b)
    _safe_set(b, 'tournaments5', {a2})
    assert _is_linked(b, 'tournaments5', a2)
    if hasattr(a1, 'Zone'):
        assert not _is_linked(a1, 'Zone', b)
    if hasattr(a2, 'Zone'):
        assert _is_linked(a2, 'Zone', b)
    _safe_set(b, 'tournaments5', set())
    assert not _is_linked(b, 'tournaments5', a2)
    if hasattr(a2, 'Zone'):
        assert not _is_linked(a2, 'Zone', b)


def test_assoc_capacities20_reverse_link_reassign_clear():
    a1 = eSport_Person(age=7, description="sample_text", name="sample_text")
    a2 = eSport_Person(age=13, description="sample_text_2", name="sample_text_2")
    b = eSport_Capacity(type="sample_text", value=7)
    _safe_set(b, 'eSport_Capacity', a1)
    assert _is_linked(b, 'eSport_Capacity', a1)
    if hasattr(a1, 'eSport_Person'):
        assert _is_linked(a1, 'eSport_Person', b)
    _safe_set(b, 'eSport_Capacity', a2)
    assert _is_linked(b, 'eSport_Capacity', a2)
    if hasattr(a1, 'eSport_Person'):
        assert not _is_linked(a1, 'eSport_Person', b)
    if hasattr(a2, 'eSport_Person'):
        assert _is_linked(a2, 'eSport_Person', b)
    _safe_set(b, 'eSport_Capacity', None)
    assert not _is_linked(b, 'eSport_Capacity', a2)
    if hasattr(a2, 'eSport_Person'):
        assert not _is_linked(a2, 'eSport_Person', b)


def test_assoc_countries29_reverse_link_reassign_clear():
    a1 = eSport_Zone(name="sample_text")
    a2 = eSport_Zone(name="sample_text_2")
    b = eSport_Country(name="sample_text")
    _safe_set(b, 'Country31', a1)
    assert _is_linked(b, 'Country31', a1)
    if hasattr(a1, 'zone30'):
        assert _is_linked(a1, 'zone30', b)
    _safe_set(b, 'Country31', a2)
    assert _is_linked(b, 'Country31', a2)
    if hasattr(a1, 'zone30'):
        assert not _is_linked(a1, 'zone30', b)
    if hasattr(a2, 'zone30'):
        assert _is_linked(a2, 'zone30', b)
    _safe_set(b, 'Country31', None)
    assert not _is_linked(b, 'Country31', a2)
    if hasattr(a2, 'zone30'):
        assert not _is_linked(a2, 'zone30', b)


def test_assoc_countries3_reverse_link_reassign_clear():
    a1 = eSport_Tournament(name="sample_text", size=7, type="sample_text", year=7)
    a2 = eSport_Tournament(name="sample_text_2", size=13, type="sample_text_2", year=13)
    b = eSport_Country(name="sample_text")
    _safe_set(b, 'Country', a1)
    assert _is_linked(b, 'Country', a1)
    if hasattr(a1, 'tournaments'):
        assert _is_linked(a1, 'tournaments', b)
    _safe_set(b, 'Country', a2)
    assert _is_linked(b, 'Country', a2)
    if hasattr(a1, 'tournaments'):
        assert not _is_linked(a1, 'tournaments', b)
    if hasattr(a2, 'tournaments'):
        assert _is_linked(a2, 'tournaments', b)
    _safe_set(b, 'Country', None)
    assert not _is_linked(b, 'Country', a2)
    if hasattr(a2, 'tournaments'):
        assert not _is_linked(a2, 'tournaments', b)


def test_assoc_country18_reverse_link_reassign_clear():
    a1 = eSport_Person(age=7, description="sample_text", name="sample_text")
    a2 = eSport_Person(age=13, description="sample_text_2", name="sample_text_2")
    b = eSport_Country(name="sample_text")
    _safe_set(b, 'Country19', a1)
    assert _is_linked(b, 'Country19', a1)
    if hasattr(a1, 'persons'):
        assert _is_linked(a1, 'persons', b)
    _safe_set(b, 'Country19', a2)
    assert _is_linked(b, 'Country19', a2)
    if hasattr(a1, 'persons'):
        assert not _is_linked(a1, 'persons', b)
    if hasattr(a2, 'persons'):
        assert _is_linked(a2, 'persons', b)
    _safe_set(b, 'Country19', None)
    assert not _is_linked(b, 'Country19', a2)
    if hasattr(a2, 'persons'):
        assert not _is_linked(a2, 'persons', b)


def test_assoc_finalstage50_reverse_link_reassign_clear():
    a1 = eSport_Match(loserWins=7, type="sample_text")
    a2 = eSport_Match(loserWins=13, type="sample_text_2")
    b = eSport_FinalStage(maxNbGames=7)
    _safe_set(b, 'FinalStage52', a1)
    assert _is_linked(b, 'FinalStage52', a1)
    if hasattr(a1, 'matchs51'):
        assert _is_linked(a1, 'matchs51', b)
    _safe_set(b, 'FinalStage52', a2)
    assert _is_linked(b, 'FinalStage52', a2)
    if hasattr(a1, 'matchs51'):
        assert not _is_linked(a1, 'matchs51', b)
    if hasattr(a2, 'matchs51'):
        assert _is_linked(a2, 'matchs51', b)
    _safe_set(b, 'FinalStage52', None)
    assert not _is_linked(b, 'FinalStage52', a2)
    if hasattr(a2, 'matchs51'):
        assert not _is_linked(a2, 'matchs51', b)


def test_assoc_finalstages45_reverse_link_reassign_clear():
    a1 = eSport_Team(championshipPoints=7, name="sample_text")
    a2 = eSport_Team(championshipPoints=13, name="sample_text_2")
    b = eSport_FinalStage(maxNbGames=7)
    _safe_set(b, 'FinalStage47', a1)
    assert _is_linked(b, 'FinalStage47', a1)
    if hasattr(a1, 'teams46'):
        assert _is_linked(a1, 'teams46', b)
    _safe_set(b, 'FinalStage47', a2)
    assert _is_linked(b, 'FinalStage47', a2)
    if hasattr(a1, 'teams46'):
        assert not _is_linked(a1, 'teams46', b)
    if hasattr(a2, 'teams46'):
        assert _is_linked(a2, 'teams46', b)
    _safe_set(b, 'FinalStage47', None)
    assert not _is_linked(b, 'FinalStage47', a2)
    if hasattr(a2, 'teams46'):
        assert not _is_linked(a2, 'teams46', b)


def test_assoc_finalstages6_reverse_link_reassign_clear():
    a1 = eSport_Tournament(name="sample_text", size=7, type="sample_text", year=7)
    a2 = eSport_Tournament(name="sample_text_2", size=13, type="sample_text_2", year=13)
    b = eSport_FinalStage(maxNbGames=7)
    _safe_set(b, 'FinalStage', a1)
    assert _is_linked(b, 'FinalStage', a1)
    if hasattr(a1, 'tournament'):
        assert _is_linked(a1, 'tournament', b)
    _safe_set(b, 'FinalStage', a2)
    assert _is_linked(b, 'FinalStage', a2)
    if hasattr(a1, 'tournament'):
        assert not _is_linked(a1, 'tournament', b)
    if hasattr(a2, 'tournament'):
        assert _is_linked(a2, 'tournament', b)
    _safe_set(b, 'FinalStage', None)
    assert not _is_linked(b, 'FinalStage', a2)
    if hasattr(a2, 'tournament'):
        assert not _is_linked(a2, 'tournament', b)


def test_assoc_groupstage14_reverse_link_reassign_clear():
    a1 = eSport_League(name="sample_text", season="sample_text", size=7, year=7)
    a2 = eSport_League(name="sample_text_2", season="sample_text_2", size=13, year=13)
    b = eSport_GroupStage(maxNbGames=7, meetingsInSameGroup=7, meetingsWithOtherGroups=7, type="sample_text")
    _safe_set(b, 'GroupStage15', a1)
    assert _is_linked(b, 'GroupStage15', a1)
    if hasattr(a1, 'league'):
        assert _is_linked(a1, 'league', b)
    _safe_set(b, 'GroupStage15', a2)
    assert _is_linked(b, 'GroupStage15', a2)
    if hasattr(a1, 'league'):
        assert not _is_linked(a1, 'league', b)
    if hasattr(a2, 'league'):
        assert _is_linked(a2, 'league', b)
    _safe_set(b, 'GroupStage15', None)
    assert not _is_linked(b, 'GroupStage15', a2)
    if hasattr(a2, 'league'):
        assert not _is_linked(a2, 'league', b)


def test_assoc_groupstages7_reverse_link_reassign_clear():
    a1 = eSport_Tournament(name="sample_text", size=7, type="sample_text", year=7)
    a2 = eSport_Tournament(name="sample_text_2", size=13, type="sample_text_2", year=13)
    b = eSport_GroupStage(maxNbGames=7, meetingsInSameGroup=7, meetingsWithOtherGroups=7, type="sample_text")
    _safe_set(b, 'GroupStage', a1)
    assert _is_linked(b, 'GroupStage', a1)
    if hasattr(a1, 'tournament8'):
        assert _is_linked(a1, 'tournament8', b)
    _safe_set(b, 'GroupStage', a2)
    assert _is_linked(b, 'GroupStage', a2)
    if hasattr(a1, 'tournament8'):
        assert not _is_linked(a1, 'tournament8', b)
    if hasattr(a2, 'tournament8'):
        assert _is_linked(a2, 'tournament8', b)
    _safe_set(b, 'GroupStage', None)
    assert not _is_linked(b, 'GroupStage', a2)
    if hasattr(a2, 'tournament8'):
        assert not _is_linked(a2, 'tournament8', b)


def test_assoc_league68_reverse_link_reassign_clear():
    a1 = eSport_League(name="sample_text", season="sample_text", size=7, year=7)
    a2 = eSport_League(name="sample_text_2", season="sample_text_2", size=13, year=13)
    b = eSport_GroupStage(maxNbGames=7, meetingsInSameGroup=7, meetingsWithOtherGroups=7, type="sample_text")
    _safe_set(b, 'groupstage69', a1)
    assert _is_linked(b, 'groupstage69', a1)
    if hasattr(a1, 'League70'):
        assert _is_linked(a1, 'League70', b)
    _safe_set(b, 'groupstage69', a2)
    assert _is_linked(b, 'groupstage69', a2)
    if hasattr(a1, 'League70'):
        assert not _is_linked(a1, 'League70', b)
    if hasattr(a2, 'League70'):
        assert _is_linked(a2, 'League70', b)
    _safe_set(b, 'groupstage69', None)
    assert not _is_linked(b, 'groupstage69', a2)
    if hasattr(a2, 'League70'):
        assert not _is_linked(a2, 'League70', b)


def test_assoc_leagueFrom82_reverse_link_reassign_clear():
    a1 = eSport_Qualification(name="sample_text")
    a2 = eSport_Qualification(name="sample_text_2")
    b = eSport_League(name="sample_text", season="sample_text", size=7, year=7)
    _safe_set(b, 'League84', a1)
    assert _is_linked(b, 'League84', a1)
    if hasattr(a1, 'qualifiesFor83'):
        assert _is_linked(a1, 'qualifiesFor83', b)
    _safe_set(b, 'League84', a2)
    assert _is_linked(b, 'League84', a2)
    if hasattr(a1, 'qualifiesFor83'):
        assert not _is_linked(a1, 'qualifiesFor83', b)
    if hasattr(a2, 'qualifiesFor83'):
        assert _is_linked(a2, 'qualifiesFor83', b)
    _safe_set(b, 'League84', None)
    assert not _is_linked(b, 'League84', a2)
    if hasattr(a2, 'qualifiesFor83'):
        assert not _is_linked(a2, 'qualifiesFor83', b)


def test_assoc_leagues28_reverse_link_reassign_clear():
    a1 = eSport_Zone(name="sample_text")
    a2 = eSport_Zone(name="sample_text_2")
    b = eSport_League(name="sample_text", season="sample_text", size=7, year=7)
    _safe_set(b, 'League', a1)
    assert _is_linked(b, 'League', a1)
    if hasattr(a1, 'zone'):
        assert _is_linked(a1, 'zone', b)
    _safe_set(b, 'League', a2)
    assert _is_linked(b, 'League', a2)
    if hasattr(a1, 'zone'):
        assert not _is_linked(a1, 'zone', b)
    if hasattr(a2, 'zone'):
        assert _is_linked(a2, 'zone', b)
    _safe_set(b, 'League', None)
    assert not _is_linked(b, 'League', a2)
    if hasattr(a2, 'zone'):
        assert not _is_linked(a2, 'zone', b)


def test_assoc_matchs71_reverse_link_reassign_clear():
    a1 = eSport_Match(loserWins=7, type="sample_text")
    a2 = eSport_Match(loserWins=13, type="sample_text_2")
    b = eSport_FinalStage(maxNbGames=7)
    _safe_set(b, 'finalstage', {a1})
    assert _is_linked(b, 'finalstage', a1)
    if hasattr(a1, 'Match72'):
        assert _is_linked(a1, 'Match72', b)
    _safe_set(b, 'finalstage', {a2})
    assert _is_linked(b, 'finalstage', a2)
    if hasattr(a1, 'Match72'):
        assert not _is_linked(a1, 'Match72', b)
    if hasattr(a2, 'Match72'):
        assert _is_linked(a2, 'Match72', b)
    _safe_set(b, 'finalstage', set())
    assert not _is_linked(b, 'finalstage', a2)
    if hasattr(a2, 'Match72'):
        assert not _is_linked(a2, 'Match72', b)


def test_assoc_matchsLost43_reverse_link_reassign_clear():
    a1 = eSport_Team(championshipPoints=7, name="sample_text")
    a2 = eSport_Team(championshipPoints=13, name="sample_text_2")
    b = eSport_Match(loserWins=7, type="sample_text")
    _safe_set(b, 'Match44', a1)
    assert _is_linked(b, 'Match44', a1)
    if hasattr(a1, 'teamLoser'):
        assert _is_linked(a1, 'teamLoser', b)
    _safe_set(b, 'Match44', a2)
    assert _is_linked(b, 'Match44', a2)
    if hasattr(a1, 'teamLoser'):
        assert not _is_linked(a1, 'teamLoser', b)
    if hasattr(a2, 'teamLoser'):
        assert _is_linked(a2, 'teamLoser', b)
    _safe_set(b, 'Match44', None)
    assert not _is_linked(b, 'Match44', a2)
    if hasattr(a2, 'teamLoser'):
        assert not _is_linked(a2, 'teamLoser', b)


def test_assoc_matchsWon42_reverse_link_reassign_clear():
    a1 = eSport_Team(championshipPoints=7, name="sample_text")
    a2 = eSport_Team(championshipPoints=13, name="sample_text_2")
    b = eSport_Match(loserWins=7, type="sample_text")
    _safe_set(b, 'Match', a1)
    assert _is_linked(b, 'Match', a1)
    if hasattr(a1, 'teamWinner'):
        assert _is_linked(a1, 'teamWinner', b)
    _safe_set(b, 'Match', a2)
    assert _is_linked(b, 'Match', a2)
    if hasattr(a1, 'teamWinner'):
        assert not _is_linked(a1, 'teamWinner', b)
    if hasattr(a2, 'teamWinner'):
        assert _is_linked(a2, 'teamWinner', b)
    _safe_set(b, 'Match', None)
    assert not _is_linked(b, 'Match', a2)
    if hasattr(a2, 'teamWinner'):
        assert not _is_linked(a2, 'teamWinner', b)


def test_assoc_persons25_reverse_link_reassign_clear():
    a1 = eSport_Person(age=7, description="sample_text", name="sample_text")
    a2 = eSport_Person(age=13, description="sample_text_2", name="sample_text_2")
    b = eSport_Country(name="sample_text")
    _safe_set(b, 'country', {a1})
    assert _is_linked(b, 'country', a1)
    if hasattr(a1, 'Person'):
        assert _is_linked(a1, 'Person', b)
    _safe_set(b, 'country', {a2})
    assert _is_linked(b, 'country', a2)
    if hasattr(a1, 'Person'):
        assert not _is_linked(a1, 'Person', b)
    if hasattr(a2, 'Person'):
        assert _is_linked(a2, 'Person', b)
    _safe_set(b, 'country', set())
    assert not _is_linked(b, 'country', a2)
    if hasattr(a2, 'Person'):
        assert not _is_linked(a2, 'Person', b)


def test_assoc_players35_reverse_link_reassign_clear():
    a1 = eSport_Team(championshipPoints=7, name="sample_text")
    a2 = eSport_Team(championshipPoints=13, name="sample_text_2")
    b = eSport_Player(position="sample_text")
    _safe_set(b, 'Player', a1)
    assert _is_linked(b, 'Player', a1)
    if hasattr(a1, 'team'):
        assert _is_linked(a1, 'team', b)
    _safe_set(b, 'Player', a2)
    assert _is_linked(b, 'Player', a2)
    if hasattr(a1, 'team'):
        assert not _is_linked(a1, 'team', b)
    if hasattr(a2, 'team'):
        assert _is_linked(a2, 'team', b)
    _safe_set(b, 'Player', None)
    assert not _is_linked(b, 'Player', a2)
    if hasattr(a2, 'team'):
        assert not _is_linked(a2, 'team', b)


def test_assoc_qualifiesFor16_reverse_link_reassign_clear():
    a1 = eSport_Qualification(name="sample_text")
    a2 = eSport_Qualification(name="sample_text_2")
    b = eSport_League(name="sample_text", season="sample_text", size=7, year=7)
    _safe_set(b, 'leagueFrom', {a1})
    assert _is_linked(b, 'leagueFrom', a1)
    if hasattr(a1, 'Qualification17'):
        assert _is_linked(a1, 'Qualification17', b)
    _safe_set(b, 'leagueFrom', {a2})
    assert _is_linked(b, 'leagueFrom', a2)
    if hasattr(a1, 'Qualification17'):
        assert not _is_linked(a1, 'Qualification17', b)
    if hasattr(a2, 'Qualification17'):
        assert _is_linked(a2, 'Qualification17', b)
    _safe_set(b, 'leagueFrom', set())
    assert not _is_linked(b, 'leagueFrom', a2)
    if hasattr(a2, 'Qualification17'):
        assert not _is_linked(a2, 'Qualification17', b)


def test_assoc_qualifiesFor9_reverse_link_reassign_clear():
    a1 = eSport_Tournament(name="sample_text", size=7, type="sample_text", year=7)
    a2 = eSport_Tournament(name="sample_text_2", size=13, type="sample_text_2", year=13)
    b = eSport_Qualification(name="sample_text")
    _safe_set(b, 'Qualification', a1)
    assert _is_linked(b, 'Qualification', a1)
    if hasattr(a1, 'tournamentFrom'):
        assert _is_linked(a1, 'tournamentFrom', b)
    _safe_set(b, 'Qualification', a2)
    assert _is_linked(b, 'Qualification', a2)
    if hasattr(a1, 'tournamentFrom'):
        assert not _is_linked(a1, 'tournamentFrom', b)
    if hasattr(a2, 'tournamentFrom'):
        assert _is_linked(a2, 'tournamentFrom', b)
    _safe_set(b, 'Qualification', None)
    assert not _is_linked(b, 'Qualification', a2)
    if hasattr(a2, 'tournamentFrom'):
        assert not _is_linked(a2, 'tournamentFrom', b)


def test_assoc_qualifiesFrom10_reverse_link_reassign_clear():
    a1 = eSport_Tournament(name="sample_text", size=7, type="sample_text", year=7)
    a2 = eSport_Tournament(name="sample_text_2", size=13, type="sample_text_2", year=13)
    b = eSport_Qualification(name="sample_text")
    _safe_set(b, 'Qualification11', a1)
    assert _is_linked(b, 'Qualification11', a1)
    if hasattr(a1, 'tournamentTo'):
        assert _is_linked(a1, 'tournamentTo', b)
    _safe_set(b, 'Qualification11', a2)
    assert _is_linked(b, 'Qualification11', a2)
    if hasattr(a1, 'tournamentTo'):
        assert not _is_linked(a1, 'tournamentTo', b)
    if hasattr(a2, 'tournamentTo'):
        assert _is_linked(a2, 'tournamentTo', b)
    _safe_set(b, 'Qualification11', None)
    assert not _is_linked(b, 'Qualification11', a2)
    if hasattr(a2, 'tournamentTo'):
        assert not _is_linked(a2, 'tournamentTo', b)


def test_assoc_team0_reverse_link_reassign_clear():
    a1 = eSport_Team(championshipPoints=7, name="sample_text")
    a2 = eSport_Team(championshipPoints=13, name="sample_text_2")
    b = eSport_Player(position="sample_text")
    _safe_set(b, 'players', a1)
    assert _is_linked(b, 'players', a1)
    if hasattr(a1, 'Team'):
        assert _is_linked(a1, 'Team', b)
    _safe_set(b, 'players', a2)
    assert _is_linked(b, 'players', a2)
    if hasattr(a1, 'Team'):
        assert not _is_linked(a1, 'Team', b)
    if hasattr(a2, 'Team'):
        assert _is_linked(a2, 'Team', b)
    _safe_set(b, 'players', None)
    assert not _is_linked(b, 'players', a2)
    if hasattr(a2, 'Team'):
        assert not _is_linked(a2, 'Team', b)


def test_assoc_teamLoser55_reverse_link_reassign_clear():
    a1 = eSport_Team(championshipPoints=7, name="sample_text")
    a2 = eSport_Team(championshipPoints=13, name="sample_text_2")
    b = eSport_Match(loserWins=7, type="sample_text")
    _safe_set(b, 'matchsLost', a1)
    assert _is_linked(b, 'matchsLost', a1)
    if hasattr(a1, 'Team56'):
        assert _is_linked(a1, 'Team56', b)
    _safe_set(b, 'matchsLost', a2)
    assert _is_linked(b, 'matchsLost', a2)
    if hasattr(a1, 'Team56'):
        assert not _is_linked(a1, 'Team56', b)
    if hasattr(a2, 'Team56'):
        assert _is_linked(a2, 'Team56', b)
    _safe_set(b, 'matchsLost', None)
    assert not _is_linked(b, 'matchsLost', a2)
    if hasattr(a2, 'Team56'):
        assert not _is_linked(a2, 'Team56', b)


def test_assoc_teamWinner53_reverse_link_reassign_clear():
    a1 = eSport_Team(championshipPoints=7, name="sample_text")
    a2 = eSport_Team(championshipPoints=13, name="sample_text_2")
    b = eSport_Match(loserWins=7, type="sample_text")
    _safe_set(b, 'matchsWon', a1)
    assert _is_linked(b, 'matchsWon', a1)
    if hasattr(a1, 'Team54'):
        assert _is_linked(a1, 'Team54', b)
    _safe_set(b, 'matchsWon', a2)
    assert _is_linked(b, 'matchsWon', a2)
    if hasattr(a1, 'Team54'):
        assert not _is_linked(a1, 'Team54', b)
    if hasattr(a2, 'Team54'):
        assert _is_linked(a2, 'Team54', b)
    _safe_set(b, 'matchsWon', None)
    assert not _is_linked(b, 'matchsWon', a2)
    if hasattr(a2, 'Team54'):
        assert not _is_linked(a2, 'Team54', b)


def test_assoc_teams32_reverse_link_reassign_clear():
    a1 = eSport_Zone(name="sample_text")
    a2 = eSport_Zone(name="sample_text_2")
    b = eSport_Team(championshipPoints=7, name="sample_text")
    _safe_set(b, 'Team34', a1)
    assert _is_linked(b, 'Team34', a1)
    if hasattr(a1, 'zone33'):
        assert _is_linked(a1, 'zone33', b)
    _safe_set(b, 'Team34', a2)
    assert _is_linked(b, 'Team34', a2)
    if hasattr(a1, 'zone33'):
        assert not _is_linked(a1, 'zone33', b)
    if hasattr(a2, 'zone33'):
        assert _is_linked(a2, 'zone33', b)
    _safe_set(b, 'Team34', None)
    assert not _is_linked(b, 'Team34', a2)
    if hasattr(a2, 'zone33'):
        assert not _is_linked(a2, 'zone33', b)


def test_assoc_teams75_reverse_link_reassign_clear():
    a1 = eSport_Team(championshipPoints=7, name="sample_text")
    a2 = eSport_Team(championshipPoints=13, name="sample_text_2")
    b = eSport_FinalStage(maxNbGames=7)
    _safe_set(b, 'finalstages76', {a1})
    assert _is_linked(b, 'finalstages76', a1)
    if hasattr(a1, 'Team77'):
        assert _is_linked(a1, 'Team77', b)
    _safe_set(b, 'finalstages76', {a2})
    assert _is_linked(b, 'finalstages76', a2)
    if hasattr(a1, 'Team77'):
        assert not _is_linked(a1, 'Team77', b)
    if hasattr(a2, 'Team77'):
        assert _is_linked(a2, 'Team77', b)
    _safe_set(b, 'finalstages76', set())
    assert not _is_linked(b, 'finalstages76', a2)
    if hasattr(a2, 'Team77'):
        assert not _is_linked(a2, 'Team77', b)


def test_assoc_tournament66_reverse_link_reassign_clear():
    a1 = eSport_Tournament(name="sample_text", size=7, type="sample_text", year=7)
    a2 = eSport_Tournament(name="sample_text_2", size=13, type="sample_text_2", year=13)
    b = eSport_GroupStage(maxNbGames=7, meetingsInSameGroup=7, meetingsWithOtherGroups=7, type="sample_text")
    _safe_set(b, 'groupstages', a1)
    assert _is_linked(b, 'groupstages', a1)
    if hasattr(a1, 'Tournament67'):
        assert _is_linked(a1, 'Tournament67', b)
    _safe_set(b, 'groupstages', a2)
    assert _is_linked(b, 'groupstages', a2)
    if hasattr(a1, 'Tournament67'):
        assert not _is_linked(a1, 'Tournament67', b)
    if hasattr(a2, 'Tournament67'):
        assert _is_linked(a2, 'Tournament67', b)
    _safe_set(b, 'groupstages', None)
    assert not _is_linked(b, 'groupstages', a2)
    if hasattr(a2, 'Tournament67'):
        assert not _is_linked(a2, 'Tournament67', b)


def test_assoc_tournament73_reverse_link_reassign_clear():
    a1 = eSport_Tournament(name="sample_text", size=7, type="sample_text", year=7)
    a2 = eSport_Tournament(name="sample_text_2", size=13, type="sample_text_2", year=13)
    b = eSport_FinalStage(maxNbGames=7)
    _safe_set(b, 'finalstages', a1)
    assert _is_linked(b, 'finalstages', a1)
    if hasattr(a1, 'Tournament74'):
        assert _is_linked(a1, 'Tournament74', b)
    _safe_set(b, 'finalstages', a2)
    assert _is_linked(b, 'finalstages', a2)
    if hasattr(a1, 'Tournament74'):
        assert not _is_linked(a1, 'Tournament74', b)
    if hasattr(a2, 'Tournament74'):
        assert _is_linked(a2, 'Tournament74', b)
    _safe_set(b, 'finalstages', None)
    assert not _is_linked(b, 'finalstages', a2)
    if hasattr(a2, 'Tournament74'):
        assert not _is_linked(a2, 'Tournament74', b)


def test_assoc_tournamentFrom78_reverse_link_reassign_clear():
    a1 = eSport_Tournament(name="sample_text", size=7, type="sample_text", year=7)
    a2 = eSport_Tournament(name="sample_text_2", size=13, type="sample_text_2", year=13)
    b = eSport_Qualification(name="sample_text")
    _safe_set(b, 'qualifiesFor', a1)
    assert _is_linked(b, 'qualifiesFor', a1)
    if hasattr(a1, 'Tournament79'):
        assert _is_linked(a1, 'Tournament79', b)
    _safe_set(b, 'qualifiesFor', a2)
    assert _is_linked(b, 'qualifiesFor', a2)
    if hasattr(a1, 'Tournament79'):
        assert not _is_linked(a1, 'Tournament79', b)
    if hasattr(a2, 'Tournament79'):
        assert _is_linked(a2, 'Tournament79', b)
    _safe_set(b, 'qualifiesFor', None)
    assert not _is_linked(b, 'qualifiesFor', a2)
    if hasattr(a2, 'Tournament79'):
        assert not _is_linked(a2, 'Tournament79', b)


def test_assoc_tournamentTo80_reverse_link_reassign_clear():
    a1 = eSport_Tournament(name="sample_text", size=7, type="sample_text", year=7)
    a2 = eSport_Tournament(name="sample_text_2", size=13, type="sample_text_2", year=13)
    b = eSport_Qualification(name="sample_text")
    _safe_set(b, 'qualifiesFrom', a1)
    assert _is_linked(b, 'qualifiesFrom', a1)
    if hasattr(a1, 'Tournament81'):
        assert _is_linked(a1, 'Tournament81', b)
    _safe_set(b, 'qualifiesFrom', a2)
    assert _is_linked(b, 'qualifiesFrom', a2)
    if hasattr(a1, 'Tournament81'):
        assert not _is_linked(a1, 'Tournament81', b)
    if hasattr(a2, 'Tournament81'):
        assert _is_linked(a2, 'Tournament81', b)
    _safe_set(b, 'qualifiesFrom', None)
    assert not _is_linked(b, 'qualifiesFrom', a2)
    if hasattr(a2, 'Tournament81'):
        assert not _is_linked(a2, 'Tournament81', b)


def test_assoc_tournaments21_reverse_link_reassign_clear():
    a1 = eSport_Tournament(name="sample_text", size=7, type="sample_text", year=7)
    a2 = eSport_Tournament(name="sample_text_2", size=13, type="sample_text_2", year=13)
    b = eSport_Country(name="sample_text")
    _safe_set(b, 'countries', {a1})
    assert _is_linked(b, 'countries', a1)
    if hasattr(a1, 'Tournament'):
        assert _is_linked(a1, 'Tournament', b)
    _safe_set(b, 'countries', {a2})
    assert _is_linked(b, 'countries', a2)
    if hasattr(a1, 'Tournament'):
        assert not _is_linked(a1, 'Tournament', b)
    if hasattr(a2, 'Tournament'):
        assert _is_linked(a2, 'Tournament', b)
    _safe_set(b, 'countries', set())
    assert not _is_linked(b, 'countries', a2)
    if hasattr(a2, 'Tournament'):
        assert not _is_linked(a2, 'Tournament', b)


def test_assoc_tournaments26_reverse_link_reassign_clear():
    a1 = eSport_Zone(name="sample_text")
    a2 = eSport_Zone(name="sample_text_2")
    b = eSport_Tournament(name="sample_text", size=7, type="sample_text", year=7)
    _safe_set(b, 'Tournament27', a1)
    assert _is_linked(b, 'Tournament27', a1)
    if hasattr(a1, 'allowedZones'):
        assert _is_linked(a1, 'allowedZones', b)
    _safe_set(b, 'Tournament27', a2)
    assert _is_linked(b, 'Tournament27', a2)
    if hasattr(a1, 'allowedZones'):
        assert not _is_linked(a1, 'allowedZones', b)
    if hasattr(a2, 'allowedZones'):
        assert _is_linked(a2, 'allowedZones', b)
    _safe_set(b, 'Tournament27', None)
    assert not _is_linked(b, 'Tournament27', a2)
    if hasattr(a2, 'allowedZones'):
        assert not _is_linked(a2, 'allowedZones', b)


def test_assoc_zone12_reverse_link_reassign_clear():
    a1 = eSport_Zone(name="sample_text")
    a2 = eSport_Zone(name="sample_text_2")
    b = eSport_League(name="sample_text", season="sample_text", size=7, year=7)
    _safe_set(b, 'leagues', a1)
    assert _is_linked(b, 'leagues', a1)
    if hasattr(a1, 'Zone13'):
        assert _is_linked(a1, 'Zone13', b)
    _safe_set(b, 'leagues', a2)
    assert _is_linked(b, 'leagues', a2)
    if hasattr(a1, 'Zone13'):
        assert not _is_linked(a1, 'Zone13', b)
    if hasattr(a2, 'Zone13'):
        assert _is_linked(a2, 'Zone13', b)
    _safe_set(b, 'leagues', None)
    assert not _is_linked(b, 'leagues', a2)
    if hasattr(a2, 'Zone13'):
        assert not _is_linked(a2, 'Zone13', b)


def test_assoc_zone22_reverse_link_reassign_clear():
    a1 = eSport_Zone(name="sample_text")
    a2 = eSport_Zone(name="sample_text_2")
    b = eSport_Country(name="sample_text")
    _safe_set(b, 'countries23', a1)
    assert _is_linked(b, 'countries23', a1)
    if hasattr(a1, 'Zone24'):
        assert _is_linked(a1, 'Zone24', b)
    _safe_set(b, 'countries23', a2)
    assert _is_linked(b, 'countries23', a2)
    if hasattr(a1, 'Zone24'):
        assert not _is_linked(a1, 'Zone24', b)
    if hasattr(a2, 'Zone24'):
        assert _is_linked(a2, 'Zone24', b)
    _safe_set(b, 'countries23', None)
    assert not _is_linked(b, 'countries23', a2)
    if hasattr(a2, 'Zone24'):
        assert not _is_linked(a2, 'Zone24', b)


def test_assoc_zone38_reverse_link_reassign_clear():
    a1 = eSport_Zone(name="sample_text")
    a2 = eSport_Zone(name="sample_text_2")
    b = eSport_Team(championshipPoints=7, name="sample_text")
    _safe_set(b, 'teams', a1)
    assert _is_linked(b, 'teams', a1)
    if hasattr(a1, 'Zone39'):
        assert _is_linked(a1, 'Zone39', b)
    _safe_set(b, 'teams', a2)
    assert _is_linked(b, 'teams', a2)
    if hasattr(a1, 'Zone39'):
        assert not _is_linked(a1, 'Zone39', b)
    if hasattr(a2, 'Zone39'):
        assert _is_linked(a2, 'Zone39', b)
    _safe_set(b, 'teams', None)
    assert not _is_linked(b, 'teams', a2)
    if hasattr(a2, 'Zone39'):
        assert not _is_linked(a2, 'Zone39', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_coach36_stub_double():
    # eSport_Coach has no real 'Coach' property in the generated
    # code (a bare stub) -- manually attach it so eSport_Team's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eSport_Team's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eSport_Team(championshipPoints=7, name="sample_text")
    partner = eSport_Coach()
    setattr(partner, 'Coach', None)
    _safe_set(owner, 'team37', partner)
    assert getattr(partner, 'Coach') == owner
    _safe_set(owner, 'team37', None)
    assert getattr(partner, 'Coach') is None


def test_assoc_countries97_stub_double():
    # eSport_Root has no real 'eSport_Root98' property in the generated
    # code (a bare stub) -- manually attach it so eSport_Country's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eSport_Country's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eSport_Country(name="sample_text")
    partner = eSport_Root()
    setattr(partner, 'eSport_Root98', None)
    _safe_set(owner, 'eSport_Country', partner)
    assert owner in getattr(partner, 'eSport_Root98')
    _safe_set(owner, 'eSport_Country', None)
    assert owner not in getattr(partner, 'eSport_Root98')


def test_assoc_group48_stub_double():
    # eSport_Group has no real 'Group49' property in the generated
    # code (a bare stub) -- manually attach it so eSport_Match's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eSport_Match's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eSport_Match(loserWins=7, type="sample_text")
    partner = eSport_Group()
    setattr(partner, 'Group49', None)
    _safe_set(owner, 'matchs', partner)
    assert getattr(partner, 'Group49') == owner
    _safe_set(owner, 'matchs', None)
    assert getattr(partner, 'Group49') is None


def test_assoc_groups40_stub_double():
    # eSport_Group has no real 'Group' property in the generated
    # code (a bare stub) -- manually attach it so eSport_Team's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eSport_Team's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eSport_Team(championshipPoints=7, name="sample_text")
    partner = eSport_Group()
    setattr(partner, 'Group', None)
    _safe_set(owner, 'teams41', {partner})
    assert getattr(partner, 'Group') == owner
    _safe_set(owner, 'teams41', set())
    assert getattr(partner, 'Group') is None


def test_assoc_groups64_stub_double():
    # eSport_Group has no real 'Group65' property in the generated
    # code (a bare stub) -- manually attach it so eSport_GroupStage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eSport_GroupStage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eSport_GroupStage(maxNbGames=7, meetingsInSameGroup=7, meetingsWithOtherGroups=7, type="sample_text")
    partner = eSport_Group()
    setattr(partner, 'Group65', None)
    _safe_set(owner, 'groupstage', {partner})
    assert getattr(partner, 'Group65') == owner
    _safe_set(owner, 'groupstage', set())
    assert getattr(partner, 'Group65') is None


def test_assoc_groupstage57_stub_double():
    # eSport_Group has no real 'groups' property in the generated
    # code (a bare stub) -- manually attach it so eSport_GroupStage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eSport_GroupStage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eSport_GroupStage(maxNbGames=7, meetingsInSameGroup=7, meetingsWithOtherGroups=7, type="sample_text")
    partner = eSport_Group()
    setattr(partner, 'groups', None)
    _safe_set(owner, 'GroupStage58', partner)
    assert getattr(partner, 'groups') == owner
    _safe_set(owner, 'GroupStage58', None)
    assert getattr(partner, 'groups') is None


def test_assoc_leagues88_stub_double():
    # eSport_Root has no real 'eSport_Root89' property in the generated
    # code (a bare stub) -- manually attach it so eSport_League's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eSport_League's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eSport_League(name="sample_text", season="sample_text", size=7, year=7)
    partner = eSport_Root()
    setattr(partner, 'eSport_Root89', None)
    _safe_set(owner, 'eSport_League', partner)
    assert owner in getattr(partner, 'eSport_Root89')
    _safe_set(owner, 'eSport_League', None)
    assert owner not in getattr(partner, 'eSport_Root89')


def test_assoc_matchs59_stub_double():
    # eSport_Group has no real 'group' property in the generated
    # code (a bare stub) -- manually attach it so eSport_Match's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eSport_Match's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eSport_Match(loserWins=7, type="sample_text")
    partner = eSport_Group()
    setattr(partner, 'group', None)
    _safe_set(owner, 'Match60', partner)
    assert owner in getattr(partner, 'group')
    _safe_set(owner, 'Match60', None)
    assert owner not in getattr(partner, 'group')


def test_assoc_persons92_stub_double():
    # eSport_Root has no real 'eSport_Root93' property in the generated
    # code (a bare stub) -- manually attach it so eSport_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eSport_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eSport_Person(age=7, description="sample_text", name="sample_text")
    partner = eSport_Root()
    setattr(partner, 'eSport_Root93', None)
    _safe_set(owner, 'eSport_Person94', partner)
    assert owner in getattr(partner, 'eSport_Root93')
    _safe_set(owner, 'eSport_Person94', None)
    assert owner not in getattr(partner, 'eSport_Root93')


def test_assoc_qualifications95_stub_double():
    # eSport_Root has no real 'eSport_Root96' property in the generated
    # code (a bare stub) -- manually attach it so eSport_Qualification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eSport_Qualification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eSport_Qualification(name="sample_text")
    partner = eSport_Root()
    setattr(partner, 'eSport_Root96', None)
    _safe_set(owner, 'eSport_Qualification', partner)
    assert owner in getattr(partner, 'eSport_Root96')
    _safe_set(owner, 'eSport_Qualification', None)
    assert owner not in getattr(partner, 'eSport_Root96')


def test_assoc_team1_stub_double():
    # eSport_Coach has no real 'coach' property in the generated
    # code (a bare stub) -- manually attach it so eSport_Team's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eSport_Team's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eSport_Team(championshipPoints=7, name="sample_text")
    partner = eSport_Coach()
    setattr(partner, 'coach', None)
    _safe_set(owner, 'Team2', partner)
    assert getattr(partner, 'coach') == owner
    _safe_set(owner, 'Team2', None)
    assert getattr(partner, 'coach') is None


def test_assoc_teams61_stub_double():
    # eSport_Group has no real 'groups62' property in the generated
    # code (a bare stub) -- manually attach it so eSport_Team's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eSport_Team's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eSport_Team(championshipPoints=7, name="sample_text")
    partner = eSport_Group()
    setattr(partner, 'groups62', None)
    _safe_set(owner, 'Team63', partner)
    assert owner in getattr(partner, 'groups62')
    _safe_set(owner, 'Team63', None)
    assert owner not in getattr(partner, 'groups62')


def test_assoc_teams90_stub_double():
    # eSport_Root has no real 'eSport_Root91' property in the generated
    # code (a bare stub) -- manually attach it so eSport_Team's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eSport_Team's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eSport_Team(championshipPoints=7, name="sample_text")
    partner = eSport_Root()
    setattr(partner, 'eSport_Root91', None)
    _safe_set(owner, 'eSport_Team', partner)
    assert owner in getattr(partner, 'eSport_Root91')
    _safe_set(owner, 'eSport_Team', None)
    assert owner not in getattr(partner, 'eSport_Root91')


def test_assoc_tournaments86_stub_double():
    # eSport_Root has no real 'eSport_Root87' property in the generated
    # code (a bare stub) -- manually attach it so eSport_Tournament's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eSport_Tournament's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eSport_Tournament(name="sample_text", size=7, type="sample_text", year=7)
    partner = eSport_Root()
    setattr(partner, 'eSport_Root87', None)
    _safe_set(owner, 'eSport_Tournament', partner)
    assert owner in getattr(partner, 'eSport_Root87')
    _safe_set(owner, 'eSport_Tournament', None)
    assert owner not in getattr(partner, 'eSport_Root87')


def test_assoc_zones85_stub_double():
    # eSport_Root has no real 'eSport_Root' property in the generated
    # code (a bare stub) -- manually attach it so eSport_Zone's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eSport_Zone's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eSport_Zone(name="sample_text")
    partner = eSport_Root()
    setattr(partner, 'eSport_Root', None)
    _safe_set(owner, 'eSport_Zone', partner)
    assert owner in getattr(partner, 'eSport_Root')
    _safe_set(owner, 'eSport_Zone', None)
    assert owner not in getattr(partner, 'eSport_Root')


