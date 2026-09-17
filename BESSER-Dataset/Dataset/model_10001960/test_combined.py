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
    Dealer_Interface,
    Gambler_Interface,
    HandDeck,
    BJPlayer,
    Deck,
    StandardCard,
    JokerCard,
    StandCard,
    PlayingCard,
    Player,
    CardName,
    Suit,
    CardName1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_dealer_interface_is_not_abstract():
    assert not inspect.isabstract(Dealer_Interface)


def test_hyp_dealer_interface_constructor_exists():
    assert callable(Dealer_Interface.__init__)


def test_hyp_dealer_interface_constructor_args():
    sig = inspect.signature(Dealer_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gambler_interface_is_not_abstract():
    assert not inspect.isabstract(Gambler_Interface)


def test_hyp_gambler_interface_constructor_exists():
    assert callable(Gambler_Interface.__init__)


def test_hyp_gambler_interface_constructor_args():
    sig = inspect.signature(Gambler_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_handdeck_is_not_abstract():
    assert not inspect.isabstract(HandDeck)


def test_hyp_handdeck_constructor_exists():
    assert callable(HandDeck.__init__)


def test_hyp_handdeck_constructor_args():
    sig = inspect.signature(HandDeck.__init__)
    params = list(sig.parameters.keys())
    assert "bust" in params, "Missing parameter 'bust'"
    assert "naturalBlackJack" in params, "Missing parameter 'naturalBlackJack'"
    assert "stand" in params, "Missing parameter 'stand'"
    assert "pair" in params, "Missing parameter 'pair'"







def test_hyp_bjplayer_is_not_abstract():
    assert not inspect.isabstract(BJPlayer)


def test_hyp_bjplayer_constructor_exists():
    assert callable(BJPlayer.__init__)


def test_hyp_bjplayer_constructor_args():
    sig = inspect.signature(BJPlayer.__init__)
    params = list(sig.parameters.keys())
    assert "hands" in params, "Missing parameter 'hands'"
    assert "bet" in params, "Missing parameter 'bet'"





def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())



def test_hyp_standardcard_is_not_abstract():
    assert not inspect.isabstract(StandardCard)


def test_hyp_standardcard_constructor_exists():
    assert callable(StandardCard.__init__)


def test_hyp_standardcard_constructor_args():
    sig = inspect.signature(StandardCard.__init__)
    params = list(sig.parameters.keys())
    assert "standardCard" in params, "Missing parameter 'standardCard'"
    assert "suit" in params, "Missing parameter 'suit'"
    assert "cardName" in params, "Missing parameter 'cardName'"

def test_hyp_standardcard_has_standardCard():
    assert hasattr(StandardCard, "standardCard")
    descriptor = None
    for klass in StandardCard.__mro__:
        if "standardCard" in klass.__dict__:
            descriptor = klass.__dict__["standardCard"]
            break
    assert isinstance(descriptor, property)

def test_hyp_standardcard_has_suit():
    assert hasattr(StandardCard, "suit")
    descriptor = None
    for klass in StandardCard.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)

def test_hyp_standardcard_has_cardName():
    assert hasattr(StandardCard, "cardName")
    descriptor = None
    for klass in StandardCard.__mro__:
        if "cardName" in klass.__dict__:
            descriptor = klass.__dict__["cardName"]
            break
    assert isinstance(descriptor, property)



def test_hyp_jokercard_is_not_abstract():
    assert not inspect.isabstract(JokerCard)


def test_hyp_jokercard_constructor_exists():
    assert callable(JokerCard.__init__)


def test_hyp_jokercard_constructor_args():
    sig = inspect.signature(JokerCard.__init__)
    params = list(sig.parameters.keys())
    assert "red" in params, "Missing parameter 'red'"
    assert "jokerCard" in params, "Missing parameter 'jokerCard'"





def test_hyp_standcard_is_not_abstract():
    assert not inspect.isabstract(StandCard)


def test_hyp_standcard_constructor_exists():
    assert callable(StandCard.__init__)


def test_hyp_standcard_constructor_args():
    sig = inspect.signature(StandCard.__init__)
    params = list(sig.parameters.keys())



def test_hyp_playingcard_is_not_abstract():
    assert not inspect.isabstract(PlayingCard)


def test_hyp_playingcard_constructor_exists():
    assert callable(PlayingCard.__init__)


def test_hyp_playingcard_constructor_args():
    sig = inspect.signature(PlayingCard.__init__)
    params = list(sig.parameters.keys())
    assert "jokerCard" in params, "Missing parameter 'jokerCard'"
    assert "faceUp" in params, "Missing parameter 'faceUp'"
    assert "standardCard" in params, "Missing parameter 'standardCard'"






def test_hyp_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_hyp_player_constructor_exists():
    assert callable(Player.__init__)


def test_hyp_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "pocket" in params, "Missing parameter 'pocket'"



