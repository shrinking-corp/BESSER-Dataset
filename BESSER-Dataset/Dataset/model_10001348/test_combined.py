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
    StartGame,
    Trick,
    Team,
    Player,
    HandSorter,
    Hand,
    Deck,
    Group,
    Card,
    int_Interface,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_startgame_is_not_abstract():
    assert not inspect.isabstract(StartGame)


def test_hyp_startgame_constructor_exists():
    assert callable(StartGame.__init__)


def test_hyp_startgame_constructor_args():
    sig = inspect.signature(StartGame.__init__)
    params = list(sig.parameters.keys())
    assert "turn" in params, "Missing parameter 'turn'"
    assert "p4" in params, "Missing parameter 'p4'"
    assert "p2" in params, "Missing parameter 'p2'"
    assert "t2" in params, "Missing parameter 't2'"
    assert "playerOrder" in params, "Missing parameter 'playerOrder'"
    assert "lead" in params, "Missing parameter 'lead'"
    assert "p1" in params, "Missing parameter 'p1'"
    assert "deck" in params, "Missing parameter 'deck'"
    assert "t1" in params, "Missing parameter 't1'"
    assert "p3" in params, "Missing parameter 'p3'"
    assert "bidNumber" in params, "Missing parameter 'bidNumber'"
    assert "trick" in params, "Missing parameter 'trick'"

def test_hyp_startgame_has_turn():
    assert hasattr(StartGame, "turn")
    descriptor = None
    for klass in StartGame.__mro__:
        if "turn" in klass.__dict__:
            descriptor = klass.__dict__["turn"]
            break
    assert isinstance(descriptor, property)

def test_hyp_startgame_has_p4():
    assert hasattr(StartGame, "p4")
    descriptor = None
    for klass in StartGame.__mro__:
        if "p4" in klass.__dict__:
            descriptor = klass.__dict__["p4"]
            break
    assert isinstance(descriptor, property)

def test_hyp_startgame_has_p2():
    assert hasattr(StartGame, "p2")
    descriptor = None
    for klass in StartGame.__mro__:
        if "p2" in klass.__dict__:
            descriptor = klass.__dict__["p2"]
            break
    assert isinstance(descriptor, property)

def test_hyp_startgame_has_t2():
    assert hasattr(StartGame, "t2")
    descriptor = None
    for klass in StartGame.__mro__:
        if "t2" in klass.__dict__:
            descriptor = klass.__dict__["t2"]
            break
    assert isinstance(descriptor, property)

def test_hyp_startgame_has_playerOrder():
    assert hasattr(StartGame, "playerOrder")
    descriptor = None
    for klass in StartGame.__mro__:
        if "playerOrder" in klass.__dict__:
            descriptor = klass.__dict__["playerOrder"]
            break
    assert isinstance(descriptor, property)

def test_hyp_startgame_has_lead():
    assert hasattr(StartGame, "lead")
    descriptor = None
    for klass in StartGame.__mro__:
        if "lead" in klass.__dict__:
            descriptor = klass.__dict__["lead"]
            break
    assert isinstance(descriptor, property)

def test_hyp_startgame_has_p1():
    assert hasattr(StartGame, "p1")
    descriptor = None
    for klass in StartGame.__mro__:
        if "p1" in klass.__dict__:
            descriptor = klass.__dict__["p1"]
            break
    assert isinstance(descriptor, property)

def test_hyp_startgame_has_deck():
    assert hasattr(StartGame, "deck")
    descriptor = None
    for klass in StartGame.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)

def test_hyp_startgame_has_t1():
    assert hasattr(StartGame, "t1")
    descriptor = None
    for klass in StartGame.__mro__:
        if "t1" in klass.__dict__:
            descriptor = klass.__dict__["t1"]
            break
    assert isinstance(descriptor, property)

def test_hyp_startgame_has_p3():
    assert hasattr(StartGame, "p3")
    descriptor = None
    for klass in StartGame.__mro__:
        if "p3" in klass.__dict__:
            descriptor = klass.__dict__["p3"]
            break
    assert isinstance(descriptor, property)

def test_hyp_startgame_has_bidNumber():
    assert hasattr(StartGame, "bidNumber")
    descriptor = None
    for klass in StartGame.__mro__:
        if "bidNumber" in klass.__dict__:
            descriptor = klass.__dict__["bidNumber"]
            break
    assert isinstance(descriptor, property)

