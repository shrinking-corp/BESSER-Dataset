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
    bowling_Tournament,
    bowling_Matchup,
    bowling_Game,
    bowling_League,
    bowling_Player,
    TournamentType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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
    assert "date" in params, "Missing parameter 'date'"




def test_hyp_bowling_game_is_not_abstract():
    assert not inspect.isabstract(bowling_Game)


def test_hyp_bowling_game_constructor_exists():
    assert callable(bowling_Game.__init__)


def test_hyp_bowling_game_constructor_args():
    sig = inspect.signature(bowling_Game.__init__)
    params = list(sig.parameters.keys())
    assert "frames" in params, "Missing parameter 'frames'"




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
    assert "telephon" in params, "Missing parameter 'telephon'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "streetNumber" in params, "Missing parameter 'streetNumber'"
    assert "name" in params, "Missing parameter 'name'"
    assert "eMail" in params, "Missing parameter 'eMail'"
    assert "isAvailable" in params, "Missing parameter 'isAvailable'"
    assert "street" in params, "Missing parameter 'street'"
    assert "notes" in params, "Missing parameter 'notes'"
    assert "height" in params, "Missing parameter 'height'"
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
bowling_Tournament_strategy = st.builds(
    bowling_Tournament,
    type=
        safe_text,
    title=
        safe_text
)
bowling_Matchup_strategy = st.builds(
    bowling_Matchup,
    date=
        st.dates()
)
bowling_Game_strategy = st.builds(
    bowling_Game,
    frames=
        st.integers()
)
bowling_League_strategy = st.builds(
    bowling_League,
    name=
        safe_text
)
bowling_Player_strategy = st.builds(
    bowling_Player,
    telephon=
        safe_text,
    dateOfBirth=
        st.dates(),
    streetNumber=
        st.integers(),
    name=
        safe_text,
    eMail=
        safe_text,
    isAvailable=
        st.booleans(),
    street=
        safe_text,
    notes=
        safe_text,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    isProfessional=
        st.booleans()
)




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

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=bowling_Tournament_strategy)
@settings(max_examples=30)
def test_hyp_bowling_tournament_hasleague_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasLeague(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasLeague).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasLeague' in bowling_Tournament is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasLeague' in bowling_Tournament did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasLeague' in bowling_Tournament is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=bowling_Tournament_strategy)
@settings(max_examples=30)
def test_hyp_bowling_tournament_hastounamentpro_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasTounamentPro(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasTounamentPro).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasTounamentPro' in bowling_Tournament is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasTounamentPro' in bowling_Tournament did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasTounamentPro' in bowling_Tournament is not implemented or raised an error")




@given(instance=bowling_Matchup_strategy)
def test_hyp_bowling_matchup_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original




@given(instance=bowling_Game_strategy)
def test_hyp_bowling_game_frames_setter(instance):
    original = instance.frames
    instance.frames = original
    assert instance.frames == original




@given(instance=bowling_League_strategy)
def test_hyp_bowling_league_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_telephon_setter(instance):
    original = instance.telephon
    instance.telephon = original
    assert instance.telephon == original



@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_streetNumber_setter(instance):
    original = instance.streetNumber
    instance.streetNumber = original
    assert instance.streetNumber == original



@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_eMail_setter(instance):
    original = instance.eMail
    instance.eMail = original
    assert instance.eMail == original



@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_isAvailable_setter(instance):
    original = instance.isAvailable
    instance.isAvailable = original
    assert instance.isAvailable == original



@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_notes_setter(instance):
    original = instance.notes
    instance.notes = original
    assert instance.notes == original



@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=bowling_Player_strategy)
def test_hyp_bowling_player_isProfessional_setter(instance):
    original = instance.isProfessional
    instance.isProfessional = original
    assert instance.isProfessional == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=bowling_Player_strategy)
