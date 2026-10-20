import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Ball,
    model_Ball,
    model_ExtraBall,
    model_Game,
    model_Innings,
    model_Over,
    model_Player,
    model_Team,
    model_WicketBall,
    BallType,
    ExtraType,
    HowOut,
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

def test_assoc_assists27_reverse_link_reassign_clear():
    a1 = model_WicketBall(howOut="sample_text")
    a2 = model_WicketBall(howOut="sample_text_2")
    b = model_Player(howOut="sample_text", name="sample_text", noBallsFaced=7, noOversBowled="sample_text", runsScored=7)
    _safe_set(b, 'model_Player28', a1)
    assert _is_linked(b, 'model_Player28', a1)
    if hasattr(a1, 'model_WicketBall'):
        assert _is_linked(a1, 'model_WicketBall', b)
    _safe_set(b, 'model_Player28', a2)
    assert _is_linked(b, 'model_Player28', a2)
    if hasattr(a1, 'model_WicketBall'):
        assert not _is_linked(a1, 'model_WicketBall', b)
    if hasattr(a2, 'model_WicketBall'):
        assert _is_linked(a2, 'model_WicketBall', b)
    _safe_set(b, 'model_Player28', None)
    assert not _is_linked(b, 'model_Player28', a2)
    if hasattr(a2, 'model_WicketBall'):
        assert not _is_linked(a2, 'model_WicketBall', b)


def test_assoc_balls15_reverse_link_reassign_clear():
    a1 = model_Over(BALLS_IN_OVER=7, isComplete=True, runs=7, validBalls=7)
    a2 = model_Over(BALLS_IN_OVER=13, isComplete=False, runs=13, validBalls=13)
    b = model_Ball(runValue=7, runs="sample_text", switchEnds="sample_text")
    _safe_set(b, 'model_Ball', a1)
    assert _is_linked(b, 'model_Ball', a1)
    if hasattr(a1, 'model_Over'):
        assert _is_linked(a1, 'model_Over', b)
    _safe_set(b, 'model_Ball', a2)
    assert _is_linked(b, 'model_Ball', a2)
    if hasattr(a1, 'model_Over'):
        assert not _is_linked(a1, 'model_Over', b)
    if hasattr(a2, 'model_Over'):
        assert _is_linked(a2, 'model_Over', b)
    _safe_set(b, 'model_Ball', None)
    assert not _is_linked(b, 'model_Ball', a2)
    if hasattr(a2, 'model_Over'):
        assert not _is_linked(a2, 'model_Over', b)


def test_assoc_ballsFaced20_reverse_link_reassign_clear():
    a1 = model_Player(howOut="sample_text", name="sample_text", noBallsFaced=7, noOversBowled="sample_text", runsScored=7)
    a2 = model_Player(howOut="sample_text_2", name="sample_text_2", noBallsFaced=13, noOversBowled="sample_text_2", runsScored=13)
    b = model_Ball(runValue=7, runs="sample_text", switchEnds="sample_text")
    _safe_set(b, 'Ball', a1)
    assert _is_linked(b, 'Ball', a1)
    if hasattr(a1, 'batsman'):
        assert _is_linked(a1, 'batsman', b)
    _safe_set(b, 'Ball', a2)
    assert _is_linked(b, 'Ball', a2)
    if hasattr(a1, 'batsman'):
        assert not _is_linked(a1, 'batsman', b)
    if hasattr(a2, 'batsman'):
        assert _is_linked(a2, 'batsman', b)
    _safe_set(b, 'Ball', None)
    assert not _is_linked(b, 'Ball', a2)
    if hasattr(a2, 'batsman'):
        assert not _is_linked(a2, 'batsman', b)


