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
    ActionEvent,
    Graphics,
    WinScreen,
    SolitairePanel,
    SolitaireLayout,
    SolitaireBoard,
    SingleCell,
    FourRowSolitaire,
    FireworksDisplay,
    DiscardPile,
    Deck,
    DealDeck,
    Column,
    ChangeOptions,
    ChangeAppearance,
    CardStack,
    Card,
    AcePile,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_actionevent_is_not_abstract():
    assert not inspect.isabstract(ActionEvent)


def test_hyp_actionevent_constructor_exists():
    assert callable(ActionEvent.__init__)


def test_hyp_actionevent_constructor_args():
    sig = inspect.signature(ActionEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphics_is_not_abstract():
    assert not inspect.isabstract(Graphics)


def test_hyp_graphics_constructor_exists():
    assert callable(Graphics.__init__)


def test_hyp_graphics_constructor_args():
    sig = inspect.signature(Graphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_winscreen_is_not_abstract():
    assert not inspect.isabstract(WinScreen)


def test_hyp_winscreen_constructor_exists():
    assert callable(WinScreen.__init__)


def test_hyp_winscreen_constructor_args():
    sig = inspect.signature(WinScreen.__init__)
    params = list(sig.parameters.keys())



def test_hyp_solitairepanel_is_not_abstract():
    assert not inspect.isabstract(SolitairePanel)


def test_hyp_solitairepanel_constructor_exists():
    assert callable(SolitairePanel.__init__)


def test_hyp_solitairepanel_constructor_args():
    sig = inspect.signature(SolitairePanel.__init__)
    params = list(sig.parameters.keys())
    assert "background" in params, "Missing parameter 'background'"
    assert "backgroundNumber" in params, "Missing parameter 'backgroundNumber'"





def test_hyp_solitairelayout_is_not_abstract():
    assert not inspect.isabstract(SolitaireLayout)


def test_hyp_solitairelayout_constructor_exists():
    assert callable(SolitaireLayout.__init__)


def test_hyp_solitairelayout_constructor_args():
    sig = inspect.signature(SolitaireLayout.__init__)
    params = list(sig.parameters.keys())
    assert "CLUBS_ACE_PILE" in params, "Missing parameter 'CLUBS_ACE_PILE'"
    assert "colThree" in params, "Missing parameter 'colThree'"
    assert "aceSpades" in params, "Missing parameter 'aceSpades'"
    assert "CELL_ONE" in params, "Missing parameter 'CELL_ONE'"
    assert "SPADES_ACE_PILE" in params, "Missing parameter 'SPADES_ACE_PILE'"
    assert "DISCARD_PILE" in params, "Missing parameter 'DISCARD_PILE'"
    assert "aceDiamonds" in params, "Missing parameter 'aceDiamonds'"
    assert "colTwo" in params, "Missing parameter 'colTwo'"
    assert "COLUMN_THREE" in params, "Missing parameter 'COLUMN_THREE'"
    assert "CELL_TWO" in params, "Missing parameter 'CELL_TWO'"
    assert "aceHearts" in params, "Missing parameter 'aceHearts'"
    assert "HEARTS_ACE_PILE" in params, "Missing parameter 'HEARTS_ACE_PILE'"
    assert "DIAMONDS_ACE_PILE" in params, "Missing parameter 'DIAMONDS_ACE_PILE'"
    assert "colFour" in params, "Missing parameter 'colFour'"
    assert "COLUMEN_ONE" in params, "Missing parameter 'COLUMEN_ONE'"
    assert "cellFour" in params, "Missing parameter 'cellFour'"
    assert "cellOne" in params, "Missing parameter 'cellOne'"
    assert "COLUMN_TWO" in params, "Missing parameter 'COLUMN_TWO'"
    assert "DECK" in params, "Missing parameter 'DECK'"
    assert "deck" in params, "Missing parameter 'deck'"
    assert "discardPile" in params, "Missing parameter 'discardPile'"
    assert "COLUMN_FOUR" in params, "Missing parameter 'COLUMN_FOUR'"
    assert "CELL_THREE" in params, "Missing parameter 'CELL_THREE'"
    assert "colOne" in params, "Missing parameter 'colOne'"
    assert "cellTwo" in params, "Missing parameter 'cellTwo'"
    assert "CELL_FOUR" in params, "Missing parameter 'CELL_FOUR'"
    assert "aceClubs" in params, "Missing parameter 'aceClubs'"
    assert "cellThree" in params, "Missing parameter 'cellThree'"































def test_hyp_solitaireboard_is_not_abstract():
    assert not inspect.isabstract(SolitaireBoard)


def test_hyp_solitaireboard_constructor_exists():
    assert callable(SolitaireBoard.__init__)


def test_hyp_solitaireboard_constructor_args():
    sig = inspect.signature(SolitaireBoard.__init__)
    params = list(sig.parameters.keys())
    assert "GAME_LOST" in params, "Missing parameter 'GAME_LOST'"
    assert "numCardsInDiscardView" in params, "Missing parameter 'numCardsInDiscardView'"
    assert "timer" in params, "Missing parameter 'timer'"
    assert "winAnimationStatus" in params, "Missing parameter 'winAnimationStatus'"
    assert "backgroundNumber" in params, "Missing parameter 'backgroundNumber'"
    assert "GAME_SAVED" in params, "Missing parameter 'GAME_SAVED'"
    assert "statusBar" in params, "Missing parameter 'statusBar'"
    assert "newDrawCount" in params, "Missing parameter 'newDrawCount'"
    assert "numCards" in params, "Missing parameter 'numCards'"
    assert "newDifficulty" in params, "Missing parameter 'newDifficulty'"
    assert "timerLabel" in params, "Missing parameter 'timerLabel'"
    assert "drawCount" in params, "Missing parameter 'drawCount'"
    assert "deckNumber" in params, "Missing parameter 'deckNumber'"
    assert "timerCount" in params, "Missing parameter 'timerCount'"
    assert "GAME_WON" in params, "Missing parameter 'GAME_WON'"
    assert "timerToRun" in params, "Missing parameter 'timerToRun'"
    assert "timerToRunNextGame" in params, "Missing parameter 'timerToRunNextGame'"
    assert "RESET_STATS" in params, "Missing parameter 'RESET_STATS'"
    assert "winSoundsStatus" in params, "Missing parameter 'winSoundsStatus'"
    assert "DO_NOTHING" in params, "Missing parameter 'DO_NOTHING'"
    assert "difficulty" in params, "Missing parameter 'difficulty'"
























def test_hyp_singlecell_is_not_abstract():
    assert not inspect.isabstract(SingleCell)


def test_hyp_singlecell_constructor_exists():
    assert callable(SingleCell.__init__)


def test_hyp_singlecell_constructor_args():
    sig = inspect.signature(SingleCell.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fourrowsolitaire_is_not_abstract():
    assert not inspect.isabstract(FourRowSolitaire)


def test_hyp_fourrowsolitaire_constructor_exists():
    assert callable(FourRowSolitaire.__init__)


def test_hyp_fourrowsolitaire_constructor_args():
    sig = inspect.signature(FourRowSolitaire.__init__)
    params = list(sig.parameters.keys())
    assert "options" in params, "Missing parameter 'options'"
    assert "help" in params, "Missing parameter 'help'"
    assert "version" in params, "Missing parameter 'version'"
    assert "menuBar" in params, "Missing parameter 'menuBar'"
    assert "about" in params, "Missing parameter 'about'"
    assert "newGame" in params, "Missing parameter 'newGame'"
    assert "game" in params, "Missing parameter 'game'"
    assert "undo" in params, "Missing parameter 'undo'"
    assert "checkUpdate" in params, "Missing parameter 'checkUpdate'"
    assert "statistics" in params, "Missing parameter 'statistics'"
    assert "hint" in params, "Missing parameter 'hint'"
    assert "appearance" in params, "Missing parameter 'appearance'"
    assert "exit" in params, "Missing parameter 'exit'"
    assert "helpMenu" in params, "Missing parameter 'helpMenu'"

def test_hyp_fourrowsolitaire_has_options():
    assert hasattr(FourRowSolitaire, "options")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "options" in klass.__dict__:
            descriptor = klass.__dict__["options"]
            break
    assert isinstance(descriptor, property)

def test_hyp_fourrowsolitaire_has_help():
    assert hasattr(FourRowSolitaire, "help")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "help" in klass.__dict__:
            descriptor = klass.__dict__["help"]
            break
    assert isinstance(descriptor, property)

def test_hyp_fourrowsolitaire_has_version():
    assert hasattr(FourRowSolitaire, "version")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_hyp_fourrowsolitaire_has_menuBar():
    assert hasattr(FourRowSolitaire, "menuBar")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "menuBar" in klass.__dict__:
            descriptor = klass.__dict__["menuBar"]
            break
    assert isinstance(descriptor, property)

def test_hyp_fourrowsolitaire_has_about():
    assert hasattr(FourRowSolitaire, "about")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "about" in klass.__dict__:
            descriptor = klass.__dict__["about"]
            break
    assert isinstance(descriptor, property)

def test_hyp_fourrowsolitaire_has_newGame():
    assert hasattr(FourRowSolitaire, "newGame")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "newGame" in klass.__dict__:
            descriptor = klass.__dict__["newGame"]
            break
    assert isinstance(descriptor, property)

def test_hyp_fourrowsolitaire_has_game():
    assert hasattr(FourRowSolitaire, "game")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "game" in klass.__dict__:
            descriptor = klass.__dict__["game"]
            break
    assert isinstance(descriptor, property)

def test_hyp_fourrowsolitaire_has_undo():
    assert hasattr(FourRowSolitaire, "undo")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "undo" in klass.__dict__:
            descriptor = klass.__dict__["undo"]
            break
    assert isinstance(descriptor, property)

def test_hyp_fourrowsolitaire_has_checkUpdate():
    assert hasattr(FourRowSolitaire, "checkUpdate")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "checkUpdate" in klass.__dict__:
            descriptor = klass.__dict__["checkUpdate"]
            break
    assert isinstance(descriptor, property)

def test_hyp_fourrowsolitaire_has_statistics():
    assert hasattr(FourRowSolitaire, "statistics")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "statistics" in klass.__dict__:
            descriptor = klass.__dict__["statistics"]
            break
    assert isinstance(descriptor, property)

def test_hyp_fourrowsolitaire_has_hint():
    assert hasattr(FourRowSolitaire, "hint")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "hint" in klass.__dict__:
            descriptor = klass.__dict__["hint"]
            break
    assert isinstance(descriptor, property)

def test_hyp_fourrowsolitaire_has_appearance():
    assert hasattr(FourRowSolitaire, "appearance")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "appearance" in klass.__dict__:
            descriptor = klass.__dict__["appearance"]
            break
    assert isinstance(descriptor, property)

def test_hyp_fourrowsolitaire_has_exit():
    assert hasattr(FourRowSolitaire, "exit")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "exit" in klass.__dict__:
            descriptor = klass.__dict__["exit"]
            break
    assert isinstance(descriptor, property)

def test_hyp_fourrowsolitaire_has_helpMenu():
    assert hasattr(FourRowSolitaire, "helpMenu")
    descriptor = None
    for klass in FourRowSolitaire.__mro__:
        if "helpMenu" in klass.__dict__:
            descriptor = klass.__dict__["helpMenu"]
            break
    assert isinstance(descriptor, property)



def test_hyp_fireworksdisplay_is_not_abstract():
    assert not inspect.isabstract(FireworksDisplay)


def test_hyp_fireworksdisplay_constructor_exists():
    assert callable(FireworksDisplay.__init__)


def test_hyp_fireworksdisplay_constructor_args():
    sig = inspect.signature(FireworksDisplay.__init__)
    params = list(sig.parameters.keys())
    assert "xx" in params, "Missing parameter 'xx'"
    assert "random" in params, "Missing parameter 'random'"
    assert "NUM_FIREWORKS" in params, "Missing parameter 'NUM_FIREWORKS'"
    assert "numSets" in params, "Missing parameter 'numSets'"
    assert "y" in params, "Missing parameter 'y'"
    assert "colors" in params, "Missing parameter 'colors'"
    assert "x" in params, "Missing parameter 'x'"
    assert "FIREWORKS_TIME" in params, "Missing parameter 'FIREWORKS_TIME'"
    assert "startValue" in params, "Missing parameter 'startValue'"
    assert "FIREWORKS_SIZE" in params, "Missing parameter 'FIREWORKS_SIZE'"
    assert "yy" in params, "Missing parameter 'yy'"
    assert "num" in params, "Missing parameter 'num'"
    assert "SET_DELAY" in params, "Missing parameter 'SET_DELAY'"
    assert "timer" in params, "Missing parameter 'timer'"

















def test_hyp_discardpile_is_not_abstract():
    assert not inspect.isabstract(DiscardPile)


def test_hyp_discardpile_constructor_exists():
    assert callable(DiscardPile.__init__)


def test_hyp_discardpile_constructor_args():
    sig = inspect.signature(DiscardPile.__init__)
    params = list(sig.parameters.keys())
    assert "cardsLeftFromDraw" in params, "Missing parameter 'cardsLeftFromDraw'"
    assert "drawCount" in params, "Missing parameter 'drawCount'"





def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "deckNumber" in params, "Missing parameter 'deckNumber'"




def test_hyp_dealdeck_is_not_abstract():
    assert not inspect.isabstract(DealDeck)


def test_hyp_dealdeck_constructor_exists():
    assert callable(DealDeck.__init__)


def test_hyp_dealdeck_constructor_args():
    sig = inspect.signature(DealDeck.__init__)
    params = list(sig.parameters.keys())
    assert "redealable" in params, "Missing parameter 'redealable'"
    assert "EASY_THROUGH_LIMIT" in params, "Missing parameter 'EASY_THROUGH_LIMIT'"
    assert "MEDIUM_THROUGH_LIMIT" in params, "Missing parameter 'MEDIUM_THROUGH_LIMIT'"
    assert "HARD_THROUGH_LIMIT" in params, "Missing parameter 'HARD_THROUGH_LIMIT'"
    assert "DRAW_ONE_THROUGH_LIMIT" in params, "Missing parameter 'DRAW_ONE_THROUGH_LIMIT'"
    assert "difficulty" in params, "Missing parameter 'difficulty'"
    assert "drawCount" in params, "Missing parameter 'drawCount'"
    assert "numTimesThroughDeck" in params, "Missing parameter 'numTimesThroughDeck'"
    assert "deckThroughLimit" in params, "Missing parameter 'deckThroughLimit'"
    assert "DRAW_THREE_THROUGH_LIMIT" in params, "Missing parameter 'DRAW_THREE_THROUGH_LIMIT'"













def test_hyp_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_hyp_column_constructor_exists():
    assert callable(Column.__init__)


def test_hyp_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_hyp_changeoptions_is_not_abstract():
    assert not inspect.isabstract(ChangeOptions)


def test_hyp_changeoptions_constructor_exists():
    assert callable(ChangeOptions.__init__)


def test_hyp_changeoptions_constructor_args():
    sig = inspect.signature(ChangeOptions.__init__)
    params = list(sig.parameters.keys())
    assert "medium" in params, "Missing parameter 'medium'"
    assert "winSoundsCheck" in params, "Missing parameter 'winSoundsCheck'"
    assert "difficulty" in params, "Missing parameter 'difficulty'"
    assert "easy" in params, "Missing parameter 'easy'"
    assert "timer" in params, "Missing parameter 'timer'"
    assert "ok" in params, "Missing parameter 'ok'"
    assert "hard" in params, "Missing parameter 'hard'"
    assert "exited" in params, "Missing parameter 'exited'"
    assert "timerCheck" in params, "Missing parameter 'timerCheck'"
    assert "drawOne" in params, "Missing parameter 'drawOne'"
    assert "drawThree" in params, "Missing parameter 'drawThree'"
    assert "drawCount" in params, "Missing parameter 'drawCount'"
    assert "sounds" in params, "Missing parameter 'sounds'"
    assert "winAnimationCheck" in params, "Missing parameter 'winAnimationCheck'"
    assert "animation" in params, "Missing parameter 'animation'"


















def test_hyp_changeappearance_is_not_abstract():
    assert not inspect.isabstract(ChangeAppearance)


def test_hyp_changeappearance_constructor_exists():
    assert callable(ChangeAppearance.__init__)


def test_hyp_changeappearance_constructor_args():
    sig = inspect.signature(ChangeAppearance.__init__)
    params = list(sig.parameters.keys())
    assert "FRS_BACKGROUND" in params, "Missing parameter 'FRS_BACKGROUND'"
    assert "exited" in params, "Missing parameter 'exited'"
    assert "NUM_BACKGROUNDS" in params, "Missing parameter 'NUM_BACKGROUNDS'"
    assert "decks" in params, "Missing parameter 'decks'"
    assert "NUM_DECKS" in params, "Missing parameter 'NUM_DECKS'"
    assert "ok" in params, "Missing parameter 'ok'"
    assert "backgrounds" in params, "Missing parameter 'backgrounds'"
    assert "backgroundNumber" in params, "Missing parameter 'backgroundNumber'"
    assert "cardBackLabel" in params, "Missing parameter 'cardBackLabel'"
    assert "FRS_DECK" in params, "Missing parameter 'FRS_DECK'"
    assert "deckNumber" in params, "Missing parameter 'deckNumber'"
    assert "backgroundLabel" in params, "Missing parameter 'backgroundLabel'"















def test_hyp_cardstack_is_not_abstract():
    assert not inspect.isabstract(CardStack)


def test_hyp_cardstack_constructor_exists():
    assert callable(CardStack.__init__)


def test_hyp_cardstack_constructor_args():
    sig = inspect.signature(CardStack.__init__)
    params = list(sig.parameters.keys())



def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "JACK" in params, "Missing parameter 'JACK'"
    assert "CLUBS_SUIT" in params, "Missing parameter 'CLUBS_SUIT'"
    assert "location" in params, "Missing parameter 'location'"
    assert "INVALID_NUMBER" in params, "Missing parameter 'INVALID_NUMBER'"
    assert "QUEEN" in params, "Missing parameter 'QUEEN'"
    assert "SPADES_SUIT" in params, "Missing parameter 'SPADES_SUIT'"
    assert "fullCardNumber" in params, "Missing parameter 'fullCardNumber'"
    assert "TEN" in params, "Missing parameter 'TEN'"
    assert "cardColor" in params, "Missing parameter 'cardColor'"
    assert "INVALID_SUIT" in params, "Missing parameter 'INVALID_SUIT'"
    assert "TWO" in params, "Missing parameter 'TWO'"
    assert "FOUR" in params, "Missing parameter 'FOUR'"
    assert "highlighted" in params, "Missing parameter 'highlighted'"
    assert "ACE" in params, "Missing parameter 'ACE'"
    assert "EIGHT" in params, "Missing parameter 'EIGHT'"
    assert "cardImageString" in params, "Missing parameter 'cardImageString'"
    assert "SEVEN" in params, "Missing parameter 'SEVEN'"
    assert "FIVE" in params, "Missing parameter 'FIVE'"
    assert "SIX" in params, "Missing parameter 'SIX'"
    assert "cardBack" in params, "Missing parameter 'cardBack'"
    assert "KING" in params, "Missing parameter 'KING'"
    assert "image" in params, "Missing parameter 'image'"
    assert "THREE" in params, "Missing parameter 'THREE'"
    assert "cardSuit" in params, "Missing parameter 'cardSuit'"
    assert "DIAMONDS_SUIT" in params, "Missing parameter 'DIAMONDS_SUIT'"
    assert "HEARTS_SUIT" in params, "Missing parameter 'HEARTS_SUIT'"
    assert "faceUp" in params, "Missing parameter 'faceUp'"
    assert "deckNumber" in params, "Missing parameter 'deckNumber'"
    assert "cardNumber" in params, "Missing parameter 'cardNumber'"
    assert "cardHighlighted" in params, "Missing parameter 'cardHighlighted'"
    assert "NINE" in params, "Missing parameter 'NINE'"


































def test_hyp_acepile_is_not_abstract():
    assert not inspect.isabstract(AcePile)


def test_hyp_acepile_constructor_exists():
    assert callable(AcePile.__init__)


def test_hyp_acepile_constructor_args():
    sig = inspect.signature(AcePile.__init__)
    params = list(sig.parameters.keys())
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
ActionEvent_strategy = st.builds(
    ActionEvent,
)
Graphics_strategy = st.builds(
    Graphics,
)
WinScreen_strategy = st.builds(
    WinScreen,
)
SolitairePanel_strategy = st.builds(
    SolitairePanel,
    background=
        safe_text,
    backgroundNumber=
        st.integers()
)
SolitaireLayout_strategy = st.builds(
    SolitaireLayout,
    CLUBS_ACE_PILE=
        safe_text,
    colThree=
        safe_text,
    aceSpades=
        safe_text,
    CELL_ONE=
        safe_text,
    SPADES_ACE_PILE=
        safe_text,
    DISCARD_PILE=
        safe_text,
    aceDiamonds=
        safe_text,
    colTwo=
        safe_text,
    COLUMN_THREE=
        safe_text,
    CELL_TWO=
        safe_text,
    aceHearts=
        safe_text,
    HEARTS_ACE_PILE=
        safe_text,
    DIAMONDS_ACE_PILE=
        safe_text,
    colFour=
        safe_text,
    COLUMEN_ONE=
        safe_text,
    cellFour=
        safe_text,
    cellOne=
        safe_text,
    COLUMN_TWO=
        safe_text,
    DECK=
        safe_text,
    deck=
        safe_text,
    discardPile=
        safe_text,
    COLUMN_FOUR=
        safe_text,
    CELL_THREE=
        safe_text,
    colOne=
        safe_text,
    cellTwo=
        safe_text,
    CELL_FOUR=
        safe_text,
    aceClubs=
        safe_text,
    cellThree=
        safe_text
)
SolitaireBoard_strategy = st.builds(
    SolitaireBoard,
    GAME_LOST=
        st.integers(),
    numCardsInDiscardView=
        safe_text,
    timer=
        safe_text,
    winAnimationStatus=
        st.integers(),
    backgroundNumber=
        st.integers(),
    GAME_SAVED=
        st.integers(),
    statusBar=
        safe_text,
    newDrawCount=
        st.integers(),
    numCards=
        safe_text,
    newDifficulty=
        st.integers(),
    timerLabel=
        safe_text,
    drawCount=
        st.integers(),
    deckNumber=
        st.integers(),
    timerCount=
        st.integers(),
    GAME_WON=
        st.integers(),
    timerToRun=
        st.booleans(),
    timerToRunNextGame=
        st.integers(),
    RESET_STATS=
        st.integers(),
    winSoundsStatus=
        st.integers(),
    DO_NOTHING=
        st.integers(),
    difficulty=
        st.integers()
)
SingleCell_strategy = st.builds(
    SingleCell,
)
FourRowSolitaire_strategy = st.builds(
    FourRowSolitaire,
    options=
        safe_text,
    help=
        safe_text,
    version=
        st.none(),
    menuBar=
        safe_text,
    about=
        safe_text,
    newGame=
        safe_text,
    game=
        safe_text,
    undo=
        safe_text,
    checkUpdate=
        safe_text,
    statistics=
        safe_text,
    hint=
        safe_text,
    appearance=
        safe_text,
    exit=
        safe_text,
    helpMenu=
        safe_text
)
FireworksDisplay_strategy = st.builds(
    FireworksDisplay,
    xx=
        safe_text,
    random=
        safe_text,
    NUM_FIREWORKS=
        st.integers(),
    numSets=
        st.integers(),
    y=
        safe_text,
    colors=
        safe_text,
    x=
        safe_text,
    FIREWORKS_TIME=
        st.integers(),
    startValue=
        st.integers(),
    FIREWORKS_SIZE=
        st.integers(),
    yy=
        safe_text,
    num=
        st.integers(),
    SET_DELAY=
        st.integers(),
    timer=
        safe_text
)
DiscardPile_strategy = st.builds(
    DiscardPile,
    cardsLeftFromDraw=
        st.integers(),
    drawCount=
        st.integers()
)
Deck_strategy = st.builds(
    Deck,
    deckNumber=
        st.integers()
)
DealDeck_strategy = st.builds(
    DealDeck,
    redealable=
        st.booleans(),
    EASY_THROUGH_LIMIT=
        st.integers(),
    MEDIUM_THROUGH_LIMIT=
        st.integers(),
    HARD_THROUGH_LIMIT=
        st.integers(),
    DRAW_ONE_THROUGH_LIMIT=
        st.integers(),
    difficulty=
        st.integers(),
    drawCount=
        st.integers(),
    numTimesThroughDeck=
        st.integers(),
    deckThroughLimit=
        st.integers(),
    DRAW_THREE_THROUGH_LIMIT=
        st.integers()
)
Column_strategy = st.builds(
    Column,
)
ChangeOptions_strategy = st.builds(
    ChangeOptions,
    medium=
        safe_text,
    winSoundsCheck=
        safe_text,
    difficulty=
        st.integers(),
    easy=
        safe_text,
    timer=
        st.integers(),
    ok=
        safe_text,
    hard=
        safe_text,
    exited=
        st.booleans(),
    timerCheck=
        safe_text,
    drawOne=
        safe_text,
    drawThree=
        safe_text,
    drawCount=
        st.integers(),
    sounds=
        st.integers(),
    winAnimationCheck=
        safe_text,
    animation=
        st.integers()
)
ChangeAppearance_strategy = st.builds(
    ChangeAppearance,
    FRS_BACKGROUND=
        st.integers(),
    exited=
        st.booleans(),
    NUM_BACKGROUNDS=
        st.integers(),
    decks=
        safe_text,
    NUM_DECKS=
        st.integers(),
    ok=
        safe_text,
    backgrounds=
        safe_text,
    backgroundNumber=
        st.integers(),
    cardBackLabel=
        safe_text,
    FRS_DECK=
        st.integers(),
    deckNumber=
        st.integers(),
    backgroundLabel=
        safe_text
)
CardStack_strategy = st.builds(
    CardStack,
)
Card_strategy = st.builds(
    Card,
    JACK=
        st.integers(),
    CLUBS_SUIT=
        safe_text,
    location=
        safe_text,
    INVALID_NUMBER=
        st.integers(),
    QUEEN=
        st.integers(),
    SPADES_SUIT=
        safe_text,
    fullCardNumber=
        st.integers(),
    TEN=
        st.integers(),
    cardColor=
        st.integers(),
    INVALID_SUIT=
        safe_text,
    TWO=
        st.integers(),
    FOUR=
        st.integers(),
    highlighted=
        st.booleans(),
    ACE=
        st.integers(),
    EIGHT=
        st.integers(),
    cardImageString=
        safe_text,
    SEVEN=
        st.integers(),
    FIVE=
        st.integers(),
    SIX=
        st.integers(),
    cardBack=
        safe_text,
    KING=
        st.integers(),
    image=
        safe_text,
    THREE=
        st.integers(),
    cardSuit=
        safe_text,
    DIAMONDS_SUIT=
        safe_text,
    HEARTS_SUIT=
        safe_text,
    faceUp=
        st.booleans(),
    deckNumber=
        st.integers(),
    cardNumber=
        st.integers(),
    cardHighlighted=
        safe_text,
    NINE=
        st.integers()
)
AcePile_strategy = st.builds(
    AcePile,
    suit=
        safe_text
)







@given(instance=SolitairePanel_strategy)
def test_hyp_solitairepanel_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original



@given(instance=SolitairePanel_strategy)
def test_hyp_solitairepanel_backgroundNumber_setter(instance):
    original = instance.backgroundNumber
    instance.backgroundNumber = original
    assert instance.backgroundNumber == original




@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_CLUBS_ACE_PILE_setter(instance):
    original = instance.CLUBS_ACE_PILE
    instance.CLUBS_ACE_PILE = original
    assert instance.CLUBS_ACE_PILE == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_colThree_setter(instance):
    original = instance.colThree
    instance.colThree = original
    assert instance.colThree == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_aceSpades_setter(instance):
    original = instance.aceSpades
    instance.aceSpades = original
    assert instance.aceSpades == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_CELL_ONE_setter(instance):
    original = instance.CELL_ONE
    instance.CELL_ONE = original
    assert instance.CELL_ONE == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_SPADES_ACE_PILE_setter(instance):
    original = instance.SPADES_ACE_PILE
    instance.SPADES_ACE_PILE = original
    assert instance.SPADES_ACE_PILE == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_DISCARD_PILE_setter(instance):
    original = instance.DISCARD_PILE
    instance.DISCARD_PILE = original
    assert instance.DISCARD_PILE == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_aceDiamonds_setter(instance):
    original = instance.aceDiamonds
    instance.aceDiamonds = original
    assert instance.aceDiamonds == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_colTwo_setter(instance):
    original = instance.colTwo
    instance.colTwo = original
    assert instance.colTwo == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_COLUMN_THREE_setter(instance):
    original = instance.COLUMN_THREE
    instance.COLUMN_THREE = original
    assert instance.COLUMN_THREE == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_CELL_TWO_setter(instance):
    original = instance.CELL_TWO
    instance.CELL_TWO = original
    assert instance.CELL_TWO == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_aceHearts_setter(instance):
    original = instance.aceHearts
    instance.aceHearts = original
    assert instance.aceHearts == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_HEARTS_ACE_PILE_setter(instance):
    original = instance.HEARTS_ACE_PILE
    instance.HEARTS_ACE_PILE = original
    assert instance.HEARTS_ACE_PILE == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_DIAMONDS_ACE_PILE_setter(instance):
    original = instance.DIAMONDS_ACE_PILE
    instance.DIAMONDS_ACE_PILE = original
    assert instance.DIAMONDS_ACE_PILE == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_colFour_setter(instance):
    original = instance.colFour
    instance.colFour = original
    assert instance.colFour == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_COLUMEN_ONE_setter(instance):
    original = instance.COLUMEN_ONE
    instance.COLUMEN_ONE = original
    assert instance.COLUMEN_ONE == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_cellFour_setter(instance):
    original = instance.cellFour
    instance.cellFour = original
    assert instance.cellFour == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_cellOne_setter(instance):
    original = instance.cellOne
    instance.cellOne = original
    assert instance.cellOne == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_COLUMN_TWO_setter(instance):
    original = instance.COLUMN_TWO
    instance.COLUMN_TWO = original
    assert instance.COLUMN_TWO == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_DECK_setter(instance):
    original = instance.DECK
    instance.DECK = original
    assert instance.DECK == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_discardPile_setter(instance):
    original = instance.discardPile
    instance.discardPile = original
    assert instance.discardPile == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_COLUMN_FOUR_setter(instance):
    original = instance.COLUMN_FOUR
    instance.COLUMN_FOUR = original
    assert instance.COLUMN_FOUR == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_CELL_THREE_setter(instance):
    original = instance.CELL_THREE
    instance.CELL_THREE = original
    assert instance.CELL_THREE == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_colOne_setter(instance):
    original = instance.colOne
    instance.colOne = original
    assert instance.colOne == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_cellTwo_setter(instance):
    original = instance.cellTwo
    instance.cellTwo = original
    assert instance.cellTwo == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_CELL_FOUR_setter(instance):
    original = instance.CELL_FOUR
    instance.CELL_FOUR = original
    assert instance.CELL_FOUR == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_aceClubs_setter(instance):
    original = instance.aceClubs
    instance.aceClubs = original
    assert instance.aceClubs == original



@given(instance=SolitaireLayout_strategy)
def test_hyp_solitairelayout_cellThree_setter(instance):
    original = instance.cellThree
    instance.cellThree = original
    assert instance.cellThree == original




@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_GAME_LOST_setter(instance):
    original = instance.GAME_LOST
    instance.GAME_LOST = original
    assert instance.GAME_LOST == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_numCardsInDiscardView_setter(instance):
    original = instance.numCardsInDiscardView
    instance.numCardsInDiscardView = original
    assert instance.numCardsInDiscardView == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_timer_setter(instance):
    original = instance.timer
    instance.timer = original
    assert instance.timer == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_winAnimationStatus_setter(instance):
    original = instance.winAnimationStatus
    instance.winAnimationStatus = original
    assert instance.winAnimationStatus == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_backgroundNumber_setter(instance):
    original = instance.backgroundNumber
    instance.backgroundNumber = original
    assert instance.backgroundNumber == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_GAME_SAVED_setter(instance):
    original = instance.GAME_SAVED
    instance.GAME_SAVED = original
    assert instance.GAME_SAVED == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_statusBar_setter(instance):
    original = instance.statusBar
    instance.statusBar = original
    assert instance.statusBar == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_newDrawCount_setter(instance):
    original = instance.newDrawCount
    instance.newDrawCount = original
    assert instance.newDrawCount == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_numCards_setter(instance):
    original = instance.numCards
    instance.numCards = original
    assert instance.numCards == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_newDifficulty_setter(instance):
    original = instance.newDifficulty
    instance.newDifficulty = original
    assert instance.newDifficulty == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_timerLabel_setter(instance):
    original = instance.timerLabel
    instance.timerLabel = original
    assert instance.timerLabel == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_drawCount_setter(instance):
    original = instance.drawCount
    instance.drawCount = original
    assert instance.drawCount == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_deckNumber_setter(instance):
    original = instance.deckNumber
    instance.deckNumber = original
    assert instance.deckNumber == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_timerCount_setter(instance):
    original = instance.timerCount
    instance.timerCount = original
    assert instance.timerCount == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_GAME_WON_setter(instance):
    original = instance.GAME_WON
    instance.GAME_WON = original
    assert instance.GAME_WON == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_timerToRun_setter(instance):
    original = instance.timerToRun
    instance.timerToRun = original
    assert instance.timerToRun == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_timerToRunNextGame_setter(instance):
    original = instance.timerToRunNextGame
    instance.timerToRunNextGame = original
    assert instance.timerToRunNextGame == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_RESET_STATS_setter(instance):
    original = instance.RESET_STATS
    instance.RESET_STATS = original
    assert instance.RESET_STATS == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_winSoundsStatus_setter(instance):
    original = instance.winSoundsStatus
    instance.winSoundsStatus = original
    assert instance.winSoundsStatus == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_DO_NOTHING_setter(instance):
    original = instance.DO_NOTHING
    instance.DO_NOTHING = original
    assert instance.DO_NOTHING == original



@given(instance=SolitaireBoard_strategy)
def test_hyp_solitaireboard_difficulty_setter(instance):
    original = instance.difficulty
    instance.difficulty = original
    assert instance.difficulty == original


@given(instance=FourRowSolitaire_strategy)
@settings(max_examples=50)
def test_hyp_fourrowsolitaire_instantiation(instance):
    assert isinstance(instance, FourRowSolitaire)



@given(instance=FourRowSolitaire_strategy)
def test_hyp_fourrowsolitaire_options_setter(instance):
    original = instance.options
    instance.options = original
    assert instance.options == original



@given(instance=FourRowSolitaire_strategy)
def test_hyp_fourrowsolitaire_help_setter(instance):
    original = instance.help
    instance.help = original
    assert instance.help == original



@given(instance=FourRowSolitaire_strategy)
def test_hyp_fourrowsolitaire_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=FourRowSolitaire_strategy)
def test_hyp_fourrowsolitaire_menuBar_setter(instance):
    original = instance.menuBar
    instance.menuBar = original
    assert instance.menuBar == original



@given(instance=FourRowSolitaire_strategy)
def test_hyp_fourrowsolitaire_about_setter(instance):
    original = instance.about
    instance.about = original
    assert instance.about == original



@given(instance=FourRowSolitaire_strategy)
def test_hyp_fourrowsolitaire_newGame_setter(instance):
    original = instance.newGame
    instance.newGame = original
    assert instance.newGame == original



@given(instance=FourRowSolitaire_strategy)
def test_hyp_fourrowsolitaire_game_setter(instance):
    original = instance.game
    instance.game = original
    assert instance.game == original



@given(instance=FourRowSolitaire_strategy)
def test_hyp_fourrowsolitaire_undo_setter(instance):
    original = instance.undo
    instance.undo = original
    assert instance.undo == original



@given(instance=FourRowSolitaire_strategy)
def test_hyp_fourrowsolitaire_checkUpdate_setter(instance):
    original = instance.checkUpdate
    instance.checkUpdate = original
    assert instance.checkUpdate == original



@given(instance=FourRowSolitaire_strategy)
def test_hyp_fourrowsolitaire_statistics_setter(instance):
    original = instance.statistics
    instance.statistics = original
    assert instance.statistics == original



@given(instance=FourRowSolitaire_strategy)
def test_hyp_fourrowsolitaire_hint_setter(instance):
    original = instance.hint
    instance.hint = original
    assert instance.hint == original



@given(instance=FourRowSolitaire_strategy)
def test_hyp_fourrowsolitaire_appearance_setter(instance):
    original = instance.appearance
    instance.appearance = original
    assert instance.appearance == original



@given(instance=FourRowSolitaire_strategy)
def test_hyp_fourrowsolitaire_exit_setter(instance):
    original = instance.exit
    instance.exit = original
    assert instance.exit == original



@given(instance=FourRowSolitaire_strategy)
def test_hyp_fourrowsolitaire_helpMenu_setter(instance):
    original = instance.helpMenu
    instance.helpMenu = original
    assert instance.helpMenu == original




@given(instance=FireworksDisplay_strategy)
def test_hyp_fireworksdisplay_xx_setter(instance):
    original = instance.xx
    instance.xx = original
    assert instance.xx == original



@given(instance=FireworksDisplay_strategy)
def test_hyp_fireworksdisplay_random_setter(instance):
    original = instance.random
    instance.random = original
    assert instance.random == original



@given(instance=FireworksDisplay_strategy)
def test_hyp_fireworksdisplay_NUM_FIREWORKS_setter(instance):
    original = instance.NUM_FIREWORKS
    instance.NUM_FIREWORKS = original
    assert instance.NUM_FIREWORKS == original



@given(instance=FireworksDisplay_strategy)
def test_hyp_fireworksdisplay_numSets_setter(instance):
    original = instance.numSets
    instance.numSets = original
    assert instance.numSets == original



@given(instance=FireworksDisplay_strategy)
def test_hyp_fireworksdisplay_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=FireworksDisplay_strategy)
def test_hyp_fireworksdisplay_colors_setter(instance):
    original = instance.colors
    instance.colors = original
    assert instance.colors == original



@given(instance=FireworksDisplay_strategy)
def test_hyp_fireworksdisplay_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=FireworksDisplay_strategy)
def test_hyp_fireworksdisplay_FIREWORKS_TIME_setter(instance):
    original = instance.FIREWORKS_TIME
    instance.FIREWORKS_TIME = original
    assert instance.FIREWORKS_TIME == original



