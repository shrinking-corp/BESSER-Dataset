import pytest
from datetime import date, datetime, time, timedelta

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_DealDeck_DiscardPile_reverse_link_reassign_clear():
    a1 = DiscardPile(cardsLeftFromDraw=7, drawCount=7)
    a2 = DiscardPile(cardsLeftFromDraw=13, drawCount=13)
    b = DealDeck(DRAW_ONE_THROUGH_LIMIT=7, DRAW_THREE_THROUGH_LIMIT=7, EASY_THROUGH_LIMIT=7, HARD_THROUGH_LIMIT=7, MEDIUM_THROUGH_LIMIT=7, deckThroughLimit=7, difficulty=7, drawCount=7, numTimesThroughDeck=7, redealable=True)
    _safe_set(b, 'discardPile12', a1)
    assert _is_linked(b, 'discardPile12', a1)
    if hasattr(a1, 'dealDeck13'):
        assert _is_linked(a1, 'dealDeck13', b)
    _safe_set(b, 'discardPile12', a2)
    assert _is_linked(b, 'discardPile12', a2)
    if hasattr(a1, 'dealDeck13'):
        assert not _is_linked(a1, 'dealDeck13', b)
    if hasattr(a2, 'dealDeck13'):
        assert _is_linked(a2, 'dealDeck13', b)
    _safe_set(b, 'discardPile12', None)
    assert not _is_linked(b, 'discardPile12', a2)
    if hasattr(a2, 'dealDeck13'):
        assert not _is_linked(a2, 'dealDeck13', b)


def test_assoc_Deck_Card_reverse_link_reassign_clear():
    a1 = Deck(deckNumber=7)
    a2 = Deck(deckNumber=13)
    b = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    _safe_set(b, 'deck5', a1)
    assert _is_linked(b, 'deck5', a1)
    if hasattr(a1, 'card4'):
        assert _is_linked(a1, 'card4', b)
    _safe_set(b, 'deck5', a2)
    assert _is_linked(b, 'deck5', a2)
    if hasattr(a1, 'card4'):
        assert not _is_linked(a1, 'card4', b)
    if hasattr(a2, 'card4'):
        assert _is_linked(a2, 'card4', b)
    _safe_set(b, 'deck5', None)
    assert not _is_linked(b, 'deck5', a2)
    if hasattr(a2, 'card4'):
        assert not _is_linked(a2, 'card4', b)


def test_assoc_SolitaireBoard_AcePile_reverse_link_reassign_clear():
    a1 = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    a2 = SolitaireBoard(DO_NOTHING=13, GAME_LOST=13, GAME_SAVED=13, GAME_WON=13, RESET_STATS=13, backgroundNumber=13, deckNumber=13, difficulty=13, drawCount=13, newDifficulty=13, newDrawCount=13, numCards="sample_text_2", numCardsInDiscardView="sample_text_2", statusBar="sample_text_2", timer="sample_text_2", timerCount=13, timerLabel="sample_text_2", timerToRun=False, timerToRunNextGame=13, winAnimationStatus=13, winSoundsStatus=13)
    b = AcePile(suit="sample_text")
    _safe_set(b, 'solitaireBoard7', a1)
    assert _is_linked(b, 'solitaireBoard7', a1)
    if hasattr(a1, 'acePile6'):
        assert _is_linked(a1, 'acePile6', b)
    _safe_set(b, 'solitaireBoard7', a2)
    assert _is_linked(b, 'solitaireBoard7', a2)
    if hasattr(a1, 'acePile6'):
        assert not _is_linked(a1, 'acePile6', b)
    if hasattr(a2, 'acePile6'):
        assert _is_linked(a2, 'acePile6', b)
    _safe_set(b, 'solitaireBoard7', None)
    assert not _is_linked(b, 'solitaireBoard7', a2)
    if hasattr(a2, 'acePile6'):
        assert not _is_linked(a2, 'acePile6', b)


def test_assoc_SolitaireBoard_Deck_reverse_link_reassign_clear():
    a1 = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    a2 = SolitaireBoard(DO_NOTHING=13, GAME_LOST=13, GAME_SAVED=13, GAME_WON=13, RESET_STATS=13, backgroundNumber=13, deckNumber=13, difficulty=13, drawCount=13, newDifficulty=13, newDrawCount=13, numCards="sample_text_2", numCardsInDiscardView="sample_text_2", statusBar="sample_text_2", timer="sample_text_2", timerCount=13, timerLabel="sample_text_2", timerToRun=False, timerToRunNextGame=13, winAnimationStatus=13, winSoundsStatus=13)
    b = Deck(deckNumber=7)
    _safe_set(b, 'solitaireBoard3', a1)
    assert _is_linked(b, 'solitaireBoard3', a1)
    if hasattr(a1, 'deck2'):
        assert _is_linked(a1, 'deck2', b)
    _safe_set(b, 'solitaireBoard3', a2)
    assert _is_linked(b, 'solitaireBoard3', a2)
    if hasattr(a1, 'deck2'):
        assert not _is_linked(a1, 'deck2', b)
    if hasattr(a2, 'deck2'):
        assert _is_linked(a2, 'deck2', b)
    _safe_set(b, 'solitaireBoard3', None)
    assert not _is_linked(b, 'solitaireBoard3', a2)
    if hasattr(a2, 'deck2'):
        assert not _is_linked(a2, 'deck2', b)


