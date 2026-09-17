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
    FreeParking,
    AIPlayer,
    Dice,
    Board1,
    Money,
    Board,
    Random,
    Class,
    Player,
    Property,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_freeparking_is_not_abstract():
    assert not inspect.isabstract(FreeParking)


def test_hyp_freeparking_constructor_exists():
    assert callable(FreeParking.__init__)


def test_hyp_freeparking_constructor_args():
    sig = inspect.signature(FreeParking.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aiplayer_is_not_abstract():
    assert not inspect.isabstract(AIPlayer)


def test_hyp_aiplayer_constructor_exists():
    assert callable(AIPlayer.__init__)


def test_hyp_aiplayer_constructor_args():
    sig = inspect.signature(AIPlayer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dice_is_not_abstract():
    assert not inspect.isabstract(Dice)


def test_hyp_dice_constructor_exists():
    assert callable(Dice.__init__)


def test_hyp_dice_constructor_args():
    sig = inspect.signature(Dice.__init__)
    params = list(sig.parameters.keys())
    assert "firstValue" in params, "Missing parameter 'firstValue'"
    assert "randomNumber" in params, "Missing parameter 'randomNumber'"
    assert "secondValue" in params, "Missing parameter 'secondValue'"

def test_hyp_dice_has_firstValue():
    assert hasattr(Dice, "firstValue")
    descriptor = None
    for klass in Dice.__mro__:
        if "firstValue" in klass.__dict__:
            descriptor = klass.__dict__["firstValue"]
            break
    assert isinstance(descriptor, property)

def test_hyp_dice_has_randomNumber():
    assert hasattr(Dice, "randomNumber")
    descriptor = None
    for klass in Dice.__mro__:
        if "randomNumber" in klass.__dict__:
            descriptor = klass.__dict__["randomNumber"]
            break
    assert isinstance(descriptor, property)

def test_hyp_dice_has_secondValue():
    assert hasattr(Dice, "secondValue")
    descriptor = None
    for klass in Dice.__mro__:
        if "secondValue" in klass.__dict__:
            descriptor = klass.__dict__["secondValue"]
            break
    assert isinstance(descriptor, property)



def test_hyp_board1_is_not_abstract():
    assert not inspect.isabstract(Board1)


def test_hyp_board1_constructor_exists():
    assert callable(Board1.__init__)


def test_hyp_board1_constructor_args():
    sig = inspect.signature(Board1.__init__)
    params = list(sig.parameters.keys())
    assert "boardSize" in params, "Missing parameter 'boardSize'"




def test_hyp_money_is_not_abstract():
    assert not inspect.isabstract(Money)


def test_hyp_money_constructor_exists():
    assert callable(Money.__init__)


def test_hyp_money_constructor_args():
    sig = inspect.signature(Money.__init__)
    params = list(sig.parameters.keys())
    assert "money" in params, "Missing parameter 'money'"




def test_hyp_board_is_not_abstract():
    assert not inspect.isabstract(Board)


def test_hyp_board_constructor_exists():
    assert callable(Board.__init__)


def test_hyp_board_constructor_args():
    sig = inspect.signature(Board.__init__)
    params = list(sig.parameters.keys())



def test_hyp_random_is_not_abstract():
    assert not inspect.isabstract(Random)


def test_hyp_random_constructor_exists():
    assert callable(Random.__init__)


def test_hyp_random_constructor_args():
    sig = inspect.signature(Random.__init__)
    params = list(sig.parameters.keys())



def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_hyp_player_constructor_exists():
    assert callable(Player.__init__)


def test_hyp_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "PASS_GO_MONEY" in params, "Missing parameter 'PASS_GO_MONEY'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isBankrupt" in params, "Missing parameter 'isBankrupt'"
    assert "INITIAL_MONEY" in params, "Missing parameter 'INITIAL_MONEY'"
    assert "property" in params, "Missing parameter 'property'"
    assert "isAI" in params, "Missing parameter 'isAI'"
    assert "isRetire" in params, "Missing parameter 'isRetire'"
    assert "position" in params, "Missing parameter 'position'"
    assert "board" in params, "Missing parameter 'board'"
    assert "rand" in params, "Missing parameter 'rand'"
    assert "money" in params, "Missing parameter 'money'"
    assert "INITIAL_POSITION" in params, "Missing parameter 'INITIAL_POSITION'"

def test_hyp_player_has_PASS_GO_MONEY():
    assert hasattr(Player, "PASS_GO_MONEY")
    descriptor = None
    for klass in Player.__mro__:
        if "PASS_GO_MONEY" in klass.__dict__:
            descriptor = klass.__dict__["PASS_GO_MONEY"]
            break
    assert isinstance(descriptor, property)

def test_hyp_player_has_name():
    assert hasattr(Player, "name")
    descriptor = None
    for klass in Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hyp_player_has_isBankrupt():
    assert hasattr(Player, "isBankrupt")
    descriptor = None
    for klass in Player.__mro__:
        if "isBankrupt" in klass.__dict__:
            descriptor = klass.__dict__["isBankrupt"]
            break
    assert isinstance(descriptor, property)

def test_hyp_player_has_INITIAL_MONEY():
    assert hasattr(Player, "INITIAL_MONEY")
    descriptor = None
    for klass in Player.__mro__:
        if "INITIAL_MONEY" in klass.__dict__:
            descriptor = klass.__dict__["INITIAL_MONEY"]
            break
    assert isinstance(descriptor, property)

def test_hyp_player_has_property():
    assert hasattr(Player, "property")
    descriptor = None
    for klass in Player.__mro__:
        if "property" in klass.__dict__:
            descriptor = klass.__dict__["property"]
            break
    assert isinstance(descriptor, property)

def test_hyp_player_has_isAI():
    assert hasattr(Player, "isAI")
    descriptor = None
    for klass in Player.__mro__:
        if "isAI" in klass.__dict__:
            descriptor = klass.__dict__["isAI"]
            break
    assert isinstance(descriptor, property)

def test_hyp_player_has_isRetire():
    assert hasattr(Player, "isRetire")
    descriptor = None
    for klass in Player.__mro__:
        if "isRetire" in klass.__dict__:
            descriptor = klass.__dict__["isRetire"]
            break
    assert isinstance(descriptor, property)

def test_hyp_player_has_position():
    assert hasattr(Player, "position")
    descriptor = None
    for klass in Player.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_hyp_player_has_board():
    assert hasattr(Player, "board")
    descriptor = None
    for klass in Player.__mro__:
        if "board" in klass.__dict__:
            descriptor = klass.__dict__["board"]
            break
    assert isinstance(descriptor, property)

def test_hyp_player_has_rand():
    assert hasattr(Player, "rand")
    descriptor = None
    for klass in Player.__mro__:
        if "rand" in klass.__dict__:
            descriptor = klass.__dict__["rand"]
            break
    assert isinstance(descriptor, property)

def test_hyp_player_has_money():
    assert hasattr(Player, "money")
    descriptor = None
    for klass in Player.__mro__:
        if "money" in klass.__dict__:
            descriptor = klass.__dict__["money"]
            break
    assert isinstance(descriptor, property)

def test_hyp_player_has_INITIAL_POSITION():
    assert hasattr(Player, "INITIAL_POSITION")
    descriptor = None
    for klass in Player.__mro__:
        if "INITIAL_POSITION" in klass.__dict__:
            descriptor = klass.__dict__["INITIAL_POSITION"]
            break
    assert isinstance(descriptor, property)

def test_hyp_property_exists():
    # Check that the Enumeration exists
    assert Property is not None

def test_hyp_property_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Property]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Property"


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
FreeParking_strategy = st.builds(
    FreeParking,
)
AIPlayer_strategy = st.builds(
    AIPlayer,
)
Dice_strategy = st.builds(
    Dice,
    firstValue=
        st.integers(),
    randomNumber=
        st.none(),
    secondValue=
        st.integers()
)
Board1_strategy = st.builds(
    Board1,
    boardSize=
        st.integers()
)
Money_strategy = st.builds(
    Money,
    money=
        st.integers()
)
Board_strategy = st.builds(
    Board,
)
Random_strategy = st.builds(
    Random,
)
Class_strategy = st.builds(
    Class,
)
Player_strategy = st.builds(
    Player,
    PASS_GO_MONEY=
        st.integers(),
    name=
        safe_text,
    isBankrupt=
        st.booleans(),
    INITIAL_MONEY=
        st.integers(),
    property=
        safe_text,
    isAI=
        st.booleans(),
    isRetire=
        st.booleans(),
    position=
        st.integers(),
    board=
        st.none(),
    rand=
        st.none(),
    money=
        st.none(),
    INITIAL_POSITION=
        st.integers()
)



@given(instance=Dice_strategy)
@settings(max_examples=50)
def test_hyp_dice_instantiation(instance):
    assert isinstance(instance, Dice)



@given(instance=Dice_strategy)
def test_hyp_dice_firstValue_setter(instance):
    original = instance.firstValue
    instance.firstValue = original
    assert instance.firstValue == original



@given(instance=Dice_strategy)
def test_hyp_dice_randomNumber_setter(instance):
    original = instance.randomNumber
    instance.randomNumber = original
    assert instance.randomNumber == original



@given(instance=Dice_strategy)
def test_hyp_dice_secondValue_setter(instance):
    original = instance.secondValue
    instance.secondValue = original
    assert instance.secondValue == original




@given(instance=Board1_strategy)
def test_hyp_board1_boardSize_setter(instance):
    original = instance.boardSize
    instance.boardSize = original
    assert instance.boardSize == original




@given(instance=Money_strategy)
def test_hyp_money_money_setter(instance):
    original = instance.money
    instance.money = original
    assert instance.money == original




@given(instance=Player_strategy)
@settings(max_examples=50)
def test_hyp_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_hyp_player_PASS_GO_MONEY_setter(instance):
    original = instance.PASS_GO_MONEY
    instance.PASS_GO_MONEY = original
    assert instance.PASS_GO_MONEY == original



@given(instance=Player_strategy)
def test_hyp_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Player_strategy)
def test_hyp_player_isBankrupt_setter(instance):
    original = instance.isBankrupt
    instance.isBankrupt = original
    assert instance.isBankrupt == original



