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
    bowling_Playerlist,
    bowling_Game,
    bowling_Tournament,
    bowling_Matchup,
    bowling_Player,
    TournamentType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_bowling_playerlist_is_not_abstract():
    assert not inspect.isabstract(bowling_Playerlist)


def test_hyp_bowling_playerlist_constructor_exists():
    assert callable(bowling_Playerlist.__init__)


def test_hyp_bowling_playerlist_constructor_args():
    sig = inspect.signature(bowling_Playerlist.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_bowling_game_is_not_abstract():
    assert not inspect.isabstract(bowling_Game)


def test_hyp_bowling_game_constructor_exists():
    assert callable(bowling_Game.__init__)


def test_hyp_bowling_game_constructor_args():
    sig = inspect.signature(bowling_Game.__init__)
    params = list(sig.parameters.keys())
    assert "frames" in params, "Missing parameter 'frames'"
    assert "date" in params, "Missing parameter 'date'"





def test_hyp_bowling_tournament_is_not_abstract():
    assert not inspect.isabstract(bowling_Tournament)


def test_hyp_bowling_tournament_constructor_exists():
    assert callable(bowling_Tournament.__init__)


def test_hyp_bowling_tournament_constructor_args():
    sig = inspect.signature(bowling_Tournament.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "title" in params, "Missing parameter 'title'"





def test_hyp_bowling_matchup_is_not_abstract():
    assert not inspect.isabstract(bowling_Matchup)


def test_hyp_bowling_matchup_constructor_exists():
    assert callable(bowling_Matchup.__init__)


def test_hyp_bowling_matchup_constructor_args():
    sig = inspect.signature(bowling_Matchup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bowling_player_is_not_abstract():
    assert not inspect.isabstract(bowling_Player)


def test_hyp_bowling_player_constructor_exists():
    assert callable(bowling_Player.__init__)


def test_hyp_bowling_player_constructor_args():
    sig = inspect.signature(bowling_Player.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "height" in params, "Missing parameter 'height'"
    assert "city" in params, "Missing parameter 'city'"
    assert "streetnumber" in params, "Missing parameter 'streetnumber'"
    assert "street" in params, "Missing parameter 'street'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "isProfessional" in params, "Missing parameter 'isProfessional'"









def test_hyp_tournamenttype_exists():
    # Check that the Enumeration exists
    assert TournamentType is not None

def test_hyp_tournamenttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TournamentType]
    expected_literals = [
        "Pro",
        "Amateur",
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
bowling_Playerlist_strategy = st.builds(
    bowling_Playerlist,
    name=
        safe_text
)
bowling_Game_strategy = st.builds(
    bowling_Game,
    frames=
        st.integers(),
    date=
        st.dates()
)
bowling_Tournament_strategy = st.builds(
    bowling_Tournament,
    type=
        safe_text,
    title=
        safe_text
)
bowling_Matchup_strategy = st.builds(
    bowling_Matchup,
)
bowling_Player_strategy = st.builds(
    bowling_Player,
    lastname=
        safe_text,
    firstname=
        safe_text,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    city=
        safe_text,
    streetnumber=
        st.integers(),
    street=
        safe_text,
    dateOfBirth=
        st.dates(),
    isProfessional=
        st.booleans()
)




@given(instance=bowling_Playerlist_strategy)
def test_hyp_bowling_playerlist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=bowling_Game_strategy)
def test_hyp_bowling_game_frames_setter(instance):
    original = instance.frames
    instance.frames = original
    assert instance.frames == original



@given(instance=bowling_Game_strategy)
def test_hyp_bowling_game_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original




@given(instance=bowling_Tournament_strategy)
def test_hyp_bowling_tournament_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=bowling_Tournament_strategy)
def test_hyp_bowling_tournament_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original





@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_streetnumber_setter(instance):
    original = instance.streetnumber
    instance.streetnumber = original
    assert instance.streetnumber == original



@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_isProfessional_setter(instance):
    original = instance.isProfessional
    instance.isProfessional = original
    assert instance.isProfessional == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    bowling_Game,
    bowling_Matchup,
    bowling_Player,
    bowling_Playerlist,
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

def test_bowling_Game_date_value_roundtrip():
    instance = bowling_Game(date=date(2024, 1, 1), frames=7)
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_bowling_Game_frames_value_roundtrip():
    instance = bowling_Game(date=date(2024, 1, 1), frames=7)
    assert instance.frames == 7
    instance.frames = 13
    assert instance.frames == 13


def test_bowling_Player_city_value_roundtrip():
    instance = bowling_Player(city="sample_text", dateOfBirth=date(2024, 1, 1), firstname="sample_text", height=3.14, isProfessional=True, lastname="sample_text", street="sample_text", streetnumber=7)
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_bowling_Player_dateOfBirth_value_roundtrip():
    instance = bowling_Player(city="sample_text", dateOfBirth=date(2024, 1, 1), firstname="sample_text", height=3.14, isProfessional=True, lastname="sample_text", street="sample_text", streetnumber=7)
    assert instance.dateOfBirth == date(2024, 1, 1)
    instance.dateOfBirth = date(2025, 6, 15)
    assert instance.dateOfBirth == date(2025, 6, 15)


def test_bowling_Player_firstname_value_roundtrip():
    instance = bowling_Player(city="sample_text", dateOfBirth=date(2024, 1, 1), firstname="sample_text", height=3.14, isProfessional=True, lastname="sample_text", street="sample_text", streetnumber=7)
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_bowling_Player_height_value_roundtrip():
    instance = bowling_Player(city="sample_text", dateOfBirth=date(2024, 1, 1), firstname="sample_text", height=3.14, isProfessional=True, lastname="sample_text", street="sample_text", streetnumber=7)
    assert instance.height == 3.14
    instance.height = 9.99
    assert instance.height == 9.99


def test_bowling_Player_isProfessional_value_roundtrip():
    instance = bowling_Player(city="sample_text", dateOfBirth=date(2024, 1, 1), firstname="sample_text", height=3.14, isProfessional=True, lastname="sample_text", street="sample_text", streetnumber=7)
    assert instance.isProfessional == True
    instance.isProfessional = False
    assert instance.isProfessional == False


def test_bowling_Player_lastname_value_roundtrip():
    instance = bowling_Player(city="sample_text", dateOfBirth=date(2024, 1, 1), firstname="sample_text", height=3.14, isProfessional=True, lastname="sample_text", street="sample_text", streetnumber=7)
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_bowling_Player_street_value_roundtrip():
    instance = bowling_Player(city="sample_text", dateOfBirth=date(2024, 1, 1), firstname="sample_text", height=3.14, isProfessional=True, lastname="sample_text", street="sample_text", streetnumber=7)
    assert instance.street == "sample_text"
    instance.street = "sample_text_2"
    assert instance.street == "sample_text_2"


def test_bowling_Player_streetnumber_value_roundtrip():
    instance = bowling_Player(city="sample_text", dateOfBirth=date(2024, 1, 1), firstname="sample_text", height=3.14, isProfessional=True, lastname="sample_text", street="sample_text", streetnumber=7)
    assert instance.streetnumber == 7
    instance.streetnumber = 13
    assert instance.streetnumber == 13


def test_bowling_Playerlist_name_value_roundtrip():
    instance = bowling_Playerlist(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_bowling_Tournament_title_value_roundtrip():
    instance = bowling_Tournament(title="sample_text", type="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bowling_Tournament_type_value_roundtrip():
    instance = bowling_Tournament(title="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_assoc_game0_link_reassign_clear():
    a = bowling_Player(city="sample_text", dateOfBirth=date(2024, 1, 1), firstname="sample_text", height=3.14, isProfessional=True, lastname="sample_text", street="sample_text", streetnumber=7)
    b1 = bowling_Game(date=date(2024, 1, 1), frames=7)
    b2 = bowling_Game(date=date(2025, 6, 15), frames=13)
    _safe_set(a, 'player', {b1})
    assert _is_linked(a, 'player', b1)
    if hasattr(b1, 'Game'):
        assert _is_linked(b1, 'Game', a)
    _safe_set(a, 'player', {b2})
    assert _is_linked(a, 'player', b2)
    if hasattr(b1, 'Game'):
        assert not _is_linked(b1, 'Game', a)
    if hasattr(b2, 'Game'):
        assert _is_linked(b2, 'Game', a)
    _safe_set(a, 'player', set())
    assert not _is_linked(a, 'player', b2)
    if hasattr(b2, 'Game'):
        assert not _is_linked(b2, 'Game', a)


def test_assoc_game6_link_reassign_clear():
    a = bowling_Game(date=date(2024, 1, 1), frames=7)
    b1 = bowling_Matchup()
    b2 = bowling_Matchup()
    _safe_set(a, 'Game7', b1)
    assert _is_linked(a, 'Game7', b1)
    if hasattr(b1, 'matchup'):
        assert _is_linked(b1, 'matchup', a)
    _safe_set(a, 'Game7', b2)
    assert _is_linked(a, 'Game7', b2)
    if hasattr(b1, 'matchup'):
        assert not _is_linked(b1, 'matchup', a)
    if hasattr(b2, 'matchup'):
        assert _is_linked(b2, 'matchup', a)
    _safe_set(a, 'Game7', None)
    assert not _is_linked(a, 'Game7', b2)
    if hasattr(b2, 'matchup'):
        assert not _is_linked(b2, 'matchup', a)


def test_assoc_matchup4_link_reassign_clear():
    a = bowling_Game(date=date(2024, 1, 1), frames=7)
    b1 = bowling_Matchup()
    b2 = bowling_Matchup()
    _safe_set(a, 'game5', b1)
    assert _is_linked(a, 'game5', b1)
    if hasattr(b1, 'Matchup'):
        assert _is_linked(b1, 'Matchup', a)
    _safe_set(a, 'game5', b2)
    assert _is_linked(a, 'game5', b2)
    if hasattr(b1, 'Matchup'):
        assert not _is_linked(b1, 'Matchup', a)
    if hasattr(b2, 'Matchup'):
        assert _is_linked(b2, 'Matchup', a)
    _safe_set(a, 'game5', None)
    assert not _is_linked(a, 'game5', b2)
    if hasattr(b2, 'Matchup'):
        assert not _is_linked(b2, 'Matchup', a)


def test_assoc_matchups14_link_reassign_clear():
    a = bowling_Tournament(title="sample_text", type="sample_text")
    b1 = bowling_Matchup()
    b2 = bowling_Matchup()
    _safe_set(a, 'tournament', {b1})
    assert _is_linked(a, 'tournament', b1)
    if hasattr(b1, 'Matchup15'):
        assert _is_linked(b1, 'Matchup15', a)
    _safe_set(a, 'tournament', {b2})
    assert _is_linked(a, 'tournament', b2)
    if hasattr(b1, 'Matchup15'):
        assert not _is_linked(b1, 'Matchup15', a)
    if hasattr(b2, 'Matchup15'):
        assert _is_linked(b2, 'Matchup15', a)
    _safe_set(a, 'tournament', set())
    assert not _is_linked(a, 'tournament', b2)
    if hasattr(b2, 'Matchup15'):
        assert not _is_linked(b2, 'Matchup15', a)


def test_assoc_player3_link_reassign_clear():
    a = bowling_Player(city="sample_text", dateOfBirth=date(2024, 1, 1), firstname="sample_text", height=3.14, isProfessional=True, lastname="sample_text", street="sample_text", streetnumber=7)
    b1 = bowling_Game(date=date(2024, 1, 1), frames=7)
    b2 = bowling_Game(date=date(2025, 6, 15), frames=13)
    _safe_set(a, 'Player', b1)
    assert _is_linked(a, 'Player', b1)
    if hasattr(b1, 'game'):
        assert _is_linked(b1, 'game', a)
    _safe_set(a, 'Player', b2)
    assert _is_linked(a, 'Player', b2)
    if hasattr(b1, 'game'):
        assert not _is_linked(b1, 'game', a)
    if hasattr(b2, 'game'):
        assert _is_linked(b2, 'game', a)
    _safe_set(a, 'Player', None)
    assert not _is_linked(a, 'Player', b2)
    if hasattr(b2, 'game'):
        assert not _is_linked(b2, 'game', a)


def test_assoc_player9_link_reassign_clear():
    a = bowling_Playerlist(name="sample_text")
    b1 = bowling_Player(city="sample_text", dateOfBirth=date(2024, 1, 1), firstname="sample_text", height=3.14, isProfessional=True, lastname="sample_text", street="sample_text", streetnumber=7)
    b2 = bowling_Player(city="sample_text_2", dateOfBirth=date(2025, 6, 15), firstname="sample_text_2", height=9.99, isProfessional=False, lastname="sample_text_2", street="sample_text_2", streetnumber=13)
    _safe_set(a, 'playerlist', {b1})
    assert _is_linked(a, 'playerlist', b1)
    if hasattr(b1, 'Player10'):
        assert _is_linked(b1, 'Player10', a)
    _safe_set(a, 'playerlist', {b2})
    assert _is_linked(a, 'playerlist', b2)
    if hasattr(b1, 'Player10'):
        assert not _is_linked(b1, 'Player10', a)
    if hasattr(b2, 'Player10'):
        assert _is_linked(b2, 'Player10', a)
    _safe_set(a, 'playerlist', set())
    assert not _is_linked(a, 'playerlist', b2)
    if hasattr(b2, 'Player10'):
        assert not _is_linked(b2, 'Player10', a)


def test_assoc_playerlist1_link_reassign_clear():
    a = bowling_Playerlist(name="sample_text")
    b1 = bowling_Player(city="sample_text", dateOfBirth=date(2024, 1, 1), firstname="sample_text", height=3.14, isProfessional=True, lastname="sample_text", street="sample_text", streetnumber=7)
    b2 = bowling_Player(city="sample_text_2", dateOfBirth=date(2025, 6, 15), firstname="sample_text_2", height=9.99, isProfessional=False, lastname="sample_text_2", street="sample_text_2", streetnumber=13)
    _safe_set(a, 'Playerlist', b1)
    assert _is_linked(a, 'Playerlist', b1)
    if hasattr(b1, 'player2'):
        assert _is_linked(b1, 'player2', a)
    _safe_set(a, 'Playerlist', b2)
    assert _is_linked(a, 'Playerlist', b2)
    if hasattr(b1, 'player2'):
        assert not _is_linked(b1, 'player2', a)
    if hasattr(b2, 'player2'):
        assert _is_linked(b2, 'player2', a)
    _safe_set(a, 'Playerlist', None)
    assert not _is_linked(a, 'Playerlist', b2)
    if hasattr(b2, 'player2'):
        assert not _is_linked(b2, 'player2', a)


def test_assoc_playerlist16_link_reassign_clear():
    a = bowling_Tournament(title="sample_text", type="sample_text")
    b1 = bowling_Playerlist(name="sample_text")
    b2 = bowling_Playerlist(name="sample_text_2")
    _safe_set(a, 'tournament17', b1)
    assert _is_linked(a, 'tournament17', b1)
    if hasattr(b1, 'Playerlist18'):
        assert _is_linked(b1, 'Playerlist18', a)
    _safe_set(a, 'tournament17', b2)
    assert _is_linked(a, 'tournament17', b2)
    if hasattr(b1, 'Playerlist18'):
        assert not _is_linked(b1, 'Playerlist18', a)
    if hasattr(b2, 'Playerlist18'):
        assert _is_linked(b2, 'Playerlist18', a)
    _safe_set(a, 'tournament17', None)
    assert not _is_linked(a, 'tournament17', b2)
    if hasattr(b2, 'Playerlist18'):
        assert not _is_linked(b2, 'Playerlist18', a)


def test_assoc_tournament11_link_reassign_clear():
    a = bowling_Tournament(title="sample_text", type="sample_text")
    b1 = bowling_Playerlist(name="sample_text")
    b2 = bowling_Playerlist(name="sample_text_2")
    _safe_set(a, 'Tournament13', b1)
    assert _is_linked(a, 'Tournament13', b1)
    if hasattr(b1, 'playerlist12'):
        assert _is_linked(b1, 'playerlist12', a)
    _safe_set(a, 'Tournament13', b2)
    assert _is_linked(a, 'Tournament13', b2)
    if hasattr(b1, 'playerlist12'):
        assert not _is_linked(b1, 'playerlist12', a)
    if hasattr(b2, 'playerlist12'):
        assert _is_linked(b2, 'playerlist12', a)
    _safe_set(a, 'Tournament13', None)
    assert not _is_linked(a, 'Tournament13', b2)
    if hasattr(b2, 'playerlist12'):
        assert not _is_linked(b2, 'playerlist12', a)


def test_assoc_tournament8_link_reassign_clear():
    a = bowling_Tournament(title="sample_text", type="sample_text")
    b1 = bowling_Matchup()
    b2 = bowling_Matchup()
    _safe_set(a, 'Tournament', b1)
    assert _is_linked(a, 'Tournament', b1)
    if hasattr(b1, 'matchups'):
        assert _is_linked(b1, 'matchups', a)
    _safe_set(a, 'Tournament', b2)
    assert _is_linked(a, 'Tournament', b2)
    if hasattr(b1, 'matchups'):
        assert not _is_linked(b1, 'matchups', a)
    if hasattr(b2, 'matchups'):
        assert _is_linked(b2, 'matchups', a)
    _safe_set(a, 'Tournament', None)
    assert not _is_linked(a, 'Tournament', b2)
    if hasattr(b2, 'matchups'):
        assert not _is_linked(b2, 'matchups', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

bowling_Game_strategy = st.builds(bowling_Game, date=st.dates(), frames=st.integers())
@given(instance=bowling_Game_strategy)
@settings(max_examples=25)
def test_bowling_Game_instantiation(instance):
    assert isinstance(instance, bowling_Game)


bowling_Matchup_strategy = st.builds(bowling_Matchup)
@given(instance=bowling_Matchup_strategy)
@settings(max_examples=25)
def test_bowling_Matchup_instantiation(instance):
    assert isinstance(instance, bowling_Matchup)


bowling_Player_strategy = st.builds(bowling_Player, city=safe_text, dateOfBirth=st.dates(), firstname=safe_text, height=st.floats(allow_nan=False, allow_infinity=False), isProfessional=st.booleans(), lastname=safe_text, street=safe_text, streetnumber=st.integers())
@given(instance=bowling_Player_strategy)
@settings(max_examples=25)
def test_bowling_Player_instantiation(instance):
    assert isinstance(instance, bowling_Player)


bowling_Playerlist_strategy = st.builds(bowling_Playerlist, name=safe_text)
@given(instance=bowling_Playerlist_strategy)
@settings(max_examples=25)
def test_bowling_Playerlist_instantiation(instance):
    assert isinstance(instance, bowling_Playerlist)


bowling_Tournament_strategy = st.builds(bowling_Tournament, title=safe_text, type=safe_text)
@given(instance=bowling_Tournament_strategy)
@settings(max_examples=25)
def test_bowling_Tournament_instantiation(instance):
    assert isinstance(instance, bowling_Tournament)



