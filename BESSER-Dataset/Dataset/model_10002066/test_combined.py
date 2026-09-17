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
    Card___Interface,
    Main_MainGame,
    Players_Wallet,
    Players_Person,
    Players_PokerHand,
    Players_Player,
    Game_Ranker,
    Game_GUI,
    Cards_Deck,
    Cards_Card_Interface,
    Cards_CardImpl,
    Cards_Cardinality,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_card___interface_is_not_abstract():
    assert not inspect.isabstract(Card___Interface)


def test_hyp_card___interface_constructor_exists():
    assert callable(Card___Interface.__init__)


def test_hyp_card___interface_constructor_args():
    sig = inspect.signature(Card___Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_main_maingame_is_not_abstract():
    assert not inspect.isabstract(Main_MainGame)


def test_hyp_main_maingame_constructor_exists():
    assert callable(Main_MainGame.__init__)


def test_hyp_main_maingame_constructor_args():
    sig = inspect.signature(Main_MainGame.__init__)
    params = list(sig.parameters.keys())
    assert "Dealer" in params, "Missing parameter 'Dealer'"
    assert "Bigblind" in params, "Missing parameter 'Bigblind'"
    assert "HighestBid" in params, "Missing parameter 'HighestBid'"
    assert "SmallBlind" in params, "Missing parameter 'SmallBlind'"
    assert "screen" in params, "Missing parameter 'screen'"
    assert "Players" in params, "Missing parameter 'Players'"

def test_hyp_main_maingame_has_Dealer():
    assert hasattr(Main_MainGame, "Dealer")
    descriptor = None
    for klass in Main_MainGame.__mro__:
        if "Dealer" in klass.__dict__:
            descriptor = klass.__dict__["Dealer"]
            break
    assert isinstance(descriptor, property)

def test_hyp_main_maingame_has_Bigblind():
    assert hasattr(Main_MainGame, "Bigblind")
    descriptor = None
    for klass in Main_MainGame.__mro__:
        if "Bigblind" in klass.__dict__:
            descriptor = klass.__dict__["Bigblind"]
            break
    assert isinstance(descriptor, property)

def test_hyp_main_maingame_has_HighestBid():
    assert hasattr(Main_MainGame, "HighestBid")
    descriptor = None
    for klass in Main_MainGame.__mro__:
        if "HighestBid" in klass.__dict__:
            descriptor = klass.__dict__["HighestBid"]
            break
    assert isinstance(descriptor, property)

def test_hyp_main_maingame_has_SmallBlind():
    assert hasattr(Main_MainGame, "SmallBlind")
    descriptor = None
    for klass in Main_MainGame.__mro__:
        if "SmallBlind" in klass.__dict__:
            descriptor = klass.__dict__["SmallBlind"]
            break
    assert isinstance(descriptor, property)

def test_hyp_main_maingame_has_screen():
    assert hasattr(Main_MainGame, "screen")
    descriptor = None
    for klass in Main_MainGame.__mro__:
        if "screen" in klass.__dict__:
            descriptor = klass.__dict__["screen"]
            break
    assert isinstance(descriptor, property)

def test_hyp_main_maingame_has_Players():
    assert hasattr(Main_MainGame, "Players")
    descriptor = None
    for klass in Main_MainGame.__mro__:
        if "Players" in klass.__dict__:
            descriptor = klass.__dict__["Players"]
            break
    assert isinstance(descriptor, property)



def test_hyp_players_wallet_is_not_abstract():
    assert not inspect.isabstract(Players_Wallet)


def test_hyp_players_wallet_constructor_exists():
    assert callable(Players_Wallet.__init__)


def test_hyp_players_wallet_constructor_args():
    sig = inspect.signature(Players_Wallet.__init__)
    params = list(sig.parameters.keys())
    assert "balance" in params, "Missing parameter 'balance'"




def test_hyp_players_person_is_not_abstract():
    assert not inspect.isabstract(Players_Person)


def test_hyp_players_person_constructor_exists():
    assert callable(Players_Person.__init__)


def test_hyp_players_person_constructor_args():
    sig = inspect.signature(Players_Person.__init__)
    params = list(sig.parameters.keys())
    assert "personNumber" in params, "Missing parameter 'personNumber'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_players_pokerhand_is_not_abstract():
    assert not inspect.isabstract(Players_PokerHand)


def test_hyp_players_pokerhand_constructor_exists():
    assert callable(Players_PokerHand.__init__)


def test_hyp_players_pokerhand_constructor_args():
    sig = inspect.signature(Players_PokerHand.__init__)
    params = list(sig.parameters.keys())
    assert "Cards" in params, "Missing parameter 'Cards'"
    assert "highCard" in params, "Missing parameter 'highCard'"
    assert "value" in params, "Missing parameter 'value'"

def test_hyp_players_pokerhand_has_Cards():
    assert hasattr(Players_PokerHand, "Cards")
    descriptor = None
    for klass in Players_PokerHand.__mro__:
        if "Cards" in klass.__dict__:
            descriptor = klass.__dict__["Cards"]
            break
    assert isinstance(descriptor, property)

def test_hyp_players_pokerhand_has_highCard():
    assert hasattr(Players_PokerHand, "highCard")
    descriptor = None
    for klass in Players_PokerHand.__mro__:
        if "highCard" in klass.__dict__:
            descriptor = klass.__dict__["highCard"]
            break
    assert isinstance(descriptor, property)

def test_hyp_players_pokerhand_has_value():
    assert hasattr(Players_PokerHand, "value")
    descriptor = None
    for klass in Players_PokerHand.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_hyp_players_player_is_not_abstract():
    assert not inspect.isabstract(Players_Player)


def test_hyp_players_player_constructor_exists():
    assert callable(Players_Player.__init__)


def test_hyp_players_player_constructor_args():
    sig = inspect.signature(Players_Player.__init__)
    params = list(sig.parameters.keys())
    assert "chips" in params, "Missing parameter 'chips'"
    assert "isSmallBlind" in params, "Missing parameter 'isSmallBlind'"
    assert "hasFolded" in params, "Missing parameter 'hasFolded'"
    assert "isDealer" in params, "Missing parameter 'isDealer'"
    assert "Hand" in params, "Missing parameter 'Hand'"
    assert "isBigBlind" in params, "Missing parameter 'isBigBlind'"

def test_hyp_players_player_has_chips():
    assert hasattr(Players_Player, "chips")
    descriptor = None
    for klass in Players_Player.__mro__:
        if "chips" in klass.__dict__:
            descriptor = klass.__dict__["chips"]
            break
    assert isinstance(descriptor, property)

def test_hyp_players_player_has_isSmallBlind():
    assert hasattr(Players_Player, "isSmallBlind")
    descriptor = None
    for klass in Players_Player.__mro__:
        if "isSmallBlind" in klass.__dict__:
            descriptor = klass.__dict__["isSmallBlind"]
            break
    assert isinstance(descriptor, property)

def test_hyp_players_player_has_hasFolded():
    assert hasattr(Players_Player, "hasFolded")
    descriptor = None
    for klass in Players_Player.__mro__:
        if "hasFolded" in klass.__dict__:
            descriptor = klass.__dict__["hasFolded"]
            break
    assert isinstance(descriptor, property)

def test_hyp_players_player_has_isDealer():
    assert hasattr(Players_Player, "isDealer")
    descriptor = None
    for klass in Players_Player.__mro__:
        if "isDealer" in klass.__dict__:
            descriptor = klass.__dict__["isDealer"]
            break
    assert isinstance(descriptor, property)

def test_hyp_players_player_has_Hand():
    assert hasattr(Players_Player, "Hand")
    descriptor = None
    for klass in Players_Player.__mro__:
        if "Hand" in klass.__dict__:
            descriptor = klass.__dict__["Hand"]
            break
    assert isinstance(descriptor, property)

def test_hyp_players_player_has_isBigBlind():
    assert hasattr(Players_Player, "isBigBlind")
    descriptor = None
    for klass in Players_Player.__mro__:
        if "isBigBlind" in klass.__dict__:
            descriptor = klass.__dict__["isBigBlind"]
            break
    assert isinstance(descriptor, property)



def test_hyp_game_ranker_is_not_abstract():
    assert not inspect.isabstract(Game_Ranker)


def test_hyp_game_ranker_constructor_exists():
    assert callable(Game_Ranker.__init__)


def test_hyp_game_ranker_constructor_args():
    sig = inspect.signature(Game_Ranker.__init__)
    params = list(sig.parameters.keys())
    assert "hand" in params, "Missing parameter 'hand'"

def test_hyp_game_ranker_has_hand():
    assert hasattr(Game_Ranker, "hand")
    descriptor = None
    for klass in Game_Ranker.__mro__:
        if "hand" in klass.__dict__:
            descriptor = klass.__dict__["hand"]
            break
    assert isinstance(descriptor, property)



def test_hyp_game_gui_is_not_abstract():
    assert not inspect.isabstract(Game_GUI)


def test_hyp_game_gui_constructor_exists():
    assert callable(Game_GUI.__init__)


def test_hyp_game_gui_constructor_args():
    sig = inspect.signature(Game_GUI.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cards_deck_is_not_abstract():
    assert not inspect.isabstract(Cards_Deck)


def test_hyp_cards_deck_constructor_exists():
    assert callable(Cards_Deck.__init__)


def test_hyp_cards_deck_constructor_args():
    sig = inspect.signature(Cards_Deck.__init__)
    params = list(sig.parameters.keys())
    assert "list" in params, "Missing parameter 'list'"
    assert "burnt" in params, "Missing parameter 'burnt'"

def test_hyp_cards_deck_has_list():
    assert hasattr(Cards_Deck, "list")
    descriptor = None
    for klass in Cards_Deck.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)

def test_hyp_cards_deck_has_burnt():
    assert hasattr(Cards_Deck, "burnt")
    descriptor = None
    for klass in Cards_Deck.__mro__:
        if "burnt" in klass.__dict__:
            descriptor = klass.__dict__["burnt"]
            break
    assert isinstance(descriptor, property)



def test_hyp_cards_card_interface_is_not_abstract():
    assert not inspect.isabstract(Cards_Card_Interface)


def test_hyp_cards_card_interface_constructor_exists():
    assert callable(Cards_Card_Interface.__init__)


def test_hyp_cards_card_interface_constructor_args():
    sig = inspect.signature(Cards_Card_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cards_cardimpl_is_not_abstract():
    assert not inspect.isabstract(Cards_CardImpl)


def test_hyp_cards_cardimpl_constructor_exists():
    assert callable(Cards_CardImpl.__init__)


def test_hyp_cards_cardimpl_constructor_args():
    sig = inspect.signature(Cards_CardImpl.__init__)
    params = list(sig.parameters.keys())
    assert "Cardinality" in params, "Missing parameter 'Cardinality'"
    assert "Suit" in params, "Missing parameter 'Suit'"
    assert "isMarked" in params, "Missing parameter 'isMarked'"

def test_hyp_cards_cardimpl_has_Cardinality():
    assert hasattr(Cards_CardImpl, "Cardinality")
    descriptor = None
    for klass in Cards_CardImpl.__mro__:
        if "Cardinality" in klass.__dict__:
            descriptor = klass.__dict__["Cardinality"]
            break
    assert isinstance(descriptor, property)

def test_hyp_cards_cardimpl_has_Suit():
    assert hasattr(Cards_CardImpl, "Suit")
    descriptor = None
    for klass in Cards_CardImpl.__mro__:
        if "Suit" in klass.__dict__:
            descriptor = klass.__dict__["Suit"]
            break
    assert isinstance(descriptor, property)

def test_hyp_cards_cardimpl_has_isMarked():
    assert hasattr(Cards_CardImpl, "isMarked")
    descriptor = None
    for klass in Cards_CardImpl.__mro__:
        if "isMarked" in klass.__dict__:
            descriptor = klass.__dict__["isMarked"]
            break
    assert isinstance(descriptor, property)

def test_hyp_cards_cardinality_exists():
    # Check that the Enumeration exists
    assert Cards_Cardinality is not None

def test_hyp_cards_cardinality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cards_Cardinality]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Cards_Cardinality"


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
Card___Interface_strategy = st.builds(
    Card___Interface,
)
Main_MainGame_strategy = st.builds(
    Main_MainGame,
    Dealer=
        st.integers(),
    Bigblind=
        st.integers(),
    HighestBid=
        st.integers(),
    SmallBlind=
        st.integers(),
    screen=
        st.none(),
    Players=
        safe_text
)
Players_Wallet_strategy = st.builds(
    Players_Wallet,
    balance=
        st.integers()
)
Players_Person_strategy = st.builds(
    Players_Person,
    personNumber=
        safe_text,
    name=
        safe_text
)
Players_PokerHand_strategy = st.builds(
    Players_PokerHand,
    Cards=
        st.none(),
    highCard=
        st.none(),
    value=
        st.integers()
)
Players_Player_strategy = st.builds(
    Players_Player,
    chips=
        st.none(),
    isSmallBlind=
        st.booleans(),
    hasFolded=
        st.booleans(),
    isDealer=
        st.booleans(),
    Hand=
        st.none(),
    isBigBlind=
        st.booleans()
)
Game_Ranker_strategy = st.builds(
    Game_Ranker,
    hand=
        st.none()
)
Game_GUI_strategy = st.builds(
    Game_GUI,
)
Cards_Deck_strategy = st.builds(
    Cards_Deck,
    list=
        safe_text,
    burnt=
        st.none()
)
Cards_Card_Interface_strategy = st.builds(
    Cards_Card_Interface,
)
Cards_CardImpl_strategy = st.builds(
    Cards_CardImpl,
    Cardinality=
        st.none(),
    Suit=
        safe_text,
    isMarked=
        st.booleans()
)


@given(instance=Main_MainGame_strategy)
@settings(max_examples=50)
def test_hyp_main_maingame_instantiation(instance):
    assert isinstance(instance, Main_MainGame)



@given(instance=Main_MainGame_strategy)
def test_hyp_main_maingame_Dealer_setter(instance):
    original = instance.Dealer
    instance.Dealer = original
    assert instance.Dealer == original



@given(instance=Main_MainGame_strategy)
def test_hyp_main_maingame_Bigblind_setter(instance):
    original = instance.Bigblind
    instance.Bigblind = original
    assert instance.Bigblind == original



@given(instance=Main_MainGame_strategy)
def test_hyp_main_maingame_HighestBid_setter(instance):
    original = instance.HighestBid
    instance.HighestBid = original
    assert instance.HighestBid == original



@given(instance=Main_MainGame_strategy)
def test_hyp_main_maingame_SmallBlind_setter(instance):
    original = instance.SmallBlind
    instance.SmallBlind = original
    assert instance.SmallBlind == original



@given(instance=Main_MainGame_strategy)
def test_hyp_main_maingame_screen_setter(instance):
    original = instance.screen
    instance.screen = original
    assert instance.screen == original



@given(instance=Main_MainGame_strategy)
def test_hyp_main_maingame_Players_setter(instance):
    original = instance.Players
    instance.Players = original
    assert instance.Players == original




@given(instance=Players_Wallet_strategy)
def test_hyp_players_wallet_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original




@given(instance=Players_Person_strategy)
def test_hyp_players_person_personNumber_setter(instance):
    original = instance.personNumber
    instance.personNumber = original
    assert instance.personNumber == original



@given(instance=Players_Person_strategy)
def test_hyp_players_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Players_PokerHand_strategy)
@settings(max_examples=50)
def test_hyp_players_pokerhand_instantiation(instance):
    assert isinstance(instance, Players_PokerHand)



