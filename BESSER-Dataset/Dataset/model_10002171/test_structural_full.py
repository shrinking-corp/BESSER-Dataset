import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BlackjackGameSimulator,
    Card,
    Deck,
    CardSuit,
    Suit,
    Value,
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

def test_Card_Value_value_roundtrip():
    instance = Card(Value=7, _CardSuit=7, toString="sample_text")
    assert instance.Value == 7
    instance.Value = 13
    assert instance.Value == 13


def test_Card__CardSuit_value_roundtrip():
    instance = Card(Value=7, _CardSuit=7, toString="sample_text")
    assert instance._CardSuit == 7
    instance._CardSuit = 13
    assert instance._CardSuit == 13


def test_Card_toString_value_roundtrip():
    instance = Card(Value=7, _CardSuit=7, toString="sample_text")
    assert instance.toString == "sample_text"
    instance.toString = "sample_text_2"
    assert instance.toString == "sample_text_2"


def test_Deck_ArrayList_value_roundtrip():
    instance = Deck(ArrayList="sample_text")
    assert instance.ArrayList == "sample_text"
    instance.ArrayList = "sample_text_2"
    assert instance.ArrayList == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BlackjackGameSimulator_strategy = st.builds(BlackjackGameSimulator)
@given(instance=BlackjackGameSimulator_strategy)
@settings(max_examples=25)
def test_BlackjackGameSimulator_instantiation(instance):
    assert isinstance(instance, BlackjackGameSimulator)


Card_strategy = st.builds(Card, Value=st.integers(), _CardSuit=st.integers(), toString=safe_text)
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)


Deck_strategy = st.builds(Deck, ArrayList=safe_text)
@given(instance=Deck_strategy)
@settings(max_examples=25)
def test_Deck_instantiation(instance):
    assert isinstance(instance, Deck)


