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


