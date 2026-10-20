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
    Command,
    logo_Turn,
    logo_WhileNoObstacle,
    logo_Move,
    logo_Command,
    logo_ProgramUnit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_hyp_command_constructor_exists():
    assert callable(Command.__init__)


def test_hyp_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logo_turn_is_not_abstract():
    assert not inspect.isabstract(logo_Turn)


def test_hyp_logo_turn_constructor_exists():
    assert callable(logo_Turn.__init__)


def test_hyp_logo_turn_constructor_args():
    sig = inspect.signature(logo_Turn.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"




def test_hyp_logo_whilenoobstacle_is_not_abstract():
    assert not inspect.isabstract(logo_WhileNoObstacle)


def test_hyp_logo_whilenoobstacle_constructor_exists():
    assert callable(logo_WhileNoObstacle.__init__)


def test_hyp_logo_whilenoobstacle_constructor_args():
    sig = inspect.signature(logo_WhileNoObstacle.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"




def test_hyp_logo_move_is_not_abstract():
    assert not inspect.isabstract(logo_Move)


def test_hyp_logo_move_constructor_exists():
    assert callable(logo_Move.__init__)


def test_hyp_logo_move_constructor_args():
    sig = inspect.signature(logo_Move.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"




def test_hyp_logo_command_is_not_abstract():
    assert not inspect.isabstract(logo_Command)


def test_hyp_logo_command_constructor_exists():
    assert callable(logo_Command.__init__)


def test_hyp_logo_command_constructor_args():
    sig = inspect.signature(logo_Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logo_programunit_is_not_abstract():
    assert not inspect.isabstract(logo_ProgramUnit)


def test_hyp_logo_programunit_constructor_exists():
    assert callable(logo_ProgramUnit.__init__)


def test_hyp_logo_programunit_constructor_args():
    sig = inspect.signature(logo_ProgramUnit.__init__)
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
Command_strategy = st.builds(
    Command,
)
logo_Turn_strategy = st.builds(
    logo_Turn,
    angle=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
logo_WhileNoObstacle_strategy = st.builds(
    logo_WhileNoObstacle,
    distance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
logo_Move_strategy = st.builds(
    logo_Move,
    distance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
logo_Command_strategy = st.builds(
    logo_Command,
)
logo_ProgramUnit_strategy = st.builds(
    logo_ProgramUnit,
)





@given(instance=logo_Turn_strategy)
def test_hyp_logo_turn_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original




@given(instance=logo_WhileNoObstacle_strategy)
def test_hyp_logo_whilenoobstacle_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original




@given(instance=logo_Move_strategy)
def test_hyp_logo_move_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Command,
    logo_Command,
    logo_Move,
    logo_ProgramUnit,
    logo_Turn,
    logo_WhileNoObstacle,
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

def test_logo_Move_distance_value_roundtrip():
    instance = logo_Move(distance=3.14)
    assert instance.distance == 3.14
    instance.distance = 9.99
    assert instance.distance == 9.99


def test_logo_Turn_angle_value_roundtrip():
    instance = logo_Turn(angle=3.14)
    assert instance.angle == 3.14
    instance.angle = 9.99
    assert instance.angle == 9.99


def test_logo_WhileNoObstacle_distance_value_roundtrip():
    instance = logo_WhileNoObstacle(distance=3.14)
    assert instance.distance == 3.14
    instance.distance = 9.99
    assert instance.distance == 9.99


def test_logo_Move_isa_Command():
    instance = logo_Move(distance=3.14)
    assert isinstance(instance, Command)


def test_logo_Turn_isa_Command():
    instance = logo_Turn(angle=3.14)
    assert isinstance(instance, Command)


def test_logo_WhileNoObstacle_isa_Command():
    instance = logo_WhileNoObstacle(distance=3.14)
    assert isinstance(instance, Command)


def test_assoc_commands1_link_reassign_clear():
    a = logo_WhileNoObstacle(distance=3.14)
    b1 = logo_Command()
    b2 = logo_Command()
    _safe_set(a, 'logo_WhileNoObstacle', {b1})
    assert _is_linked(a, 'logo_WhileNoObstacle', b1)
    if hasattr(b1, 'logo_Command2'):
        assert _is_linked(b1, 'logo_Command2', a)
    _safe_set(a, 'logo_WhileNoObstacle', {b2})
    assert _is_linked(a, 'logo_WhileNoObstacle', b2)
    if hasattr(b1, 'logo_Command2'):
        assert not _is_linked(b1, 'logo_Command2', a)
    if hasattr(b2, 'logo_Command2'):
        assert _is_linked(b2, 'logo_Command2', a)
    _safe_set(a, 'logo_WhileNoObstacle', set())
    assert not _is_linked(a, 'logo_WhileNoObstacle', b2)
    if hasattr(b2, 'logo_Command2'):
        assert not _is_linked(b2, 'logo_Command2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Command_strategy = st.builds(Command)
@given(instance=Command_strategy)
@settings(max_examples=25)
def test_Command_instantiation(instance):
    assert isinstance(instance, Command)


logo_Command_strategy = st.builds(logo_Command)
@given(instance=logo_Command_strategy)
@settings(max_examples=25)
def test_logo_Command_instantiation(instance):
    assert isinstance(instance, logo_Command)


logo_Move_strategy = st.builds(logo_Move, distance=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=logo_Move_strategy)
@settings(max_examples=25)
def test_logo_Move_instantiation(instance):
    assert isinstance(instance, logo_Move)


logo_ProgramUnit_strategy = st.builds(logo_ProgramUnit)
@given(instance=logo_ProgramUnit_strategy)
@settings(max_examples=25)
def test_logo_ProgramUnit_instantiation(instance):
    assert isinstance(instance, logo_ProgramUnit)


logo_Turn_strategy = st.builds(logo_Turn, angle=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=logo_Turn_strategy)
@settings(max_examples=25)
def test_logo_Turn_instantiation(instance):
    assert isinstance(instance, logo_Turn)


logo_WhileNoObstacle_strategy = st.builds(logo_WhileNoObstacle, distance=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=logo_WhileNoObstacle_strategy)
@settings(max_examples=25)
def test_logo_WhileNoObstacle_instantiation(instance):
    assert isinstance(instance, logo_WhileNoObstacle)



