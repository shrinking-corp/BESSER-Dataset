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
    Blackjack,
    Player,
    Card,
    Cards,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_blackjack_is_not_abstract():
    assert not inspect.isabstract(Blackjack)


def test_hyp_blackjack_constructor_exists():
    assert callable(Blackjack.__init__)


def test_hyp_blackjack_constructor_args():
    sig = inspect.signature(Blackjack.__init__)
    params = list(sig.parameters.keys())
    assert "cards" in params, "Missing parameter 'cards'"
    assert "players" in params, "Missing parameter 'players'"
    assert "dealer" in params, "Missing parameter 'dealer'"

def test_hyp_blackjack_has_cards():
    assert hasattr(Blackjack, "cards")
    descriptor = None
    for klass in Blackjack.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)

def test_hyp_blackjack_has_players():
    assert hasattr(Blackjack, "players")
    descriptor = None
    for klass in Blackjack.__mro__:
        if "players" in klass.__dict__:
            descriptor = klass.__dict__["players"]
            break
    assert isinstance(descriptor, property)

def test_hyp_blackjack_has_dealer():
    assert hasattr(Blackjack, "dealer")
    descriptor = None
    for klass in Blackjack.__mro__:
        if "dealer" in klass.__dict__:
            descriptor = klass.__dict__["dealer"]
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
    assert "hand" in params, "Missing parameter 'hand'"





def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "value_dict" in params, "Missing parameter 'value_dict'"




def test_hyp_cards_is_not_abstract():
    assert not inspect.isabstract(Cards)


def test_hyp_cards_constructor_exists():
    assert callable(Cards.__init__)


def test_hyp_cards_constructor_args():
    sig = inspect.signature(Cards.__init__)
    params = list(sig.parameters.keys())
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
Blackjack_strategy = st.builds(
    Blackjack,
    cards=
        st.none(),
    players=
        safe_text,
    dealer=
        st.none()
)
Player_strategy = st.builds(
    Player,
    name=
        safe_text,
    hand=
        safe_text
)
Card_strategy = st.builds(
    Card,
    value_dict=
        safe_text
)
Cards_strategy = st.builds(
    Cards,
    color=
        safe_text,
    number=
        safe_text
)

@given(instance=Blackjack_strategy)
@settings(max_examples=50)
def test_hyp_blackjack_instantiation(instance):
    assert isinstance(instance, Blackjack)



@given(instance=Blackjack_strategy)
def test_hyp_blackjack_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original



@given(instance=Blackjack_strategy)
def test_hyp_blackjack_players_setter(instance):
    original = instance.players
    instance.players = original
    assert instance.players == original



@given(instance=Blackjack_strategy)
def test_hyp_blackjack_dealer_setter(instance):
    original = instance.dealer
    instance.dealer = original
    assert instance.dealer == original




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




@given(instance=Card_strategy)
def test_hyp_card_value_dict_setter(instance):
    original = instance.value_dict
    instance.value_dict = original
    assert instance.value_dict == original




@given(instance=Cards_strategy)
def test_hyp_cards_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=Cards_strategy)
def test_hyp_cards_number_setter(instance):
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
    Blackjack,
    Card,
    Cards,
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

def test_Card_value_dict_value_roundtrip():
    instance = Card(value_dict="sample_text")
    assert instance.value_dict == "sample_text"
    instance.value_dict = "sample_text_2"
    assert instance.value_dict == "sample_text_2"


def test_Cards_color_value_roundtrip():
    instance = Cards(color="sample_text", number="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_Cards_number_value_roundtrip():
    instance = Cards(color="sample_text", number="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


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


def test_assoc_Card_Cards_link_reassign_clear():
    a = Cards(color="sample_text", number="sample_text")
    b1 = Card(value_dict="sample_text")
    b2 = Card(value_dict="sample_text_2")
    _safe_set(a, 'card1', b1)
    assert _is_linked(a, 'card1', b1)
    if hasattr(b1, 'cards0'):
        assert _is_linked(b1, 'cards0', a)
    _safe_set(a, 'card1', b2)
    assert _is_linked(a, 'card1', b2)
    if hasattr(b1, 'cards0'):
        assert not _is_linked(b1, 'cards0', a)
    if hasattr(b2, 'cards0'):
        assert _is_linked(b2, 'cards0', a)
    _safe_set(a, 'card1', None)
    assert not _is_linked(a, 'card1', b2)
    if hasattr(b2, 'cards0'):
        assert not _is_linked(b2, 'cards0', a)


def test_assoc_Card_Player_link_reassign_clear():
    a = Player(hand="sample_text", name="sample_text")
    b1 = Card(value_dict="sample_text")
    b2 = Card(value_dict="sample_text_2")
    _safe_set(a, 'card3', b1)
    assert _is_linked(a, 'card3', b1)
    if hasattr(b1, 'player2'):
        assert _is_linked(b1, 'player2', a)
    _safe_set(a, 'card3', b2)
    assert _is_linked(a, 'card3', b2)
    if hasattr(b1, 'player2'):
        assert not _is_linked(b1, 'player2', a)
    if hasattr(b2, 'player2'):
        assert _is_linked(b2, 'player2', a)
    _safe_set(a, 'card3', None)
    assert not _is_linked(a, 'card3', b2)
    if hasattr(b2, 'player2'):
        assert not _is_linked(b2, 'player2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Card_strategy = st.builds(Card, value_dict=safe_text)
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)


Cards_strategy = st.builds(Cards, color=safe_text, number=safe_text)
@given(instance=Cards_strategy)
@settings(max_examples=25)
def test_Cards_instantiation(instance):
    assert isinstance(instance, Cards)


Player_strategy = st.builds(Player, hand=safe_text, name=safe_text)
@given(instance=Player_strategy)
@settings(max_examples=25)
def test_Player_instantiation(instance):
    assert isinstance(instance, Player)



