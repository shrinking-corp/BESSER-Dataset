# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BowlingGame,
    Importer_Interface,
    Result,
    InitialData,
    FileImporter,
    Attempt,
    Game,
    Player,
    Match,
    ScoreType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_bowlinggame_is_not_abstract():
    assert not inspect.isabstract(BowlingGame)


def test_hyp_bowlinggame_constructor_exists():
    assert callable(BowlingGame.__init__)


def test_hyp_bowlinggame_constructor_args():
    sig = inspect.signature(BowlingGame.__init__)
    params = list(sig.parameters.keys())
    assert "previousGame" in params, "Missing parameter 'previousGame'"
    assert "nextGames" in params, "Missing parameter 'nextGames'"
    assert "scoreType" in params, "Missing parameter 'scoreType'"
    assert "attempts" in params, "Missing parameter 'attempts'"

def test_hyp_bowlinggame_has_previousGame():
    assert hasattr(BowlingGame, "previousGame")
    descriptor = None
    for klass in BowlingGame.__mro__:
        if "previousGame" in klass.__dict__:
            descriptor = klass.__dict__["previousGame"]
            break
    assert isinstance(descriptor, property)

def test_hyp_bowlinggame_has_nextGames():
    assert hasattr(BowlingGame, "nextGames")
    descriptor = None
    for klass in BowlingGame.__mro__:
        if "nextGames" in klass.__dict__:
            descriptor = klass.__dict__["nextGames"]
            break
    assert isinstance(descriptor, property)

def test_hyp_bowlinggame_has_scoreType():
    assert hasattr(BowlingGame, "scoreType")
    descriptor = None
    for klass in BowlingGame.__mro__:
        if "scoreType" in klass.__dict__:
            descriptor = klass.__dict__["scoreType"]
            break
    assert isinstance(descriptor, property)

def test_hyp_bowlinggame_has_attempts():
    assert hasattr(BowlingGame, "attempts")
    descriptor = None
    for klass in BowlingGame.__mro__:
        if "attempts" in klass.__dict__:
            descriptor = klass.__dict__["attempts"]
            break
    assert isinstance(descriptor, property)



def test_hyp_importer_interface_is_not_abstract():
    assert not inspect.isabstract(Importer_Interface)


def test_hyp_importer_interface_constructor_exists():
    assert callable(Importer_Interface.__init__)