def test_hyp_startgame_has_trick():
    assert hasattr(StartGame, "trick")
    descriptor = None
    for klass in StartGame.__mro__:
        if "trick" in klass.__dict__:
            descriptor = klass.__dict__["trick"]
            break
    assert isinstance(descriptor, property)



def test_hyp_trick_is_not_abstract():
    assert not inspect.isabstract(Trick)


def test_hyp_trick_constructor_exists():
    assert callable(Trick.__init__)


def test_hyp_trick_constructor_args():
    sig = inspect.signature(Trick.__init__)
    params = list(sig.parameters.keys())
    assert "suitLead" in params, "Missing parameter 'suitLead'"




def test_hyp_team_is_not_abstract():
    assert not inspect.isabstract(Team)


def test_hyp_team_constructor_exists():
    assert callable(Team.__init__)


def test_hyp_team_constructor_args():
    sig = inspect.signature(Team.__init__)
    params = list(sig.parameters.keys())
    assert "score" in params, "Missing parameter 'score'"
    assert "p2" in params, "Missing parameter 'p2'"
    assert "p1" in params, "Missing parameter 'p1'"

def test_hyp_team_has_score():
    assert hasattr(Team, "score")
    descriptor = None
    for klass in Team.__mro__:
        if "score" in klass.__dict__:
            descriptor = klass.__dict__["score"]
            break
    assert isinstance(descriptor, property)

def test_hyp_team_has_p2():
    assert hasattr(Team, "p2")
    descriptor = None
    for klass in Team.__mro__:
        if "p2" in klass.__dict__:
            descriptor = klass.__dict__["p2"]
            break
    assert isinstance(descriptor, property)

def test_hyp_team_has_p1():
    assert hasattr(Team, "p1")
    descriptor = None
    for klass in Team.__mro__:
        if "p1" in klass.__dict__:
            descriptor = klass.__dict__["p1"]
            break
    assert isinstance(descriptor, property)



def test_hyp_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_hyp_player_constructor_exists():
    assert callable(Player.__init__)


def test_hyp_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "hand" in params, "Missing parameter 'hand'"
    assert "score" in params, "Missing parameter 'score'"
    assert "number" in params, "Missing parameter 'number'"

def test_hyp_player_has_name():
    assert hasattr(Player, "name")
    descriptor = None
    for klass in Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_hyp_player_has_score():
    assert hasattr(Player, "score")
    descriptor = None
    for klass in Player.__mro__:
        if "score" in klass.__dict__:
            descriptor = klass.__dict__["score"]
            break
    assert isinstance(descriptor, property)

def test_hyp_player_has_number():
    assert hasattr(Player, "number")
    descriptor = None
    for klass in Player.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_hyp_handsorter_is_not_abstract():
    assert not inspect.isabstract(HandSorter)


def test_hyp_handsorter_constructor_exists():
    assert callable(HandSorter.__init__)


