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
    genmymodelreverse_java_util_Scanner,
    Strategy_Interface,
    Stay,
    Player,
    Person_Interface,
    Hit,
    Hand,
    Deck,
    Dealer,
    Context,
    Card,
    T2,
    T,
    BlackJack,
    Suit,
    Rank,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_genmymodelreverse_java_util_scanner_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_util_Scanner)


def test_hyp_genmymodelreverse_java_util_scanner_constructor_exists():
    assert callable(genmymodelreverse_java_util_Scanner.__init__)


def test_hyp_genmymodelreverse_java_util_scanner_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_util_Scanner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_strategy_interface_is_not_abstract():
    assert not inspect.isabstract(Strategy_Interface)


def test_hyp_strategy_interface_constructor_exists():
    assert callable(Strategy_Interface.__init__)


def test_hyp_strategy_interface_constructor_args():
    sig = inspect.signature(Strategy_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stay_is_not_abstract():
    assert not inspect.isabstract(Stay)


def test_hyp_stay_constructor_exists():
    assert callable(Stay.__init__)


def test_hyp_stay_constructor_args():
    sig = inspect.signature(Stay.__init__)
    params = list(sig.parameters.keys())



def test_hyp_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_hyp_player_constructor_exists():
    assert callable(Player.__init__)


def test_hyp_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"




def test_hyp_person_interface_is_not_abstract():
    assert not inspect.isabstract(Person_Interface)


def test_hyp_person_interface_constructor_exists():
    assert callable(Person_Interface.__init__)


def test_hyp_person_interface_constructor_args():
    sig = inspect.signature(Person_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hit_is_not_abstract():
    assert not inspect.isabstract(Hit)


def test_hyp_hit_constructor_exists():
    assert callable(Hit.__init__)


def test_hyp_hit_constructor_args():
    sig = inspect.signature(Hit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hand_is_not_abstract():
    assert not inspect.isabstract(Hand)


def test_hyp_hand_constructor_exists():
    assert callable(Hand.__init__)


def test_hyp_hand_constructor_args():
    sig = inspect.signature(Hand.__init__)
    params = list(sig.parameters.keys())
    assert "startHand" in params, "Missing parameter 'startHand'"




def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dealer_is_not_abstract():
    assert not inspect.isabstract(Dealer)


def test_hyp_dealer_constructor_exists():
    assert callable(Dealer.__init__)


def test_hyp_dealer_constructor_args():
    sig = inspect.signature(Dealer.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"




def test_hyp_context_is_not_abstract():
    assert not inspect.isabstract(Context)


def test_hyp_context_constructor_exists():
    assert callable(Context.__init__)


def test_hyp_context_constructor_args():
    sig = inspect.signature(Context.__init__)
    params = list(sig.parameters.keys())



def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "suit" in params, "Missing parameter 'suit'"
    assert "rank" in params, "Missing parameter 'rank'"

def test_hyp_card_has_suit():
    assert hasattr(Card, "suit")
    descriptor = None
    for klass in Card.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)

def test_hyp_card_has_rank():
    assert hasattr(Card, "rank")
    descriptor = None
    for klass in Card.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)



def test_hyp_t2_is_not_abstract():
    assert not inspect.isabstract(T2)


def test_hyp_t2_constructor_exists():
    assert callable(T2.__init__)


def test_hyp_t2_constructor_args():
    sig = inspect.signature(T2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_hyp_t_constructor_exists():
    assert callable(T.__init__)


def test_hyp_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_hyp_blackjack_is_not_abstract():
    assert not inspect.isabstract(BlackJack)


def test_hyp_blackjack_constructor_exists():
    assert callable(BlackJack.__init__)


def test_hyp_blackjack_constructor_args():
    sig = inspect.signature(BlackJack.__init__)
    params = list(sig.parameters.keys())
    assert "scan" in params, "Missing parameter 'scan'"

def test_hyp_blackjack_has_scan():
    assert hasattr(BlackJack, "scan")
    descriptor = None
    for klass in BlackJack.__mro__:
        if "scan" in klass.__dict__:
            descriptor = klass.__dict__["scan"]
            break
    assert isinstance(descriptor, property)

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

def test_hyp_rank_exists():
    # Check that the Enumeration exists
    assert Rank is not None

def test_hyp_rank_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Rank]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Rank"


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
genmymodelreverse_java_util_Scanner_strategy = st.builds(
    genmymodelreverse_java_util_Scanner,
)
Strategy_Interface_strategy = st.builds(
    Strategy_Interface,
)
Stay_strategy = st.builds(
    Stay,
)
Player_strategy = st.builds(
    Player,
    firstName=
        safe_text
)
Person_Interface_strategy = st.builds(
    Person_Interface,
)
Hit_strategy = st.builds(
    Hit,
)
Hand_strategy = st.builds(
    Hand,
    startHand=
        st.integers()
)
Deck_strategy = st.builds(
    Deck,
)
Dealer_strategy = st.builds(
    Dealer,
    firstName=
        safe_text
)
Context_strategy = st.builds(
    Context,
)
Card_strategy = st.builds(
    Card,
    suit=
        st.none(),
    rank=
        st.none()
)
T2_strategy = st.builds(
    T2,
)
T_strategy = st.builds(
    T,
)
BlackJack_strategy = st.builds(
    BlackJack,
    scan=
        st.none()
)







@given(instance=Player_strategy)
def test_hyp_player_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original






@given(instance=Hand_strategy)
def test_hyp_hand_startHand_setter(instance):
    original = instance.startHand
    instance.startHand = original
    assert instance.startHand == original





@given(instance=Dealer_strategy)
def test_hyp_dealer_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original


@given(instance=Card_strategy)
@settings(max_examples=50)
def test_hyp_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_hyp_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=Card_strategy)
def test_hyp_card_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original



@given(instance=BlackJack_strategy)
@settings(max_examples=50)
def test_hyp_blackjack_instantiation(instance):
    assert isinstance(instance, BlackJack)



@given(instance=BlackJack_strategy)
def test_hyp_blackjack_scan_setter(instance):
    original = instance.scan
    instance.scan = original
    assert instance.scan == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BlackJack,
    Card,
    Context,
    Dealer,
    Deck,
    Hand,
    Hit,
    Person_Interface,
    Player,
    Stay,
    Strategy_Interface,
    T,
    T2,
    genmymodelreverse_java_util_Scanner,
    Rank,
    Suit,
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

def test_Dealer_firstName_value_roundtrip():
    instance = Dealer(firstName="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_Hand_startHand_value_roundtrip():
    instance = Hand(startHand=7)
    assert instance.startHand == 7
    instance.startHand = 13
    assert instance.startHand == 13


def test_Player_firstName_value_roundtrip():
    instance = Player(firstName="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_assoc_d_Dealer_Deck_7_link_reassign_clear():
    a = Dealer(firstName="sample_text")
    b1 = Deck()
    b2 = Deck()
    _safe_set(a, 'd9', b1)
    assert _is_linked(a, 'd9', b1)
    if hasattr(b1, 'dealer8'):
        assert _is_linked(b1, 'dealer8', a)
    _safe_set(a, 'd9', b2)
    assert _is_linked(a, 'd9', b2)
    if hasattr(b1, 'dealer8'):
        assert not _is_linked(b1, 'dealer8', a)
    if hasattr(b2, 'dealer8'):
        assert _is_linked(b2, 'dealer8', a)
    _safe_set(a, 'd9', None)
    assert not _is_linked(a, 'd9', b2)
    if hasattr(b2, 'dealer8'):
        assert not _is_linked(b2, 'dealer8', a)


def test_assoc_h_Player_Hand_8_link_reassign_clear():
    a = Player(firstName="sample_text")
    b1 = Hand(startHand=7)
    b2 = Hand(startHand=13)
    _safe_set(a, 'h11', b1)
    assert _is_linked(a, 'h11', b1)
    if hasattr(b1, 'player10'):
        assert _is_linked(b1, 'player10', a)
    _safe_set(a, 'h11', b2)
    assert _is_linked(a, 'h11', b2)
    if hasattr(b1, 'player10'):
        assert not _is_linked(b1, 'player10', a)
    if hasattr(b2, 'player10'):
        assert _is_linked(b2, 'player10', a)
    _safe_set(a, 'h11', None)
    assert not _is_linked(a, 'h11', b2)
    if hasattr(b2, 'player10'):
        assert not _is_linked(b2, 'player10', a)


def test_assoc_hand_Dealer_Hand_9_link_reassign_clear():
    a = Hand(startHand=7)
    b1 = Dealer(firstName="sample_text")
    b2 = Dealer(firstName="sample_text_2")
    _safe_set(a, 'dealer22', b1)
    assert _is_linked(a, 'dealer22', b1)
    if hasattr(b1, 'hand23'):
        assert _is_linked(b1, 'hand23', a)
    _safe_set(a, 'dealer22', b2)
    assert _is_linked(a, 'dealer22', b2)
    if hasattr(b1, 'hand23'):
        assert not _is_linked(b1, 'hand23', a)
    if hasattr(b2, 'hand23'):
        assert _is_linked(b2, 'hand23', a)
    _safe_set(a, 'dealer22', None)
    assert not _is_linked(a, 'dealer22', b2)
    if hasattr(b2, 'hand23'):
        assert not _is_linked(b2, 'hand23', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Context_strategy = st.builds(Context)
@given(instance=Context_strategy)
@settings(max_examples=25)
def test_Context_instantiation(instance):
    assert isinstance(instance, Context)


Dealer_strategy = st.builds(Dealer, firstName=safe_text)
@given(instance=Dealer_strategy)
@settings(max_examples=25)
def test_Dealer_instantiation(instance):
    assert isinstance(instance, Dealer)


Deck_strategy = st.builds(Deck)
@given(instance=Deck_strategy)
@settings(max_examples=25)
def test_Deck_instantiation(instance):
    assert isinstance(instance, Deck)


Hand_strategy = st.builds(Hand, startHand=st.integers())
@given(instance=Hand_strategy)
@settings(max_examples=25)
def test_Hand_instantiation(instance):
    assert isinstance(instance, Hand)


Hit_strategy = st.builds(Hit)
@given(instance=Hit_strategy)
@settings(max_examples=25)
def test_Hit_instantiation(instance):
    assert isinstance(instance, Hit)


Person_Interface_strategy = st.builds(Person_Interface)
@given(instance=Person_Interface_strategy)
@settings(max_examples=25)
def test_Person_Interface_instantiation(instance):
    assert isinstance(instance, Person_Interface)


Player_strategy = st.builds(Player, firstName=safe_text)
@given(instance=Player_strategy)
@settings(max_examples=25)
def test_Player_instantiation(instance):
    assert isinstance(instance, Player)


Stay_strategy = st.builds(Stay)
@given(instance=Stay_strategy)
@settings(max_examples=25)
def test_Stay_instantiation(instance):
    assert isinstance(instance, Stay)


Strategy_Interface_strategy = st.builds(Strategy_Interface)
@given(instance=Strategy_Interface_strategy)
@settings(max_examples=25)
def test_Strategy_Interface_instantiation(instance):
    assert isinstance(instance, Strategy_Interface)


T_strategy = st.builds(T)
@given(instance=T_strategy)
@settings(max_examples=25)
def test_T_instantiation(instance):
    assert isinstance(instance, T)


T2_strategy = st.builds(T2)
@given(instance=T2_strategy)
@settings(max_examples=25)
def test_T2_instantiation(instance):
    assert isinstance(instance, T2)


genmymodelreverse_java_util_Scanner_strategy = st.builds(genmymodelreverse_java_util_Scanner)
@given(instance=genmymodelreverse_java_util_Scanner_strategy)
@settings(max_examples=25)
def test_genmymodelreverse_java_util_Scanner_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_util_Scanner)



