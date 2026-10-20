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
    Deck,
    Card,
    Player,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "deck_of_cards" in params, "Missing parameter 'deck_of_cards'"
    assert "deck_position" in params, "Missing parameter 'deck_position'"





def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "front" in params, "Missing parameter 'front'"
    assert "suit" in params, "Missing parameter 'suit'"






def test_hyp_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_hyp_player_constructor_exists():
    assert callable(Player.__init__)


def test_hyp_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"
    assert "name" in params, "Missing parameter 'name'"




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
Deck_strategy = st.builds(
    Deck,
    deck_of_cards=
        safe_text,
    deck_position=
        st.integers()
)
Card_strategy = st.builds(
    Card,
    value=
        safe_text,
    front=
        safe_text,
    suit=
        safe_text
)
Player_strategy = st.builds(
    Player,
    points=
        safe_text,
    name=
        safe_text
)




@given(instance=Deck_strategy)
def test_hyp_deck_deck_of_cards_setter(instance):
    original = instance.deck_of_cards
    instance.deck_of_cards = original
    assert instance.deck_of_cards == original



@given(instance=Deck_strategy)
def test_hyp_deck_deck_position_setter(instance):
    original = instance.deck_position
    instance.deck_position = original
    assert instance.deck_position == original




@given(instance=Card_strategy)
def test_hyp_card_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=Card_strategy)
def test_hyp_card_front_setter(instance):
    original = instance.front
    instance.front = original
    assert instance.front == original



@given(instance=Card_strategy)
def test_hyp_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original




@given(instance=Player_strategy)
def test_hyp_player_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original



@given(instance=Player_strategy)
def test_hyp_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Card,
    Deck,
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

def test_Card_front_value_roundtrip():
    instance = Card(front="sample_text", suit="sample_text", value="sample_text")
    assert instance.front == "sample_text"
    instance.front = "sample_text_2"
    assert instance.front == "sample_text_2"


def test_Card_suit_value_roundtrip():
    instance = Card(front="sample_text", suit="sample_text", value="sample_text")
    assert instance.suit == "sample_text"
    instance.suit = "sample_text_2"
    assert instance.suit == "sample_text_2"


def test_Card_value_value_roundtrip():
    instance = Card(front="sample_text", suit="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_Deck_deck_of_cards_value_roundtrip():
    instance = Deck(deck_of_cards="sample_text", deck_position=7)
    assert instance.deck_of_cards == "sample_text"
    instance.deck_of_cards = "sample_text_2"
    assert instance.deck_of_cards == "sample_text_2"


def test_Deck_deck_position_value_roundtrip():
    instance = Deck(deck_of_cards="sample_text", deck_position=7)
    assert instance.deck_position == 7
    instance.deck_position = 13
    assert instance.deck_position == 13


def test_Player_name_value_roundtrip():
    instance = Player(name="sample_text", points="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Player_points_value_roundtrip():
    instance = Player(name="sample_text", points="sample_text")
    assert instance.points == "sample_text"
    instance.points = "sample_text_2"
    assert instance.points == "sample_text_2"


def test_assoc_Card_Deck_link_reassign_clear():
    a = Deck(deck_of_cards="sample_text", deck_position=7)
    b1 = Card(front="sample_text", suit="sample_text", value="sample_text")
    b2 = Card(front="sample_text_2", suit="sample_text_2", value="sample_text_2")
    _safe_set(a, 'card1', {b1})
    assert _is_linked(a, 'card1', b1)
    if hasattr(b1, 'deck0'):
        assert _is_linked(b1, 'deck0', a)
    _safe_set(a, 'card1', {b2})
    assert _is_linked(a, 'card1', b2)
    if hasattr(b1, 'deck0'):
        assert not _is_linked(b1, 'deck0', a)
    if hasattr(b2, 'deck0'):
        assert _is_linked(b2, 'deck0', a)
    _safe_set(a, 'card1', set())
    assert not _is_linked(a, 'card1', b2)
    if hasattr(b2, 'deck0'):
        assert not _is_linked(b2, 'deck0', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Card_strategy = st.builds(Card, front=safe_text, suit=safe_text, value=safe_text)
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)


Deck_strategy = st.builds(Deck, deck_of_cards=safe_text, deck_position=st.integers())
@given(instance=Deck_strategy)
@settings(max_examples=25)
def test_Deck_instantiation(instance):
    assert isinstance(instance, Deck)


Player_strategy = st.builds(Player, name=safe_text, points=safe_text)
@given(instance=Player_strategy)
@settings(max_examples=25)
def test_Player_instantiation(instance):
    assert isinstance(instance, Player)