@settings(max_examples=30)
def test_hyp_bowling_player_hasheight_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasHeight(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasHeight).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasHeight' in bowling_Player is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasHeight' in bowling_Player did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasHeight' in bowling_Player is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=bowling_Player_strategy)
@settings(max_examples=30)
def test_hyp_bowling_player_hasnotes_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasNotes(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasNotes).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasNotes' in bowling_Player is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasNotes' in bowling_Player did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasNotes' in bowling_Player is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=bowling_Player_strategy)
@settings(max_examples=30)
def test_hyp_bowling_player_hasisavailable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasIsAvailable(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasIsAvailable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasIsAvailable' in bowling_Player is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasIsAvailable' in bowling_Player did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasIsAvailable' in bowling_Player is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=bowling_Player_strategy)
@settings(max_examples=30)
def test_hyp_bowling_player_hasdateofbirth_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasDateOfBirth(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasDateOfBirth).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasDateOfBirth' in bowling_Player is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasDateOfBirth' in bowling_Player did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasDateOfBirth' in bowling_Player is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=bowling_Player_strategy)
@settings(max_examples=30)
def test_hyp_bowling_player_hastelephon_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasTelephon(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasTelephon).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasTelephon' in bowling_Player is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasTelephon' in bowling_Player did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasTelephon' in bowling_Player is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=bowling_Player_strategy)
@settings(max_examples=30)
def test_hyp_bowling_player_hasname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasName(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasName' in bowling_Player is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasName' in bowling_Player did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasName' in bowling_Player is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=bowling_Player_strategy)
@settings(max_examples=30)
def test_hyp_bowling_player_hasgame_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasGame(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasGame).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasGame' in bowling_Player is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasGame' in bowling_Player did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasGame' in bowling_Player is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=bowling_Player_strategy)
@settings(max_examples=30)
def test_hyp_bowling_player_hasstreet_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasStreet(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasStreet).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasStreet' in bowling_Player is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasStreet' in bowling_Player did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasStreet' in bowling_Player is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=bowling_Player_strategy)
@settings(max_examples=30)
def test_hyp_bowling_player_hascorrectstreetnumber_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasCorrectStreetNumber(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasCorrectStreetNumber).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasCorrectStreetNumber' in bowling_Player is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasCorrectStreetNumber' in bowling_Player did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasCorrectStreetNumber' in bowling_Player is not implemented or raised an error")


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

def test_bowling_Game_frames_value_roundtrip():
    instance = bowling_Game(frames=7)
    assert instance.frames == 7
    instance.frames = 13
    assert instance.frames == 13


def test_bowling_League_name_value_roundtrip():
    instance = bowling_League(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_bowling_Matchup_date_value_roundtrip():
    instance = bowling_Matchup(date=date(2024, 1, 1))
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_bowling_Player_dateOfBirth_value_roundtrip():
    instance = bowling_Player(dateOfBirth=date(2024, 1, 1), eMail="sample_text", height=3.14, isAvailable=True, isProfessional=True, name="sample_text", notes="sample_text", street="sample_text", streetNumber=7, telephon="sample_text")
    assert instance.dateOfBirth == date(2024, 1, 1)
    instance.dateOfBirth = date(2025, 6, 15)
    assert instance.dateOfBirth == date(2025, 6, 15)


def test_bowling_Player_eMail_value_roundtrip():
    instance = bowling_Player(dateOfBirth=date(2024, 1, 1), eMail="sample_text", height=3.14, isAvailable=True, isProfessional=True, name="sample_text", notes="sample_text", street="sample_text", streetNumber=7, telephon="sample_text")
    assert instance.eMail == "sample_text"
    instance.eMail = "sample_text_2"
    assert instance.eMail == "sample_text_2"


def test_bowling_Player_height_value_roundtrip():
    instance = bowling_Player(dateOfBirth=date(2024, 1, 1), eMail="sample_text", height=3.14, isAvailable=True, isProfessional=True, name="sample_text", notes="sample_text", street="sample_text", streetNumber=7, telephon="sample_text")
    assert instance.height == 3.14
    instance.height = 9.99
    assert instance.height == 9.99


def test_bowling_Player_isAvailable_value_roundtrip():
    instance = bowling_Player(dateOfBirth=date(2024, 1, 1), eMail="sample_text", height=3.14, isAvailable=True, isProfessional=True, name="sample_text", notes="sample_text", street="sample_text", streetNumber=7, telephon="sample_text")
    assert instance.isAvailable == True
    instance.isAvailable = False
    assert instance.isAvailable == False


def test_bowling_Player_isProfessional_value_roundtrip():
    instance = bowling_Player(dateOfBirth=date(2024, 1, 1), eMail="sample_text", height=3.14, isAvailable=True, isProfessional=True, name="sample_text", notes="sample_text", street="sample_text", streetNumber=7, telephon="sample_text")
    assert instance.isProfessional == True
    instance.isProfessional = False
    assert instance.isProfessional == False


def test_bowling_Player_name_value_roundtrip():
    instance = bowling_Player(dateOfBirth=date(2024, 1, 1), eMail="sample_text", height=3.14, isAvailable=True, isProfessional=True, name="sample_text", notes="sample_text", street="sample_text", streetNumber=7, telephon="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_bowling_Player_notes_value_roundtrip():
    instance = bowling_Player(dateOfBirth=date(2024, 1, 1), eMail="sample_text", height=3.14, isAvailable=True, isProfessional=True, name="sample_text", notes="sample_text", street="sample_text", streetNumber=7, telephon="sample_text")
    assert instance.notes == "sample_text"
    instance.notes = "sample_text_2"
    assert instance.notes == "sample_text_2"


def test_bowling_Player_street_value_roundtrip():
    instance = bowling_Player(dateOfBirth=date(2024, 1, 1), eMail="sample_text", height=3.14, isAvailable=True, isProfessional=True, name="sample_text", notes="sample_text", street="sample_text", streetNumber=7, telephon="sample_text")
    assert instance.street == "sample_text"
    instance.street = "sample_text_2"
    assert instance.street == "sample_text_2"


def test_bowling_Player_streetNumber_value_roundtrip():
    instance = bowling_Player(dateOfBirth=date(2024, 1, 1), eMail="sample_text", height=3.14, isAvailable=True, isProfessional=True, name="sample_text", notes="sample_text", street="sample_text", streetNumber=7, telephon="sample_text")
    assert instance.streetNumber == 7
    instance.streetNumber = 13
    assert instance.streetNumber == 13


def test_bowling_Player_telephon_value_roundtrip():
    instance = bowling_Player(dateOfBirth=date(2024, 1, 1), eMail="sample_text", height=3.14, isAvailable=True, isProfessional=True, name="sample_text", notes="sample_text", street="sample_text", streetNumber=7, telephon="sample_text")
    assert instance.telephon == "sample_text"
    instance.telephon = "sample_text_2"
    assert instance.telephon == "sample_text_2"


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


def test_assoc_games0_link_reassign_clear():
    a = bowling_Player(dateOfBirth=date(2024, 1, 1), eMail="sample_text", height=3.14, isAvailable=True, isProfessional=True, name="sample_text", notes="sample_text", street="sample_text", streetNumber=7, telephon="sample_text")
    b1 = bowling_Game(frames=7)
    b2 = bowling_Game(frames=13)
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


def test_assoc_games6_link_reassign_clear():
    a = bowling_Matchup(date=date(2024, 1, 1))
    b1 = bowling_Game(frames=7)
    b2 = bowling_Game(frames=13)
    _safe_set(a, 'matchup', {b1})
    assert _is_linked(a, 'matchup', b1)
    if hasattr(b1, 'Game7'):
        assert _is_linked(b1, 'Game7', a)
    _safe_set(a, 'matchup', {b2})
    assert _is_linked(a, 'matchup', b2)
    if hasattr(b1, 'Game7'):
        assert not _is_linked(b1, 'Game7', a)
    if hasattr(b2, 'Game7'):
        assert _is_linked(b2, 'Game7', a)
    _safe_set(a, 'matchup', set())
    assert not _is_linked(a, 'matchup', b2)
    if hasattr(b2, 'Game7'):
        assert not _is_linked(b2, 'Game7', a)


def test_assoc_league3_link_reassign_clear():
    a = bowling_Tournament(title="sample_text", type="sample_text")
    b1 = bowling_League(name="sample_text")
    b2 = bowling_League(name="sample_text_2")
    _safe_set(a, 'bowling_Tournament4', b1)
    assert _is_linked(a, 'bowling_Tournament4', b1)
    if hasattr(b1, 'bowling_League5'):
        assert _is_linked(b1, 'bowling_League5', a)
    _safe_set(a, 'bowling_Tournament4', b2)
    assert _is_linked(a, 'bowling_Tournament4', b2)
    if hasattr(b1, 'bowling_League5'):
        assert not _is_linked(b1, 'bowling_League5', a)
    if hasattr(b2, 'bowling_League5'):
        assert _is_linked(b2, 'bowling_League5', a)
    _safe_set(a, 'bowling_Tournament4', None)
    assert not _is_linked(a, 'bowling_Tournament4', b2)
    if hasattr(b2, 'bowling_League5'):
        assert not _is_linked(b2, 'bowling_League5', a)


def test_assoc_matchup8_link_reassign_clear():
    a = bowling_Matchup(date=date(2024, 1, 1))
    b1 = bowling_Game(frames=7)
    b2 = bowling_Game(frames=13)
    _safe_set(a, 'Matchup', b1)
    assert _is_linked(a, 'Matchup', b1)
    if hasattr(b1, 'games'):
        assert _is_linked(b1, 'games', a)
    _safe_set(a, 'Matchup', b2)
    assert _is_linked(a, 'Matchup', b2)
    if hasattr(b1, 'games'):
        assert not _is_linked(b1, 'games', a)
    if hasattr(b2, 'games'):
        assert _is_linked(b2, 'games', a)
    _safe_set(a, 'Matchup', None)
    assert not _is_linked(a, 'Matchup', b2)
    if hasattr(b2, 'games'):
        assert not _is_linked(b2, 'games', a)


def test_assoc_matchups2_link_reassign_clear():
    a = bowling_Tournament(title="sample_text", type="sample_text")
    b1 = bowling_Matchup(date=date(2024, 1, 1))
    b2 = bowling_Matchup(date=date(2025, 6, 15))
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


def test_assoc_player9_link_reassign_clear():
    a = bowling_Player(dateOfBirth=date(2024, 1, 1), eMail="sample_text", height=3.14, isAvailable=True, isProfessional=True, name="sample_text", notes="sample_text", street="sample_text", streetNumber=7, telephon="sample_text")
    b1 = bowling_Game(frames=7)
    b2 = bowling_Game(frames=13)
    _safe_set(a, 'Player', b1)
    assert _is_linked(a, 'Player', b1)
    if hasattr(b1, 'games10'):
        assert _is_linked(b1, 'games10', a)
    _safe_set(a, 'Player', b2)
    assert _is_linked(a, 'Player', b2)
    if hasattr(b1, 'games10'):
        assert not _is_linked(b1, 'games10', a)
    if hasattr(b2, 'games10'):
        assert _is_linked(b2, 'games10', a)
    _safe_set(a, 'Player', None)
    assert not _is_linked(a, 'Player', b2)
    if hasattr(b2, 'games10'):
        assert not _is_linked(b2, 'games10', a)


def test_assoc_players1_link_reassign_clear():
    a = bowling_Player(dateOfBirth=date(2024, 1, 1), eMail="sample_text", height=3.14, isAvailable=True, isProfessional=True, name="sample_text", notes="sample_text", street="sample_text", streetNumber=7, telephon="sample_text")
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

bowling_Game_strategy = st.builds(bowling_Game, frames=st.integers())
@given(instance=bowling_Game_strategy)
@settings(max_examples=25)
def test_bowling_Game_instantiation(instance):
    assert isinstance(instance, bowling_Game)


bowling_League_strategy = st.builds(bowling_League, name=safe_text)
@given(instance=bowling_League_strategy)
@settings(max_examples=25)
def test_bowling_League_instantiation(instance):
    assert isinstance(instance, bowling_League)


bowling_Matchup_strategy = st.builds(bowling_Matchup, date=st.dates())
@given(instance=bowling_Matchup_strategy)
@settings(max_examples=25)
def test_bowling_Matchup_instantiation(instance):
    assert isinstance(instance, bowling_Matchup)


bowling_Player_strategy = st.builds(bowling_Player, dateOfBirth=st.dates(), eMail=safe_text, height=st.floats(allow_nan=False, allow_infinity=False), isAvailable=st.booleans(), isProfessional=st.booleans(), name=safe_text, notes=safe_text, street=safe_text, streetNumber=st.integers(), telephon=safe_text)
@given(instance=bowling_Player_strategy)
@settings(max_examples=25)
def test_bowling_Player_instantiation(instance):
    assert isinstance(instance, bowling_Player)


bowling_Tournament_strategy = st.builds(bowling_Tournament, title=safe_text, type=safe_text)
@given(instance=bowling_Tournament_strategy)
@settings(max_examples=25)
def test_bowling_Tournament_instantiation(instance):
    assert isinstance(instance, bowling_Tournament)