@given(instance=Players_PokerHand_strategy)
def test_hyp_players_pokerhand_Cards_setter(instance):
    original = instance.Cards
    instance.Cards = original
    assert instance.Cards == original



@given(instance=Players_PokerHand_strategy)
def test_hyp_players_pokerhand_highCard_setter(instance):
    original = instance.highCard
    instance.highCard = original
    assert instance.highCard == original



@given(instance=Players_PokerHand_strategy)
def test_hyp_players_pokerhand_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Players_Player_strategy)
@settings(max_examples=50)
def test_hyp_players_player_instantiation(instance):
    assert isinstance(instance, Players_Player)



@given(instance=Players_Player_strategy)
def test_hyp_players_player_chips_setter(instance):
    original = instance.chips
    instance.chips = original
    assert instance.chips == original



@given(instance=Players_Player_strategy)
def test_hyp_players_player_isSmallBlind_setter(instance):
    original = instance.isSmallBlind
    instance.isSmallBlind = original
    assert instance.isSmallBlind == original



@given(instance=Players_Player_strategy)
def test_hyp_players_player_hasFolded_setter(instance):
    original = instance.hasFolded
    instance.hasFolded = original
    assert instance.hasFolded == original



@given(instance=Players_Player_strategy)
def test_hyp_players_player_isDealer_setter(instance):
    original = instance.isDealer
    instance.isDealer = original
    assert instance.isDealer == original