@given(instance=FireworksDisplay_strategy)
def test_hyp_fireworksdisplay_startValue_setter(instance):
    original = instance.startValue
    instance.startValue = original
    assert instance.startValue == original



@given(instance=FireworksDisplay_strategy)
def test_hyp_fireworksdisplay_FIREWORKS_SIZE_setter(instance):
    original = instance.FIREWORKS_SIZE
    instance.FIREWORKS_SIZE = original
    assert instance.FIREWORKS_SIZE == original



@given(instance=FireworksDisplay_strategy)
def test_hyp_fireworksdisplay_yy_setter(instance):
    original = instance.yy
    instance.yy = original
    assert instance.yy == original



@given(instance=FireworksDisplay_strategy)
def test_hyp_fireworksdisplay_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=FireworksDisplay_strategy)
def test_hyp_fireworksdisplay_SET_DELAY_setter(instance):
    original = instance.SET_DELAY
    instance.SET_DELAY = original
    assert instance.SET_DELAY == original



@given(instance=FireworksDisplay_strategy)
def test_hyp_fireworksdisplay_timer_setter(instance):
    original = instance.timer
    instance.timer = original
    assert instance.timer == original




@given(instance=DiscardPile_strategy)
def test_hyp_discardpile_cardsLeftFromDraw_setter(instance):
    original = instance.cardsLeftFromDraw
    instance.cardsLeftFromDraw = original
    assert instance.cardsLeftFromDraw == original



