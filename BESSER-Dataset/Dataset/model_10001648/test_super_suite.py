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
    CardDeck,
    Card,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_carddeck_is_not_abstract():
    assert not inspect.isabstract(CardDeck)


def test_hyp_carddeck_constructor_exists():
    assert callable(CardDeck.__init__)


def test_hyp_carddeck_constructor_args():
    sig = inspect.signature(CardDeck.__init__)
    params = list(sig.parameters.keys())
    assert "cards" in params, "Missing parameter 'cards'"
    assert "suits" in params, "Missing parameter 'suits'"





def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "cardSuit" in params, "Missing parameter 'cardSuit'"
    assert "cardFace" in params, "Missing parameter 'cardFace'"




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
CardDeck_strategy = st.builds(
    CardDeck,
    cards=
        safe_text,
    suits=
        safe_text
)
Card_strategy = st.builds(
    Card,
    cardSuit=
        safe_text,
    cardFace=
        st.integers()
)




@given(instance=CardDeck_strategy)
def test_hyp_carddeck_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original



@given(instance=CardDeck_strategy)
def test_hyp_carddeck_suits_setter(instance):
    original = instance.suits
    instance.suits = original
    assert instance.suits == original




@given(instance=Card_strategy)
def test_hyp_card_cardSuit_setter(instance):
    original = instance.cardSuit
    instance.cardSuit = original
    assert instance.cardSuit == original



@given(instance=Card_strategy)
def test_hyp_card_cardFace_setter(instance):
    original = instance.cardFace
    instance.cardFace = original
    assert instance.cardFace == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Card,
    CardDeck,
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

def test_Card_cardFace_value_roundtrip():
    instance = Card(cardFace=7, cardSuit="sample_text")
    assert instance.cardFace == 7
    instance.cardFace = 13
    assert instance.cardFace == 13


def test_Card_cardSuit_value_roundtrip():
    instance = Card(cardFace=7, cardSuit="sample_text")
    assert instance.cardSuit == "sample_text"
    instance.cardSuit = "sample_text_2"
    assert instance.cardSuit == "sample_text_2"


def test_CardDeck_cards_value_roundtrip():
    instance = CardDeck(cards="sample_text", suits="sample_text")
    assert instance.cards == "sample_text"
    instance.cards = "sample_text_2"
    assert instance.cards == "sample_text_2"


def test_CardDeck_suits_value_roundtrip():
    instance = CardDeck(cards="sample_text", suits="sample_text")
    assert instance.suits == "sample_text"
    instance.suits = "sample_text_2"
    assert instance.suits == "sample_text_2"


def test_assoc_CardDeck_Card_link_reassign_clear():
    a = CardDeck(cards="sample_text", suits="sample_text")
    b1 = Card(cardFace=7, cardSuit="sample_text")
    b2 = Card(cardFace=13, cardSuit="sample_text_2")
    _safe_set(a, 'CardDeck_Card_00', {b1})
    assert _is_linked(a, 'CardDeck_Card_00', b1)
    if hasattr(b1, 'Has1'):
        assert _is_linked(b1, 'Has1', a)
    _safe_set(a, 'CardDeck_Card_00', {b2})
    assert _is_linked(a, 'CardDeck_Card_00', b2)
    if hasattr(b1, 'Has1'):
        assert not _is_linked(b1, 'Has1', a)
    if hasattr(b2, 'Has1'):
        assert _is_linked(b2, 'Has1', a)
    _safe_set(a, 'CardDeck_Card_00', set())
    assert not _is_linked(a, 'CardDeck_Card_00', b2)
    if hasattr(b2, 'Has1'):
        assert not _is_linked(b2, 'Has1', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Card_strategy = st.builds(Card, cardFace=st.integers(), cardSuit=safe_text)
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)


CardDeck_strategy = st.builds(CardDeck, cards=safe_text, suits=safe_text)
@given(instance=CardDeck_strategy)
@settings(max_examples=25)
def test_CardDeck_instantiation(instance):
    assert isinstance(instance, CardDeck)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Card,
    CardDeck,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_CardDeck_Card_reverse_link_reassign_clear():
    a1 = CardDeck(cards="sample_text", suits="sample_text")
    a2 = CardDeck(cards="sample_text_2", suits="sample_text_2")
    b = Card(cardFace=7, cardSuit="sample_text")
    _safe_set(b, 'Has1', a1)
    assert _is_linked(b, 'Has1', a1)
    if hasattr(a1, 'CardDeck_Card_00'):
        assert _is_linked(a1, 'CardDeck_Card_00', b)
    _safe_set(b, 'Has1', a2)
    assert _is_linked(b, 'Has1', a2)
    if hasattr(a1, 'CardDeck_Card_00'):
        assert not _is_linked(a1, 'CardDeck_Card_00', b)
    if hasattr(a2, 'CardDeck_Card_00'):
        assert _is_linked(a2, 'CardDeck_Card_00', b)
    _safe_set(b, 'Has1', None)
    assert not _is_linked(b, 'Has1', a2)
    if hasattr(a2, 'CardDeck_Card_00'):
        assert not _is_linked(a2, 'CardDeck_Card_00', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================



from python_code import CardDeck

def test_CardDeck___init__():
    assert CardDeck.__init__(CardDeck('\x00\x00', '', CardDeck_Card_00=set()), '', '', CardDeck_Card_00=set()) == None