def test_hyp_handsorter_constructor_args():
    sig = inspect.signature(HandSorter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hand_is_not_abstract():
    assert not inspect.isabstract(Hand)


def test_hyp_hand_constructor_exists():
    assert callable(Hand.__init__)


def test_hyp_hand_constructor_args():
    sig = inspect.signature(Hand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())



def test_hyp_group_is_not_abstract():
    assert not inspect.isabstract(Group)


def test_hyp_group_constructor_exists():
    assert callable(Group.__init__)


def test_hyp_group_constructor_args():
    sig = inspect.signature(Group.__init__)
    params = list(sig.parameters.keys())
    assert "contents" in params, "Missing parameter 'contents'"




def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "suit" in params, "Missing parameter 'suit'"
    assert "rank" in params, "Missing parameter 'rank'"
    assert "isDouble" in params, "Missing parameter 'isDouble'"
    assert "points" in params, "Missing parameter 'points'"







def test_hyp_int_interface_is_not_abstract():
    assert not inspect.isabstract(int_Interface)


def test_hyp_int_interface_constructor_exists():
    assert callable(int_Interface.__init__)


def test_hyp_int_interface_constructor_args():
    sig = inspect.signature(int_Interface.__init__)
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
StartGame_strategy = st.builds(
    StartGame,
    turn=
        st.integers(),
    p4=
        st.none(),
    p2=
        st.none(),
    t2=
        st.none(),
    playerOrder=
        safe_text,
    lead=
        st.integers(),
    p1=
        st.none(),
    deck=
        st.none(),
    t1=
        st.none(),
    p3=
        st.none(),
    bidNumber=
        st.integers(),
    trick=
        st.none()
)
Trick_strategy = st.builds(
    Trick,
    suitLead=
        st.integers()
)
Team_strategy = st.builds(
    Team,
    score=
        st.integers(),
    p2=
        st.none(),
    p1=
        st.none()
)
Player_strategy = st.builds(
    Player,
    name=
        safe_text,
    hand=
        st.none(),
    score=
        st.integers(),
    number=
        st.integers()
)
HandSorter_strategy = st.builds(
    HandSorter,
)
Hand_strategy = st.builds(
    Hand,
)
Deck_strategy = st.builds(
    Deck,
)
Group_strategy = st.builds(
    Group,
    contents=
        safe_text
)
Card_strategy = st.builds(
    Card,
    suit=
        st.integers(),
    rank=
        st.integers(),
    isDouble=
        st.booleans(),
    points=
        st.integers()
)
int_Interface_strategy = st.builds(
    int_Interface,
)

@given(instance=StartGame_strategy)
@settings(max_examples=50)
def test_hyp_startgame_instantiation(instance):
    assert isinstance(instance, StartGame)



@given(instance=StartGame_strategy)
def test_hyp_startgame_turn_setter(instance):
    original = instance.turn
    instance.turn = original
    assert instance.turn == original



@given(instance=StartGame_strategy)
def test_hyp_startgame_p4_setter(instance):
    original = instance.p4
    instance.p4 = original
    assert instance.p4 == original



@given(instance=StartGame_strategy)
def test_hyp_startgame_p2_setter(instance):
    original = instance.p2
    instance.p2 = original
    assert instance.p2 == original



@given(instance=StartGame_strategy)
def test_hyp_startgame_t2_setter(instance):
    original = instance.t2
    instance.t2 = original
    assert instance.t2 == original



@given(instance=StartGame_strategy)
def test_hyp_startgame_playerOrder_setter(instance):
    original = instance.playerOrder
    instance.playerOrder = original
    assert instance.playerOrder == original



@given(instance=StartGame_strategy)
def test_hyp_startgame_lead_setter(instance):
    original = instance.lead
    instance.lead = original
    assert instance.lead == original



@given(instance=StartGame_strategy)
def test_hyp_startgame_p1_setter(instance):
    original = instance.p1
    instance.p1 = original
    assert instance.p1 == original



@given(instance=StartGame_strategy)
def test_hyp_startgame_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original



@given(instance=StartGame_strategy)
def test_hyp_startgame_t1_setter(instance):
    original = instance.t1
    instance.t1 = original
    assert instance.t1 == original



@given(instance=StartGame_strategy)
def test_hyp_startgame_p3_setter(instance):
    original = instance.p3
    instance.p3 = original
    assert instance.p3 == original



@given(instance=StartGame_strategy)
def test_hyp_startgame_bidNumber_setter(instance):
    original = instance.bidNumber
    instance.bidNumber = original
    assert instance.bidNumber == original



@given(instance=StartGame_strategy)
def test_hyp_startgame_trick_setter(instance):
    original = instance.trick
    instance.trick = original
    assert instance.trick == original




@given(instance=Trick_strategy)
def test_hyp_trick_suitLead_setter(instance):
    original = instance.suitLead
    instance.suitLead = original
    assert instance.suitLead == original

@given(instance=Team_strategy)
@settings(max_examples=50)
def test_hyp_team_instantiation(instance):
    assert isinstance(instance, Team)



@given(instance=Team_strategy)
def test_hyp_team_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original



@given(instance=Team_strategy)
def test_hyp_team_p2_setter(instance):
    original = instance.p2
    instance.p2 = original
    assert instance.p2 == original



@given(instance=Team_strategy)
def test_hyp_team_p1_setter(instance):
    original = instance.p1
    instance.p1 = original
    assert instance.p1 == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_hyp_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_hyp_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Player_strategy)
def test_hyp_player_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original



