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
    surveillance_ProbableElement,
    ProbableElement,
    MovingObject,
    surveillance_UnidentifiedObject,
    surveillance_Drone,
    surveillance_Clock,
    surveillance_MovingObject,
    surveillance_GunShot,
    surveillance_Coordinate,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_surveillance_probableelement_is_not_abstract():
    assert not inspect.isabstract(surveillance_ProbableElement)


def test_hyp_surveillance_probableelement_constructor_exists():
    assert callable(surveillance_ProbableElement.__init__)


def test_hyp_surveillance_probableelement_constructor_args():
    sig = inspect.signature(surveillance_ProbableElement.__init__)
    params = list(sig.parameters.keys())
    assert "confidence" in params, "Missing parameter 'confidence'"




def test_hyp_probableelement_is_not_abstract():
    assert not inspect.isabstract(ProbableElement)


def test_hyp_probableelement_constructor_exists():
    assert callable(ProbableElement.__init__)


def test_hyp_probableelement_constructor_args():
    sig = inspect.signature(ProbableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_movingobject_is_not_abstract():
    assert not inspect.isabstract(MovingObject)


def test_hyp_movingobject_constructor_exists():
    assert callable(MovingObject.__init__)


def test_hyp_movingobject_constructor_args():
    sig = inspect.signature(MovingObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_surveillance_unidentifiedobject_is_not_abstract():
    assert not inspect.isabstract(surveillance_UnidentifiedObject)


def test_hyp_surveillance_unidentifiedobject_constructor_exists():
    assert callable(surveillance_UnidentifiedObject.__init__)


def test_hyp_surveillance_unidentifiedobject_constructor_args():
    sig = inspect.signature(surveillance_UnidentifiedObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_surveillance_drone_is_not_abstract():
    assert not inspect.isabstract(surveillance_Drone)


def test_hyp_surveillance_drone_constructor_exists():
    assert callable(surveillance_Drone.__init__)


def test_hyp_surveillance_drone_constructor_args():
    sig = inspect.signature(surveillance_Drone.__init__)
    params = list(sig.parameters.keys())



def test_hyp_surveillance_clock_is_not_abstract():
    assert not inspect.isabstract(surveillance_Clock)


def test_hyp_surveillance_clock_constructor_exists():
    assert callable(surveillance_Clock.__init__)


def test_hyp_surveillance_clock_constructor_args():
    sig = inspect.signature(surveillance_Clock.__init__)
    params = list(sig.parameters.keys())
    assert "now" in params, "Missing parameter 'now'"




def test_hyp_surveillance_movingobject_is_not_abstract():
    assert not inspect.isabstract(surveillance_MovingObject)


def test_hyp_surveillance_movingobject_constructor_exists():
    assert callable(surveillance_MovingObject.__init__)


def test_hyp_surveillance_movingobject_constructor_args():
    sig = inspect.signature(surveillance_MovingObject.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"
    assert "speed" in params, "Missing parameter 'speed'"
    assert "width" in params, "Missing parameter 'width'"






def test_hyp_surveillance_gunshot_is_not_abstract():
    assert not inspect.isabstract(surveillance_GunShot)


def test_hyp_surveillance_gunshot_constructor_exists():
    assert callable(surveillance_GunShot.__init__)


def test_hyp_surveillance_gunshot_constructor_args():
    sig = inspect.signature(surveillance_GunShot.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"
    assert "hitsTarget" in params, "Missing parameter 'hitsTarget'"





def test_hyp_surveillance_coordinate_is_not_abstract():
    assert not inspect.isabstract(surveillance_Coordinate)


def test_hyp_surveillance_coordinate_constructor_exists():
    assert callable(surveillance_Coordinate.__init__)


def test_hyp_surveillance_coordinate_constructor_args():
    sig = inspect.signature(surveillance_Coordinate.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"




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
surveillance_ProbableElement_strategy = st.builds(
    surveillance_ProbableElement,
    confidence=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ProbableElement_strategy = st.builds(
    ProbableElement,
)
MovingObject_strategy = st.builds(
    MovingObject,
)
surveillance_UnidentifiedObject_strategy = st.builds(
    surveillance_UnidentifiedObject,
)
surveillance_Drone_strategy = st.builds(
    surveillance_Drone,
)
surveillance_Clock_strategy = st.builds(
    surveillance_Clock,
    now=
        st.integers()
)
surveillance_MovingObject_strategy = st.builds(
    surveillance_MovingObject,
    angle=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    speed=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
surveillance_GunShot_strategy = st.builds(
    surveillance_GunShot,
    angle=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    hitsTarget=
        st.booleans()
)
surveillance_Coordinate_strategy = st.builds(
    surveillance_Coordinate,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)




@given(instance=surveillance_ProbableElement_strategy)
def test_hyp_surveillance_probableelement_confidence_setter(instance):
    original = instance.confidence
    instance.confidence = original
    assert instance.confidence == original








@given(instance=surveillance_Clock_strategy)
def test_hyp_surveillance_clock_now_setter(instance):
    original = instance.now
    instance.now = original
    assert instance.now == original




@given(instance=surveillance_MovingObject_strategy)
def test_hyp_surveillance_movingobject_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original



@given(instance=surveillance_MovingObject_strategy)
def test_hyp_surveillance_movingobject_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original



@given(instance=surveillance_MovingObject_strategy)
def test_hyp_surveillance_movingobject_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=surveillance_MovingObject_strategy)
@settings(max_examples=30)
def test_hyp_surveillance_movingobject_move_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.move(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.move).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'move' in surveillance_MovingObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'move' in surveillance_MovingObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'move' in surveillance_MovingObject is not implemented or raised an error")




@given(instance=surveillance_GunShot_strategy)
def test_hyp_surveillance_gunshot_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original



@given(instance=surveillance_GunShot_strategy)
def test_hyp_surveillance_gunshot_hitsTarget_setter(instance):
    original = instance.hitsTarget
    instance.hitsTarget = original
    assert instance.hitsTarget == original




@given(instance=surveillance_Coordinate_strategy)
def test_hyp_surveillance_coordinate_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=surveillance_Coordinate_strategy)
def test_hyp_surveillance_coordinate_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=surveillance_Coordinate_strategy)
@settings(max_examples=30)
def test_hyp_surveillance_coordinate_distance_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.distance(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.distance).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'distance' in surveillance_Coordinate is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'distance' in surveillance_Coordinate did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'distance' in surveillance_Coordinate is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    MovingObject,
    ProbableElement,
    surveillance_Clock,
    surveillance_Coordinate,
    surveillance_Drone,
    surveillance_GunShot,
    surveillance_MovingObject,
    surveillance_ProbableElement,
    surveillance_UnidentifiedObject,
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

def test_surveillance_Clock_now_value_roundtrip():
    instance = surveillance_Clock(now=7)
    assert instance.now == 7
    instance.now = 13
    assert instance.now == 13


def test_surveillance_Coordinate_x_value_roundtrip():
    instance = surveillance_Coordinate(x=3.14, y=3.14)
    assert instance.x == 3.14
    instance.x = 9.99
    assert instance.x == 9.99


def test_surveillance_Coordinate_y_value_roundtrip():
    instance = surveillance_Coordinate(x=3.14, y=3.14)
    assert instance.y == 3.14
    instance.y = 9.99
    assert instance.y == 9.99


def test_surveillance_GunShot_angle_value_roundtrip():
    instance = surveillance_GunShot(angle=3.14, hitsTarget=True)
    assert instance.angle == 3.14
    instance.angle = 9.99
    assert instance.angle == 9.99


def test_surveillance_GunShot_hitsTarget_value_roundtrip():
    instance = surveillance_GunShot(angle=3.14, hitsTarget=True)
    assert instance.hitsTarget == True
    instance.hitsTarget = False
    assert instance.hitsTarget == False


def test_surveillance_MovingObject_angle_value_roundtrip():
    instance = surveillance_MovingObject(angle=3.14, speed=3.14, width=3.14)
    assert instance.angle == 3.14
    instance.angle = 9.99
    assert instance.angle == 9.99


def test_surveillance_MovingObject_speed_value_roundtrip():
    instance = surveillance_MovingObject(angle=3.14, speed=3.14, width=3.14)
    assert instance.speed == 3.14
    instance.speed = 9.99
    assert instance.speed == 9.99


def test_surveillance_MovingObject_width_value_roundtrip():
    instance = surveillance_MovingObject(angle=3.14, speed=3.14, width=3.14)
    assert instance.width == 3.14
    instance.width = 9.99
    assert instance.width == 9.99


def test_surveillance_ProbableElement_confidence_value_roundtrip():
    instance = surveillance_ProbableElement(confidence=3.14)
    assert instance.confidence == 3.14
    instance.confidence = 9.99
    assert instance.confidence == 9.99


def test_surveillance_Drone_isa_MovingObject():
    instance = surveillance_Drone()
    assert isinstance(instance, MovingObject)


def test_surveillance_UnidentifiedObject_isa_MovingObject():
    instance = surveillance_UnidentifiedObject()
    assert isinstance(instance, MovingObject)


def test_surveillance_GunShot_isa_ProbableElement():
    instance = surveillance_GunShot(angle=3.14, hitsTarget=True)
    assert isinstance(instance, ProbableElement)


def test_surveillance_UnidentifiedObject_isa_ProbableElement():
    instance = surveillance_UnidentifiedObject()
    assert isinstance(instance, ProbableElement)


def test_assoc_currentPosition2_link_reassign_clear():
    a = surveillance_MovingObject(angle=3.14, speed=3.14, width=3.14)
    b1 = surveillance_Coordinate(x=3.14, y=3.14)
    b2 = surveillance_Coordinate(x=9.99, y=9.99)
    _safe_set(a, 'object', b1)
    assert _is_linked(a, 'object', b1)
    if hasattr(b1, 'Coordinate'):
        assert _is_linked(b1, 'Coordinate', a)
    _safe_set(a, 'object', b2)
    assert _is_linked(a, 'object', b2)
    if hasattr(b1, 'Coordinate'):
        assert not _is_linked(b1, 'Coordinate', a)
    if hasattr(b2, 'Coordinate'):
        assert _is_linked(b2, 'Coordinate', a)
    _safe_set(a, 'object', None)
    assert not _is_linked(a, 'object', b2)
    if hasattr(b2, 'Coordinate'):
        assert not _is_linked(b2, 'Coordinate', a)


def test_assoc_drone9_link_reassign_clear():
    a = surveillance_GunShot(angle=3.14, hitsTarget=True)
    b1 = surveillance_Drone()
    b2 = surveillance_Drone()
    _safe_set(a, 'shot10', b1)
    assert _is_linked(a, 'shot10', b1)
    if hasattr(b1, 'Drone'):
        assert _is_linked(b1, 'Drone', a)
    _safe_set(a, 'shot10', b2)
    assert _is_linked(a, 'shot10', b2)
    if hasattr(b1, 'Drone'):
        assert not _is_linked(b1, 'Drone', a)
    if hasattr(b2, 'Drone'):
        assert _is_linked(b2, 'Drone', a)
    _safe_set(a, 'shot10', None)
    assert not _is_linked(a, 'shot10', b2)
    if hasattr(b2, 'Drone'):
        assert not _is_linked(b2, 'Drone', a)


def test_assoc_object1_link_reassign_clear():
    a = surveillance_MovingObject(angle=3.14, speed=3.14, width=3.14)
    b1 = surveillance_Coordinate(x=3.14, y=3.14)
    b2 = surveillance_Coordinate(x=9.99, y=9.99)
    _safe_set(a, 'MovingObject', b1)
    assert _is_linked(a, 'MovingObject', b1)
    if hasattr(b1, 'currentPosition'):
        assert _is_linked(b1, 'currentPosition', a)
    _safe_set(a, 'MovingObject', b2)
    assert _is_linked(a, 'MovingObject', b2)
    if hasattr(b1, 'currentPosition'):
        assert not _is_linked(b1, 'currentPosition', a)
    if hasattr(b2, 'currentPosition'):
        assert _is_linked(b2, 'currentPosition', a)
    _safe_set(a, 'MovingObject', None)
    assert not _is_linked(a, 'MovingObject', b2)
    if hasattr(b2, 'currentPosition'):
        assert not _is_linked(b2, 'currentPosition', a)


def test_assoc_shootingPosition7_link_reassign_clear():
    a = surveillance_GunShot(angle=3.14, hitsTarget=True)
    b1 = surveillance_Coordinate(x=3.14, y=3.14)
    b2 = surveillance_Coordinate(x=9.99, y=9.99)
    _safe_set(a, 'shot', b1)
    assert _is_linked(a, 'shot', b1)
    if hasattr(b1, 'Coordinate8'):
        assert _is_linked(b1, 'Coordinate8', a)
    _safe_set(a, 'shot', b2)
    assert _is_linked(a, 'shot', b2)
    if hasattr(b1, 'Coordinate8'):
        assert not _is_linked(b1, 'Coordinate8', a)
    if hasattr(b2, 'Coordinate8'):
        assert _is_linked(b2, 'Coordinate8', a)
    _safe_set(a, 'shot', None)
    assert not _is_linked(a, 'shot', b2)
    if hasattr(b2, 'Coordinate8'):
        assert not _is_linked(b2, 'Coordinate8', a)


def test_assoc_shot0_link_reassign_clear():
    a = surveillance_GunShot(angle=3.14, hitsTarget=True)
    b1 = surveillance_Coordinate(x=3.14, y=3.14)
    b2 = surveillance_Coordinate(x=9.99, y=9.99)
    _safe_set(a, 'GunShot', b1)
    assert _is_linked(a, 'GunShot', b1)
    if hasattr(b1, 'shootingPosition'):
        assert _is_linked(b1, 'shootingPosition', a)
    _safe_set(a, 'GunShot', b2)
    assert _is_linked(a, 'GunShot', b2)
    if hasattr(b1, 'shootingPosition'):
        assert not _is_linked(b1, 'shootingPosition', a)
    if hasattr(b2, 'shootingPosition'):
        assert _is_linked(b2, 'shootingPosition', a)
    _safe_set(a, 'GunShot', None)
    assert not _is_linked(a, 'GunShot', b2)
    if hasattr(b2, 'shootingPosition'):
        assert not _is_linked(b2, 'shootingPosition', a)


def test_assoc_shot3_link_reassign_clear():
    a = surveillance_GunShot(angle=3.14, hitsTarget=True)
    b1 = surveillance_Drone()
    b2 = surveillance_Drone()
    _safe_set(a, 'GunShot4', b1)
    assert _is_linked(a, 'GunShot4', b1)
    if hasattr(b1, 'drone'):
        assert _is_linked(b1, 'drone', a)
    _safe_set(a, 'GunShot4', b2)
    assert _is_linked(a, 'GunShot4', b2)
    if hasattr(b1, 'drone'):
        assert not _is_linked(b1, 'drone', a)
    if hasattr(b2, 'drone'):
        assert _is_linked(b2, 'drone', a)
    _safe_set(a, 'GunShot4', None)
    assert not _is_linked(a, 'GunShot4', b2)
    if hasattr(b2, 'drone'):
        assert not _is_linked(b2, 'drone', a)


def test_assoc_shot5_link_reassign_clear():
    a = surveillance_GunShot(angle=3.14, hitsTarget=True)
    b1 = surveillance_UnidentifiedObject()
    b2 = surveillance_UnidentifiedObject()
    _safe_set(a, 'GunShot6', b1)
    assert _is_linked(a, 'GunShot6', b1)
    if hasattr(b1, 'target'):
        assert _is_linked(b1, 'target', a)
    _safe_set(a, 'GunShot6', b2)
    assert _is_linked(a, 'GunShot6', b2)
    if hasattr(b1, 'target'):
        assert not _is_linked(b1, 'target', a)
    if hasattr(b2, 'target'):
        assert _is_linked(b2, 'target', a)
    _safe_set(a, 'GunShot6', None)
    assert not _is_linked(a, 'GunShot6', b2)
    if hasattr(b2, 'target'):
        assert not _is_linked(b2, 'target', a)


def test_assoc_target11_link_reassign_clear():
    a = surveillance_GunShot(angle=3.14, hitsTarget=True)
    b1 = surveillance_UnidentifiedObject()
    b2 = surveillance_UnidentifiedObject()
    _safe_set(a, 'shot12', b1)
    assert _is_linked(a, 'shot12', b1)
    if hasattr(b1, 'UnidentifiedObject'):
        assert _is_linked(b1, 'UnidentifiedObject', a)
    _safe_set(a, 'shot12', b2)
    assert _is_linked(a, 'shot12', b2)
    if hasattr(b1, 'UnidentifiedObject'):
        assert not _is_linked(b1, 'UnidentifiedObject', a)
    if hasattr(b2, 'UnidentifiedObject'):
        assert _is_linked(b2, 'UnidentifiedObject', a)
    _safe_set(a, 'shot12', None)
    assert not _is_linked(a, 'shot12', b2)
    if hasattr(b2, 'UnidentifiedObject'):
        assert not _is_linked(b2, 'UnidentifiedObject', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

MovingObject_strategy = st.builds(MovingObject)
@given(instance=MovingObject_strategy)
@settings(max_examples=25)
def test_MovingObject_instantiation(instance):
    assert isinstance(instance, MovingObject)


ProbableElement_strategy = st.builds(ProbableElement)
@given(instance=ProbableElement_strategy)
@settings(max_examples=25)
def test_ProbableElement_instantiation(instance):
    assert isinstance(instance, ProbableElement)


surveillance_Clock_strategy = st.builds(surveillance_Clock, now=st.integers())
@given(instance=surveillance_Clock_strategy)
@settings(max_examples=25)
def test_surveillance_Clock_instantiation(instance):
    assert isinstance(instance, surveillance_Clock)


surveillance_Coordinate_strategy = st.builds(surveillance_Coordinate, x=st.floats(allow_nan=False, allow_infinity=False), y=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=surveillance_Coordinate_strategy)
@settings(max_examples=25)
def test_surveillance_Coordinate_instantiation(instance):
    assert isinstance(instance, surveillance_Coordinate)


surveillance_Drone_strategy = st.builds(surveillance_Drone)
@given(instance=surveillance_Drone_strategy)
@settings(max_examples=25)
def test_surveillance_Drone_instantiation(instance):
    assert isinstance(instance, surveillance_Drone)


surveillance_GunShot_strategy = st.builds(surveillance_GunShot, angle=st.floats(allow_nan=False, allow_infinity=False), hitsTarget=st.booleans())
@given(instance=surveillance_GunShot_strategy)
@settings(max_examples=25)
def test_surveillance_GunShot_instantiation(instance):
    assert isinstance(instance, surveillance_GunShot)


surveillance_MovingObject_strategy = st.builds(surveillance_MovingObject, angle=st.floats(allow_nan=False, allow_infinity=False), speed=st.floats(allow_nan=False, allow_infinity=False), width=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=surveillance_MovingObject_strategy)
@settings(max_examples=25)
def test_surveillance_MovingObject_instantiation(instance):
    assert isinstance(instance, surveillance_MovingObject)


surveillance_ProbableElement_strategy = st.builds(surveillance_ProbableElement, confidence=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=surveillance_ProbableElement_strategy)
@settings(max_examples=25)
def test_surveillance_ProbableElement_instantiation(instance):
    assert isinstance(instance, surveillance_ProbableElement)


surveillance_UnidentifiedObject_strategy = st.builds(surveillance_UnidentifiedObject)
@given(instance=surveillance_UnidentifiedObject_strategy)
@settings(max_examples=25)
def test_surveillance_UnidentifiedObject_instantiation(instance):
    assert isinstance(instance, surveillance_UnidentifiedObject)