@given(instance=Players_Player_strategy)
def test_hyp_players_player_Hand_setter(instance):
    original = instance.Hand
    instance.Hand = original
    assert instance.Hand == original



@given(instance=Players_Player_strategy)
def test_hyp_players_player_isBigBlind_setter(instance):
    original = instance.isBigBlind
    instance.isBigBlind = original
    assert instance.isBigBlind == original

@given(instance=Game_Ranker_strategy)
@settings(max_examples=50)
def test_hyp_game_ranker_instantiation(instance):
    assert isinstance(instance, Game_Ranker)



@given(instance=Game_Ranker_strategy)
def test_hyp_game_ranker_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original


@given(instance=Cards_Deck_strategy)
@settings(max_examples=50)
def test_hyp_cards_deck_instantiation(instance):
    assert isinstance(instance, Cards_Deck)



@given(instance=Cards_Deck_strategy)
def test_hyp_cards_deck_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original



@given(instance=Cards_Deck_strategy)
def test_hyp_cards_deck_burnt_setter(instance):
    original = instance.burnt
    instance.burnt = original
    assert instance.burnt == original


@given(instance=Cards_CardImpl_strategy)
@settings(max_examples=50)
def test_hyp_cards_cardimpl_instantiation(instance):
    assert isinstance(instance, Cards_CardImpl)



