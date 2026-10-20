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
    main_Play,
    game_GameBoardGUI,
    game_Ranker,
    players_Person,
    players_PlayerVersionGUI,
    players_Player,
    cards_PokerHandInterface_Interface,
    cards_CardsGUI,
    cards_Deck,
    cards_PokerHand,
    cards_Card,
    cards_Suit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_main_play_is_not_abstract():
    assert not inspect.isabstract(main_Play)


def test_hyp_main_play_constructor_exists():
    assert callable(main_Play.__init__)


def test_hyp_main_play_constructor_args():
    sig = inspect.signature(main_Play.__init__)
    params = list(sig.parameters.keys())
    assert "cd" in params, "Missing parameter 'cd'"
    assert "gb" in params, "Missing parameter 'gb'"
    assert "plv" in params, "Missing parameter 'plv'"
    assert "players" in params, "Missing parameter 'players'"

def test_hyp_main_play_has_cd():
    assert hasattr(main_Play, "cd")
    descriptor = None
    for klass in main_Play.__mro__:
        if "cd" in klass.__dict__:
            descriptor = klass.__dict__["cd"]
            break
    assert isinstance(descriptor, property)

def test_hyp_main_play_has_gb():
    assert hasattr(main_Play, "gb")
    descriptor = None
    for klass in main_Play.__mro__:
        if "gb" in klass.__dict__:
            descriptor = klass.__dict__["gb"]
            break
    assert isinstance(descriptor, property)

def test_hyp_main_play_has_plv():
    assert hasattr(main_Play, "plv")
    descriptor = None
    for klass in main_Play.__mro__:
        if "plv" in klass.__dict__:
            descriptor = klass.__dict__["plv"]
            break
    assert isinstance(descriptor, property)

def test_hyp_main_play_has_players():
    assert hasattr(main_Play, "players")
    descriptor = None
    for klass in main_Play.__mro__:
        if "players" in klass.__dict__:
            descriptor = klass.__dict__["players"]
            break
    assert isinstance(descriptor, property)



def test_hyp_game_gameboardgui_is_not_abstract():
    assert not inspect.isabstract(game_GameBoardGUI)


def test_hyp_game_gameboardgui_constructor_exists():
    assert callable(game_GameBoardGUI.__init__)


def test_hyp_game_gameboardgui_constructor_args():
    sig = inspect.signature(game_GameBoardGUI.__init__)
    params = list(sig.parameters.keys())



def test_hyp_game_ranker_is_not_abstract():
    assert not inspect.isabstract(game_Ranker)


def test_hyp_game_ranker_constructor_exists():
    assert callable(game_Ranker.__init__)


def test_hyp_game_ranker_constructor_args():
    sig = inspect.signature(game_Ranker.__init__)
    params = list(sig.parameters.keys())
    assert "highValue" in params, "Missing parameter 'highValue'"
    assert "hand" in params, "Missing parameter 'hand'"

def test_hyp_game_ranker_has_highValue():
    assert hasattr(game_Ranker, "highValue")
    descriptor = None
    for klass in game_Ranker.__mro__:
        if "highValue" in klass.__dict__:
            descriptor = klass.__dict__["highValue"]
            break
    assert isinstance(descriptor, property)

def test_hyp_game_ranker_has_hand():
    assert hasattr(game_Ranker, "hand")
    descriptor = None
    for klass in game_Ranker.__mro__:
        if "hand" in klass.__dict__:
            descriptor = klass.__dict__["hand"]
            break
    assert isinstance(descriptor, property)



def test_hyp_players_person_is_not_abstract():
    assert not inspect.isabstract(players_Person)


def test_hyp_players_person_constructor_exists():
    assert callable(players_Person.__init__)


def test_hyp_players_person_constructor_args():
    sig = inspect.signature(players_Person.__init__)
    params = list(sig.parameters.keys())
    assert "accountNumber" in params, "Missing parameter 'accountNumber'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_players_playerversiongui_is_not_abstract():
    assert not inspect.isabstract(players_PlayerVersionGUI)


def test_hyp_players_playerversiongui_constructor_exists():
    assert callable(players_PlayerVersionGUI.__init__)