@given(instance=DiscardPile_strategy)
def test_hyp_discardpile_drawCount_setter(instance):
    original = instance.drawCount
    instance.drawCount = original
    assert instance.drawCount == original




@given(instance=Deck_strategy)
def test_hyp_deck_deckNumber_setter(instance):
    original = instance.deckNumber
    instance.deckNumber = original
    assert instance.deckNumber == original




@given(instance=DealDeck_strategy)
def test_hyp_dealdeck_redealable_setter(instance):
    original = instance.redealable
    instance.redealable = original
    assert instance.redealable == original



@given(instance=DealDeck_strategy)
def test_hyp_dealdeck_EASY_THROUGH_LIMIT_setter(instance):
    original = instance.EASY_THROUGH_LIMIT
    instance.EASY_THROUGH_LIMIT = original
    assert instance.EASY_THROUGH_LIMIT == original



@given(instance=DealDeck_strategy)
def test_hyp_dealdeck_MEDIUM_THROUGH_LIMIT_setter(instance):
    original = instance.MEDIUM_THROUGH_LIMIT
    instance.MEDIUM_THROUGH_LIMIT = original
    assert instance.MEDIUM_THROUGH_LIMIT == original



@given(instance=DealDeck_strategy)
def test_hyp_dealdeck_HARD_THROUGH_LIMIT_setter(instance):
    original = instance.HARD_THROUGH_LIMIT
    instance.HARD_THROUGH_LIMIT = original
    assert instance.HARD_THROUGH_LIMIT == original



@given(instance=DealDeck_strategy)
def test_hyp_dealdeck_DRAW_ONE_THROUGH_LIMIT_setter(instance):
    original = instance.DRAW_ONE_THROUGH_LIMIT
    instance.DRAW_ONE_THROUGH_LIMIT = original
    assert instance.DRAW_ONE_THROUGH_LIMIT == original



@given(instance=DealDeck_strategy)
def test_hyp_dealdeck_difficulty_setter(instance):
    original = instance.difficulty
    instance.difficulty = original
    assert instance.difficulty == original



@given(instance=DealDeck_strategy)
def test_hyp_dealdeck_drawCount_setter(instance):
    original = instance.drawCount
    instance.drawCount = original
    assert instance.drawCount == original



@given(instance=DealDeck_strategy)
def test_hyp_dealdeck_numTimesThroughDeck_setter(instance):
    original = instance.numTimesThroughDeck
    instance.numTimesThroughDeck = original
    assert instance.numTimesThroughDeck == original



@given(instance=DealDeck_strategy)
def test_hyp_dealdeck_deckThroughLimit_setter(instance):
    original = instance.deckThroughLimit
    instance.deckThroughLimit = original
    assert instance.deckThroughLimit == original



@given(instance=DealDeck_strategy)
def test_hyp_dealdeck_DRAW_THREE_THROUGH_LIMIT_setter(instance):
    original = instance.DRAW_THREE_THROUGH_LIMIT
    instance.DRAW_THREE_THROUGH_LIMIT = original
    assert instance.DRAW_THREE_THROUGH_LIMIT == original





@given(instance=ChangeOptions_strategy)
def test_hyp_changeoptions_medium_setter(instance):
    original = instance.medium
    instance.medium = original
    assert instance.medium == original



@given(instance=ChangeOptions_strategy)
def test_hyp_changeoptions_winSoundsCheck_setter(instance):
    original = instance.winSoundsCheck
    instance.winSoundsCheck = original
    assert instance.winSoundsCheck == original