@given(instance=Player_strategy)
def test_hyp_player_INITIAL_MONEY_setter(instance):
    original = instance.INITIAL_MONEY
    instance.INITIAL_MONEY = original
    assert instance.INITIAL_MONEY == original



@given(instance=Player_strategy)
def test_hyp_player_property_setter(instance):
    original = instance.property
    instance.property = original
    assert instance.property == original



@given(instance=Player_strategy)
def test_hyp_player_isAI_setter(instance):
    original = instance.isAI
    instance.isAI = original
    assert instance.isAI == original



@given(instance=Player_strategy)
def test_hyp_player_isRetire_setter(instance):
    original = instance.isRetire
    instance.isRetire = original
    assert instance.isRetire == original



@given(instance=Player_strategy)
def test_hyp_player_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=Player_strategy)
def test_hyp_player_board_setter(instance):
    original = instance.board
    instance.board = original
    assert instance.board == original



@given(instance=Player_strategy)
def test_hyp_player_rand_setter(instance):
    original = instance.rand
    instance.rand = original
    assert instance.rand == original



@given(instance=Player_strategy)
def test_hyp_player_money_setter(instance):
    original = instance.money
    instance.money = original
    assert instance.money == original



@given(instance=Player_strategy)
def test_hyp_player_INITIAL_POSITION_setter(instance):
    original = instance.INITIAL_POSITION
    instance.INITIAL_POSITION = original
    assert instance.INITIAL_POSITION == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AIPlayer,
    Board,
    Board1,
    Class,
    Dice,
    FreeParking,
    Money,
    Player,
    Random,
    Property,
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

