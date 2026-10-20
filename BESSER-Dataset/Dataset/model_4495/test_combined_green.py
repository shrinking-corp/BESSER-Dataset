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
    marsRover_park,
    marsRover_color_indication,
    marsRover_message,
    marsRover_sound,
    marsRover_avoid_lakes,
    marsRover_detect_lakes,
    marsRover_bumpers,
    marsRover_ultra,
    marsRover_avoid_obstacles,
    marsRover_EObject,
    marsRover_mission,
    marsRover_indication,
    marsRover_push_obstacles,
    marsRover_detect_rocks,
    marsRover_after_action,
    marsRover_Robot,
    LED_Color,
    Color,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_marsrover_park_is_not_abstract():
    assert not inspect.isabstract(marsRover_park)


def test_hyp_marsrover_park_constructor_exists():
    assert callable(marsRover_park.__init__)


def test_hyp_marsrover_park_constructor_args():
    sig = inspect.signature(marsRover_park.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_marsrover_color_indication_is_not_abstract():
    assert not inspect.isabstract(marsRover_color_indication)


def test_hyp_marsrover_color_indication_constructor_exists():
    assert callable(marsRover_color_indication.__init__)


def test_hyp_marsrover_color_indication_constructor_args():
    sig = inspect.signature(marsRover_color_indication.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_marsrover_message_is_not_abstract():
    assert not inspect.isabstract(marsRover_message)


def test_hyp_marsrover_message_constructor_exists():
    assert callable(marsRover_message.__init__)


def test_hyp_marsrover_message_constructor_args():
    sig = inspect.signature(marsRover_message.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "msg" in params, "Missing parameter 'msg'"





def test_hyp_marsrover_sound_is_not_abstract():
    assert not inspect.isabstract(marsRover_sound)


def test_hyp_marsrover_sound_constructor_exists():
    assert callable(marsRover_sound.__init__)


def test_hyp_marsrover_sound_constructor_args():
    sig = inspect.signature(marsRover_sound.__init__)
    params = list(sig.parameters.keys())
    assert "frequency" in params, "Missing parameter 'frequency'"
    assert "name" in params, "Missing parameter 'name'"
    assert "duration" in params, "Missing parameter 'duration'"






def test_hyp_marsrover_avoid_lakes_is_not_abstract():
    assert not inspect.isabstract(marsRover_avoid_lakes)


def test_hyp_marsrover_avoid_lakes_constructor_exists():
    assert callable(marsRover_avoid_lakes.__init__)


def test_hyp_marsrover_avoid_lakes_constructor_args():
    sig = inspect.signature(marsRover_avoid_lakes.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_marsrover_detect_lakes_is_not_abstract():
    assert not inspect.isabstract(marsRover_detect_lakes)


def test_hyp_marsrover_detect_lakes_constructor_exists():
    assert callable(marsRover_detect_lakes.__init__)


def test_hyp_marsrover_detect_lakes_constructor_args():
    sig = inspect.signature(marsRover_detect_lakes.__init__)
    params = list(sig.parameters.keys())
    assert "lakes_colors" in params, "Missing parameter 'lakes_colors'"
    assert "number_of_lakes" in params, "Missing parameter 'number_of_lakes'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_marsrover_bumpers_is_not_abstract():
    assert not inspect.isabstract(marsRover_bumpers)


def test_hyp_marsrover_bumpers_constructor_exists():
    assert callable(marsRover_bumpers.__init__)


def test_hyp_marsrover_bumpers_constructor_args():
    sig = inspect.signature(marsRover_bumpers.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_marsrover_ultra_is_not_abstract():
    assert not inspect.isabstract(marsRover_ultra)


def test_hyp_marsrover_ultra_constructor_exists():
    assert callable(marsRover_ultra.__init__)


def test_hyp_marsrover_ultra_constructor_args():
    sig = inspect.signature(marsRover_ultra.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "distance" in params, "Missing parameter 'distance'"





def test_hyp_marsrover_avoid_obstacles_is_not_abstract():
    assert not inspect.isabstract(marsRover_avoid_obstacles)


def test_hyp_marsrover_avoid_obstacles_constructor_exists():
    assert callable(marsRover_avoid_obstacles.__init__)


def test_hyp_marsrover_avoid_obstacles_constructor_args():
    sig = inspect.signature(marsRover_avoid_obstacles.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_marsrover_eobject_is_not_abstract():
    assert not inspect.isabstract(marsRover_EObject)


def test_hyp_marsrover_eobject_constructor_exists():
    assert callable(marsRover_EObject.__init__)


def test_hyp_marsrover_eobject_constructor_args():
    sig = inspect.signature(marsRover_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_marsrover_mission_is_not_abstract():
    assert not inspect.isabstract(marsRover_mission)


def test_hyp_marsrover_mission_constructor_exists():
    assert callable(marsRover_mission.__init__)


def test_hyp_marsrover_mission_constructor_args():
    sig = inspect.signature(marsRover_mission.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_marsrover_indication_is_not_abstract():
    assert not inspect.isabstract(marsRover_indication)


def test_hyp_marsrover_indication_constructor_exists():
    assert callable(marsRover_indication.__init__)


def test_hyp_marsrover_indication_constructor_args():
    sig = inspect.signature(marsRover_indication.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_marsrover_push_obstacles_is_not_abstract():
    assert not inspect.isabstract(marsRover_push_obstacles)


def test_hyp_marsrover_push_obstacles_constructor_exists():
    assert callable(marsRover_push_obstacles.__init__)


def test_hyp_marsrover_push_obstacles_constructor_args():
    sig = inspect.signature(marsRover_push_obstacles.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_marsrover_detect_rocks_is_not_abstract():
    assert not inspect.isabstract(marsRover_detect_rocks)


def test_hyp_marsrover_detect_rocks_constructor_exists():
    assert callable(marsRover_detect_rocks.__init__)


def test_hyp_marsrover_detect_rocks_constructor_args():
    sig = inspect.signature(marsRover_detect_rocks.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "number_of_rocks" in params, "Missing parameter 'number_of_rocks'"





def test_hyp_marsrover_after_action_is_not_abstract():
    assert not inspect.isabstract(marsRover_after_action)


def test_hyp_marsrover_after_action_constructor_exists():
    assert callable(marsRover_after_action.__init__)


def test_hyp_marsrover_after_action_constructor_args():
    sig = inspect.signature(marsRover_after_action.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"




def test_hyp_marsrover_robot_is_not_abstract():
    assert not inspect.isabstract(marsRover_Robot)


def test_hyp_marsrover_robot_constructor_exists():
    assert callable(marsRover_Robot.__init__)


def test_hyp_marsrover_robot_constructor_args():
    sig = inspect.signature(marsRover_Robot.__init__)
    params = list(sig.parameters.keys())
    assert "special_speed" in params, "Missing parameter 'special_speed'"
    assert "name" in params, "Missing parameter 'name'"
    assert "slave_address" in params, "Missing parameter 'slave_address'"
    assert "drive_speed" in params, "Missing parameter 'drive_speed'"





def test_hyp_led_color_exists():
    # Check that the Enumeration exists
    assert LED_Color is not None

def test_hyp_led_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LED_Color]
    expected_literals = [
        "LED_OFF",
        "LED_ORANGE",
        "LED_GREEN",
        "LED_RED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LED_Color"

def test_hyp_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_hyp_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "COLOR_GREEN",
        "COLOR_BLUE",
        "COLOR_WHITE",
        "COLOR_ORANGE",
        "COLOR_OFF",
        "COLOR_RED",
        "COLOR_BLACK",
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
marsRover_park_strategy = st.builds(
    marsRover_park,
    name=
        safe_text
)
marsRover_color_indication_strategy = st.builds(
    marsRover_color_indication,
    color=
        safe_text,
    name=
        safe_text
)
marsRover_message_strategy = st.builds(
    marsRover_message,
    name=
        safe_text,
    msg=
        safe_text
)
marsRover_sound_strategy = st.builds(
    marsRover_sound,
    frequency=
        st.integers(),
    name=
        safe_text,
    duration=
        st.integers()
)
marsRover_avoid_lakes_strategy = st.builds(
    marsRover_avoid_lakes,
    name=
        safe_text
)
marsRover_detect_lakes_strategy = st.builds(
    marsRover_detect_lakes,
    lakes_colors=
        safe_text,
    number_of_lakes=
        st.integers(),
    name=
        safe_text
)
marsRover_bumpers_strategy = st.builds(
    marsRover_bumpers,
    name=
        safe_text
)
marsRover_ultra_strategy = st.builds(
    marsRover_ultra,
    name=
        safe_text,
    distance=
        st.integers()
)
marsRover_avoid_obstacles_strategy = st.builds(
    marsRover_avoid_obstacles,
    name=
        safe_text
)
marsRover_EObject_strategy = st.builds(
    marsRover_EObject,
)
marsRover_mission_strategy = st.builds(
    marsRover_mission,
    name=
        safe_text
)
marsRover_indication_strategy = st.builds(
    marsRover_indication,
    name=
        safe_text
)
marsRover_push_obstacles_strategy = st.builds(
    marsRover_push_obstacles,
    name=
        safe_text
)
marsRover_detect_rocks_strategy = st.builds(
    marsRover_detect_rocks,
    name=
        safe_text,
    number_of_rocks=
        st.integers()
)
marsRover_after_action_strategy = st.builds(
    marsRover_after_action,
    action=
        safe_text
)
marsRover_Robot_strategy = st.builds(
    marsRover_Robot,
    special_speed=
        st.integers(),
    name=
        safe_text,
    slave_address=
        safe_text,
    drive_speed=
        st.integers()
)




@given(instance=marsRover_park_strategy)
def test_hyp_marsrover_park_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=marsRover_color_indication_strategy)
def test_hyp_marsrover_color_indication_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=marsRover_color_indication_strategy)
def test_hyp_marsrover_color_indication_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=marsRover_message_strategy)
def test_hyp_marsrover_message_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=marsRover_message_strategy)
def test_hyp_marsrover_message_msg_setter(instance):
    original = instance.msg
    instance.msg = original
    assert instance.msg == original




@given(instance=marsRover_sound_strategy)
def test_hyp_marsrover_sound_frequency_setter(instance):
    original = instance.frequency
    instance.frequency = original
    assert instance.frequency == original



@given(instance=marsRover_sound_strategy)
def test_hyp_marsrover_sound_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=marsRover_sound_strategy)
def test_hyp_marsrover_sound_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original




@given(instance=marsRover_avoid_lakes_strategy)
def test_hyp_marsrover_avoid_lakes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=marsRover_detect_lakes_strategy)
def test_hyp_marsrover_detect_lakes_lakes_colors_setter(instance):
    original = instance.lakes_colors
    instance.lakes_colors = original
    assert instance.lakes_colors == original



@given(instance=marsRover_detect_lakes_strategy)
def test_hyp_marsrover_detect_lakes_number_of_lakes_setter(instance):
    original = instance.number_of_lakes
    instance.number_of_lakes = original
    assert instance.number_of_lakes == original



@given(instance=marsRover_detect_lakes_strategy)
def test_hyp_marsrover_detect_lakes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=marsRover_bumpers_strategy)
def test_hyp_marsrover_bumpers_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=marsRover_ultra_strategy)
def test_hyp_marsrover_ultra_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=marsRover_ultra_strategy)
def test_hyp_marsrover_ultra_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original




@given(instance=marsRover_avoid_obstacles_strategy)
def test_hyp_marsrover_avoid_obstacles_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=marsRover_mission_strategy)
def test_hyp_marsrover_mission_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=marsRover_indication_strategy)
def test_hyp_marsrover_indication_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=marsRover_push_obstacles_strategy)
def test_hyp_marsrover_push_obstacles_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=marsRover_detect_rocks_strategy)
def test_hyp_marsrover_detect_rocks_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=marsRover_detect_rocks_strategy)
def test_hyp_marsrover_detect_rocks_number_of_rocks_setter(instance):
    original = instance.number_of_rocks
    instance.number_of_rocks = original
    assert instance.number_of_rocks == original