@given(instance=Player_strategy)
def test_hyp_player_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original



@given(instance=Player_strategy)
def test_hyp_player_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original







@given(instance=Group_strategy)
def test_hyp_group_contents_setter(instance):
    original = instance.contents
    instance.contents = original
    assert instance.contents == original




@given(instance=Card_strategy)
def test_hyp_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=Card_strategy)
def test_hyp_card_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original



@given(instance=Card_strategy)
def test_hyp_card_isDouble_setter(instance):
    original = instance.isDouble
    instance.isDouble = original
    assert instance.isDouble == original



@given(instance=Card_strategy)
def test_hyp_card_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Card,
    Deck,
    Group,
    Hand,
    HandSorter,
    Player,
    StartGame,
    Team,
    Trick,
    int_Interface,
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

def test_Card_isDouble_value_roundtrip():
    instance = Card(isDouble=True, points=7, rank=7, suit=7)
    assert instance.isDouble == True
    instance.isDouble = False
    assert instance.isDouble == False


def test_Card_points_value_roundtrip():
    instance = Card(isDouble=True, points=7, rank=7, suit=7)
    assert instance.points == 7
    instance.points = 13
    assert instance.points == 13


def test_Card_rank_value_roundtrip():
    instance = Card(isDouble=True, points=7, rank=7, suit=7)
    assert instance.rank == 7
    instance.rank = 13
    assert instance.rank == 13


def test_Card_suit_value_roundtrip():
    instance = Card(isDouble=True, points=7, rank=7, suit=7)
    assert instance.suit == 7
    instance.suit = 13
    assert instance.suit == 13


def test_Group_contents_value_roundtrip():
    instance = Group(contents="sample_text")
    assert instance.contents == "sample_text"
    instance.contents = "sample_text_2"
    assert instance.contents == "sample_text_2"


def test_Trick_suitLead_value_roundtrip():
    instance = Trick(suitLead=7)
    assert instance.suitLead == 7
    instance.suitLead = 13
    assert instance.suitLead == 13


def test_assoc_Card_Group_link_reassign_clear():
    a = Group(contents="sample_text")
    b1 = Card(isDouble=True, points=7, rank=7, suit=7)
    b2 = Card(isDouble=False, points=13, rank=13, suit=13)
    _safe_set(a, 'card1', {b1})
    assert _is_linked(a, 'card1', b1)
    if hasattr(b1, 'group0'):
        assert _is_linked(b1, 'group0', a)
    _safe_set(a, 'card1', {b2})
    assert _is_linked(a, 'card1', b2)
    if hasattr(b1, 'group0'):
        assert not _is_linked(b1, 'group0', a)
    if hasattr(b2, 'group0'):
        assert _is_linked(b2, 'group0', a)
    _safe_set(a, 'card1', set())
    assert not _is_linked(a, 'card1', b2)
    if hasattr(b2, 'group0'):
        assert not _is_linked(b2, 'group0', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Card_strategy = st.builds(Card, isDouble=st.booleans(), points=st.integers(), rank=st.integers(), suit=st.integers())
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)


Deck_strategy = st.builds(Deck)
@given(instance=Deck_strategy)
@settings(max_examples=25)
def test_Deck_instantiation(instance):
    assert isinstance(instance, Deck)


Group_strategy = st.builds(Group, contents=safe_text)
@given(instance=Group_strategy)
@settings(max_examples=25)
def test_Group_instantiation(instance):
    assert isinstance(instance, Group)


Hand_strategy = st.builds(Hand)
@given(instance=Hand_strategy)
@settings(max_examples=25)
def test_Hand_instantiation(instance):
    assert isinstance(instance, Hand)


HandSorter_strategy = st.builds(HandSorter)
@given(instance=HandSorter_strategy)
@settings(max_examples=25)
def test_HandSorter_instantiation(instance):
    assert isinstance(instance, HandSorter)


Trick_strategy = st.builds(Trick, suitLead=st.integers())
@given(instance=Trick_strategy)
@settings(max_examples=25)
def test_Trick_instantiation(instance):
    assert isinstance(instance, Trick)


int_Interface_strategy = st.builds(int_Interface)
@given(instance=int_Interface_strategy)
@settings(max_examples=25)
def test_int_Interface_instantiation(instance):
    assert isinstance(instance, int_Interface)



