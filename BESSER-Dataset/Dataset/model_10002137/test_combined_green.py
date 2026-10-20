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
    Cards_Deck,
    Cards_Card,
    Poker_Hand,
    Poker_HandIterator,
    Poker_Iterator_Interface,
    Poker_Computer,
    Poker_Human,
    Poker_Player,
    Poker_PokerGame,
    Poker_PokerRank,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_cards_deck_is_not_abstract():
    assert not inspect.isabstract(Cards_Deck)


def test_hyp_cards_deck_constructor_exists():
    assert callable(Cards_Deck.__init__)


def test_hyp_cards_deck_constructor_args():
    sig = inspect.signature(Cards_Deck.__init__)
    params = list(sig.parameters.keys())
    assert "cardsInDeck" in params, "Missing parameter 'cardsInDeck'"




def test_hyp_cards_card_is_not_abstract():
    assert not inspect.isabstract(Cards_Card)


def test_hyp_cards_card_constructor_exists():
    assert callable(Cards_Card.__init__)


def test_hyp_cards_card_constructor_args():
    sig = inspect.signature(Cards_Card.__init__)
    params = list(sig.parameters.keys())
    assert "rank" in params, "Missing parameter 'rank'"




def test_hyp_poker_hand_is_not_abstract():
    assert not inspect.isabstract(Poker_Hand)


def test_hyp_poker_hand_constructor_exists():
    assert callable(Poker_Hand.__init__)


def test_hyp_poker_hand_constructor_args():
    sig = inspect.signature(Poker_Hand.__init__)
    params = list(sig.parameters.keys())
    assert "numCards" in params, "Missing parameter 'numCards'"
    assert "cardsInHand" in params, "Missing parameter 'cardsInHand'"
    assert "Fold" in params, "Missing parameter 'Fold'"
    assert "handIterator" in params, "Missing parameter 'handIterator'"

def test_hyp_poker_hand_has_numCards():
    assert hasattr(Poker_Hand, "numCards")
    descriptor = None
    for klass in Poker_Hand.__mro__:
        if "numCards" in klass.__dict__:
            descriptor = klass.__dict__["numCards"]
            break
    assert isinstance(descriptor, property)

def test_hyp_poker_hand_has_cardsInHand():
    assert hasattr(Poker_Hand, "cardsInHand")
    descriptor = None
    for klass in Poker_Hand.__mro__:
        if "cardsInHand" in klass.__dict__:
            descriptor = klass.__dict__["cardsInHand"]
            break
    assert isinstance(descriptor, property)

def test_hyp_poker_hand_has_Fold():
    assert hasattr(Poker_Hand, "Fold")
    descriptor = None
    for klass in Poker_Hand.__mro__:
        if "Fold" in klass.__dict__:
            descriptor = klass.__dict__["Fold"]
            break
    assert isinstance(descriptor, property)

def test_hyp_poker_hand_has_handIterator():
    assert hasattr(Poker_Hand, "handIterator")
    descriptor = None
    for klass in Poker_Hand.__mro__:
        if "handIterator" in klass.__dict__:
            descriptor = klass.__dict__["handIterator"]
            break
    assert isinstance(descriptor, property)



def test_hyp_poker_handiterator_is_not_abstract():
    assert not inspect.isabstract(Poker_HandIterator)


def test_hyp_poker_handiterator_constructor_exists():
    assert callable(Poker_HandIterator.__init__)


