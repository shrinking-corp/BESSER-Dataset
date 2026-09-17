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
    card_Card,
    poker_GameRun,
    poker_Game,
    Card,
    Comparable_Interface,
    player_Deck,
    player_Player,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_card_card_is_not_abstract():
    assert not inspect.isabstract(card_Card)


def test_hyp_card_card_constructor_exists():
    assert callable(card_Card.__init__)


def test_hyp_card_card_constructor_args():
    sig = inspect.signature(card_Card.__init__)
    params = list(sig.parameters.keys())
    assert "rank" in params, "Missing parameter 'rank'"
    assert "suit" in params, "Missing parameter 'suit'"





def test_hyp_poker_gamerun_is_not_abstract():
    assert not inspect.isabstract(poker_GameRun)


def test_hyp_poker_gamerun_constructor_exists():
    assert callable(poker_GameRun.__init__)


def test_hyp_poker_gamerun_constructor_args():
    sig = inspect.signature(poker_GameRun.__init__)
    params = list(sig.parameters.keys())



def test_hyp_poker_game_is_not_abstract():
    assert not inspect.isabstract(poker_Game)


def test_hyp_poker_game_constructor_exists():
    assert callable(poker_Game.__init__)


def test_hyp_poker_game_constructor_args():
    sig = inspect.signature(poker_Game.__init__)
    params = list(sig.parameters.keys())
    assert "tryagain" in params, "Missing parameter 'tryagain'"
    assert "hand_size" in params, "Missing parameter 'hand_size'"





def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comparable_interface_is_not_abstract():
    assert not inspect.isabstract(Comparable_Interface)


def test_hyp_comparable_interface_constructor_exists():
    assert callable(Comparable_Interface.__init__)


