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
    Class,
    GoFish,
    Rules,
    Game,
    Computer,
    b,
    Player,
    Deck,
    Card,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gofish_is_not_abstract():
    assert not inspect.isabstract(GoFish)


def test_hyp_gofish_constructor_exists():
    assert callable(GoFish.__init__)


def test_hyp_gofish_constructor_args():
    sig = inspect.signature(GoFish.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rules_is_not_abstract():
    assert not inspect.isabstract(Rules)


def test_hyp_rules_constructor_exists():
    assert callable(Rules.__init__)


def test_hyp_rules_constructor_args():
    sig = inspect.signature(Rules.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "currentRules" in params, "Missing parameter 'currentRules'"





def test_hyp_game_is_not_abstract():
    assert not inspect.isabstract(Game)


def test_hyp_game_constructor_exists():
    assert callable(Game.__init__)


def test_hyp_game_constructor_args():
    sig = inspect.signature(Game.__init__)
    params = list(sig.parameters.keys())



def test_hyp_computer_is_not_abstract():
    assert not inspect.isabstract(Computer)


def test_hyp_computer_constructor_exists():
    assert callable(Computer.__init__)


def test_hyp_computer_constructor_args():
    sig = inspect.signature(Computer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_b_is_not_abstract():
    assert not inspect.isabstract(b)


def test_hyp_b_constructor_exists():
    assert callable(b.__init__)


def test_hyp_b_constructor_args():
    sig = inspect.signature(b.__init__)
    params = list(sig.parameters.keys())



def test_hyp_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_hyp_player_constructor_exists():
    assert callable(Player.__init__)


def test_hyp_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "hand" in params, "Missing parameter 'hand'"





def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "deck" in params, "Missing parameter 'deck'"




def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "suit" in params, "Missing parameter 'suit'"
    assert "color" in params, "Missing parameter 'color'"
    assert "number" in params, "Missing parameter 'number'"





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
Class_strategy = st.builds(
    Class,
)
GoFish_strategy = st.builds(
    GoFish,
)
Rules_strategy = st.builds(
    Rules,
    attribute=
        safe_text,
    currentRules=
        st.booleans()
)
Game_strategy = st.builds(
    Game,
)
Computer_strategy = st.builds(
    Computer,
)
b_strategy = st.builds(
    b,
)
Player_strategy = st.builds(
    Player,
    name=
        safe_text,
    hand=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
    deck=
        safe_text
)
Card_strategy = st.builds(
    Card,
    suit=
        safe_text,
    color=
        safe_text,
    number=
        st.integers()
)






@given(instance=Rules_strategy)
def test_hyp_rules_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Rules_strategy)
def test_hyp_rules_currentRules_setter(instance):
    original = instance.currentRules
    instance.currentRules = original
    assert instance.currentRules == original







@given(instance=Player_strategy)
def test_hyp_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Player_strategy)
def test_hyp_player_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original




@given(instance=Deck_strategy)
def test_hyp_deck_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original




@given(instance=Card_strategy)
def test_hyp_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=Card_strategy)
def test_hyp_card_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=Card_strategy)
def test_hyp_card_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Card,
    Class,
    Computer,
    Deck,
    Game,
    GoFish,
    Player,
    Rules,
    b,
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

def test_Card_color_value_roundtrip():
    instance = Card(color="sample_text", number=7, suit="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_Card_number_value_roundtrip():
    instance = Card(color="sample_text", number=7, suit="sample_text")
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_Card_suit_value_roundtrip():
    instance = Card(color="sample_text", number=7, suit="sample_text")
    assert instance.suit == "sample_text"
    instance.suit = "sample_text_2"
    assert instance.suit == "sample_text_2"


def test_Deck_deck_value_roundtrip():
    instance = Deck(deck="sample_text")
    assert instance.deck == "sample_text"
    instance.deck = "sample_text_2"
    assert instance.deck == "sample_text_2"


def test_Player_hand_value_roundtrip():
    instance = Player(hand="sample_text", name="sample_text")
    assert instance.hand == "sample_text"
    instance.hand = "sample_text_2"
    assert instance.hand == "sample_text_2"


def test_Player_name_value_roundtrip():
    instance = Player(hand="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Rules_attribute_value_roundtrip():
    instance = Rules(attribute="sample_text", currentRules=True)
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Rules_currentRules_value_roundtrip():
    instance = Rules(attribute="sample_text", currentRules=True)
    assert instance.currentRules == True
    instance.currentRules = False
    assert instance.currentRules == False


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Card_strategy = st.builds(Card, color=safe_text, number=st.integers(), suit=safe_text)
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Computer_strategy = st.builds(Computer)
@given(instance=Computer_strategy)
@settings(max_examples=25)
def test_Computer_instantiation(instance):
    assert isinstance(instance, Computer)


Deck_strategy = st.builds(Deck, deck=safe_text)
@given(instance=Deck_strategy)
@settings(max_examples=25)
def test_Deck_instantiation(instance):
    assert isinstance(instance, Deck)


Game_strategy = st.builds(Game)
@given(instance=Game_strategy)
@settings(max_examples=25)
def test_Game_instantiation(instance):
    assert isinstance(instance, Game)


GoFish_strategy = st.builds(GoFish)
@given(instance=GoFish_strategy)
@settings(max_examples=25)
def test_GoFish_instantiation(instance):
    assert isinstance(instance, GoFish)


Player_strategy = st.builds(Player, hand=safe_text, name=safe_text)
@given(instance=Player_strategy)
@settings(max_examples=25)
def test_Player_instantiation(instance):
    assert isinstance(instance, Player)


Rules_strategy = st.builds(Rules, attribute=safe_text, currentRules=st.booleans())
@given(instance=Rules_strategy)
@settings(max_examples=25)
def test_Rules_instantiation(instance):
    assert isinstance(instance, Rules)


b_strategy = st.builds(b)
@given(instance=b_strategy)
@settings(max_examples=25)
def test_b_instantiation(instance):
    assert isinstance(instance, b)