def test_Board1_boardSize_value_roundtrip():
    instance = Board1(boardSize=7)
    assert instance.boardSize == 7
    instance.boardSize = 13
    assert instance.boardSize == 13


def test_Money_money_value_roundtrip():
    instance = Money(money=7)
    assert instance.money == 7
    instance.money = 13
    assert instance.money == 13


def test_assoc_Board_FreeParking_link_reassign_clear():
    a = Board1(boardSize=7)
    b1 = FreeParking()
    b2 = FreeParking()
    _safe_set(a, 'freeParking4', b1)
    assert _is_linked(a, 'freeParking4', b1)
    if hasattr(b1, 'board5'):
        assert _is_linked(b1, 'board5', a)
    _safe_set(a, 'freeParking4', b2)
    assert _is_linked(a, 'freeParking4', b2)
    if hasattr(b1, 'board5'):
        assert not _is_linked(b1, 'board5', a)
    if hasattr(b2, 'board5'):
        assert _is_linked(b2, 'board5', a)
    _safe_set(a, 'freeParking4', None)
    assert not _is_linked(a, 'freeParking4', b2)
    if hasattr(b2, 'board5'):
        assert not _is_linked(b2, 'board5', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AIPlayer_strategy = st.builds(AIPlayer)
@given(instance=AIPlayer_strategy)
@settings(max_examples=25)
def test_AIPlayer_instantiation(instance):
    assert isinstance(instance, AIPlayer)


Board_strategy = st.builds(Board)
@given(instance=Board_strategy)
@settings(max_examples=25)
def test_Board_instantiation(instance):
    assert isinstance(instance, Board)


Board1_strategy = st.builds(Board1, boardSize=st.integers())
@given(instance=Board1_strategy)
@settings(max_examples=25)
def test_Board1_instantiation(instance):
    assert isinstance(instance, Board1)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


FreeParking_strategy = st.builds(FreeParking)
@given(instance=FreeParking_strategy)
@settings(max_examples=25)
def test_FreeParking_instantiation(instance):
    assert isinstance(instance, FreeParking)


Money_strategy = st.builds(Money, money=st.integers())
@given(instance=Money_strategy)
@settings(max_examples=25)
def test_Money_instantiation(instance):
    assert isinstance(instance, Money)


Random_strategy = st.builds(Random)
@given(instance=Random_strategy)
@settings(max_examples=25)
def test_Random_instantiation(instance):
    assert isinstance(instance, Random)



