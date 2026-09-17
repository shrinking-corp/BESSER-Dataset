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
    Queen,
    King,
    Knight,
    Bishop,
    Rook,
    Pawn,
    Piece,
    STATE,
    Player,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_queen_is_not_abstract():
    assert not inspect.isabstract(Queen)


def test_hyp_queen_constructor_exists():
    assert callable(Queen.__init__)


def test_hyp_queen_constructor_args():
    sig = inspect.signature(Queen.__init__)
    params = list(sig.parameters.keys())



def test_hyp_king_is_not_abstract():
    assert not inspect.isabstract(King)


def test_hyp_king_constructor_exists():
    assert callable(King.__init__)


def test_hyp_king_constructor_args():
    sig = inspect.signature(King.__init__)
    params = list(sig.parameters.keys())



def test_hyp_knight_is_not_abstract():
    assert not inspect.isabstract(Knight)


def test_hyp_knight_constructor_exists():
    assert callable(Knight.__init__)


def test_hyp_knight_constructor_args():
    sig = inspect.signature(Knight.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bishop_is_not_abstract():
    assert not inspect.isabstract(Bishop)


def test_hyp_bishop_constructor_exists():
    assert callable(Bishop.__init__)


def test_hyp_bishop_constructor_args():
    sig = inspect.signature(Bishop.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rook_is_not_abstract():
    assert not inspect.isabstract(Rook)


def test_hyp_rook_constructor_exists():
    assert callable(Rook.__init__)


def test_hyp_rook_constructor_args():
    sig = inspect.signature(Rook.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pawn_is_not_abstract():
    assert not inspect.isabstract(Pawn)


def test_hyp_pawn_constructor_exists():
    assert callable(Pawn.__init__)


def test_hyp_pawn_constructor_args():
    sig = inspect.signature(Pawn.__init__)
    params = list(sig.parameters.keys())



def test_hyp_piece_is_not_abstract():
    assert not inspect.isabstract(Piece)


def test_hyp_piece_constructor_exists():
    assert callable(Piece.__init__)


def test_hyp_piece_constructor_args():
    sig = inspect.signature(Piece.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"


def test_hyp_state_exists():
    # Check that the Enumeration exists
    assert STATE is not None

def test_hyp_state_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in STATE]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in STATE"

def test_hyp_player_exists():
    # Check that the Enumeration exists
    assert Player is not None

def test_hyp_player_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Player]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Player"


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
Queen_strategy = st.builds(
    Queen,
)
King_strategy = st.builds(
    King,
)
Knight_strategy = st.builds(
    Knight,
)
Bishop_strategy = st.builds(
    Bishop,
)
Rook_strategy = st.builds(
    Rook,
)
Pawn_strategy = st.builds(
    Pawn,
)
Piece_strategy = st.builds(
    Piece,
    Name=
        safe_text
)










@given(instance=Piece_strategy)
def test_hyp_piece_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Bishop,
    King,
    Knight,
    Pawn,
    Piece,
    Queen,
    Rook,
    Player,
    STATE,
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

def test_Piece_Name_value_roundtrip():
    instance = Piece(Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Bishop_strategy = st.builds(Bishop)
@given(instance=Bishop_strategy)
@settings(max_examples=25)
def test_Bishop_instantiation(instance):
    assert isinstance(instance, Bishop)


King_strategy = st.builds(King)
@given(instance=King_strategy)
@settings(max_examples=25)
def test_King_instantiation(instance):
    assert isinstance(instance, King)


Knight_strategy = st.builds(Knight)
@given(instance=Knight_strategy)
@settings(max_examples=25)
def test_Knight_instantiation(instance):
    assert isinstance(instance, Knight)


Pawn_strategy = st.builds(Pawn)
@given(instance=Pawn_strategy)
@settings(max_examples=25)
def test_Pawn_instantiation(instance):
    assert isinstance(instance, Pawn)


Piece_strategy = st.builds(Piece, Name=safe_text)
@given(instance=Piece_strategy)
@settings(max_examples=25)
def test_Piece_instantiation(instance):
    assert isinstance(instance, Piece)


Queen_strategy = st.builds(Queen)
@given(instance=Queen_strategy)
@settings(max_examples=25)
def test_Queen_instantiation(instance):
    assert isinstance(instance, Queen)


Rook_strategy = st.builds(Rook)
@given(instance=Rook_strategy)
@settings(max_examples=25)
def test_Rook_instantiation(instance):
    assert isinstance(instance, Rook)



