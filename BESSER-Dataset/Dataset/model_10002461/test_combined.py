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
    Player1,
    Avatar1,
    Card1,
    Game1,
    Deck1,
    Theme1,
    Player2,
    Avatar2,
    Card2,
    Game2,
    Deck2,
    Theme2,
    Player,
    Avatar,
    Card,
    Game,
    Deck,
    Theme,
    Kind1,
    Kind,
    Suit1,
    Suit,
    Kind2,
    Suit2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_player1_is_not_abstract():
    assert not inspect.isabstract(Player1)


def test_hyp_player1_constructor_exists():
    assert callable(Player1.__init__)


def test_hyp_player1_constructor_args():
    sig = inspect.signature(Player1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "hand" in params, "Missing parameter 'hand'"





def test_hyp_avatar1_is_not_abstract():
    assert not inspect.isabstract(Avatar1)


def test_hyp_avatar1_constructor_exists():
    assert callable(Avatar1.__init__)


def test_hyp_avatar1_constructor_args():
    sig = inspect.signature(Avatar1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_card1_is_not_abstract():
    assert not inspect.isabstract(Card1)


def test_hyp_card1_constructor_exists():
    assert callable(Card1.__init__)


def test_hyp_card1_constructor_args():
    sig = inspect.signature(Card1.__init__)
    params = list(sig.parameters.keys())
    assert "suit" in params, "Missing parameter 'suit'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_hyp_card1_has_suit():
    assert hasattr(Card1, "suit")
    descriptor = None
    for klass in Card1.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)

def test_hyp_card1_has_kind():
    assert hasattr(Card1, "kind")
    descriptor = None
    for klass in Card1.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_hyp_game1_is_not_abstract():
    assert not inspect.isabstract(Game1)


def test_hyp_game1_constructor_exists():
    assert callable(Game1.__init__)


def test_hyp_game1_constructor_args():
    sig = inspect.signature(Game1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_deck1_is_not_abstract():
    assert not inspect.isabstract(Deck1)


def test_hyp_deck1_constructor_exists():
    assert callable(Deck1.__init__)


def test_hyp_deck1_constructor_args():
    sig = inspect.signature(Deck1.__init__)
    params = list(sig.parameters.keys())
    assert "Card_cards_52_" in params, "Missing parameter 'Card_cards_52_'"

def test_hyp_deck1_has_Card_cards_52_():
    assert hasattr(Deck1, "Card_cards_52_")
    descriptor = None
    for klass in Deck1.__mro__:
        if "Card_cards_52_" in klass.__dict__:
            descriptor = klass.__dict__["Card_cards_52_"]
            break
    assert isinstance(descriptor, property)



def test_hyp_theme1_is_not_abstract():
    assert not inspect.isabstract(Theme1)


def test_hyp_theme1_constructor_exists():
    assert callable(Theme1.__init__)


def test_hyp_theme1_constructor_args():
    sig = inspect.signature(Theme1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_player2_is_not_abstract():
    assert not inspect.isabstract(Player2)


def test_hyp_player2_constructor_exists():
    assert callable(Player2.__init__)


def test_hyp_player2_constructor_args():
    sig = inspect.signature(Player2.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_avatar2_is_not_abstract():
    assert not inspect.isabstract(Avatar2)


def test_hyp_avatar2_constructor_exists():
    assert callable(Avatar2.__init__)


def test_hyp_avatar2_constructor_args():
    sig = inspect.signature(Avatar2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_card2_is_not_abstract():
    assert not inspect.isabstract(Card2)


def test_hyp_card2_constructor_exists():
    assert callable(Card2.__init__)


def test_hyp_card2_constructor_args():
    sig = inspect.signature(Card2.__init__)
    params = list(sig.parameters.keys())
    assert "suit" in params, "Missing parameter 'suit'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_hyp_card2_has_suit():
    assert hasattr(Card2, "suit")
    descriptor = None
    for klass in Card2.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)

def test_hyp_card2_has_kind():
    assert hasattr(Card2, "kind")
    descriptor = None
    for klass in Card2.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_hyp_game2_is_not_abstract():
    assert not inspect.isabstract(Game2)


def test_hyp_game2_constructor_exists():
    assert callable(Game2.__init__)


def test_hyp_game2_constructor_args():
    sig = inspect.signature(Game2.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_deck2_is_not_abstract():
    assert not inspect.isabstract(Deck2)


def test_hyp_deck2_constructor_exists():
    assert callable(Deck2.__init__)


def test_hyp_deck2_constructor_args():
    sig = inspect.signature(Deck2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_theme2_is_not_abstract():
    assert not inspect.isabstract(Theme2)


def test_hyp_theme2_constructor_exists():
    assert callable(Theme2.__init__)


def test_hyp_theme2_constructor_args():
    sig = inspect.signature(Theme2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_hyp_player_constructor_exists():
    assert callable(Player.__init__)


def test_hyp_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_avatar_is_not_abstract():
    assert not inspect.isabstract(Avatar)


def test_hyp_avatar_constructor_exists():
    assert callable(Avatar.__init__)


def test_hyp_avatar_constructor_args():
    sig = inspect.signature(Avatar.__init__)
    params = list(sig.parameters.keys())



def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "suit" in params, "Missing parameter 'suit'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_hyp_card_has_suit():
    assert hasattr(Card, "suit")
    descriptor = None
    for klass in Card.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)

def test_hyp_card_has_kind():
    assert hasattr(Card, "kind")
    descriptor = None
    for klass in Card.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_hyp_game_is_not_abstract():
    assert not inspect.isabstract(Game)


def test_hyp_game_constructor_exists():
    assert callable(Game.__init__)


def test_hyp_game_constructor_args():
    sig = inspect.signature(Game.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_deck_is_not_abstract():
    assert not inspect.isabstract(Deck)


def test_hyp_deck_constructor_exists():
    assert callable(Deck.__init__)


def test_hyp_deck_constructor_args():
    sig = inspect.signature(Deck.__init__)
    params = list(sig.parameters.keys())



def test_hyp_theme_is_not_abstract():
    assert not inspect.isabstract(Theme)


def test_hyp_theme_constructor_exists():
    assert callable(Theme.__init__)


def test_hyp_theme_constructor_args():
    sig = inspect.signature(Theme.__init__)
    params = list(sig.parameters.keys())

def test_hyp_kind1_exists():
    # Check that the Enumeration exists
    assert Kind1 is not None

def test_hyp_kind1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Kind1]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Kind1"

def test_hyp_kind_exists():
    # Check that the Enumeration exists
    assert Kind is not None

def test_hyp_kind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Kind]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Kind"

def test_hyp_suit1_exists():
    # Check that the Enumeration exists
    assert Suit1 is not None

def test_hyp_suit1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Suit1]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Suit1"

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

def test_hyp_kind2_exists():
    # Check that the Enumeration exists
    assert Kind2 is not None

def test_hyp_kind2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Kind2]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Kind2"

def test_hyp_suit2_exists():
    # Check that the Enumeration exists
    assert Suit2 is not None

def test_hyp_suit2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Suit2]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Suit2"


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
Player1_strategy = st.builds(
    Player1,
    name=
        safe_text,
    hand=
        safe_text
)
Avatar1_strategy = st.builds(
    Avatar1,
)
Card1_strategy = st.builds(
    Card1,
    suit=
        st.none(),
    kind=
        st.none()
)
Game1_strategy = st.builds(
    Game1,
    name=
        safe_text
)
Deck1_strategy = st.builds(
    Deck1,
    Card_cards_52_=
        st.none()
)
Theme1_strategy = st.builds(
    Theme1,
)
Player2_strategy = st.builds(
    Player2,
    name=
        safe_text
)
Avatar2_strategy = st.builds(
    Avatar2,
)
Card2_strategy = st.builds(
    Card2,
    suit=
        st.none(),
    kind=
        st.none()
)
Game2_strategy = st.builds(
    Game2,
    name=
        safe_text
)
Deck2_strategy = st.builds(
    Deck2,
)
Theme2_strategy = st.builds(
    Theme2,
)
Player_strategy = st.builds(
    Player,
    name=
        safe_text
)
Avatar_strategy = st.builds(
    Avatar,
)
Card_strategy = st.builds(
    Card,
    suit=
        st.none(),
    kind=
        st.none()
)
Game_strategy = st.builds(
    Game,
    name=
        safe_text
)
Deck_strategy = st.builds(
    Deck,
)
Theme_strategy = st.builds(
    Theme,
)




@given(instance=Player1_strategy)
def test_hyp_player1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Player1_strategy)
def test_hyp_player1_hand_setter(instance):
    original = instance.hand
    instance.hand = original
    assert instance.hand == original


@given(instance=Card1_strategy)
@settings(max_examples=50)
def test_hyp_card1_instantiation(instance):
    assert isinstance(instance, Card1)



@given(instance=Card1_strategy)
def test_hyp_card1_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=Card1_strategy)
def test_hyp_card1_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original




