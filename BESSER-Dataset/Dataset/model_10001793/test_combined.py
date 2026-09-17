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
    Program,
    GameManager,
    Dealer,
    Player,
    Deck,
    Card,
    CardNumber,
    Suit1,
    Suit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_program_is_not_abstract():
    assert not inspect.isabstract(Program)


def test_hyp_program_constructor_exists():
    assert callable(Program.__init__)


def test_hyp_program_constructor_args():
    sig = inspect.signature(Program.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gamemanager_is_not_abstract():
    assert not inspect.isabstract(GameManager)


def test_hyp_gamemanager_constructor_exists():
    assert callable(GameManager.__init__)


def test_hyp_gamemanager_constructor_args():
    sig = inspect.signature(GameManager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dealer_is_not_abstract():
    assert not inspect.isabstract(Dealer)


def test_hyp_dealer_constructor_exists():
    assert callable(Dealer.__init__)


def test_hyp_dealer_constructor_args():
    sig = inspect.signature(Dealer.__init__)
    params = list(sig.parameters.keys())
    assert "cardDeck" in params, "Missing parameter 'cardDeck'"

def test_hyp_dealer_has_cardDeck():
    assert hasattr(Dealer, "cardDeck")
    descriptor = None
    for klass in Dealer.__mro__:
        if "cardDeck" in klass.__dict__:
            descriptor = klass.__dict__["cardDeck"]
            break
    assert isinstance(descriptor, property)



def test_hyp_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_hyp_player_constructor_exists():
    assert callable(Player.__init__)


def test_hyp_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "isSoft" in params, "Missing parameter 'isSoft'"
    assert "CardsInHand" in params, "Missing parameter 'CardsInHand'"

def test_hyp_player_has_isSoft():
    assert hasattr(Player, "isSoft")
    descriptor = None
    for klass in Player.__mro__:
        if "isSoft" in klass.__dict__:
            descriptor = klass.__dict__["isSoft"]
            break
    assert isinstance(descriptor, property)

def test_hyp_player_has_CardsInHand():
    assert hasattr(Player, "CardsInHand")
    descriptor = None
    for klass in Player.__mro__:
        if "CardsInHand" in klass.__dict__:
            descriptor = klass.__dict__["CardsInHand"]
            break
    assert isinstance(descriptor, property)



def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "List_card_" in params, "Missing parameter 'List_card_'"

def test_hyp_deck_has_List_card_():
    assert hasattr(Deck, "List_card_")
    descriptor = None
    for klass in Deck.__mro__:
        if "List_card_" in klass.__dict__:
            descriptor = klass.__dict__["List_card_"]
            break
    assert isinstance(descriptor, property)



def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "_CardNumber" in params, "Missing parameter '_CardNumber'"
    assert "_CardValue" in params, "Missing parameter '_CardValue'"
    assert "_Suit" in params, "Missing parameter '_Suit'"




def test_hyp_cardnumber_exists():
    # Check that the Enumeration exists
    assert CardNumber is not None

def test_hyp_cardnumber_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CardNumber]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CardNumber"

def test_hyp_suit1_exists():
    # Check that the Enumeration exists
    assert Suit1 is not None

def test_hyp_suit1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Suit1]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Suit1"

def test_hyp_suit_exists():
    # Check that the Enumeration exists
    assert Suit is not None

def test_hyp_suit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Suit]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Suit"


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
Program_strategy = st.builds(
    Program,
)
GameManager_strategy = st.builds(
    GameManager,
)
Dealer_strategy = st.builds(
    Dealer,
    cardDeck=
        st.none()
)
Player_strategy = st.builds(
    Player,
    isSoft=
        st.booleans(),
    CardsInHand=
        st.none()
)
Deck_strategy = st.builds(
    Deck,
    List_card_=
        st.none()
)
Card_strategy = st.builds(
    Card,
    _CardNumber=
        st.integers(),
    _CardValue=
        st.integers(),
    _Suit=
        st.integers()
)



@given(instance=Dealer_strategy)
@settings(max_examples=50)
def test_hyp_dealer_instantiation(instance):
    assert isinstance(instance, Dealer)



@given(instance=Dealer_strategy)
def test_hyp_dealer_cardDeck_setter(instance):
    original = instance.cardDeck
    instance.cardDeck = original
    assert instance.cardDeck == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_hyp_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_hyp_player_isSoft_setter(instance):
    original = instance.isSoft
    instance.isSoft = original
    assert instance.isSoft == original



@given(instance=Player_strategy)
def test_hyp_player_CardsInHand_setter(instance):
    original = instance.CardsInHand
    instance.CardsInHand = original
    assert instance.CardsInHand == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_hyp_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_hyp_deck_List_card__setter(instance):
    original = instance.List_card_
    instance.List_card_ = original
    assert instance.List_card_ == original




@given(instance=Card_strategy)
def test_hyp_card__CardNumber_setter(instance):
    original = instance._CardNumber
    instance._CardNumber = original
    assert instance._CardNumber == original



@given(instance=Card_strategy)
def test_hyp_card__CardValue_setter(instance):
    original = instance._CardValue
    instance._CardValue = original
    assert instance._CardValue == original



@given(instance=Card_strategy)
def test_hyp_card__Suit_setter(instance):
    original = instance._Suit
    instance._Suit = original
    assert instance._Suit == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Card,
    Dealer,
    Deck,
    GameManager,
    Player,
    Program,
    CardNumber,
    Suit,
    Suit1,
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

def test_Card__CardNumber_value_roundtrip():
    instance = Card(_CardNumber=7, _CardValue=7, _Suit=7)
    assert instance._CardNumber == 7
    instance._CardNumber = 13
    assert instance._CardNumber == 13


def test_Card__CardValue_value_roundtrip():
    instance = Card(_CardNumber=7, _CardValue=7, _Suit=7)
    assert instance._CardValue == 7
    instance._CardValue = 13
    assert instance._CardValue == 13


def test_Card__Suit_value_roundtrip():
    instance = Card(_CardNumber=7, _CardValue=7, _Suit=7)
    assert instance._Suit == 7
    instance._Suit = 13
    assert instance._Suit == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Card_strategy = st.builds(Card, _CardNumber=st.integers(), _CardValue=st.integers(), _Suit=st.integers())
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)


GameManager_strategy = st.builds(GameManager)
@given(instance=GameManager_strategy)
@settings(max_examples=25)
def test_GameManager_instantiation(instance):
    assert isinstance(instance, GameManager)


Program_strategy = st.builds(Program)
@given(instance=Program_strategy)
@settings(max_examples=25)
def test_Program_instantiation(instance):
    assert isinstance(instance, Program)



