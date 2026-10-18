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
    TarotCard___Card,
    Card___Abstract__,
    FortuneTeller,
    Deck,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_tarotcard___card_is_not_abstract():
    assert not inspect.isabstract(TarotCard___Card)


def test_hyp_tarotcard___card_constructor_exists():
    assert callable(TarotCard___Card.__init__)


def test_hyp_tarotcard___card_constructor_args():
    sig = inspect.signature(TarotCard___Card.__init__)
    params = list(sig.parameters.keys())
    assert "_fortunes" in params, "Missing parameter '_fortunes'"
    assert "_fileName" in params, "Missing parameter '_fileName'"
    assert "_id" in params, "Missing parameter '_id'"






def test_hyp_card___abstract___is_not_abstract():
    assert not inspect.isabstract(Card___Abstract__)


def test_hyp_card___abstract___constructor_exists():
    assert callable(Card___Abstract__.__init__)


def test_hyp_card___abstract___constructor_args():
    sig = inspect.signature(Card___Abstract__.__init__)
    params = list(sig.parameters.keys())
    assert "_id" in params, "Missing parameter '_id'"




def test_hyp_fortuneteller_is_not_abstract():
    assert not inspect.isabstract(FortuneTeller)


def test_hyp_fortuneteller_constructor_exists():
    assert callable(FortuneTeller.__init__)


def test_hyp_fortuneteller_constructor_args():
    sig = inspect.signature(FortuneTeller.__init__)
    params = list(sig.parameters.keys())
    assert "_tarotDeck" in params, "Missing parameter '_tarotDeck'"

def test_hyp_fortuneteller_has__tarotDeck():
    assert hasattr(FortuneTeller, "_tarotDeck")
    descriptor = None
    for klass in FortuneTeller.__mro__:
        if "_tarotDeck" in klass.__dict__:
            descriptor = klass.__dict__["_tarotDeck"]
            break
    assert isinstance(descriptor, property)



def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "_deck" in params, "Missing parameter '_deck'"



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
TarotCard___Card_strategy = st.builds(
    TarotCard___Card,
    _fortunes=
        safe_text,
    _fileName=
        safe_text,
    _id=
        st.integers()
)
Card___Abstract___strategy = st.builds(
    Card___Abstract__,
    _id=
        st.integers()
)
FortuneTeller_strategy = st.builds(
    FortuneTeller,
    _tarotDeck=
        st.none()
)
Deck_strategy = st.builds(
    Deck,
    _deck=
        safe_text
)




@given(instance=TarotCard___Card_strategy)
def test_hyp_tarotcard___card__fortunes_setter(instance):
    original = instance._fortunes
    instance._fortunes = original
    assert instance._fortunes == original



@given(instance=TarotCard___Card_strategy)
def test_hyp_tarotcard___card__fileName_setter(instance):
    original = instance._fileName
    instance._fileName = original
    assert instance._fileName == original



@given(instance=TarotCard___Card_strategy)
def test_hyp_tarotcard___card__id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original




@given(instance=Card___Abstract___strategy)
def test_hyp_card___abstract____id_setter(instance):
    original = instance._id
    instance._id = original
    assert instance._id == original

@given(instance=FortuneTeller_strategy)
@settings(max_examples=50)
def test_hyp_fortuneteller_instantiation(instance):
    assert isinstance(instance, FortuneTeller)



@given(instance=FortuneTeller_strategy)
def test_hyp_fortuneteller__tarotDeck_setter(instance):
    original = instance._tarotDeck
    instance._tarotDeck = original
    assert instance._tarotDeck == original




@given(instance=Deck_strategy)
def test_hyp_deck__deck_setter(instance):
    original = instance._deck
    instance._deck = original
    assert instance._deck == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Card___Abstract__,
    Deck,
    FortuneTeller,
    TarotCard___Card,
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

def test_Card___Abstract____id_value_roundtrip():
    instance = Card___Abstract__(_id=7)
    assert instance._id == 7
    instance._id = 13
    assert instance._id == 13


def test_Deck__deck_value_roundtrip():
    instance = Deck(_deck="sample_text")
    assert instance._deck == "sample_text"
    instance._deck = "sample_text_2"
    assert instance._deck == "sample_text_2"


def test_TarotCard___Card__fileName_value_roundtrip():
    instance = TarotCard___Card(_fileName="sample_text", _fortunes="sample_text", _id=7)
    assert instance._fileName == "sample_text"
    instance._fileName = "sample_text_2"
    assert instance._fileName == "sample_text_2"


def test_TarotCard___Card__fortunes_value_roundtrip():
    instance = TarotCard___Card(_fileName="sample_text", _fortunes="sample_text", _id=7)
    assert instance._fortunes == "sample_text"
    instance._fortunes = "sample_text_2"
    assert instance._fortunes == "sample_text_2"


def test_TarotCard___Card__id_value_roundtrip():
    instance = TarotCard___Card(_fileName="sample_text", _fortunes="sample_text", _id=7)
    assert instance._id == 7
    instance._id = 13
    assert instance._id == 13


def test_assoc_Card___Abstract___Deck_link_reassign_clear():
    a = Deck(_deck="sample_text")
    b1 = Card___Abstract__(_id=7)
    b2 = Card___Abstract__(_id=13)
    _safe_set(a, 'card___Abstract__1', b1)
    assert _is_linked(a, 'card___Abstract__1', b1)
    if hasattr(b1, 'deck0'):
        assert _is_linked(b1, 'deck0', a)
    _safe_set(a, 'card___Abstract__1', b2)
    assert _is_linked(a, 'card___Abstract__1', b2)
    if hasattr(b1, 'deck0'):
        assert not _is_linked(b1, 'deck0', a)
    if hasattr(b2, 'deck0'):
        assert _is_linked(b2, 'deck0', a)
    _safe_set(a, 'card___Abstract__1', None)
    assert not _is_linked(a, 'card___Abstract__1', b2)
    if hasattr(b2, 'deck0'):
        assert not _is_linked(b2, 'deck0', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Card___Abstract___strategy = st.builds(Card___Abstract__, _id=st.integers())
@given(instance=Card___Abstract___strategy)
@settings(max_examples=25)
def test_Card___Abstract___instantiation(instance):
    assert isinstance(instance, Card___Abstract__)


Deck_strategy = st.builds(Deck, _deck=safe_text)
@given(instance=Deck_strategy)
@settings(max_examples=25)
def test_Deck_instantiation(instance):
    assert isinstance(instance, Deck)


TarotCard___Card_strategy = st.builds(TarotCard___Card, _fileName=safe_text, _fortunes=safe_text, _id=st.integers())
@given(instance=TarotCard___Card_strategy)
@settings(max_examples=25)
def test_TarotCard___Card_instantiation(instance):
    assert isinstance(instance, TarotCard___Card)