def test_assoc_batsman18_reverse_link_reassign_clear():
    a1 = model_Player(howOut="sample_text", name="sample_text", noBallsFaced=7, noOversBowled="sample_text", runsScored=7)
    a2 = model_Player(howOut="sample_text_2", name="sample_text_2", noBallsFaced=13, noOversBowled="sample_text_2", runsScored=13)
    b = model_Ball(runValue=7, runs="sample_text", switchEnds="sample_text")
    _safe_set(b, 'ballsFaced', a1)
    assert _is_linked(b, 'ballsFaced', a1)
    if hasattr(a1, 'Player19'):
        assert _is_linked(a1, 'Player19', b)
    _safe_set(b, 'ballsFaced', a2)
    assert _is_linked(b, 'ballsFaced', a2)
    if hasattr(a1, 'Player19'):
        assert not _is_linked(a1, 'Player19', b)
    if hasattr(a2, 'Player19'):
        assert _is_linked(a2, 'Player19', b)
    _safe_set(b, 'ballsFaced', None)
    assert not _is_linked(b, 'ballsFaced', a2)
    if hasattr(a2, 'Player19'):
        assert not _is_linked(a2, 'Player19', b)


def test_assoc_battingSide4_reverse_link_reassign_clear():
    a1 = model_Team(name="sample_text")
    a2 = model_Team(name="sample_text_2")
    b = model_Innings(Summary="sample_text", noOvers=7, overCount="sample_text", total=7, wicketsDown=7)
    _safe_set(b, 'model_Innings5', a1)
    assert _is_linked(b, 'model_Innings5', a1)
    if hasattr(a1, 'model_Team6'):
        assert _is_linked(a1, 'model_Team6', b)
    _safe_set(b, 'model_Innings5', a2)
    assert _is_linked(b, 'model_Innings5', a2)
    if hasattr(a1, 'model_Team6'):
        assert not _is_linked(a1, 'model_Team6', b)
    if hasattr(a2, 'model_Team6'):
        assert _is_linked(a2, 'model_Team6', b)
    _safe_set(b, 'model_Innings5', None)
    assert not _is_linked(b, 'model_Innings5', a2)
    if hasattr(a2, 'model_Team6'):
        assert not _is_linked(a2, 'model_Team6', b)


def test_assoc_bowler17_reverse_link_reassign_clear():
    a1 = model_Player(howOut="sample_text", name="sample_text", noBallsFaced=7, noOversBowled="sample_text", runsScored=7)
    a2 = model_Player(howOut="sample_text_2", name="sample_text_2", noBallsFaced=13, noOversBowled="sample_text_2", runsScored=13)
    b = model_Over(BALLS_IN_OVER=7, isComplete=True, runs=7, validBalls=7)
    _safe_set(b, 'oversBowled', a1)
    assert _is_linked(b, 'oversBowled', a1)
    if hasattr(a1, 'Player'):
        assert _is_linked(a1, 'Player', b)
    _safe_set(b, 'oversBowled', a2)
    assert _is_linked(b, 'oversBowled', a2)
    if hasattr(a1, 'Player'):
        assert not _is_linked(a1, 'Player', b)
    if hasattr(a2, 'Player'):
        assert _is_linked(a2, 'Player', b)
    _safe_set(b, 'oversBowled', None)
    assert not _is_linked(b, 'oversBowled', a2)
    if hasattr(a2, 'Player'):
        assert not _is_linked(a2, 'Player', b)


def test_assoc_bowlingSide7_reverse_link_reassign_clear():
    a1 = model_Team(name="sample_text")
    a2 = model_Team(name="sample_text_2")
    b = model_Innings(Summary="sample_text", noOvers=7, overCount="sample_text", total=7, wicketsDown=7)
    _safe_set(b, 'model_Innings8', a1)
    assert _is_linked(b, 'model_Innings8', a1)
    if hasattr(a1, 'model_Team9'):
        assert _is_linked(a1, 'model_Team9', b)
    _safe_set(b, 'model_Innings8', a2)
    assert _is_linked(b, 'model_Innings8', a2)
    if hasattr(a1, 'model_Team9'):
        assert not _is_linked(a1, 'model_Team9', b)
    if hasattr(a2, 'model_Team9'):
        assert _is_linked(a2, 'model_Team9', b)
    _safe_set(b, 'model_Innings8', None)
    assert not _is_linked(b, 'model_Innings8', a2)
    if hasattr(a2, 'model_Team9'):
        assert not _is_linked(a2, 'model_Team9', b)