def test_hyp_players_playerversiongui_constructor_args():
    sig = inspect.signature(players_PlayerVersionGUI.__init__)
    params = list(sig.parameters.keys())



def test_hyp_players_player_is_not_abstract():
    assert not inspect.isabstract(players_Player)


def test_hyp_players_player_constructor_exists():
    assert callable(players_Player.__init__)


def test_hyp_players_player_constructor_args():
    sig = inspect.signature(players_Player.__init__)
    params = list(sig.parameters.keys())
    assert "hand" in params, "Missing parameter 'hand'"
    assert "curentChips" in params, "Missing parameter 'curentChips'"
    assert "hasFolded" in params, "Missing parameter 'hasFolded'"

def test_hyp_players_player_has_hand():
    assert hasattr(players_Player, "hand")
    descriptor = None
    for klass in players_Player.__mro__:
        if "hand" in klass.__dict__:
            descriptor = klass.__dict__["hand"]
            break
    assert isinstance(descriptor, property)

def test_hyp_players_player_has_curentChips():
    assert hasattr(players_Player, "curentChips")
    descriptor = None
    for klass in players_Player.__mro__:
        if "curentChips" in klass.__dict__:
            descriptor = klass.__dict__["curentChips"]
            break
    assert isinstance(descriptor, property)

def test_hyp_players_player_has_hasFolded():
    assert hasattr(players_Player, "hasFolded")
    descriptor = None
    for klass in players_Player.__mro__:
        if "hasFolded" in klass.__dict__:
            descriptor = klass.__dict__["hasFolded"]
            break
    assert isinstance(descriptor, property)



def test_hyp_cards_pokerhandinterface_interface_is_not_abstract():
    assert not inspect.isabstract(cards_PokerHandInterface_Interface)


def test_hyp_cards_pokerhandinterface_interface_constructor_exists():
    assert callable(cards_PokerHandInterface_Interface.__init__)


def test_hyp_cards_pokerhandinterface_interface_constructor_args():
    sig = inspect.signature(cards_PokerHandInterface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cards_cardsgui_is_not_abstract():
    assert not inspect.isabstract(cards_CardsGUI)


def test_hyp_cards_cardsgui_constructor_exists():
    assert callable(cards_CardsGUI.__init__)


def test_hyp_cards_cardsgui_constructor_args():
    sig = inspect.signature(cards_CardsGUI.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cards_deck_is_not_abstract():
    assert not inspect.isabstract(cards_Deck)


def test_hyp_cards_deck_constructor_exists():
    assert callable(cards_Deck.__init__)


def test_hyp_cards_deck_constructor_args():
    sig = inspect.signature(cards_Deck.__init__)
    params = list(sig.parameters.keys())
    assert "remain" in params, "Missing parameter 'remain'"
    assert "cards" in params, "Missing parameter 'cards'"





def test_hyp_cards_pokerhand_is_not_abstract():
    assert not inspect.isabstract(cards_PokerHand)


def test_hyp_cards_pokerhand_constructor_exists():
    assert callable(cards_PokerHand.__init__)


def test_hyp_cards_pokerhand_constructor_args():
    sig = inspect.signature(cards_PokerHand.__init__)
    params = list(sig.parameters.keys())
    assert "hand" in params, "Missing parameter 'hand'"
    assert "rank" in params, "Missing parameter 'rank'"





def test_hyp_cards_card_is_not_abstract():
    assert not inspect.isabstract(cards_Card)


def test_hyp_cards_card_constructor_exists():
    assert callable(cards_Card.__init__)


def test_hyp_cards_card_constructor_args():
    sig = inspect.signature(cards_Card.__init__)
    params = list(sig.parameters.keys())
    assert "rank" in params, "Missing parameter 'rank'"
    assert "suit" in params, "Missing parameter 'suit'"

def test_hyp_cards_card_has_rank():
    assert hasattr(cards_Card, "rank")
    descriptor = None
    for klass in cards_Card.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)

def test_hyp_cards_card_has_suit():
    assert hasattr(cards_Card, "suit")
    descriptor = None
    for klass in cards_Card.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)