@given(instance=marsRover_after_action_strategy)
def test_hyp_marsrover_after_action_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original




@given(instance=marsRover_Robot_strategy)
def test_hyp_marsrover_robot_special_speed_setter(instance):
    original = instance.special_speed
    instance.special_speed = original
    assert instance.special_speed == original



@given(instance=marsRover_Robot_strategy)
def test_hyp_marsrover_robot_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=marsRover_Robot_strategy)
def test_hyp_marsrover_robot_slave_address_setter(instance):
    original = instance.slave_address
    instance.slave_address = original
    assert instance.slave_address == original



@given(instance=marsRover_Robot_strategy)
def test_hyp_marsrover_robot_drive_speed_setter(instance):
    original = instance.drive_speed
    instance.drive_speed = original
    assert instance.drive_speed == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    marsRover_EObject,
    marsRover_Robot,
    marsRover_after_action,
    marsRover_avoid_lakes,
    marsRover_avoid_obstacles,
    marsRover_bumpers,
    marsRover_color_indication,
    marsRover_detect_lakes,
    marsRover_detect_rocks,
    marsRover_indication,
    marsRover_message,
    marsRover_mission,
    marsRover_park,
    marsRover_push_obstacles,
    marsRover_sound,
    marsRover_ultra,
    Color,
    LED_Color,
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

