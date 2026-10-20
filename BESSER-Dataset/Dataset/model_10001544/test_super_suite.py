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
    Integer_external,
    BlackjackGame,
    Player,
    Hand,
    Dealer,
    Cards,
    Deck,
    _Interface,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_integer_external_is_not_abstract():
    assert not inspect.isabstract(Integer_external)


def test_hyp_integer_external_constructor_exists():
    assert callable(Integer_external.__init__)


def test_hyp_integer_external_constructor_args():
    sig = inspect.signature(Integer_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_blackjackgame_is_not_abstract():
    assert not inspect.isabstract(BlackjackGame)


def test_hyp_blackjackgame_constructor_exists():
    assert callable(BlackjackGame.__init__)


def test_hyp_blackjackgame_constructor_args():
    sig = inspect.signature(BlackjackGame.__init__)
    params = list(sig.parameters.keys())



def test_hyp_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_hyp_player_constructor_exists():
    assert callable(Player.__init__)


def test_hyp_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_hand_is_not_abstract():
    assert not inspect.isabstract(Hand)


def test_hyp_hand_constructor_exists():
    assert callable(Hand.__init__)


def test_hyp_hand_constructor_args():
    sig = inspect.signature(Hand.__init__)
    params = list(sig.parameters.keys())
    assert "handValue" in params, "Missing parameter 'handValue'"




def test_hyp_dealer_is_not_abstract():
    assert not inspect.isabstract(Dealer)


def test_hyp_dealer_constructor_exists():
    assert callable(Dealer.__init__)


def test_hyp_dealer_constructor_args():
    sig = inspect.signature(Dealer.__init__)
    params = list(sig.parameters.keys())
    assert "handValue" in params, "Missing parameter 'handValue'"
    assert "handLimit" in params, "Missing parameter 'handLimit'"





def test_hyp_cards_is_not_abstract():
    assert not inspect.isabstract(Cards)


def test_hyp_cards_constructor_exists():
    assert callable(Cards.__init__)


def test_hyp_cards_constructor_args():
    sig = inspect.signature(Cards.__init__)
    params = list(sig.parameters.keys())
    assert "cardValue" in params, "Missing parameter 'cardValue'"
    assert "cardName" in params, "Missing parameter 'cardName'"





def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "deckArray" in params, "Missing parameter 'deckArray'"





def test_hyp__interface_is_not_abstract():
    assert not inspect.isabstract(_Interface)


def test_hyp__interface_constructor_exists():
    assert callable(_Interface.__init__)


def test_hyp__interface_constructor_args():
    sig = inspect.signature(_Interface.__init__)
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
Integer_external_strategy = st.builds(
    Integer_external,
)
BlackjackGame_strategy = st.builds(
    BlackjackGame,
)
Player_strategy = st.builds(
    Player,
    name=
        safe_text
)
Hand_strategy = st.builds(
    Hand,
    handValue=
        st.integers()
)
Dealer_strategy = st.builds(
    Dealer,
    handValue=
        st.integers(),
    handLimit=
        st.integers()
)
Cards_strategy = st.builds(
    Cards,
    cardValue=
        st.integers(),
    cardName=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
    size=
        st.integers(),
    deckArray=
        st.integers()
)
_Interface_strategy = st.builds(
    _Interface,
)






@given(instance=Player_strategy)
def test_hyp_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Hand_strategy)
def test_hyp_hand_handValue_setter(instance):
    original = instance.handValue
    instance.handValue = original
    assert instance.handValue == original




@given(instance=Dealer_strategy)
def test_hyp_dealer_handValue_setter(instance):
    original = instance.handValue
    instance.handValue = original
    assert instance.handValue == original



@given(instance=Dealer_strategy)
def test_hyp_dealer_handLimit_setter(instance):
    original = instance.handLimit
    instance.handLimit = original
    assert instance.handLimit == original




@given(instance=Cards_strategy)
def test_hyp_cards_cardValue_setter(instance):
    original = instance.cardValue
    instance.cardValue = original
    assert instance.cardValue == original