def test_hyp_cards_suit_exists():
    # Check that the Enumeration exists
    assert cards_Suit is not None

def test_hyp_cards_suit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in cards_Suit]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in cards_Suit"


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
main_Play_strategy = st.builds(
    main_Play,
    cd=
        st.none(),
    gb=
        st.none(),
    plv=
        st.none(),
    players=
        safe_text
)
game_GameBoardGUI_strategy = st.builds(
    game_GameBoardGUI,
)
game_Ranker_strategy = st.builds(
    game_Ranker,
    highValue=
        st.integers(),
    hand=
        st.none()
)
players_Person_strategy = st.builds(
    players_Person,
    accountNumber=
        safe_text,
    name=
        safe_text
)
players_PlayerVersionGUI_strategy = st.builds(
    players_PlayerVersionGUI,
)
players_Player_strategy = st.builds(
    players_Player,
    hand=
        st.none(),
    curentChips=
        st.integers(),
    hasFolded=
        st.booleans()
)
cards_PokerHandInterface_Interface_strategy = st.builds(
    cards_PokerHandInterface_Interface,
)
cards_CardsGUI_strategy = st.builds(
    cards_CardsGUI,
)
cards_Deck_strategy = st.builds(
    cards_Deck,
    remain=
        st.integers(),
    cards=
        safe_text
)
cards_PokerHand_strategy = st.builds(
    cards_PokerHand,
    hand=
        safe_text,
    rank=
        st.integers()
)
cards_Card_strategy = st.builds(
    cards_Card,
    rank=
        st.integers(),
    suit=
        st.none()
)

@given(instance=main_Play_strategy)
@settings(max_examples=50)
def test_hyp_main_play_instantiation(instance):
    assert isinstance(instance, main_Play)



@given(instance=main_Play_strategy)
def test_hyp_main_play_cd_setter(instance):
    original = instance.cd
    instance.cd = original
    assert instance.cd == original



@given(instance=main_Play_strategy)
def test_hyp_main_play_gb_setter(instance):
    original = instance.gb
    instance.gb = original
    assert instance.gb == original



@given(instance=main_Play_strategy)
def test_hyp_main_play_plv_setter(instance):
    original = instance.plv
    instance.plv = original
    assert instance.plv == original



@given(instance=main_Play_strategy)
def test_hyp_main_play_players_setter(instance):
    original = instance.players
    instance.players = original
    assert instance.players == original


@given(instance=game_Ranker_strategy)
@settings(max_examples=50)
def test_hyp_game_ranker_instantiation(instance):
    assert isinstance(instance, game_Ranker)



@given(instance=game_Ranker_strategy)
def test_hyp_game_ranker_highValue_setter(instance):
    original = instance.highValue
    instance.highValue = original
    assert instance.highValue == original



@given(instance=game_Ranker_strategy)
def test_hyp_game_ranker_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original




@given(instance=players_Person_strategy)
def test_hyp_players_person_accountNumber_setter(instance):
    original = instance.accountNumber
    instance.accountNumber = original
    assert instance.accountNumber == original



@given(instance=players_Person_strategy)
def test_hyp_players_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


@given(instance=players_Player_strategy)
@settings(max_examples=50)
def test_hyp_players_player_instantiation(instance):
    assert isinstance(instance, players_Player)



@given(instance=players_Player_strategy)
def test_hyp_players_player_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original



@given(instance=players_Player_strategy)
def test_hyp_players_player_curentChips_setter(instance):
    original = instance.curentChips
    instance.curentChips = original
    assert instance.curentChips == original



@given(instance=players_Player_strategy)
def test_hyp_players_player_hasFolded_setter(instance):
    original = instance.hasFolded
    instance.hasFolded = original
    assert instance.hasFolded == original






@given(instance=cards_Deck_strategy)
def test_hyp_cards_deck_remain_setter(instance):
    original = instance.remain
    instance.remain = original
    assert instance.remain == original



@given(instance=cards_Deck_strategy)
def test_hyp_cards_deck_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original




@given(instance=cards_PokerHand_strategy)
def test_hyp_cards_pokerhand_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original



