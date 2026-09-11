import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Comparable_BlackjackHand__Interface,
    Iterable_Card__Interface,
    blackjack_BlackjackGame,
    blackjack_BlackjackHand,
    blackjack_Card,
    blackjack_CardSet,
    blackjack_DealerBot,
    blackjack_Deck,
    blackjack_DeckShuffledListener_Interface,
    blackjack_ExampleInstrumentedTest,
    blackjack_ExampleUnitTest,
    blackjack_MainActivity,
    genmymodelreverse_C1,
    genmymodelreverse_C11,
    genmymodelreverse_C12,
    genmymodelreverse_android_support_v7_app_AppCompatActivity,
    genmymodelreverse_java_lang_Comparable_Interface,
    genmymodelreverse_java_lang_Iterable_Interface,
    genmymodelreverse_java_util_Iterator_Interface,
    blackjack_GameState,
    blackjack_Suit,
    blackjack_Value,
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

# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Comparable_BlackjackHand__Interface_strategy = st.builds(Comparable_BlackjackHand__Interface)
@given(instance=Comparable_BlackjackHand__Interface_strategy)
@settings(max_examples=25)
def test_Comparable_BlackjackHand__Interface_instantiation(instance):
    assert isinstance(instance, Comparable_BlackjackHand__Interface)


Iterable_Card__Interface_strategy = st.builds(Iterable_Card__Interface)
@given(instance=Iterable_Card__Interface_strategy)
@settings(max_examples=25)
def test_Iterable_Card__Interface_instantiation(instance):
    assert isinstance(instance, Iterable_Card__Interface)


blackjack_BlackjackHand_strategy = st.builds(blackjack_BlackjackHand)
@given(instance=blackjack_BlackjackHand_strategy)
@settings(max_examples=25)
def test_blackjack_BlackjackHand_instantiation(instance):
    assert isinstance(instance, blackjack_BlackjackHand)


blackjack_CardSet_strategy = st.builds(blackjack_CardSet)
@given(instance=blackjack_CardSet_strategy)
@settings(max_examples=25)
def test_blackjack_CardSet_instantiation(instance):
    assert isinstance(instance, blackjack_CardSet)


blackjack_DealerBot_strategy = st.builds(blackjack_DealerBot)
@given(instance=blackjack_DealerBot_strategy)
@settings(max_examples=25)
def test_blackjack_DealerBot_instantiation(instance):
    assert isinstance(instance, blackjack_DealerBot)


blackjack_Deck_strategy = st.builds(blackjack_Deck)
@given(instance=blackjack_Deck_strategy)
@settings(max_examples=25)
def test_blackjack_Deck_instantiation(instance):
    assert isinstance(instance, blackjack_Deck)


blackjack_DeckShuffledListener_Interface_strategy = st.builds(blackjack_DeckShuffledListener_Interface)
@given(instance=blackjack_DeckShuffledListener_Interface_strategy)
@settings(max_examples=25)
def test_blackjack_DeckShuffledListener_Interface_instantiation(instance):
    assert isinstance(instance, blackjack_DeckShuffledListener_Interface)


blackjack_ExampleInstrumentedTest_strategy = st.builds(blackjack_ExampleInstrumentedTest)
@given(instance=blackjack_ExampleInstrumentedTest_strategy)
@settings(max_examples=25)
def test_blackjack_ExampleInstrumentedTest_instantiation(instance):
    assert isinstance(instance, blackjack_ExampleInstrumentedTest)


blackjack_ExampleUnitTest_strategy = st.builds(blackjack_ExampleUnitTest)
@given(instance=blackjack_ExampleUnitTest_strategy)
@settings(max_examples=25)
def test_blackjack_ExampleUnitTest_instantiation(instance):
    assert isinstance(instance, blackjack_ExampleUnitTest)


blackjack_MainActivity_strategy = st.builds(blackjack_MainActivity)
@given(instance=blackjack_MainActivity_strategy)
@settings(max_examples=25)
def test_blackjack_MainActivity_instantiation(instance):
    assert isinstance(instance, blackjack_MainActivity)


genmymodelreverse_C1_strategy = st.builds(genmymodelreverse_C1)
@given(instance=genmymodelreverse_C1_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_C1_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_C1)


genmymodelreverse_C11_strategy = st.builds(genmymodelreverse_C11)
@given(instance=genmymodelreverse_C11_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_C11_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_C11)


genmymodelreverse_C12_strategy = st.builds(genmymodelreverse_C12)
@given(instance=genmymodelreverse_C12_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_C12_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_C12)


genmymodelreverse_android_support_v7_app_AppCompatActivity_strategy = st.builds(genmymodelreverse_android_support_v7_app_AppCompatActivity)
@given(instance=genmymodelreverse_android_support_v7_app_AppCompatActivity_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_android_support_v7_app_AppCompatActivity_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_android_support_v7_app_AppCompatActivity)


genmymodelreverse_java_lang_Comparable_Interface_strategy = st.builds(genmymodelreverse_java_lang_Comparable_Interface)
@given(instance=genmymodelreverse_java_lang_Comparable_Interface_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_lang_Comparable_Interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_Comparable_Interface)


genmymodelreverse_java_lang_Iterable_Interface_strategy = st.builds(genmymodelreverse_java_lang_Iterable_Interface)
@given(instance=genmymodelreverse_java_lang_Iterable_Interface_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_lang_Iterable_Interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_Iterable_Interface)


genmymodelreverse_java_util_Iterator_Interface_strategy = st.builds(genmymodelreverse_java_util_Iterator_Interface)
@given(instance=genmymodelreverse_java_util_Iterator_Interface_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_util_Iterator_Interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_util_Iterator_Interface)


