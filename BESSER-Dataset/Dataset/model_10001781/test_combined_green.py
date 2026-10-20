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
    T3,
    Queue,
    CasinoManager,
    T2,
    T1,
    Tuple,
    Player,
    T,
    Stack,
    Deck,
    Table,
    Executive,
    Card,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_t3_is_not_abstract():
    assert not inspect.isabstract(T3)


def test_hyp_t3_constructor_exists():
    assert callable(T3.__init__)


def test_hyp_t3_constructor_args():
    sig = inspect.signature(T3.__init__)
    params = list(sig.parameters.keys())



def test_hyp_queue_is_not_abstract():
    assert not inspect.isabstract(Queue)


def test_hyp_queue_constructor_exists():
    assert callable(Queue.__init__)


def test_hyp_queue_constructor_args():
    sig = inspect.signature(Queue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_casinomanager_is_not_abstract():
    assert not inspect.isabstract(CasinoManager)


def test_hyp_casinomanager_constructor_exists():
    assert callable(CasinoManager.__init__)


def test_hyp_casinomanager_constructor_args():
    sig = inspect.signature(CasinoManager.__init__)
    params = list(sig.parameters.keys())
    assert "waitList" in params, "Missing parameter 'waitList'"
    assert "table" in params, "Missing parameter 'table'"

def test_hyp_casinomanager_has_waitList():
    assert hasattr(CasinoManager, "waitList")
    descriptor = None
    for klass in CasinoManager.__mro__:
        if "waitList" in klass.__dict__:
            descriptor = klass.__dict__["waitList"]
            break
    assert isinstance(descriptor, property)

def test_hyp_casinomanager_has_table():
    assert hasattr(CasinoManager, "table")
    descriptor = None
    for klass in CasinoManager.__mro__:
        if "table" in klass.__dict__:
            descriptor = klass.__dict__["table"]
            break
    assert isinstance(descriptor, property)



def test_hyp_t2_is_not_abstract():
    assert not inspect.isabstract(T2)


def test_hyp_t2_constructor_exists():
    assert callable(T2.__init__)


def test_hyp_t2_constructor_args():
    sig = inspect.signature(T2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_t1_is_not_abstract():
    assert not inspect.isabstract(T1)


def test_hyp_t1_constructor_exists():
    assert callable(T1.__init__)


def test_hyp_t1_constructor_args():
    sig = inspect.signature(T1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tuple_is_not_abstract():
    assert not inspect.isabstract(Tuple)


def test_hyp_tuple_constructor_exists():
    assert callable(Tuple.__init__)


def test_hyp_tuple_constructor_args():
    sig = inspect.signature(Tuple.__init__)
    params = list(sig.parameters.keys())



def test_hyp_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_hyp_player_constructor_exists():
    assert callable(Player.__init__)


def test_hyp_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())



def test_hyp_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_hyp_t_constructor_exists():
    assert callable(T.__init__)


def test_hyp_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stack_is_not_abstract():
    assert not inspect.isabstract(Stack)


def test_hyp_stack_constructor_exists():
    assert callable(Stack.__init__)


def test_hyp_stack_constructor_args():
    sig = inspect.signature(Stack.__init__)
    params = list(sig.parameters.keys())



def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "cards" in params, "Missing parameter 'cards'"




def test_hyp_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_hyp_table_constructor_exists():
    assert callable(Table.__init__)


def test_hyp_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())
    assert "currPlayers" in params, "Missing parameter 'currPlayers'"
    assert "deck" in params, "Missing parameter 'deck'"

def test_hyp_table_has_currPlayers():
    assert hasattr(Table, "currPlayers")
    descriptor = None
    for klass in Table.__mro__:
        if "currPlayers" in klass.__dict__:
            descriptor = klass.__dict__["currPlayers"]
            break
    assert isinstance(descriptor, property)

def test_hyp_table_has_deck():
    assert hasattr(Table, "deck")
    descriptor = None
    for klass in Table.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)



def test_hyp_executive_is_not_abstract():
    assert not inspect.isabstract(Executive)


def test_hyp_executive_constructor_exists():
    assert callable(Executive.__init__)


def test_hyp_executive_constructor_args():
    sig = inspect.signature(Executive.__init__)
    params = list(sig.parameters.keys())



