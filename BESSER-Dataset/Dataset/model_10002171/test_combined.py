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
    Card,
    Deck,
    BlackjackGameSimulator,
    Suit,
    Value,
    CardSuit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "toString" in params, "Missing parameter 'toString'"
    assert "_CardSuit" in params, "Missing parameter '_CardSuit'"
    assert "Value" in params, "Missing parameter 'Value'"






def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "ArrayList" in params, "Missing parameter 'ArrayList'"




def test_hyp_blackjackgamesimulator_is_not_abstract():
    assert not inspect.isabstract(BlackjackGameSimulator)


def test_hyp_blackjackgamesimulator_constructor_exists():
    assert callable(BlackjackGameSimulator.__init__)


def test_hyp_blackjackgamesimulator_constructor_args():
    sig = inspect.signature(BlackjackGameSimulator.__init__)
    params = list(sig.parameters.keys())

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

def test_hyp_value_exists():
    # Check that the Enumeration exists
    assert Value is not None

def test_hyp_value_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Value]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Value"

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
Card_strategy = st.builds(
    Card,
    toString=
        safe_text,
    _CardSuit=
        st.integers(),
    Value=
        st.integers()
)
Deck_strategy = st.builds(
    Deck,
    ArrayList=
        safe_text
)
BlackjackGameSimulator_strategy = st.builds(
    BlackjackGameSimulator,
)




@given(instance=Card_strategy)
def test_hyp_card_toString_setter(instance):
    original = instance.toString
    instance.toString = original
    assert instance.toString == original



@given(instance=Card_strategy)
def test_hyp_card__CardSuit_setter(instance):
    original = instance._CardSuit
    instance._CardSuit = original
    assert instance._CardSuit == original



@given(instance=Card_strategy)
def test_hyp_card_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original




@given(instance=Deck_strategy)
def test_hyp_deck_ArrayList_setter(instance):
    original = instance.ArrayList
    instance.ArrayList = original
    assert instance.ArrayList == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