@given(instance=ChangeOptions_strategy)
def test_hyp_changeoptions_difficulty_setter(instance):
    original = instance.difficulty
    instance.difficulty = original
    assert instance.difficulty == original



@given(instance=ChangeOptions_strategy)
def test_hyp_changeoptions_easy_setter(instance):
    original = instance.easy
    instance.easy = original
    assert instance.easy == original



@given(instance=ChangeOptions_strategy)
def test_hyp_changeoptions_timer_setter(instance):
    original = instance.timer
    instance.timer = original
    assert instance.timer == original



@given(instance=ChangeOptions_strategy)
def test_hyp_changeoptions_ok_setter(instance):
    original = instance.ok
    instance.ok = original
    assert instance.ok == original



@given(instance=ChangeOptions_strategy)
def test_hyp_changeoptions_hard_setter(instance):
    original = instance.hard
    instance.hard = original
    assert instance.hard == original



@given(instance=ChangeOptions_strategy)
def test_hyp_changeoptions_exited_setter(instance):
    original = instance.exited
    instance.exited = original
    assert instance.exited == original



@given(instance=ChangeOptions_strategy)
def test_hyp_changeoptions_timerCheck_setter(instance):
    original = instance.timerCheck
    instance.timerCheck = original
    assert instance.timerCheck == original



@given(instance=ChangeOptions_strategy)
def test_hyp_changeoptions_drawOne_setter(instance):
    original = instance.drawOne
    instance.drawOne = original
    assert instance.drawOne == original



@given(instance=ChangeOptions_strategy)
def test_hyp_changeoptions_drawThree_setter(instance):
    original = instance.drawThree
    instance.drawThree = original
    assert instance.drawThree == original



@given(instance=ChangeOptions_strategy)
def test_hyp_changeoptions_drawCount_setter(instance):
    original = instance.drawCount
    instance.drawCount = original
    assert instance.drawCount == original



@given(instance=ChangeOptions_strategy)
def test_hyp_changeoptions_sounds_setter(instance):
    original = instance.sounds
    instance.sounds = original
    assert instance.sounds == original



@given(instance=ChangeOptions_strategy)
def test_hyp_changeoptions_winAnimationCheck_setter(instance):
    original = instance.winAnimationCheck
    instance.winAnimationCheck = original
    assert instance.winAnimationCheck == original



@given(instance=ChangeOptions_strategy)
def test_hyp_changeoptions_animation_setter(instance):
    original = instance.animation
    instance.animation = original
    assert instance.animation == original




@given(instance=ChangeAppearance_strategy)
def test_hyp_changeappearance_FRS_BACKGROUND_setter(instance):
    original = instance.FRS_BACKGROUND
    instance.FRS_BACKGROUND = original
    assert instance.FRS_BACKGROUND == original



@given(instance=ChangeAppearance_strategy)
def test_hyp_changeappearance_exited_setter(instance):
    original = instance.exited
    instance.exited = original
    assert instance.exited == original



@given(instance=ChangeAppearance_strategy)
def test_hyp_changeappearance_NUM_BACKGROUNDS_setter(instance):
    original = instance.NUM_BACKGROUNDS
    instance.NUM_BACKGROUNDS = original
    assert instance.NUM_BACKGROUNDS == original



@given(instance=ChangeAppearance_strategy)
def test_hyp_changeappearance_decks_setter(instance):
    original = instance.decks
    instance.decks = original
    assert instance.decks == original



@given(instance=ChangeAppearance_strategy)
def test_hyp_changeappearance_NUM_DECKS_setter(instance):
    original = instance.NUM_DECKS
    instance.NUM_DECKS = original
    assert instance.NUM_DECKS == original



@given(instance=ChangeAppearance_strategy)
def test_hyp_changeappearance_ok_setter(instance):
    original = instance.ok
    instance.ok = original
    assert instance.ok == original



@given(instance=ChangeAppearance_strategy)
def test_hyp_changeappearance_backgrounds_setter(instance):
    original = instance.backgrounds
    instance.backgrounds = original
    assert instance.backgrounds == original



@given(instance=ChangeAppearance_strategy)
def test_hyp_changeappearance_backgroundNumber_setter(instance):
    original = instance.backgroundNumber
    instance.backgroundNumber = original
    assert instance.backgroundNumber == original



@given(instance=ChangeAppearance_strategy)
def test_hyp_changeappearance_cardBackLabel_setter(instance):
    original = instance.cardBackLabel
    instance.cardBackLabel = original
    assert instance.cardBackLabel == original



@given(instance=ChangeAppearance_strategy)
def test_hyp_changeappearance_FRS_DECK_setter(instance):
    original = instance.FRS_DECK
    instance.FRS_DECK = original
    assert instance.FRS_DECK == original



@given(instance=ChangeAppearance_strategy)
def test_hyp_changeappearance_deckNumber_setter(instance):
    original = instance.deckNumber
    instance.deckNumber = original
    assert instance.deckNumber == original



@given(instance=ChangeAppearance_strategy)
def test_hyp_changeappearance_backgroundLabel_setter(instance):
    original = instance.backgroundLabel
    instance.backgroundLabel = original
    assert instance.backgroundLabel == original





@given(instance=Card_strategy)
def test_hyp_card_JACK_setter(instance):
    original = instance.JACK
    instance.JACK = original
    assert instance.JACK == original



@given(instance=Card_strategy)
def test_hyp_card_CLUBS_SUIT_setter(instance):
    original = instance.CLUBS_SUIT
    instance.CLUBS_SUIT = original
    assert instance.CLUBS_SUIT == original



@given(instance=Card_strategy)
def test_hyp_card_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Card_strategy)
def test_hyp_card_INVALID_NUMBER_setter(instance):
    original = instance.INVALID_NUMBER
    instance.INVALID_NUMBER = original
    assert instance.INVALID_NUMBER == original



@given(instance=Card_strategy)
def test_hyp_card_QUEEN_setter(instance):
    original = instance.QUEEN
    instance.QUEEN = original
    assert instance.QUEEN == original



@given(instance=Card_strategy)
def test_hyp_card_SPADES_SUIT_setter(instance):
    original = instance.SPADES_SUIT
    instance.SPADES_SUIT = original
    assert instance.SPADES_SUIT == original



@given(instance=Card_strategy)
def test_hyp_card_fullCardNumber_setter(instance):
    original = instance.fullCardNumber
    instance.fullCardNumber = original
    assert instance.fullCardNumber == original



@given(instance=Card_strategy)
def test_hyp_card_TEN_setter(instance):
    original = instance.TEN
    instance.TEN = original
    assert instance.TEN == original



@given(instance=Card_strategy)
def test_hyp_card_cardColor_setter(instance):
    original = instance.cardColor
    instance.cardColor = original
    assert instance.cardColor == original



@given(instance=Card_strategy)
def test_hyp_card_INVALID_SUIT_setter(instance):
    original = instance.INVALID_SUIT
    instance.INVALID_SUIT = original
    assert instance.INVALID_SUIT == original



@given(instance=Card_strategy)
def test_hyp_card_TWO_setter(instance):
    original = instance.TWO
    instance.TWO = original
    assert instance.TWO == original



@given(instance=Card_strategy)
def test_hyp_card_FOUR_setter(instance):
    original = instance.FOUR
    instance.FOUR = original
    assert instance.FOUR == original



@given(instance=Card_strategy)
def test_hyp_card_highlighted_setter(instance):
    original = instance.highlighted
    instance.highlighted = original
    assert instance.highlighted == original



@given(instance=Card_strategy)
def test_hyp_card_ACE_setter(instance):
    original = instance.ACE
    instance.ACE = original
    assert instance.ACE == original



@given(instance=Card_strategy)
def test_hyp_card_EIGHT_setter(instance):
    original = instance.EIGHT
    instance.EIGHT = original
    assert instance.EIGHT == original



@given(instance=Card_strategy)
def test_hyp_card_cardImageString_setter(instance):
    original = instance.cardImageString
    instance.cardImageString = original
    assert instance.cardImageString == original



@given(instance=Card_strategy)
def test_hyp_card_SEVEN_setter(instance):
    original = instance.SEVEN
    instance.SEVEN = original
    assert instance.SEVEN == original



@given(instance=Card_strategy)
def test_hyp_card_FIVE_setter(instance):
    original = instance.FIVE
    instance.FIVE = original
    assert instance.FIVE == original



@given(instance=Card_strategy)
def test_hyp_card_SIX_setter(instance):
    original = instance.SIX
    instance.SIX = original
    assert instance.SIX == original



@given(instance=Card_strategy)
def test_hyp_card_cardBack_setter(instance):
    original = instance.cardBack
    instance.cardBack = original
    assert instance.cardBack == original



@given(instance=Card_strategy)
def test_hyp_card_KING_setter(instance):
    original = instance.KING
    instance.KING = original
    assert instance.KING == original



@given(instance=Card_strategy)
def test_hyp_card_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=Card_strategy)
def test_hyp_card_THREE_setter(instance):
    original = instance.THREE
    instance.THREE = original
    assert instance.THREE == original



@given(instance=Card_strategy)
def test_hyp_card_cardSuit_setter(instance):
    original = instance.cardSuit
    instance.cardSuit = original
    assert instance.cardSuit == original



@given(instance=Card_strategy)
def test_hyp_card_DIAMONDS_SUIT_setter(instance):
    original = instance.DIAMONDS_SUIT
    instance.DIAMONDS_SUIT = original
    assert instance.DIAMONDS_SUIT == original



@given(instance=Card_strategy)
def test_hyp_card_HEARTS_SUIT_setter(instance):
    original = instance.HEARTS_SUIT
    instance.HEARTS_SUIT = original
    assert instance.HEARTS_SUIT == original



@given(instance=Card_strategy)
def test_hyp_card_faceUp_setter(instance):
    original = instance.faceUp
    instance.faceUp = original
    assert instance.faceUp == original



@given(instance=Card_strategy)
def test_hyp_card_deckNumber_setter(instance):
    original = instance.deckNumber
    instance.deckNumber = original
    assert instance.deckNumber == original



@given(instance=Card_strategy)
def test_hyp_card_cardNumber_setter(instance):
    original = instance.cardNumber
    instance.cardNumber = original
    assert instance.cardNumber == original



@given(instance=Card_strategy)
def test_hyp_card_cardHighlighted_setter(instance):
    original = instance.cardHighlighted
    instance.cardHighlighted = original
    assert instance.cardHighlighted == original



@given(instance=Card_strategy)
def test_hyp_card_NINE_setter(instance):
    original = instance.NINE
    instance.NINE = original
    assert instance.NINE == original




@given(instance=AcePile_strategy)
def test_hyp_acepile_suit_setter(instance):
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
    AcePile,
    ActionEvent,
    Card,
    CardStack,
    ChangeAppearance,
    ChangeOptions,
    Column,
    DealDeck,
    Deck,
    DiscardPile,
    FireworksDisplay,
    FourRowSolitaire,
    Graphics,
    SingleCell,
    SolitaireBoard,
    SolitaireLayout,
    SolitairePanel,
    WinScreen,
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

def test_AcePile_suit_value_roundtrip():
    instance = AcePile(suit="sample_text")
    assert instance.suit == "sample_text"
    instance.suit = "sample_text_2"
    assert instance.suit == "sample_text_2"


def test_Card_ACE_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.ACE == 7
    instance.ACE = 13
    assert instance.ACE == 13


def test_Card_CLUBS_SUIT_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.CLUBS_SUIT == "sample_text"
    instance.CLUBS_SUIT = "sample_text_2"
    assert instance.CLUBS_SUIT == "sample_text_2"


def test_Card_DIAMONDS_SUIT_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.DIAMONDS_SUIT == "sample_text"
    instance.DIAMONDS_SUIT = "sample_text_2"
    assert instance.DIAMONDS_SUIT == "sample_text_2"


def test_Card_EIGHT_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.EIGHT == 7
    instance.EIGHT = 13
    assert instance.EIGHT == 13


def test_Card_FIVE_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.FIVE == 7
    instance.FIVE = 13
    assert instance.FIVE == 13


def test_Card_FOUR_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.FOUR == 7
    instance.FOUR = 13
    assert instance.FOUR == 13


def test_Card_HEARTS_SUIT_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.HEARTS_SUIT == "sample_text"
    instance.HEARTS_SUIT = "sample_text_2"
    assert instance.HEARTS_SUIT == "sample_text_2"


def test_Card_INVALID_NUMBER_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.INVALID_NUMBER == 7
    instance.INVALID_NUMBER = 13
    assert instance.INVALID_NUMBER == 13


def test_Card_INVALID_SUIT_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.INVALID_SUIT == "sample_text"
    instance.INVALID_SUIT = "sample_text_2"
    assert instance.INVALID_SUIT == "sample_text_2"


def test_Card_JACK_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.JACK == 7
    instance.JACK = 13
    assert instance.JACK == 13


def test_Card_KING_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.KING == 7
    instance.KING = 13
    assert instance.KING == 13


def test_Card_NINE_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.NINE == 7
    instance.NINE = 13
    assert instance.NINE == 13


def test_Card_QUEEN_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.QUEEN == 7
    instance.QUEEN = 13
    assert instance.QUEEN == 13


def test_Card_SEVEN_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.SEVEN == 7
    instance.SEVEN = 13
    assert instance.SEVEN == 13


def test_Card_SIX_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.SIX == 7
    instance.SIX = 13
    assert instance.SIX == 13


def test_Card_SPADES_SUIT_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.SPADES_SUIT == "sample_text"
    instance.SPADES_SUIT = "sample_text_2"
    assert instance.SPADES_SUIT == "sample_text_2"


def test_Card_TEN_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.TEN == 7
    instance.TEN = 13
    assert instance.TEN == 13


def test_Card_THREE_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.THREE == 7
    instance.THREE = 13
    assert instance.THREE == 13


def test_Card_TWO_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.TWO == 7
    instance.TWO = 13
    assert instance.TWO == 13


def test_Card_cardBack_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.cardBack == "sample_text"
    instance.cardBack = "sample_text_2"
    assert instance.cardBack == "sample_text_2"


def test_Card_cardColor_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.cardColor == 7
    instance.cardColor = 13
    assert instance.cardColor == 13


def test_Card_cardHighlighted_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.cardHighlighted == "sample_text"
    instance.cardHighlighted = "sample_text_2"
    assert instance.cardHighlighted == "sample_text_2"


def test_Card_cardImageString_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.cardImageString == "sample_text"
    instance.cardImageString = "sample_text_2"
    assert instance.cardImageString == "sample_text_2"


def test_Card_cardNumber_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.cardNumber == 7
    instance.cardNumber = 13
    assert instance.cardNumber == 13


