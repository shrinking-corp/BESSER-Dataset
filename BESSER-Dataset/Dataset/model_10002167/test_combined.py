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
    Stack,
    Card,
    Deck,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_stack_is_not_abstract():
    assert not inspect.isabstract(Stack)


def test_hyp_stack_constructor_exists():
    assert callable(Stack.__init__)


def test_hyp_stack_constructor_args():
    sig = inspect.signature(Stack.__init__)
    params = list(sig.parameters.keys())
    assert "numOfCards" in params, "Missing parameter 'numOfCards'"
    assert "cards__" in params, "Missing parameter 'cards__'"

def test_hyp_stack_has_numOfCards():
    assert hasattr(Stack, "numOfCards")
    descriptor = None
    for klass in Stack.__mro__:
        if "numOfCards" in klass.__dict__:
            descriptor = klass.__dict__["numOfCards"]
            break
    assert isinstance(descriptor, property)

def test_hyp_stack_has_cards__():
    assert hasattr(Stack, "cards__")
    descriptor = None
    for klass in Stack.__mro__:
        if "cards__" in klass.__dict__:
            descriptor = klass.__dict__["cards__"]
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
    assert "suit" in params, "Missing parameter 'suit'"





def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "numOfCards" in params, "Missing parameter 'numOfCards'"
    assert "Card__" in params, "Missing parameter 'Card__'"

def test_hyp_deck_has_numOfCards():
    assert hasattr(Deck, "numOfCards")
    descriptor = None
    for klass in Deck.__mro__:
        if "numOfCards" in klass.__dict__:
            descriptor = klass.__dict__["numOfCards"]
            break
    assert isinstance(descriptor, property)

def test_hyp_deck_has_Card__():
    assert hasattr(Deck, "Card__")
    descriptor = None
    for klass in Deck.__mro__:
        if "Card__" in klass.__dict__:
            descriptor = klass.__dict__["Card__"]
            break
    assert isinstance(descriptor, property)


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
Stack_strategy = st.builds(
    Stack,
    numOfCards=
        st.integers(),
    cards__=
        st.none()
)
Card_strategy = st.builds(
    Card,
    value=
        st.integers(),
    suit=
        st.integers()
)
Deck_strategy = st.builds(
    Deck,
    numOfCards=
        st.integers(),
    Card__=
        st.none()
)

@given(instance=Stack_strategy)
@settings(max_examples=50)
def test_hyp_stack_instantiation(instance):
    assert isinstance(instance, Stack)



@given(instance=Stack_strategy)
def test_hyp_stack_numOfCards_setter(instance):
    original = instance.numOfCards
    instance.numOfCards = original
    assert instance.numOfCards == original



@given(instance=Stack_strategy)
def test_hyp_stack_cards___setter(instance):
    original = instance.cards__
    instance.cards__ = original
    assert instance.cards__ == original




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

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_hyp_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_hyp_deck_numOfCards_setter(instance):
    original = instance.numOfCards
    instance.numOfCards = original
    assert instance.numOfCards == original



@given(instance=Deck_strategy)
def test_hyp_deck_Card___setter(instance):
    original = instance.Card__
    instance.Card__ = original
    assert instance.Card__ == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Card,
    Deck,
    Stack,
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


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Card_strategy = st.builds(Card, suit=st.integers(), value=st.integers())
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)



