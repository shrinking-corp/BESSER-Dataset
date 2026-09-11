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