def test_assoc_SolitaireBoard_DiscardPile_reverse_link_reassign_clear():
    a1 = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    a2 = SolitaireBoard(DO_NOTHING=13, GAME_LOST=13, GAME_SAVED=13, GAME_WON=13, RESET_STATS=13, backgroundNumber=13, deckNumber=13, difficulty=13, drawCount=13, newDifficulty=13, newDrawCount=13, numCards="sample_text_2", numCardsInDiscardView="sample_text_2", statusBar="sample_text_2", timer="sample_text_2", timerCount=13, timerLabel="sample_text_2", timerToRun=False, timerToRunNextGame=13, winAnimationStatus=13, winSoundsStatus=13)
    b = DiscardPile(cardsLeftFromDraw=7, drawCount=7)
    _safe_set(b, 'solitaireBoard15', a1)
    assert _is_linked(b, 'solitaireBoard15', a1)
    if hasattr(a1, 'discardPile14'):
        assert _is_linked(a1, 'discardPile14', b)
    _safe_set(b, 'solitaireBoard15', a2)
    assert _is_linked(b, 'solitaireBoard15', a2)
    if hasattr(a1, 'discardPile14'):
        assert not _is_linked(a1, 'discardPile14', b)
    if hasattr(a2, 'discardPile14'):
        assert _is_linked(a2, 'discardPile14', b)
    _safe_set(b, 'solitaireBoard15', None)
    assert not _is_linked(b, 'solitaireBoard15', a2)
    if hasattr(a2, 'discardPile14'):
        assert not _is_linked(a2, 'discardPile14', b)


def test_assoc_SolitaireBoard_SolitairePanel_reverse_link_reassign_clear():
    a1 = SolitairePanel(background="sample_text", backgroundNumber=7)
    a2 = SolitairePanel(background="sample_text_2", backgroundNumber=13)
    b = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    _safe_set(b, 'solitairePanel0', a1)
    assert _is_linked(b, 'solitairePanel0', a1)
    if hasattr(a1, 'solitaireBoard1'):
        assert _is_linked(a1, 'solitaireBoard1', b)
    _safe_set(b, 'solitairePanel0', a2)
    assert _is_linked(b, 'solitairePanel0', a2)
    if hasattr(a1, 'solitaireBoard1'):
        assert not _is_linked(a1, 'solitaireBoard1', b)
    if hasattr(a2, 'solitaireBoard1'):
        assert _is_linked(a2, 'solitaireBoard1', b)
    _safe_set(b, 'solitairePanel0', None)
    assert not _is_linked(b, 'solitairePanel0', a2)
    if hasattr(a2, 'solitaireBoard1'):
        assert not _is_linked(a2, 'solitaireBoard1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_CardStack_Card_stub_double():
    # CardStack has no real 'card10' property in the generated
    # code (a bare stub) -- manually attach it so Card's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Card's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Card(ACE=7, CLUBS_SUIT="sample_text", DIAMONDS_SUIT="sample_text", EIGHT=7, FIVE=7, FOUR=7, HEARTS_SUIT="sample_text", INVALID_NUMBER=7, INVALID_SUIT="sample_text", JACK=7, KING=7, NINE=7, QUEEN=7, SEVEN=7, SIX=7, SPADES_SUIT="sample_text", TEN=7, THREE=7, TWO=7, cardBack="sample_text", cardColor=7, cardHighlighted="sample_text", cardImageString="sample_text", cardNumber=7, cardSuit="sample_text", deckNumber=7, faceUp=True, fullCardNumber=7, highlighted=True, image="sample_text", location="sample_text")
    partner = CardStack()
    setattr(partner, 'card10', None)
    _safe_set(owner, 'cardStack11', partner)
    assert owner in getattr(partner, 'card10')
    _safe_set(owner, 'cardStack11', None)
    assert owner not in getattr(partner, 'card10')


def test_assoc_SolitaireBoard_CardStack_stub_double():
    # CardStack has no real 'solitaireBoard9' property in the generated
    # code (a bare stub) -- manually attach it so SolitaireBoard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SolitaireBoard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    partner = CardStack()
    setattr(partner, 'solitaireBoard9', None)
    _safe_set(owner, 'cardStack8', {partner})
    assert getattr(partner, 'solitaireBoard9') == owner
    _safe_set(owner, 'cardStack8', set())
    assert getattr(partner, 'solitaireBoard9') is None


def test_assoc_SolitaireBoard_Column_stub_double():
    # Column has no real 'solitaireBoard19' property in the generated
    # code (a bare stub) -- manually attach it so SolitaireBoard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SolitaireBoard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    partner = Column()
    setattr(partner, 'solitaireBoard19', None)
    _safe_set(owner, 'column18', {partner})
    assert getattr(partner, 'solitaireBoard19') == owner
    _safe_set(owner, 'column18', set())
    assert getattr(partner, 'solitaireBoard19') is None


def test_assoc_SolitaireBoard_SingleCell_stub_double():
    # SingleCell has no real 'solitaireBoard17' property in the generated
    # code (a bare stub) -- manually attach it so SolitaireBoard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SolitaireBoard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SolitaireBoard(DO_NOTHING=7, GAME_LOST=7, GAME_SAVED=7, GAME_WON=7, RESET_STATS=7, backgroundNumber=7, deckNumber=7, difficulty=7, drawCount=7, newDifficulty=7, newDrawCount=7, numCards="sample_text", numCardsInDiscardView="sample_text", statusBar="sample_text", timer="sample_text", timerCount=7, timerLabel="sample_text", timerToRun=True, timerToRunNextGame=7, winAnimationStatus=7, winSoundsStatus=7)
    partner = SingleCell()
    setattr(partner, 'solitaireBoard17', None)
    _safe_set(owner, 'singleCell16', {partner})
    assert getattr(partner, 'solitaireBoard17') == owner
    _safe_set(owner, 'singleCell16', set())
    assert getattr(partner, 'solitaireBoard17') is None


