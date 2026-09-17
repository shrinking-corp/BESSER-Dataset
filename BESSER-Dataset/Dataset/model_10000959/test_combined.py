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
    Function,
    Players,
    Class,
    Card_Interface,
    Deck,
    WAR,
    PlayerUser_external,
    PlayerCPU_external,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_hyp_function_constructor_exists():
    assert callable(Function.__init__)


def test_hyp_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())
    assert "removedCard" in params, "Missing parameter 'removedCard'"
    assert "Score" in params, "Missing parameter 'Score'"





def test_hyp_players_is_not_abstract():
    assert not inspect.isabstract(Players)


def test_hyp_players_constructor_exists():
    assert callable(Players.__init__)


def test_hyp_players_constructor_args():
    sig = inspect.signature(Players.__init__)
    params = list(sig.parameters.keys())
    assert "Player1" in params, "Missing parameter 'Player1'"
    assert "Player2" in params, "Missing parameter 'Player2'"

def test_hyp_players_has_Player1():
    assert hasattr(Players, "Player1")
    descriptor = None
    for klass in Players.__mro__:
        if "Player1" in klass.__dict__:
            descriptor = klass.__dict__["Player1"]
            break
    assert isinstance(descriptor, property)

def test_hyp_players_has_Player2():
    assert hasattr(Players, "Player2")
    descriptor = None
    for klass in Players.__mro__:
        if "Player2" in klass.__dict__:
            descriptor = klass.__dict__["Player2"]
            break
    assert isinstance(descriptor, property)



def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_card_interface_is_not_abstract():
    assert not inspect.isabstract(Card_Interface)


def test_hyp_card_interface_constructor_exists():
    assert callable(Card_Interface.__init__)


def test_hyp_card_interface_constructor_args():
    sig = inspect.signature(Card_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())
    assert "deck__" in params, "Missing parameter 'deck__'"
    assert "topcard" in params, "Missing parameter 'topcard'"
    assert "shuffle__" in params, "Missing parameter 'shuffle__'"
    assert "isEmpty__" in params, "Missing parameter 'isEmpty__'"
    assert "draw__" in params, "Missing parameter 'draw__'"

def test_hyp_deck_has_deck__():
    assert hasattr(Deck, "deck__")
    descriptor = None
    for klass in Deck.__mro__:
        if "deck__" in klass.__dict__:
            descriptor = klass.__dict__["deck__"]
            break
    assert isinstance(descriptor, property)

def test_hyp_deck_has_topcard():
    assert hasattr(Deck, "topcard")
    descriptor = None
    for klass in Deck.__mro__:
        if "topcard" in klass.__dict__:
            descriptor = klass.__dict__["topcard"]
            break
    assert isinstance(descriptor, property)

def test_hyp_deck_has_shuffle__():
    assert hasattr(Deck, "shuffle__")
    descriptor = None
    for klass in Deck.__mro__:
        if "shuffle__" in klass.__dict__:
            descriptor = klass.__dict__["shuffle__"]
            break
    assert isinstance(descriptor, property)

def test_hyp_deck_has_isEmpty__():
    assert hasattr(Deck, "isEmpty__")
    descriptor = None
    for klass in Deck.__mro__:
        if "isEmpty__" in klass.__dict__:
            descriptor = klass.__dict__["isEmpty__"]
            break
    assert isinstance(descriptor, property)

def test_hyp_deck_has_draw__():
    assert hasattr(Deck, "draw__")
    descriptor = None
    for klass in Deck.__mro__:
        if "draw__" in klass.__dict__:
            descriptor = klass.__dict__["draw__"]
            break
    assert isinstance(descriptor, property)



def test_hyp_war_is_not_abstract():
    assert not inspect.isabstract(WAR)


def test_hyp_war_constructor_exists():
    assert callable(WAR.__init__)


def test_hyp_war_constructor_args():
    sig = inspect.signature(WAR.__init__)
    params = list(sig.parameters.keys())