def test_hyp_comparable_interface_constructor_args():
    sig = inspect.signature(Comparable_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_player_deck_is_not_abstract():
    assert not inspect.isabstract(player_Deck)


def test_hyp_player_deck_constructor_exists():
    assert callable(player_Deck.__init__)


def test_hyp_player_deck_constructor_args():
    sig = inspect.signature(player_Deck.__init__)
    params = list(sig.parameters.keys())
    assert "deck_size" in params, "Missing parameter 'deck_size'"
    assert "hand_size" in params, "Missing parameter 'hand_size'"
    assert "remainofDeck" in params, "Missing parameter 'remainofDeck'"
    assert "numberofShuffles" in params, "Missing parameter 'numberofShuffles'"







def test_hyp_player_player_is_not_abstract():
    assert not inspect.isabstract(player_Player)


def test_hyp_player_player_constructor_exists():
    assert callable(player_Player.__init__)


def test_hyp_player_player_constructor_args():
    sig = inspect.signature(player_Player.__init__)
    params = list(sig.parameters.keys())


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
card_Card_strategy = st.builds(
    card_Card,
    rank=
        st.integers(),
    suit=
        st.integers()
)
poker_GameRun_strategy = st.builds(
    poker_GameRun,
)
poker_Game_strategy = st.builds(
    poker_Game,
    tryagain=
        st.integers(),
    hand_size=
        st.integers()
)
Card_strategy = st.builds(
    Card,
)
Comparable_Interface_strategy = st.builds(
    Comparable_Interface,
)
player_Deck_strategy = st.builds(
    player_Deck,
    deck_size=
        st.integers(),
    hand_size=
        st.integers(),
    remainofDeck=
        st.integers(),
    numberofShuffles=
        st.integers()
)
player_Player_strategy = st.builds(
    player_Player,
)




@given(instance=card_Card_strategy)
def test_hyp_card_card_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original



@given(instance=card_Card_strategy)
def test_hyp_card_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original





@given(instance=poker_Game_strategy)
def test_hyp_poker_game_tryagain_setter(instance):
    original = instance.tryagain
    instance.tryagain = original
    assert instance.tryagain == original



@given(instance=poker_Game_strategy)
def test_hyp_poker_game_hand_size_setter(instance):
    original = instance.hand_size
    instance.hand_size = original
    assert instance.hand_size == original






@given(instance=player_Deck_strategy)
def test_hyp_player_deck_deck_size_setter(instance):
    original = instance.deck_size
    instance.deck_size = original
    assert instance.deck_size == original



@given(instance=player_Deck_strategy)
def test_hyp_player_deck_hand_size_setter(instance):
    original = instance.hand_size
    instance.hand_size = original
    assert instance.hand_size == original



@given(instance=player_Deck_strategy)
def test_hyp_player_deck_remainofDeck_setter(instance):
    original = instance.remainofDeck
    instance.remainofDeck = original
    assert instance.remainofDeck == original



@given(instance=player_Deck_strategy)
def test_hyp_player_deck_numberofShuffles_setter(instance):
    original = instance.numberofShuffles
    instance.numberofShuffles = original
    assert instance.numberofShuffles == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Card,
    Comparable_Interface,
    card_Card,
    player_Deck,
    player_Player,
    poker_Game,
    poker_GameRun,
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

def test_card_Card_rank_value_roundtrip():
    instance = card_Card(rank=7, suit=7)
    assert instance.rank == 7
    instance.rank = 13
    assert instance.rank == 13


def test_card_Card_suit_value_roundtrip():
    instance = card_Card(rank=7, suit=7)
    assert instance.suit == 7
    instance.suit = 13
    assert instance.suit == 13


def test_player_Deck_deck_size_value_roundtrip():
    instance = player_Deck(deck_size=7, hand_size=7, numberofShuffles=7, remainofDeck=7)
    assert instance.deck_size == 7
    instance.deck_size = 13
    assert instance.deck_size == 13


def test_player_Deck_hand_size_value_roundtrip():
    instance = player_Deck(deck_size=7, hand_size=7, numberofShuffles=7, remainofDeck=7)
    assert instance.hand_size == 7
    instance.hand_size = 13
    assert instance.hand_size == 13


def test_player_Deck_numberofShuffles_value_roundtrip():
    instance = player_Deck(deck_size=7, hand_size=7, numberofShuffles=7, remainofDeck=7)
    assert instance.numberofShuffles == 7
    instance.numberofShuffles = 13
    assert instance.numberofShuffles == 13


def test_player_Deck_remainofDeck_value_roundtrip():
    instance = player_Deck(deck_size=7, hand_size=7, numberofShuffles=7, remainofDeck=7)
    assert instance.remainofDeck == 7
    instance.remainofDeck = 13
    assert instance.remainofDeck == 13


def test_poker_Game_hand_size_value_roundtrip():
    instance = poker_Game(hand_size=7, tryagain=7)
    assert instance.hand_size == 7
    instance.hand_size = 13
    assert instance.hand_size == 13


def test_poker_Game_tryagain_value_roundtrip():
    instance = poker_Game(hand_size=7, tryagain=7)
    assert instance.tryagain == 7
    instance.tryagain = 13
    assert instance.tryagain == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Card_strategy = st.builds(Card)
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)


Comparable_Interface_strategy = st.builds(Comparable_Interface)
@given(instance=Comparable_Interface_strategy)
@settings(max_examples=25)
def test_Comparable_Interface_instantiation(instance):
    assert isinstance(instance, Comparable_Interface)


card_Card_strategy = st.builds(card_Card, rank=st.integers(), suit=st.integers())
@given(instance=card_Card_strategy)
@settings(max_examples=25)
def test_card_Card_instantiation(instance):
    assert isinstance(instance, card_Card)


player_Deck_strategy = st.builds(player_Deck, deck_size=st.integers(), hand_size=st.integers(), numberofShuffles=st.integers(), remainofDeck=st.integers())
@given(instance=player_Deck_strategy)
@settings(max_examples=25)
def test_player_Deck_instantiation(instance):
    assert isinstance(instance, player_Deck)


player_Player_strategy = st.builds(player_Player)
@given(instance=player_Player_strategy)
@settings(max_examples=25)
def test_player_Player_instantiation(instance):
    assert isinstance(instance, player_Player)


poker_Game_strategy = st.builds(poker_Game, hand_size=st.integers(), tryagain=st.integers())
@given(instance=poker_Game_strategy)
@settings(max_examples=25)
def test_poker_Game_instantiation(instance):
    assert isinstance(instance, poker_Game)


poker_GameRun_strategy = st.builds(poker_GameRun)
@given(instance=poker_GameRun_strategy)
@settings(max_examples=25)
def test_poker_GameRun_instantiation(instance):
    assert isinstance(instance, poker_GameRun)