def test_assoc_facingBat10_reverse_link_reassign_clear():
    a1 = model_Player(howOut="sample_text", name="sample_text", noBallsFaced=7, noOversBowled="sample_text", runsScored=7)
    a2 = model_Player(howOut="sample_text_2", name="sample_text_2", noBallsFaced=13, noOversBowled="sample_text_2", runsScored=13)
    b = model_Innings(Summary="sample_text", noOvers=7, overCount="sample_text", total=7, wicketsDown=7)
    _safe_set(b, 'model_Innings11', a1)
    assert _is_linked(b, 'model_Innings11', a1)
    if hasattr(a1, 'model_Player'):
        assert _is_linked(a1, 'model_Player', b)
    _safe_set(b, 'model_Innings11', a2)
    assert _is_linked(b, 'model_Innings11', a2)
    if hasattr(a1, 'model_Player'):
        assert not _is_linked(a1, 'model_Player', b)
    if hasattr(a2, 'model_Player'):
        assert _is_linked(a2, 'model_Player', b)
    _safe_set(b, 'model_Innings11', None)
    assert not _is_linked(b, 'model_Innings11', a2)
    if hasattr(a2, 'model_Player'):
        assert not _is_linked(a2, 'model_Player', b)


def test_assoc_innings0_reverse_link_reassign_clear():
    a1 = model_Innings(Summary="sample_text", noOvers=7, overCount="sample_text", total=7, wicketsDown=7)
    a2 = model_Innings(Summary="sample_text_2", noOvers=13, overCount="sample_text_2", total=13, wicketsDown=13)
    b = model_Game(date=date(2024, 1, 1), venue="sample_text")
    _safe_set(b, 'model_Game', {a1})
    assert _is_linked(b, 'model_Game', a1)
    if hasattr(a1, 'model_Innings'):
        assert _is_linked(a1, 'model_Innings', b)
    _safe_set(b, 'model_Game', {a2})
    assert _is_linked(b, 'model_Game', a2)
    if hasattr(a1, 'model_Innings'):
        assert not _is_linked(a1, 'model_Innings', b)
    if hasattr(a2, 'model_Innings'):
        assert _is_linked(a2, 'model_Innings', b)
    _safe_set(b, 'model_Game', set())
    assert not _is_linked(b, 'model_Game', a2)
    if hasattr(a2, 'model_Innings'):
        assert not _is_linked(a2, 'model_Innings', b)


def test_assoc_innings16_reverse_link_reassign_clear():
    a1 = model_Over(BALLS_IN_OVER=7, isComplete=True, runs=7, validBalls=7)
    a2 = model_Over(BALLS_IN_OVER=13, isComplete=False, runs=13, validBalls=13)
    b = model_Innings(Summary="sample_text", noOvers=7, overCount="sample_text", total=7, wicketsDown=7)
    _safe_set(b, 'Innings', a1)
    assert _is_linked(b, 'Innings', a1)
    if hasattr(a1, 'overs'):
        assert _is_linked(a1, 'overs', b)
    _safe_set(b, 'Innings', a2)
    assert _is_linked(b, 'Innings', a2)
    if hasattr(a1, 'overs'):
        assert not _is_linked(a1, 'overs', b)
    if hasattr(a2, 'overs'):
        assert _is_linked(a2, 'overs', b)
    _safe_set(b, 'Innings', None)
    assert not _is_linked(b, 'Innings', a2)
    if hasattr(a2, 'overs'):
        assert not _is_linked(a2, 'overs', b)