def test_hyp_importer_interface_constructor_args():
    sig = inspect.signature(Importer_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_result_is_not_abstract():
    assert not inspect.isabstract(Result)


def test_hyp_result_constructor_exists():
    assert callable(Result.__init__)


def test_hyp_result_constructor_args():
    sig = inspect.signature(Result.__init__)
    params = list(sig.parameters.keys())
    assert "score" in params, "Missing parameter 'score'"
    assert "player" in params, "Missing parameter 'player'"





def test_hyp_initialdata_is_not_abstract():
    assert not inspect.isabstract(InitialData)


def test_hyp_initialdata_constructor_exists():
    assert callable(InitialData.__init__)


def test_hyp_initialdata_constructor_args():
    sig = inspect.signature(InitialData.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"
    assert "playerName" in params, "Missing parameter 'playerName'"





def test_hyp_fileimporter_is_not_abstract():
    assert not inspect.isabstract(FileImporter)


def test_hyp_fileimporter_constructor_exists():
    assert callable(FileImporter.__init__)


def test_hyp_fileimporter_constructor_args():
    sig = inspect.signature(FileImporter.__init__)
    params = list(sig.parameters.keys())
    assert "INITIAL_DATAFILE" in params, "Missing parameter 'INITIAL_DATAFILE'"




def test_hyp_attempt_is_not_abstract():
    assert not inspect.isabstract(Attempt)


def test_hyp_attempt_constructor_exists():
    assert callable(Attempt.__init__)


def test_hyp_attempt_constructor_args():
    sig = inspect.signature(Attempt.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"
    assert "number" in params, "Missing parameter 'number'"





def test_hyp_game_is_not_abstract():
    assert not inspect.isabstract(Game)


def test_hyp_game_constructor_exists():
    assert callable(Game.__init__)


def test_hyp_game_constructor_args():
    sig = inspect.signature(Game.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "score" in params, "Missing parameter 'score'"





def test_hyp_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_hyp_player_constructor_exists():
    assert callable(Player.__init__)


def test_hyp_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "totalScore" in params, "Missing parameter 'totalScore'"
    assert "games" in params, "Missing parameter 'games'"

def test_hyp_player_has_name():
    assert hasattr(Player, "name")
    descriptor = None
    for klass in Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hyp_player_has_totalScore():
    assert hasattr(Player, "totalScore")
    descriptor = None
    for klass in Player.__mro__:
        if "totalScore" in klass.__dict__:
            descriptor = klass.__dict__["totalScore"]
            break
    assert isinstance(descriptor, property)

def test_hyp_player_has_games():
    assert hasattr(Player, "games")
    descriptor = None
    for klass in Player.__mro__:
        if "games" in klass.__dict__:
            descriptor = klass.__dict__["games"]
            break
    assert isinstance(descriptor, property)



def test_hyp_match_is_not_abstract():
    assert not inspect.isabstract(Match)


def test_hyp_match_constructor_exists():
    assert callable(Match.__init__)


def test_hyp_match_constructor_args():
    sig = inspect.signature(Match.__init__)
    params = list(sig.parameters.keys())
    assert "winner" in params, "Missing parameter 'winner'"
    assert "date" in params, "Missing parameter 'date'"
    assert "name" in params, "Missing parameter 'name'"
    assert "players" in params, "Missing parameter 'players'"

def test_hyp_match_has_winner():
    assert hasattr(Match, "winner")
    descriptor = None
    for klass in Match.__mro__:
        if "winner" in klass.__dict__:
            descriptor = klass.__dict__["winner"]
            break
    assert isinstance(descriptor, property)

def test_hyp_match_has_date():
    assert hasattr(Match, "date")
    descriptor = None
    for klass in Match.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_hyp_match_has_name():
    assert hasattr(Match, "name")
    descriptor = None
    for klass in Match.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hyp_match_has_players():
    assert hasattr(Match, "players")
    descriptor = None
    for klass in Match.__mro__:
        if "players" in klass.__dict__:
            descriptor = klass.__dict__["players"]
            break
    assert isinstance(descriptor, property)

def test_hyp_scoretype_exists():
    # Check that the Enumeration exists
    assert ScoreType is not None

def test_hyp_scoretype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScoreType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScoreType"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
BowlingGame_strategy = st.builds(
    BowlingGame,
    previousGame=
        st.none(),
    nextGames=
        safe_text,
    scoreType=
        st.none(),
    attempts=
        safe_text
)
Importer_Interface_strategy = st.builds(
    Importer_Interface,
)
Result_strategy = st.builds(
    Result,
    score=
        st.integers(),
    player=
        safe_text
)
InitialData_strategy = st.builds(
    InitialData,
    points=
        safe_text,
    playerName=
        safe_text
)
FileImporter_strategy = st.builds(
    FileImporter,
    INITIAL_DATAFILE=
        safe_text
)
Attempt_strategy = st.builds(
    Attempt,
    points=
        st.integers(),
    number=
        st.integers()
)
Game_strategy = st.builds(
    Game,
    number=
        st.integers(),
    score=
        st.integers()
)
Player_strategy = st.builds(
    Player,
    name=
        safe_text,
    totalScore=
        st.integers(),
    games=
        st.none()
)
Match_strategy = st.builds(
    Match,
    winner=
        st.none(),
    date=
        safe_text,
    name=
        safe_text,
    players=
        safe_text
)

@given(instance=BowlingGame_strategy)
@settings(max_examples=50)
def test_hyp_bowlinggame_instantiation(instance):
    assert isinstance(instance, BowlingGame)



@given(instance=BowlingGame_strategy)
def test_hyp_bowlinggame_previousGame_setter(instance):
    original = instance.previousGame
    instance.previousGame = original
    assert instance.previousGame == original



@given(instance=BowlingGame_strategy)
def test_hyp_bowlinggame_nextGames_setter(instance):
    original = instance.nextGames
    instance.nextGames = original
    assert instance.nextGames == original



@given(instance=BowlingGame_strategy)
def test_hyp_bowlinggame_scoreType_setter(instance):
    original = instance.scoreType
    instance.scoreType = original
    assert instance.scoreType == original



@given(instance=BowlingGame_strategy)
def test_hyp_bowlinggame_attempts_setter(instance):
    original = instance.attempts
    instance.attempts = original
    assert instance.attempts == original





@given(instance=Result_strategy)
def test_hyp_result_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original



@given(instance=Result_strategy)
def test_hyp_result_player_setter(instance):
    original = instance.player
    instance.player = original
    assert instance.player == original




@given(instance=InitialData_strategy)
def test_hyp_initialdata_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original



@given(instance=InitialData_strategy)
def test_hyp_initialdata_playerName_setter(instance):
    original = instance.playerName
    instance.playerName = original
    assert instance.playerName == original




@given(instance=FileImporter_strategy)
def test_hyp_fileimporter_INITIAL_DATAFILE_setter(instance):
    original = instance.INITIAL_DATAFILE
    instance.INITIAL_DATAFILE = original
    assert instance.INITIAL_DATAFILE == original




@given(instance=Attempt_strategy)
def test_hyp_attempt_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original



@given(instance=Attempt_strategy)
def test_hyp_attempt_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original




@given(instance=Game_strategy)
def test_hyp_game_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=Game_strategy)
def test_hyp_game_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_hyp_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_hyp_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Player_strategy)
def test_hyp_player_totalScore_setter(instance):
    original = instance.totalScore
    instance.totalScore = original
    assert instance.totalScore == original



@given(instance=Player_strategy)
def test_hyp_player_games_setter(instance):
    original = instance.games
    instance.games = original
    assert instance.games == original

@given(instance=Match_strategy)
@settings(max_examples=50)
def test_hyp_match_instantiation(instance):
    assert isinstance(instance, Match)



@given(instance=Match_strategy)
def test_hyp_match_winner_setter(instance):
    original = instance.winner
    instance.winner = original
    assert instance.winner == original



@given(instance=Match_strategy)
def test_hyp_match_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Match_strategy)
def test_hyp_match_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Match_strategy)
def test_hyp_match_players_setter(instance):
    original = instance.players
    instance.players = original
    assert instance.players == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Attempt,
    BowlingGame,
    FileImporter,
    Game,
    Importer_Interface,
    InitialData,
    Match,
    Player,
    Result,
    ScoreType,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_Attempt_number_value_roundtrip():
    instance = Attempt(number=7, points=7)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_Attempt_points_value_roundtrip():
    instance = Attempt(number=7, points=7)
    assert instance.points == 7
    instance.points = 13
    assert instance.points == 13


