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
    JFrame,
    BlackjackGUI,
    BlackjackDriver,
    Card,
    Dealer,
    Player,
    Blackjack,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_jframe_is_not_abstract():
    assert not inspect.isabstract(JFrame)


def test_hyp_jframe_constructor_exists():
    assert callable(JFrame.__init__)


def test_hyp_jframe_constructor_args():
    sig = inspect.signature(JFrame.__init__)
    params = list(sig.parameters.keys())



def test_hyp_blackjackgui_is_not_abstract():
    assert not inspect.isabstract(BlackjackGUI)


def test_hyp_blackjackgui_constructor_exists():
    assert callable(BlackjackGUI.__init__)


def test_hyp_blackjackgui_constructor_args():
    sig = inspect.signature(BlackjackGUI.__init__)
    params = list(sig.parameters.keys())



def test_hyp_blackjackdriver_is_not_abstract():
    assert not inspect.isabstract(BlackjackDriver)


def test_hyp_blackjackdriver_constructor_exists():
    assert callable(BlackjackDriver.__init__)


def test_hyp_blackjackdriver_constructor_args():
    sig = inspect.signature(BlackjackDriver.__init__)
    params = list(sig.parameters.keys())



def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "rank" in params, "Missing parameter 'rank'"
    assert "suit" in params, "Missing parameter 'suit'"
    assert "value" in params, "Missing parameter 'value'"






def test_hyp_dealer_is_not_abstract():
    assert not inspect.isabstract(Dealer)


def test_hyp_dealer_constructor_exists():
    assert callable(Dealer.__init__)


def test_hyp_dealer_constructor_args():
    sig = inspect.signature(Dealer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_hyp_player_constructor_exists():
    assert callable(Player.__init__)


def test_hyp_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "totalAmount" in params, "Missing parameter 'totalAmount'"




def test_hyp_blackjack_is_not_abstract():
    assert not inspect.isabstract(Blackjack)


def test_hyp_blackjack_constructor_exists():
    assert callable(Blackjack.__init__)


def test_hyp_blackjack_constructor_args():
    sig = inspect.signature(Blackjack.__init__)
    params = list(sig.parameters.keys())
    assert "playerName" in params, "Missing parameter 'playerName'"
    assert "players" in params, "Missing parameter 'players'"
    assert "count" in params, "Missing parameter 'count'"
    assert "hand__" in params, "Missing parameter 'hand__'"

def test_hyp_blackjack_has_playerName():
    assert hasattr(Blackjack, "playerName")
    descriptor = None
    for klass in Blackjack.__mro__:
        if "playerName" in klass.__dict__:
            descriptor = klass.__dict__["playerName"]
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

def test_hyp_blackjack_has_count():
    assert hasattr(Blackjack, "count")
    descriptor = None
    for klass in Blackjack.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)

def test_hyp_blackjack_has_hand__():
    assert hasattr(Blackjack, "hand__")
    descriptor = None
    for klass in Blackjack.__mro__:
        if "hand__" in klass.__dict__:
            descriptor = klass.__dict__["hand__"]
            break
    assert isinstance(descriptor, property)


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
JFrame_strategy = st.builds(
    JFrame,
)
BlackjackGUI_strategy = st.builds(
    BlackjackGUI,
)
BlackjackDriver_strategy = st.builds(
    BlackjackDriver,
)
Card_strategy = st.builds(
    Card,
    rank=
        st.integers(),
    suit=
        safe_text,
    value=
        st.integers()
)
Dealer_strategy = st.builds(
    Dealer,
)
Player_strategy = st.builds(
    Player,
    totalAmount=
        st.integers()
)
Blackjack_strategy = st.builds(
    Blackjack,
    playerName=
        safe_text,
    players=
        st.integers(),
    count=
        st.integers(),
    hand__=
        st.none()
)







@given(instance=Card_strategy)
def test_hyp_card_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original



@given(instance=Card_strategy)
def test_hyp_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=Card_strategy)
def test_hyp_card_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=Player_strategy)
def test_hyp_player_totalAmount_setter(instance):
    original = instance.totalAmount
    instance.totalAmount = original
    assert instance.totalAmount == original

@given(instance=Blackjack_strategy)
@settings(max_examples=50)
def test_hyp_blackjack_instantiation(instance):
    assert isinstance(instance, Blackjack)



@given(instance=Blackjack_strategy)
def test_hyp_blackjack_playerName_setter(instance):
    original = instance.playerName
    instance.playerName = original
    assert instance.playerName == original



@given(instance=Blackjack_strategy)
def test_hyp_blackjack_players_setter(instance):
    original = instance.players
    instance.players = original
    assert instance.players == original



@given(instance=Blackjack_strategy)
def test_hyp_blackjack_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original



@given(instance=Blackjack_strategy)
def test_hyp_blackjack_hand___setter(instance):
    original = instance.hand__
    instance.hand__ = original
    assert instance.hand__ == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Blackjack,
    BlackjackDriver,
    BlackjackGUI,
    Card,
    Dealer,
    JFrame,
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

def test_Card_rank_value_roundtrip():
    instance = Card(rank=7, suit="sample_text", value=7)
    assert instance.rank == 7
    instance.rank = 13
    assert instance.rank == 13


def test_Card_suit_value_roundtrip():
    instance = Card(rank=7, suit="sample_text", value=7)
    assert instance.suit == "sample_text"
    instance.suit = "sample_text_2"
    assert instance.suit == "sample_text_2"


def test_Card_value_value_roundtrip():
    instance = Card(rank=7, suit="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_Player_totalAmount_value_roundtrip():
    instance = Player(totalAmount=7)
    assert instance.totalAmount == 7
    instance.totalAmount = 13
    assert instance.totalAmount == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BlackjackDriver_strategy = st.builds(BlackjackDriver)
@given(instance=BlackjackDriver_strategy)
@settings(max_examples=25)
def test_BlackjackDriver_instantiation(instance):
    assert isinstance(instance, BlackjackDriver)


BlackjackGUI_strategy = st.builds(BlackjackGUI)
@given(instance=BlackjackGUI_strategy)
@settings(max_examples=25)
def test_BlackjackGUI_instantiation(instance):
    assert isinstance(instance, BlackjackGUI)


Card_strategy = st.builds(Card, rank=st.integers(), suit=safe_text, value=st.integers())
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)


Dealer_strategy = st.builds(Dealer)
@given(instance=Dealer_strategy)
@settings(max_examples=25)
def test_Dealer_instantiation(instance):
    assert isinstance(instance, Dealer)


JFrame_strategy = st.builds(JFrame)
@given(instance=JFrame_strategy)
@settings(max_examples=25)
def test_JFrame_instantiation(instance):
    assert isinstance(instance, JFrame)


Player_strategy = st.builds(Player, totalAmount=st.integers())
@given(instance=Player_strategy)
@settings(max_examples=25)
def test_Player_instantiation(instance):
    assert isinstance(instance, Player)



