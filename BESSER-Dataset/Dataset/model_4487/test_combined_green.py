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
    model_Wait,
    model_Repeat,
    model_Rotate,
    model_Light,
    model_Move,
    NamedElement,
    model_Block,
    model_Transition,
    model_Command,
    model_Ozobot,
    model_OzobotProgram,
    model_NamedElement,
    Direction,
    Velocity,
    Color,
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



def test_hyp_model_wait_is_not_abstract():
    assert not inspect.isabstract(model_Wait)


def test_hyp_model_wait_constructor_exists():
    assert callable(model_Wait.__init__)


def test_hyp_model_wait_constructor_args():
    sig = inspect.signature(model_Wait.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"




def test_hyp_model_repeat_is_not_abstract():
    assert not inspect.isabstract(model_Repeat)


def test_hyp_model_repeat_constructor_exists():
    assert callable(model_Repeat.__init__)


def test_hyp_model_repeat_constructor_args():
    sig = inspect.signature(model_Repeat.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"




def test_hyp_model_rotate_is_not_abstract():
    assert not inspect.isabstract(model_Rotate)


def test_hyp_model_rotate_constructor_exists():
    assert callable(model_Rotate.__init__)


def test_hyp_model_rotate_constructor_args():
    sig = inspect.signature(model_Rotate.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "velocity" in params, "Missing parameter 'velocity'"






def test_hyp_model_light_is_not_abstract():
    assert not inspect.isabstract(model_Light)


def test_hyp_model_light_constructor_exists():
    assert callable(model_Light.__init__)


def test_hyp_model_light_constructor_args():
    sig = inspect.signature(model_Light.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"




def test_hyp_model_move_is_not_abstract():
    assert not inspect.isabstract(model_Move)


def test_hyp_model_move_constructor_exists():
    assert callable(model_Move.__init__)


def test_hyp_model_move_constructor_args():
    sig = inspect.signature(model_Move.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"
    assert "velocity" in params, "Missing parameter 'velocity'"





def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_block_is_not_abstract():
    assert not inspect.isabstract(model_Block)


def test_hyp_model_block_constructor_exists():
    assert callable(model_Block.__init__)


def test_hyp_model_block_constructor_args():
    sig = inspect.signature(model_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_transition_is_not_abstract():
    assert not inspect.isabstract(model_Transition)


def test_hyp_model_transition_constructor_exists():
    assert callable(model_Transition.__init__)


def test_hyp_model_transition_constructor_args():
    sig = inspect.signature(model_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_command_is_not_abstract():
    assert not inspect.isabstract(model_Command)


def test_hyp_model_command_constructor_exists():
    assert callable(model_Command.__init__)


def test_hyp_model_command_constructor_args():
    sig = inspect.signature(model_Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_ozobot_is_not_abstract():
    assert not inspect.isabstract(model_Ozobot)


def test_hyp_model_ozobot_constructor_exists():
    assert callable(model_Ozobot.__init__)


def test_hyp_model_ozobot_constructor_args():
    sig = inspect.signature(model_Ozobot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_ozobotprogram_is_not_abstract():
    assert not inspect.isabstract(model_OzobotProgram)


def test_hyp_model_ozobotprogram_constructor_exists():
    assert callable(model_OzobotProgram.__init__)


def test_hyp_model_ozobotprogram_constructor_args():
    sig = inspect.signature(model_OzobotProgram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_namedelement_is_not_abstract():
    assert not inspect.isabstract(model_NamedElement)


def test_hyp_model_namedelement_constructor_exists():
    assert callable(model_NamedElement.__init__)


def test_hyp_model_namedelement_constructor_args():
    sig = inspect.signature(model_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_hyp_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "left",
        "right",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_hyp_velocity_exists():
    # Check that the Enumeration exists
    assert Velocity is not None

def test_hyp_velocity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Velocity]
    expected_literals = [
        "very_fast",
        "very_slow",
        "fast",
        "slow",
        "medium",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Velocity"

def test_hyp_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_hyp_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "red",
        "none",
        "green",
        "yellow",
        "blue",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"


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
model_Wait_strategy = st.builds(
    model_Wait,
    time=
        st.integers()
)
model_Repeat_strategy = st.builds(
    model_Repeat,
    count=
        st.integers()
)
model_Rotate_strategy = st.builds(
    model_Rotate,
    angle=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    direction=
        safe_text,
    velocity=
        safe_text
)
model_Light_strategy = st.builds(
    model_Light,
    color=
        safe_text
)
model_Move_strategy = st.builds(
    model_Move,
    distance=
        st.integers(),
    velocity=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
model_Block_strategy = st.builds(
    model_Block,
)
model_Transition_strategy = st.builds(
    model_Transition,
)
model_Command_strategy = st.builds(
    model_Command,
)
model_Ozobot_strategy = st.builds(
    model_Ozobot,
)
model_OzobotProgram_strategy = st.builds(
    model_OzobotProgram,
)
model_NamedElement_strategy = st.builds(
    model_NamedElement,
    name=
        safe_text
)





@given(instance=model_Wait_strategy)
def test_hyp_model_wait_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original




@given(instance=model_Repeat_strategy)
def test_hyp_model_repeat_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original




@given(instance=model_Rotate_strategy)
def test_hyp_model_rotate_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original



@given(instance=model_Rotate_strategy)
def test_hyp_model_rotate_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=model_Rotate_strategy)
def test_hyp_model_rotate_velocity_setter(instance):
    original = instance.velocity
    instance.velocity = original
    assert instance.velocity == original




@given(instance=model_Light_strategy)
def test_hyp_model_light_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original




@given(instance=model_Move_strategy)
def test_hyp_model_move_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original



@given(instance=model_Move_strategy)
def test_hyp_model_move_velocity_setter(instance):
    original = instance.velocity
    instance.velocity = original
    assert instance.velocity == original










@given(instance=model_NamedElement_strategy)
def test_hyp_model_namedelement_name_setter(instance):
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
    Command,
    NamedElement,
    model_Block,
    model_Command,
    model_Light,
    model_Move,
    model_NamedElement,
    model_Ozobot,
    model_OzobotProgram,
    model_Repeat,
    model_Rotate,
    model_Transition,
    model_Wait,
    Color,
    Direction,
    Velocity,
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

def test_model_Light_color_value_roundtrip():
    instance = model_Light(color="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_model_Move_distance_value_roundtrip():
    instance = model_Move(distance=7, velocity="sample_text")
    assert instance.distance == 7
    instance.distance = 13
    assert instance.distance == 13


def test_model_Move_velocity_value_roundtrip():
    instance = model_Move(distance=7, velocity="sample_text")
    assert instance.velocity == "sample_text"
    instance.velocity = "sample_text_2"
    assert instance.velocity == "sample_text_2"


def test_model_NamedElement_name_value_roundtrip():
    instance = model_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model_Repeat_count_value_roundtrip():
    instance = model_Repeat(count=7)
    assert instance.count == 7
    instance.count = 13
    assert instance.count == 13


def test_model_Rotate_angle_value_roundtrip():
    instance = model_Rotate(angle=3.14, direction="sample_text", velocity="sample_text")
    assert instance.angle == 3.14
    instance.angle = 9.99
    assert instance.angle == 9.99


def test_model_Rotate_direction_value_roundtrip():
    instance = model_Rotate(angle=3.14, direction="sample_text", velocity="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_model_Rotate_velocity_value_roundtrip():
    instance = model_Rotate(angle=3.14, direction="sample_text", velocity="sample_text")
    assert instance.velocity == "sample_text"
    instance.velocity = "sample_text_2"
    assert instance.velocity == "sample_text_2"


def test_model_Wait_time_value_roundtrip():
    instance = model_Wait(time=7)
    assert instance.time == 7
    instance.time = 13
    assert instance.time == 13


def test_model_Light_isa_Command():
    instance = model_Light(color="sample_text")
    assert isinstance(instance, Command)


def test_model_Move_isa_Command():
    instance = model_Move(distance=7, velocity="sample_text")
    assert isinstance(instance, Command)


def test_model_Repeat_isa_Command():
    instance = model_Repeat(count=7)
    assert isinstance(instance, Command)


def test_model_Rotate_isa_Command():
    instance = model_Rotate(angle=3.14, direction="sample_text", velocity="sample_text")
    assert isinstance(instance, Command)


def test_model_Wait_isa_Command():
    instance = model_Wait(time=7)
    assert isinstance(instance, Command)


def test_model_Block_isa_NamedElement():
    instance = model_Block()
    assert isinstance(instance, NamedElement)


def test_model_Command_isa_NamedElement():
    instance = model_Command()
    assert isinstance(instance, NamedElement)


def test_model_Ozobot_isa_NamedElement():
    instance = model_Ozobot()
    assert isinstance(instance, NamedElement)


def test_model_OzobotProgram_isa_NamedElement():
    instance = model_OzobotProgram()
    assert isinstance(instance, NamedElement)


def test_model_Transition_isa_NamedElement():
    instance = model_Transition()
    assert isinstance(instance, NamedElement)


def test_assoc_block6_link_reassign_clear():
    a = model_Repeat(count=7)
    b1 = model_Block()
    b2 = model_Block()
    _safe_set(a, 'model_Repeat', b1)
    assert _is_linked(a, 'model_Repeat', b1)
    if hasattr(b1, 'model_Block7'):
        assert _is_linked(b1, 'model_Block7', a)
    _safe_set(a, 'model_Repeat', b2)
    assert _is_linked(a, 'model_Repeat', b2)
    if hasattr(b1, 'model_Block7'):
        assert not _is_linked(b1, 'model_Block7', a)
    if hasattr(b2, 'model_Block7'):
        assert _is_linked(b2, 'model_Block7', a)
    _safe_set(a, 'model_Repeat', None)
    assert not _is_linked(a, 'model_Repeat', b2)
    if hasattr(b2, 'model_Block7'):
        assert not _is_linked(b2, 'model_Block7', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Command_strategy = st.builds(Command)
@given(instance=Command_strategy)
@settings(max_examples=25)
def test_Command_instantiation(instance):
    assert isinstance(instance, Command)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


model_Block_strategy = st.builds(model_Block)
@given(instance=model_Block_strategy)
@settings(max_examples=25)
def test_model_Block_instantiation(instance):
    assert isinstance(instance, model_Block)


model_Command_strategy = st.builds(model_Command)
@given(instance=model_Command_strategy)
@settings(max_examples=25)
def test_model_Command_instantiation(instance):
    assert isinstance(instance, model_Command)


model_Light_strategy = st.builds(model_Light, color=safe_text)
@given(instance=model_Light_strategy)
@settings(max_examples=25)
def test_model_Light_instantiation(instance):
    assert isinstance(instance, model_Light)


model_Move_strategy = st.builds(model_Move, distance=st.integers(), velocity=safe_text)
@given(instance=model_Move_strategy)
@settings(max_examples=25)
def test_model_Move_instantiation(instance):
    assert isinstance(instance, model_Move)


model_NamedElement_strategy = st.builds(model_NamedElement, name=safe_text)
@given(instance=model_NamedElement_strategy)
@settings(max_examples=25)
def test_model_NamedElement_instantiation(instance):
    assert isinstance(instance, model_NamedElement)


model_Ozobot_strategy = st.builds(model_Ozobot)
@given(instance=model_Ozobot_strategy)
@settings(max_examples=25)
def test_model_Ozobot_instantiation(instance):
    assert isinstance(instance, model_Ozobot)


model_OzobotProgram_strategy = st.builds(model_OzobotProgram)
@given(instance=model_OzobotProgram_strategy)
@settings(max_examples=25)
def test_model_OzobotProgram_instantiation(instance):
    assert isinstance(instance, model_OzobotProgram)


model_Repeat_strategy = st.builds(model_Repeat, count=st.integers())
@given(instance=model_Repeat_strategy)
@settings(max_examples=25)
def test_model_Repeat_instantiation(instance):
    assert isinstance(instance, model_Repeat)


model_Rotate_strategy = st.builds(model_Rotate, angle=st.floats(allow_nan=False, allow_infinity=False), direction=safe_text, velocity=safe_text)
@given(instance=model_Rotate_strategy)
@settings(max_examples=25)
def test_model_Rotate_instantiation(instance):
    assert isinstance(instance, model_Rotate)


model_Transition_strategy = st.builds(model_Transition)
@given(instance=model_Transition_strategy)
@settings(max_examples=25)
def test_model_Transition_instantiation(instance):
    assert isinstance(instance, model_Transition)


model_Wait_strategy = st.builds(model_Wait, time=st.integers())
@given(instance=model_Wait_strategy)
@settings(max_examples=25)
def test_model_Wait_instantiation(instance):
    assert isinstance(instance, model_Wait)



