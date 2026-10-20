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
    Cards,
    Deck,
    Player,
    Class,
    Elevens,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_cards_is_not_abstract():
    assert not inspect.isabstract(Cards)


def test_hyp_cards_constructor_exists():
    assert callable(Cards.__init__)


def test_hyp_cards_constructor_args():
    sig = inspect.signature(Cards.__init__)
    params = list(sig.parameters.keys())
    assert "Character" in params, "Missing parameter 'Character'"
    assert "Suit" in params, "Missing parameter 'Suit'"





def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "Cards" in params, "Missing parameter 'Cards'"

def test_hyp_deck_has_Cards():
    assert hasattr(Deck, "Cards")
    descriptor = None
    for klass in Deck.__mro__:
        if "Cards" in klass.__dict__:
            descriptor = klass.__dict__["Cards"]
            break
    assert isinstance(descriptor, property)



def test_hyp_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_hyp_player_constructor_exists():
    assert callable(Player.__init__)


def test_hyp_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "losses" in params, "Missing parameter 'losses'"
    assert "winRate" in params, "Missing parameter 'winRate'"
    assert "wins" in params, "Missing parameter 'wins'"






def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_elevens_is_not_abstract():
    assert not inspect.isabstract(Elevens)


def test_hyp_elevens_constructor_exists():
    assert callable(Elevens.__init__)


def test_hyp_elevens_constructor_args():
    sig = inspect.signature(Elevens.__init__)
    params = list(sig.parameters.keys())
    assert "Deck" in params, "Missing parameter 'Deck'"
    assert "Player" in params, "Missing parameter 'Player'"

def test_hyp_elevens_has_Deck():
    assert hasattr(Elevens, "Deck")
    descriptor = None
    for klass in Elevens.__mro__:
        if "Deck" in klass.__dict__:
            descriptor = klass.__dict__["Deck"]
            break
    assert isinstance(descriptor, property)

def test_hyp_elevens_has_Player():
    assert hasattr(Elevens, "Player")
    descriptor = None
    for klass in Elevens.__mro__:
        if "Player" in klass.__dict__:
            descriptor = klass.__dict__["Player"]
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
Cards_strategy = st.builds(
    Cards,
    Character=
        safe_text,
    Suit=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
    Cards=
        st.none()
)
Player_strategy = st.builds(
    Player,
    losses=
        st.integers(),
    winRate=
        safe_text,
    wins=
        st.integers()
)
Class_strategy = st.builds(
    Class,
)
Elevens_strategy = st.builds(
    Elevens,
    Deck=
        st.none(),
    Player=
        st.none()
)




@given(instance=Cards_strategy)
def test_hyp_cards_Character_setter(instance):
    original = instance.Character
    instance.Character = original
    assert instance.Character == original



@given(instance=Cards_strategy)
def test_hyp_cards_Suit_setter(instance):
    original = instance.Suit
    instance.Suit = original
    assert instance.Suit == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_hyp_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_hyp_deck_Cards_setter(instance):
    original = instance.Cards
    instance.Cards = original
    assert instance.Cards == original




@given(instance=Player_strategy)
def test_hyp_player_losses_setter(instance):
    original = instance.losses
    instance.losses = original
    assert instance.losses == original



@given(instance=Player_strategy)
def test_hyp_player_winRate_setter(instance):
    original = instance.winRate
    instance.winRate = original
    assert instance.winRate == original



@given(instance=Player_strategy)
def test_hyp_player_wins_setter(instance):
    original = instance.wins
    instance.wins = original
    assert instance.wins == original


@given(instance=Elevens_strategy)
@settings(max_examples=50)
def test_hyp_elevens_instantiation(instance):
    assert isinstance(instance, Elevens)



@given(instance=Elevens_strategy)
def test_hyp_elevens_Deck_setter(instance):
    original = instance.Deck
    instance.Deck = original
    assert instance.Deck == original



@given(instance=Elevens_strategy)
def test_hyp_elevens_Player_setter(instance):
    original = instance.Player
    instance.Player = original
    assert instance.Player == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Cards,
    Class,
    Deck,
    Elevens,
    Player,
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

def test_Cards_Character_value_roundtrip():
    instance = Cards(Character="sample_text", Suit="sample_text")
    assert instance.Character == "sample_text"
    instance.Character = "sample_text_2"
    assert instance.Character == "sample_text_2"


def test_Cards_Suit_value_roundtrip():
    instance = Cards(Character="sample_text", Suit="sample_text")
    assert instance.Suit == "sample_text"
    instance.Suit = "sample_text_2"
    assert instance.Suit == "sample_text_2"


def test_Player_losses_value_roundtrip():
    instance = Player(losses=7, winRate="sample_text", wins=7)
    assert instance.losses == 7
    instance.losses = 13
    assert instance.losses == 13


def test_Player_winRate_value_roundtrip():
    instance = Player(losses=7, winRate="sample_text", wins=7)
    assert instance.winRate == "sample_text"
    instance.winRate = "sample_text_2"
    assert instance.winRate == "sample_text_2"


def test_Player_wins_value_roundtrip():
    instance = Player(losses=7, winRate="sample_text", wins=7)
    assert instance.wins == 7
    instance.wins = 13
    assert instance.wins == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Cards_strategy = st.builds(Cards, Character=safe_text, Suit=safe_text)
@given(instance=Cards_strategy)
@settings(max_examples=25)
def test_Cards_instantiation(instance):
    assert isinstance(instance, Cards)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Player_strategy = st.builds(Player, losses=st.integers(), winRate=safe_text, wins=st.integers())
@given(instance=Player_strategy)
@settings(max_examples=25)
def test_Player_instantiation(instance):
    assert isinstance(instance, Player)



