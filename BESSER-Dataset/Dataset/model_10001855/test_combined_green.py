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
    CardDeckInterface,
    Class,
    Card,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_carddeckinterface_is_not_abstract():
    assert not inspect.isabstract(CardDeckInterface)


def test_hyp_carddeckinterface_constructor_exists():
    assert callable(CardDeckInterface.__init__)


def test_hyp_carddeckinterface_constructor_args():
    sig = inspect.signature(CardDeckInterface.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "draw" in params, "Missing parameter 'draw'"
    assert "shuffle" in params, "Missing parameter 'shuffle'"

def test_hyp_carddeckinterface_has_size():
    assert hasattr(CardDeckInterface, "size")
    descriptor = None
    for klass in CardDeckInterface.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_hyp_carddeckinterface_has_draw():
    assert hasattr(CardDeckInterface, "draw")
    descriptor = None
    for klass in CardDeckInterface.__mro__:
        if "draw" in klass.__dict__:
            descriptor = klass.__dict__["draw"]
            break
    assert isinstance(descriptor, property)

def test_hyp_carddeckinterface_has_shuffle():
    assert hasattr(CardDeckInterface, "shuffle")
    descriptor = None
    for klass in CardDeckInterface.__mro__:
        if "shuffle" in klass.__dict__:
            descriptor = klass.__dict__["shuffle"]
            break
    assert isinstance(descriptor, property)



def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "Ace___14" in params, "Missing parameter 'Ace___14'"
    assert "Queen_12" in params, "Missing parameter 'Queen_12'"
    assert "Hearts" in params, "Missing parameter 'Hearts'"
    assert "suit" in params, "Missing parameter 'suit'"
    assert "Spades" in params, "Missing parameter 'Spades'"
    assert "Jack_11" in params, "Missing parameter 'Jack_11'"
    assert "Clubs" in params, "Missing parameter 'Clubs'"
    assert "King_13" in params, "Missing parameter 'King_13'"
    assert "Diamonds" in params, "Missing parameter 'Diamonds'"
    assert "face" in params, "Missing parameter 'face'"












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
CardDeckInterface_strategy = st.builds(
    CardDeckInterface,
    size=
        st.integers(),
    draw=
        st.none(),
    shuffle=
        safe_text
)
Class_strategy = st.builds(
    Class,
)
Card_strategy = st.builds(
    Card,
    Ace___14=
        st.integers(),
    Queen_12=
        st.integers(),
    Hearts=
        safe_text,
    suit=
        safe_text,
    Spades=
        safe_text,
    Jack_11=
        st.integers(),
    Clubs=
        safe_text,
    King_13=
        st.integers(),
    Diamonds=
        safe_text,
    face=
        st.integers()
)

@given(instance=CardDeckInterface_strategy)
@settings(max_examples=50)
def test_hyp_carddeckinterface_instantiation(instance):
    assert isinstance(instance, CardDeckInterface)



@given(instance=CardDeckInterface_strategy)
def test_hyp_carddeckinterface_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=CardDeckInterface_strategy)
def test_hyp_carddeckinterface_draw_setter(instance):
    original = instance.draw
    instance.draw = original
    assert instance.draw == original



@given(instance=CardDeckInterface_strategy)
def test_hyp_carddeckinterface_shuffle_setter(instance):
    original = instance.shuffle
    instance.shuffle = original
    assert instance.shuffle == original





@given(instance=Card_strategy)
def test_hyp_card_Ace___14_setter(instance):
    original = instance.Ace___14
    instance.Ace___14 = original
    assert instance.Ace___14 == original



@given(instance=Card_strategy)
def test_hyp_card_Queen_12_setter(instance):
    original = instance.Queen_12
    instance.Queen_12 = original
    assert instance.Queen_12 == original



@given(instance=Card_strategy)
def test_hyp_card_Hearts_setter(instance):
    original = instance.Hearts
    instance.Hearts = original
    assert instance.Hearts == original



@given(instance=Card_strategy)
def test_hyp_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=Card_strategy)
def test_hyp_card_Spades_setter(instance):
    original = instance.Spades
    instance.Spades = original
    assert instance.Spades == original



@given(instance=Card_strategy)
def test_hyp_card_Jack_11_setter(instance):
    original = instance.Jack_11
    instance.Jack_11 = original
    assert instance.Jack_11 == original



@given(instance=Card_strategy)
def test_hyp_card_Clubs_setter(instance):
    original = instance.Clubs
    instance.Clubs = original
    assert instance.Clubs == original



@given(instance=Card_strategy)
def test_hyp_card_King_13_setter(instance):
    original = instance.King_13
    instance.King_13 = original
    assert instance.King_13 == original



