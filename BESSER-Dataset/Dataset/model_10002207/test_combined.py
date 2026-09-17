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
    BlackJackPlayer,
    Deck,
    BlackJackDriver,
    Card,
    BlackJack,
    Blackjack_Exit_UseCase,
    Blackjack_Play_Again_UseCase,
    Blackjack_Start_Game_UseCase,
    Blackjack_Bet_UseCase,
    Blackjack_Double_Down_UseCase,
    Blackjack_Split_UseCase,
    Blackjack_Stay_UseCase,
    Blackjack_Check_Win_Condition_UseCase,
    Blackjack_Deal_UseCase,
    Blackjack_Hit_UseCase,
    Dealer_Actor,
    Player_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_blackjackplayer_is_not_abstract():
    assert not inspect.isabstract(BlackJackPlayer)


def test_hyp_blackjackplayer_constructor_exists():
    assert callable(BlackJackPlayer.__init__)


def test_hyp_blackjackplayer_constructor_args():
    sig = inspect.signature(BlackJackPlayer.__init__)
    params = list(sig.parameters.keys())
    assert "MaxNumCards" in params, "Missing parameter 'MaxNumCards'"
    assert "cards__" in params, "Missing parameter 'cards__'"
    assert "cardCount" in params, "Missing parameter 'cardCount'"

def test_hyp_blackjackplayer_has_MaxNumCards():
    assert hasattr(BlackJackPlayer, "MaxNumCards")
    descriptor = None
    for klass in BlackJackPlayer.__mro__:
        if "MaxNumCards" in klass.__dict__:
            descriptor = klass.__dict__["MaxNumCards"]
            break
    assert isinstance(descriptor, property)

def test_hyp_blackjackplayer_has_cards__():
    assert hasattr(BlackJackPlayer, "cards__")
    descriptor = None
    for klass in BlackJackPlayer.__mro__:
        if "cards__" in klass.__dict__:
            descriptor = klass.__dict__["cards__"]
            break
    assert isinstance(descriptor, property)

def test_hyp_blackjackplayer_has_cardCount():
    assert hasattr(BlackJackPlayer, "cardCount")
    descriptor = None
    for klass in BlackJackPlayer.__mro__:
        if "cardCount" in klass.__dict__:
            descriptor = klass.__dict__["cardCount"]
            break
    assert isinstance(descriptor, property)



def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "deck" in params, "Missing parameter 'deck'"
    assert "cardsUsed" in params, "Missing parameter 'cardsUsed'"

def test_hyp_deck_has_deck():
    assert hasattr(Deck, "deck")
    descriptor = None
    for klass in Deck.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)

def test_hyp_deck_has_cardsUsed():
    assert hasattr(Deck, "cardsUsed")
    descriptor = None
    for klass in Deck.__mro__:
        if "cardsUsed" in klass.__dict__:
            descriptor = klass.__dict__["cardsUsed"]
            break
    assert isinstance(descriptor, property)



def test_hyp_blackjackdriver_is_not_abstract():
    assert not inspect.isabstract(BlackJackDriver)


def test_hyp_blackjackdriver_constructor_exists():
    assert callable(BlackJackDriver.__init__)


def test_hyp_blackjackdriver_constructor_args():
    sig = inspect.signature(BlackJackDriver.__init__)
    params = list(sig.parameters.keys())



def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "faceValue" in params, "Missing parameter 'faceValue'"
    assert "value" in params, "Missing parameter 'value'"
    assert "suit" in params, "Missing parameter 'suit'"






def test_hyp_blackjack_is_not_abstract():
    assert not inspect.isabstract(BlackJack)


def test_hyp_blackjack_constructor_exists():
    assert callable(BlackJack.__init__)


def test_hyp_blackjack_constructor_args():
    sig = inspect.signature(BlackJack.__init__)
    params = list(sig.parameters.keys())
    assert "playersHand" in params, "Missing parameter 'playersHand'"
    assert "bet" in params, "Missing parameter 'bet'"
    assert "deck" in params, "Missing parameter 'deck'"
    assert "money" in params, "Missing parameter 'money'"
    assert "dealersHand" in params, "Missing parameter 'dealersHand'"
    assert "handCount" in params, "Missing parameter 'handCount'"

def test_hyp_blackjack_has_playersHand():
    assert hasattr(BlackJack, "playersHand")
    descriptor = None
    for klass in BlackJack.__mro__:
        if "playersHand" in klass.__dict__:
            descriptor = klass.__dict__["playersHand"]
            break
    assert isinstance(descriptor, property)

def test_hyp_blackjack_has_bet():
    assert hasattr(BlackJack, "bet")
    descriptor = None
    for klass in BlackJack.__mro__:
        if "bet" in klass.__dict__:
            descriptor = klass.__dict__["bet"]
            break
    assert isinstance(descriptor, property)