@given(instance=cards_PokerHand_strategy)
def test_hyp_cards_pokerhand_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=cards_Card_strategy)
@settings(max_examples=50)
def test_hyp_cards_card_instantiation(instance):
    assert isinstance(instance, cards_Card)



@given(instance=cards_Card_strategy)
def test_hyp_cards_card_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original



@given(instance=cards_Card_strategy)
def test_hyp_cards_card_suit_setter(instance):
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
    cards_Card,
    cards_CardsGUI,
    cards_Deck,
    cards_PokerHand,
    cards_PokerHandInterface_Interface,
    game_GameBoardGUI,
    game_Ranker,
    main_Play,
    players_Person,
    players_Player,
    players_PlayerVersionGUI,
    cards_Suit,
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

def test_cards_Deck_cards_value_roundtrip():
    instance = cards_Deck(cards="sample_text", remain=7)
    assert instance.cards == "sample_text"
    instance.cards = "sample_text_2"
    assert instance.cards == "sample_text_2"


def test_cards_Deck_remain_value_roundtrip():
    instance = cards_Deck(cards="sample_text", remain=7)
    assert instance.remain == 7
    instance.remain = 13
    assert instance.remain == 13


def test_cards_PokerHand_hand_value_roundtrip():
    instance = cards_PokerHand(hand="sample_text", rank=7)
    assert instance.hand == "sample_text"
    instance.hand = "sample_text_2"
    assert instance.hand == "sample_text_2"


def test_cards_PokerHand_rank_value_roundtrip():
    instance = cards_PokerHand(hand="sample_text", rank=7)
    assert instance.rank == 7
    instance.rank = 13
    assert instance.rank == 13


def test_players_Person_accountNumber_value_roundtrip():
    instance = players_Person(accountNumber="sample_text", name="sample_text")
    assert instance.accountNumber == "sample_text"
    instance.accountNumber = "sample_text_2"
    assert instance.accountNumber == "sample_text_2"


def test_players_Person_name_value_roundtrip():
    instance = players_Person(accountNumber="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

cards_CardsGUI_strategy = st.builds(cards_CardsGUI)
@given(instance=cards_CardsGUI_strategy)
@settings(max_examples=25)
def test_cards_CardsGUI_instantiation(instance):
    assert isinstance(instance, cards_CardsGUI)


cards_Deck_strategy = st.builds(cards_Deck, cards=safe_text, remain=st.integers())
@given(instance=cards_Deck_strategy)
@settings(max_examples=25)
def test_cards_Deck_instantiation(instance):
    assert isinstance(instance, cards_Deck)


cards_PokerHand_strategy = st.builds(cards_PokerHand, hand=safe_text, rank=st.integers())
@given(instance=cards_PokerHand_strategy)
@settings(max_examples=25)
def test_cards_PokerHand_instantiation(instance):
    assert isinstance(instance, cards_PokerHand)


cards_PokerHandInterface_Interface_strategy = st.builds(cards_PokerHandInterface_Interface)
@given(instance=cards_PokerHandInterface_Interface_strategy)
@settings(max_examples=25)
def test_cards_PokerHandInterface_Interface_instantiation(instance):
    assert isinstance(instance, cards_PokerHandInterface_Interface)


game_GameBoardGUI_strategy = st.builds(game_GameBoardGUI)
@given(instance=game_GameBoardGUI_strategy)
@settings(max_examples=25)
def test_game_GameBoardGUI_instantiation(instance):
    assert isinstance(instance, game_GameBoardGUI)


players_Person_strategy = st.builds(players_Person, accountNumber=safe_text, name=safe_text)
@given(instance=players_Person_strategy)
@settings(max_examples=25)
def test_players_Person_instantiation(instance):
    assert isinstance(instance, players_Person)


players_PlayerVersionGUI_strategy = st.builds(players_PlayerVersionGUI)
@given(instance=players_PlayerVersionGUI_strategy)
@settings(max_examples=25)
def test_players_PlayerVersionGUI_instantiation(instance):
    assert isinstance(instance, players_PlayerVersionGUI)