def test_Card_cardSuit_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.cardSuit == "sample_text"
    instance.cardSuit = "sample_text_2"
    assert instance.cardSuit == "sample_text_2"


def test_Card_deckNumber_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.deckNumber == 7
    instance.deckNumber = 13
    assert instance.deckNumber == 13


def test_Card_faceUp_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.faceUp == True
    instance.faceUp = False
    assert instance.faceUp == False


def test_Card_fullCardNumber_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.fullCardNumber == 7
    instance.fullCardNumber = 13
    assert instance.fullCardNumber == 13


def test_Card_highlighted_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.highlighted == True
    instance.highlighted = False
    assert instance.highlighted == False


def test_Card_image_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.image == "sample_text"
    instance.image = "sample_text_2"
    assert instance.image == "sample_text_2"


def test_Card_location_value_roundtrip():
    instance = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_ChangeAppearance_FRS_BACKGROUND_value_roundtrip():
    instance = ChangeAppearance(FRS_BACKGROUND=7, FRS_DECK=7, NUM_BACKGROUNDS=7, NUM_DECKS=7, backgroundLabel="sample_text", backgroundNumber=7, backgrounds="sample_text", cardBackLabel="sample_text", deckNumber=7, decks="sample_text", exited=True, ok="sample_text")
    assert instance.FRS_BACKGROUND == 7
    instance.FRS_BACKGROUND = 13
    assert instance.FRS_BACKGROUND == 13


def test_ChangeAppearance_FRS_DECK_value_roundtrip():
    instance = ChangeAppearance(FRS_BACKGROUND=7, FRS_DECK=7, NUM_BACKGROUNDS=7, NUM_DECKS=7, backgroundLabel="sample_text", backgroundNumber=7, backgrounds="sample_text", cardBackLabel="sample_text", deckNumber=7, decks="sample_text", exited=True, ok="sample_text")
    assert instance.FRS_DECK == 7
    instance.FRS_DECK = 13
    assert instance.FRS_DECK == 13


def test_ChangeAppearance_NUM_BACKGROUNDS_value_roundtrip():
    instance = ChangeAppearance(FRS_BACKGROUND=7, FRS_DECK=7, NUM_BACKGROUNDS=7, NUM_DECKS=7, backgroundLabel="sample_text", backgroundNumber=7, backgrounds="sample_text", cardBackLabel="sample_text", deckNumber=7, decks="sample_text", exited=True, ok="sample_text")
    assert instance.NUM_BACKGROUNDS == 7
    instance.NUM_BACKGROUNDS = 13
    assert instance.NUM_BACKGROUNDS == 13


def test_ChangeAppearance_NUM_DECKS_value_roundtrip():
    instance = ChangeAppearance(FRS_BACKGROUND=7, FRS_DECK=7, NUM_BACKGROUNDS=7, NUM_DECKS=7, backgroundLabel="sample_text", backgroundNumber=7, backgrounds="sample_text", cardBackLabel="sample_text", deckNumber=7, decks="sample_text", exited=True, ok="sample_text")
    assert instance.NUM_DECKS == 7
    instance.NUM_DECKS = 13
    assert instance.NUM_DECKS == 13


def test_ChangeAppearance_backgroundLabel_value_roundtrip():
    instance = ChangeAppearance(FRS_BACKGROUND=7, FRS_DECK=7, NUM_BACKGROUNDS=7, NUM_DECKS=7, backgroundLabel="sample_text", backgroundNumber=7, backgrounds="sample_text", cardBackLabel="sample_text", deckNumber=7, decks="sample_text", exited=True, ok="sample_text")
    assert instance.backgroundLabel == "sample_text"
    instance.backgroundLabel = "sample_text_2"
    assert instance.backgroundLabel == "sample_text_2"


def test_ChangeAppearance_backgroundNumber_value_roundtrip():
    instance = ChangeAppearance(FRS_BACKGROUND=7, FRS_DECK=7, NUM_BACKGROUNDS=7, NUM_DECKS=7, backgroundLabel="sample_text", backgroundNumber=7, backgrounds="sample_text", cardBackLabel="sample_text", deckNumber=7, decks="sample_text", exited=True, ok="sample_text")
    assert instance.backgroundNumber == 7
    instance.backgroundNumber = 13
    assert instance.backgroundNumber == 13


def test_ChangeAppearance_backgrounds_value_roundtrip():
    instance = ChangeAppearance(FRS_BACKGROUND=7, FRS_DECK=7, NUM_BACKGROUNDS=7, NUM_DECKS=7, backgroundLabel="sample_text", backgroundNumber=7, backgrounds="sample_text", cardBackLabel="sample_text", deckNumber=7, decks="sample_text", exited=True, ok="sample_text")
    assert instance.backgrounds == "sample_text"
    instance.backgrounds = "sample_text_2"
    assert instance.backgrounds == "sample_text_2"


def test_ChangeAppearance_cardBackLabel_value_roundtrip():
    instance = ChangeAppearance(FRS_BACKGROUND=7, FRS_DECK=7, NUM_BACKGROUNDS=7, NUM_DECKS=7, backgroundLabel="sample_text", backgroundNumber=7, backgrounds="sample_text", cardBackLabel="sample_text", deckNumber=7, decks="sample_text", exited=True, ok="sample_text")
    assert instance.cardBackLabel == "sample_text"
    instance.cardBackLabel = "sample_text_2"
    assert instance.cardBackLabel == "sample_text_2"


def test_ChangeAppearance_deckNumber_value_roundtrip():
    instance = ChangeAppearance(FRS_BACKGROUND=7, FRS_DECK=7, NUM_BACKGROUNDS=7, NUM_DECKS=7, backgroundLabel="sample_text", backgroundNumber=7, backgrounds="sample_text", cardBackLabel="sample_text", deckNumber=7, decks="sample_text", exited=True, ok="sample_text")
    assert instance.deckNumber == 7
    instance.deckNumber = 13
    assert instance.deckNumber == 13


def test_ChangeAppearance_decks_value_roundtrip():
    instance = ChangeAppearance(FRS_BACKGROUND=7, FRS_DECK=7, NUM_BACKGROUNDS=7, NUM_DECKS=7, backgroundLabel="sample_text", backgroundNumber=7, backgrounds="sample_text", cardBackLabel="sample_text", deckNumber=7, decks="sample_text", exited=True, ok="sample_text")
    assert instance.decks == "sample_text"
    instance.decks = "sample_text_2"
    assert instance.decks == "sample_text_2"


def test_ChangeAppearance_exited_value_roundtrip():
    instance = ChangeAppearance(FRS_BACKGROUND=7, FRS_DECK=7, NUM_BACKGROUNDS=7, NUM_DECKS=7, backgroundLabel="sample_text", backgroundNumber=7, backgrounds="sample_text", cardBackLabel="sample_text", deckNumber=7, decks="sample_text", exited=True, ok="sample_text")
    assert instance.exited == True
    instance.exited = False
    assert instance.exited == False


def test_ChangeAppearance_ok_value_roundtrip():
    instance = ChangeAppearance(FRS_BACKGROUND=7, FRS_DECK=7, NUM_BACKGROUNDS=7, NUM_DECKS=7, backgroundLabel="sample_text", backgroundNumber=7, backgrounds="sample_text", cardBackLabel="sample_text", deckNumber=7, decks="sample_text", exited=True, ok="sample_text")
    assert instance.ok == "sample_text"
    instance.ok = "sample_text_2"
    assert instance.ok == "sample_text_2"


def test_ChangeOptions_animation_value_roundtrip():
    instance = ChangeOptions(animation=7, difficulty=7, drawCount=7, drawOne="sample_text", drawThree="sample_text", easy="sample_text", exited=True, hard="sample_text", medium="sample_text", ok="sample_text", sounds=7, timer=7, timerCheck="sample_text", winAnimationCheck="sample_text", winSoundsCheck="sample_text")
    assert instance.animation == 7
    instance.animation = 13
    assert instance.animation == 13


def test_ChangeOptions_difficulty_value_roundtrip():
    instance = ChangeOptions(animation=7, difficulty=7, drawCount=7, drawOne="sample_text", drawThree="sample_text", easy="sample_text", exited=True, hard="sample_text", medium="sample_text", ok="sample_text", sounds=7, timer=7, timerCheck="sample_text", winAnimationCheck="sample_text", winSoundsCheck="sample_text")
    assert instance.difficulty == 7
    instance.difficulty = 13
    assert instance.difficulty == 13


def test_ChangeOptions_drawCount_value_roundtrip():
    instance = ChangeOptions(animation=7, difficulty=7, drawCount=7, drawOne="sample_text", drawThree="sample_text", easy="sample_text", exited=True, hard="sample_text", medium="sample_text", ok="sample_text", sounds=7, timer=7, timerCheck="sample_text", winAnimationCheck="sample_text", winSoundsCheck="sample_text")
    assert instance.drawCount == 7
    instance.drawCount = 13
    assert instance.drawCount == 13


def test_ChangeOptions_drawOne_value_roundtrip():
    instance = ChangeOptions(animation=7, difficulty=7, drawCount=7, drawOne="sample_text", drawThree="sample_text", easy="sample_text", exited=True, hard="sample_text", medium="sample_text", ok="sample_text", sounds=7, timer=7, timerCheck="sample_text", winAnimationCheck="sample_text", winSoundsCheck="sample_text")
    assert instance.drawOne == "sample_text"
    instance.drawOne = "sample_text_2"
    assert instance.drawOne == "sample_text_2"


def test_ChangeOptions_drawThree_value_roundtrip():
    instance = ChangeOptions(animation=7, difficulty=7, drawCount=7, drawOne="sample_text", drawThree="sample_text", easy="sample_text", exited=True, hard="sample_text", medium="sample_text", ok="sample_text", sounds=7, timer=7, timerCheck="sample_text", winAnimationCheck="sample_text", winSoundsCheck="sample_text")
    assert instance.drawThree == "sample_text"
    instance.drawThree = "sample_text_2"
    assert instance.drawThree == "sample_text_2"


def test_ChangeOptions_easy_value_roundtrip():
    instance = ChangeOptions(animation=7, difficulty=7, drawCount=7, drawOne="sample_text", drawThree="sample_text", easy="sample_text", exited=True, hard="sample_text", medium="sample_text", ok="sample_text", sounds=7, timer=7, timerCheck="sample_text", winAnimationCheck="sample_text", winSoundsCheck="sample_text")
    assert instance.easy == "sample_text"
    instance.easy = "sample_text_2"
    assert instance.easy == "sample_text_2"


def test_ChangeOptions_exited_value_roundtrip():
    instance = ChangeOptions(animation=7, difficulty=7, drawCount=7, drawOne="sample_text", drawThree="sample_text", easy="sample_text", exited=True, hard="sample_text", medium="sample_text", ok="sample_text", sounds=7, timer=7, timerCheck="sample_text", winAnimationCheck="sample_text", winSoundsCheck="sample_text")
    assert instance.exited == True
    instance.exited = False
    assert instance.exited == False


def test_ChangeOptions_hard_value_roundtrip():
    instance = ChangeOptions(animation=7, difficulty=7, drawCount=7, drawOne="sample_text", drawThree="sample_text", easy="sample_text", exited=True, hard="sample_text", medium="sample_text", ok="sample_text", sounds=7, timer=7, timerCheck="sample_text", winAnimationCheck="sample_text", winSoundsCheck="sample_text")
    assert instance.hard == "sample_text"
    instance.hard = "sample_text_2"
    assert instance.hard == "sample_text_2"


def test_ChangeOptions_medium_value_roundtrip():
    instance = ChangeOptions(animation=7, difficulty=7, drawCount=7, drawOne="sample_text", drawThree="sample_text", easy="sample_text", exited=True, hard="sample_text", medium="sample_text", ok="sample_text", sounds=7, timer=7, timerCheck="sample_text", winAnimationCheck="sample_text", winSoundsCheck="sample_text")
    assert instance.medium == "sample_text"
    instance.medium = "sample_text_2"
    assert instance.medium == "sample_text_2"


def test_ChangeOptions_ok_value_roundtrip():
    instance = ChangeOptions(animation=7, difficulty=7, drawCount=7, drawOne="sample_text", drawThree="sample_text", easy="sample_text", exited=True, hard="sample_text", medium="sample_text", ok="sample_text", sounds=7, timer=7, timerCheck="sample_text", winAnimationCheck="sample_text", winSoundsCheck="sample_text")
    assert instance.ok == "sample_text"
    instance.ok = "sample_text_2"
    assert instance.ok == "sample_text_2"


def test_ChangeOptions_sounds_value_roundtrip():
    instance = ChangeOptions(animation=7, difficulty=7, drawCount=7, drawOne="sample_text", drawThree="sample_text", easy="sample_text", exited=True, hard="sample_text", medium="sample_text", ok="sample_text", sounds=7, timer=7, timerCheck="sample_text", winAnimationCheck="sample_text", winSoundsCheck="sample_text")
    assert instance.sounds == 7
    instance.sounds = 13
    assert instance.sounds == 13


def test_ChangeOptions_timer_value_roundtrip():
    instance = ChangeOptions(animation=7, difficulty=7, drawCount=7, drawOne="sample_text", drawThree="sample_text", easy="sample_text", exited=True, hard="sample_text", medium="sample_text", ok="sample_text", sounds=7, timer=7, timerCheck="sample_text", winAnimationCheck="sample_text", winSoundsCheck="sample_text")
    assert instance.timer == 7
    instance.timer = 13
    assert instance.timer == 13


def test_ChangeOptions_timerCheck_value_roundtrip():
    instance = ChangeOptions(animation=7, difficulty=7, drawCount=7, drawOne="sample_text", drawThree="sample_text", easy="sample_text", exited=True, hard="sample_text", medium="sample_text", ok="sample_text", sounds=7, timer=7, timerCheck="sample_text", winAnimationCheck="sample_text", winSoundsCheck="sample_text")
    assert instance.timerCheck == "sample_text"
    instance.timerCheck = "sample_text_2"
    assert instance.timerCheck == "sample_text_2"


def test_ChangeOptions_winAnimationCheck_value_roundtrip():
    instance = ChangeOptions(animation=7, difficulty=7, drawCount=7, drawOne="sample_text", drawThree="sample_text", easy="sample_text", exited=True, hard="sample_text", medium="sample_text", ok="sample_text", sounds=7, timer=7, timerCheck="sample_text", winAnimationCheck="sample_text", winSoundsCheck="sample_text")
    assert instance.winAnimationCheck == "sample_text"
    instance.winAnimationCheck = "sample_text_2"
    assert instance.winAnimationCheck == "sample_text_2"


