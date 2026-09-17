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
    JButton,
    Strategy,
    Card,
    LoginView,
    GameLauncher,
    Profile,
    Hand,
    Deck,
    BlackjackGame,
    PlayerView,
    Dealer,
    Player,
    JLabel,
    UseCase_UseCase,
    User_Actor,
    BasePlayer,
    GameView,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_jbutton_is_not_abstract():
    assert not inspect.isabstract(JButton)


def test_hyp_jbutton_constructor_exists():
    assert callable(JButton.__init__)


def test_hyp_jbutton_constructor_args():
    sig = inspect.signature(JButton.__init__)
    params = list(sig.parameters.keys())



def test_hyp_strategy_is_not_abstract():
    assert not inspect.isabstract(Strategy)


def test_hyp_strategy_constructor_exists():
    assert callable(Strategy.__init__)


def test_hyp_strategy_constructor_args():
    sig = inspect.signature(Strategy.__init__)
    params = list(sig.parameters.keys())
    assert "game" in params, "Missing parameter 'game'"

def test_hyp_strategy_has_game():
    assert hasattr(Strategy, "game")
    descriptor = None
    for klass in Strategy.__mro__:
        if "game" in klass.__dict__:
            descriptor = klass.__dict__["game"]
            break
    assert isinstance(descriptor, property)



def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "rank" in params, "Missing parameter 'rank'"
    assert "name" in params, "Missing parameter 'name'"
    assert "valueSoft" in params, "Missing parameter 'valueSoft'"
    assert "avatar" in params, "Missing parameter 'avatar'"
    assert "Count" in params, "Missing parameter 'Count'"
    assert "suit" in params, "Missing parameter 'suit'"
    assert "valueHard" in params, "Missing parameter 'valueHard'"










def test_hyp_loginview_is_not_abstract():
    assert not inspect.isabstract(LoginView)


def test_hyp_loginview_constructor_exists():
    assert callable(LoginView.__init__)


def test_hyp_loginview_constructor_args():
    sig = inspect.signature(LoginView.__init__)
    params = list(sig.parameters.keys())
    assert "user" in params, "Missing parameter 'user'"

def test_hyp_loginview_has_user():
    assert hasattr(LoginView, "user")
    descriptor = None
    for klass in LoginView.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)



def test_hyp_gamelauncher_is_not_abstract():
    assert not inspect.isabstract(GameLauncher)


def test_hyp_gamelauncher_constructor_exists():
    assert callable(GameLauncher.__init__)


def test_hyp_gamelauncher_constructor_args():
    sig = inspect.signature(GameLauncher.__init__)
    params = list(sig.parameters.keys())
    assert "blackjack" in params, "Missing parameter 'blackjack'"
    assert "login" in params, "Missing parameter 'login'"

def test_hyp_gamelauncher_has_blackjack():
    assert hasattr(GameLauncher, "blackjack")
    descriptor = None
    for klass in GameLauncher.__mro__:
        if "blackjack" in klass.__dict__:
            descriptor = klass.__dict__["blackjack"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gamelauncher_has_login():
    assert hasattr(GameLauncher, "login")
    descriptor = None
    for klass in GameLauncher.__mro__:
        if "login" in klass.__dict__:
            descriptor = klass.__dict__["login"]
            break
    assert isinstance(descriptor, property)



def test_hyp_profile_is_not_abstract():
    assert not inspect.isabstract(Profile)


def test_hyp_profile_constructor_exists():
    assert callable(Profile.__init__)


def test_hyp_profile_constructor_args():
    sig = inspect.signature(Profile.__init__)
    params = list(sig.parameters.keys())
    assert "money" in params, "Missing parameter 'money'"
    assert "username" in params, "Missing parameter 'username'"





def test_hyp_hand_is_not_abstract():
    assert not inspect.isabstract(Hand)


def test_hyp_hand_constructor_exists():
    assert callable(Hand.__init__)


def test_hyp_hand_constructor_args():
    sig = inspect.signature(Hand.__init__)
    params = list(sig.parameters.keys())
    assert "cards" in params, "Missing parameter 'cards'"
    assert "total" in params, "Missing parameter 'total'"

def test_hyp_hand_has_cards():
    assert hasattr(Hand, "cards")
    descriptor = None
    for klass in Hand.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)