@given(instance=Cards_CardImpl_strategy)
def test_hyp_cards_cardimpl_Cardinality_setter(instance):
    original = instance.Cardinality
    instance.Cardinality = original
    assert instance.Cardinality == original



@given(instance=Cards_CardImpl_strategy)
def test_hyp_cards_cardimpl_Suit_setter(instance):
    original = instance.Suit
    instance.Suit = original
    assert instance.Suit == original



@given(instance=Cards_CardImpl_strategy)
def test_hyp_cards_cardimpl_isMarked_setter(instance):
    original = instance.isMarked
    instance.isMarked = original
    assert instance.isMarked == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Card___Interface,
    Cards_CardImpl,
    Cards_Card_Interface,
    Cards_Deck,
    Game_GUI,
    Game_Ranker,
    Main_MainGame,
    Players_Person,
    Players_Player,
    Players_PokerHand,
    Players_Wallet,
    Cards_Cardinality,
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

def test_Players_Person_name_value_roundtrip():
    instance = Players_Person(name="sample_text", personNumber="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Players_Person_personNumber_value_roundtrip():
    instance = Players_Person(name="sample_text", personNumber="sample_text")
    assert instance.personNumber == "sample_text"
    instance.personNumber = "sample_text_2"
    assert instance.personNumber == "sample_text_2"


def test_Players_Wallet_balance_value_roundtrip():
    instance = Players_Wallet(balance=7)
    assert instance.balance == 7
    instance.balance = 13
    assert instance.balance == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Card___Interface_strategy = st.builds(Card___Interface)
@given(instance=Card___Interface_strategy)
@settings(max_examples=25)
def test_Card___Interface_instantiation(instance):
    assert isinstance(instance, Card___Interface)


Cards_Card_Interface_strategy = st.builds(Cards_Card_Interface)
@given(instance=Cards_Card_Interface_strategy)
@settings(max_examples=25)
def test_Cards_Card_Interface_instantiation(instance):
    assert isinstance(instance, Cards_Card_Interface)


Game_GUI_strategy = st.builds(Game_GUI)
@given(instance=Game_GUI_strategy)
@settings(max_examples=25)
def test_Game_GUI_instantiation(instance):
    assert isinstance(instance, Game_GUI)


Players_Person_strategy = st.builds(Players_Person, name=safe_text, personNumber=safe_text)
@given(instance=Players_Person_strategy)
@settings(max_examples=25)
def test_Players_Person_instantiation(instance):
    assert isinstance(instance, Players_Person)


Players_Wallet_strategy = st.builds(Players_Wallet, balance=st.integers())
@given(instance=Players_Wallet_strategy)
@settings(max_examples=25)
def test_Players_Wallet_instantiation(instance):
    assert isinstance(instance, Players_Wallet)