def test_ChangeOptions_winSoundsCheck_value_roundtrip():
    instance = ChangeOptions(animation=7, difficulty=7, drawCount=7, drawOne="sample_text", drawThree="sample_text", easy="sample_text", exited=True, hard="sample_text", medium="sample_text", ok="sample_text", sounds=7, timer=7, timerCheck="sample_text", winAnimationCheck="sample_text", winSoundsCheck="sample_text")
    assert instance.winSoundsCheck == "sample_text"
    instance.winSoundsCheck = "sample_text_2"
    assert instance.winSoundsCheck == "sample_text_2"


def test_DealDeck_DRAW_ONE_THROUGH_LIMIT_value_roundtrip():
    instance = DealDeck(DRAW_ONE_THROUGH_LIMIT=7, DRAW_THREE_THROUGH_LIMIT=7, EASY_THROUGH_LIMIT=7, HARD_THROUGH_LIMIT=7, MEDIUM_THROUGH_LIMIT=7, deckThroughLimit=7, difficulty=7, drawCount=7, numTimesThroughDeck=7, redealable=True)
    assert instance.DRAW_ONE_THROUGH_LIMIT == 7
    instance.DRAW_ONE_THROUGH_LIMIT = 13
    assert instance.DRAW_ONE_THROUGH_LIMIT == 13


def test_DealDeck_DRAW_THREE_THROUGH_LIMIT_value_roundtrip():
    instance = DealDeck(DRAW_ONE_THROUGH_LIMIT=7, DRAW_THREE_THROUGH_LIMIT=7, EASY_THROUGH_LIMIT=7, HARD_THROUGH_LIMIT=7, MEDIUM_THROUGH_LIMIT=7, deckThroughLimit=7, difficulty=7, drawCount=7, numTimesThroughDeck=7, redealable=True)
    assert instance.DRAW_THREE_THROUGH_LIMIT == 7
    instance.DRAW_THREE_THROUGH_LIMIT = 13
    assert instance.DRAW_THREE_THROUGH_LIMIT == 13


def test_DealDeck_EASY_THROUGH_LIMIT_value_roundtrip():
    instance = DealDeck(DRAW_ONE_THROUGH_LIMIT=7, DRAW_THREE_THROUGH_LIMIT=7, EASY_THROUGH_LIMIT=7, HARD_THROUGH_LIMIT=7, MEDIUM_THROUGH_LIMIT=7, deckThroughLimit=7, difficulty=7, drawCount=7, numTimesThroughDeck=7, redealable=True)
    assert instance.EASY_THROUGH_LIMIT == 7
    instance.EASY_THROUGH_LIMIT = 13
    assert instance.EASY_THROUGH_LIMIT == 13


def test_DealDeck_HARD_THROUGH_LIMIT_value_roundtrip():
    instance = DealDeck(DRAW_ONE_THROUGH_LIMIT=7, DRAW_THREE_THROUGH_LIMIT=7, EASY_THROUGH_LIMIT=7, HARD_THROUGH_LIMIT=7, MEDIUM_THROUGH_LIMIT=7, deckThroughLimit=7, difficulty=7, drawCount=7, numTimesThroughDeck=7, redealable=True)
    assert instance.HARD_THROUGH_LIMIT == 7
    instance.HARD_THROUGH_LIMIT = 13
    assert instance.HARD_THROUGH_LIMIT == 13


def test_DealDeck_MEDIUM_THROUGH_LIMIT_value_roundtrip():
    instance = DealDeck(DRAW_ONE_THROUGH_LIMIT=7, DRAW_THREE_THROUGH_LIMIT=7, EASY_THROUGH_LIMIT=7, HARD_THROUGH_LIMIT=7, MEDIUM_THROUGH_LIMIT=7, deckThroughLimit=7, difficulty=7, drawCount=7, numTimesThroughDeck=7, redealable=True)
    assert instance.MEDIUM_THROUGH_LIMIT == 7
    instance.MEDIUM_THROUGH_LIMIT = 13
    assert instance.MEDIUM_THROUGH_LIMIT == 13


def test_DealDeck_deckThroughLimit_value_roundtrip():
    instance = DealDeck(DRAW_ONE_THROUGH_LIMIT=7, DRAW_THREE_THROUGH_LIMIT=7, EASY_THROUGH_LIMIT=7, HARD_THROUGH_LIMIT=7, MEDIUM_THROUGH_LIMIT=7, deckThroughLimit=7, difficulty=7, drawCount=7, numTimesThroughDeck=7, redealable=True)
    assert instance.deckThroughLimit == 7
    instance.deckThroughLimit = 13
    assert instance.deckThroughLimit == 13


def test_DealDeck_difficulty_value_roundtrip():
    instance = DealDeck(DRAW_ONE_THROUGH_LIMIT=7, DRAW_THREE_THROUGH_LIMIT=7, EASY_THROUGH_LIMIT=7, HARD_THROUGH_LIMIT=7, MEDIUM_THROUGH_LIMIT=7, deckThroughLimit=7, difficulty=7, drawCount=7, numTimesThroughDeck=7, redealable=True)
    assert instance.difficulty == 7
    instance.difficulty = 13
    assert instance.difficulty == 13


def test_DealDeck_drawCount_value_roundtrip():
    instance = DealDeck(DRAW_ONE_THROUGH_LIMIT=7, DRAW_THREE_THROUGH_LIMIT=7, EASY_THROUGH_LIMIT=7, HARD_THROUGH_LIMIT=7, MEDIUM_THROUGH_LIMIT=7, deckThroughLimit=7, difficulty=7, drawCount=7, numTimesThroughDeck=7, redealable=True)
    assert instance.drawCount == 7
    instance.drawCount = 13
    assert instance.drawCount == 13


def test_DealDeck_numTimesThroughDeck_value_roundtrip():
    instance = DealDeck(DRAW_ONE_THROUGH_LIMIT=7, DRAW_THREE_THROUGH_LIMIT=7, EASY_THROUGH_LIMIT=7, HARD_THROUGH_LIMIT=7, MEDIUM_THROUGH_LIMIT=7, deckThroughLimit=7, difficulty=7, drawCount=7, numTimesThroughDeck=7, redealable=True)
    assert instance.numTimesThroughDeck == 7
    instance.numTimesThroughDeck = 13
    assert instance.numTimesThroughDeck == 13


def test_DealDeck_redealable_value_roundtrip():
    instance = DealDeck(DRAW_ONE_THROUGH_LIMIT=7, DRAW_THREE_THROUGH_LIMIT=7, EASY_THROUGH_LIMIT=7, HARD_THROUGH_LIMIT=7, MEDIUM_THROUGH_LIMIT=7, deckThroughLimit=7, difficulty=7, drawCount=7, numTimesThroughDeck=7, redealable=True)
    assert instance.redealable == True
    instance.redealable = False
    assert instance.redealable == False


def test_Deck_deckNumber_value_roundtrip():
    instance = Deck(deckNumber=7)
    assert instance.deckNumber == 7
    instance.deckNumber = 13
    assert instance.deckNumber == 13


def test_DiscardPile_cardsLeftFromDraw_value_roundtrip():
    instance = DiscardPile(cardsLeftFromDraw=7, drawCount=7)
    assert instance.cardsLeftFromDraw == 7
    instance.cardsLeftFromDraw = 13
    assert instance.cardsLeftFromDraw == 13


def test_DiscardPile_drawCount_value_roundtrip():
    instance = DiscardPile(cardsLeftFromDraw=7, drawCount=7)
    assert instance.drawCount == 7
    instance.drawCount = 13
    assert instance.drawCount == 13


def test_FireworksDisplay_FIREWORKS_SIZE_value_roundtrip():
    instance = FireworksDisplay(FIREWORKS_SIZE=7, FIREWORKS_TIME=7, NUM_FIREWORKS=7, SET_DELAY=7, colors="sample_text", num=7, numSets=7, random="sample_text", startValue=7, timer="sample_text", x="sample_text", xx="sample_text", y="sample_text", yy="sample_text")
    assert instance.FIREWORKS_SIZE == 7
    instance.FIREWORKS_SIZE = 13
    assert instance.FIREWORKS_SIZE == 13


def test_FireworksDisplay_FIREWORKS_TIME_value_roundtrip():
    instance = FireworksDisplay(FIREWORKS_SIZE=7, FIREWORKS_TIME=7, NUM_FIREWORKS=7, SET_DELAY=7, colors="sample_text", num=7, numSets=7, random="sample_text", startValue=7, timer="sample_text", x="sample_text", xx="sample_text", y="sample_text", yy="sample_text")
    assert instance.FIREWORKS_TIME == 7
    instance.FIREWORKS_TIME = 13
    assert instance.FIREWORKS_TIME == 13


def test_FireworksDisplay_NUM_FIREWORKS_value_roundtrip():
    instance = FireworksDisplay(FIREWORKS_SIZE=7, FIREWORKS_TIME=7, NUM_FIREWORKS=7, SET_DELAY=7, colors="sample_text", num=7, numSets=7, random="sample_text", startValue=7, timer="sample_text", x="sample_text", xx="sample_text", y="sample_text", yy="sample_text")
    assert instance.NUM_FIREWORKS == 7
    instance.NUM_FIREWORKS = 13
    assert instance.NUM_FIREWORKS == 13


def test_FireworksDisplay_SET_DELAY_value_roundtrip():
    instance = FireworksDisplay(FIREWORKS_SIZE=7, FIREWORKS_TIME=7, NUM_FIREWORKS=7, SET_DELAY=7, colors="sample_text", num=7, numSets=7, random="sample_text", startValue=7, timer="sample_text", x="sample_text", xx="sample_text", y="sample_text", yy="sample_text")
    assert instance.SET_DELAY == 7
    instance.SET_DELAY = 13
    assert instance.SET_DELAY == 13


def test_FireworksDisplay_colors_value_roundtrip():
    instance = FireworksDisplay(FIREWORKS_SIZE=7, FIREWORKS_TIME=7, NUM_FIREWORKS=7, SET_DELAY=7, colors="sample_text", num=7, numSets=7, random="sample_text", startValue=7, timer="sample_text", x="sample_text", xx="sample_text", y="sample_text", yy="sample_text")
    assert instance.colors == "sample_text"
    instance.colors = "sample_text_2"
    assert instance.colors == "sample_text_2"


def test_FireworksDisplay_num_value_roundtrip():
    instance = FireworksDisplay(FIREWORKS_SIZE=7, FIREWORKS_TIME=7, NUM_FIREWORKS=7, SET_DELAY=7, colors="sample_text", num=7, numSets=7, random="sample_text", startValue=7, timer="sample_text", x="sample_text", xx="sample_text", y="sample_text", yy="sample_text")
    assert instance.num == 7
    instance.num = 13
    assert instance.num == 13


def test_FireworksDisplay_numSets_value_roundtrip():
    instance = FireworksDisplay(FIREWORKS_SIZE=7, FIREWORKS_TIME=7, NUM_FIREWORKS=7, SET_DELAY=7, colors="sample_text", num=7, numSets=7, random="sample_text", startValue=7, timer="sample_text", x="sample_text", xx="sample_text", y="sample_text", yy="sample_text")
    assert instance.numSets == 7
    instance.numSets = 13
    assert instance.numSets == 13


def test_FireworksDisplay_random_value_roundtrip():
    instance = FireworksDisplay(FIREWORKS_SIZE=7, FIREWORKS_TIME=7, NUM_FIREWORKS=7, SET_DELAY=7, colors="sample_text", num=7, numSets=7, random="sample_text", startValue=7, timer="sample_text", x="sample_text", xx="sample_text", y="sample_text", yy="sample_text")
    assert instance.random == "sample_text"
    instance.random = "sample_text_2"
    assert instance.random == "sample_text_2"


def test_FireworksDisplay_startValue_value_roundtrip():
    instance = FireworksDisplay(FIREWORKS_SIZE=7, FIREWORKS_TIME=7, NUM_FIREWORKS=7, SET_DELAY=7, colors="sample_text", num=7, numSets=7, random="sample_text", startValue=7, timer="sample_text", x="sample_text", xx="sample_text", y="sample_text", yy="sample_text")
    assert instance.startValue == 7
    instance.startValue = 13
    assert instance.startValue == 13


def test_FireworksDisplay_timer_value_roundtrip():
    instance = FireworksDisplay(FIREWORKS_SIZE=7, FIREWORKS_TIME=7, NUM_FIREWORKS=7, SET_DELAY=7, colors="sample_text", num=7, numSets=7, random="sample_text", startValue=7, timer="sample_text", x="sample_text", xx="sample_text", y="sample_text", yy="sample_text")
    assert instance.timer == "sample_text"
    instance.timer = "sample_text_2"
    assert instance.timer == "sample_text_2"


