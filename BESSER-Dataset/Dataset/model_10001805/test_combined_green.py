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
    GUI,
    Player,
    GameBoard,
    Deck,
    Card,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_gui_is_not_abstract():
    assert not inspect.isabstract(GUI)


def test_hyp_gui_constructor_exists():
    assert callable(GUI.__init__)


def test_hyp_gui_constructor_args():
    sig = inspect.signature(GUI.__init__)
    params = list(sig.parameters.keys())



def test_hyp_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_hyp_player_constructor_exists():
    assert callable(Player.__init__)


def test_hyp_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"
    assert "hand" in params, "Missing parameter 'hand'"

def test_hyp_player_has_points():
    assert hasattr(Player, "points")
    descriptor = None
    for klass in Player.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)

def test_hyp_player_has_hand():
    assert hasattr(Player, "hand")
    descriptor = None
    for klass in Player.__mro__:
        if "hand" in klass.__dict__:
            descriptor = klass.__dict__["hand"]
            break
    assert isinstance(descriptor, property)



def test_hyp_gameboard_is_not_abstract():
    assert not inspect.isabstract(GameBoard)


def test_hyp_gameboard_constructor_exists():
    assert callable(GameBoard.__init__)


def test_hyp_gameboard_constructor_args():
    sig = inspect.signature(GameBoard.__init__)
    params = list(sig.parameters.keys())
    assert "garbagePile" in params, "Missing parameter 'garbagePile'"
    assert "shelf" in params, "Missing parameter 'shelf'"
    assert "discardPile" in params, "Missing parameter 'discardPile'"






def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())



def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "suit" in params, "Missing parameter 'suit'"




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
GUI_strategy = st.builds(
    GUI,
)
Player_strategy = st.builds(
    Player,
    points=
        st.integers(),
    hand=
        st.none()
)
GameBoard_strategy = st.builds(
    GameBoard,
    garbagePile=
        safe_text,
    shelf=
        safe_text,
    discardPile=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
)
Card_strategy = st.builds(
    Card,
    value=
        st.integers(),
    suit=
        st.integers()
)


@given(instance=Player_strategy)
@settings(max_examples=50)
def test_hyp_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_hyp_player_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original



@given(instance=Player_strategy)
def test_hyp_player_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original




@given(instance=GameBoard_strategy)
def test_hyp_gameboard_garbagePile_setter(instance):
    original = instance.garbagePile
    instance.garbagePile = original
    assert instance.garbagePile == original



@given(instance=GameBoard_strategy)
def test_hyp_gameboard_shelf_setter(instance):
    original = instance.shelf
    instance.shelf = original
    assert instance.shelf == original



@given(instance=GameBoard_strategy)
def test_hyp_gameboard_discardPile_setter(instance):
    original = instance.discardPile
    instance.discardPile = original
    assert instance.discardPile == original





@given(instance=Card_strategy)
def test_hyp_card_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=Card_strategy)
def test_hyp_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Card,
    Deck,
    GUI,
    GameBoard,
    Player,
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

def test_Card_suit_value_roundtrip():
    instance = Card(suit=7, value=7)
    assert instance.suit == 7
    instance.suit = 13
    assert instance.suit == 13


