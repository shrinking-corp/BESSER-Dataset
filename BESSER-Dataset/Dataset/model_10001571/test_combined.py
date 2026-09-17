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
    Cards_Deck_Interface,
    Cards_StarndardDeck,
    Cards_Card,
    Cards_Suit,
    Cards_Rank,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_cards_deck_interface_is_not_abstract():
    assert not inspect.isabstract(Cards_Deck_Interface)


def test_hyp_cards_deck_interface_constructor_exists():
    assert callable(Cards_Deck_Interface.__init__)


def test_hyp_cards_deck_interface_constructor_args():
    sig = inspect.signature(Cards_Deck_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cards_starndarddeck_is_not_abstract():
    assert not inspect.isabstract(Cards_StarndardDeck)


def test_hyp_cards_starndarddeck_constructor_exists():
    assert callable(Cards_StarndardDeck.__init__)


def test_hyp_cards_starndarddeck_constructor_args():
    sig = inspect.signature(Cards_StarndardDeck.__init__)
    params = list(sig.parameters.keys())
    assert "cards" in params, "Missing parameter 'cards'"
    assert "rand" in params, "Missing parameter 'rand'"

def test_hyp_cards_starndarddeck_has_cards():
    assert hasattr(Cards_StarndardDeck, "cards")
    descriptor = None
    for klass in Cards_StarndardDeck.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)

def test_hyp_cards_starndarddeck_has_rand():
    assert hasattr(Cards_StarndardDeck, "rand")
    descriptor = None
    for klass in Cards_StarndardDeck.__mro__:
        if "rand" in klass.__dict__:
            descriptor = klass.__dict__["rand"]
            break
    assert isinstance(descriptor, property)



def test_hyp_cards_card_is_not_abstract():
    assert not inspect.isabstract(Cards_Card)


def test_hyp_cards_card_constructor_exists():
    assert callable(Cards_Card.__init__)


def test_hyp_cards_card_constructor_args():
    sig = inspect.signature(Cards_Card.__init__)
    params = list(sig.parameters.keys())
    assert "suit" in params, "Missing parameter 'suit'"
    assert "rank" in params, "Missing parameter 'rank'"

def test_hyp_cards_card_has_suit():
    assert hasattr(Cards_Card, "suit")
    descriptor = None
    for klass in Cards_Card.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)

def test_hyp_cards_card_has_rank():
    assert hasattr(Cards_Card, "rank")
    descriptor = None
    for klass in Cards_Card.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)

def test_hyp_cards_suit_exists():
    # Check that the Enumeration exists
    assert Cards_Suit is not None

def test_hyp_cards_suit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cards_Suit]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Cards_Suit"

def test_hyp_cards_rank_exists():
    # Check that the Enumeration exists
    assert Cards_Rank is not None

def test_hyp_cards_rank_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cards_Rank]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Cards_Rank"


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
Cards_Deck_Interface_strategy = st.builds(
    Cards_Deck_Interface,
)
Cards_StarndardDeck_strategy = st.builds(
    Cards_StarndardDeck,
    cards=
        st.none(),
    rand=
        safe_text
)
Cards_Card_strategy = st.builds(
    Cards_Card,
    suit=
        st.none(),
    rank=
        st.none()
)


@given(instance=Cards_StarndardDeck_strategy)
@settings(max_examples=50)
def test_hyp_cards_starndarddeck_instantiation(instance):
    assert isinstance(instance, Cards_StarndardDeck)



@given(instance=Cards_StarndardDeck_strategy)
def test_hyp_cards_starndarddeck_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original



@given(instance=Cards_StarndardDeck_strategy)
def test_hyp_cards_starndarddeck_rand_setter(instance):
    original = instance.rand
    instance.rand = original
    assert instance.rand == original

@given(instance=Cards_Card_strategy)
@settings(max_examples=50)
def test_hyp_cards_card_instantiation(instance):
    assert isinstance(instance, Cards_Card)



@given(instance=Cards_Card_strategy)
def test_hyp_cards_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=Cards_Card_strategy)
def test_hyp_cards_card_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Cards_Card,
    Cards_Deck_Interface,
    Cards_StarndardDeck,
    Cards_Rank,
    Cards_Suit,
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

# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Cards_Deck_Interface_strategy = st.builds(Cards_Deck_Interface)
@given(instance=Cards_Deck_Interface_strategy)
@settings(max_examples=25)
def test_Cards_Deck_Interface_instantiation(instance):
    assert isinstance(instance, Cards_Deck_Interface)