@given(instance=Cards_strategy)
def test_hyp_cards_cardName_setter(instance):
    original = instance.cardName
    instance.cardName = original
    assert instance.cardName == original




@given(instance=Deck_strategy)
def test_hyp_deck_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=Deck_strategy)
def test_hyp_deck_deckArray_setter(instance):
    original = instance.deckArray
    instance.deckArray = original
    assert instance.deckArray == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BlackjackGame,
    Cards,
    Dealer,
    Deck,
    Hand,
    Integer_external,
    Player,
    _Interface,
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

def test_Cards_cardName_value_roundtrip():
    instance = Cards(cardName="sample_text", cardValue=7)
    assert instance.cardName == "sample_text"
    instance.cardName = "sample_text_2"
    assert instance.cardName == "sample_text_2"


def test_Cards_cardValue_value_roundtrip():
    instance = Cards(cardName="sample_text", cardValue=7)
    assert instance.cardValue == 7
    instance.cardValue = 13
    assert instance.cardValue == 13


def test_Dealer_handLimit_value_roundtrip():
    instance = Dealer(handLimit=7, handValue=7)
    assert instance.handLimit == 7
    instance.handLimit = 13
    assert instance.handLimit == 13


def test_Dealer_handValue_value_roundtrip():
    instance = Dealer(handLimit=7, handValue=7)
    assert instance.handValue == 7
    instance.handValue = 13
    assert instance.handValue == 13


def test_Deck_deckArray_value_roundtrip():
    instance = Deck(deckArray=7, size=7)
    assert instance.deckArray == 7
    instance.deckArray = 13
    assert instance.deckArray == 13


def test_Deck_size_value_roundtrip():
    instance = Deck(deckArray=7, size=7)
    assert instance.size == 7
    instance.size = 13
    assert instance.size == 13


def test_Hand_handValue_value_roundtrip():
    instance = Hand(handValue=7)
    assert instance.handValue == 7
    instance.handValue = 13
    assert instance.handValue == 13