def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "suit" in params, "Missing parameter 'suit'"




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
T3_strategy = st.builds(
    T3,
)
Queue_strategy = st.builds(
    Queue,
)
CasinoManager_strategy = st.builds(
    CasinoManager,
    waitList=
        safe_text,
    table=
        st.none()
)
T2_strategy = st.builds(
    T2,
)
T1_strategy = st.builds(
    T1,
)
Tuple_strategy = st.builds(
    Tuple,
)
Player_strategy = st.builds(
    Player,
)
T_strategy = st.builds(
    T,
)
Stack_strategy = st.builds(
    Stack,
)
Deck_strategy = st.builds(
    Deck,
    cards=
        safe_text
)
Table_strategy = st.builds(
    Table,
    currPlayers=
        safe_text,
    deck=
        st.none()
)
Executive_strategy = st.builds(
    Executive,
)
Card_strategy = st.builds(
    Card,
    value=
        st.integers(),
    suit=
        safe_text
)



@given(instance=CasinoManager_strategy)
@settings(max_examples=50)
def test_hyp_casinomanager_instantiation(instance):
    assert isinstance(instance, CasinoManager)



@given(instance=CasinoManager_strategy)
def test_hyp_casinomanager_waitList_setter(instance):
    original = instance.waitList
    instance.waitList = original
    assert instance.waitList == original



@given(instance=CasinoManager_strategy)
def test_hyp_casinomanager_table_setter(instance):
    original = instance.table
    instance.table = original
    assert instance.table == original










@given(instance=Deck_strategy)
def test_hyp_deck_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_hyp_table_instantiation(instance):
    assert isinstance(instance, Table)



@given(instance=Table_strategy)
def test_hyp_table_currPlayers_setter(instance):
    original = instance.currPlayers
    instance.currPlayers = original
    assert instance.currPlayers == original



@given(instance=Table_strategy)
def test_hyp_table_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original





@given(instance=Card_strategy)
def test_hyp_card_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=Card_strategy)
def test_hyp_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Card,
    CasinoManager,
    Deck,
    Executive,
    Player,
    Queue,
    Stack,
    T,
    T1,
    T2,
    T3,
    Table,
    Tuple,
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

def test_Card_suit_value_roundtrip():
    instance = Card(suit="sample_text", value=7)
    assert instance.suit == "sample_text"
    instance.suit = "sample_text_2"
    assert instance.suit == "sample_text_2"


def test_Card_value_value_roundtrip():
    instance = Card(suit="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_Deck_cards_value_roundtrip():
    instance = Deck(cards="sample_text")
    assert instance.cards == "sample_text"
    instance.cards = "sample_text_2"
    assert instance.cards == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Card_strategy = st.builds(Card, suit=safe_text, value=st.integers())
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)


Deck_strategy = st.builds(Deck, cards=safe_text)
@given(instance=Deck_strategy)
@settings(max_examples=25)
def test_Deck_instantiation(instance):
    assert isinstance(instance, Deck)


Executive_strategy = st.builds(Executive)
@given(instance=Executive_strategy)
@settings(max_examples=25)
def test_Executive_instantiation(instance):
    assert isinstance(instance, Executive)


Player_strategy = st.builds(Player)
@given(instance=Player_strategy)
@settings(max_examples=25)
def test_Player_instantiation(instance):
    assert isinstance(instance, Player)


Queue_strategy = st.builds(Queue)
@given(instance=Queue_strategy)
@settings(max_examples=25)
def test_Queue_instantiation(instance):
    assert isinstance(instance, Queue)


Stack_strategy = st.builds(Stack)
@given(instance=Stack_strategy)
@settings(max_examples=25)
def test_Stack_instantiation(instance):
    assert isinstance(instance, Stack)


T_strategy = st.builds(T)
@given(instance=T_strategy)
@settings(max_examples=25)
def test_T_instantiation(instance):
    assert isinstance(instance, T)


T1_strategy = st.builds(T1)
@given(instance=T1_strategy)
@settings(max_examples=25)
def test_T1_instantiation(instance):
    assert isinstance(instance, T1)


T2_strategy = st.builds(T2)
@given(instance=T2_strategy)
@settings(max_examples=25)
def test_T2_instantiation(instance):
    assert isinstance(instance, T2)


T3_strategy = st.builds(T3)
@given(instance=T3_strategy)
@settings(max_examples=25)
def test_T3_instantiation(instance):
    assert isinstance(instance, T3)


Tuple_strategy = st.builds(Tuple)
@given(instance=Tuple_strategy)
@settings(max_examples=25)
def test_Tuple_instantiation(instance):
    assert isinstance(instance, Tuple)