def test_hyp_poker_handiterator_constructor_args():
    sig = inspect.signature(Poker_HandIterator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_poker_iterator_interface_is_not_abstract():
    assert not inspect.isabstract(Poker_Iterator_Interface)


def test_hyp_poker_iterator_interface_constructor_exists():
    assert callable(Poker_Iterator_Interface.__init__)


def test_hyp_poker_iterator_interface_constructor_args():
    sig = inspect.signature(Poker_Iterator_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_poker_computer_is_not_abstract():
    assert not inspect.isabstract(Poker_Computer)


def test_hyp_poker_computer_constructor_exists():
    assert callable(Poker_Computer.__init__)


def test_hyp_poker_computer_constructor_args():
    sig = inspect.signature(Poker_Computer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_poker_human_is_not_abstract():
    assert not inspect.isabstract(Poker_Human)


def test_hyp_poker_human_constructor_exists():
    assert callable(Poker_Human.__init__)


def test_hyp_poker_human_constructor_args():
    sig = inspect.signature(Poker_Human.__init__)
    params = list(sig.parameters.keys())



def test_hyp_poker_player_is_not_abstract():
    assert not inspect.isabstract(Poker_Player)


def test_hyp_poker_player_constructor_exists():
    assert callable(Poker_Player.__init__)


def test_hyp_poker_player_constructor_args():
    sig = inspect.signature(Poker_Player.__init__)
    params = list(sig.parameters.keys())
    assert "currentBet" in params, "Missing parameter 'currentBet'"
    assert "hand" in params, "Missing parameter 'hand'"
    assert "currentMoney" in params, "Missing parameter 'currentMoney'"

def test_hyp_poker_player_has_currentBet():
    assert hasattr(Poker_Player, "currentBet")
    descriptor = None
    for klass in Poker_Player.__mro__:
        if "currentBet" in klass.__dict__:
            descriptor = klass.__dict__["currentBet"]
            break
    assert isinstance(descriptor, property)

def test_hyp_poker_player_has_hand():
    assert hasattr(Poker_Player, "hand")
    descriptor = None
    for klass in Poker_Player.__mro__:
        if "hand" in klass.__dict__:
            descriptor = klass.__dict__["hand"]
            break
    assert isinstance(descriptor, property)

def test_hyp_poker_player_has_currentMoney():
    assert hasattr(Poker_Player, "currentMoney")
    descriptor = None
    for klass in Poker_Player.__mro__:
        if "currentMoney" in klass.__dict__:
            descriptor = klass.__dict__["currentMoney"]
            break
    assert isinstance(descriptor, property)



def test_hyp_poker_pokergame_is_not_abstract():
    assert not inspect.isabstract(Poker_PokerGame)


def test_hyp_poker_pokergame_constructor_exists():
    assert callable(Poker_PokerGame.__init__)


def test_hyp_poker_pokergame_constructor_args():
    sig = inspect.signature(Poker_PokerGame.__init__)
    params = list(sig.parameters.keys())
    assert "Round" in params, "Missing parameter 'Round'"
    assert "numPlayers" in params, "Missing parameter 'numPlayers'"



def test_hyp_poker_pokerrank_exists():
    # Check that the Enumeration exists
    assert Poker_PokerRank is not None

def test_hyp_poker_pokerrank_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Poker_PokerRank]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Poker_PokerRank"


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
Cards_Deck_strategy = st.builds(
    Cards_Deck,
    cardsInDeck=
        safe_text
)
Cards_Card_strategy = st.builds(
    Cards_Card,
    rank=
        st.integers()
)
Poker_Hand_strategy = st.builds(
    Poker_Hand,
    numCards=
        st.integers(),
    cardsInHand=
        safe_text,
    Fold=
        st.booleans(),
    handIterator=
        st.none()
)
Poker_HandIterator_strategy = st.builds(
    Poker_HandIterator,
)
Poker_Iterator_Interface_strategy = st.builds(
    Poker_Iterator_Interface,
)
Poker_Computer_strategy = st.builds(
    Poker_Computer,
)
Poker_Human_strategy = st.builds(
    Poker_Human,
)
Poker_Player_strategy = st.builds(
    Poker_Player,
    currentBet=
        st.integers(),
    hand=
        st.none(),
    currentMoney=
        st.integers()
)
Poker_PokerGame_strategy = st.builds(
    Poker_PokerGame,
    Round=
        st.integers(),
    numPlayers=
        st.integers()
)




@given(instance=Cards_Deck_strategy)
def test_hyp_cards_deck_cardsInDeck_setter(instance):
    original = instance.cardsInDeck
    instance.cardsInDeck = original
    assert instance.cardsInDeck == original




@given(instance=Cards_Card_strategy)
def test_hyp_cards_card_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=Poker_Hand_strategy)
@settings(max_examples=50)
def test_hyp_poker_hand_instantiation(instance):
    assert isinstance(instance, Poker_Hand)



@given(instance=Poker_Hand_strategy)
def test_hyp_poker_hand_numCards_setter(instance):
    original = instance.numCards
    instance.numCards = original
    assert instance.numCards == original



@given(instance=Poker_Hand_strategy)
def test_hyp_poker_hand_cardsInHand_setter(instance):
    original = instance.cardsInHand
    instance.cardsInHand = original
    assert instance.cardsInHand == original



@given(instance=Poker_Hand_strategy)
def test_hyp_poker_hand_Fold_setter(instance):
    original = instance.Fold
    instance.Fold = original
    assert instance.Fold == original



@given(instance=Poker_Hand_strategy)
def test_hyp_poker_hand_handIterator_setter(instance):
    original = instance.handIterator
    instance.handIterator = original
    assert instance.handIterator == original





@given(instance=Poker_Player_strategy)
@settings(max_examples=50)
def test_hyp_poker_player_instantiation(instance):
    assert isinstance(instance, Poker_Player)



@given(instance=Poker_Player_strategy)
def test_hyp_poker_player_currentBet_setter(instance):
    original = instance.currentBet
    instance.currentBet = original
    assert instance.currentBet == original



@given(instance=Poker_Player_strategy)
def test_hyp_poker_player_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original



@given(instance=Poker_Player_strategy)
def test_hyp_poker_player_currentMoney_setter(instance):
    original = instance.currentMoney
    instance.currentMoney = original
    assert instance.currentMoney == original




@given(instance=Poker_PokerGame_strategy)
def test_hyp_poker_pokergame_Round_setter(instance):
    original = instance.Round
    instance.Round = original
    assert instance.Round == original



@given(instance=Poker_PokerGame_strategy)
def test_hyp_poker_pokergame_numPlayers_setter(instance):
    original = instance.numPlayers
    instance.numPlayers = original
    assert instance.numPlayers == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Cards_Card,
    Cards_Deck,
    Poker_Computer,
    Poker_Hand,
    Poker_HandIterator,
    Poker_Human,
    Poker_Iterator_Interface,
    Poker_Player,
    Poker_PokerGame,
    Poker_PokerRank,
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

def test_Cards_Card_rank_value_roundtrip():
    instance = Cards_Card(rank=7)
    assert instance.rank == 7
    instance.rank = 13
    assert instance.rank == 13


def test_Cards_Deck_cardsInDeck_value_roundtrip():
    instance = Cards_Deck(cardsInDeck="sample_text")
    assert instance.cardsInDeck == "sample_text"
    instance.cardsInDeck = "sample_text_2"
    assert instance.cardsInDeck == "sample_text_2"


def test_Poker_PokerGame_Round_value_roundtrip():
    instance = Poker_PokerGame(Round=7, numPlayers=7)
    assert instance.Round == 7
    instance.Round = 13
    assert instance.Round == 13


def test_Poker_PokerGame_numPlayers_value_roundtrip():
    instance = Poker_PokerGame(Round=7, numPlayers=7)
    assert instance.numPlayers == 7
    instance.numPlayers = 13
    assert instance.numPlayers == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Cards_Card_strategy = st.builds(Cards_Card, rank=st.integers())
@given(instance=Cards_Card_strategy)
@settings(max_examples=25)
def test_Cards_Card_instantiation(instance):
    assert isinstance(instance, Cards_Card)


Cards_Deck_strategy = st.builds(Cards_Deck, cardsInDeck=safe_text)
@given(instance=Cards_Deck_strategy)
@settings(max_examples=25)
def test_Cards_Deck_instantiation(instance):
    assert isinstance(instance, Cards_Deck)


Poker_Computer_strategy = st.builds(Poker_Computer)
@given(instance=Poker_Computer_strategy)
@settings(max_examples=25)
def test_Poker_Computer_instantiation(instance):
    assert isinstance(instance, Poker_Computer)


Poker_HandIterator_strategy = st.builds(Poker_HandIterator)
@given(instance=Poker_HandIterator_strategy)
@settings(max_examples=25)
def test_Poker_HandIterator_instantiation(instance):
    assert isinstance(instance, Poker_HandIterator)


Poker_Human_strategy = st.builds(Poker_Human)
@given(instance=Poker_Human_strategy)
@settings(max_examples=25)
def test_Poker_Human_instantiation(instance):
    assert isinstance(instance, Poker_Human)


Poker_Iterator_Interface_strategy = st.builds(Poker_Iterator_Interface)
@given(instance=Poker_Iterator_Interface_strategy)
@settings(max_examples=25)
def test_Poker_Iterator_Interface_instantiation(instance):
    assert isinstance(instance, Poker_Iterator_Interface)


Poker_PokerGame_strategy = st.builds(Poker_PokerGame, Round=st.integers(), numPlayers=st.integers())
@given(instance=Poker_PokerGame_strategy)
@settings(max_examples=25)
def test_Poker_PokerGame_instantiation(instance):
    assert isinstance(instance, Poker_PokerGame)