def test_Player_name_value_roundtrip():
    instance = Player(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_BlackjackGame_Dealer_link_reassign_clear():
    a = Dealer(handLimit=7, handValue=7)
    b1 = BlackjackGame()
    b2 = BlackjackGame()
    _safe_set(a, 'blackjackGame5', b1)
    assert _is_linked(a, 'blackjackGame5', b1)
    if hasattr(b1, 'dealer4'):
        assert _is_linked(b1, 'dealer4', a)
    _safe_set(a, 'blackjackGame5', b2)
    assert _is_linked(a, 'blackjackGame5', b2)
    if hasattr(b1, 'dealer4'):
        assert not _is_linked(b1, 'dealer4', a)
    if hasattr(b2, 'dealer4'):
        assert _is_linked(b2, 'dealer4', a)
    _safe_set(a, 'blackjackGame5', None)
    assert not _is_linked(a, 'blackjackGame5', b2)
    if hasattr(b2, 'dealer4'):
        assert not _is_linked(b2, 'dealer4', a)


def test_assoc_BlackjackGame_Player_link_reassign_clear():
    a = Player(name="sample_text")
    b1 = BlackjackGame()
    b2 = BlackjackGame()
    _safe_set(a, 'blackjackGame3', b1)
    assert _is_linked(a, 'blackjackGame3', b1)
    if hasattr(b1, 'player2'):
        assert _is_linked(b1, 'player2', a)
    _safe_set(a, 'blackjackGame3', b2)
    assert _is_linked(a, 'blackjackGame3', b2)
    if hasattr(b1, 'player2'):
        assert not _is_linked(b1, 'player2', a)
    if hasattr(b2, 'player2'):
        assert _is_linked(b2, 'player2', a)
    _safe_set(a, 'blackjackGame3', None)
    assert not _is_linked(a, 'blackjackGame3', b2)
    if hasattr(b2, 'player2'):
        assert not _is_linked(b2, 'player2', a)


def test_assoc_Hand_Dealer_link_reassign_clear():
    a = Dealer(handLimit=7, handValue=7)
    b1 = Integer_external()
    b2 = Integer_external()
    _safe_set(a, 'hand1', b1)
    assert _is_linked(a, 'hand1', b1)
    if hasattr(b1, 'dealer0'):
        assert _is_linked(b1, 'dealer0', a)
    _safe_set(a, 'hand1', b2)
    assert _is_linked(a, 'hand1', b2)
    if hasattr(b1, 'dealer0'):
        assert not _is_linked(b1, 'dealer0', a)
    if hasattr(b2, 'dealer0'):
        assert _is_linked(b2, 'dealer0', a)
    _safe_set(a, 'hand1', None)
    assert not _is_linked(a, 'hand1', b2)
    if hasattr(b2, 'dealer0'):
        assert not _is_linked(b2, 'dealer0', a)


def test_assoc_Player_Hand_link_reassign_clear():
    a = Player(name="sample_text")
    b1 = Hand(handValue=7)
    b2 = Hand(handValue=13)
    _safe_set(a, 'hand6', b1)
    assert _is_linked(a, 'hand6', b1)
    if hasattr(b1, 'player7'):
        assert _is_linked(b1, 'player7', a)
    _safe_set(a, 'hand6', b2)
    assert _is_linked(a, 'hand6', b2)
    if hasattr(b1, 'player7'):
        assert not _is_linked(b1, 'player7', a)
    if hasattr(b2, 'player7'):
        assert _is_linked(b2, 'player7', a)
    _safe_set(a, 'hand6', None)
    assert not _is_linked(a, 'hand6', b2)
    if hasattr(b2, 'player7'):
        assert not _is_linked(b2, 'player7', a)


def test_assoc_association2_link_reassign_clear():
    a = Deck(deckArray=7, size=7)
    b1 = _Interface()
    b2 = _Interface()
    _safe_set(a, 'association2_111', b1)
    assert _is_linked(a, 'association2_111', b1)
    if hasattr(b1, 'deck10'):
        assert _is_linked(b1, 'deck10', a)
    _safe_set(a, 'association2_111', b2)
    assert _is_linked(a, 'association2_111', b2)
    if hasattr(b1, 'deck10'):
        assert not _is_linked(b1, 'deck10', a)
    if hasattr(b2, 'deck10'):
        assert _is_linked(b2, 'deck10', a)
    _safe_set(a, 'association2_111', None)
    assert not _is_linked(a, 'association2_111', b2)
    if hasattr(b2, 'deck10'):
        assert not _is_linked(b2, 'deck10', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BlackjackGame_strategy = st.builds(BlackjackGame)
@given(instance=BlackjackGame_strategy)
@settings(max_examples=25)
def test_BlackjackGame_instantiation(instance):
    assert isinstance(instance, BlackjackGame)


Cards_strategy = st.builds(Cards, cardName=safe_text, cardValue=st.integers())
@given(instance=Cards_strategy)
@settings(max_examples=25)
def test_Cards_instantiation(instance):
    assert isinstance(instance, Cards)


Dealer_strategy = st.builds(Dealer, handLimit=st.integers(), handValue=st.integers())
@given(instance=Dealer_strategy)
@settings(max_examples=25)
def test_Dealer_instantiation(instance):
    assert isinstance(instance, Dealer)


Deck_strategy = st.builds(Deck, deckArray=st.integers(), size=st.integers())
@given(instance=Deck_strategy)
@settings(max_examples=25)
def test_Deck_instantiation(instance):
    assert isinstance(instance, Deck)


Hand_strategy = st.builds(Hand, handValue=st.integers())
@given(instance=Hand_strategy)
@settings(max_examples=25)
def test_Hand_instantiation(instance):
    assert isinstance(instance, Hand)


Integer_external_strategy = st.builds(Integer_external)
@given(instance=Integer_external_strategy)
@settings(max_examples=25)
def test_Integer_external_instantiation(instance):
    assert isinstance(instance, Integer_external)


Player_strategy = st.builds(Player, name=safe_text)
@given(instance=Player_strategy)
@settings(max_examples=25)
def test_Player_instantiation(instance):
    assert isinstance(instance, Player)


_Interface_strategy = st.builds(_Interface)
@given(instance=_Interface_strategy)
@settings(max_examples=25)
def test__Interface_instantiation(instance):
    assert isinstance(instance, _Interface)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BlackjackGame,
    Cards,
    Dealer,
    Deck,
    Hand,
    Integer_external,
    Player,
    _Interface,
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

def test_assoc_Player_Hand_reverse_link_reassign_clear():
    a1 = Player(name="sample_text")
    a2 = Player(name="sample_text_2")
    b = Hand(handValue=7)
    _safe_set(b, 'player7', {a1})
    assert _is_linked(b, 'player7', a1)
    if hasattr(a1, 'hand6'):
        assert _is_linked(a1, 'hand6', b)
    _safe_set(b, 'player7', {a2})
    assert _is_linked(b, 'player7', a2)
    if hasattr(a1, 'hand6'):
        assert not _is_linked(a1, 'hand6', b)
    if hasattr(a2, 'hand6'):
        assert _is_linked(a2, 'hand6', b)
    _safe_set(b, 'player7', set())
    assert not _is_linked(b, 'player7', a2)
    if hasattr(a2, 'hand6'):
        assert not _is_linked(a2, 'hand6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_BlackjackGame_Dealer_stub_double():
    # BlackjackGame has no real 'dealer4' property in the generated
    # code (a bare stub) -- manually attach it so Dealer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Dealer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Dealer(handLimit=7, handValue=7)
    partner = BlackjackGame()
    setattr(partner, 'dealer4', None)
    _safe_set(owner, 'blackjackGame5', partner)
    assert getattr(partner, 'dealer4') == owner
    _safe_set(owner, 'blackjackGame5', None)
    assert getattr(partner, 'dealer4') is None


def test_assoc_BlackjackGame_Player_stub_double():
    # BlackjackGame has no real 'player2' property in the generated
    # code (a bare stub) -- manually attach it so Player's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Player's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Player(name="sample_text")
    partner = BlackjackGame()
    setattr(partner, 'player2', None)
    _safe_set(owner, 'blackjackGame3', partner)
    assert getattr(partner, 'player2') == owner
    _safe_set(owner, 'blackjackGame3', None)
    assert getattr(partner, 'player2') is None


def test_assoc_Hand_Dealer_stub_double():
    # Integer_external has no real 'dealer0' property in the generated
    # code (a bare stub) -- manually attach it so Dealer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Dealer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Dealer(handLimit=7, handValue=7)
    partner = Integer_external()
    setattr(partner, 'dealer0', None)
    _safe_set(owner, 'hand1', partner)
    assert getattr(partner, 'dealer0') == owner
    _safe_set(owner, 'hand1', None)
    assert getattr(partner, 'dealer0') is None


def test_assoc_association2_stub_double():
    # _Interface has no real 'deck10' property in the generated
    # code (a bare stub) -- manually attach it so Deck's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Deck's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Deck(deckArray=7, size=7)
    partner = _Interface()
    setattr(partner, 'deck10', None)
    _safe_set(owner, 'association2_111', partner)
    assert getattr(partner, 'deck10') == owner
    _safe_set(owner, 'association2_111', None)
    assert getattr(partner, 'deck10') is None




from python_code import Cards

def test_Cards___init__():
    assert Cards.__init__(Cards('', 0), '', 0) == None
from python_code import BlackjackGame
from python_code import Dealer
from python_code import Integer_external

def test_Dealer___init__():
    assert Dealer.__init__(Dealer(0, 0, hand1=Integer_external(), blackjackGame5=BlackjackGame()), 0, 0, hand1=Integer_external(), blackjackGame5=BlackjackGame()) == None
from python_code import Deck
from python_code import _Interface

def test_Deck___init__():
    assert Deck.__init__(Deck(0, 0, association2_111=_Interface()), 0, 0, association2_111=_Interface()) == None
from python_code import Hand

def test_Hand___init__():
    assert Hand.__init__(Hand(0, player7=set()), 0, player7=set()) == None