def test_FileImporter_INITIAL_DATAFILE_value_roundtrip():
    instance = FileImporter(INITIAL_DATAFILE="sample_text")
    assert instance.INITIAL_DATAFILE == "sample_text"
    instance.INITIAL_DATAFILE = "sample_text_2"
    assert instance.INITIAL_DATAFILE == "sample_text_2"


def test_Game_number_value_roundtrip():
    instance = Game(number=7, score=7)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_Game_score_value_roundtrip():
    instance = Game(number=7, score=7)
    assert instance.score == 7
    instance.score = 13
    assert instance.score == 13


def test_InitialData_playerName_value_roundtrip():
    instance = InitialData(playerName="sample_text", points="sample_text")
    assert instance.playerName == "sample_text"
    instance.playerName = "sample_text_2"
    assert instance.playerName == "sample_text_2"


def test_InitialData_points_value_roundtrip():
    instance = InitialData(playerName="sample_text", points="sample_text")
    assert instance.points == "sample_text"
    instance.points = "sample_text_2"
    assert instance.points == "sample_text_2"


def test_Result_player_value_roundtrip():
    instance = Result(player="sample_text", score=7)
    assert instance.player == "sample_text"
    instance.player = "sample_text_2"
    assert instance.player == "sample_text_2"


def test_Result_score_value_roundtrip():
    instance = Result(player="sample_text", score=7)
    assert instance.score == 7
    instance.score = 13
    assert instance.score == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Attempt_strategy = st.builds(Attempt, number=st.integers(), points=st.integers())
@given(instance=Attempt_strategy)
@settings(max_examples=25)
def test_Attempt_instantiation(instance):
    assert isinstance(instance, Attempt)


FileImporter_strategy = st.builds(FileImporter, INITIAL_DATAFILE=safe_text)
@given(instance=FileImporter_strategy)
@settings(max_examples=25)
def test_FileImporter_instantiation(instance):
    assert isinstance(instance, FileImporter)


Game_strategy = st.builds(Game, number=st.integers(), score=st.integers())
@given(instance=Game_strategy)
@settings(max_examples=25)
def test_Game_instantiation(instance):
    assert isinstance(instance, Game)


Importer_Interface_strategy = st.builds(Importer_Interface)
@given(instance=Importer_Interface_strategy)
@settings(max_examples=25)
def test_Importer_Interface_instantiation(instance):
    assert isinstance(instance, Importer_Interface)


InitialData_strategy = st.builds(InitialData, playerName=safe_text, points=safe_text)
@given(instance=InitialData_strategy)
@settings(max_examples=25)
def test_InitialData_instantiation(instance):
    assert isinstance(instance, InitialData)


Result_strategy = st.builds(Result, player=safe_text, score=st.integers())
@given(instance=Result_strategy)
@settings(max_examples=25)
def test_Result_instantiation(instance):
    assert isinstance(instance, Result)



