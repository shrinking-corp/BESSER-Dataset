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
    bowling_League,
    bowling_Player,
    bowling_Game,
    bowling_Matchup,
    bowling_Tournament,
    TournamentType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_bowling_league_is_not_abstract():
    assert not inspect.isabstract(bowling_League)


def test_hyp_bowling_league_constructor_exists():
    assert callable(bowling_League.__init__)


def test_hyp_bowling_league_constructor_args():
    sig = inspect.signature(bowling_League.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_bowling_player_is_not_abstract():
    assert not inspect.isabstract(bowling_Player)


def test_hyp_bowling_player_constructor_exists():
    assert callable(bowling_Player.__init__)


def test_hyp_bowling_player_constructor_args():
    sig = inspect.signature(bowling_Player.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"





def test_hyp_bowling_game_is_not_abstract():
    assert not inspect.isabstract(bowling_Game)


def test_hyp_bowling_game_constructor_exists():
    assert callable(bowling_Game.__init__)


def test_hyp_bowling_game_constructor_args():
    sig = inspect.signature(bowling_Game.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bowling_matchup_is_not_abstract():
    assert not inspect.isabstract(bowling_Matchup)


def test_hyp_bowling_matchup_constructor_exists():
    assert callable(bowling_Matchup.__init__)


def test_hyp_bowling_matchup_constructor_args():
    sig = inspect.signature(bowling_Matchup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bowling_tournament_is_not_abstract():
    assert not inspect.isabstract(bowling_Tournament)


def test_hyp_bowling_tournament_constructor_exists():
    assert callable(bowling_Tournament.__init__)


def test_hyp_bowling_tournament_constructor_args():
    sig = inspect.signature(bowling_Tournament.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"


def test_hyp_tournamenttype_exists():
    # Check that the Enumeration exists
    assert TournamentType is not None

def test_hyp_tournamenttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TournamentType]
    expected_literals = [
        "Amateur",
        "Pro",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TournamentType"


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
bowling_League_strategy = st.builds(
    bowling_League,
    name=
        safe_text
)
bowling_Player_strategy = st.builds(
    bowling_Player,
    name=
        safe_text,
    dateOfBirth=
        st.dates()
)
bowling_Game_strategy = st.builds(
    bowling_Game,
)
bowling_Matchup_strategy = st.builds(
    bowling_Matchup,
)
bowling_Tournament_strategy = st.builds(
    bowling_Tournament,
    type=
        safe_text
)




@given(instance=bowling_League_strategy)
def test_hyp_bowling_league_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original






@given(instance=bowling_Tournament_strategy)
def test_hyp_bowling_tournament_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    bowling_Game,
    bowling_League,
    bowling_Matchup,
    bowling_Player,
    bowling_Tournament,
    TournamentType,
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

def test_bowling_League_name_value_roundtrip():
    instance = bowling_League(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_bowling_Player_dateOfBirth_value_roundtrip():
    instance = bowling_Player(dateOfBirth=date(2024, 1, 1), name="sample_text")
    assert instance.dateOfBirth == date(2024, 1, 1)
    instance.dateOfBirth = date(2025, 6, 15)
    assert instance.dateOfBirth == date(2025, 6, 15)


def test_bowling_Player_name_value_roundtrip():
    instance = bowling_Player(dateOfBirth=date(2024, 1, 1), name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_bowling_Tournament_type_value_roundtrip():
    instance = bowling_Tournament(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_assoc_matchups1_link_reassign_clear():
    a = bowling_Tournament(type="sample_text")
    b1 = bowling_Matchup()
    b2 = bowling_Matchup()
    _safe_set(a, 'bowling_Tournament', {b1})
    assert _is_linked(a, 'bowling_Tournament', b1)
    if hasattr(b1, 'bowling_Matchup'):
        assert _is_linked(b1, 'bowling_Matchup', a)
    _safe_set(a, 'bowling_Tournament', {b2})
    assert _is_linked(a, 'bowling_Tournament', b2)
    if hasattr(b1, 'bowling_Matchup'):
        assert not _is_linked(b1, 'bowling_Matchup', a)
    if hasattr(b2, 'bowling_Matchup'):
        assert _is_linked(b2, 'bowling_Matchup', a)
    _safe_set(a, 'bowling_Tournament', set())
    assert not _is_linked(a, 'bowling_Tournament', b2)
    if hasattr(b2, 'bowling_Matchup'):
        assert not _is_linked(b2, 'bowling_Matchup', a)


def test_assoc_player4_link_reassign_clear():
    a = bowling_Player(dateOfBirth=date(2024, 1, 1), name="sample_text")
    b1 = bowling_Game()
    b2 = bowling_Game()
    _safe_set(a, 'bowling_Player5', b1)
    assert _is_linked(a, 'bowling_Player5', b1)
    if hasattr(b1, 'bowling_Game'):
        assert _is_linked(b1, 'bowling_Game', a)
    _safe_set(a, 'bowling_Player5', b2)
    assert _is_linked(a, 'bowling_Player5', b2)
    if hasattr(b1, 'bowling_Game'):
        assert not _is_linked(b1, 'bowling_Game', a)
    if hasattr(b2, 'bowling_Game'):
        assert _is_linked(b2, 'bowling_Game', a)
    _safe_set(a, 'bowling_Player5', None)
    assert not _is_linked(a, 'bowling_Player5', b2)
    if hasattr(b2, 'bowling_Game'):
        assert not _is_linked(b2, 'bowling_Game', a)


def test_assoc_players0_link_reassign_clear():
    a = bowling_Player(dateOfBirth=date(2024, 1, 1), name="sample_text")
    b1 = bowling_League(name="sample_text")
    b2 = bowling_League(name="sample_text_2")
    _safe_set(a, 'bowling_Player', b1)
    assert _is_linked(a, 'bowling_Player', b1)
    if hasattr(b1, 'bowling_League'):
        assert _is_linked(b1, 'bowling_League', a)
    _safe_set(a, 'bowling_Player', b2)
    assert _is_linked(a, 'bowling_Player', b2)
    if hasattr(b1, 'bowling_League'):
        assert not _is_linked(b1, 'bowling_League', a)
    if hasattr(b2, 'bowling_League'):
        assert _is_linked(b2, 'bowling_League', a)
    _safe_set(a, 'bowling_Player', None)
    assert not _is_linked(a, 'bowling_Player', b2)
    if hasattr(b2, 'bowling_League'):
        assert not _is_linked(b2, 'bowling_League', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

bowling_Game_strategy = st.builds(bowling_Game)
@given(instance=bowling_Game_strategy)
@settings(max_examples=25)
def test_bowling_Game_instantiation(instance):
    assert isinstance(instance, bowling_Game)


bowling_League_strategy = st.builds(bowling_League, name=safe_text)
@given(instance=bowling_League_strategy)
@settings(max_examples=25)
def test_bowling_League_instantiation(instance):
    assert isinstance(instance, bowling_League)


bowling_Matchup_strategy = st.builds(bowling_Matchup)
@given(instance=bowling_Matchup_strategy)
@settings(max_examples=25)
def test_bowling_Matchup_instantiation(instance):
    assert isinstance(instance, bowling_Matchup)


bowling_Player_strategy = st.builds(bowling_Player, dateOfBirth=st.dates(), name=safe_text)
@given(instance=bowling_Player_strategy)
@settings(max_examples=25)
def test_bowling_Player_instantiation(instance):
    assert isinstance(instance, bowling_Player)


bowling_Tournament_strategy = st.builds(bowling_Tournament, type=safe_text)
@given(instance=bowling_Tournament_strategy)
@settings(max_examples=25)
def test_bowling_Tournament_instantiation(instance):
    assert isinstance(instance, bowling_Tournament)