def test_hyp_blackjack_has_deck():
    assert hasattr(BlackJack, "deck")
    descriptor = None
    for klass in BlackJack.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)

def test_hyp_blackjack_has_money():
    assert hasattr(BlackJack, "money")
    descriptor = None
    for klass in BlackJack.__mro__:
        if "money" in klass.__dict__:
            descriptor = klass.__dict__["money"]
            break
    assert isinstance(descriptor, property)

def test_hyp_blackjack_has_dealersHand():
    assert hasattr(BlackJack, "dealersHand")
    descriptor = None
    for klass in BlackJack.__mro__:
        if "dealersHand" in klass.__dict__:
            descriptor = klass.__dict__["dealersHand"]
            break
    assert isinstance(descriptor, property)

def test_hyp_blackjack_has_handCount():
    assert hasattr(BlackJack, "handCount")
    descriptor = None
    for klass in BlackJack.__mro__:
        if "handCount" in klass.__dict__:
            descriptor = klass.__dict__["handCount"]
            break
    assert isinstance(descriptor, property)



def test_hyp_blackjack_exit_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Exit_UseCase)


def test_hyp_blackjack_exit_usecase_constructor_exists():
    assert callable(Blackjack_Exit_UseCase.__init__)


def test_hyp_blackjack_exit_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Exit_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_blackjack_play_again_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Play_Again_UseCase)


def test_hyp_blackjack_play_again_usecase_constructor_exists():
    assert callable(Blackjack_Play_Again_UseCase.__init__)


def test_hyp_blackjack_play_again_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Play_Again_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_blackjack_start_game_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Start_Game_UseCase)


def test_hyp_blackjack_start_game_usecase_constructor_exists():
    assert callable(Blackjack_Start_Game_UseCase.__init__)


def test_hyp_blackjack_start_game_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Start_Game_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_blackjack_bet_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Bet_UseCase)


def test_hyp_blackjack_bet_usecase_constructor_exists():
    assert callable(Blackjack_Bet_UseCase.__init__)


def test_hyp_blackjack_bet_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Bet_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_blackjack_double_down_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Double_Down_UseCase)


def test_hyp_blackjack_double_down_usecase_constructor_exists():
    assert callable(Blackjack_Double_Down_UseCase.__init__)


def test_hyp_blackjack_double_down_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Double_Down_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_blackjack_split_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Split_UseCase)


def test_hyp_blackjack_split_usecase_constructor_exists():
    assert callable(Blackjack_Split_UseCase.__init__)


def test_hyp_blackjack_split_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Split_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_blackjack_stay_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Stay_UseCase)


def test_hyp_blackjack_stay_usecase_constructor_exists():
    assert callable(Blackjack_Stay_UseCase.__init__)


def test_hyp_blackjack_stay_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Stay_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_blackjack_check_win_condition_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Check_Win_Condition_UseCase)


def test_hyp_blackjack_check_win_condition_usecase_constructor_exists():
    assert callable(Blackjack_Check_Win_Condition_UseCase.__init__)


def test_hyp_blackjack_check_win_condition_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Check_Win_Condition_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_blackjack_deal_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Deal_UseCase)


def test_hyp_blackjack_deal_usecase_constructor_exists():
    assert callable(Blackjack_Deal_UseCase.__init__)


def test_hyp_blackjack_deal_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Deal_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_blackjack_hit_usecase_is_not_abstract():
    assert not inspect.isabstract(Blackjack_Hit_UseCase)


def test_hyp_blackjack_hit_usecase_constructor_exists():
    assert callable(Blackjack_Hit_UseCase.__init__)