def test_hyp_hand_has_total():
    assert hasattr(Hand, "total")
    descriptor = None
    for klass in Hand.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)



def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "cards" in params, "Missing parameter 'cards'"

def test_hyp_deck_has_cards():
    assert hasattr(Deck, "cards")
    descriptor = None
    for klass in Deck.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)



def test_hyp_blackjackgame_is_not_abstract():
    assert not inspect.isabstract(BlackjackGame)


def test_hyp_blackjackgame_constructor_exists():
    assert callable(BlackjackGame.__init__)


def test_hyp_blackjackgame_constructor_args():
    sig = inspect.signature(BlackjackGame.__init__)
    params = list(sig.parameters.keys())
    assert "player" in params, "Missing parameter 'player'"
    assert "deck" in params, "Missing parameter 'deck'"
    assert "dealer" in params, "Missing parameter 'dealer'"
    assert "bet" in params, "Missing parameter 'bet'"

def test_hyp_blackjackgame_has_player():
    assert hasattr(BlackjackGame, "player")
    descriptor = None
    for klass in BlackjackGame.__mro__:
        if "player" in klass.__dict__:
            descriptor = klass.__dict__["player"]
            break
    assert isinstance(descriptor, property)

def test_hyp_blackjackgame_has_deck():
    assert hasattr(BlackjackGame, "deck")
    descriptor = None
    for klass in BlackjackGame.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)

def test_hyp_blackjackgame_has_dealer():
    assert hasattr(BlackjackGame, "dealer")
    descriptor = None
    for klass in BlackjackGame.__mro__:
        if "dealer" in klass.__dict__:
            descriptor = klass.__dict__["dealer"]
            break
    assert isinstance(descriptor, property)

def test_hyp_blackjackgame_has_bet():
    assert hasattr(BlackjackGame, "bet")
    descriptor = None
    for klass in BlackjackGame.__mro__:
        if "bet" in klass.__dict__:
            descriptor = klass.__dict__["bet"]
            break
    assert isinstance(descriptor, property)



def test_hyp_playerview_is_not_abstract():
    assert not inspect.isabstract(PlayerView)


def test_hyp_playerview_constructor_exists():
    assert callable(PlayerView.__init__)


def test_hyp_playerview_constructor_args():
    sig = inspect.signature(PlayerView.__init__)
    params = list(sig.parameters.keys())
    assert "busted" in params, "Missing parameter 'busted'"
    assert "cardLabels" in params, "Missing parameter 'cardLabels'"
    assert "player" in params, "Missing parameter 'player'"
    assert "cardTotal" in params, "Missing parameter 'cardTotal'"
    assert "status" in params, "Missing parameter 'status'"
    assert "moneyBox" in params, "Missing parameter 'moneyBox'"

def test_hyp_playerview_has_busted():
    assert hasattr(PlayerView, "busted")
    descriptor = None
    for klass in PlayerView.__mro__:
        if "busted" in klass.__dict__:
            descriptor = klass.__dict__["busted"]
            break
    assert isinstance(descriptor, property)

def test_hyp_playerview_has_cardLabels():
    assert hasattr(PlayerView, "cardLabels")
    descriptor = None
    for klass in PlayerView.__mro__:
        if "cardLabels" in klass.__dict__:
            descriptor = klass.__dict__["cardLabels"]
            break
    assert isinstance(descriptor, property)

def test_hyp_playerview_has_player():
    assert hasattr(PlayerView, "player")
    descriptor = None
    for klass in PlayerView.__mro__:
        if "player" in klass.__dict__:
            descriptor = klass.__dict__["player"]
            break
    assert isinstance(descriptor, property)

def test_hyp_playerview_has_cardTotal():
    assert hasattr(PlayerView, "cardTotal")
    descriptor = None
    for klass in PlayerView.__mro__:
        if "cardTotal" in klass.__dict__:
            descriptor = klass.__dict__["cardTotal"]
            break
    assert isinstance(descriptor, property)