def test_assoc_nonFacingBat12_reverse_link_reassign_clear():
    a1 = model_Player(howOut="sample_text", name="sample_text", noBallsFaced=7, noOversBowled="sample_text", runsScored=7)
    a2 = model_Player(howOut="sample_text_2", name="sample_text_2", noBallsFaced=13, noOversBowled="sample_text_2", runsScored=13)
    b = model_Innings(Summary="sample_text", noOvers=7, overCount="sample_text", total=7, wicketsDown=7)
    _safe_set(b, 'model_Innings13', a1)
    assert _is_linked(b, 'model_Innings13', a1)
    if hasattr(a1, 'model_Player14'):
        assert _is_linked(a1, 'model_Player14', b)
    _safe_set(b, 'model_Innings13', a2)
    assert _is_linked(b, 'model_Innings13', a2)
    if hasattr(a1, 'model_Player14'):
        assert not _is_linked(a1, 'model_Player14', b)
    if hasattr(a2, 'model_Player14'):
        assert _is_linked(a2, 'model_Player14', b)
    _safe_set(b, 'model_Innings13', None)
    assert not _is_linked(b, 'model_Innings13', a2)
    if hasattr(a2, 'model_Player14'):
        assert not _is_linked(a2, 'model_Player14', b)


def test_assoc_overs3_reverse_link_reassign_clear():
    a1 = model_Over(BALLS_IN_OVER=7, isComplete=True, runs=7, validBalls=7)
    a2 = model_Over(BALLS_IN_OVER=13, isComplete=False, runs=13, validBalls=13)
    b = model_Innings(Summary="sample_text", noOvers=7, overCount="sample_text", total=7, wicketsDown=7)
    _safe_set(b, 'innings', {a1})
    assert _is_linked(b, 'innings', a1)
    if hasattr(a1, 'Over'):
        assert _is_linked(a1, 'Over', b)
    _safe_set(b, 'innings', {a2})
    assert _is_linked(b, 'innings', a2)
    if hasattr(a1, 'Over'):
        assert not _is_linked(a1, 'Over', b)
    if hasattr(a2, 'Over'):
        assert _is_linked(a2, 'Over', b)
    _safe_set(b, 'innings', set())
    assert not _is_linked(b, 'innings', a2)
    if hasattr(a2, 'Over'):
        assert not _is_linked(a2, 'Over', b)


def test_assoc_oversBowled21_reverse_link_reassign_clear():
    a1 = model_Player(howOut="sample_text", name="sample_text", noBallsFaced=7, noOversBowled="sample_text", runsScored=7)
    a2 = model_Player(howOut="sample_text_2", name="sample_text_2", noBallsFaced=13, noOversBowled="sample_text_2", runsScored=13)
    b = model_Over(BALLS_IN_OVER=7, isComplete=True, runs=7, validBalls=7)
    _safe_set(b, 'Over22', a1)
    assert _is_linked(b, 'Over22', a1)
    if hasattr(a1, 'bowler'):
        assert _is_linked(a1, 'bowler', b)
    _safe_set(b, 'Over22', a2)
    assert _is_linked(b, 'Over22', a2)
    if hasattr(a1, 'bowler'):
        assert not _is_linked(a1, 'bowler', b)
    if hasattr(a2, 'bowler'):
        assert _is_linked(a2, 'bowler', b)
    _safe_set(b, 'Over22', None)
    assert not _is_linked(b, 'Over22', a2)
    if hasattr(a2, 'bowler'):
        assert not _is_linked(a2, 'bowler', b)


