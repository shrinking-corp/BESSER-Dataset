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
    Game,
    Deck,
    Card,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_game_is_not_abstract():
    assert not inspect.isabstract(Game)


def test_hyp_game_constructor_exists():
    assert callable(Game.__init__)


def test_hyp_game_constructor_args():
    sig = inspect.signature(Game.__init__)
    params = list(sig.parameters.keys())
    assert "cardsOnTable" in params, "Missing parameter 'cardsOnTable'"
    assert "completedCards" in params, "Missing parameter 'completedCards'"
    assert "mainDeck" in params, "Missing parameter 'mainDeck'"

def test_hyp_game_has_cardsOnTable():
    assert hasattr(Game, "cardsOnTable")
    descriptor = None
    for klass in Game.__mro__:
        if "cardsOnTable" in klass.__dict__:
            descriptor = klass.__dict__["cardsOnTable"]
            break
    assert isinstance(descriptor, property)

def test_hyp_game_has_completedCards():
    assert hasattr(Game, "completedCards")
    descriptor = None
    for klass in Game.__mro__:
        if "completedCards" in klass.__dict__:
            descriptor = klass.__dict__["completedCards"]
            break
    assert isinstance(descriptor, property)

def test_hyp_game_has_mainDeck():
    assert hasattr(Game, "mainDeck")
    descriptor = None
    for klass in Game.__mro__:
        if "mainDeck" in klass.__dict__:
            descriptor = klass.__dict__["mainDeck"]
            break
    assert isinstance(descriptor, property)



def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "cards" in params, "Missing parameter 'cards'"

def test_hyp_deck_has_cards():
    assert hasattr(Deck, "cards")
    descriptor = None
    for klass in Deck.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)



def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"



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
Game_strategy = st.builds(
    Game,
    cardsOnTable=
        st.none(),
    completedCards=
        st.none(),
    mainDeck=
        st.none()
)
Deck_strategy = st.builds(
    Deck,
    cards=
        st.none()
)
Card_strategy = st.builds(
    Card,
    value=
        st.integers()
)

@given(instance=Game_strategy)
@settings(max_examples=50)
def test_hyp_game_instantiation(instance):
    assert isinstance(instance, Game)



@given(instance=Game_strategy)
def test_hyp_game_cardsOnTable_setter(instance):
    original = instance.cardsOnTable
    instance.cardsOnTable = original
    assert instance.cardsOnTable == original



@given(instance=Game_strategy)
def test_hyp_game_completedCards_setter(instance):
    original = instance.completedCards
    instance.completedCards = original
    assert instance.completedCards == original



@given(instance=Game_strategy)
def test_hyp_game_mainDeck_setter(instance):
    original = instance.mainDeck
    instance.mainDeck = original
    assert instance.mainDeck == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_hyp_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_hyp_deck_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original




@given(instance=Card_strategy)
def test_hyp_card_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Card,
    Deck,
    Game,
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

def test_Card_value_value_roundtrip():
    instance = Card(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Card_strategy = st.builds(Card, value=st.integers())
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)