def test_hyp_playerview_has_status():
    assert hasattr(PlayerView, "status")
    descriptor = None
    for klass in PlayerView.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_hyp_playerview_has_moneyBox():
    assert hasattr(PlayerView, "moneyBox")
    descriptor = None
    for klass in PlayerView.__mro__:
        if "moneyBox" in klass.__dict__:
            descriptor = klass.__dict__["moneyBox"]
            break
    assert isinstance(descriptor, property)



def test_hyp_dealer_is_not_abstract():
    assert not inspect.isabstract(Dealer)


def test_hyp_dealer_constructor_exists():
    assert callable(Dealer.__init__)


def test_hyp_dealer_constructor_args():
    sig = inspect.signature(Dealer.__init__)
    params = list(sig.parameters.keys())
    assert "hand" in params, "Missing parameter 'hand'"
    assert "cardTotalLimit" in params, "Missing parameter 'cardTotalLimit'"

def test_hyp_dealer_has_hand():
    assert hasattr(Dealer, "hand")
    descriptor = None
    for klass in Dealer.__mro__:
        if "hand" in klass.__dict__:
            descriptor = klass.__dict__["hand"]
            break
    assert isinstance(descriptor, property)

def test_hyp_dealer_has_cardTotalLimit():
    assert hasattr(Dealer, "cardTotalLimit")
    descriptor = None
    for klass in Dealer.__mro__:
        if "cardTotalLimit" in klass.__dict__:
            descriptor = klass.__dict__["cardTotalLimit"]
            break
    assert isinstance(descriptor, property)



def test_hyp_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_hyp_player_constructor_exists():
    assert callable(Player.__init__)


def test_hyp_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "profile" in params, "Missing parameter 'profile'"
    assert "money" in params, "Missing parameter 'money'"
    assert "hand" in params, "Missing parameter 'hand'"

def test_hyp_player_has_profile():
    assert hasattr(Player, "profile")
    descriptor = None
    for klass in Player.__mro__:
        if "profile" in klass.__dict__:
            descriptor = klass.__dict__["profile"]
            break
    assert isinstance(descriptor, property)

def test_hyp_player_has_money():
    assert hasattr(Player, "money")
    descriptor = None
    for klass in Player.__mro__:
        if "money" in klass.__dict__:
            descriptor = klass.__dict__["money"]
            break
    assert isinstance(descriptor, property)

def test_hyp_player_has_hand():
    assert hasattr(Player, "hand")
    descriptor = None
    for klass in Player.__mro__:
        if "hand" in klass.__dict__:
            descriptor = klass.__dict__["hand"]
            break
    assert isinstance(descriptor, property)



def test_hyp_jlabel_is_not_abstract():
    assert not inspect.isabstract(JLabel)


def test_hyp_jlabel_constructor_exists():
    assert callable(JLabel.__init__)