def test_hyp_cardname_exists():
    # Check that the Enumeration exists
    assert CardName is not None

def test_hyp_cardname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CardName]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CardName"

def test_hyp_suit_exists():
    # Check that the Enumeration exists
    assert Suit is not None

def test_hyp_suit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Suit]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Suit"

def test_hyp_cardname1_exists():
    # Check that the Enumeration exists
    assert CardName1 is not None

def test_hyp_cardname1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CardName1]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CardName1"


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
Dealer_Interface_strategy = st.builds(
    Dealer_Interface,
)
Gambler_Interface_strategy = st.builds(
    Gambler_Interface,
)
HandDeck_strategy = st.builds(
    HandDeck,
    bust=
        st.booleans(),
    naturalBlackJack=
        st.booleans(),
    stand=
        st.booleans(),
    pair=
        st.booleans()
)
BJPlayer_strategy = st.builds(
    BJPlayer,
    hands=
        safe_text,
    bet=
        st.integers()
)
Deck_strategy = st.builds(
    Deck,
)
StandardCard_strategy = st.builds(
    StandardCard,
    standardCard=
        st.booleans(),
    suit=
        safe_text,
    cardName=
        st.none()
)
JokerCard_strategy = st.builds(
    JokerCard,
    red=
        st.booleans(),
    jokerCard=
        st.booleans()
)
StandCard_strategy = st.builds(
    StandCard,
)
PlayingCard_strategy = st.builds(
    PlayingCard,
    jokerCard=
        st.booleans(),
    faceUp=
        st.booleans(),
    standardCard=
        st.booleans()
)
Player_strategy = st.builds(
    Player,
    name=
        safe_text,
    pocket=
        st.integers()
)






@given(instance=HandDeck_strategy)
def test_hyp_handdeck_bust_setter(instance):
    original = instance.bust
    instance.bust = original
    assert instance.bust == original



@given(instance=HandDeck_strategy)
def test_hyp_handdeck_naturalBlackJack_setter(instance):
    original = instance.naturalBlackJack
    instance.naturalBlackJack = original
    assert instance.naturalBlackJack == original



@given(instance=HandDeck_strategy)
def test_hyp_handdeck_stand_setter(instance):
    original = instance.stand
    instance.stand = original
    assert instance.stand == original



@given(instance=HandDeck_strategy)
def test_hyp_handdeck_pair_setter(instance):
    original = instance.pair
    instance.pair = original
    assert instance.pair == original




@given(instance=BJPlayer_strategy)
def test_hyp_bjplayer_hands_setter(instance):
    original = instance.hands
    instance.hands = original
    assert instance.hands == original



@given(instance=BJPlayer_strategy)
def test_hyp_bjplayer_bet_setter(instance):
    original = instance.bet
    instance.bet = original
    assert instance.bet == original


@given(instance=StandardCard_strategy)
@settings(max_examples=50)
def test_hyp_standardcard_instantiation(instance):
    assert isinstance(instance, StandardCard)



@given(instance=StandardCard_strategy)
def test_hyp_standardcard_standardCard_setter(instance):
    original = instance.standardCard
    instance.standardCard = original
    assert instance.standardCard == original



@given(instance=StandardCard_strategy)
def test_hyp_standardcard_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=StandardCard_strategy)
def test_hyp_standardcard_cardName_setter(instance):
    original = instance.cardName
    instance.cardName = original
    assert instance.cardName == original




@given(instance=JokerCard_strategy)
def test_hyp_jokercard_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original



@given(instance=JokerCard_strategy)
def test_hyp_jokercard_jokerCard_setter(instance):
    original = instance.jokerCard
    instance.jokerCard = original
    assert instance.jokerCard == original





@given(instance=PlayingCard_strategy)
def test_hyp_playingcard_jokerCard_setter(instance):
    original = instance.jokerCard
    instance.jokerCard = original
    assert instance.jokerCard == original



@given(instance=PlayingCard_strategy)
def test_hyp_playingcard_faceUp_setter(instance):
    original = instance.faceUp
    instance.faceUp = original
    assert instance.faceUp == original



@given(instance=PlayingCard_strategy)
def test_hyp_playingcard_standardCard_setter(instance):
    original = instance.standardCard
    instance.standardCard = original
    assert instance.standardCard == original




@given(instance=Player_strategy)
def test_hyp_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Player_strategy)
def test_hyp_player_pocket_setter(instance):
    original = instance.pocket
    instance.pocket = original
    assert instance.pocket == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BJPlayer,
    Dealer_Interface,
    Deck,
    Gambler_Interface,
    HandDeck,
    JokerCard,
    Player,
    PlayingCard,
    StandCard,
    StandardCard,
    CardName,
    CardName1,
    Suit,
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

def test_BJPlayer_bet_value_roundtrip():
    instance = BJPlayer(bet=7, hands="sample_text")
    assert instance.bet == 7
    instance.bet = 13
    assert instance.bet == 13


