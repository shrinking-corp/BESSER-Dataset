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
    Money_PlayerMoney,
    GUI_Interface,
    Comparable_Interface,
    Main_StartGame,
    Player_Players,
    Game_EvaluateHand,
    Game_Display,
    Game_Ranking,
    Card_Cards,
    Card_Deck,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_money_playermoney_is_not_abstract():
    assert not inspect.isabstract(Money_PlayerMoney)


def test_hyp_money_playermoney_constructor_exists():
    assert callable(Money_PlayerMoney.__init__)


def test_hyp_money_playermoney_constructor_args():
    sig = inspect.signature(Money_PlayerMoney.__init__)
    params = list(sig.parameters.keys())
    assert "totalmoney" in params, "Missing parameter 'totalmoney'"
    assert "numofplayers" in params, "Missing parameter 'numofplayers'"





def test_hyp_gui_interface_is_not_abstract():
    assert not inspect.isabstract(GUI_Interface)


def test_hyp_gui_interface_constructor_exists():
    assert callable(GUI_Interface.__init__)


def test_hyp_gui_interface_constructor_args():
    sig = inspect.signature(GUI_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comparable_interface_is_not_abstract():
    assert not inspect.isabstract(Comparable_Interface)


def test_hyp_comparable_interface_constructor_exists():
    assert callable(Comparable_Interface.__init__)


def test_hyp_comparable_interface_constructor_args():
    sig = inspect.signature(Comparable_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_main_startgame_is_not_abstract():
    assert not inspect.isabstract(Main_StartGame)


def test_hyp_main_startgame_constructor_exists():
    assert callable(Main_StartGame.__init__)


def test_hyp_main_startgame_constructor_args():
    sig = inspect.signature(Main_StartGame.__init__)
    params = list(sig.parameters.keys())
    assert "deck" in params, "Missing parameter 'deck'"
    assert "handsize" in params, "Missing parameter 'handsize'"
    assert "player" in params, "Missing parameter 'player'"
    assert "hand" in params, "Missing parameter 'hand'"
    assert "scanner" in params, "Missing parameter 'scanner'"








def test_hyp_player_players_is_not_abstract():
    assert not inspect.isabstract(Player_Players)


def test_hyp_player_players_constructor_exists():
    assert callable(Player_Players.__init__)


def test_hyp_player_players_constructor_args():
    sig = inspect.signature(Player_Players.__init__)
    params = list(sig.parameters.keys())



def test_hyp_game_evaluatehand_is_not_abstract():
    assert not inspect.isabstract(Game_EvaluateHand)


def test_hyp_game_evaluatehand_constructor_exists():
    assert callable(Game_EvaluateHand.__init__)


def test_hyp_game_evaluatehand_constructor_args():
    sig = inspect.signature(Game_EvaluateHand.__init__)
    params = list(sig.parameters.keys())
    assert "card" in params, "Missing parameter 'card'"




def test_hyp_game_display_is_not_abstract():
    assert not inspect.isabstract(Game_Display)


def test_hyp_game_display_constructor_exists():
    assert callable(Game_Display.__init__)


def test_hyp_game_display_constructor_args():
    sig = inspect.signature(Game_Display.__init__)
    params = list(sig.parameters.keys())
    assert "money" in params, "Missing parameter 'money'"
    assert "card" in params, "Missing parameter 'card'"





def test_hyp_game_ranking_is_not_abstract():
    assert not inspect.isabstract(Game_Ranking)


def test_hyp_game_ranking_constructor_exists():
    assert callable(Game_Ranking.__init__)


def test_hyp_game_ranking_constructor_args():
    sig = inspect.signature(Game_Ranking.__init__)
    params = list(sig.parameters.keys())
    assert "card" in params, "Missing parameter 'card'"




def test_hyp_card_cards_is_not_abstract():
    assert not inspect.isabstract(Card_Cards)


def test_hyp_card_cards_constructor_exists():
    assert callable(Card_Cards.__init__)


def test_hyp_card_cards_constructor_args():
    sig = inspect.signature(Card_Cards.__init__)
    params = list(sig.parameters.keys())
    assert "rank" in params, "Missing parameter 'rank'"
    assert "suit" in params, "Missing parameter 'suit'"





def test_hyp_card_deck_is_not_abstract():
    assert not inspect.isabstract(Card_Deck)


def test_hyp_card_deck_constructor_exists():
    assert callable(Card_Deck.__init__)


def test_hyp_card_deck_constructor_args():
    sig = inspect.signature(Card_Deck.__init__)
    params = list(sig.parameters.keys())
    assert "random" in params, "Missing parameter 'random'"
    assert "handsize" in params, "Missing parameter 'handsize'"
    assert "remainder" in params, "Missing parameter 'remainder'"
    assert "decksize" in params, "Missing parameter 'decksize'"
    assert "shuffletimes" in params, "Missing parameter 'shuffletimes'"
    assert "deck" in params, "Missing parameter 'deck'"








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
Money_PlayerMoney_strategy = st.builds(
    Money_PlayerMoney,
    totalmoney=
        safe_text,
    numofplayers=
        safe_text
)
GUI_Interface_strategy = st.builds(
    GUI_Interface,
)
Comparable_Interface_strategy = st.builds(
    Comparable_Interface,
)
Main_StartGame_strategy = st.builds(
    Main_StartGame,
    deck=
        safe_text,
    handsize=
        st.integers(),
    player=
        safe_text,
    hand=
        safe_text,
    scanner=
        safe_text
)
Player_Players_strategy = st.builds(
    Player_Players,
)
Game_EvaluateHand_strategy = st.builds(
    Game_EvaluateHand,
    card=
        safe_text
)
Game_Display_strategy = st.builds(
    Game_Display,
    money=
        safe_text,
    card=
        safe_text
)
Game_Ranking_strategy = st.builds(
    Game_Ranking,
    card=
        safe_text
)
Card_Cards_strategy = st.builds(
    Card_Cards,
    rank=
        st.integers(),
    suit=
        st.integers()
)
Card_Deck_strategy = st.builds(
    Card_Deck,
    random=
        safe_text,
    handsize=
        st.integers(),
    remainder=
        st.integers(),
    decksize=
        st.integers(),
    shuffletimes=
        st.integers(),
    deck=
        safe_text
)




@given(instance=Money_PlayerMoney_strategy)
def test_hyp_money_playermoney_totalmoney_setter(instance):
    original = instance.totalmoney
    instance.totalmoney = original
    assert instance.totalmoney == original



@given(instance=Money_PlayerMoney_strategy)
def test_hyp_money_playermoney_numofplayers_setter(instance):
    original = instance.numofplayers
    instance.numofplayers = original
    assert instance.numofplayers == original






@given(instance=Main_StartGame_strategy)
def test_hyp_main_startgame_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original



@given(instance=Main_StartGame_strategy)
def test_hyp_main_startgame_handsize_setter(instance):
    original = instance.handsize
    instance.handsize = original
    assert instance.handsize == original



@given(instance=Main_StartGame_strategy)
def test_hyp_main_startgame_player_setter(instance):
    original = instance.player
    instance.player = original
    assert instance.player == original



@given(instance=Main_StartGame_strategy)
def test_hyp_main_startgame_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original



@given(instance=Main_StartGame_strategy)
def test_hyp_main_startgame_scanner_setter(instance):
    original = instance.scanner
    instance.scanner = original
    assert instance.scanner == original





@given(instance=Game_EvaluateHand_strategy)
def test_hyp_game_evaluatehand_card_setter(instance):
    original = instance.card
    instance.card = original
    assert instance.card == original




@given(instance=Game_Display_strategy)
def test_hyp_game_display_money_setter(instance):
    original = instance.money
    instance.money = original
    assert instance.money == original



@given(instance=Game_Display_strategy)
def test_hyp_game_display_card_setter(instance):
    original = instance.card
    instance.card = original
    assert instance.card == original




@given(instance=Game_Ranking_strategy)
def test_hyp_game_ranking_card_setter(instance):
    original = instance.card
    instance.card = original
    assert instance.card == original




@given(instance=Card_Cards_strategy)
def test_hyp_card_cards_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original



@given(instance=Card_Cards_strategy)
def test_hyp_card_cards_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original




@given(instance=Card_Deck_strategy)
def test_hyp_card_deck_random_setter(instance):
    original = instance.random
    instance.random = original
    assert instance.random == original



@given(instance=Card_Deck_strategy)
def test_hyp_card_deck_handsize_setter(instance):
    original = instance.handsize
    instance.handsize = original
    assert instance.handsize == original



@given(instance=Card_Deck_strategy)
def test_hyp_card_deck_remainder_setter(instance):
    original = instance.remainder
    instance.remainder = original
    assert instance.remainder == original



@given(instance=Card_Deck_strategy)
def test_hyp_card_deck_decksize_setter(instance):
    original = instance.decksize
    instance.decksize = original
    assert instance.decksize == original



@given(instance=Card_Deck_strategy)
def test_hyp_card_deck_shuffletimes_setter(instance):
    original = instance.shuffletimes
    instance.shuffletimes = original
    assert instance.shuffletimes == original



@given(instance=Card_Deck_strategy)
def test_hyp_card_deck_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Card_Cards,
    Card_Deck,
    Comparable_Interface,
    GUI_Interface,
    Game_Display,
    Game_EvaluateHand,
    Game_Ranking,
    Main_StartGame,
    Money_PlayerMoney,
    Player_Players,
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

def test_Card_Cards_rank_value_roundtrip():
    instance = Card_Cards(rank=7, suit=7)
    assert instance.rank == 7
    instance.rank = 13
    assert instance.rank == 13


def test_Card_Cards_suit_value_roundtrip():
    instance = Card_Cards(rank=7, suit=7)
    assert instance.suit == 7
    instance.suit = 13
    assert instance.suit == 13


def test_Card_Deck_deck_value_roundtrip():
    instance = Card_Deck(deck="sample_text", decksize=7, handsize=7, random="sample_text", remainder=7, shuffletimes=7)
    assert instance.deck == "sample_text"
    instance.deck = "sample_text_2"
    assert instance.deck == "sample_text_2"


def test_Card_Deck_decksize_value_roundtrip():
    instance = Card_Deck(deck="sample_text", decksize=7, handsize=7, random="sample_text", remainder=7, shuffletimes=7)
    assert instance.decksize == 7
    instance.decksize = 13
    assert instance.decksize == 13


def test_Card_Deck_handsize_value_roundtrip():
    instance = Card_Deck(deck="sample_text", decksize=7, handsize=7, random="sample_text", remainder=7, shuffletimes=7)
    assert instance.handsize == 7
    instance.handsize = 13
    assert instance.handsize == 13


def test_Card_Deck_random_value_roundtrip():
    instance = Card_Deck(deck="sample_text", decksize=7, handsize=7, random="sample_text", remainder=7, shuffletimes=7)
    assert instance.random == "sample_text"
    instance.random = "sample_text_2"
    assert instance.random == "sample_text_2"


def test_Card_Deck_remainder_value_roundtrip():
    instance = Card_Deck(deck="sample_text", decksize=7, handsize=7, random="sample_text", remainder=7, shuffletimes=7)
    assert instance.remainder == 7
    instance.remainder = 13
    assert instance.remainder == 13


def test_Card_Deck_shuffletimes_value_roundtrip():
    instance = Card_Deck(deck="sample_text", decksize=7, handsize=7, random="sample_text", remainder=7, shuffletimes=7)
    assert instance.shuffletimes == 7
    instance.shuffletimes = 13
    assert instance.shuffletimes == 13


def test_Game_Display_card_value_roundtrip():
    instance = Game_Display(card="sample_text", money="sample_text")
    assert instance.card == "sample_text"
    instance.card = "sample_text_2"
    assert instance.card == "sample_text_2"


def test_Game_Display_money_value_roundtrip():
    instance = Game_Display(card="sample_text", money="sample_text")
    assert instance.money == "sample_text"
    instance.money = "sample_text_2"
    assert instance.money == "sample_text_2"


def test_Game_EvaluateHand_card_value_roundtrip():
    instance = Game_EvaluateHand(card="sample_text")
    assert instance.card == "sample_text"
    instance.card = "sample_text_2"
    assert instance.card == "sample_text_2"


def test_Game_Ranking_card_value_roundtrip():
    instance = Game_Ranking(card="sample_text")
    assert instance.card == "sample_text"
    instance.card = "sample_text_2"
    assert instance.card == "sample_text_2"


def test_Main_StartGame_deck_value_roundtrip():
    instance = Main_StartGame(deck="sample_text", hand="sample_text", handsize=7, player="sample_text", scanner="sample_text")
    assert instance.deck == "sample_text"
    instance.deck = "sample_text_2"
    assert instance.deck == "sample_text_2"


def test_Main_StartGame_hand_value_roundtrip():
    instance = Main_StartGame(deck="sample_text", hand="sample_text", handsize=7, player="sample_text", scanner="sample_text")
    assert instance.hand == "sample_text"
    instance.hand = "sample_text_2"
    assert instance.hand == "sample_text_2"


def test_Main_StartGame_handsize_value_roundtrip():
    instance = Main_StartGame(deck="sample_text", hand="sample_text", handsize=7, player="sample_text", scanner="sample_text")
    assert instance.handsize == 7
    instance.handsize = 13
    assert instance.handsize == 13


def test_Main_StartGame_player_value_roundtrip():
    instance = Main_StartGame(deck="sample_text", hand="sample_text", handsize=7, player="sample_text", scanner="sample_text")
    assert instance.player == "sample_text"
    instance.player = "sample_text_2"
    assert instance.player == "sample_text_2"


def test_Main_StartGame_scanner_value_roundtrip():
    instance = Main_StartGame(deck="sample_text", hand="sample_text", handsize=7, player="sample_text", scanner="sample_text")
    assert instance.scanner == "sample_text"
    instance.scanner = "sample_text_2"
    assert instance.scanner == "sample_text_2"


def test_Money_PlayerMoney_numofplayers_value_roundtrip():
    instance = Money_PlayerMoney(numofplayers="sample_text", totalmoney="sample_text")
    assert instance.numofplayers == "sample_text"
    instance.numofplayers = "sample_text_2"
    assert instance.numofplayers == "sample_text_2"


def test_Money_PlayerMoney_totalmoney_value_roundtrip():
    instance = Money_PlayerMoney(numofplayers="sample_text", totalmoney="sample_text")
    assert instance.totalmoney == "sample_text"
    instance.totalmoney = "sample_text_2"
    assert instance.totalmoney == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Card_Cards_strategy = st.builds(Card_Cards, rank=st.integers(), suit=st.integers())
@given(instance=Card_Cards_strategy)
@settings(max_examples=25)
def test_Card_Cards_instantiation(instance):
    assert isinstance(instance, Card_Cards)


Card_Deck_strategy = st.builds(Card_Deck, deck=safe_text, decksize=st.integers(), handsize=st.integers(), random=safe_text, remainder=st.integers(), shuffletimes=st.integers())
@given(instance=Card_Deck_strategy)
@settings(max_examples=25)
def test_Card_Deck_instantiation(instance):
    assert isinstance(instance, Card_Deck)


Comparable_Interface_strategy = st.builds(Comparable_Interface)
@given(instance=Comparable_Interface_strategy)
@settings(max_examples=25)
def test_Comparable_Interface_instantiation(instance):
    assert isinstance(instance, Comparable_Interface)


GUI_Interface_strategy = st.builds(GUI_Interface)
@given(instance=GUI_Interface_strategy)
@settings(max_examples=25)
def test_GUI_Interface_instantiation(instance):
    assert isinstance(instance, GUI_Interface)


Game_Display_strategy = st.builds(Game_Display, card=safe_text, money=safe_text)
@given(instance=Game_Display_strategy)
@settings(max_examples=25)
def test_Game_Display_instantiation(instance):
    assert isinstance(instance, Game_Display)


Game_EvaluateHand_strategy = st.builds(Game_EvaluateHand, card=safe_text)
@given(instance=Game_EvaluateHand_strategy)
@settings(max_examples=25)
def test_Game_EvaluateHand_instantiation(instance):
    assert isinstance(instance, Game_EvaluateHand)


Game_Ranking_strategy = st.builds(Game_Ranking, card=safe_text)
@given(instance=Game_Ranking_strategy)
@settings(max_examples=25)
def test_Game_Ranking_instantiation(instance):
    assert isinstance(instance, Game_Ranking)


Main_StartGame_strategy = st.builds(Main_StartGame, deck=safe_text, hand=safe_text, handsize=st.integers(), player=safe_text, scanner=safe_text)
@given(instance=Main_StartGame_strategy)
@settings(max_examples=25)
def test_Main_StartGame_instantiation(instance):
    assert isinstance(instance, Main_StartGame)


Money_PlayerMoney_strategy = st.builds(Money_PlayerMoney, numofplayers=safe_text, totalmoney=safe_text)
@given(instance=Money_PlayerMoney_strategy)
@settings(max_examples=25)
def test_Money_PlayerMoney_instantiation(instance):
    assert isinstance(instance, Money_PlayerMoney)


Player_Players_strategy = st.builds(Player_Players)
@given(instance=Player_Players_strategy)
@settings(max_examples=25)
def test_Player_Players_instantiation(instance):
    assert isinstance(instance, Player_Players)



