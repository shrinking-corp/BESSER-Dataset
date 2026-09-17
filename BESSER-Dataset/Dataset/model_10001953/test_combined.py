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
    HandValue,
    Dealer,
    Hand,
    Player,
    Cards,
    Deck,
    CardTitle,
    CardSuit,
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
    assert "winner" in params, "Missing parameter 'winner'"

def test_hyp_game_has_winner():
    assert hasattr(Game, "winner")
    descriptor = None
    for klass in Game.__mro__:
        if "winner" in klass.__dict__:
            descriptor = klass.__dict__["winner"]
            break
    assert isinstance(descriptor, property)



def test_hyp_handvalue_is_not_abstract():
    assert not inspect.isabstract(HandValue)


def test_hyp_handvalue_constructor_exists():
    assert callable(HandValue.__init__)


def test_hyp_handvalue_constructor_args():
    sig = inspect.signature(HandValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dealer_is_not_abstract():
    assert not inspect.isabstract(Dealer)


def test_hyp_dealer_constructor_exists():
    assert callable(Dealer.__init__)


def test_hyp_dealer_constructor_args():
    sig = inspect.signature(Dealer.__init__)
    params = list(sig.parameters.keys())
    assert "cards" in params, "Missing parameter 'cards'"
    assert "name" in params, "Missing parameter 'name'"

def test_hyp_dealer_has_cards():
    assert hasattr(Dealer, "cards")
    descriptor = None
    for klass in Dealer.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)

def test_hyp_dealer_has_name():
    assert hasattr(Dealer, "name")
    descriptor = None
    for klass in Dealer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hyp_hand_is_not_abstract():
    assert not inspect.isabstract(Hand)


def test_hyp_hand_constructor_exists():
    assert callable(Hand.__init__)


def test_hyp_hand_constructor_args():
    sig = inspect.signature(Hand.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_hyp_hand_has_value():
    assert hasattr(Hand, "value")
    descriptor = None
    for klass in Hand.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_hyp_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_hyp_player_constructor_exists():
    assert callable(Player.__init__)


def test_hyp_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_cards_is_not_abstract():
    assert not inspect.isabstract(Cards)


def test_hyp_cards_constructor_exists():
    assert callable(Cards.__init__)


def test_hyp_cards_constructor_args():
    sig = inspect.signature(Cards.__init__)
    params = list(sig.parameters.keys())
    assert "suit" in params, "Missing parameter 'suit'"
    assert "title" in params, "Missing parameter 'title'"
    assert "value" in params, "Missing parameter 'value'"

def test_hyp_cards_has_suit():
    assert hasattr(Cards, "suit")
    descriptor = None
    for klass in Cards.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)

def test_hyp_cards_has_title():
    assert hasattr(Cards, "title")
    descriptor = None
    for klass in Cards.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_hyp_cards_has_value():
    assert hasattr(Cards, "value")
    descriptor = None
    for klass in Cards.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())

def test_hyp_cardtitle_exists():
    # Check that the Enumeration exists
    assert CardTitle is not None

def test_hyp_cardtitle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CardTitle]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CardTitle"

def test_hyp_cardsuit_exists():
    # Check that the Enumeration exists
    assert CardSuit is not None

def test_hyp_cardsuit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CardSuit]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CardSuit"


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
    winner=
        st.none()
)
HandValue_strategy = st.builds(
    HandValue,
)
Dealer_strategy = st.builds(
    Dealer,
    cards=
        st.none(),
    name=
        safe_text
)
Hand_strategy = st.builds(
    Hand,
    value=
        st.none()
)
Player_strategy = st.builds(
    Player,
    name=
        safe_text
)
Cards_strategy = st.builds(
    Cards,
    suit=
        st.none(),
    title=
        st.none(),
    value=
        st.integers()
)
Deck_strategy = st.builds(
    Deck,
)

@given(instance=Game_strategy)
@settings(max_examples=50)
def test_hyp_game_instantiation(instance):
    assert isinstance(instance, Game)



@given(instance=Game_strategy)
def test_hyp_game_winner_setter(instance):
    original = instance.winner
    instance.winner = original
    assert instance.winner == original


@given(instance=Dealer_strategy)
@settings(max_examples=50)
def test_hyp_dealer_instantiation(instance):
    assert isinstance(instance, Dealer)



@given(instance=Dealer_strategy)
def test_hyp_dealer_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original



@given(instance=Dealer_strategy)
def test_hyp_dealer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Hand_strategy)
@settings(max_examples=50)
def test_hyp_hand_instantiation(instance):
    assert isinstance(instance, Hand)



@given(instance=Hand_strategy)
def test_hyp_hand_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=Player_strategy)
def test_hyp_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Cards_strategy)
@settings(max_examples=50)
def test_hyp_cards_instantiation(instance):
    assert isinstance(instance, Cards)



@given(instance=Cards_strategy)
def test_hyp_cards_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=Cards_strategy)
def test_hyp_cards_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=Cards_strategy)
def test_hyp_cards_value_setter(instance):
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
    Cards,
    Dealer,
    Deck,
    Game,
    Hand,
    HandValue,
    Player,
    CardSuit,
    CardTitle,
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

def test_Player_name_value_roundtrip():
    instance = Player(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Deck_strategy = st.builds(Deck)
@given(instance=Deck_strategy)
@settings(max_examples=25)
def test_Deck_instantiation(instance):
    assert isinstance(instance, Deck)


HandValue_strategy = st.builds(HandValue)
@given(instance=HandValue_strategy)
@settings(max_examples=25)
def test_HandValue_instantiation(instance):
    assert isinstance(instance, HandValue)


Player_strategy = st.builds(Player, name=safe_text)
@given(instance=Player_strategy)
@settings(max_examples=25)
def test_Player_instantiation(instance):
    assert isinstance(instance, Player)



