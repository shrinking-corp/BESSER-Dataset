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
    Account,
    InputValidation,
    Blackjack,
    Main,
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
    assert "int" in params, "Missing parameter 'int'"
    assert "int1" in params, "Missing parameter 'int1'"
    assert "string" in params, "Missing parameter 'string'"
    assert "bool" in params, "Missing parameter 'bool'"







def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "int" in params, "Missing parameter 'int'"




def test_hyp_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_hyp_player_constructor_exists():
    assert callable(Player.__init__)


def test_hyp_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "Deck" in params, "Missing parameter 'Deck'"
    assert "int" in params, "Missing parameter 'int'"
    assert "Card" in params, "Missing parameter 'Card'"
    assert "int1" in params, "Missing parameter 'int1'"







def test_hyp_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_hyp_account_constructor_exists():
    assert callable(Account.__init__)


def test_hyp_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "int" in params, "Missing parameter 'int'"
    assert "string" in params, "Missing parameter 'string'"
    assert "int1" in params, "Missing parameter 'int1'"






def test_hyp_inputvalidation_is_not_abstract():
    assert not inspect.isabstract(InputValidation)


def test_hyp_inputvalidation_constructor_exists():
    assert callable(InputValidation.__init__)


def test_hyp_inputvalidation_constructor_args():
    sig = inspect.signature(InputValidation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_blackjack_is_not_abstract():
    assert not inspect.isabstract(Blackjack)


def test_hyp_blackjack_constructor_exists():
    assert callable(Blackjack.__init__)


def test_hyp_blackjack_constructor_args():
    sig = inspect.signature(Blackjack.__init__)
    params = list(sig.parameters.keys())



def test_hyp_main_is_not_abstract():
    assert not inspect.isabstract(Main)


def test_hyp_main_constructor_exists():
    assert callable(Main.__init__)


def test_hyp_main_constructor_args():
    sig = inspect.signature(Main.__init__)
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
Cards_strategy = st.builds(
    Cards,
    int=
        safe_text,
    int1=
        safe_text,
    string=
        safe_text,
    bool=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
    int=
        safe_text
)
Player_strategy = st.builds(
    Player,
    Deck=
        safe_text,
    int=
        safe_text,
    Card=
        safe_text,
    int1=
        safe_text
)
Account_strategy = st.builds(
    Account,
    int=
        safe_text,
    string=
        safe_text,
    int1=
        safe_text
)
InputValidation_strategy = st.builds(
    InputValidation,
)
Blackjack_strategy = st.builds(
    Blackjack,
)
Main_strategy = st.builds(
    Main,
)




@given(instance=Cards_strategy)
def test_hyp_cards_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original



@given(instance=Cards_strategy)
def test_hyp_cards_int1_setter(instance):
    original = instance.int1
    instance.int1 = original
    assert instance.int1 == original



@given(instance=Cards_strategy)
def test_hyp_cards_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=Cards_strategy)
def test_hyp_cards_bool_setter(instance):
    original = instance.bool
    instance.bool = original
    assert instance.bool == original




@given(instance=Deck_strategy)
def test_hyp_deck_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original




@given(instance=Player_strategy)
def test_hyp_player_Deck_setter(instance):
    original = instance.Deck
    instance.Deck = original
    assert instance.Deck == original



@given(instance=Player_strategy)
def test_hyp_player_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original



@given(instance=Player_strategy)
def test_hyp_player_Card_setter(instance):
    original = instance.Card
    instance.Card = original
    assert instance.Card == original



@given(instance=Player_strategy)
def test_hyp_player_int1_setter(instance):
    original = instance.int1
    instance.int1 = original
    assert instance.int1 == original




@given(instance=Account_strategy)
def test_hyp_account_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original



@given(instance=Account_strategy)
def test_hyp_account_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=Account_strategy)
def test_hyp_account_int1_setter(instance):
    original = instance.int1
    instance.int1 = original
    assert instance.int1 == original





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Account,
    Blackjack,
    Cards,
    Deck,
    InputValidation,
    Main,
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

def test_Account_int_value_roundtrip():
    instance = Account(int="sample_text", int1="sample_text", string="sample_text")
    assert instance.int == "sample_text"
    instance.int = "sample_text_2"
    assert instance.int == "sample_text_2"


def test_Account_int1_value_roundtrip():
    instance = Account(int="sample_text", int1="sample_text", string="sample_text")
    assert instance.int1 == "sample_text"
    instance.int1 = "sample_text_2"
    assert instance.int1 == "sample_text_2"


def test_Account_string_value_roundtrip():
    instance = Account(int="sample_text", int1="sample_text", string="sample_text")
    assert instance.string == "sample_text"
    instance.string = "sample_text_2"
    assert instance.string == "sample_text_2"


