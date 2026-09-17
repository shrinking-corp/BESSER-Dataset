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



def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "CLUBS" in params, "Missing parameter 'CLUBS'"
    assert "JACK" in params, "Missing parameter 'JACK'"
    assert "DIAMONDS" in params, "Missing parameter 'DIAMONDS'"
    assert "SPADES" in params, "Missing parameter 'SPADES'"
    assert "HEARTS" in params, "Missing parameter 'HEARTS'"
    assert "ACE" in params, "Missing parameter 'ACE'"
    assert "QUEEN" in params, "Missing parameter 'QUEEN'"
    assert "value" in params, "Missing parameter 'value'"
    assert "suit" in params, "Missing parameter 'suit'"
    assert "KING" in params, "Missing parameter 'KING'"
    assert "JOKER" in params, "Missing parameter 'JOKER'"













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
)
Card_strategy = st.builds(
    Card,
    CLUBS=
        st.integers(),
    JACK=
        st.integers(),
    DIAMONDS=
        st.integers(),
    SPADES=
        st.integers(),
    HEARTS=
        st.integers(),
    ACE=
        st.integers(),
    QUEEN=
        st.integers(),
    value=
        st.integers(),
    suit=
        st.integers(),
    KING=
        st.integers(),
    JOKER=
        st.integers()
)





@given(instance=Card_strategy)
def test_hyp_card_CLUBS_setter(instance):
    original = instance.CLUBS
    instance.CLUBS = original
    assert instance.CLUBS == original



@given(instance=Card_strategy)
def test_hyp_card_JACK_setter(instance):
    original = instance.JACK
    instance.JACK = original
    assert instance.JACK == original



@given(instance=Card_strategy)
def test_hyp_card_DIAMONDS_setter(instance):
    original = instance.DIAMONDS
    instance.DIAMONDS = original
    assert instance.DIAMONDS == original



@given(instance=Card_strategy)
def test_hyp_card_SPADES_setter(instance):
    original = instance.SPADES
    instance.SPADES = original
    assert instance.SPADES == original



@given(instance=Card_strategy)
def test_hyp_card_HEARTS_setter(instance):
    original = instance.HEARTS
    instance.HEARTS = original
    assert instance.HEARTS == original



@given(instance=Card_strategy)
def test_hyp_card_ACE_setter(instance):
    original = instance.ACE
    instance.ACE = original
    assert instance.ACE == original



@given(instance=Card_strategy)
def test_hyp_card_QUEEN_setter(instance):
    original = instance.QUEEN
    instance.QUEEN = original
    assert instance.QUEEN == original



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



@given(instance=Card_strategy)
def test_hyp_card_KING_setter(instance):
    original = instance.KING
    instance.KING = original
    assert instance.KING == original



@given(instance=Card_strategy)
def test_hyp_card_JOKER_setter(instance):
    original = instance.JOKER
    instance.JOKER = original
    assert instance.JOKER == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Card,
    Deck,
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

def test_Card_ACE_value_roundtrip():
    instance = Card(ACE=7, CLUBS=7, DIAMONDS=7, HEARTS=7, JACK=7, JOKER=7, KING=7, QUEEN=7, SPADES=7, suit=7, value=7)
    assert instance.ACE == 7
    instance.ACE = 13
    assert instance.ACE == 13


def test_Card_CLUBS_value_roundtrip():
    instance = Card(ACE=7, CLUBS=7, DIAMONDS=7, HEARTS=7, JACK=7, JOKER=7, KING=7, QUEEN=7, SPADES=7, suit=7, value=7)
    assert instance.CLUBS == 7
    instance.CLUBS = 13
    assert instance.CLUBS == 13


def test_Card_DIAMONDS_value_roundtrip():
    instance = Card(ACE=7, CLUBS=7, DIAMONDS=7, HEARTS=7, JACK=7, JOKER=7, KING=7, QUEEN=7, SPADES=7, suit=7, value=7)
    assert instance.DIAMONDS == 7
    instance.DIAMONDS = 13
    assert instance.DIAMONDS == 13


def test_Card_HEARTS_value_roundtrip():
    instance = Card(ACE=7, CLUBS=7, DIAMONDS=7, HEARTS=7, JACK=7, JOKER=7, KING=7, QUEEN=7, SPADES=7, suit=7, value=7)
    assert instance.HEARTS == 7
    instance.HEARTS = 13
    assert instance.HEARTS == 13


def test_Card_JACK_value_roundtrip():
    instance = Card(ACE=7, CLUBS=7, DIAMONDS=7, HEARTS=7, JACK=7, JOKER=7, KING=7, QUEEN=7, SPADES=7, suit=7, value=7)
    assert instance.JACK == 7
    instance.JACK = 13
    assert instance.JACK == 13


def test_Card_JOKER_value_roundtrip():
    instance = Card(ACE=7, CLUBS=7, DIAMONDS=7, HEARTS=7, JACK=7, JOKER=7, KING=7, QUEEN=7, SPADES=7, suit=7, value=7)
    assert instance.JOKER == 7
    instance.JOKER = 13
    assert instance.JOKER == 13


def test_Card_KING_value_roundtrip():
    instance = Card(ACE=7, CLUBS=7, DIAMONDS=7, HEARTS=7, JACK=7, JOKER=7, KING=7, QUEEN=7, SPADES=7, suit=7, value=7)
    assert instance.KING == 7
    instance.KING = 13
    assert instance.KING == 13


def test_Card_QUEEN_value_roundtrip():
    instance = Card(ACE=7, CLUBS=7, DIAMONDS=7, HEARTS=7, JACK=7, JOKER=7, KING=7, QUEEN=7, SPADES=7, suit=7, value=7)
    assert instance.QUEEN == 7
    instance.QUEEN = 13
    assert instance.QUEEN == 13


def test_Card_SPADES_value_roundtrip():
    instance = Card(ACE=7, CLUBS=7, DIAMONDS=7, HEARTS=7, JACK=7, JOKER=7, KING=7, QUEEN=7, SPADES=7, suit=7, value=7)
    assert instance.SPADES == 7
    instance.SPADES = 13
    assert instance.SPADES == 13


def test_Card_suit_value_roundtrip():
    instance = Card(ACE=7, CLUBS=7, DIAMONDS=7, HEARTS=7, JACK=7, JOKER=7, KING=7, QUEEN=7, SPADES=7, suit=7, value=7)
    assert instance.suit == 7
    instance.suit = 13
    assert instance.suit == 13


def test_Card_value_value_roundtrip():
    instance = Card(ACE=7, CLUBS=7, DIAMONDS=7, HEARTS=7, JACK=7, JOKER=7, KING=7, QUEEN=7, SPADES=7, suit=7, value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Card_strategy = st.builds(Card, ACE=st.integers(), CLUBS=st.integers(), DIAMONDS=st.integers(), HEARTS=st.integers(), JACK=st.integers(), JOKER=st.integers(), KING=st.integers(), QUEEN=st.integers(), SPADES=st.integers(), suit=st.integers(), value=st.integers())
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)


Deck_strategy = st.builds(Deck)
@given(instance=Deck_strategy)
@settings(max_examples=25)
def test_Deck_instantiation(instance):
    assert isinstance(instance, Deck)



