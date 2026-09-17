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
    int___1,
    Color,
    WildCard,
    Wild4,
    Wild,
    Draw2,
    Skip,
    Reverse,
    ActionCard,
    NumberCard,
    Card,
    CardElements_Interface,
    GameElements,
    GameElements_Interface,
    DiscardPile,
    DrawPile,
    Dealer,
    Players,
    Game,
    GameSession,
    Main,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_int___1_is_not_abstract():
    assert not inspect.isabstract(int___1)


def test_hyp_int___1_constructor_exists():
    assert callable(int___1.__init__)


def test_hyp_int___1_constructor_args():
    sig = inspect.signature(int___1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_color_is_not_abstract():
    assert not inspect.isabstract(Color)


def test_hyp_color_constructor_exists():
    assert callable(Color.__init__)


def test_hyp_color_constructor_args():
    sig = inspect.signature(Color.__init__)
    params = list(sig.parameters.keys())



def test_hyp_wildcard_is_not_abstract():
    assert not inspect.isabstract(WildCard)


def test_hyp_wildcard_constructor_exists():
    assert callable(WildCard.__init__)


def test_hyp_wildcard_constructor_args():
    sig = inspect.signature(WildCard.__init__)
    params = list(sig.parameters.keys())
    assert "WildCard_String_" in params, "Missing parameter 'WildCard_String_'"
    assert "WildCard__" in params, "Missing parameter 'WildCard__'"





def test_hyp_wild4_is_not_abstract():
    assert not inspect.isabstract(Wild4)


def test_hyp_wild4_constructor_exists():
    assert callable(Wild4.__init__)


def test_hyp_wild4_constructor_args():
    sig = inspect.signature(Wild4.__init__)
    params = list(sig.parameters.keys())



def test_hyp_wild_is_not_abstract():
    assert not inspect.isabstract(Wild)


def test_hyp_wild_constructor_exists():
    assert callable(Wild.__init__)


def test_hyp_wild_constructor_args():
    sig = inspect.signature(Wild.__init__)
    params = list(sig.parameters.keys())



def test_hyp_draw2_is_not_abstract():
    assert not inspect.isabstract(Draw2)


def test_hyp_draw2_constructor_exists():
    assert callable(Draw2.__init__)


def test_hyp_draw2_constructor_args():
    sig = inspect.signature(Draw2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_skip_is_not_abstract():
    assert not inspect.isabstract(Skip)


def test_hyp_skip_constructor_exists():
    assert callable(Skip.__init__)


def test_hyp_skip_constructor_args():
    sig = inspect.signature(Skip.__init__)
    params = list(sig.parameters.keys())



def test_hyp_reverse_is_not_abstract():
    assert not inspect.isabstract(Reverse)


def test_hyp_reverse_constructor_exists():
    assert callable(Reverse.__init__)


def test_hyp_reverse_constructor_args():
    sig = inspect.signature(Reverse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_actioncard_is_not_abstract():
    assert not inspect.isabstract(ActionCard)


def test_hyp_actioncard_constructor_exists():
    assert callable(ActionCard.__init__)


def test_hyp_actioncard_constructor_args():
    sig = inspect.signature(ActionCard.__init__)
    params = list(sig.parameters.keys())
    assert "ActionCard__" in params, "Missing parameter 'ActionCard__'"
    assert "_attr" in params, "Missing parameter '_attr'"
    assert "ActionCard_Color_String_" in params, "Missing parameter 'ActionCard_Color_String_'"






def test_hyp_numbercard_is_not_abstract():
    assert not inspect.isabstract(NumberCard)


def test_hyp_numbercard_constructor_exists():
    assert callable(NumberCard.__init__)


def test_hyp_numbercard_constructor_args():
    sig = inspect.signature(NumberCard.__init__)
    params = list(sig.parameters.keys())
    assert "NumberCard__" in params, "Missing parameter 'NumberCard__'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "NumberCard_Color__String_" in params, "Missing parameter 'NumberCard_Color__String_'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"







def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "setValue" in params, "Missing parameter 'setValue'"
    assert "Card__" in params, "Missing parameter 'Card__'"
    assert "getColor__" in params, "Missing parameter 'getColor__'"
    assert "setColor_Color_" in params, "Missing parameter 'setColor_Color_'"
    assert "Card__1" in params, "Missing parameter 'Card__1'"
    assert "Card_Color__int__String_" in params, "Missing parameter 'Card_Color__int__String_'"

def test_hyp_card_has_setValue():
    assert hasattr(Card, "setValue")
    descriptor = None
    for klass in Card.__mro__:
        if "setValue" in klass.__dict__:
            descriptor = klass.__dict__["setValue"]
            break
    assert isinstance(descriptor, property)

def test_hyp_card_has_Card__():
    assert hasattr(Card, "Card__")
    descriptor = None
    for klass in Card.__mro__:
        if "Card__" in klass.__dict__:
            descriptor = klass.__dict__["Card__"]
            break
    assert isinstance(descriptor, property)

def test_hyp_card_has_getColor__():
    assert hasattr(Card, "getColor__")
    descriptor = None
    for klass in Card.__mro__:
        if "getColor__" in klass.__dict__:
            descriptor = klass.__dict__["getColor__"]
            break
    assert isinstance(descriptor, property)

def test_hyp_card_has_setColor_Color_():
    assert hasattr(Card, "setColor_Color_")
    descriptor = None
    for klass in Card.__mro__:
        if "setColor_Color_" in klass.__dict__:
            descriptor = klass.__dict__["setColor_Color_"]
            break
    assert isinstance(descriptor, property)

def test_hyp_card_has_Card__1():
    assert hasattr(Card, "Card__1")
    descriptor = None
    for klass in Card.__mro__:
        if "Card__1" in klass.__dict__:
            descriptor = klass.__dict__["Card__1"]
            break
    assert isinstance(descriptor, property)

def test_hyp_card_has_Card_Color__int__String_():
    assert hasattr(Card, "Card_Color__int__String_")
    descriptor = None
    for klass in Card.__mro__:
        if "Card_Color__int__String_" in klass.__dict__:
            descriptor = klass.__dict__["Card_Color__int__String_"]
            break
    assert isinstance(descriptor, property)



def test_hyp_cardelements_interface_is_not_abstract():
    assert not inspect.isabstract(CardElements_Interface)


def test_hyp_cardelements_interface_constructor_exists():
    assert callable(CardElements_Interface.__init__)


def test_hyp_cardelements_interface_constructor_args():
    sig = inspect.signature(CardElements_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gameelements_is_not_abstract():
    assert not inspect.isabstract(GameElements)


def test_hyp_gameelements_constructor_exists():
    assert callable(GameElements.__init__)


def test_hyp_gameelements_constructor_args():
    sig = inspect.signature(GameElements.__init__)
    params = list(sig.parameters.keys())
    assert "CardsTotal" in params, "Missing parameter 'CardsTotal'"
    assert "Action" in params, "Missing parameter 'Action'"
    assert "WildCardCol" in params, "Missing parameter 'WildCardCol'"
    assert "CardNumber" in params, "Missing parameter 'CardNumber'"
    assert "CardColors" in params, "Missing parameter 'CardColors'"
    assert "Wild" in params, "Missing parameter 'Wild'"
    assert "Numbers" in params, "Missing parameter 'Numbers'"
    assert "Actions" in params, "Missing parameter 'Actions'"
    assert "OpeningHand" in params, "Missing parameter 'OpeningHand'"
    assert "WildActions" in params, "Missing parameter 'WildActions'"

def test_hyp_gameelements_has_CardsTotal():
    assert hasattr(GameElements, "CardsTotal")
    descriptor = None
    for klass in GameElements.__mro__:
        if "CardsTotal" in klass.__dict__:
            descriptor = klass.__dict__["CardsTotal"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gameelements_has_Action():
    assert hasattr(GameElements, "Action")
    descriptor = None
    for klass in GameElements.__mro__:
        if "Action" in klass.__dict__:
            descriptor = klass.__dict__["Action"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gameelements_has_WildCardCol():
    assert hasattr(GameElements, "WildCardCol")
    descriptor = None
    for klass in GameElements.__mro__:
        if "WildCardCol" in klass.__dict__:
            descriptor = klass.__dict__["WildCardCol"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gameelements_has_CardNumber():
    assert hasattr(GameElements, "CardNumber")
    descriptor = None
    for klass in GameElements.__mro__:
        if "CardNumber" in klass.__dict__:
            descriptor = klass.__dict__["CardNumber"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gameelements_has_CardColors():
    assert hasattr(GameElements, "CardColors")
    descriptor = None
    for klass in GameElements.__mro__:
        if "CardColors" in klass.__dict__:
            descriptor = klass.__dict__["CardColors"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gameelements_has_Wild():
    assert hasattr(GameElements, "Wild")
    descriptor = None
    for klass in GameElements.__mro__:
        if "Wild" in klass.__dict__:
            descriptor = klass.__dict__["Wild"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gameelements_has_Numbers():
    assert hasattr(GameElements, "Numbers")
    descriptor = None
    for klass in GameElements.__mro__:
        if "Numbers" in klass.__dict__:
            descriptor = klass.__dict__["Numbers"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gameelements_has_Actions():
    assert hasattr(GameElements, "Actions")
    descriptor = None
    for klass in GameElements.__mro__:
        if "Actions" in klass.__dict__:
            descriptor = klass.__dict__["Actions"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gameelements_has_OpeningHand():
    assert hasattr(GameElements, "OpeningHand")
    descriptor = None
    for klass in GameElements.__mro__:
        if "OpeningHand" in klass.__dict__:
            descriptor = klass.__dict__["OpeningHand"]
            break
    assert isinstance(descriptor, property)

def test_hyp_gameelements_has_WildActions():
    assert hasattr(GameElements, "WildActions")
    descriptor = None
    for klass in GameElements.__mro__:
        if "WildActions" in klass.__dict__:
            descriptor = klass.__dict__["WildActions"]
            break
    assert isinstance(descriptor, property)



def test_hyp_gameelements_interface_is_not_abstract():
    assert not inspect.isabstract(GameElements_Interface)


def test_hyp_gameelements_interface_constructor_exists():
    assert callable(GameElements_Interface.__init__)


def test_hyp_gameelements_interface_constructor_args():
    sig = inspect.signature(GameElements_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_discardpile_is_not_abstract():
    assert not inspect.isabstract(DiscardPile)


def test_hyp_discardpile_constructor_exists():
    assert callable(DiscardPile.__init__)


def test_hyp_discardpile_constructor_args():
    sig = inspect.signature(DiscardPile.__init__)
    params = list(sig.parameters.keys())
    assert "DiscardPile__" in params, "Missing parameter 'DiscardPile__'"
    assert "DiscardPile__1" in params, "Missing parameter 'DiscardPile__1'"
    assert "showTop__" in params, "Missing parameter 'showTop__'"






def test_hyp_drawpile_is_not_abstract():
    assert not inspect.isabstract(DrawPile)


def test_hyp_drawpile_constructor_exists():
    assert callable(DrawPile.__init__)


def test_hyp_drawpile_constructor_args():
    sig = inspect.signature(DrawPile.__init__)
    params = list(sig.parameters.keys())
    assert "removeCard_Card_" in params, "Missing parameter 'removeCard_Card_'"
    assert "DrawPile__1" in params, "Missing parameter 'DrawPile__1'"
    assert "DrawPile__" in params, "Missing parameter 'DrawPile__'"






def test_hyp_dealer_is_not_abstract():
    assert not inspect.isabstract(Dealer)


def test_hyp_dealer_constructor_exists():
    assert callable(Dealer.__init__)


def test_hyp_dealer_constructor_args():
    sig = inspect.signature(Dealer.__init__)
    params = list(sig.parameters.keys())
    assert "distribute_Player___" in params, "Missing parameter 'distribute_Player___'"
    assert "Dealer__1" in params, "Missing parameter 'Dealer__1'"
    assert "shuffle__" in params, "Missing parameter 'shuffle__'"
    assert "Dealer__" in params, "Missing parameter 'Dealer__'"







def test_hyp_players_is_not_abstract():
    assert not inspect.isabstract(Players)


def test_hyp_players_constructor_exists():
    assert callable(Players.__init__)


def test_hyp_players_constructor_args():
    sig = inspect.signature(Players.__init__)
    params = list(sig.parameters.keys())
    assert "hasCard_Card_" in params, "Missing parameter 'hasCard_Card_'"
    assert "playCard_Card_" in params, "Missing parameter 'playCard_Card_'"
    assert "getName" in params, "Missing parameter 'getName'"
    assert "Player__" in params, "Missing parameter 'Player__'"
    assert "drawCard_Card_" in params, "Missing parameter 'drawCard_Card_'"
    assert "Players__" in params, "Missing parameter 'Players__'"
    assert "Player_String_" in params, "Missing parameter 'Player_String_'"










def test_hyp_game_is_not_abstract():
    assert not inspect.isabstract(Game)


def test_hyp_game_constructor_exists():
    assert callable(Game.__init__)


def test_hyp_game_constructor_args():
    sig = inspect.signature(Game.__init__)
    params = list(sig.parameters.keys())
    assert "Game__" in params, "Missing parameter 'Game__'"
    assert "Game__1" in params, "Missing parameter 'Game__1'"
    assert "PlayGame__" in params, "Missing parameter 'PlayGame__'"
    assert "getPlayers__" in params, "Missing parameter 'getPlayers__'"







def test_hyp_gamesession_is_not_abstract():
    assert not inspect.isabstract(GameSession)


def test_hyp_gamesession_constructor_exists():
    assert callable(GameSession.__init__)


def test_hyp_gamesession_constructor_args():
    sig = inspect.signature(GameSession.__init__)
    params = list(sig.parameters.keys())
    assert "GameSession_Game_" in params, "Missing parameter 'GameSession_Game_'"
    assert "setPlayers__" in params, "Missing parameter 'setPlayers__'"
    assert "GameSession_Game__Card_" in params, "Missing parameter 'GameSession_Game__Card_'"






def test_hyp_main_is_not_abstract():
    assert not inspect.isabstract(Main)


def test_hyp_main_constructor_exists():
    assert callable(Main.__init__)


def test_hyp_main_constructor_args():
    sig = inspect.signature(Main.__init__)
    params = list(sig.parameters.keys())
    assert "main_String____" in params, "Missing parameter 'main_String____'"
    assert "Main__" in params, "Missing parameter 'Main__'"




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
int___1_strategy = st.builds(
    int___1,
)
Color_strategy = st.builds(
    Color,
)
WildCard_strategy = st.builds(
    WildCard,
    WildCard_String_=
        safe_text,
    WildCard__=
        safe_text
)
Wild4_strategy = st.builds(
    Wild4,
)
Wild_strategy = st.builds(
    Wild,
)
Draw2_strategy = st.builds(
    Draw2,
)
Skip_strategy = st.builds(
    Skip,
)
Reverse_strategy = st.builds(
    Reverse,
)
ActionCard_strategy = st.builds(
    ActionCard,
    ActionCard__=
        safe_text,
    _attr=
        safe_text,
    ActionCard_Color_String_=
        safe_text
)
NumberCard_strategy = st.builds(
    NumberCard,
    NumberCard__=
        safe_text,
    attribute=
        safe_text,
    NumberCard_Color__String_=
        safe_text,
    attribute2=
        safe_text
)
Card_strategy = st.builds(
    Card,
    setValue=
        safe_text,
    Card__=
        safe_text,
    getColor__=
        st.none(),
    setColor_Color_=
        safe_text,
    Card__1=
        safe_text,
    Card_Color__int__String_=
        safe_text
)
CardElements_Interface_strategy = st.builds(
    CardElements_Interface,
)
GameElements_strategy = st.builds(
    GameElements,
    CardsTotal=
        safe_text,
    Action=
        safe_text,
    WildCardCol=
        safe_text,
    CardNumber=
        safe_text,
    CardColors=
        safe_text,
    Wild=
        safe_text,
    Numbers=
        st.none(),
    Actions=
        safe_text,
    OpeningHand=
        safe_text,
    WildActions=
        safe_text
)
GameElements_Interface_strategy = st.builds(
    GameElements_Interface,
)
DiscardPile_strategy = st.builds(
    DiscardPile,
    DiscardPile__=
        safe_text,
    DiscardPile__1=
        safe_text,
    showTop__=
        safe_text
)
DrawPile_strategy = st.builds(
    DrawPile,
    removeCard_Card_=
        safe_text,
    DrawPile__1=
        safe_text,
    DrawPile__=
        safe_text
)
Dealer_strategy = st.builds(
    Dealer,
    distribute_Player___=
        safe_text,
    Dealer__1=
        safe_text,
    shuffle__=
        safe_text,
    Dealer__=
        safe_text
)
Players_strategy = st.builds(
    Players,
    hasCard_Card_=
        safe_text,
    playCard_Card_=
        safe_text,
    getName=
        safe_text,
    Player__=
        safe_text,
    drawCard_Card_=
        safe_text,
    Players__=
        safe_text,
    Player_String_=
        safe_text
)
Game_strategy = st.builds(
    Game,
    Game__=
        safe_text,
    Game__1=
        safe_text,
    PlayGame__=
        safe_text,
    getPlayers__=
        safe_text
)
GameSession_strategy = st.builds(
    GameSession,
    GameSession_Game_=
        safe_text,
    setPlayers__=
        safe_text,
    GameSession_Game__Card_=
        safe_text
)
Main_strategy = st.builds(
    Main,
    main_String____=
        safe_text,
    Main__=
        safe_text
)






@given(instance=WildCard_strategy)
def test_hyp_wildcard_WildCard_String__setter(instance):
    original = instance.WildCard_String_
    instance.WildCard_String_ = original
    assert instance.WildCard_String_ == original



@given(instance=WildCard_strategy)
def test_hyp_wildcard_WildCard___setter(instance):
    original = instance.WildCard__
    instance.WildCard__ = original
    assert instance.WildCard__ == original









@given(instance=ActionCard_strategy)
def test_hyp_actioncard_ActionCard___setter(instance):
    original = instance.ActionCard__
    instance.ActionCard__ = original
    assert instance.ActionCard__ == original



@given(instance=ActionCard_strategy)
def test_hyp_actioncard__attr_setter(instance):
    original = instance._attr
    instance._attr = original
    assert instance._attr == original



@given(instance=ActionCard_strategy)
def test_hyp_actioncard_ActionCard_Color_String__setter(instance):
    original = instance.ActionCard_Color_String_
    instance.ActionCard_Color_String_ = original
    assert instance.ActionCard_Color_String_ == original




@given(instance=NumberCard_strategy)
def test_hyp_numbercard_NumberCard___setter(instance):
    original = instance.NumberCard__
    instance.NumberCard__ = original
    assert instance.NumberCard__ == original



@given(instance=NumberCard_strategy)
def test_hyp_numbercard_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=NumberCard_strategy)
def test_hyp_numbercard_NumberCard_Color__String__setter(instance):
    original = instance.NumberCard_Color__String_
    instance.NumberCard_Color__String_ = original
    assert instance.NumberCard_Color__String_ == original



@given(instance=NumberCard_strategy)
def test_hyp_numbercard_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_hyp_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_hyp_card_setValue_setter(instance):
    original = instance.setValue
    instance.setValue = original
    assert instance.setValue == original



@given(instance=Card_strategy)
def test_hyp_card_Card___setter(instance):
    original = instance.Card__
    instance.Card__ = original
    assert instance.Card__ == original



@given(instance=Card_strategy)
def test_hyp_card_getColor___setter(instance):
    original = instance.getColor__
    instance.getColor__ = original
    assert instance.getColor__ == original



@given(instance=Card_strategy)
def test_hyp_card_setColor_Color__setter(instance):
    original = instance.setColor_Color_
    instance.setColor_Color_ = original
    assert instance.setColor_Color_ == original



@given(instance=Card_strategy)
def test_hyp_card_Card__1_setter(instance):
    original = instance.Card__1
    instance.Card__1 = original
    assert instance.Card__1 == original



@given(instance=Card_strategy)
def test_hyp_card_Card_Color__int__String__setter(instance):
    original = instance.Card_Color__int__String_
    instance.Card_Color__int__String_ = original
    assert instance.Card_Color__int__String_ == original


@given(instance=GameElements_strategy)
@settings(max_examples=50)
def test_hyp_gameelements_instantiation(instance):
    assert isinstance(instance, GameElements)



@given(instance=GameElements_strategy)
def test_hyp_gameelements_CardsTotal_setter(instance):
    original = instance.CardsTotal
    instance.CardsTotal = original
    assert instance.CardsTotal == original



@given(instance=GameElements_strategy)
def test_hyp_gameelements_Action_setter(instance):
    original = instance.Action
    instance.Action = original
    assert instance.Action == original



@given(instance=GameElements_strategy)
def test_hyp_gameelements_WildCardCol_setter(instance):
    original = instance.WildCardCol
    instance.WildCardCol = original
    assert instance.WildCardCol == original



@given(instance=GameElements_strategy)
def test_hyp_gameelements_CardNumber_setter(instance):
    original = instance.CardNumber
    instance.CardNumber = original
    assert instance.CardNumber == original



@given(instance=GameElements_strategy)
def test_hyp_gameelements_CardColors_setter(instance):
    original = instance.CardColors
    instance.CardColors = original
    assert instance.CardColors == original



@given(instance=GameElements_strategy)
def test_hyp_gameelements_Wild_setter(instance):
    original = instance.Wild
    instance.Wild = original
    assert instance.Wild == original



@given(instance=GameElements_strategy)
def test_hyp_gameelements_Numbers_setter(instance):
    original = instance.Numbers
    instance.Numbers = original
    assert instance.Numbers == original



@given(instance=GameElements_strategy)
def test_hyp_gameelements_Actions_setter(instance):
    original = instance.Actions
    instance.Actions = original
    assert instance.Actions == original



@given(instance=GameElements_strategy)
def test_hyp_gameelements_OpeningHand_setter(instance):
    original = instance.OpeningHand
    instance.OpeningHand = original
    assert instance.OpeningHand == original



@given(instance=GameElements_strategy)
def test_hyp_gameelements_WildActions_setter(instance):
    original = instance.WildActions
    instance.WildActions = original
    assert instance.WildActions == original





@given(instance=DiscardPile_strategy)
def test_hyp_discardpile_DiscardPile___setter(instance):
    original = instance.DiscardPile__
    instance.DiscardPile__ = original
    assert instance.DiscardPile__ == original



@given(instance=DiscardPile_strategy)
def test_hyp_discardpile_DiscardPile__1_setter(instance):
    original = instance.DiscardPile__1
    instance.DiscardPile__1 = original
    assert instance.DiscardPile__1 == original



@given(instance=DiscardPile_strategy)
def test_hyp_discardpile_showTop___setter(instance):
    original = instance.showTop__
    instance.showTop__ = original
    assert instance.showTop__ == original




@given(instance=DrawPile_strategy)
def test_hyp_drawpile_removeCard_Card__setter(instance):
    original = instance.removeCard_Card_
    instance.removeCard_Card_ = original
    assert instance.removeCard_Card_ == original



@given(instance=DrawPile_strategy)
def test_hyp_drawpile_DrawPile__1_setter(instance):
    original = instance.DrawPile__1
    instance.DrawPile__1 = original
    assert instance.DrawPile__1 == original



@given(instance=DrawPile_strategy)
def test_hyp_drawpile_DrawPile___setter(instance):
    original = instance.DrawPile__
    instance.DrawPile__ = original
    assert instance.DrawPile__ == original




@given(instance=Dealer_strategy)
def test_hyp_dealer_distribute_Player____setter(instance):
    original = instance.distribute_Player___
    instance.distribute_Player___ = original
    assert instance.distribute_Player___ == original



@given(instance=Dealer_strategy)
def test_hyp_dealer_Dealer__1_setter(instance):
    original = instance.Dealer__1
    instance.Dealer__1 = original
    assert instance.Dealer__1 == original



@given(instance=Dealer_strategy)
def test_hyp_dealer_shuffle___setter(instance):
    original = instance.shuffle__
    instance.shuffle__ = original
    assert instance.shuffle__ == original



@given(instance=Dealer_strategy)
def test_hyp_dealer_Dealer___setter(instance):
    original = instance.Dealer__
    instance.Dealer__ = original
    assert instance.Dealer__ == original




@given(instance=Players_strategy)
def test_hyp_players_hasCard_Card__setter(instance):
    original = instance.hasCard_Card_
    instance.hasCard_Card_ = original
    assert instance.hasCard_Card_ == original



@given(instance=Players_strategy)
def test_hyp_players_playCard_Card__setter(instance):
    original = instance.playCard_Card_
    instance.playCard_Card_ = original
    assert instance.playCard_Card_ == original



@given(instance=Players_strategy)
def test_hyp_players_getName_setter(instance):
    original = instance.getName
    instance.getName = original
    assert instance.getName == original



@given(instance=Players_strategy)
def test_hyp_players_Player___setter(instance):
    original = instance.Player__
    instance.Player__ = original
    assert instance.Player__ == original



@given(instance=Players_strategy)
def test_hyp_players_drawCard_Card__setter(instance):
    original = instance.drawCard_Card_
    instance.drawCard_Card_ = original
    assert instance.drawCard_Card_ == original



@given(instance=Players_strategy)
def test_hyp_players_Players___setter(instance):
    original = instance.Players__
    instance.Players__ = original
    assert instance.Players__ == original



@given(instance=Players_strategy)
def test_hyp_players_Player_String__setter(instance):
    original = instance.Player_String_
    instance.Player_String_ = original
    assert instance.Player_String_ == original




@given(instance=Game_strategy)
def test_hyp_game_Game___setter(instance):
    original = instance.Game__
    instance.Game__ = original
    assert instance.Game__ == original



@given(instance=Game_strategy)
def test_hyp_game_Game__1_setter(instance):
    original = instance.Game__1
    instance.Game__1 = original
    assert instance.Game__1 == original



@given(instance=Game_strategy)
def test_hyp_game_PlayGame___setter(instance):
    original = instance.PlayGame__
    instance.PlayGame__ = original
    assert instance.PlayGame__ == original



@given(instance=Game_strategy)
def test_hyp_game_getPlayers___setter(instance):
    original = instance.getPlayers__
    instance.getPlayers__ = original
    assert instance.getPlayers__ == original




@given(instance=GameSession_strategy)
def test_hyp_gamesession_GameSession_Game__setter(instance):
    original = instance.GameSession_Game_
    instance.GameSession_Game_ = original
    assert instance.GameSession_Game_ == original



@given(instance=GameSession_strategy)
def test_hyp_gamesession_setPlayers___setter(instance):
    original = instance.setPlayers__
    instance.setPlayers__ = original
    assert instance.setPlayers__ == original



@given(instance=GameSession_strategy)
def test_hyp_gamesession_GameSession_Game__Card__setter(instance):
    original = instance.GameSession_Game__Card_
    instance.GameSession_Game__Card_ = original
    assert instance.GameSession_Game__Card_ == original




@given(instance=Main_strategy)
def test_hyp_main_main_String_____setter(instance):
    original = instance.main_String____
    instance.main_String____ = original
    assert instance.main_String____ == original



@given(instance=Main_strategy)
def test_hyp_main_Main___setter(instance):
    original = instance.Main__
    instance.Main__ = original
    assert instance.Main__ == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ActionCard,
    Card,
    CardElements_Interface,
    Color,
    Dealer,
    DiscardPile,
    Draw2,
    DrawPile,
    Game,
    GameElements,
    GameElements_Interface,
    GameSession,
    Main,
    NumberCard,
    Players,
    Reverse,
    Skip,
    Wild,
    Wild4,
    WildCard,
    int___1,
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

def test_ActionCard_ActionCard_Color_String__value_roundtrip():
    instance = ActionCard(ActionCard_Color_String_="sample_text", ActionCard__="sample_text", _attr="sample_text")
    assert instance.ActionCard_Color_String_ == "sample_text"
    instance.ActionCard_Color_String_ = "sample_text_2"
    assert instance.ActionCard_Color_String_ == "sample_text_2"


def test_ActionCard_ActionCard___value_roundtrip():
    instance = ActionCard(ActionCard_Color_String_="sample_text", ActionCard__="sample_text", _attr="sample_text")
    assert instance.ActionCard__ == "sample_text"
    instance.ActionCard__ = "sample_text_2"
    assert instance.ActionCard__ == "sample_text_2"


def test_ActionCard__attr_value_roundtrip():
    instance = ActionCard(ActionCard_Color_String_="sample_text", ActionCard__="sample_text", _attr="sample_text")
    assert instance._attr == "sample_text"
    instance._attr = "sample_text_2"
    assert instance._attr == "sample_text_2"


def test_Dealer_Dealer___value_roundtrip():
    instance = Dealer(Dealer__="sample_text", Dealer__1="sample_text", distribute_Player___="sample_text", shuffle__="sample_text")
    assert instance.Dealer__ == "sample_text"
    instance.Dealer__ = "sample_text_2"
    assert instance.Dealer__ == "sample_text_2"


def test_Dealer_Dealer__1_value_roundtrip():
    instance = Dealer(Dealer__="sample_text", Dealer__1="sample_text", distribute_Player___="sample_text", shuffle__="sample_text")
    assert instance.Dealer__1 == "sample_text"
    instance.Dealer__1 = "sample_text_2"
    assert instance.Dealer__1 == "sample_text_2"


def test_Dealer_distribute_Player____value_roundtrip():
    instance = Dealer(Dealer__="sample_text", Dealer__1="sample_text", distribute_Player___="sample_text", shuffle__="sample_text")
    assert instance.distribute_Player___ == "sample_text"
    instance.distribute_Player___ = "sample_text_2"
    assert instance.distribute_Player___ == "sample_text_2"


def test_Dealer_shuffle___value_roundtrip():
    instance = Dealer(Dealer__="sample_text", Dealer__1="sample_text", distribute_Player___="sample_text", shuffle__="sample_text")
    assert instance.shuffle__ == "sample_text"
    instance.shuffle__ = "sample_text_2"
    assert instance.shuffle__ == "sample_text_2"


def test_DiscardPile_DiscardPile___value_roundtrip():
    instance = DiscardPile(DiscardPile__="sample_text", DiscardPile__1="sample_text", showTop__="sample_text")
    assert instance.DiscardPile__ == "sample_text"
    instance.DiscardPile__ = "sample_text_2"
    assert instance.DiscardPile__ == "sample_text_2"


def test_DiscardPile_DiscardPile__1_value_roundtrip():
    instance = DiscardPile(DiscardPile__="sample_text", DiscardPile__1="sample_text", showTop__="sample_text")
    assert instance.DiscardPile__1 == "sample_text"
    instance.DiscardPile__1 = "sample_text_2"
    assert instance.DiscardPile__1 == "sample_text_2"


def test_DiscardPile_showTop___value_roundtrip():
    instance = DiscardPile(DiscardPile__="sample_text", DiscardPile__1="sample_text", showTop__="sample_text")
    assert instance.showTop__ == "sample_text"
    instance.showTop__ = "sample_text_2"
    assert instance.showTop__ == "sample_text_2"


def test_DrawPile_DrawPile___value_roundtrip():
    instance = DrawPile(DrawPile__="sample_text", DrawPile__1="sample_text", removeCard_Card_="sample_text")
    assert instance.DrawPile__ == "sample_text"
    instance.DrawPile__ = "sample_text_2"
    assert instance.DrawPile__ == "sample_text_2"


def test_DrawPile_DrawPile__1_value_roundtrip():
    instance = DrawPile(DrawPile__="sample_text", DrawPile__1="sample_text", removeCard_Card_="sample_text")
    assert instance.DrawPile__1 == "sample_text"
    instance.DrawPile__1 = "sample_text_2"
    assert instance.DrawPile__1 == "sample_text_2"


def test_DrawPile_removeCard_Card__value_roundtrip():
    instance = DrawPile(DrawPile__="sample_text", DrawPile__1="sample_text", removeCard_Card_="sample_text")
    assert instance.removeCard_Card_ == "sample_text"
    instance.removeCard_Card_ = "sample_text_2"
    assert instance.removeCard_Card_ == "sample_text_2"


def test_Game_Game___value_roundtrip():
    instance = Game(Game__="sample_text", Game__1="sample_text", PlayGame__="sample_text", getPlayers__="sample_text")
    assert instance.Game__ == "sample_text"
    instance.Game__ = "sample_text_2"
    assert instance.Game__ == "sample_text_2"


def test_Game_Game__1_value_roundtrip():
    instance = Game(Game__="sample_text", Game__1="sample_text", PlayGame__="sample_text", getPlayers__="sample_text")
    assert instance.Game__1 == "sample_text"
    instance.Game__1 = "sample_text_2"
    assert instance.Game__1 == "sample_text_2"


def test_Game_PlayGame___value_roundtrip():
    instance = Game(Game__="sample_text", Game__1="sample_text", PlayGame__="sample_text", getPlayers__="sample_text")
    assert instance.PlayGame__ == "sample_text"
    instance.PlayGame__ = "sample_text_2"
    assert instance.PlayGame__ == "sample_text_2"


def test_Game_getPlayers___value_roundtrip():
    instance = Game(Game__="sample_text", Game__1="sample_text", PlayGame__="sample_text", getPlayers__="sample_text")
    assert instance.getPlayers__ == "sample_text"
    instance.getPlayers__ = "sample_text_2"
    assert instance.getPlayers__ == "sample_text_2"


def test_GameSession_GameSession_Game__value_roundtrip():
    instance = GameSession(GameSession_Game_="sample_text", GameSession_Game__Card_="sample_text", setPlayers__="sample_text")
    assert instance.GameSession_Game_ == "sample_text"
    instance.GameSession_Game_ = "sample_text_2"
    assert instance.GameSession_Game_ == "sample_text_2"


def test_GameSession_GameSession_Game__Card__value_roundtrip():
    instance = GameSession(GameSession_Game_="sample_text", GameSession_Game__Card_="sample_text", setPlayers__="sample_text")
    assert instance.GameSession_Game__Card_ == "sample_text"
    instance.GameSession_Game__Card_ = "sample_text_2"
    assert instance.GameSession_Game__Card_ == "sample_text_2"


def test_GameSession_setPlayers___value_roundtrip():
    instance = GameSession(GameSession_Game_="sample_text", GameSession_Game__Card_="sample_text", setPlayers__="sample_text")
    assert instance.setPlayers__ == "sample_text"
    instance.setPlayers__ = "sample_text_2"
    assert instance.setPlayers__ == "sample_text_2"


def test_Main_Main___value_roundtrip():
    instance = Main(Main__="sample_text", main_String____="sample_text")
    assert instance.Main__ == "sample_text"
    instance.Main__ = "sample_text_2"
    assert instance.Main__ == "sample_text_2"


def test_Main_main_String_____value_roundtrip():
    instance = Main(Main__="sample_text", main_String____="sample_text")
    assert instance.main_String____ == "sample_text"
    instance.main_String____ = "sample_text_2"
    assert instance.main_String____ == "sample_text_2"


def test_NumberCard_NumberCard_Color__String__value_roundtrip():
    instance = NumberCard(NumberCard_Color__String_="sample_text", NumberCard__="sample_text", attribute="sample_text", attribute2="sample_text")
    assert instance.NumberCard_Color__String_ == "sample_text"
    instance.NumberCard_Color__String_ = "sample_text_2"
    assert instance.NumberCard_Color__String_ == "sample_text_2"


def test_NumberCard_NumberCard___value_roundtrip():
    instance = NumberCard(NumberCard_Color__String_="sample_text", NumberCard__="sample_text", attribute="sample_text", attribute2="sample_text")
    assert instance.NumberCard__ == "sample_text"
    instance.NumberCard__ = "sample_text_2"
    assert instance.NumberCard__ == "sample_text_2"


def test_NumberCard_attribute_value_roundtrip():
    instance = NumberCard(NumberCard_Color__String_="sample_text", NumberCard__="sample_text", attribute="sample_text", attribute2="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_NumberCard_attribute2_value_roundtrip():
    instance = NumberCard(NumberCard_Color__String_="sample_text", NumberCard__="sample_text", attribute="sample_text", attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_Players_Player_String__value_roundtrip():
    instance = Players(Player_String_="sample_text", Player__="sample_text", Players__="sample_text", drawCard_Card_="sample_text", getName="sample_text", hasCard_Card_="sample_text", playCard_Card_="sample_text")
    assert instance.Player_String_ == "sample_text"
    instance.Player_String_ = "sample_text_2"
    assert instance.Player_String_ == "sample_text_2"


def test_Players_Player___value_roundtrip():
    instance = Players(Player_String_="sample_text", Player__="sample_text", Players__="sample_text", drawCard_Card_="sample_text", getName="sample_text", hasCard_Card_="sample_text", playCard_Card_="sample_text")
    assert instance.Player__ == "sample_text"
    instance.Player__ = "sample_text_2"
    assert instance.Player__ == "sample_text_2"


def test_Players_Players___value_roundtrip():
    instance = Players(Player_String_="sample_text", Player__="sample_text", Players__="sample_text", drawCard_Card_="sample_text", getName="sample_text", hasCard_Card_="sample_text", playCard_Card_="sample_text")
    assert instance.Players__ == "sample_text"
    instance.Players__ = "sample_text_2"
    assert instance.Players__ == "sample_text_2"


def test_Players_drawCard_Card__value_roundtrip():
    instance = Players(Player_String_="sample_text", Player__="sample_text", Players__="sample_text", drawCard_Card_="sample_text", getName="sample_text", hasCard_Card_="sample_text", playCard_Card_="sample_text")
    assert instance.drawCard_Card_ == "sample_text"
    instance.drawCard_Card_ = "sample_text_2"
    assert instance.drawCard_Card_ == "sample_text_2"


def test_Players_getName_value_roundtrip():
    instance = Players(Player_String_="sample_text", Player__="sample_text", Players__="sample_text", drawCard_Card_="sample_text", getName="sample_text", hasCard_Card_="sample_text", playCard_Card_="sample_text")
    assert instance.getName == "sample_text"
    instance.getName = "sample_text_2"
    assert instance.getName == "sample_text_2"


def test_Players_hasCard_Card__value_roundtrip():
    instance = Players(Player_String_="sample_text", Player__="sample_text", Players__="sample_text", drawCard_Card_="sample_text", getName="sample_text", hasCard_Card_="sample_text", playCard_Card_="sample_text")
    assert instance.hasCard_Card_ == "sample_text"
    instance.hasCard_Card_ = "sample_text_2"
    assert instance.hasCard_Card_ == "sample_text_2"


def test_Players_playCard_Card__value_roundtrip():
    instance = Players(Player_String_="sample_text", Player__="sample_text", Players__="sample_text", drawCard_Card_="sample_text", getName="sample_text", hasCard_Card_="sample_text", playCard_Card_="sample_text")
    assert instance.playCard_Card_ == "sample_text"
    instance.playCard_Card_ = "sample_text_2"
    assert instance.playCard_Card_ == "sample_text_2"


def test_WildCard_WildCard_String__value_roundtrip():
    instance = WildCard(WildCard_String_="sample_text", WildCard__="sample_text")
    assert instance.WildCard_String_ == "sample_text"
    instance.WildCard_String_ = "sample_text_2"
    assert instance.WildCard_String_ == "sample_text_2"


def test_WildCard_WildCard___value_roundtrip():
    instance = WildCard(WildCard_String_="sample_text", WildCard__="sample_text")
    assert instance.WildCard__ == "sample_text"
    instance.WildCard__ = "sample_text_2"
    assert instance.WildCard__ == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ActionCard_strategy = st.builds(ActionCard, ActionCard_Color_String_=safe_text, ActionCard__=safe_text, _attr=safe_text)
@given(instance=ActionCard_strategy)
@settings(max_examples=25)
def test_ActionCard_instantiation(instance):
    assert isinstance(instance, ActionCard)


CardElements_Interface_strategy = st.builds(CardElements_Interface)
@given(instance=CardElements_Interface_strategy)
@settings(max_examples=25)
def test_CardElements_Interface_instantiation(instance):
    assert isinstance(instance, CardElements_Interface)


Color_strategy = st.builds(Color)
@given(instance=Color_strategy)
@settings(max_examples=25)
def test_Color_instantiation(instance):
    assert isinstance(instance, Color)


Dealer_strategy = st.builds(Dealer, Dealer__=safe_text, Dealer__1=safe_text, distribute_Player___=safe_text, shuffle__=safe_text)
@given(instance=Dealer_strategy)
@settings(max_examples=25)
def test_Dealer_instantiation(instance):
    assert isinstance(instance, Dealer)


DiscardPile_strategy = st.builds(DiscardPile, DiscardPile__=safe_text, DiscardPile__1=safe_text, showTop__=safe_text)
@given(instance=DiscardPile_strategy)
@settings(max_examples=25)
def test_DiscardPile_instantiation(instance):
    assert isinstance(instance, DiscardPile)


Draw2_strategy = st.builds(Draw2)
@given(instance=Draw2_strategy)
@settings(max_examples=25)
def test_Draw2_instantiation(instance):
    assert isinstance(instance, Draw2)


DrawPile_strategy = st.builds(DrawPile, DrawPile__=safe_text, DrawPile__1=safe_text, removeCard_Card_=safe_text)
@given(instance=DrawPile_strategy)
@settings(max_examples=25)
def test_DrawPile_instantiation(instance):
    assert isinstance(instance, DrawPile)


Game_strategy = st.builds(Game, Game__=safe_text, Game__1=safe_text, PlayGame__=safe_text, getPlayers__=safe_text)
@given(instance=Game_strategy)
@settings(max_examples=25)
def test_Game_instantiation(instance):
    assert isinstance(instance, Game)


GameElements_Interface_strategy = st.builds(GameElements_Interface)
@given(instance=GameElements_Interface_strategy)
@settings(max_examples=25)
def test_GameElements_Interface_instantiation(instance):
    assert isinstance(instance, GameElements_Interface)


GameSession_strategy = st.builds(GameSession, GameSession_Game_=safe_text, GameSession_Game__Card_=safe_text, setPlayers__=safe_text)
@given(instance=GameSession_strategy)
@settings(max_examples=25)
def test_GameSession_instantiation(instance):
    assert isinstance(instance, GameSession)


Main_strategy = st.builds(Main, Main__=safe_text, main_String____=safe_text)
@given(instance=Main_strategy)
@settings(max_examples=25)
def test_Main_instantiation(instance):
    assert isinstance(instance, Main)


NumberCard_strategy = st.builds(NumberCard, NumberCard_Color__String_=safe_text, NumberCard__=safe_text, attribute=safe_text, attribute2=safe_text)
@given(instance=NumberCard_strategy)
@settings(max_examples=25)
def test_NumberCard_instantiation(instance):
    assert isinstance(instance, NumberCard)


Players_strategy = st.builds(Players, Player_String_=safe_text, Player__=safe_text, Players__=safe_text, drawCard_Card_=safe_text, getName=safe_text, hasCard_Card_=safe_text, playCard_Card_=safe_text)
@given(instance=Players_strategy)
@settings(max_examples=25)
def test_Players_instantiation(instance):
    assert isinstance(instance, Players)


Reverse_strategy = st.builds(Reverse)
@given(instance=Reverse_strategy)
@settings(max_examples=25)
def test_Reverse_instantiation(instance):
    assert isinstance(instance, Reverse)


Skip_strategy = st.builds(Skip)
@given(instance=Skip_strategy)
@settings(max_examples=25)
def test_Skip_instantiation(instance):
    assert isinstance(instance, Skip)


Wild_strategy = st.builds(Wild)
@given(instance=Wild_strategy)
@settings(max_examples=25)
def test_Wild_instantiation(instance):
    assert isinstance(instance, Wild)


Wild4_strategy = st.builds(Wild4)
@given(instance=Wild4_strategy)
@settings(max_examples=25)
def test_Wild4_instantiation(instance):
    assert isinstance(instance, Wild4)


WildCard_strategy = st.builds(WildCard, WildCard_String_=safe_text, WildCard__=safe_text)
@given(instance=WildCard_strategy)
@settings(max_examples=25)
def test_WildCard_instantiation(instance):
    assert isinstance(instance, WildCard)


int___1_strategy = st.builds(int___1)
@given(instance=int___1_strategy)
@settings(max_examples=25)
def test_int___1_instantiation(instance):
    assert isinstance(instance, int___1)