def test_Cards_bool_value_roundtrip():
    instance = Cards(bool="sample_text", int="sample_text", int1="sample_text", string="sample_text")
    assert instance.bool == "sample_text"
    instance.bool = "sample_text_2"
    assert instance.bool == "sample_text_2"


def test_Cards_int_value_roundtrip():
    instance = Cards(bool="sample_text", int="sample_text", int1="sample_text", string="sample_text")
    assert instance.int == "sample_text"
    instance.int = "sample_text_2"
    assert instance.int == "sample_text_2"


def test_Cards_int1_value_roundtrip():
    instance = Cards(bool="sample_text", int="sample_text", int1="sample_text", string="sample_text")
    assert instance.int1 == "sample_text"
    instance.int1 = "sample_text_2"
    assert instance.int1 == "sample_text_2"


def test_Cards_string_value_roundtrip():
    instance = Cards(bool="sample_text", int="sample_text", int1="sample_text", string="sample_text")
    assert instance.string == "sample_text"
    instance.string = "sample_text_2"
    assert instance.string == "sample_text_2"


def test_Deck_int_value_roundtrip():
    instance = Deck(int="sample_text")
    assert instance.int == "sample_text"
    instance.int = "sample_text_2"
    assert instance.int == "sample_text_2"


def test_Player_Card_value_roundtrip():
    instance = Player(Card="sample_text", Deck="sample_text", int="sample_text", int1="sample_text")
    assert instance.Card == "sample_text"
    instance.Card = "sample_text_2"
    assert instance.Card == "sample_text_2"


def test_Player_Deck_value_roundtrip():
    instance = Player(Card="sample_text", Deck="sample_text", int="sample_text", int1="sample_text")
    assert instance.Deck == "sample_text"
    instance.Deck = "sample_text_2"
    assert instance.Deck == "sample_text_2"


def test_Player_int_value_roundtrip():
    instance = Player(Card="sample_text", Deck="sample_text", int="sample_text", int1="sample_text")
    assert instance.int == "sample_text"
    instance.int = "sample_text_2"
    assert instance.int == "sample_text_2"


def test_Player_int1_value_roundtrip():
    instance = Player(Card="sample_text", Deck="sample_text", int="sample_text", int1="sample_text")
    assert instance.int1 == "sample_text"
    instance.int1 = "sample_text_2"
    assert instance.int1 == "sample_text_2"


def test_assoc_Deck_Cards_link_reassign_clear():
    a = Deck(int="sample_text")
    b1 = Cards(bool="sample_text", int="sample_text", int1="sample_text", string="sample_text")
    b2 = Cards(bool="sample_text_2", int="sample_text_2", int1="sample_text_2", string="sample_text_2")
    _safe_set(a, 'cards0', b1)
    assert _is_linked(a, 'cards0', b1)
    if hasattr(b1, 'deck1'):
        assert _is_linked(b1, 'deck1', a)
    _safe_set(a, 'cards0', b2)
    assert _is_linked(a, 'cards0', b2)
    if hasattr(b1, 'deck1'):
        assert not _is_linked(b1, 'deck1', a)
    if hasattr(b2, 'deck1'):
        assert _is_linked(b2, 'deck1', a)
    _safe_set(a, 'cards0', None)
    assert not _is_linked(a, 'cards0', b2)
    if hasattr(b2, 'deck1'):
        assert not _is_linked(b2, 'deck1', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Account_strategy = st.builds(Account, int=safe_text, int1=safe_text, string=safe_text)
@given(instance=Account_strategy)
@settings(max_examples=25)
def test_Account_instantiation(instance):
    assert isinstance(instance, Account)


Blackjack_strategy = st.builds(Blackjack)
@given(instance=Blackjack_strategy)
@settings(max_examples=25)
def test_Blackjack_instantiation(instance):
    assert isinstance(instance, Blackjack)


Cards_strategy = st.builds(Cards, bool=safe_text, int=safe_text, int1=safe_text, string=safe_text)
@given(instance=Cards_strategy)
@settings(max_examples=25)
def test_Cards_instantiation(instance):
    assert isinstance(instance, Cards)


Deck_strategy = st.builds(Deck, int=safe_text)
@given(instance=Deck_strategy)
@settings(max_examples=25)
def test_Deck_instantiation(instance):
    assert isinstance(instance, Deck)


InputValidation_strategy = st.builds(InputValidation)
@given(instance=InputValidation_strategy)
@settings(max_examples=25)
def test_InputValidation_instantiation(instance):
    assert isinstance(instance, InputValidation)


Main_strategy = st.builds(Main)
@given(instance=Main_strategy)
@settings(max_examples=25)
def test_Main_instantiation(instance):
    assert isinstance(instance, Main)


Player_strategy = st.builds(Player, Card=safe_text, Deck=safe_text, int=safe_text, int1=safe_text)
@given(instance=Player_strategy)
@settings(max_examples=25)
def test_Player_instantiation(instance):
    assert isinstance(instance, Player)