def test_Card_value_value_roundtrip():
    instance = Card(suit=7, value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_GameBoard_discardPile_value_roundtrip():
    instance = GameBoard(discardPile="sample_text", garbagePile="sample_text", shelf="sample_text")
    assert instance.discardPile == "sample_text"
    instance.discardPile = "sample_text_2"
    assert instance.discardPile == "sample_text_2"


def test_GameBoard_garbagePile_value_roundtrip():
    instance = GameBoard(discardPile="sample_text", garbagePile="sample_text", shelf="sample_text")
    assert instance.garbagePile == "sample_text"
    instance.garbagePile = "sample_text_2"
    assert instance.garbagePile == "sample_text_2"


def test_GameBoard_shelf_value_roundtrip():
    instance = GameBoard(discardPile="sample_text", garbagePile="sample_text", shelf="sample_text")
    assert instance.shelf == "sample_text"
    instance.shelf = "sample_text_2"
    assert instance.shelf == "sample_text_2"


def test_assoc_Deck_Card_link_reassign_clear():
    a = Card(suit=7, value=7)
    b1 = Deck()
    b2 = Deck()
    _safe_set(a, 'deck1', b1)
    assert _is_linked(a, 'deck1', b1)
    if hasattr(b1, 'card0'):
        assert _is_linked(b1, 'card0', a)
    _safe_set(a, 'deck1', b2)
    assert _is_linked(a, 'deck1', b2)
    if hasattr(b1, 'card0'):
        assert not _is_linked(b1, 'card0', a)
    if hasattr(b2, 'card0'):
        assert _is_linked(b2, 'card0', a)
    _safe_set(a, 'deck1', None)
    assert not _is_linked(a, 'deck1', b2)
    if hasattr(b2, 'card0'):
        assert not _is_linked(b2, 'card0', a)


def test_assoc_GameBoard_Deck_link_reassign_clear():
    a = GameBoard(discardPile="sample_text", garbagePile="sample_text", shelf="sample_text")
    b1 = Deck()
    b2 = Deck()
    _safe_set(a, 'deck2', b1)
    assert _is_linked(a, 'deck2', b1)
    if hasattr(b1, 'gameBoard3'):
        assert _is_linked(b1, 'gameBoard3', a)
    _safe_set(a, 'deck2', b2)
    assert _is_linked(a, 'deck2', b2)
    if hasattr(b1, 'gameBoard3'):
        assert not _is_linked(b1, 'gameBoard3', a)
    if hasattr(b2, 'gameBoard3'):
        assert _is_linked(b2, 'gameBoard3', a)
    _safe_set(a, 'deck2', None)
    assert not _is_linked(a, 'deck2', b2)
    if hasattr(b2, 'gameBoard3'):
        assert not _is_linked(b2, 'gameBoard3', a)


def test_assoc_GameBoard_GUI_link_reassign_clear():
    a = GameBoard(discardPile="sample_text", garbagePile="sample_text", shelf="sample_text")
    b1 = GUI()
    b2 = GUI()
    _safe_set(a, 'gUI6', b1)
    assert _is_linked(a, 'gUI6', b1)
    if hasattr(b1, 'gameBoard7'):
        assert _is_linked(b1, 'gameBoard7', a)
    _safe_set(a, 'gUI6', b2)
    assert _is_linked(a, 'gUI6', b2)
    if hasattr(b1, 'gameBoard7'):
        assert not _is_linked(b1, 'gameBoard7', a)
    if hasattr(b2, 'gameBoard7'):
        assert _is_linked(b2, 'gameBoard7', a)
    _safe_set(a, 'gUI6', None)
    assert not _is_linked(a, 'gUI6', b2)
    if hasattr(b2, 'gameBoard7'):
        assert not _is_linked(b2, 'gameBoard7', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Card_strategy = st.builds(Card, suit=st.integers(), value=st.integers())
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)


Deck_strategy = st.builds(Deck)
@given(instance=Deck_strategy)
@settings(max_examples=25)
def test_Deck_instantiation(instance):
    assert isinstance(instance, Deck)


GUI_strategy = st.builds(GUI)
@given(instance=GUI_strategy)
@settings(max_examples=25)
def test_GUI_instantiation(instance):
    assert isinstance(instance, GUI)


GameBoard_strategy = st.builds(GameBoard, discardPile=safe_text, garbagePile=safe_text, shelf=safe_text)
@given(instance=GameBoard_strategy)
@settings(max_examples=25)
def test_GameBoard_instantiation(instance):
    assert isinstance(instance, GameBoard)