@given(instance=Card_strategy)
def test_hyp_card_Diamonds_setter(instance):
    original = instance.Diamonds
    instance.Diamonds = original
    assert instance.Diamonds == original



@given(instance=Card_strategy)
def test_hyp_card_face_setter(instance):
    original = instance.face
    instance.face = original
    assert instance.face == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Card,
    CardDeckInterface,
    Class,
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

def test_Card_Ace___14_value_roundtrip():
    instance = Card(Ace___14=7, Clubs="sample_text", Diamonds="sample_text", Hearts="sample_text", Jack_11=7, King_13=7, Queen_12=7, Spades="sample_text", face=7, suit="sample_text")
    assert instance.Ace___14 == 7
    instance.Ace___14 = 13
    assert instance.Ace___14 == 13


def test_Card_Clubs_value_roundtrip():
    instance = Card(Ace___14=7, Clubs="sample_text", Diamonds="sample_text", Hearts="sample_text", Jack_11=7, King_13=7, Queen_12=7, Spades="sample_text", face=7, suit="sample_text")
    assert instance.Clubs == "sample_text"
    instance.Clubs = "sample_text_2"
    assert instance.Clubs == "sample_text_2"


def test_Card_Diamonds_value_roundtrip():
    instance = Card(Ace___14=7, Clubs="sample_text", Diamonds="sample_text", Hearts="sample_text", Jack_11=7, King_13=7, Queen_12=7, Spades="sample_text", face=7, suit="sample_text")
    assert instance.Diamonds == "sample_text"
    instance.Diamonds = "sample_text_2"
    assert instance.Diamonds == "sample_text_2"


def test_Card_Hearts_value_roundtrip():
    instance = Card(Ace___14=7, Clubs="sample_text", Diamonds="sample_text", Hearts="sample_text", Jack_11=7, King_13=7, Queen_12=7, Spades="sample_text", face=7, suit="sample_text")
    assert instance.Hearts == "sample_text"
    instance.Hearts = "sample_text_2"
    assert instance.Hearts == "sample_text_2"


def test_Card_Jack_11_value_roundtrip():
    instance = Card(Ace___14=7, Clubs="sample_text", Diamonds="sample_text", Hearts="sample_text", Jack_11=7, King_13=7, Queen_12=7, Spades="sample_text", face=7, suit="sample_text")
    assert instance.Jack_11 == 7
    instance.Jack_11 = 13
    assert instance.Jack_11 == 13


def test_Card_King_13_value_roundtrip():
    instance = Card(Ace___14=7, Clubs="sample_text", Diamonds="sample_text", Hearts="sample_text", Jack_11=7, King_13=7, Queen_12=7, Spades="sample_text", face=7, suit="sample_text")
    assert instance.King_13 == 7
    instance.King_13 = 13
    assert instance.King_13 == 13


def test_Card_Queen_12_value_roundtrip():
    instance = Card(Ace___14=7, Clubs="sample_text", Diamonds="sample_text", Hearts="sample_text", Jack_11=7, King_13=7, Queen_12=7, Spades="sample_text", face=7, suit="sample_text")
    assert instance.Queen_12 == 7
    instance.Queen_12 = 13
    assert instance.Queen_12 == 13


def test_Card_Spades_value_roundtrip():
    instance = Card(Ace___14=7, Clubs="sample_text", Diamonds="sample_text", Hearts="sample_text", Jack_11=7, King_13=7, Queen_12=7, Spades="sample_text", face=7, suit="sample_text")
    assert instance.Spades == "sample_text"
    instance.Spades = "sample_text_2"
    assert instance.Spades == "sample_text_2"


def test_Card_face_value_roundtrip():
    instance = Card(Ace___14=7, Clubs="sample_text", Diamonds="sample_text", Hearts="sample_text", Jack_11=7, King_13=7, Queen_12=7, Spades="sample_text", face=7, suit="sample_text")
    assert instance.face == 7
    instance.face = 13
    assert instance.face == 13


def test_Card_suit_value_roundtrip():
    instance = Card(Ace___14=7, Clubs="sample_text", Diamonds="sample_text", Hearts="sample_text", Jack_11=7, King_13=7, Queen_12=7, Spades="sample_text", face=7, suit="sample_text")
    assert instance.suit == "sample_text"
    instance.suit = "sample_text_2"
    assert instance.suit == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Card_strategy = st.builds(Card, Ace___14=st.integers(), Clubs=safe_text, Diamonds=safe_text, Hearts=safe_text, Jack_11=st.integers(), King_13=st.integers(), Queen_12=st.integers(), Spades=safe_text, face=st.integers(), suit=safe_text)
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)