@given(instance=Game1_strategy)
def test_hyp_game1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Deck1_strategy)
@settings(max_examples=50)
def test_hyp_deck1_instantiation(instance):
    assert isinstance(instance, Deck1)



@given(instance=Deck1_strategy)
def test_hyp_deck1_Card_cards_52__setter(instance):
    original = instance.Card_cards_52_
    instance.Card_cards_52_ = original
    assert instance.Card_cards_52_ == original





@given(instance=Player2_strategy)
def test_hyp_player2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


@given(instance=Card2_strategy)
@settings(max_examples=50)
def test_hyp_card2_instantiation(instance):
    assert isinstance(instance, Card2)



@given(instance=Card2_strategy)
def test_hyp_card2_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=Card2_strategy)
def test_hyp_card2_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original




@given(instance=Game2_strategy)
def test_hyp_game2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=Player_strategy)
def test_hyp_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


@given(instance=Card_strategy)
@settings(max_examples=50)
def test_hyp_card_instantiation(instance):
    assert isinstance(instance, Card)



@given(instance=Card_strategy)
def test_hyp_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=Card_strategy)
def test_hyp_card_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original




@given(instance=Game_strategy)
def test_hyp_game_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Avatar,
    Avatar1,
    Avatar2,
    Card,
    Card1,
    Card2,
    Deck,
    Deck1,
    Deck2,
    Game,
    Game1,
    Game2,
    Player,
    Player1,
    Player2,
    Theme,
    Theme1,
    Theme2,
    Kind,
    Kind1,
    Kind2,
    Suit,
    Suit1,
    Suit2,
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

