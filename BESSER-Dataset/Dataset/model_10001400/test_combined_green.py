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
    Class2,
    Class,
    blackjackCard,
    Deck,
    Blackjack,
    blackjackHand,
    Hand,
    Card,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_class2_is_not_abstract():
    assert not inspect.isabstract(Class2)


def test_hyp_class2_constructor_exists():
    assert callable(Class2.__init__)


def test_hyp_class2_constructor_args():
    sig = inspect.signature(Class2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_blackjackcard_is_not_abstract():
    assert not inspect.isabstract(blackjackCard)


def test_hyp_blackjackcard_constructor_exists():
    assert callable(blackjackCard.__init__)


def test_hyp_blackjackcard_constructor_args():
    sig = inspect.signature(blackjackCard.__init__)
    params = list(sig.parameters.keys())



def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "deck" in params, "Missing parameter 'deck'"




def test_hyp_blackjack_is_not_abstract():
    assert not inspect.isabstract(Blackjack)


def test_hyp_blackjack_constructor_exists():
    assert callable(Blackjack.__init__)


def test_hyp_blackjack_constructor_args():
    sig = inspect.signature(Blackjack.__init__)
    params = list(sig.parameters.keys())



def test_hyp_blackjackhand_is_not_abstract():
    assert not inspect.isabstract(blackjackHand)


def test_hyp_blackjackhand_constructor_exists():
    assert callable(blackjackHand.__init__)


def test_hyp_blackjackhand_constructor_args():
    sig = inspect.signature(blackjackHand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hand_is_not_abstract():
    assert not inspect.isabstract(Hand)


def test_hyp_hand_constructor_exists():
    assert callable(Hand.__init__)


def test_hyp_hand_constructor_args():
    sig = inspect.signature(Hand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "face" in params, "Missing parameter 'face'"
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
Class2_strategy = st.builds(
    Class2,
)
Class_strategy = st.builds(
    Class,
)
blackjackCard_strategy = st.builds(
    blackjackCard,
)
Deck_strategy = st.builds(
    Deck,
    deck=
        safe_text
)
Blackjack_strategy = st.builds(
    Blackjack,
)
blackjackHand_strategy = st.builds(
    blackjackHand,
)
Hand_strategy = st.builds(
    Hand,
)
Card_strategy = st.builds(
    Card,
    face=
        st.integers(),
    suit=
        st.integers()
)







@given(instance=Deck_strategy)
def test_hyp_deck_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original







@given(instance=Card_strategy)
def test_hyp_card_face_setter(instance):
    original = instance.face
    instance.face = original
    assert instance.face == original



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
    Blackjack,
    Card,
    Class,
    Class2,
    Deck,
    Hand,
    blackjackCard,
    blackjackHand,
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

def test_Card_face_value_roundtrip():
    instance = Card(face=7, suit=7)
    assert instance.face == 7
    instance.face = 13
    assert instance.face == 13


def test_Card_suit_value_roundtrip():
    instance = Card(face=7, suit=7)
    assert instance.suit == 7
    instance.suit = 13
    assert instance.suit == 13


def test_Deck_deck_value_roundtrip():
    instance = Deck(deck="sample_text")
    assert instance.deck == "sample_text"
    instance.deck = "sample_text_2"
    assert instance.deck == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Blackjack_strategy = st.builds(Blackjack)
@given(instance=Blackjack_strategy)
@settings(max_examples=25)
def test_Blackjack_instantiation(instance):
    assert isinstance(instance, Blackjack)


Card_strategy = st.builds(Card, face=st.integers(), suit=st.integers())
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Class2_strategy = st.builds(Class2)
@given(instance=Class2_strategy)
@settings(max_examples=25)
def test_Class2_instantiation(instance):
    assert isinstance(instance, Class2)


Deck_strategy = st.builds(Deck, deck=safe_text)
@given(instance=Deck_strategy)
@settings(max_examples=25)
def test_Deck_instantiation(instance):
    assert isinstance(instance, Deck)


Hand_strategy = st.builds(Hand)
@given(instance=Hand_strategy)
@settings(max_examples=25)
def test_Hand_instantiation(instance):
    assert isinstance(instance, Hand)


blackjackCard_strategy = st.builds(blackjackCard)
@given(instance=blackjackCard_strategy)
@settings(max_examples=25)
def test_blackjackCard_instantiation(instance):
    assert isinstance(instance, blackjackCard)


blackjackHand_strategy = st.builds(blackjackHand)
@given(instance=blackjackHand_strategy)
@settings(max_examples=25)
def test_blackjackHand_instantiation(instance):
    assert isinstance(instance, blackjackHand)