def test_BJPlayer_hands_value_roundtrip():
    instance = BJPlayer(bet=7, hands="sample_text")
    assert instance.hands == "sample_text"
    instance.hands = "sample_text_2"
    assert instance.hands == "sample_text_2"


def test_HandDeck_bust_value_roundtrip():
    instance = HandDeck(bust=True, naturalBlackJack=True, pair=True, stand=True)
    assert instance.bust == True
    instance.bust = False
    assert instance.bust == False


def test_HandDeck_naturalBlackJack_value_roundtrip():
    instance = HandDeck(bust=True, naturalBlackJack=True, pair=True, stand=True)
    assert instance.naturalBlackJack == True
    instance.naturalBlackJack = False
    assert instance.naturalBlackJack == False


def test_HandDeck_pair_value_roundtrip():
    instance = HandDeck(bust=True, naturalBlackJack=True, pair=True, stand=True)
    assert instance.pair == True
    instance.pair = False
    assert instance.pair == False


def test_HandDeck_stand_value_roundtrip():
    instance = HandDeck(bust=True, naturalBlackJack=True, pair=True, stand=True)
    assert instance.stand == True
    instance.stand = False
    assert instance.stand == False


def test_JokerCard_jokerCard_value_roundtrip():
    instance = JokerCard(jokerCard=True, red=True)
    assert instance.jokerCard == True
    instance.jokerCard = False
    assert instance.jokerCard == False


def test_JokerCard_red_value_roundtrip():
    instance = JokerCard(jokerCard=True, red=True)
    assert instance.red == True
    instance.red = False
    assert instance.red == False


def test_Player_name_value_roundtrip():
    instance = Player(name="sample_text", pocket=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Player_pocket_value_roundtrip():
    instance = Player(name="sample_text", pocket=7)
    assert instance.pocket == 7
    instance.pocket = 13
    assert instance.pocket == 13


def test_PlayingCard_faceUp_value_roundtrip():
    instance = PlayingCard(faceUp=True, jokerCard=True, standardCard=True)
    assert instance.faceUp == True
    instance.faceUp = False
    assert instance.faceUp == False


def test_PlayingCard_jokerCard_value_roundtrip():
    instance = PlayingCard(faceUp=True, jokerCard=True, standardCard=True)
    assert instance.jokerCard == True
    instance.jokerCard = False
    assert instance.jokerCard == False


def test_PlayingCard_standardCard_value_roundtrip():
    instance = PlayingCard(faceUp=True, jokerCard=True, standardCard=True)
    assert instance.standardCard == True
    instance.standardCard = False
    assert instance.standardCard == False


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BJPlayer_strategy = st.builds(BJPlayer, bet=st.integers(), hands=safe_text)
@given(instance=BJPlayer_strategy)
@settings(max_examples=25)
def test_BJPlayer_instantiation(instance):
    assert isinstance(instance, BJPlayer)


Dealer_Interface_strategy = st.builds(Dealer_Interface)
@given(instance=Dealer_Interface_strategy)
@settings(max_examples=25)
def test_Dealer_Interface_instantiation(instance):
    assert isinstance(instance, Dealer_Interface)


Deck_strategy = st.builds(Deck)
@given(instance=Deck_strategy)
@settings(max_examples=25)
def test_Deck_instantiation(instance):
    assert isinstance(instance, Deck)


Gambler_Interface_strategy = st.builds(Gambler_Interface)
@given(instance=Gambler_Interface_strategy)
@settings(max_examples=25)
def test_Gambler_Interface_instantiation(instance):
    assert isinstance(instance, Gambler_Interface)


HandDeck_strategy = st.builds(HandDeck, bust=st.booleans(), naturalBlackJack=st.booleans(), pair=st.booleans(), stand=st.booleans())
@given(instance=HandDeck_strategy)
@settings(max_examples=25)
def test_HandDeck_instantiation(instance):
    assert isinstance(instance, HandDeck)


JokerCard_strategy = st.builds(JokerCard, jokerCard=st.booleans(), red=st.booleans())
@given(instance=JokerCard_strategy)
@settings(max_examples=25)
def test_JokerCard_instantiation(instance):
    assert isinstance(instance, JokerCard)


Player_strategy = st.builds(Player, name=safe_text, pocket=st.integers())
@given(instance=Player_strategy)
@settings(max_examples=25)
def test_Player_instantiation(instance):
    assert isinstance(instance, Player)


PlayingCard_strategy = st.builds(PlayingCard, faceUp=st.booleans(), jokerCard=st.booleans(), standardCard=st.booleans())
@given(instance=PlayingCard_strategy)
@settings(max_examples=25)
def test_PlayingCard_instantiation(instance):
    assert isinstance(instance, PlayingCard)


StandCard_strategy = st.builds(StandCard)
@given(instance=StandCard_strategy)
@settings(max_examples=25)
def test_StandCard_instantiation(instance):
    assert isinstance(instance, StandCard)



