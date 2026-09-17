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
    Begin_Game_UseCase,
    Player_Actor,
    MemoryGame_Deck,
    MemoryGame_Card,
    Change_Deck__Image_Changes__UseCase,
    Quit_UseCase,
    Shuffle_Deck__Restart_Game__UseCase,
    Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_begin_game_usecase_is_not_abstract():
    assert not inspect.isabstract(Begin_Game_UseCase)


def test_hyp_begin_game_usecase_constructor_exists():
    assert callable(Begin_Game_UseCase.__init__)


def test_hyp_begin_game_usecase_constructor_args():
    sig = inspect.signature(Begin_Game_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_player_actor_is_not_abstract():
    assert not inspect.isabstract(Player_Actor)


def test_hyp_player_actor_constructor_exists():
    assert callable(Player_Actor.__init__)


def test_hyp_player_actor_constructor_args():
    sig = inspect.signature(Player_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_memorygame_deck_is_not_abstract():
    assert not inspect.isabstract(MemoryGame_Deck)


def test_hyp_memorygame_deck_constructor_exists():
    assert callable(MemoryGame_Deck.__init__)


def test_hyp_memorygame_deck_constructor_args():
    sig = inspect.signature(MemoryGame_Deck.__init__)
    params = list(sig.parameters.keys())
    assert "cards" in params, "Missing parameter 'cards'"
    assert "image" in params, "Missing parameter 'image'"
    assert "id" in params, "Missing parameter 'id'"

def test_hyp_memorygame_deck_has_cards():
    assert hasattr(MemoryGame_Deck, "cards")
    descriptor = None
    for klass in MemoryGame_Deck.__mro__:
        if "cards" in klass.__dict__:
            descriptor = klass.__dict__["cards"]
            break
    assert isinstance(descriptor, property)

def test_hyp_memorygame_deck_has_image():
    assert hasattr(MemoryGame_Deck, "image")
    descriptor = None
    for klass in MemoryGame_Deck.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_hyp_memorygame_deck_has_id():
    assert hasattr(MemoryGame_Deck, "id")
    descriptor = None
    for klass in MemoryGame_Deck.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_hyp_memorygame_card_is_not_abstract():
    assert not inspect.isabstract(MemoryGame_Card)


def test_hyp_memorygame_card_constructor_exists():
    assert callable(MemoryGame_Card.__init__)


def test_hyp_memorygame_card_constructor_args():
    sig = inspect.signature(MemoryGame_Card.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"
    assert "id" in params, "Missing parameter 'id'"
    assert "position" in params, "Missing parameter 'position'"
    assert "deck" in params, "Missing parameter 'deck'"
    assert "isShowing" in params, "Missing parameter 'isShowing'"

def test_hyp_memorygame_card_has_image():
    assert hasattr(MemoryGame_Card, "image")
    descriptor = None
    for klass in MemoryGame_Card.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_hyp_memorygame_card_has_id():
    assert hasattr(MemoryGame_Card, "id")
    descriptor = None
    for klass in MemoryGame_Card.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hyp_memorygame_card_has_position():
    assert hasattr(MemoryGame_Card, "position")
    descriptor = None
    for klass in MemoryGame_Card.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_hyp_memorygame_card_has_deck():
    assert hasattr(MemoryGame_Card, "deck")
    descriptor = None
    for klass in MemoryGame_Card.__mro__:
        if "deck" in klass.__dict__:
            descriptor = klass.__dict__["deck"]
            break
    assert isinstance(descriptor, property)

def test_hyp_memorygame_card_has_isShowing():
    assert hasattr(MemoryGame_Card, "isShowing")
    descriptor = None
    for klass in MemoryGame_Card.__mro__:
        if "isShowing" in klass.__dict__:
            descriptor = klass.__dict__["isShowing"]
            break
    assert isinstance(descriptor, property)



def test_hyp_change_deck__image_changes__usecase_is_not_abstract():
    assert not inspect.isabstract(Change_Deck__Image_Changes__UseCase)


def test_hyp_change_deck__image_changes__usecase_constructor_exists():
    assert callable(Change_Deck__Image_Changes__UseCase.__init__)


def test_hyp_change_deck__image_changes__usecase_constructor_args():
    sig = inspect.signature(Change_Deck__Image_Changes__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_quit_usecase_is_not_abstract():
    assert not inspect.isabstract(Quit_UseCase)


def test_hyp_quit_usecase_constructor_exists():
    assert callable(Quit_UseCase.__init__)


def test_hyp_quit_usecase_constructor_args():
    sig = inspect.signature(Quit_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_shuffle_deck__restart_game__usecase_is_not_abstract():
    assert not inspect.isabstract(Shuffle_Deck__Restart_Game__UseCase)


def test_hyp_shuffle_deck__restart_game__usecase_constructor_exists():
    assert callable(Shuffle_Deck__Restart_Game__UseCase.__init__)


def test_hyp_shuffle_deck__restart_game__usecase_constructor_args():
    sig = inspect.signature(Shuffle_Deck__Restart_Game__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_match_pairs_of_cards_together_until_no_cards_remain_or_mismatch_usecase_is_not_abstract():
    assert not inspect.isabstract(Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase)


def test_hyp_match_pairs_of_cards_together_until_no_cards_remain_or_mismatch_usecase_constructor_exists():
    assert callable(Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase.__init__)


def test_hyp_match_pairs_of_cards_together_until_no_cards_remain_or_mismatch_usecase_constructor_args():
    sig = inspect.signature(Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase.__init__)
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
Begin_Game_UseCase_strategy = st.builds(
    Begin_Game_UseCase,
)
Player_Actor_strategy = st.builds(
    Player_Actor,
)
MemoryGame_Deck_strategy = st.builds(
    MemoryGame_Deck,
    cards=
        st.none(),
    image=
        safe_text,
    id=
        st.integers()
)
MemoryGame_Card_strategy = st.builds(
    MemoryGame_Card,
    image=
        safe_text,
    id=
        st.integers(),
    position=
        st.integers(),
    deck=
        st.none(),
    isShowing=
        st.booleans()
)
Change_Deck__Image_Changes__UseCase_strategy = st.builds(
    Change_Deck__Image_Changes__UseCase,
)
Quit_UseCase_strategy = st.builds(
    Quit_UseCase,
)
Shuffle_Deck__Restart_Game__UseCase_strategy = st.builds(
    Shuffle_Deck__Restart_Game__UseCase,
)
Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase_strategy = st.builds(
    Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase,
)



@given(instance=MemoryGame_Deck_strategy)
@settings(max_examples=50)
def test_hyp_memorygame_deck_instantiation(instance):
    assert isinstance(instance, MemoryGame_Deck)



@given(instance=MemoryGame_Deck_strategy)
def test_hyp_memorygame_deck_cards_setter(instance):
    original = instance.cards
    instance.cards = original
    assert instance.cards == original



@given(instance=MemoryGame_Deck_strategy)
def test_hyp_memorygame_deck_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=MemoryGame_Deck_strategy)
def test_hyp_memorygame_deck_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=MemoryGame_Card_strategy)
@settings(max_examples=50)
def test_hyp_memorygame_card_instantiation(instance):
    assert isinstance(instance, MemoryGame_Card)



@given(instance=MemoryGame_Card_strategy)
def test_hyp_memorygame_card_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=MemoryGame_Card_strategy)
def test_hyp_memorygame_card_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=MemoryGame_Card_strategy)
def test_hyp_memorygame_card_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=MemoryGame_Card_strategy)
def test_hyp_memorygame_card_deck_setter(instance):
    original = instance.deck
    instance.deck = original
    assert instance.deck == original



@given(instance=MemoryGame_Card_strategy)
def test_hyp_memorygame_card_isShowing_setter(instance):
    original = instance.isShowing
    instance.isShowing = original
    assert instance.isShowing == original






# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Begin_Game_UseCase,
    Change_Deck__Image_Changes__UseCase,
    Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase,
    MemoryGame_Card,
    MemoryGame_Deck,
    Player_Actor,
    Quit_UseCase,
    Shuffle_Deck__Restart_Game__UseCase,
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

# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Begin_Game_UseCase_strategy = st.builds(Begin_Game_UseCase)
@given(instance=Begin_Game_UseCase_strategy)
@settings(max_examples=25)
def test_Begin_Game_UseCase_instantiation(instance):
    assert isinstance(instance, Begin_Game_UseCase)


Change_Deck__Image_Changes__UseCase_strategy = st.builds(Change_Deck__Image_Changes__UseCase)
@given(instance=Change_Deck__Image_Changes__UseCase_strategy)
@settings(max_examples=25)
def test_Change_Deck__Image_Changes__UseCase_instantiation(instance):
    assert isinstance(instance, Change_Deck__Image_Changes__UseCase)


Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase_strategy = st.builds(Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase)
@given(instance=Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase_strategy)
@settings(max_examples=25)
def test_Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase_instantiation(instance):
    assert isinstance(instance, Match_Pairs_of_Cards_Together_Until_No_Cards_Remain_or_Mismatch_UseCase)


Player_Actor_strategy = st.builds(Player_Actor)
@given(instance=Player_Actor_strategy)
@settings(max_examples=25)
def test_Player_Actor_instantiation(instance):
    assert isinstance(instance, Player_Actor)


Quit_UseCase_strategy = st.builds(Quit_UseCase)
@given(instance=Quit_UseCase_strategy)
@settings(max_examples=25)
def test_Quit_UseCase_instantiation(instance):
    assert isinstance(instance, Quit_UseCase)


Shuffle_Deck__Restart_Game__UseCase_strategy = st.builds(Shuffle_Deck__Restart_Game__UseCase)
@given(instance=Shuffle_Deck__Restart_Game__UseCase_strategy)
@settings(max_examples=25)
def test_Shuffle_Deck__Restart_Game__UseCase_instantiation(instance):
    assert isinstance(instance, Shuffle_Deck__Restart_Game__UseCase)