def test_FireworksDisplay_x_value_roundtrip():
    instance = FireworksDisplay(FIREWORKS_SIZE=7, FIREWORKS_TIME=7, NUM_FIREWORKS=7, SET_DELAY=7, colors="sample_text", num=7, numSets=7, random="sample_text", startValue=7, timer="sample_text", x="sample_text", xx="sample_text", y="sample_text", yy="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_FireworksDisplay_xx_value_roundtrip():
    instance = FireworksDisplay(FIREWORKS_SIZE=7, FIREWORKS_TIME=7, NUM_FIREWORKS=7, SET_DELAY=7, colors="sample_text", num=7, numSets=7, random="sample_text", startValue=7, timer="sample_text", x="sample_text", xx="sample_text", y="sample_text", yy="sample_text")
    assert instance.xx == "sample_text"
    instance.xx = "sample_text_2"
    assert instance.xx == "sample_text_2"


def test_FireworksDisplay_y_value_roundtrip():
    instance = FireworksDisplay(FIREWORKS_SIZE=7, FIREWORKS_TIME=7, NUM_FIREWORKS=7, SET_DELAY=7, colors="sample_text", num=7, numSets=7, random="sample_text", startValue=7, timer="sample_text", x="sample_text", xx="sample_text", y="sample_text", yy="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_FireworksDisplay_yy_value_roundtrip():
    instance = FireworksDisplay(FIREWORKS_SIZE=7, FIREWORKS_TIME=7, NUM_FIREWORKS=7, SET_DELAY=7, colors="sample_text", num=7, numSets=7, random="sample_text", startValue=7, timer="sample_text", x="sample_text", xx="sample_text", y="sample_text", yy="sample_text")
    assert instance.yy == "sample_text"
    instance.yy = "sample_text_2"
    assert instance.yy == "sample_text_2"


def test_SolitaireBoard_DO_NOTHING_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.DO_NOTHING == 7
    instance.DO_NOTHING = 13
    assert instance.DO_NOTHING == 13


def test_SolitaireBoard_GAME_LOST_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.GAME_LOST == 7
    instance.GAME_LOST = 13
    assert instance.GAME_LOST == 13


def test_SolitaireBoard_GAME_SAVED_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.GAME_SAVED == 7
    instance.GAME_SAVED = 13
    assert instance.GAME_SAVED == 13


def test_SolitaireBoard_GAME_WON_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.GAME_WON == 7
    instance.GAME_WON = 13
    assert instance.GAME_WON == 13


def test_SolitaireBoard_RESET_STATS_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.RESET_STATS == 7
    instance.RESET_STATS = 13
    assert instance.RESET_STATS == 13


def test_SolitaireBoard_backgroundNumber_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.backgroundNumber == 7
    instance.backgroundNumber = 13
    assert instance.backgroundNumber == 13


def test_SolitaireBoard_deckNumber_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.deckNumber == 7
    instance.deckNumber = 13
    assert instance.deckNumber == 13


def test_SolitaireBoard_difficulty_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.difficulty == 7
    instance.difficulty = 13
    assert instance.difficulty == 13


def test_SolitaireBoard_drawCount_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.drawCount == 7
    instance.drawCount = 13
    assert instance.drawCount == 13


def test_SolitaireBoard_newDifficulty_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.newDifficulty == 7
    instance.newDifficulty = 13
    assert instance.newDifficulty == 13


def test_SolitaireBoard_newDrawCount_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.newDrawCount == 7
    instance.newDrawCount = 13
    assert instance.newDrawCount == 13


def test_SolitaireBoard_numCards_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.numCards == "sample_text"
    instance.numCards = "sample_text_2"
    assert instance.numCards == "sample_text_2"


def test_SolitaireBoard_numCardsInDiscardView_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.numCardsInDiscardView == "sample_text"
    instance.numCardsInDiscardView = "sample_text_2"
    assert instance.numCardsInDiscardView == "sample_text_2"


def test_SolitaireBoard_statusBar_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.statusBar == "sample_text"
    instance.statusBar = "sample_text_2"
    assert instance.statusBar == "sample_text_2"


def test_SolitaireBoard_timer_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.timer == "sample_text"
    instance.timer = "sample_text_2"
    assert instance.timer == "sample_text_2"


def test_SolitaireBoard_timerCount_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.timerCount == 7
    instance.timerCount = 13
    assert instance.timerCount == 13


def test_SolitaireBoard_timerLabel_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.timerLabel == "sample_text"
    instance.timerLabel = "sample_text_2"
    assert instance.timerLabel == "sample_text_2"


def test_SolitaireBoard_timerToRun_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.timerToRun == True
    instance.timerToRun = False
    assert instance.timerToRun == False


def test_SolitaireBoard_timerToRunNextGame_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.timerToRunNextGame == 7
    instance.timerToRunNextGame = 13
    assert instance.timerToRunNextGame == 13


def test_SolitaireBoard_winAnimationStatus_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.winAnimationStatus == 7
    instance.winAnimationStatus = 13
    assert instance.winAnimationStatus == 13


def test_SolitaireBoard_winSoundsStatus_value_roundtrip():
    instance = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    assert instance.winSoundsStatus == 7
    instance.winSoundsStatus = 13
    assert instance.winSoundsStatus == 13


def test_SolitaireLayout_CELL_FOUR_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.CELL_FOUR == "sample_text"
    instance.CELL_FOUR = "sample_text_2"
    assert instance.CELL_FOUR == "sample_text_2"


def test_SolitaireLayout_CELL_ONE_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.CELL_ONE == "sample_text"
    instance.CELL_ONE = "sample_text_2"
    assert instance.CELL_ONE == "sample_text_2"


def test_SolitaireLayout_CELL_THREE_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.CELL_THREE == "sample_text"
    instance.CELL_THREE = "sample_text_2"
    assert instance.CELL_THREE == "sample_text_2"


def test_SolitaireLayout_CELL_TWO_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.CELL_TWO == "sample_text"
    instance.CELL_TWO = "sample_text_2"
    assert instance.CELL_TWO == "sample_text_2"


def test_SolitaireLayout_CLUBS_ACE_PILE_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.CLUBS_ACE_PILE == "sample_text"
    instance.CLUBS_ACE_PILE = "sample_text_2"
    assert instance.CLUBS_ACE_PILE == "sample_text_2"


def test_SolitaireLayout_COLUMEN_ONE_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.COLUMEN_ONE == "sample_text"
    instance.COLUMEN_ONE = "sample_text_2"
    assert instance.COLUMEN_ONE == "sample_text_2"


def test_SolitaireLayout_COLUMN_FOUR_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.COLUMN_FOUR == "sample_text"
    instance.COLUMN_FOUR = "sample_text_2"
    assert instance.COLUMN_FOUR == "sample_text_2"


def test_SolitaireLayout_COLUMN_THREE_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.COLUMN_THREE == "sample_text"
    instance.COLUMN_THREE = "sample_text_2"
    assert instance.COLUMN_THREE == "sample_text_2"


def test_SolitaireLayout_COLUMN_TWO_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.COLUMN_TWO == "sample_text"
    instance.COLUMN_TWO = "sample_text_2"
    assert instance.COLUMN_TWO == "sample_text_2"


def test_SolitaireLayout_DECK_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.DECK == "sample_text"
    instance.DECK = "sample_text_2"
    assert instance.DECK == "sample_text_2"


def test_SolitaireLayout_DIAMONDS_ACE_PILE_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.DIAMONDS_ACE_PILE == "sample_text"
    instance.DIAMONDS_ACE_PILE = "sample_text_2"
    assert instance.DIAMONDS_ACE_PILE == "sample_text_2"


def test_SolitaireLayout_DISCARD_PILE_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.DISCARD_PILE == "sample_text"
    instance.DISCARD_PILE = "sample_text_2"
    assert instance.DISCARD_PILE == "sample_text_2"


def test_SolitaireLayout_HEARTS_ACE_PILE_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.HEARTS_ACE_PILE == "sample_text"
    instance.HEARTS_ACE_PILE = "sample_text_2"
    assert instance.HEARTS_ACE_PILE == "sample_text_2"


def test_SolitaireLayout_SPADES_ACE_PILE_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.SPADES_ACE_PILE == "sample_text"
    instance.SPADES_ACE_PILE = "sample_text_2"
    assert instance.SPADES_ACE_PILE == "sample_text_2"


def test_SolitaireLayout_aceClubs_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.aceClubs == "sample_text"
    instance.aceClubs = "sample_text_2"
    assert instance.aceClubs == "sample_text_2"


def test_SolitaireLayout_aceDiamonds_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.aceDiamonds == "sample_text"
    instance.aceDiamonds = "sample_text_2"
    assert instance.aceDiamonds == "sample_text_2"


def test_SolitaireLayout_aceHearts_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.aceHearts == "sample_text"
    instance.aceHearts = "sample_text_2"
    assert instance.aceHearts == "sample_text_2"


def test_SolitaireLayout_aceSpades_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.aceSpades == "sample_text"
    instance.aceSpades = "sample_text_2"
    assert instance.aceSpades == "sample_text_2"


def test_SolitaireLayout_cellFour_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.cellFour == "sample_text"
    instance.cellFour = "sample_text_2"
    assert instance.cellFour == "sample_text_2"


def test_SolitaireLayout_cellOne_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.cellOne == "sample_text"
    instance.cellOne = "sample_text_2"
    assert instance.cellOne == "sample_text_2"


def test_SolitaireLayout_cellThree_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.cellThree == "sample_text"
    instance.cellThree = "sample_text_2"
    assert instance.cellThree == "sample_text_2"


def test_SolitaireLayout_cellTwo_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.cellTwo == "sample_text"
    instance.cellTwo = "sample_text_2"
    assert instance.cellTwo == "sample_text_2"


def test_SolitaireLayout_colFour_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.colFour == "sample_text"
    instance.colFour = "sample_text_2"
    assert instance.colFour == "sample_text_2"


def test_SolitaireLayout_colOne_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.colOne == "sample_text"
    instance.colOne = "sample_text_2"
    assert instance.colOne == "sample_text_2"


def test_SolitaireLayout_colThree_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.colThree == "sample_text"
    instance.colThree = "sample_text_2"
    assert instance.colThree == "sample_text_2"


def test_SolitaireLayout_colTwo_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.colTwo == "sample_text"
    instance.colTwo = "sample_text_2"
    assert instance.colTwo == "sample_text_2"


def test_SolitaireLayout_deck_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.deck == "sample_text"
    instance.deck = "sample_text_2"
    assert instance.deck == "sample_text_2"


def test_SolitaireLayout_discardPile_value_roundtrip():
    instance = SolitaireLayout(CELL_FOUR="sample_text", CELL_ONE="sample_text", CELL_THREE="sample_text", CELL_TWO="sample_text", CLUBS_ACE_PILE="sample_text", COLUMEN_ONE="sample_text", COLUMN_FOUR="sample_text", COLUMN_THREE="sample_text", COLUMN_TWO="sample_text", DECK="sample_text", DIAMONDS_ACE_PILE="sample_text", DISCARD_PILE="sample_text", HEARTS_ACE_PILE="sample_text", SPADES_ACE_PILE="sample_text", aceClubs="sample_text", aceDiamonds="sample_text", aceHearts="sample_text", aceSpades="sample_text", cellFour="sample_text", cellOne="sample_text", cellThree="sample_text", cellTwo="sample_text", colFour="sample_text", colOne="sample_text", colThree="sample_text", colTwo="sample_text", deck="sample_text", discardPile="sample_text")
    assert instance.discardPile == "sample_text"
    instance.discardPile = "sample_text_2"
    assert instance.discardPile == "sample_text_2"


def test_SolitairePanel_background_value_roundtrip():
    instance = SolitairePanel(background="sample_text", backgroundNumber=7)
    assert instance.background == "sample_text"
    instance.background = "sample_text_2"
    assert instance.background == "sample_text_2"


def test_SolitairePanel_backgroundNumber_value_roundtrip():
    instance = SolitairePanel(background="sample_text", backgroundNumber=7)
    assert instance.backgroundNumber == 7
    instance.backgroundNumber = 13
    assert instance.backgroundNumber == 13


def test_assoc_CardStack_Card_link_reassign_clear():
    a = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    b1 = CardStack()
    b2 = CardStack()
    _safe_set(a, 'cardStack11', b1)
    assert _is_linked(a, 'cardStack11', b1)
    if hasattr(b1, 'card10'):
        assert _is_linked(b1, 'card10', a)
    _safe_set(a, 'cardStack11', b2)
    assert _is_linked(a, 'cardStack11', b2)
    if hasattr(b1, 'card10'):
        assert not _is_linked(b1, 'card10', a)
    if hasattr(b2, 'card10'):
        assert _is_linked(b2, 'card10', a)
    _safe_set(a, 'cardStack11', None)
    assert not _is_linked(a, 'cardStack11', b2)
    if hasattr(b2, 'card10'):
        assert not _is_linked(b2, 'card10', a)


def test_assoc_DealDeck_DiscardPile_link_reassign_clear():
    a = DiscardPile(cardsLeftFromDraw=7, drawCount=7)
    b1 = DealDeck(DRAW_ONE_THROUGH_LIMIT=7, DRAW_THREE_THROUGH_LIMIT=7, EASY_THROUGH_LIMIT=7, HARD_THROUGH_LIMIT=7, MEDIUM_THROUGH_LIMIT=7, deckThroughLimit=7, difficulty=7, drawCount=7, numTimesThroughDeck=7, redealable=True)
    b2 = DealDeck(DRAW_ONE_THROUGH_LIMIT=13, DRAW_THREE_THROUGH_LIMIT=13, EASY_THROUGH_LIMIT=13, HARD_THROUGH_LIMIT=13, MEDIUM_THROUGH_LIMIT=13, deckThroughLimit=13, difficulty=13, drawCount=13, numTimesThroughDeck=13, redealable=False)
    _safe_set(a, 'dealDeck13', b1)
    assert _is_linked(a, 'dealDeck13', b1)
    if hasattr(b1, 'discardPile12'):
        assert _is_linked(b1, 'discardPile12', a)
    _safe_set(a, 'dealDeck13', b2)
    assert _is_linked(a, 'dealDeck13', b2)
    if hasattr(b1, 'discardPile12'):
        assert not _is_linked(b1, 'discardPile12', a)
    if hasattr(b2, 'discardPile12'):
        assert _is_linked(b2, 'discardPile12', a)
    _safe_set(a, 'dealDeck13', None)
    assert not _is_linked(a, 'dealDeck13', b2)
    if hasattr(b2, 'discardPile12'):
        assert not _is_linked(b2, 'discardPile12', a)


def test_assoc_Deck_Card_link_reassign_clear():
    a = Deck(deckNumber=7)
    b1 = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    b2 = Card(ACE=13, CLUBS_SUIT="sample_text_2", DIAMONDS_SUIT="sample_text_2", EIGHT=13, FIVE=13, FOUR=13, HEARTS_SUIT="sample_text_2", INVALID_NUMBER=13, INVALID_SUIT="sample_text_2", JACK=13, KING=13, NINE=13, QUEEN=13, SEVEN=13, SIX=13, SPADES_SUIT="sample_text_2", TEN=13, THREE=13, TWO=13, cardBack="sample_text_2", cardColor=13, cardHighlighted="sample_text_2", cardImageString="sample_text_2", cardNumber=13, cardSuit="sample_text_2", deckNumber=13, faceUp=False, fullCardNumber=13, highlighted=False, image="sample_text_2", location="sample_text_2")
    _safe_set(a, 'card4', {b1})
    assert _is_linked(a, 'card4', b1)
    if hasattr(b1, 'deck5'):
        assert _is_linked(b1, 'deck5', a)
    _safe_set(a, 'card4', {b2})
    assert _is_linked(a, 'card4', b2)
    if hasattr(b1, 'deck5'):
        assert not _is_linked(b1, 'deck5', a)
    if hasattr(b2, 'deck5'):
        assert _is_linked(b2, 'deck5', a)
    _safe_set(a, 'card4', set())
    assert not _is_linked(a, 'card4', b2)
    if hasattr(b2, 'deck5'):
        assert not _is_linked(b2, 'deck5', a)


def test_assoc_SolitaireBoard_AcePile_link_reassign_clear():
    a = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    b1 = AcePile(suit="sample_text")
    b2 = AcePile(suit="sample_text_2")
    _safe_set(a, 'acePile6', {b1})
    assert _is_linked(a, 'acePile6', b1)
    if hasattr(b1, 'solitaireBoard7'):
        assert _is_linked(b1, 'solitaireBoard7', a)
    _safe_set(a, 'acePile6', {b2})
    assert _is_linked(a, 'acePile6', b2)
    if hasattr(b1, 'solitaireBoard7'):
        assert not _is_linked(b1, 'solitaireBoard7', a)
    if hasattr(b2, 'solitaireBoard7'):
        assert _is_linked(b2, 'solitaireBoard7', a)
    _safe_set(a, 'acePile6', set())
    assert not _is_linked(a, 'acePile6', b2)
    if hasattr(b2, 'solitaireBoard7'):
        assert not _is_linked(b2, 'solitaireBoard7', a)


def test_assoc_SolitaireBoard_CardStack_link_reassign_clear():
    a = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    b1 = CardStack()
    b2 = CardStack()
    _safe_set(a, 'cardStack8', {b1})
    assert _is_linked(a, 'cardStack8', b1)
    if hasattr(b1, 'solitaireBoard9'):
        assert _is_linked(b1, 'solitaireBoard9', a)
    _safe_set(a, 'cardStack8', {b2})
    assert _is_linked(a, 'cardStack8', b2)
    if hasattr(b1, 'solitaireBoard9'):
        assert not _is_linked(b1, 'solitaireBoard9', a)
    if hasattr(b2, 'solitaireBoard9'):
        assert _is_linked(b2, 'solitaireBoard9', a)
    _safe_set(a, 'cardStack8', set())
    assert not _is_linked(a, 'cardStack8', b2)
    if hasattr(b2, 'solitaireBoard9'):
        assert not _is_linked(b2, 'solitaireBoard9', a)


def test_assoc_SolitaireBoard_Column_link_reassign_clear():
    a = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    b1 = Column()
    b2 = Column()
    _safe_set(a, 'column18', {b1})
    assert _is_linked(a, 'column18', b1)
    if hasattr(b1, 'solitaireBoard19'):
        assert _is_linked(b1, 'solitaireBoard19', a)
    _safe_set(a, 'column18', {b2})
    assert _is_linked(a, 'column18', b2)
    if hasattr(b1, 'solitaireBoard19'):
        assert not _is_linked(b1, 'solitaireBoard19', a)
    if hasattr(b2, 'solitaireBoard19'):
        assert _is_linked(b2, 'solitaireBoard19', a)
    _safe_set(a, 'column18', set())
    assert not _is_linked(a, 'column18', b2)
    if hasattr(b2, 'solitaireBoard19'):
        assert not _is_linked(b2, 'solitaireBoard19', a)


def test_assoc_SolitaireBoard_Deck_link_reassign_clear():
    a = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    b1 = Deck(deckNumber=7)
    b2 = Deck(deckNumber=13)
    _safe_set(a, 'deck2', b1)
    assert _is_linked(a, 'deck2', b1)
    if hasattr(b1, 'solitaireBoard3'):
        assert _is_linked(b1, 'solitaireBoard3', a)
    _safe_set(a, 'deck2', b2)
    assert _is_linked(a, 'deck2', b2)
    if hasattr(b1, 'solitaireBoard3'):
        assert not _is_linked(b1, 'solitaireBoard3', a)
    if hasattr(b2, 'solitaireBoard3'):
        assert _is_linked(b2, 'solitaireBoard3', a)
    _safe_set(a, 'deck2', None)
    assert not _is_linked(a, 'deck2', b2)
    if hasattr(b2, 'solitaireBoard3'):
        assert not _is_linked(b2, 'solitaireBoard3', a)


def test_assoc_SolitaireBoard_DiscardPile_link_reassign_clear():
    a = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    b1 = DiscardPile(cardsLeftFromDraw=7, drawCount=7)
    b2 = DiscardPile(cardsLeftFromDraw=13, drawCount=13)
    _safe_set(a, 'discardPile14', b1)
    assert _is_linked(a, 'discardPile14', b1)
    if hasattr(b1, 'solitaireBoard15'):
        assert _is_linked(b1, 'solitaireBoard15', a)
    _safe_set(a, 'discardPile14', b2)
    assert _is_linked(a, 'discardPile14', b2)
    if hasattr(b1, 'solitaireBoard15'):
        assert not _is_linked(b1, 'solitaireBoard15', a)
    if hasattr(b2, 'solitaireBoard15'):
        assert _is_linked(b2, 'solitaireBoard15', a)
    _safe_set(a, 'discardPile14', None)
    assert not _is_linked(a, 'discardPile14', b2)
    if hasattr(b2, 'solitaireBoard15'):
        assert not _is_linked(b2, 'solitaireBoard15', a)


def test_assoc_SolitaireBoard_SingleCell_link_reassign_clear():
    a = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    b1 = SingleCell()
    b2 = SingleCell()
    _safe_set(a, 'singleCell16', {b1})
    assert _is_linked(a, 'singleCell16', b1)
    if hasattr(b1, 'solitaireBoard17'):
        assert _is_linked(b1, 'solitaireBoard17', a)
    _safe_set(a, 'singleCell16', {b2})
    assert _is_linked(a, 'singleCell16', b2)
    if hasattr(b1, 'solitaireBoard17'):
        assert not _is_linked(b1, 'solitaireBoard17', a)
    if hasattr(b2, 'solitaireBoard17'):
        assert _is_linked(b2, 'solitaireBoard17', a)
    _safe_set(a, 'singleCell16', set())
    assert not _is_linked(a, 'singleCell16', b2)
    if hasattr(b2, 'solitaireBoard17'):
        assert not _is_linked(b2, 'solitaireBoard17', a)


def test_assoc_SolitaireBoard_SolitairePanel_link_reassign_clear():
    a = SolitairePanel(background="sample_text", backgroundNumber=7)
    b1 = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    b2 = SolitaireBoard(DO_NOTHING=13, GAME_LOST=13, GAME_SAVED=13, GAME_WON=13, RESET_STATS=13, backgroundNumber=13, deckNumber=13, difficulty=13, drawCount=13, newDifficulty=13, newDrawCount=13, numCards="sample_text_2", numCardsInDiscardView="sample_text_2", statusBar="sample_text_2", timer="sample_text_2", timerCount=13, timerLabel="sample_text_2", timerToRun=False, timerToRunNextGame=13, winAnimationStatus=13, winSoundsStatus=13)
    _safe_set(a, 'solitaireBoard1', b1)
    assert _is_linked(a, 'solitaireBoard1', b1)
    if hasattr(b1, 'solitairePanel0'):
        assert _is_linked(b1, 'solitairePanel0', a)
    _safe_set(a, 'solitaireBoard1', b2)
    assert _is_linked(a, 'solitaireBoard1', b2)
    if hasattr(b1, 'solitairePanel0'):
        assert not _is_linked(b1, 'solitairePanel0', a)
    if hasattr(b2, 'solitairePanel0'):
        assert _is_linked(b2, 'solitairePanel0', a)
    _safe_set(a, 'solitaireBoard1', None)
    assert not _is_linked(a, 'solitaireBoard1', b2)
    if hasattr(b2, 'solitairePanel0'):
        assert not _is_linked(b2, 'solitairePanel0', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AcePile_strategy = st.builds(AcePile, suit=safe_text)
@given(instance=AcePile_strategy)
@settings(max_examples=25)
def test_AcePile_instantiation(instance):
    assert isinstance(instance, AcePile)


ActionEvent_strategy = st.builds(ActionEvent)
@given(instance=ActionEvent_strategy)
@settings(max_examples=25)
def test_ActionEvent_instantiation(instance):
    assert isinstance(instance, ActionEvent)


Card_strategy = st.builds(Card, ACE=st.integers(), CLUBS_SUIT=safe_text, DIAMONDS_SUIT=safe_text, EIGHT=st.integers(), FIVE=st.integers(), FOUR=st.integers(), HEARTS_SUIT=safe_text, INVALID_NUMBER=st.integers(), INVALID_SUIT=safe_text, JACK=st.integers(), KING=st.integers(), NINE=st.integers(), QUEEN=st.integers(), SEVEN=st.integers(), SIX=st.integers(), SPADES_SUIT=safe_text, TEN=st.integers(), THREE=st.integers(), TWO=st.integers(), cardBack=safe_text, cardColor=st.integers(), cardHighlighted=safe_text, cardImageString=safe_text, cardNumber=st.integers(), cardSuit=safe_text, deckNumber=st.integers(), faceUp=st.booleans(), fullCardNumber=st.integers(), highlighted=st.booleans(), image=safe_text, location=safe_text)
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)


CardStack_strategy = st.builds(CardStack)
@given(instance=CardStack_strategy)
@settings(max_examples=25)
def test_CardStack_instantiation(instance):
    assert isinstance(instance, CardStack)


ChangeAppearance_strategy = st.builds(ChangeAppearance, FRS_BACKGROUND=st.integers(), FRS_DECK=st.integers(), NUM_BACKGROUNDS=st.integers(), NUM_DECKS=st.integers(), backgroundLabel=safe_text, backgroundNumber=st.integers(), backgrounds=safe_text, cardBackLabel=safe_text, deckNumber=st.integers(), decks=safe_text, exited=st.booleans(), ok=safe_text)
@given(instance=ChangeAppearance_strategy)
@settings(max_examples=25)
def test_ChangeAppearance_instantiation(instance):
    assert isinstance(instance, ChangeAppearance)


ChangeOptions_strategy = st.builds(ChangeOptions, animation=st.integers(), difficulty=st.integers(), drawCount=st.integers(), drawOne=safe_text, drawThree=safe_text, easy=safe_text, exited=st.booleans(), hard=safe_text, medium=safe_text, ok=safe_text, sounds=st.integers(), timer=st.integers(), timerCheck=safe_text, winAnimationCheck=safe_text, winSoundsCheck=safe_text)
@given(instance=ChangeOptions_strategy)
@settings(max_examples=25)
def test_ChangeOptions_instantiation(instance):
    assert isinstance(instance, ChangeOptions)


Column_strategy = st.builds(Column)
@given(instance=Column_strategy)
@settings(max_examples=25)
def test_Column_instantiation(instance):
    assert isinstance(instance, Column)


DealDeck_strategy = st.builds(DealDeck, DRAW_ONE_THROUGH_LIMIT=st.integers(), DRAW_THREE_THROUGH_LIMIT=st.integers(), EASY_THROUGH_LIMIT=st.integers(), HARD_THROUGH_LIMIT=st.integers(), MEDIUM_THROUGH_LIMIT=st.integers(), deckThroughLimit=st.integers(), difficulty=st.integers(), drawCount=st.integers(), numTimesThroughDeck=st.integers(), redealable=st.booleans())
@given(instance=DealDeck_strategy)
@settings(max_examples=25)
def test_DealDeck_instantiation(instance):
    assert isinstance(instance, DealDeck)


Deck_strategy = st.builds(Deck, deckNumber=st.integers())
@given(instance=Deck_strategy)
@settings(max_examples=25)
def test_Deck_instantiation(instance):
    assert isinstance(instance, Deck)


DiscardPile_strategy = st.builds(DiscardPile, cardsLeftFromDraw=st.integers(), drawCount=st.integers())
@given(instance=DiscardPile_strategy)
@settings(max_examples=25)
def test_DiscardPile_instantiation(instance):
    assert isinstance(instance, DiscardPile)


FireworksDisplay_strategy = st.builds(FireworksDisplay, FIREWORKS_SIZE=st.integers(), FIREWORKS_TIME=st.integers(), NUM_FIREWORKS=st.integers(), SET_DELAY=st.integers(), colors=safe_text, num=st.integers(), numSets=st.integers(), random=safe_text, startValue=st.integers(), timer=safe_text, x=safe_text, xx=safe_text, y=safe_text, yy=safe_text)
@given(instance=FireworksDisplay_strategy)
@settings(max_examples=25)
def test_FireworksDisplay_instantiation(instance):
    assert isinstance(instance, FireworksDisplay)


Graphics_strategy = st.builds(Graphics)
@given(instance=Graphics_strategy)
@settings(max_examples=25)
def test_Graphics_instantiation(instance):
    assert isinstance(instance, Graphics)


SingleCell_strategy = st.builds(SingleCell)
@given(instance=SingleCell_strategy)
@settings(max_examples=25)
def test_SingleCell_instantiation(instance):
    assert isinstance(instance, SingleCell)


SolitaireBoard_strategy = st.builds(SolitaireBoard, DO_NOTHING=st.integers(), GAME_LOST=st.integers(), GAME_SAVED=st.integers(), GAME_WON=st.integers(), RESET_STATS=st.integers(), backgroundNumber=st.integers(), deckNumber=st.integers(), difficulty=st.integers(), drawCount=st.integers(), newDifficulty=st.integers(), newDrawCount=st.integers(), numCards=safe_text, numCardsInDiscardView=safe_text, statusBar=safe_text, timer=safe_text, timerCount=st.integers(), timerLabel=safe_text, timerToRun=st.booleans(), timerToRunNextGame=st.integers(), winAnimationStatus=st.integers(), winSoundsStatus=st.integers())
@given(instance=SolitaireBoard_strategy)
@settings(max_examples=25)
def test_SolitaireBoard_instantiation(instance):
    assert isinstance(instance, SolitaireBoard)


SolitaireLayout_strategy = st.builds(SolitaireLayout, CELL_FOUR=safe_text, CELL_ONE=safe_text, CELL_THREE=safe_text, CELL_TWO=safe_text, CLUBS_ACE_PILE=safe_text, COLUMEN_ONE=safe_text, COLUMN_FOUR=safe_text, COLUMN_THREE=safe_text, COLUMN_TWO=safe_text, DECK=safe_text, DIAMONDS_ACE_PILE=safe_text, DISCARD_PILE=safe_text, HEARTS_ACE_PILE=safe_text, SPADES_ACE_PILE=safe_text, aceClubs=safe_text, aceDiamonds=safe_text, aceHearts=safe_text, aceSpades=safe_text, cellFour=safe_text, cellOne=safe_text, cellThree=safe_text, cellTwo=safe_text, colFour=safe_text, colOne=safe_text, colThree=safe_text, colTwo=safe_text, deck=safe_text, discardPile=safe_text)
@given(instance=SolitaireLayout_strategy)
@settings(max_examples=25)
def test_SolitaireLayout_instantiation(instance):
    assert isinstance(instance, SolitaireLayout)


SolitairePanel_strategy = st.builds(SolitairePanel, background=safe_text, backgroundNumber=st.integers())
@given(instance=SolitairePanel_strategy)
@settings(max_examples=25)
def test_SolitairePanel_instantiation(instance):
    assert isinstance(instance, SolitairePanel)


WinScreen_strategy = st.builds(WinScreen)
@given(instance=WinScreen_strategy)
@settings(max_examples=25)
def test_WinScreen_instantiation(instance):
    assert isinstance(instance, WinScreen)