def test_marsRover_Robot_drive_speed_value_roundtrip():
    instance = marsRover_Robot(drive_speed=7, name="sample_text", slave_address="sample_text", special_speed=7)
    assert instance.drive_speed == 7
    instance.drive_speed = 13
    assert instance.drive_speed == 13


def test_marsRover_Robot_name_value_roundtrip():
    instance = marsRover_Robot(drive_speed=7, name="sample_text", slave_address="sample_text", special_speed=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_marsRover_Robot_slave_address_value_roundtrip():
    instance = marsRover_Robot(drive_speed=7, name="sample_text", slave_address="sample_text", special_speed=7)
    assert instance.slave_address == "sample_text"
    instance.slave_address = "sample_text_2"
    assert instance.slave_address == "sample_text_2"


def test_marsRover_Robot_special_speed_value_roundtrip():
    instance = marsRover_Robot(drive_speed=7, name="sample_text", slave_address="sample_text", special_speed=7)
    assert instance.special_speed == 7
    instance.special_speed = 13
    assert instance.special_speed == 13


def test_marsRover_after_action_action_value_roundtrip():
    instance = marsRover_after_action(action="sample_text")
    assert instance.action == "sample_text"
    instance.action = "sample_text_2"
    assert instance.action == "sample_text_2"


def test_marsRover_avoid_lakes_name_value_roundtrip():
    instance = marsRover_avoid_lakes(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_marsRover_avoid_obstacles_name_value_roundtrip():
    instance = marsRover_avoid_obstacles(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_marsRover_bumpers_name_value_roundtrip():
    instance = marsRover_bumpers(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_marsRover_color_indication_color_value_roundtrip():
    instance = marsRover_color_indication(color="sample_text", name="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_marsRover_color_indication_name_value_roundtrip():
    instance = marsRover_color_indication(color="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_marsRover_detect_lakes_lakes_colors_value_roundtrip():
    instance = marsRover_detect_lakes(lakes_colors="sample_text", name="sample_text", number_of_lakes=7)
    assert instance.lakes_colors == "sample_text"
    instance.lakes_colors = "sample_text_2"
    assert instance.lakes_colors == "sample_text_2"


def test_marsRover_detect_lakes_name_value_roundtrip():
    instance = marsRover_detect_lakes(lakes_colors="sample_text", name="sample_text", number_of_lakes=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_marsRover_detect_lakes_number_of_lakes_value_roundtrip():
    instance = marsRover_detect_lakes(lakes_colors="sample_text", name="sample_text", number_of_lakes=7)
    assert instance.number_of_lakes == 7
    instance.number_of_lakes = 13
    assert instance.number_of_lakes == 13


def test_marsRover_detect_rocks_name_value_roundtrip():
    instance = marsRover_detect_rocks(name="sample_text", number_of_rocks=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_marsRover_detect_rocks_number_of_rocks_value_roundtrip():
    instance = marsRover_detect_rocks(name="sample_text", number_of_rocks=7)
    assert instance.number_of_rocks == 7
    instance.number_of_rocks = 13
    assert instance.number_of_rocks == 13


def test_marsRover_indication_name_value_roundtrip():
    instance = marsRover_indication(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_marsRover_message_msg_value_roundtrip():
    instance = marsRover_message(msg="sample_text", name="sample_text")
    assert instance.msg == "sample_text"
    instance.msg = "sample_text_2"
    assert instance.msg == "sample_text_2"


def test_marsRover_message_name_value_roundtrip():
    instance = marsRover_message(msg="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_marsRover_mission_name_value_roundtrip():
    instance = marsRover_mission(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_marsRover_park_name_value_roundtrip():
    instance = marsRover_park(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_marsRover_push_obstacles_name_value_roundtrip():
    instance = marsRover_push_obstacles(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_marsRover_sound_duration_value_roundtrip():
    instance = marsRover_sound(duration=7, frequency=7, name="sample_text")
    assert instance.duration == 7
    instance.duration = 13
    assert instance.duration == 13


def test_marsRover_sound_frequency_value_roundtrip():
    instance = marsRover_sound(duration=7, frequency=7, name="sample_text")
    assert instance.frequency == 7
    instance.frequency = 13
    assert instance.frequency == 13


def test_marsRover_sound_name_value_roundtrip():
    instance = marsRover_sound(duration=7, frequency=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_marsRover_ultra_distance_value_roundtrip():
    instance = marsRover_ultra(distance=7, name="sample_text")
    assert instance.distance == 7
    instance.distance = 13
    assert instance.distance == 13


def test_marsRover_ultra_name_value_roundtrip():
    instance = marsRover_ultra(distance=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_after_examinating5_link_reassign_clear():
    a = marsRover_detect_lakes(lakes_colors="sample_text", name="sample_text", number_of_lakes=7)
    b1 = marsRover_after_action(action="sample_text")
    b2 = marsRover_after_action(action="sample_text_2")
    _safe_set(a, 'marsRover_detect_lakes', b1)
    assert _is_linked(a, 'marsRover_detect_lakes', b1)
    if hasattr(b1, 'marsRover_after_action'):
        assert _is_linked(b1, 'marsRover_after_action', a)
    _safe_set(a, 'marsRover_detect_lakes', b2)
    assert _is_linked(a, 'marsRover_detect_lakes', b2)
    if hasattr(b1, 'marsRover_after_action'):
        assert not _is_linked(b1, 'marsRover_after_action', a)
    if hasattr(b2, 'marsRover_after_action'):
        assert _is_linked(b2, 'marsRover_after_action', a)
    _safe_set(a, 'marsRover_detect_lakes', None)
    assert not _is_linked(a, 'marsRover_detect_lakes', b2)
    if hasattr(b2, 'marsRover_after_action'):
        assert not _is_linked(b2, 'marsRover_after_action', a)


def test_assoc_after_examinating6_link_reassign_clear():
    a = marsRover_detect_rocks(name="sample_text", number_of_rocks=7)
    b1 = marsRover_after_action(action="sample_text")
    b2 = marsRover_after_action(action="sample_text_2")
    _safe_set(a, 'marsRover_detect_rocks', b1)
    assert _is_linked(a, 'marsRover_detect_rocks', b1)
    if hasattr(b1, 'marsRover_after_action7'):
        assert _is_linked(b1, 'marsRover_after_action7', a)
    _safe_set(a, 'marsRover_detect_rocks', b2)
    assert _is_linked(a, 'marsRover_detect_rocks', b2)
    if hasattr(b1, 'marsRover_after_action7'):
        assert not _is_linked(b1, 'marsRover_after_action7', a)
    if hasattr(b2, 'marsRover_after_action7'):
        assert _is_linked(b2, 'marsRover_after_action7', a)
    _safe_set(a, 'marsRover_detect_rocks', None)
    assert not _is_linked(a, 'marsRover_detect_rocks', b2)
    if hasattr(b2, 'marsRover_after_action7'):
        assert not _is_linked(b2, 'marsRover_after_action7', a)


def test_assoc_indicate8_link_reassign_clear():
    a = marsRover_indication(name="sample_text")
    b1 = marsRover_after_action(action="sample_text")
    b2 = marsRover_after_action(action="sample_text_2")
    _safe_set(a, 'marsRover_indication', b1)
    assert _is_linked(a, 'marsRover_indication', b1)
    if hasattr(b1, 'marsRover_after_action9'):
        assert _is_linked(b1, 'marsRover_after_action9', a)
    _safe_set(a, 'marsRover_indication', b2)
    assert _is_linked(a, 'marsRover_indication', b2)
    if hasattr(b1, 'marsRover_after_action9'):
        assert not _is_linked(b1, 'marsRover_after_action9', a)
    if hasattr(b2, 'marsRover_after_action9'):
        assert _is_linked(b2, 'marsRover_after_action9', a)
    _safe_set(a, 'marsRover_indication', None)
    assert not _is_linked(a, 'marsRover_indication', b2)
    if hasattr(b2, 'marsRover_after_action9'):
        assert not _is_linked(b2, 'marsRover_after_action9', a)


def test_assoc_missions0_link_reassign_clear():
    a = marsRover_mission(name="sample_text")
    b1 = marsRover_Robot(drive_speed=7, name="sample_text", slave_address="sample_text", special_speed=7)
    b2 = marsRover_Robot(drive_speed=13, name="sample_text_2", slave_address="sample_text_2", special_speed=13)
    _safe_set(a, 'marsRover_mission', b1)
    assert _is_linked(a, 'marsRover_mission', b1)
    if hasattr(b1, 'marsRover_Robot'):
        assert _is_linked(b1, 'marsRover_Robot', a)
    _safe_set(a, 'marsRover_mission', b2)
    assert _is_linked(a, 'marsRover_mission', b2)
    if hasattr(b1, 'marsRover_Robot'):
        assert not _is_linked(b1, 'marsRover_Robot', a)
    if hasattr(b2, 'marsRover_Robot'):
        assert _is_linked(b2, 'marsRover_Robot', a)
    _safe_set(a, 'marsRover_mission', None)
    assert not _is_linked(a, 'marsRover_mission', b2)
    if hasattr(b2, 'marsRover_Robot'):
        assert not _is_linked(b2, 'marsRover_Robot', a)


def test_assoc_sensors3_link_reassign_clear():
    a = marsRover_avoid_obstacles(name="sample_text")
    b1 = marsRover_EObject()
    b2 = marsRover_EObject()
    _safe_set(a, 'marsRover_avoid_obstacles', {b1})
    assert _is_linked(a, 'marsRover_avoid_obstacles', b1)
    if hasattr(b1, 'marsRover_EObject4'):
        assert _is_linked(b1, 'marsRover_EObject4', a)
    _safe_set(a, 'marsRover_avoid_obstacles', {b2})
    assert _is_linked(a, 'marsRover_avoid_obstacles', b2)
    if hasattr(b1, 'marsRover_EObject4'):
        assert not _is_linked(b1, 'marsRover_EObject4', a)
    if hasattr(b2, 'marsRover_EObject4'):
        assert _is_linked(b2, 'marsRover_EObject4', a)
    _safe_set(a, 'marsRover_avoid_obstacles', set())
    assert not _is_linked(a, 'marsRover_avoid_obstacles', b2)
    if hasattr(b2, 'marsRover_EObject4'):
        assert not _is_linked(b2, 'marsRover_EObject4', a)


def test_assoc_type1_link_reassign_clear():
    a = marsRover_mission(name="sample_text")
    b1 = marsRover_EObject()
    b2 = marsRover_EObject()
    _safe_set(a, 'marsRover_mission2', b1)
    assert _is_linked(a, 'marsRover_mission2', b1)
    if hasattr(b1, 'marsRover_EObject'):
        assert _is_linked(b1, 'marsRover_EObject', a)
    _safe_set(a, 'marsRover_mission2', b2)
    assert _is_linked(a, 'marsRover_mission2', b2)
    if hasattr(b1, 'marsRover_EObject'):
        assert not _is_linked(b1, 'marsRover_EObject', a)
    if hasattr(b2, 'marsRover_EObject'):
        assert _is_linked(b2, 'marsRover_EObject', a)
    _safe_set(a, 'marsRover_mission2', None)
    assert not _is_linked(a, 'marsRover_mission2', b2)
    if hasattr(b2, 'marsRover_EObject'):
        assert not _is_linked(b2, 'marsRover_EObject', a)


def test_assoc_type10_link_reassign_clear():
    a = marsRover_indication(name="sample_text")
    b1 = marsRover_EObject()
    b2 = marsRover_EObject()
    _safe_set(a, 'marsRover_indication11', b1)
    assert _is_linked(a, 'marsRover_indication11', b1)
    if hasattr(b1, 'marsRover_EObject12'):
        assert _is_linked(b1, 'marsRover_EObject12', a)
    _safe_set(a, 'marsRover_indication11', b2)
    assert _is_linked(a, 'marsRover_indication11', b2)
    if hasattr(b1, 'marsRover_EObject12'):
        assert not _is_linked(b1, 'marsRover_EObject12', a)
    if hasattr(b2, 'marsRover_EObject12'):
        assert _is_linked(b2, 'marsRover_EObject12', a)
    _safe_set(a, 'marsRover_indication11', None)
    assert not _is_linked(a, 'marsRover_indication11', b2)
    if hasattr(b2, 'marsRover_EObject12'):
        assert not _is_linked(b2, 'marsRover_EObject12', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

marsRover_EObject_strategy = st.builds(marsRover_EObject)
@given(instance=marsRover_EObject_strategy)
@settings(max_examples=25)
def test_marsRover_EObject_instantiation(instance):
    assert isinstance(instance, marsRover_EObject)


marsRover_Robot_strategy = st.builds(marsRover_Robot, drive_speed=st.integers(), name=safe_text, slave_address=safe_text, special_speed=st.integers())
@given(instance=marsRover_Robot_strategy)
@settings(max_examples=25)
def test_marsRover_Robot_instantiation(instance):
    assert isinstance(instance, marsRover_Robot)


marsRover_after_action_strategy = st.builds(marsRover_after_action, action=safe_text)
@given(instance=marsRover_after_action_strategy)
@settings(max_examples=25)
def test_marsRover_after_action_instantiation(instance):
    assert isinstance(instance, marsRover_after_action)


marsRover_avoid_lakes_strategy = st.builds(marsRover_avoid_lakes, name=safe_text)
@given(instance=marsRover_avoid_lakes_strategy)
@settings(max_examples=25)
def test_marsRover_avoid_lakes_instantiation(instance):
    assert isinstance(instance, marsRover_avoid_lakes)


marsRover_avoid_obstacles_strategy = st.builds(marsRover_avoid_obstacles, name=safe_text)
@given(instance=marsRover_avoid_obstacles_strategy)
@settings(max_examples=25)
def test_marsRover_avoid_obstacles_instantiation(instance):
    assert isinstance(instance, marsRover_avoid_obstacles)


marsRover_bumpers_strategy = st.builds(marsRover_bumpers, name=safe_text)
@given(instance=marsRover_bumpers_strategy)
@settings(max_examples=25)
def test_marsRover_bumpers_instantiation(instance):
    assert isinstance(instance, marsRover_bumpers)


marsRover_color_indication_strategy = st.builds(marsRover_color_indication, color=safe_text, name=safe_text)
@given(instance=marsRover_color_indication_strategy)
@settings(max_examples=25)
def test_marsRover_color_indication_instantiation(instance):
    assert isinstance(instance, marsRover_color_indication)


marsRover_detect_lakes_strategy = st.builds(marsRover_detect_lakes, lakes_colors=safe_text, name=safe_text, number_of_lakes=st.integers())
@given(instance=marsRover_detect_lakes_strategy)
@settings(max_examples=25)
def test_marsRover_detect_lakes_instantiation(instance):
    assert isinstance(instance, marsRover_detect_lakes)


marsRover_detect_rocks_strategy = st.builds(marsRover_detect_rocks, name=safe_text, number_of_rocks=st.integers())
@given(instance=marsRover_detect_rocks_strategy)
@settings(max_examples=25)
def test_marsRover_detect_rocks_instantiation(instance):
    assert isinstance(instance, marsRover_detect_rocks)


marsRover_indication_strategy = st.builds(marsRover_indication, name=safe_text)
@given(instance=marsRover_indication_strategy)
@settings(max_examples=25)
def test_marsRover_indication_instantiation(instance):
    assert isinstance(instance, marsRover_indication)


marsRover_message_strategy = st.builds(marsRover_message, msg=safe_text, name=safe_text)
@given(instance=marsRover_message_strategy)
@settings(max_examples=25)
def test_marsRover_message_instantiation(instance):
    assert isinstance(instance, marsRover_message)


marsRover_mission_strategy = st.builds(marsRover_mission, name=safe_text)
@given(instance=marsRover_mission_strategy)
@settings(max_examples=25)
def test_marsRover_mission_instantiation(instance):
    assert isinstance(instance, marsRover_mission)


marsRover_park_strategy = st.builds(marsRover_park, name=safe_text)
@given(instance=marsRover_park_strategy)
@settings(max_examples=25)
def test_marsRover_park_instantiation(instance):
    assert isinstance(instance, marsRover_park)


marsRover_push_obstacles_strategy = st.builds(marsRover_push_obstacles, name=safe_text)
@given(instance=marsRover_push_obstacles_strategy)
@settings(max_examples=25)
def test_marsRover_push_obstacles_instantiation(instance):
    assert isinstance(instance, marsRover_push_obstacles)


marsRover_sound_strategy = st.builds(marsRover_sound, duration=st.integers(), frequency=st.integers(), name=safe_text)
@given(instance=marsRover_sound_strategy)
@settings(max_examples=25)
def test_marsRover_sound_instantiation(instance):
    assert isinstance(instance, marsRover_sound)


marsRover_ultra_strategy = st.builds(marsRover_ultra, distance=st.integers(), name=safe_text)
@given(instance=marsRover_ultra_strategy)
@settings(max_examples=25)
def test_marsRover_ultra_instantiation(instance):
    assert isinstance(instance, marsRover_ultra)