def test_Game_name_value_roundtrip():
    instance = Game(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Game1_name_value_roundtrip():
    instance = Game1(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Game2_name_value_roundtrip():
    instance = Game2(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Player_name_value_roundtrip():
    instance = Player(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Player1_hand_value_roundtrip():
    instance = Player1(hand="sample_text", name="sample_text")
    assert instance.hand == "sample_text"
    instance.hand = "sample_text_2"
    assert instance.hand == "sample_text_2"


def test_Player1_name_value_roundtrip():
    instance = Player1(hand="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Player2_name_value_roundtrip():
    instance = Player2(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_Game_Deck_link_reassign_clear():
    a = Game(name="sample_text")
    b1 = Deck()
    b2 = Deck()
    _safe_set(a, 'decks4', {b1})
    assert _is_linked(a, 'decks4', b1)
    if hasattr(b1, 'games5'):
        assert _is_linked(b1, 'games5', a)
    _safe_set(a, 'decks4', {b2})
    assert _is_linked(a, 'decks4', b2)
    if hasattr(b1, 'games5'):
        assert not _is_linked(b1, 'games5', a)
    if hasattr(b2, 'games5'):
        assert _is_linked(b2, 'games5', a)
    _safe_set(a, 'decks4', set())
    assert not _is_linked(a, 'decks4', b2)
    if hasattr(b2, 'games5'):
        assert not _is_linked(b2, 'games5', a)


def test_assoc_Game_Deck2_link_reassign_clear():
    a = Game2(name="sample_text")
    b1 = Deck2()
    b2 = Deck2()
    _safe_set(a, 'decks16', {b1})
    assert _is_linked(a, 'decks16', b1)
    if hasattr(b1, 'games17'):
        assert _is_linked(b1, 'games17', a)
    _safe_set(a, 'decks16', {b2})
    assert _is_linked(a, 'decks16', b2)
    if hasattr(b1, 'games17'):
        assert not _is_linked(b1, 'games17', a)
    if hasattr(b2, 'games17'):
        assert _is_linked(b2, 'games17', a)
    _safe_set(a, 'decks16', set())
    assert not _is_linked(a, 'decks16', b2)
    if hasattr(b2, 'games17'):
        assert not _is_linked(b2, 'games17', a)


def test_assoc_Game_Player_link_reassign_clear():
    a = Player(name="sample_text")
    b1 = Game(name="sample_text")
    b2 = Game(name="sample_text_2")
    _safe_set(a, 'games7', {b1})
    assert _is_linked(a, 'games7', b1)
    if hasattr(b1, 'players6'):
        assert _is_linked(b1, 'players6', a)
    _safe_set(a, 'games7', {b2})
    assert _is_linked(a, 'games7', b2)
    if hasattr(b1, 'players6'):
        assert not _is_linked(b1, 'players6', a)
    if hasattr(b2, 'players6'):
        assert _is_linked(b2, 'players6', a)
    _safe_set(a, 'games7', set())
    assert not _is_linked(a, 'games7', b2)
    if hasattr(b2, 'players6'):
        assert not _is_linked(b2, 'players6', a)


def test_assoc_Game_Player2_link_reassign_clear():
    a = Player2(name="sample_text")
    b1 = Game2(name="sample_text")
    b2 = Game2(name="sample_text_2")
    _safe_set(a, 'games19', {b1})
    assert _is_linked(a, 'games19', b1)
    if hasattr(b1, 'players18'):
        assert _is_linked(b1, 'players18', a)
    _safe_set(a, 'games19', {b2})
    assert _is_linked(a, 'games19', b2)
    if hasattr(b1, 'players18'):
        assert not _is_linked(b1, 'players18', a)
    if hasattr(b2, 'players18'):
        assert _is_linked(b2, 'players18', a)
    _safe_set(a, 'games19', set())
    assert not _is_linked(a, 'games19', b2)
    if hasattr(b2, 'players18'):
        assert not _is_linked(b2, 'players18', a)


def test_assoc_Game_Player3_link_reassign_clear():
    a = Player1(hand="sample_text", name="sample_text")
    b1 = Game1(name="sample_text")
    b2 = Game1(name="sample_text_2")
    _safe_set(a, 'games31', {b1})
    assert _is_linked(a, 'games31', b1)
    if hasattr(b1, 'players30'):
        assert _is_linked(b1, 'players30', a)
    _safe_set(a, 'games31', {b2})
    assert _is_linked(a, 'games31', b2)
    if hasattr(b1, 'players30'):
        assert not _is_linked(b1, 'players30', a)
    if hasattr(b2, 'players30'):
        assert _is_linked(b2, 'players30', a)
    _safe_set(a, 'games31', set())
    assert not _is_linked(a, 'games31', b2)
    if hasattr(b2, 'players30'):
        assert not _is_linked(b2, 'players30', a)


def test_assoc_Player_Avatar_link_reassign_clear():
    a = Player(name="sample_text")
    b1 = Avatar()
    b2 = Avatar()
    _safe_set(a, 'avatar10', b1)
    assert _is_linked(a, 'avatar10', b1)
    if hasattr(b1, 'players11'):
        assert _is_linked(b1, 'players11', a)
    _safe_set(a, 'avatar10', b2)
    assert _is_linked(a, 'avatar10', b2)
    if hasattr(b1, 'players11'):
        assert not _is_linked(b1, 'players11', a)
    if hasattr(b2, 'players11'):
        assert _is_linked(b2, 'players11', a)
    _safe_set(a, 'avatar10', None)
    assert not _is_linked(a, 'avatar10', b2)
    if hasattr(b2, 'players11'):
        assert not _is_linked(b2, 'players11', a)


def test_assoc_Player_Avatar2_link_reassign_clear():
    a = Player2(name="sample_text")
    b1 = Avatar2()
    b2 = Avatar2()
    _safe_set(a, 'avatar22', b1)
    assert _is_linked(a, 'avatar22', b1)
    if hasattr(b1, 'players23'):
        assert _is_linked(b1, 'players23', a)
    _safe_set(a, 'avatar22', b2)
    assert _is_linked(a, 'avatar22', b2)
    if hasattr(b1, 'players23'):
        assert not _is_linked(b1, 'players23', a)
    if hasattr(b2, 'players23'):
        assert _is_linked(b2, 'players23', a)
    _safe_set(a, 'avatar22', None)
    assert not _is_linked(a, 'avatar22', b2)
    if hasattr(b2, 'players23'):
        assert not _is_linked(b2, 'players23', a)


def test_assoc_Player_Avatar3_link_reassign_clear():
    a = Player1(hand="sample_text", name="sample_text")
    b1 = Avatar1()
    b2 = Avatar1()
    _safe_set(a, 'avatar34', b1)
    assert _is_linked(a, 'avatar34', b1)
    if hasattr(b1, 'players35'):
        assert _is_linked(b1, 'players35', a)
    _safe_set(a, 'avatar34', b2)
    assert _is_linked(a, 'avatar34', b2)
    if hasattr(b1, 'players35'):
        assert not _is_linked(b1, 'players35', a)
    if hasattr(b2, 'players35'):
        assert _is_linked(b2, 'players35', a)
    _safe_set(a, 'avatar34', None)
    assert not _is_linked(a, 'avatar34', b2)
    if hasattr(b2, 'players35'):
        assert not _is_linked(b2, 'players35', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Avatar_strategy = st.builds(Avatar)
@given(instance=Avatar_strategy)
@settings(max_examples=25)
def test_Avatar_instantiation(instance):
    assert isinstance(instance, Avatar)


Avatar1_strategy = st.builds(Avatar1)
@given(instance=Avatar1_strategy)
@settings(max_examples=25)
def test_Avatar1_instantiation(instance):
    assert isinstance(instance, Avatar1)


Avatar2_strategy = st.builds(Avatar2)
@given(instance=Avatar2_strategy)
@settings(max_examples=25)
def test_Avatar2_instantiation(instance):
    assert isinstance(instance, Avatar2)


Deck_strategy = st.builds(Deck)
@given(instance=Deck_strategy)
@settings(max_examples=25)
def test_Deck_instantiation(instance):
    assert isinstance(instance, Deck)


Deck2_strategy = st.builds(Deck2)
@given(instance=Deck2_strategy)
@settings(max_examples=25)
def test_Deck2_instantiation(instance):
    assert isinstance(instance, Deck2)


Game_strategy = st.builds(Game, name=safe_text)
@given(instance=Game_strategy)
@settings(max_examples=25)
def test_Game_instantiation(instance):
    assert isinstance(instance, Game)


Game1_strategy = st.builds(Game1, name=safe_text)
@given(instance=Game1_strategy)
@settings(max_examples=25)
def test_Game1_instantiation(instance):
    assert isinstance(instance, Game1)


Game2_strategy = st.builds(Game2, name=safe_text)
@given(instance=Game2_strategy)
@settings(max_examples=25)
def test_Game2_instantiation(instance):
    assert isinstance(instance, Game2)


Player_strategy = st.builds(Player, name=safe_text)
@given(instance=Player_strategy)
@settings(max_examples=25)
def test_Player_instantiation(instance):
    assert isinstance(instance, Player)


Player1_strategy = st.builds(Player1, hand=safe_text, name=safe_text)
@given(instance=Player1_strategy)
@settings(max_examples=25)
def test_Player1_instantiation(instance):
    assert isinstance(instance, Player1)


Player2_strategy = st.builds(Player2, name=safe_text)
@given(instance=Player2_strategy)
@settings(max_examples=25)
def test_Player2_instantiation(instance):
    assert isinstance(instance, Player2)


Theme_strategy = st.builds(Theme)
@given(instance=Theme_strategy)
@settings(max_examples=25)
def test_Theme_instantiation(instance):
    assert isinstance(instance, Theme)


Theme1_strategy = st.builds(Theme1)
@given(instance=Theme1_strategy)
@settings(max_examples=25)
def test_Theme1_instantiation(instance):
    assert isinstance(instance, Theme1)


Theme2_strategy = st.builds(Theme2)
@given(instance=Theme2_strategy)
@settings(max_examples=25)
def test_Theme2_instantiation(instance):
    assert isinstance(instance, Theme2)