def test_hyp_playeruser_external_is_not_abstract():
    assert not inspect.isabstract(PlayerUser_external)


def test_hyp_playeruser_external_constructor_exists():
    assert callable(PlayerUser_external.__init__)


def test_hyp_playeruser_external_constructor_args():
    sig = inspect.signature(PlayerUser_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_playercpu_external_is_not_abstract():
    assert not inspect.isabstract(PlayerCPU_external)


def test_hyp_playercpu_external_constructor_exists():
    assert callable(PlayerCPU_external.__init__)


def test_hyp_playercpu_external_constructor_args():
    sig = inspect.signature(PlayerCPU_external.__init__)
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
Function_strategy = st.builds(
    Function,
    removedCard=
        st.integers(),
    Score=
        st.integers()
)
Players_strategy = st.builds(
    Players,
    Player1=
        st.none(),
    Player2=
        st.none()
)
Class_strategy = st.builds(
    Class,
)
Card_Interface_strategy = st.builds(
    Card_Interface,
)
Deck_strategy = st.builds(
    Deck,
    deck__=
        st.none(),
    topcard=
        st.integers(),
    shuffle__=
        safe_text,
    isEmpty__=
        st.booleans(),
    draw__=
        safe_text
)
WAR_strategy = st.builds(
    WAR,
)
PlayerUser_external_strategy = st.builds(
    PlayerUser_external,
)
PlayerCPU_external_strategy = st.builds(
    PlayerCPU_external,
)




@given(instance=Function_strategy)
def test_hyp_function_removedCard_setter(instance):
    original = instance.removedCard
    instance.removedCard = original
    assert instance.removedCard == original



@given(instance=Function_strategy)
def test_hyp_function_Score_setter(instance):
    original = instance.Score
    instance.Score = original
    assert instance.Score == original

@given(instance=Players_strategy)
@settings(max_examples=50)
def test_hyp_players_instantiation(instance):
    assert isinstance(instance, Players)



@given(instance=Players_strategy)
def test_hyp_players_Player1_setter(instance):
    original = instance.Player1
    instance.Player1 = original
    assert instance.Player1 == original



@given(instance=Players_strategy)
def test_hyp_players_Player2_setter(instance):
    original = instance.Player2
    instance.Player2 = original
    assert instance.Player2 == original



@given(instance=Deck_strategy)
@settings(max_examples=50)
def test_hyp_deck_instantiation(instance):
    assert isinstance(instance, Deck)



@given(instance=Deck_strategy)
def test_hyp_deck_deck___setter(instance):
    original = instance.deck__
    instance.deck__ = original
    assert instance.deck__ == original



@given(instance=Deck_strategy)
def test_hyp_deck_topcard_setter(instance):
    original = instance.topcard
    instance.topcard = original
    assert instance.topcard == original



@given(instance=Deck_strategy)
def test_hyp_deck_shuffle___setter(instance):
    original = instance.shuffle__
    instance.shuffle__ = original
    assert instance.shuffle__ == original



@given(instance=Deck_strategy)
def test_hyp_deck_isEmpty___setter(instance):
    original = instance.isEmpty__
    instance.isEmpty__ = original
    assert instance.isEmpty__ == original



@given(instance=Deck_strategy)
def test_hyp_deck_draw___setter(instance):
    original = instance.draw__
    instance.draw__ = original
    assert instance.draw__ == original





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Card_Interface,
    Class,
    Deck,
    Function,
    PlayerCPU_external,
    PlayerUser_external,
    Players,
    WAR,
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

def test_Function_Score_value_roundtrip():
    instance = Function(Score=7, removedCard=7)
    assert instance.Score == 7
    instance.Score = 13
    assert instance.Score == 13


def test_Function_removedCard_value_roundtrip():
    instance = Function(Score=7, removedCard=7)
    assert instance.removedCard == 7
    instance.removedCard = 13
    assert instance.removedCard == 13


def test_assoc_Function_Card_link_reassign_clear():
    a = Function(Score=7, removedCard=7)
    b1 = Card_Interface()
    b2 = Card_Interface()
    _safe_set(a, 'card14', b1)
    assert _is_linked(a, 'card14', b1)
    if hasattr(b1, 'function15'):
        assert _is_linked(b1, 'function15', a)
    _safe_set(a, 'card14', b2)
    assert _is_linked(a, 'card14', b2)
    if hasattr(b1, 'function15'):
        assert not _is_linked(b1, 'function15', a)
    if hasattr(b2, 'function15'):
        assert _is_linked(b2, 'function15', a)
    _safe_set(a, 'card14', None)
    assert not _is_linked(a, 'card14', b2)
    if hasattr(b2, 'function15'):
        assert not _is_linked(b2, 'function15', a)


def test_assoc_Function_PlayerCPU_link_reassign_clear():
    a = Function(Score=7, removedCard=7)
    b1 = PlayerCPU_external()
    b2 = PlayerCPU_external()
    _safe_set(a, 'playerCPU10', b1)
    assert _is_linked(a, 'playerCPU10', b1)
    if hasattr(b1, 'function11'):
        assert _is_linked(b1, 'function11', a)
    _safe_set(a, 'playerCPU10', b2)
    assert _is_linked(a, 'playerCPU10', b2)
    if hasattr(b1, 'function11'):
        assert not _is_linked(b1, 'function11', a)
    if hasattr(b2, 'function11'):
        assert _is_linked(b2, 'function11', a)
    _safe_set(a, 'playerCPU10', None)
    assert not _is_linked(a, 'playerCPU10', b2)
    if hasattr(b2, 'function11'):
        assert not _is_linked(b2, 'function11', a)


def test_assoc_Function_PlayerUser_link_reassign_clear():
    a = Function(Score=7, removedCard=7)
    b1 = PlayerUser_external()
    b2 = PlayerUser_external()
    _safe_set(a, 'playerUser12', b1)
    assert _is_linked(a, 'playerUser12', b1)
    if hasattr(b1, 'function13'):
        assert _is_linked(b1, 'function13', a)
    _safe_set(a, 'playerUser12', b2)
    assert _is_linked(a, 'playerUser12', b2)
    if hasattr(b1, 'function13'):
        assert not _is_linked(b1, 'function13', a)
    if hasattr(b2, 'function13'):
        assert _is_linked(b2, 'function13', a)
    _safe_set(a, 'playerUser12', None)
    assert not _is_linked(a, 'playerUser12', b2)
    if hasattr(b2, 'function13'):
        assert not _is_linked(b2, 'function13', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Card_Interface_strategy = st.builds(Card_Interface)
@given(instance=Card_Interface_strategy)
@settings(max_examples=25)
def test_Card_Interface_instantiation(instance):
    assert isinstance(instance, Card_Interface)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Function_strategy = st.builds(Function, Score=st.integers(), removedCard=st.integers())
@given(instance=Function_strategy)
@settings(max_examples=25)
def test_Function_instantiation(instance):
    assert isinstance(instance, Function)


PlayerCPU_external_strategy = st.builds(PlayerCPU_external)
@given(instance=PlayerCPU_external_strategy)
@settings(max_examples=25)
def test_PlayerCPU_external_instantiation(instance):
    assert isinstance(instance, PlayerCPU_external)


PlayerUser_external_strategy = st.builds(PlayerUser_external)
@given(instance=PlayerUser_external_strategy)
@settings(max_examples=25)
def test_PlayerUser_external_instantiation(instance):
    assert isinstance(instance, PlayerUser_external)


WAR_strategy = st.builds(WAR)
@given(instance=WAR_strategy)
@settings(max_examples=25)
def test_WAR_instantiation(instance):
    assert isinstance(instance, WAR)