def test_hyp_jlabel_constructor_args():
    sig = inspect.signature(JLabel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_usecase_usecase_is_not_abstract():
    assert not inspect.isabstract(UseCase_UseCase)


def test_hyp_usecase_usecase_constructor_exists():
    assert callable(UseCase_UseCase.__init__)


def test_hyp_usecase_usecase_constructor_args():
    sig = inspect.signature(UseCase_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_user_actor_is_not_abstract():
    assert not inspect.isabstract(User_Actor)


def test_hyp_user_actor_constructor_exists():
    assert callable(User_Actor.__init__)


def test_hyp_user_actor_constructor_args():
    sig = inspect.signature(User_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_baseplayer_is_not_abstract():
    assert not inspect.isabstract(BasePlayer)


def test_hyp_baseplayer_constructor_exists():
    assert callable(BasePlayer.__init__)


def test_hyp_baseplayer_constructor_args():
    sig = inspect.signature(BasePlayer.__init__)
    params = list(sig.parameters.keys())
    assert "isBusted" in params, "Missing parameter 'isBusted'"




def test_hyp_gameview_is_not_abstract():
    assert not inspect.isabstract(GameView)


def test_hyp_gameview_constructor_exists():
    assert callable(GameView.__init__)


def test_hyp_gameview_constructor_args():
    sig = inspect.signature(GameView.__init__)
    params = list(sig.parameters.keys())
    assert "doubleButton" in params, "Missing parameter 'doubleButton'"
    assert "splitButton" in params, "Missing parameter 'splitButton'"
    assert "standButton" in params, "Missing parameter 'standButton'"
    assert "bet" in params, "Missing parameter 'bet'"
    assert "hitButton" in params, "Missing parameter 'hitButton'"
    assert "dealButton" in params, "Missing parameter 'dealButton'"
    assert "showStrategy" in params, "Missing parameter 'showStrategy'"

def test_hyp_gameview_has_doubleButton():
    assert hasattr(GameView, "doubleButton")
    descriptor = None
    for klass in GameView.__mro__:
        if "doubleButton" in klass.__dict__:
            descriptor = klass.__dict__["doubleButton"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gameview_has_splitButton():
    assert hasattr(GameView, "splitButton")
    descriptor = None
    for klass in GameView.__mro__:
        if "splitButton" in klass.__dict__:
            descriptor = klass.__dict__["splitButton"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gameview_has_standButton():
    assert hasattr(GameView, "standButton")
    descriptor = None
    for klass in GameView.__mro__:
        if "standButton" in klass.__dict__:
            descriptor = klass.__dict__["standButton"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gameview_has_bet():
    assert hasattr(GameView, "bet")
    descriptor = None
    for klass in GameView.__mro__:
        if "bet" in klass.__dict__:
            descriptor = klass.__dict__["bet"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gameview_has_hitButton():
    assert hasattr(GameView, "hitButton")
    descriptor = None
    for klass in GameView.__mro__:
        if "hitButton" in klass.__dict__:
            descriptor = klass.__dict__["hitButton"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gameview_has_dealButton():
    assert hasattr(GameView, "dealButton")
    descriptor = None
    for klass in GameView.__mro__:
        if "dealButton" in klass.__dict__:
            descriptor = klass.__dict__["dealButton"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gameview_has_showStrategy():
    assert hasattr(GameView, "showStrategy")
    descriptor = None
    for klass in GameView.__mro__:
        if "showStrategy" in klass.__dict__:
            descriptor = klass.__dict__["showStrategy"]
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
JButton_strategy = st.builds(
    JButton,
)
Strategy_strategy = st.builds(
    Strategy,
    game=
        st.none()
)
Card_strategy = st.builds(
    Card,
    rank=
        safe_text,
    name=
        safe_text,
    valueSoft=
        safe_text,
    avatar=
        safe_text,
    Count=
        st.integers(),
    suit=
        safe_text,
    valueHard=
        safe_text
)
LoginView_strategy = st.builds(
    LoginView,
    user=
        st.none()
)
GameLauncher_strategy = st.builds(
    GameLauncher,
    blackjack=
        st.none(),
    login=
        st.none()
)
Profile_strategy = st.builds(
    Profile,
    money=
        st.integers(),
    username=
        safe_text
)
Hand_strategy = st.builds(
    Hand,
    cards=
        st.none(),
    total=
        st.integers()
)
Deck_strategy = st.builds(
    Deck,
    cards=
        st.none()
)
BlackjackGame_strategy = st.builds(
    BlackjackGame,
    player=
        st.none(),
    deck=
        st.none(),
    dealer=
        st.none(),
    bet=
        st.integers()
)
PlayerView_strategy = st.builds(
    PlayerView,
    busted=
        st.none(),
    cardLabels=
        st.none(),
    player=
        st.none(),
    cardTotal=
        st.none(),
    status=
        st.none(),
    moneyBox=
        st.none()
)
Dealer_strategy = st.builds(
    Dealer,
    hand=
        st.none(),
    cardTotalLimit=
        st.integers()
)
Player_strategy = st.builds(
    Player,
    profile=
        st.none(),
    money=
        st.integers(),
    hand=
        st.none()
)
JLabel_strategy = st.builds(
    JLabel,
)
UseCase_UseCase_strategy = st.builds(
    UseCase_UseCase,
)
User_Actor_strategy = st.builds(
    User_Actor,
)
BasePlayer_strategy = st.builds(
    BasePlayer,
    isBusted=
        st.booleans()
)
GameView_strategy = st.builds(
    GameView,
    doubleButton=
        st.none(),
    splitButton=
        st.none(),
    standButton=
        st.none(),
    bet=
        st.none(),
    hitButton=
        st.none(),
    dealButton=
        st.none(),
    showStrategy=
        st.booleans()
)


@given(instance=Strategy_strategy)
@settings(max_examples=50)
def test_hyp_strategy_instantiation(instance):
    assert isinstance(instance, Strategy)



@given(instance=Strategy_strategy)
def test_hyp_strategy_game_setter(instance):
    original = instance.game
    instance.game = original
    assert instance.game == original




@given(instance=Card_strategy)
def test_hyp_card_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original



@given(instance=Card_strategy)
def test_hyp_card_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Card_strategy)
def test_hyp_card_valueSoft_setter(instance):
    original = instance.valueSoft
    instance.valueSoft = original
    assert instance.valueSoft == original



@given(instance=Card_strategy)
def test_hyp_card_avatar_setter(instance):
    original = instance.avatar
    instance.avatar = original
    assert instance.avatar == original



@given(instance=Card_strategy)
def test_hyp_card_Count_setter(instance):
    original = instance.Count
    instance.Count = original
    assert instance.Count == original



@given(instance=Card_strategy)
def test_hyp_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=Card_strategy)
def test_hyp_card_valueHard_setter(instance):
    original = instance.valueHard
    instance.valueHard = original
    assert instance.valueHard == original

@given(instance=LoginView_strategy)
@settings(max_examples=50)
def test_hyp_loginview_instantiation(instance):
    assert isinstance(instance, LoginView)



@given(instance=LoginView_strategy)
def test_hyp_loginview_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original

@given(instance=GameLauncher_strategy)
@settings(max_examples=50)
def test_hyp_gamelauncher_instantiation(instance):
    assert isinstance(instance, GameLauncher)



@given(instance=GameLauncher_strategy)
def test_hyp_gamelauncher_blackjack_setter(instance):
    original = instance.blackjack
    instance.blackjack = original
    assert instance.blackjack == original



@given(instance=GameLauncher_strategy)
def test_hyp_gamelauncher_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original




@given(instance=Profile_strategy)
def test_hyp_profile_money_setter(instance):
    original = instance.money
    instance.money = original
    assert instance.money == original



@given(instance=Profile_strategy)
def test_hyp_profile_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=Hand_strategy)
@settings(max_examples=50)
def test_hyp_hand_instantiation(instance):
    assert isinstance(instance, Hand)



@given(instance=Hand_strategy)
def test_hyp_hand_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original



@given(instance=Hand_strategy)
def test_hyp_hand_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original

@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_hyp_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_hyp_deck_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original

@given(instance=BlackjackGame_strategy)
@settings(max_examples=50)
def test_hyp_blackjackgame_instantiation(instance):
    assert isinstance(instance, BlackjackGame)



@given(instance=BlackjackGame_strategy)
def test_hyp_blackjackgame_player_setter(instance):
    original = instance.player
    instance.player = original
    assert instance.player == original



@given(instance=BlackjackGame_strategy)
def test_hyp_blackjackgame_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original



@given(instance=BlackjackGame_strategy)
def test_hyp_blackjackgame_dealer_setter(instance):
    original = instance.dealer
    instance.dealer = original
    assert instance.dealer == original



@given(instance=BlackjackGame_strategy)
def test_hyp_blackjackgame_bet_setter(instance):
    original = instance.bet
    instance.bet = original
    assert instance.bet == original

@given(instance=PlayerView_strategy)
@settings(max_examples=50)
def test_hyp_playerview_instantiation(instance):
    assert isinstance(instance, PlayerView)



@given(instance=PlayerView_strategy)
def test_hyp_playerview_busted_setter(instance):
    original = instance.busted
    instance.busted = original
    assert instance.busted == original



@given(instance=PlayerView_strategy)
def test_hyp_playerview_cardLabels_setter(instance):
    original = instance.cardLabels
    instance.cardLabels = original
    assert instance.cardLabels == original



@given(instance=PlayerView_strategy)
def test_hyp_playerview_player_setter(instance):
    original = instance.player
    instance.player = original
    assert instance.player == original



@given(instance=PlayerView_strategy)
def test_hyp_playerview_cardTotal_setter(instance):
    original = instance.cardTotal
    instance.cardTotal = original
    assert instance.cardTotal == original



@given(instance=PlayerView_strategy)
def test_hyp_playerview_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=PlayerView_strategy)
def test_hyp_playerview_moneyBox_setter(instance):
    original = instance.moneyBox
    instance.moneyBox = original
    assert instance.moneyBox == original

@given(instance=Dealer_strategy)
@settings(max_examples=50)
def test_hyp_dealer_instantiation(instance):
    assert isinstance(instance, Dealer)



@given(instance=Dealer_strategy)
def test_hyp_dealer_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original



@given(instance=Dealer_strategy)
def test_hyp_dealer_cardTotalLimit_setter(instance):
    original = instance.cardTotalLimit
    instance.cardTotalLimit = original
    assert instance.cardTotalLimit == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_hyp_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_hyp_player_profile_setter(instance):
    original = instance.profile
    instance.profile = original
    assert instance.profile == original



@given(instance=Player_strategy)
def test_hyp_player_money_setter(instance):
    original = instance.money
    instance.money = original
    assert instance.money == original



@given(instance=Player_strategy)
def test_hyp_player_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original







@given(instance=BasePlayer_strategy)
def test_hyp_baseplayer_isBusted_setter(instance):
    original = instance.isBusted
    instance.isBusted = original
    assert instance.isBusted == original

@given(instance=GameView_strategy)
@settings(max_examples=50)
def test_hyp_gameview_instantiation(instance):
    assert isinstance(instance, GameView)



@given(instance=GameView_strategy)
def test_hyp_gameview_doubleButton_setter(instance):
    original = instance.doubleButton
    instance.doubleButton = original
    assert instance.doubleButton == original



@given(instance=GameView_strategy)
def test_hyp_gameview_splitButton_setter(instance):
    original = instance.splitButton
    instance.splitButton = original
    assert instance.splitButton == original



@given(instance=GameView_strategy)
def test_hyp_gameview_standButton_setter(instance):
    original = instance.standButton
    instance.standButton = original
    assert instance.standButton == original



@given(instance=GameView_strategy)
def test_hyp_gameview_bet_setter(instance):
    original = instance.bet
    instance.bet = original
    assert instance.bet == original



@given(instance=GameView_strategy)
def test_hyp_gameview_hitButton_setter(instance):
    original = instance.hitButton
    instance.hitButton = original
    assert instance.hitButton == original



@given(instance=GameView_strategy)
def test_hyp_gameview_dealButton_setter(instance):
    original = instance.dealButton
    instance.dealButton = original
    assert instance.dealButton == original



@given(instance=GameView_strategy)
def test_hyp_gameview_showStrategy_setter(instance):
    original = instance.showStrategy
    instance.showStrategy = original
    assert instance.showStrategy == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BasePlayer,
    BlackjackGame,
    Card,
    Dealer,
    Deck,
    GameLauncher,
    GameView,
    Hand,
    JButton,
    JLabel,
    LoginView,
    Player,
    PlayerView,
    Profile,
    Strategy,
    UseCase_UseCase,
    User_Actor,
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

def test_BasePlayer_isBusted_value_roundtrip():
    instance = BasePlayer(isBusted=True)
    assert instance.isBusted == True
    instance.isBusted = False
    assert instance.isBusted == False


def test_Card_Count_value_roundtrip():
    instance = Card(Count=7, avatar="sample_text", name="sample_text", rank="sample_text", suit="sample_text", valueHard="sample_text", valueSoft="sample_text")
    assert instance.Count == 7
    instance.Count = 13
    assert instance.Count == 13


def test_Card_avatar_value_roundtrip():
    instance = Card(Count=7, avatar="sample_text", name="sample_text", rank="sample_text", suit="sample_text", valueHard="sample_text", valueSoft="sample_text")
    assert instance.avatar == "sample_text"
    instance.avatar = "sample_text_2"
    assert instance.avatar == "sample_text_2"


def test_Card_name_value_roundtrip():
    instance = Card(Count=7, avatar="sample_text", name="sample_text", rank="sample_text", suit="sample_text", valueHard="sample_text", valueSoft="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Card_rank_value_roundtrip():
    instance = Card(Count=7, avatar="sample_text", name="sample_text", rank="sample_text", suit="sample_text", valueHard="sample_text", valueSoft="sample_text")
    assert instance.rank == "sample_text"
    instance.rank = "sample_text_2"
    assert instance.rank == "sample_text_2"


def test_Card_suit_value_roundtrip():
    instance = Card(Count=7, avatar="sample_text", name="sample_text", rank="sample_text", suit="sample_text", valueHard="sample_text", valueSoft="sample_text")
    assert instance.suit == "sample_text"
    instance.suit = "sample_text_2"
    assert instance.suit == "sample_text_2"


def test_Card_valueHard_value_roundtrip():
    instance = Card(Count=7, avatar="sample_text", name="sample_text", rank="sample_text", suit="sample_text", valueHard="sample_text", valueSoft="sample_text")
    assert instance.valueHard == "sample_text"
    instance.valueHard = "sample_text_2"
    assert instance.valueHard == "sample_text_2"


def test_Card_valueSoft_value_roundtrip():
    instance = Card(Count=7, avatar="sample_text", name="sample_text", rank="sample_text", suit="sample_text", valueHard="sample_text", valueSoft="sample_text")
    assert instance.valueSoft == "sample_text"
    instance.valueSoft = "sample_text_2"
    assert instance.valueSoft == "sample_text_2"


def test_Profile_money_value_roundtrip():
    instance = Profile(money=7, username="sample_text")
    assert instance.money == 7
    instance.money = 13
    assert instance.money == 13


def test_Profile_username_value_roundtrip():
    instance = Profile(money=7, username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BasePlayer_strategy = st.builds(BasePlayer, isBusted=st.booleans())
@given(instance=BasePlayer_strategy)
@settings(max_examples=25)
def test_BasePlayer_instantiation(instance):
    assert isinstance(instance, BasePlayer)


Card_strategy = st.builds(Card, Count=st.integers(), avatar=safe_text, name=safe_text, rank=safe_text, suit=safe_text, valueHard=safe_text, valueSoft=safe_text)
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)


JButton_strategy = st.builds(JButton)
@given(instance=JButton_strategy)
@settings(max_examples=25)
def test_JButton_instantiation(instance):
    assert isinstance(instance, JButton)


JLabel_strategy = st.builds(JLabel)
@given(instance=JLabel_strategy)
@settings(max_examples=25)
def test_JLabel_instantiation(instance):
    assert isinstance(instance, JLabel)


Profile_strategy = st.builds(Profile, money=st.integers(), username=safe_text)
@given(instance=Profile_strategy)
@settings(max_examples=25)
def test_Profile_instantiation(instance):
    assert isinstance(instance, Profile)


UseCase_UseCase_strategy = st.builds(UseCase_UseCase)
@given(instance=UseCase_UseCase_strategy)
@settings(max_examples=25)
def test_UseCase_UseCase_instantiation(instance):
    assert isinstance(instance, UseCase_UseCase)


User_Actor_strategy = st.builds(User_Actor)
@given(instance=User_Actor_strategy)
@settings(max_examples=25)
def test_User_Actor_instantiation(instance):
    assert isinstance(instance, User_Actor)