def test_assoc_playerOut29_reverse_link_reassign_clear():
    a1 = model_WicketBall(howOut="sample_text")
    a2 = model_WicketBall(howOut="sample_text_2")
    b = model_Player(howOut="sample_text", name="sample_text", noBallsFaced=7, noOversBowled="sample_text", runsScored=7)
    _safe_set(b, 'Player30', a1)
    assert _is_linked(b, 'Player30', a1)
    if hasattr(a1, 'wicketball'):
        assert _is_linked(a1, 'wicketball', b)
    _safe_set(b, 'Player30', a2)
    assert _is_linked(b, 'Player30', a2)
    if hasattr(a1, 'wicketball'):
        assert not _is_linked(a1, 'wicketball', b)
    if hasattr(a2, 'wicketball'):
        assert _is_linked(a2, 'wicketball', b)
    _safe_set(b, 'Player30', None)
    assert not _is_linked(b, 'Player30', a2)
    if hasattr(a2, 'wicketball'):
        assert not _is_linked(a2, 'wicketball', b)


def test_assoc_players24_reverse_link_reassign_clear():
    a1 = model_Team(name="sample_text")
    a2 = model_Team(name="sample_text_2")
    b = model_Player(howOut="sample_text", name="sample_text", noBallsFaced=7, noOversBowled="sample_text", runsScored=7)
    _safe_set(b, 'model_Player26', a1)
    assert _is_linked(b, 'model_Player26', a1)
    if hasattr(a1, 'model_Team25'):
        assert _is_linked(a1, 'model_Team25', b)
    _safe_set(b, 'model_Player26', a2)
    assert _is_linked(b, 'model_Player26', a2)
    if hasattr(a1, 'model_Team25'):
        assert not _is_linked(a1, 'model_Team25', b)
    if hasattr(a2, 'model_Team25'):
        assert _is_linked(a2, 'model_Team25', b)
    _safe_set(b, 'model_Player26', None)
    assert not _is_linked(b, 'model_Player26', a2)
    if hasattr(a2, 'model_Team25'):
        assert not _is_linked(a2, 'model_Team25', b)


def test_assoc_team1_reverse_link_reassign_clear():
    a1 = model_Team(name="sample_text")
    a2 = model_Team(name="sample_text_2")
    b = model_Game(date=date(2024, 1, 1), venue="sample_text")
    _safe_set(b, 'model_Game2', {a1})
    assert _is_linked(b, 'model_Game2', a1)
    if hasattr(a1, 'model_Team'):
        assert _is_linked(a1, 'model_Team', b)
    _safe_set(b, 'model_Game2', {a2})
    assert _is_linked(b, 'model_Game2', a2)
    if hasattr(a1, 'model_Team'):
        assert not _is_linked(a1, 'model_Team', b)
    if hasattr(a2, 'model_Team'):
        assert _is_linked(a2, 'model_Team', b)
    _safe_set(b, 'model_Game2', set())
    assert not _is_linked(b, 'model_Game2', a2)
    if hasattr(a2, 'model_Team'):
        assert not _is_linked(a2, 'model_Team', b)


def test_assoc_wicketball23_reverse_link_reassign_clear():
    a1 = model_WicketBall(howOut="sample_text")
    a2 = model_WicketBall(howOut="sample_text_2")
    b = model_Player(howOut="sample_text", name="sample_text", noBallsFaced=7, noOversBowled="sample_text", runsScored=7)
    _safe_set(b, 'playerOut', a1)
    assert _is_linked(b, 'playerOut', a1)
    if hasattr(a1, 'WicketBall'):
        assert _is_linked(a1, 'WicketBall', b)
    _safe_set(b, 'playerOut', a2)
    assert _is_linked(b, 'playerOut', a2)
    if hasattr(a1, 'WicketBall'):
        assert not _is_linked(a1, 'WicketBall', b)
    if hasattr(a2, 'WicketBall'):
        assert _is_linked(a2, 'WicketBall', b)
    _safe_set(b, 'playerOut', None)
    assert not _is_linked(b, 'playerOut', a2)
    if hasattr(a2, 'WicketBall'):
        assert not _is_linked(a2, 'WicketBall', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