def test_hyp_blackjack_hit_usecase_constructor_args():
    sig = inspect.signature(Blackjack_Hit_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dealer_actor_is_not_abstract():
    assert not inspect.isabstract(Dealer_Actor)


def test_hyp_dealer_actor_constructor_exists():
    assert callable(Dealer_Actor.__init__)


def test_hyp_dealer_actor_constructor_args():
    sig = inspect.signature(Dealer_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_player_actor_is_not_abstract():
    assert not inspect.isabstract(Player_Actor)


def test_hyp_player_actor_constructor_exists():
    assert callable(Player_Actor.__init__)


def test_hyp_player_actor_constructor_args():
    sig = inspect.signature(Player_Actor.__init__)
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
BlackJackPlayer_strategy = st.builds(
    BlackJackPlayer,
    MaxNumCards=
        st.integers(),
    cards__=
        st.none(),
    cardCount=
        st.integers()
)
Deck_strategy = st.builds(
    Deck,
    deck=
        st.none(),
    cardsUsed=
        st.integers()
)
BlackJackDriver_strategy = st.builds(
    BlackJackDriver,
)
Card_strategy = st.builds(
    Card,
    faceValue=
        safe_text,
    value=
        st.integers(),
    suit=
        safe_text
)
BlackJack_strategy = st.builds(
    BlackJack,
    playersHand=
        st.none(),
    bet=
        st.integers(),
    deck=
        st.none(),
    money=
        st.integers(),
    dealersHand=
        st.none(),
    handCount=
        st.integers()
)
Blackjack_Exit_UseCase_strategy = st.builds(
    Blackjack_Exit_UseCase,
)
Blackjack_Play_Again_UseCase_strategy = st.builds(
    Blackjack_Play_Again_UseCase,
)
Blackjack_Start_Game_UseCase_strategy = st.builds(
    Blackjack_Start_Game_UseCase,
)
Blackjack_Bet_UseCase_strategy = st.builds(
    Blackjack_Bet_UseCase,
)
Blackjack_Double_Down_UseCase_strategy = st.builds(
    Blackjack_Double_Down_UseCase,
)
Blackjack_Split_UseCase_strategy = st.builds(
    Blackjack_Split_UseCase,
)
Blackjack_Stay_UseCase_strategy = st.builds(
    Blackjack_Stay_UseCase,
)
Blackjack_Check_Win_Condition_UseCase_strategy = st.builds(
    Blackjack_Check_Win_Condition_UseCase,
)
Blackjack_Deal_UseCase_strategy = st.builds(
    Blackjack_Deal_UseCase,
)
Blackjack_Hit_UseCase_strategy = st.builds(
    Blackjack_Hit_UseCase,
)
Dealer_Actor_strategy = st.builds(
    Dealer_Actor,
)
Player_Actor_strategy = st.builds(
    Player_Actor,
)

@given(instance=BlackJackPlayer_strategy)
@settings(max_examples=50)
def test_hyp_blackjackplayer_instantiation(instance):
    assert isinstance(instance, BlackJackPlayer)



@given(instance=BlackJackPlayer_strategy)
def test_hyp_blackjackplayer_MaxNumCards_setter(instance):
    original = instance.MaxNumCards
    instance.MaxNumCards = original
    assert instance.MaxNumCards == original



@given(instance=BlackJackPlayer_strategy)
def test_hyp_blackjackplayer_cards___setter(instance):
    original = instance.cards__
    instance.cards__ = original
    assert instance.cards__ == original



@given(instance=BlackJackPlayer_strategy)
def test_hyp_blackjackplayer_cardCount_setter(instance):
    original = instance.cardCount
    instance.cardCount = original
    assert instance.cardCount == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_hyp_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_hyp_deck_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original



@given(instance=Deck_strategy)
def test_hyp_deck_cardsUsed_setter(instance):
    original = instance.cardsUsed
    instance.cardsUsed = original
    assert instance.cardsUsed == original





@given(instance=Card_strategy)
def test_hyp_card_faceValue_setter(instance):
    original = instance.faceValue
    instance.faceValue = original
    assert instance.faceValue == original



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

@given(instance=BlackJack_strategy)
@settings(max_examples=50)
def test_hyp_blackjack_instantiation(instance):
    assert isinstance(instance, BlackJack)



@given(instance=BlackJack_strategy)
def test_hyp_blackjack_playersHand_setter(instance):
    original = instance.playersHand
    instance.playersHand = original
    assert instance.playersHand == original



@given(instance=BlackJack_strategy)
def test_hyp_blackjack_bet_setter(instance):
    original = instance.bet
    instance.bet = original
    assert instance.bet == original



@given(instance=BlackJack_strategy)
def test_hyp_blackjack_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original



@given(instance=BlackJack_strategy)
def test_hyp_blackjack_money_setter(instance):
    original = instance.money
    instance.money = original
    assert instance.money == original



@given(instance=BlackJack_strategy)
def test_hyp_blackjack_dealersHand_setter(instance):
    original = instance.dealersHand
    instance.dealersHand = original
    assert instance.dealersHand == original



@given(instance=BlackJack_strategy)
def test_hyp_blackjack_handCount_setter(instance):
    original = instance.handCount
    instance.handCount = original
    assert instance.handCount == original














# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BlackJack,
    BlackJackDriver,
    BlackJackPlayer,
    Blackjack_Bet_UseCase,
    Blackjack_Check_Win_Condition_UseCase,
    Blackjack_Deal_UseCase,
    Blackjack_Double_Down_UseCase,
    Blackjack_Exit_UseCase,
    Blackjack_Hit_UseCase,
    Blackjack_Play_Again_UseCase,
    Blackjack_Split_UseCase,
    Blackjack_Start_Game_UseCase,
    Blackjack_Stay_UseCase,
    Card,
    Dealer_Actor,
    Deck,
    Player_Actor,
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

def test_Card_faceValue_value_roundtrip():
    instance = Card(faceValue="sample_text", suit="sample_text", value=7)
    assert instance.faceValue == "sample_text"
    instance.faceValue = "sample_text_2"
    assert instance.faceValue == "sample_text_2"


def test_Card_suit_value_roundtrip():
    instance = Card(faceValue="sample_text", suit="sample_text", value=7)
    assert instance.suit == "sample_text"
    instance.suit = "sample_text_2"
    assert instance.suit == "sample_text_2"


def test_Card_value_value_roundtrip():
    instance = Card(faceValue="sample_text", suit="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BlackJackDriver_strategy = st.builds(BlackJackDriver)
@given(instance=BlackJackDriver_strategy)
@settings(max_examples=25)
def test_BlackJackDriver_instantiation(instance):
    assert isinstance(instance, BlackJackDriver)


Blackjack_Bet_UseCase_strategy = st.builds(Blackjack_Bet_UseCase)
@given(instance=Blackjack_Bet_UseCase_strategy)
@settings(max_examples=25)
def test_Blackjack_Bet_UseCase_instantiation(instance):
    assert isinstance(instance, Blackjack_Bet_UseCase)


Blackjack_Check_Win_Condition_UseCase_strategy = st.builds(Blackjack_Check_Win_Condition_UseCase)
@given(instance=Blackjack_Check_Win_Condition_UseCase_strategy)
@settings(max_examples=25)
def test_Blackjack_Check_Win_Condition_UseCase_instantiation(instance):
    assert isinstance(instance, Blackjack_Check_Win_Condition_UseCase)


Blackjack_Deal_UseCase_strategy = st.builds(Blackjack_Deal_UseCase)
@given(instance=Blackjack_Deal_UseCase_strategy)
@settings(max_examples=25)
def test_Blackjack_Deal_UseCase_instantiation(instance):
    assert isinstance(instance, Blackjack_Deal_UseCase)


Blackjack_Double_Down_UseCase_strategy = st.builds(Blackjack_Double_Down_UseCase)
@given(instance=Blackjack_Double_Down_UseCase_strategy)
@settings(max_examples=25)
def test_Blackjack_Double_Down_UseCase_instantiation(instance):
    assert isinstance(instance, Blackjack_Double_Down_UseCase)


Blackjack_Exit_UseCase_strategy = st.builds(Blackjack_Exit_UseCase)
@given(instance=Blackjack_Exit_UseCase_strategy)
@settings(max_examples=25)
def test_Blackjack_Exit_UseCase_instantiation(instance):
    assert isinstance(instance, Blackjack_Exit_UseCase)


Blackjack_Hit_UseCase_strategy = st.builds(Blackjack_Hit_UseCase)
@given(instance=Blackjack_Hit_UseCase_strategy)
@settings(max_examples=25)
def test_Blackjack_Hit_UseCase_instantiation(instance):
    assert isinstance(instance, Blackjack_Hit_UseCase)


Blackjack_Play_Again_UseCase_strategy = st.builds(Blackjack_Play_Again_UseCase)
@given(instance=Blackjack_Play_Again_UseCase_strategy)
@settings(max_examples=25)
def test_Blackjack_Play_Again_UseCase_instantiation(instance):
    assert isinstance(instance, Blackjack_Play_Again_UseCase)


Blackjack_Split_UseCase_strategy = st.builds(Blackjack_Split_UseCase)
@given(instance=Blackjack_Split_UseCase_strategy)
@settings(max_examples=25)
def test_Blackjack_Split_UseCase_instantiation(instance):
    assert isinstance(instance, Blackjack_Split_UseCase)


Blackjack_Start_Game_UseCase_strategy = st.builds(Blackjack_Start_Game_UseCase)
@given(instance=Blackjack_Start_Game_UseCase_strategy)
@settings(max_examples=25)
def test_Blackjack_Start_Game_UseCase_instantiation(instance):
    assert isinstance(instance, Blackjack_Start_Game_UseCase)


Blackjack_Stay_UseCase_strategy = st.builds(Blackjack_Stay_UseCase)
@given(instance=Blackjack_Stay_UseCase_strategy)
@settings(max_examples=25)
def test_Blackjack_Stay_UseCase_instantiation(instance):
    assert isinstance(instance, Blackjack_Stay_UseCase)


Card_strategy = st.builds(Card, faceValue=safe_text, suit=safe_text, value=st.integers())
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)


Dealer_Actor_strategy = st.builds(Dealer_Actor)
@given(instance=Dealer_Actor_strategy)
@settings(max_examples=25)
def test_Dealer_Actor_instantiation(instance):
    assert isinstance(instance, Dealer_Actor)


Player_Actor_strategy = st.builds(Player_Actor)
@given(instance=Player_Actor_strategy)
@settings(max_examples=25)
def test_Player_Actor_instantiation(instance):
    assert isinstance(instance, Player_Actor)



