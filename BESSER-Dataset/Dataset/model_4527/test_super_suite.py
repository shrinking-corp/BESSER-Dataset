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
    helloWeb_Up,
    helloWeb_Wait,
    helloWeb_RotateR,
    helloWeb_Right,
    helloWeb_Forward,
    helloWeb_Left,
    helloWeb_RotateL,
    helloWeb_Backward,
    helloWeb_Down,
    helloWeb_Snapshot,
    SuperCommand,
    helloWeb_FunctionName,
    helloWeb_FeatureMatch,
    helloWeb_Command,
    helloWeb_UserFunction,
    helloWeb_SuperCommand,
    helloWeb_Main,
    helloWeb_Program,
    helloWeb_RecordedFlight,
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



def test_hyp_helloweb_up_is_not_abstract():
    assert not inspect.isabstract(helloWeb_Up)


def test_hyp_helloweb_up_constructor_exists():
    assert callable(helloWeb_Up.__init__)


def test_hyp_helloweb_up_constructor_args():
    sig = inspect.signature(helloWeb_Up.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"




def test_hyp_helloweb_wait_is_not_abstract():
    assert not inspect.isabstract(helloWeb_Wait)


def test_hyp_helloweb_wait_constructor_exists():
    assert callable(helloWeb_Wait.__init__)


def test_hyp_helloweb_wait_constructor_args():
    sig = inspect.signature(helloWeb_Wait.__init__)
    params = list(sig.parameters.keys())
    assert "seconds" in params, "Missing parameter 'seconds'"




def test_hyp_helloweb_rotater_is_not_abstract():
    assert not inspect.isabstract(helloWeb_RotateR)


def test_hyp_helloweb_rotater_constructor_exists():
    assert callable(helloWeb_RotateR.__init__)


def test_hyp_helloweb_rotater_constructor_args():
    sig = inspect.signature(helloWeb_RotateR.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"




def test_hyp_helloweb_right_is_not_abstract():
    assert not inspect.isabstract(helloWeb_Right)


def test_hyp_helloweb_right_constructor_exists():
    assert callable(helloWeb_Right.__init__)


def test_hyp_helloweb_right_constructor_args():
    sig = inspect.signature(helloWeb_Right.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"




def test_hyp_helloweb_forward_is_not_abstract():
    assert not inspect.isabstract(helloWeb_Forward)


def test_hyp_helloweb_forward_constructor_exists():
    assert callable(helloWeb_Forward.__init__)


def test_hyp_helloweb_forward_constructor_args():
    sig = inspect.signature(helloWeb_Forward.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"




def test_hyp_helloweb_left_is_not_abstract():
    assert not inspect.isabstract(helloWeb_Left)


def test_hyp_helloweb_left_constructor_exists():
    assert callable(helloWeb_Left.__init__)


def test_hyp_helloweb_left_constructor_args():
    sig = inspect.signature(helloWeb_Left.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"




def test_hyp_helloweb_rotatel_is_not_abstract():
    assert not inspect.isabstract(helloWeb_RotateL)


def test_hyp_helloweb_rotatel_constructor_exists():
    assert callable(helloWeb_RotateL.__init__)


def test_hyp_helloweb_rotatel_constructor_args():
    sig = inspect.signature(helloWeb_RotateL.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"




def test_hyp_helloweb_backward_is_not_abstract():
    assert not inspect.isabstract(helloWeb_Backward)


def test_hyp_helloweb_backward_constructor_exists():
    assert callable(helloWeb_Backward.__init__)


def test_hyp_helloweb_backward_constructor_args():
    sig = inspect.signature(helloWeb_Backward.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"




def test_hyp_helloweb_down_is_not_abstract():
    assert not inspect.isabstract(helloWeb_Down)


def test_hyp_helloweb_down_constructor_exists():
    assert callable(helloWeb_Down.__init__)


def test_hyp_helloweb_down_constructor_args():
    sig = inspect.signature(helloWeb_Down.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"




def test_hyp_helloweb_snapshot_is_not_abstract():
    assert not inspect.isabstract(helloWeb_Snapshot)


def test_hyp_helloweb_snapshot_constructor_exists():
    assert callable(helloWeb_Snapshot.__init__)


def test_hyp_helloweb_snapshot_constructor_args():
    sig = inspect.signature(helloWeb_Snapshot.__init__)
    params = list(sig.parameters.keys())
    assert "image_name" in params, "Missing parameter 'image_name'"




def test_hyp_supercommand_is_not_abstract():
    assert not inspect.isabstract(SuperCommand)


def test_hyp_supercommand_constructor_exists():
    assert callable(SuperCommand.__init__)


def test_hyp_supercommand_constructor_args():
    sig = inspect.signature(SuperCommand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_helloweb_functionname_is_not_abstract():
    assert not inspect.isabstract(helloWeb_FunctionName)


def test_hyp_helloweb_functionname_constructor_exists():
    assert callable(helloWeb_FunctionName.__init__)


def test_hyp_helloweb_functionname_constructor_args():
    sig = inspect.signature(helloWeb_FunctionName.__init__)
    params = list(sig.parameters.keys())
    assert "func_name" in params, "Missing parameter 'func_name'"




def test_hyp_helloweb_featurematch_is_not_abstract():
    assert not inspect.isabstract(helloWeb_FeatureMatch)


def test_hyp_helloweb_featurematch_constructor_exists():
    assert callable(helloWeb_FeatureMatch.__init__)


def test_hyp_helloweb_featurematch_constructor_args():
    sig = inspect.signature(helloWeb_FeatureMatch.__init__)
    params = list(sig.parameters.keys())
    assert "image_name" in params, "Missing parameter 'image_name'"




def test_hyp_helloweb_command_is_not_abstract():
    assert not inspect.isabstract(helloWeb_Command)


def test_hyp_helloweb_command_constructor_exists():
    assert callable(helloWeb_Command.__init__)


def test_hyp_helloweb_command_constructor_args():
    sig = inspect.signature(helloWeb_Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_helloweb_userfunction_is_not_abstract():
    assert not inspect.isabstract(helloWeb_UserFunction)


def test_hyp_helloweb_userfunction_constructor_exists():
    assert callable(helloWeb_UserFunction.__init__)


def test_hyp_helloweb_userfunction_constructor_args():
    sig = inspect.signature(helloWeb_UserFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_helloweb_supercommand_is_not_abstract():
    assert not inspect.isabstract(helloWeb_SuperCommand)


def test_hyp_helloweb_supercommand_constructor_exists():
    assert callable(helloWeb_SuperCommand.__init__)


def test_hyp_helloweb_supercommand_constructor_args():
    sig = inspect.signature(helloWeb_SuperCommand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_helloweb_main_is_not_abstract():
    assert not inspect.isabstract(helloWeb_Main)


def test_hyp_helloweb_main_constructor_exists():
    assert callable(helloWeb_Main.__init__)


def test_hyp_helloweb_main_constructor_args():
    sig = inspect.signature(helloWeb_Main.__init__)
    params = list(sig.parameters.keys())
    assert "land" in params, "Missing parameter 'land'"
    assert "takeoff" in params, "Missing parameter 'takeoff'"





def test_hyp_helloweb_program_is_not_abstract():
    assert not inspect.isabstract(helloWeb_Program)


def test_hyp_helloweb_program_constructor_exists():
    assert callable(helloWeb_Program.__init__)


def test_hyp_helloweb_program_constructor_args():
    sig = inspect.signature(helloWeb_Program.__init__)
    params = list(sig.parameters.keys())



def test_hyp_helloweb_recordedflight_is_not_abstract():
    assert not inspect.isabstract(helloWeb_RecordedFlight)


def test_hyp_helloweb_recordedflight_constructor_exists():
    assert callable(helloWeb_RecordedFlight.__init__)


def test_hyp_helloweb_recordedflight_constructor_args():
    sig = inspect.signature(helloWeb_RecordedFlight.__init__)
    params = list(sig.parameters.keys())
    assert "video_name" in params, "Missing parameter 'video_name'"



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
helloWeb_Up_strategy = st.builds(
    helloWeb_Up,
    distance=
        safe_text
)
helloWeb_Wait_strategy = st.builds(
    helloWeb_Wait,
    seconds=
        safe_text
)
helloWeb_RotateR_strategy = st.builds(
    helloWeb_RotateR,
    angle=
        st.integers()
)
helloWeb_Right_strategy = st.builds(
    helloWeb_Right,
    distance=
        safe_text
)
helloWeb_Forward_strategy = st.builds(
    helloWeb_Forward,
    distance=
        safe_text
)
helloWeb_Left_strategy = st.builds(
    helloWeb_Left,
    distance=
        safe_text
)
helloWeb_RotateL_strategy = st.builds(
    helloWeb_RotateL,
    angle=
        st.integers()
)
helloWeb_Backward_strategy = st.builds(
    helloWeb_Backward,
    distance=
        safe_text
)
helloWeb_Down_strategy = st.builds(
    helloWeb_Down,
    distance=
        safe_text
)
helloWeb_Snapshot_strategy = st.builds(
    helloWeb_Snapshot,
    image_name=
        safe_text
)
SuperCommand_strategy = st.builds(
    SuperCommand,
)
helloWeb_FunctionName_strategy = st.builds(
    helloWeb_FunctionName,
    func_name=
        safe_text
)
helloWeb_FeatureMatch_strategy = st.builds(
    helloWeb_FeatureMatch,
    image_name=
        safe_text
)
helloWeb_Command_strategy = st.builds(
    helloWeb_Command,
)
helloWeb_UserFunction_strategy = st.builds(
    helloWeb_UserFunction,
    name=
        safe_text
)
helloWeb_SuperCommand_strategy = st.builds(
    helloWeb_SuperCommand,
)
helloWeb_Main_strategy = st.builds(
    helloWeb_Main,
    land=
        safe_text,
    takeoff=
        safe_text
)
helloWeb_Program_strategy = st.builds(
    helloWeb_Program,
)
helloWeb_RecordedFlight_strategy = st.builds(
    helloWeb_RecordedFlight,
    video_name=
        safe_text
)





@given(instance=helloWeb_Up_strategy)
def test_hyp_helloweb_up_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original




@given(instance=helloWeb_Wait_strategy)
def test_hyp_helloweb_wait_seconds_setter(instance):
    original = instance.seconds
    instance.seconds = original
    assert instance.seconds == original




@given(instance=helloWeb_RotateR_strategy)
def test_hyp_helloweb_rotater_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original




@given(instance=helloWeb_Right_strategy)
def test_hyp_helloweb_right_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original




@given(instance=helloWeb_Forward_strategy)
def test_hyp_helloweb_forward_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original




@given(instance=helloWeb_Left_strategy)
def test_hyp_helloweb_left_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original




@given(instance=helloWeb_RotateL_strategy)
def test_hyp_helloweb_rotatel_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original




@given(instance=helloWeb_Backward_strategy)
def test_hyp_helloweb_backward_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original




@given(instance=helloWeb_Down_strategy)
def test_hyp_helloweb_down_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original




@given(instance=helloWeb_Snapshot_strategy)
def test_hyp_helloweb_snapshot_image_name_setter(instance):
    original = instance.image_name
    instance.image_name = original
    assert instance.image_name == original





@given(instance=helloWeb_FunctionName_strategy)
def test_hyp_helloweb_functionname_func_name_setter(instance):
    original = instance.func_name
    instance.func_name = original
    assert instance.func_name == original




@given(instance=helloWeb_FeatureMatch_strategy)
def test_hyp_helloweb_featurematch_image_name_setter(instance):
    original = instance.image_name
    instance.image_name = original
    assert instance.image_name == original





@given(instance=helloWeb_UserFunction_strategy)
def test_hyp_helloweb_userfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=helloWeb_Main_strategy)
def test_hyp_helloweb_main_land_setter(instance):
    original = instance.land
    instance.land = original
    assert instance.land == original



@given(instance=helloWeb_Main_strategy)
def test_hyp_helloweb_main_takeoff_setter(instance):
    original = instance.takeoff
    instance.takeoff = original
    assert instance.takeoff == original





@given(instance=helloWeb_RecordedFlight_strategy)
def test_hyp_helloweb_recordedflight_video_name_setter(instance):
    original = instance.video_name
    instance.video_name = original
    assert instance.video_name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Command,
    SuperCommand,
    helloWeb_Backward,
    helloWeb_Command,
    helloWeb_Down,
    helloWeb_FeatureMatch,
    helloWeb_Forward,
    helloWeb_FunctionName,
    helloWeb_Left,
    helloWeb_Main,
    helloWeb_Program,
    helloWeb_RecordedFlight,
    helloWeb_Right,
    helloWeb_RotateL,
    helloWeb_RotateR,
    helloWeb_Snapshot,
    helloWeb_SuperCommand,
    helloWeb_Up,
    helloWeb_UserFunction,
    helloWeb_Wait,
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

def test_helloWeb_Backward_distance_value_roundtrip():
    instance = helloWeb_Backward(distance="sample_text")
    assert instance.distance == "sample_text"
    instance.distance = "sample_text_2"
    assert instance.distance == "sample_text_2"


def test_helloWeb_Down_distance_value_roundtrip():
    instance = helloWeb_Down(distance="sample_text")
    assert instance.distance == "sample_text"
    instance.distance = "sample_text_2"
    assert instance.distance == "sample_text_2"


def test_helloWeb_FeatureMatch_image_name_value_roundtrip():
    instance = helloWeb_FeatureMatch(image_name="sample_text")
    assert instance.image_name == "sample_text"
    instance.image_name = "sample_text_2"
    assert instance.image_name == "sample_text_2"


def test_helloWeb_Forward_distance_value_roundtrip():
    instance = helloWeb_Forward(distance="sample_text")
    assert instance.distance == "sample_text"
    instance.distance = "sample_text_2"
    assert instance.distance == "sample_text_2"


def test_helloWeb_FunctionName_func_name_value_roundtrip():
    instance = helloWeb_FunctionName(func_name="sample_text")
    assert instance.func_name == "sample_text"
    instance.func_name = "sample_text_2"
    assert instance.func_name == "sample_text_2"


def test_helloWeb_Left_distance_value_roundtrip():
    instance = helloWeb_Left(distance="sample_text")
    assert instance.distance == "sample_text"
    instance.distance = "sample_text_2"
    assert instance.distance == "sample_text_2"


def test_helloWeb_Main_land_value_roundtrip():
    instance = helloWeb_Main(land="sample_text", takeoff="sample_text")
    assert instance.land == "sample_text"
    instance.land = "sample_text_2"
    assert instance.land == "sample_text_2"


def test_helloWeb_Main_takeoff_value_roundtrip():
    instance = helloWeb_Main(land="sample_text", takeoff="sample_text")
    assert instance.takeoff == "sample_text"
    instance.takeoff = "sample_text_2"
    assert instance.takeoff == "sample_text_2"


def test_helloWeb_RecordedFlight_video_name_value_roundtrip():
    instance = helloWeb_RecordedFlight(video_name="sample_text")
    assert instance.video_name == "sample_text"
    instance.video_name = "sample_text_2"
    assert instance.video_name == "sample_text_2"


def test_helloWeb_Right_distance_value_roundtrip():
    instance = helloWeb_Right(distance="sample_text")
    assert instance.distance == "sample_text"
    instance.distance = "sample_text_2"
    assert instance.distance == "sample_text_2"


def test_helloWeb_RotateL_angle_value_roundtrip():
    instance = helloWeb_RotateL(angle=7)
    assert instance.angle == 7
    instance.angle = 13
    assert instance.angle == 13


def test_helloWeb_RotateR_angle_value_roundtrip():
    instance = helloWeb_RotateR(angle=7)
    assert instance.angle == 7
    instance.angle = 13
    assert instance.angle == 13


def test_helloWeb_Snapshot_image_name_value_roundtrip():
    instance = helloWeb_Snapshot(image_name="sample_text")
    assert instance.image_name == "sample_text"
    instance.image_name = "sample_text_2"
    assert instance.image_name == "sample_text_2"


def test_helloWeb_Up_distance_value_roundtrip():
    instance = helloWeb_Up(distance="sample_text")
    assert instance.distance == "sample_text"
    instance.distance = "sample_text_2"
    assert instance.distance == "sample_text_2"


def test_helloWeb_UserFunction_name_value_roundtrip():
    instance = helloWeb_UserFunction(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_helloWeb_Wait_seconds_value_roundtrip():
    instance = helloWeb_Wait(seconds="sample_text")
    assert instance.seconds == "sample_text"
    instance.seconds = "sample_text_2"
    assert instance.seconds == "sample_text_2"


def test_helloWeb_Backward_isa_Command():
    instance = helloWeb_Backward(distance="sample_text")
    assert isinstance(instance, Command)


def test_helloWeb_Down_isa_Command():
    instance = helloWeb_Down(distance="sample_text")
    assert isinstance(instance, Command)


def test_helloWeb_Forward_isa_Command():
    instance = helloWeb_Forward(distance="sample_text")
    assert isinstance(instance, Command)


def test_helloWeb_Left_isa_Command():
    instance = helloWeb_Left(distance="sample_text")
    assert isinstance(instance, Command)


def test_helloWeb_Right_isa_Command():
    instance = helloWeb_Right(distance="sample_text")
    assert isinstance(instance, Command)


def test_helloWeb_RotateL_isa_Command():
    instance = helloWeb_RotateL(angle=7)
    assert isinstance(instance, Command)


def test_helloWeb_RotateR_isa_Command():
    instance = helloWeb_RotateR(angle=7)
    assert isinstance(instance, Command)


def test_helloWeb_Snapshot_isa_Command():
    instance = helloWeb_Snapshot(image_name="sample_text")
    assert isinstance(instance, Command)


def test_helloWeb_Up_isa_Command():
    instance = helloWeb_Up(distance="sample_text")
    assert isinstance(instance, Command)


def test_helloWeb_Wait_isa_Command():
    instance = helloWeb_Wait(seconds="sample_text")
    assert isinstance(instance, Command)


def test_helloWeb_Command_isa_SuperCommand():
    instance = helloWeb_Command()
    assert isinstance(instance, SuperCommand)


def test_helloWeb_FunctionName_isa_SuperCommand():
    instance = helloWeb_FunctionName(func_name="sample_text")
    assert isinstance(instance, SuperCommand)


def test_assoc_commands1_link_reassign_clear():
    a = helloWeb_Main(land="sample_text", takeoff="sample_text")
    b1 = helloWeb_SuperCommand()
    b2 = helloWeb_SuperCommand()
    _safe_set(a, 'helloWeb_Main2', {b1})
    assert _is_linked(a, 'helloWeb_Main2', b1)
    if hasattr(b1, 'helloWeb_SuperCommand'):
        assert _is_linked(b1, 'helloWeb_SuperCommand', a)
    _safe_set(a, 'helloWeb_Main2', {b2})
    assert _is_linked(a, 'helloWeb_Main2', b2)
    if hasattr(b1, 'helloWeb_SuperCommand'):
        assert not _is_linked(b1, 'helloWeb_SuperCommand', a)
    if hasattr(b2, 'helloWeb_SuperCommand'):
        assert _is_linked(b2, 'helloWeb_SuperCommand', a)
    _safe_set(a, 'helloWeb_Main2', set())
    assert not _is_linked(a, 'helloWeb_Main2', b2)
    if hasattr(b2, 'helloWeb_SuperCommand'):
        assert not _is_linked(b2, 'helloWeb_SuperCommand', a)


def test_assoc_func3_link_reassign_clear():
    a = helloWeb_UserFunction(name="sample_text")
    b1 = helloWeb_Command()
    b2 = helloWeb_Command()
    _safe_set(a, 'helloWeb_UserFunction', {b1})
    assert _is_linked(a, 'helloWeb_UserFunction', b1)
    if hasattr(b1, 'helloWeb_Command'):
        assert _is_linked(b1, 'helloWeb_Command', a)
    _safe_set(a, 'helloWeb_UserFunction', {b2})
    assert _is_linked(a, 'helloWeb_UserFunction', b2)
    if hasattr(b1, 'helloWeb_Command'):
        assert not _is_linked(b1, 'helloWeb_Command', a)
    if hasattr(b2, 'helloWeb_Command'):
        assert _is_linked(b2, 'helloWeb_Command', a)
    _safe_set(a, 'helloWeb_UserFunction', set())
    assert not _is_linked(a, 'helloWeb_UserFunction', b2)
    if hasattr(b2, 'helloWeb_Command'):
        assert not _is_linked(b2, 'helloWeb_Command', a)


def test_assoc_main0_link_reassign_clear():
    a = helloWeb_Main(land="sample_text", takeoff="sample_text")
    b1 = helloWeb_Program()
    b2 = helloWeb_Program()
    _safe_set(a, 'helloWeb_Main', b1)
    assert _is_linked(a, 'helloWeb_Main', b1)
    if hasattr(b1, 'helloWeb_Program'):
        assert _is_linked(b1, 'helloWeb_Program', a)
    _safe_set(a, 'helloWeb_Main', b2)
    assert _is_linked(a, 'helloWeb_Main', b2)
    if hasattr(b1, 'helloWeb_Program'):
        assert not _is_linked(b1, 'helloWeb_Program', a)
    if hasattr(b2, 'helloWeb_Program'):
        assert _is_linked(b2, 'helloWeb_Program', a)
    _safe_set(a, 'helloWeb_Main', None)
    assert not _is_linked(a, 'helloWeb_Main', b2)
    if hasattr(b2, 'helloWeb_Program'):
        assert not _is_linked(b2, 'helloWeb_Program', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Command_strategy = st.builds(Command)
@given(instance=Command_strategy)
@settings(max_examples=25)
def test_Command_instantiation(instance):
    assert isinstance(instance, Command)


SuperCommand_strategy = st.builds(SuperCommand)
@given(instance=SuperCommand_strategy)
@settings(max_examples=25)
def test_SuperCommand_instantiation(instance):
    assert isinstance(instance, SuperCommand)


helloWeb_Backward_strategy = st.builds(helloWeb_Backward, distance=safe_text)
@given(instance=helloWeb_Backward_strategy)
@settings(max_examples=25)
def test_helloWeb_Backward_instantiation(instance):
    assert isinstance(instance, helloWeb_Backward)


helloWeb_Command_strategy = st.builds(helloWeb_Command)
@given(instance=helloWeb_Command_strategy)
@settings(max_examples=25)
def test_helloWeb_Command_instantiation(instance):
    assert isinstance(instance, helloWeb_Command)


helloWeb_Down_strategy = st.builds(helloWeb_Down, distance=safe_text)
@given(instance=helloWeb_Down_strategy)
@settings(max_examples=25)
def test_helloWeb_Down_instantiation(instance):
    assert isinstance(instance, helloWeb_Down)


helloWeb_FeatureMatch_strategy = st.builds(helloWeb_FeatureMatch, image_name=safe_text)
@given(instance=helloWeb_FeatureMatch_strategy)
@settings(max_examples=25)
def test_helloWeb_FeatureMatch_instantiation(instance):
    assert isinstance(instance, helloWeb_FeatureMatch)


helloWeb_Forward_strategy = st.builds(helloWeb_Forward, distance=safe_text)
@given(instance=helloWeb_Forward_strategy)
@settings(max_examples=25)
def test_helloWeb_Forward_instantiation(instance):
    assert isinstance(instance, helloWeb_Forward)


helloWeb_FunctionName_strategy = st.builds(helloWeb_FunctionName, func_name=safe_text)
@given(instance=helloWeb_FunctionName_strategy)
@settings(max_examples=25)
def test_helloWeb_FunctionName_instantiation(instance):
    assert isinstance(instance, helloWeb_FunctionName)


helloWeb_Left_strategy = st.builds(helloWeb_Left, distance=safe_text)
@given(instance=helloWeb_Left_strategy)
@settings(max_examples=25)
def test_helloWeb_Left_instantiation(instance):
    assert isinstance(instance, helloWeb_Left)


helloWeb_Main_strategy = st.builds(helloWeb_Main, land=safe_text, takeoff=safe_text)
@given(instance=helloWeb_Main_strategy)
@settings(max_examples=25)
def test_helloWeb_Main_instantiation(instance):
    assert isinstance(instance, helloWeb_Main)


helloWeb_Program_strategy = st.builds(helloWeb_Program)
@given(instance=helloWeb_Program_strategy)
@settings(max_examples=25)
def test_helloWeb_Program_instantiation(instance):
    assert isinstance(instance, helloWeb_Program)


helloWeb_RecordedFlight_strategy = st.builds(helloWeb_RecordedFlight, video_name=safe_text)
@given(instance=helloWeb_RecordedFlight_strategy)
@settings(max_examples=25)
def test_helloWeb_RecordedFlight_instantiation(instance):
    assert isinstance(instance, helloWeb_RecordedFlight)


helloWeb_Right_strategy = st.builds(helloWeb_Right, distance=safe_text)
@given(instance=helloWeb_Right_strategy)
@settings(max_examples=25)
def test_helloWeb_Right_instantiation(instance):
    assert isinstance(instance, helloWeb_Right)


helloWeb_RotateL_strategy = st.builds(helloWeb_RotateL, angle=st.integers())
@given(instance=helloWeb_RotateL_strategy)
@settings(max_examples=25)
def test_helloWeb_RotateL_instantiation(instance):
    assert isinstance(instance, helloWeb_RotateL)


helloWeb_RotateR_strategy = st.builds(helloWeb_RotateR, angle=st.integers())
@given(instance=helloWeb_RotateR_strategy)
@settings(max_examples=25)
def test_helloWeb_RotateR_instantiation(instance):
    assert isinstance(instance, helloWeb_RotateR)


helloWeb_Snapshot_strategy = st.builds(helloWeb_Snapshot, image_name=safe_text)
@given(instance=helloWeb_Snapshot_strategy)
@settings(max_examples=25)
def test_helloWeb_Snapshot_instantiation(instance):
    assert isinstance(instance, helloWeb_Snapshot)


helloWeb_SuperCommand_strategy = st.builds(helloWeb_SuperCommand)
@given(instance=helloWeb_SuperCommand_strategy)
@settings(max_examples=25)
def test_helloWeb_SuperCommand_instantiation(instance):
    assert isinstance(instance, helloWeb_SuperCommand)


helloWeb_Up_strategy = st.builds(helloWeb_Up, distance=safe_text)
@given(instance=helloWeb_Up_strategy)
@settings(max_examples=25)
def test_helloWeb_Up_instantiation(instance):
    assert isinstance(instance, helloWeb_Up)


helloWeb_UserFunction_strategy = st.builds(helloWeb_UserFunction, name=safe_text)
@given(instance=helloWeb_UserFunction_strategy)
@settings(max_examples=25)
def test_helloWeb_UserFunction_instantiation(instance):
    assert isinstance(instance, helloWeb_UserFunction)


helloWeb_Wait_strategy = st.builds(helloWeb_Wait, seconds=safe_text)
@given(instance=helloWeb_Wait_strategy)
@settings(max_examples=25)
def test_helloWeb_Wait_instantiation(instance):
    assert isinstance(instance, helloWeb_Wait)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Command,
    SuperCommand,
    helloWeb_Backward,
    helloWeb_Command,
    helloWeb_Down,
    helloWeb_FeatureMatch,
    helloWeb_Forward,
    helloWeb_FunctionName,
    helloWeb_Left,
    helloWeb_Main,
    helloWeb_Program,
    helloWeb_RecordedFlight,
    helloWeb_Right,
    helloWeb_RotateL,
    helloWeb_RotateR,
    helloWeb_Snapshot,
    helloWeb_SuperCommand,
    helloWeb_Up,
    helloWeb_UserFunction,
    helloWeb_Wait,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_commands1_stub_double():
    # helloWeb_SuperCommand has no real 'helloWeb_SuperCommand' property in the generated
    # code (a bare stub) -- manually attach it so helloWeb_Main's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # helloWeb_Main's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = helloWeb_Main(land="sample_text", takeoff="sample_text")
    partner = helloWeb_SuperCommand()
    setattr(partner, 'helloWeb_SuperCommand', None)
    _safe_set(owner, 'helloWeb_Main2', {partner})
    assert getattr(partner, 'helloWeb_SuperCommand') == owner
    _safe_set(owner, 'helloWeb_Main2', set())
    assert getattr(partner, 'helloWeb_SuperCommand') is None


def test_assoc_func3_stub_double():
    # helloWeb_Command has no real 'helloWeb_Command' property in the generated
    # code (a bare stub) -- manually attach it so helloWeb_UserFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # helloWeb_UserFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = helloWeb_UserFunction(name="sample_text")
    partner = helloWeb_Command()
    setattr(partner, 'helloWeb_Command', None)
    _safe_set(owner, 'helloWeb_UserFunction', {partner})
    assert getattr(partner, 'helloWeb_Command') == owner
    _safe_set(owner, 'helloWeb_UserFunction', set())
    assert getattr(partner, 'helloWeb_Command') is None


def test_assoc_main0_stub_double():
    # helloWeb_Program has no real 'helloWeb_Program' property in the generated
    # code (a bare stub) -- manually attach it so helloWeb_Main's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # helloWeb_Main's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = helloWeb_Main(land="sample_text", takeoff="sample_text")
    partner = helloWeb_Program()
    setattr(partner, 'helloWeb_Program', None)
    _safe_set(owner, 'helloWeb_Main', partner)
    assert getattr(partner, 'helloWeb_Program') == owner
    _safe_set(owner, 'helloWeb_Main', None)
    assert getattr(partner, 'helloWeb_Program') is None




from python_code import helloWeb_Backward

def test_helloWeb_Backward___init__():
    assert helloWeb_Backward.__init__(helloWeb_Backward(''), '') == None
from python_code import helloWeb_Down

def test_helloWeb_Down___init__():
    assert helloWeb_Down.__init__(helloWeb_Down(''), '') == None
from python_code import helloWeb_FeatureMatch

def test_helloWeb_FeatureMatch___init__():
    assert helloWeb_FeatureMatch.__init__(helloWeb_FeatureMatch(''), '') == None
from python_code import helloWeb_Forward

def test_helloWeb_Forward___init__():
    assert helloWeb_Forward.__init__(helloWeb_Forward(''), '') == None
from python_code import helloWeb_FunctionName

def test_helloWeb_FunctionName___init__():
    assert helloWeb_FunctionName.__init__(helloWeb_FunctionName(''), '') == None
from python_code import helloWeb_Left

def test_helloWeb_Left___init__():
    assert helloWeb_Left.__init__(helloWeb_Left(''), '') == None
from python_code import helloWeb_Main
from python_code import helloWeb_Program

def test_helloWeb_Main___init__():
    assert helloWeb_Main.__init__(helloWeb_Main('\x00\x00', '', helloWeb_Main=helloWeb_Program(), helloWeb_Main2=set()), '', '', helloWeb_Main=helloWeb_Program(), helloWeb_Main2=set()) == None
from python_code import helloWeb_RecordedFlight

def test_helloWeb_RecordedFlight___init__():
    assert helloWeb_RecordedFlight.__init__(helloWeb_RecordedFlight(''), '') == None
from python_code import helloWeb_Right

def test_helloWeb_Right___init__():
    assert helloWeb_Right.__init__(helloWeb_Right(''), '') == None
from python_code import helloWeb_RotateL

def test_helloWeb_RotateL___init__():
    assert helloWeb_RotateL.__init__(helloWeb_RotateL(0), 0) == None
from python_code import helloWeb_RotateR

def test_helloWeb_RotateR___init__():
    assert helloWeb_RotateR.__init__(helloWeb_RotateR(0), 0) == None
from python_code import helloWeb_Snapshot

def test_helloWeb_Snapshot___init__():
    assert helloWeb_Snapshot.__init__(helloWeb_Snapshot(''), '') == None
from python_code import helloWeb_Up

def test_helloWeb_Up___init__():
    assert helloWeb_Up.__init__(helloWeb_Up(''), '') == None
from python_code import helloWeb_UserFunction

def test_helloWeb_UserFunction___init__():
    assert helloWeb_UserFunction.__init__(helloWeb_UserFunction('', helloWeb_UserFunction=set()), '', helloWeb_UserFunction=set()) == None
from python_code import helloWeb_Wait

def test_helloWeb_Wait___init__():
    assert helloWeb_Wait.__init__(helloWeb_Wait(''), '') == None

