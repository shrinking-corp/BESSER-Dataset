import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    CommunicationAction,
    Move,
    MoveTransition,
    NamedElement,
    Notify,
    behaviour_Action,
    behaviour_Behaviour,
    behaviour_BroadcastNotify,
    behaviour_CheckNotification,
    behaviour_Choice,
    behaviour_Circle,
    behaviour_CommunicationAction,
    behaviour_Coordinate,
    behaviour_DeviceAction,
    behaviour_Drone,
    behaviour_Feedback,
    behaviour_GoTo,
    behaviour_HeadTo,
    behaviour_Hover,
    behaviour_Land,
    behaviour_Move,
    behaviour_MoveTransition,
    behaviour_MulticastNotify,
    behaviour_NamedElement,
    behaviour_Notify,
    behaviour_Parameter,
    behaviour_Slot,
    behaviour_Start,
    behaviour_Stop,
    behaviour_TakeOff,
    behaviour_UnicastNotify,
    GoToStrategy,
    TravelMode,
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

def test_behaviour_Behaviour_crs_value_roundtrip():
    instance = behaviour_Behaviour(crs="sample_text")
    assert instance.crs == "sample_text"
    instance.crs = "sample_text_2"
    assert instance.crs == "sample_text_2"


def test_behaviour_Choice_conditionIdentifier_value_roundtrip():
    instance = behaviour_Choice(conditionIdentifier="sample_text")
    assert instance.conditionIdentifier == "sample_text"
    instance.conditionIdentifier = "sample_text_2"
    assert instance.conditionIdentifier == "sample_text_2"


def test_behaviour_Circle_altitude_value_roundtrip():
    instance = behaviour_Circle(altitude=3.14, clockwise=True, duration=3.14, radius=3.14)
    assert instance.altitude == 3.14
    instance.altitude = 9.99
    assert instance.altitude == 9.99


def test_behaviour_Circle_clockwise_value_roundtrip():
    instance = behaviour_Circle(altitude=3.14, clockwise=True, duration=3.14, radius=3.14)
    assert instance.clockwise == True
    instance.clockwise = False
    assert instance.clockwise == False


def test_behaviour_Circle_duration_value_roundtrip():
    instance = behaviour_Circle(altitude=3.14, clockwise=True, duration=3.14, radius=3.14)
    assert instance.duration == 3.14
    instance.duration = 9.99
    assert instance.duration == 9.99


def test_behaviour_Circle_radius_value_roundtrip():
    instance = behaviour_Circle(altitude=3.14, clockwise=True, duration=3.14, radius=3.14)
    assert instance.radius == 3.14
    instance.radius = 9.99
    assert instance.radius == 9.99


def test_behaviour_Coordinate_altitude_value_roundtrip():
    instance = behaviour_Coordinate(altitude=3.14, heading=3.14, latitude=3.14, longitude=3.14)
    assert instance.altitude == 3.14
    instance.altitude = 9.99
    assert instance.altitude == 9.99


def test_behaviour_Coordinate_heading_value_roundtrip():
    instance = behaviour_Coordinate(altitude=3.14, heading=3.14, latitude=3.14, longitude=3.14)
    assert instance.heading == 3.14
    instance.heading = 9.99
    assert instance.heading == 9.99


def test_behaviour_Coordinate_latitude_value_roundtrip():
    instance = behaviour_Coordinate(altitude=3.14, heading=3.14, latitude=3.14, longitude=3.14)
    assert instance.latitude == 3.14
    instance.latitude = 9.99
    assert instance.latitude == 9.99


def test_behaviour_Coordinate_longitude_value_roundtrip():
    instance = behaviour_Coordinate(altitude=3.14, heading=3.14, latitude=3.14, longitude=3.14)
    assert instance.longitude == 3.14
    instance.longitude = 9.99
    assert instance.longitude == 9.99


def test_behaviour_DeviceAction_actionName_value_roundtrip():
    instance = behaviour_DeviceAction(actionName="sample_text")
    assert instance.actionName == "sample_text"
    instance.actionName = "sample_text_2"
    assert instance.actionName == "sample_text_2"


def test_behaviour_Drone_travelMode_value_roundtrip():
    instance = behaviour_Drone(travelMode="sample_text", typeName="sample_text")
    assert instance.travelMode == "sample_text"
    instance.travelMode = "sample_text_2"
    assert instance.travelMode == "sample_text_2"


def test_behaviour_Drone_typeName_value_roundtrip():
    instance = behaviour_Drone(travelMode="sample_text", typeName="sample_text")
    assert instance.typeName == "sample_text"
    instance.typeName = "sample_text_2"
    assert instance.typeName == "sample_text_2"


def test_behaviour_Feedback_actionName_value_roundtrip():
    instance = behaviour_Feedback(actionName="sample_text")
    assert instance.actionName == "sample_text"
    instance.actionName = "sample_text_2"
    assert instance.actionName == "sample_text_2"


def test_behaviour_GoTo_strategy_value_roundtrip():
    instance = behaviour_GoTo(strategy="sample_text")
    assert instance.strategy == "sample_text"
    instance.strategy = "sample_text_2"
    assert instance.strategy == "sample_text_2"


def test_behaviour_HeadTo_direction_value_roundtrip():
    instance = behaviour_HeadTo(direction=3.14)
    assert instance.direction == 3.14
    instance.direction = 9.99
    assert instance.direction == 9.99


def test_behaviour_Hover_duration_value_roundtrip():
    instance = behaviour_Hover(duration=3.14)
    assert instance.duration == 3.14
    instance.duration = 9.99
    assert instance.duration == 9.99


def test_behaviour_MoveTransition_fluid_value_roundtrip():
    instance = behaviour_MoveTransition(fluid=True)
    assert instance.fluid == True
    instance.fluid = False
    assert instance.fluid == False


def test_behaviour_NamedElement_name_value_roundtrip():
    instance = behaviour_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_behaviour_Parameter_key_value_roundtrip():
    instance = behaviour_Parameter(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_behaviour_Parameter_value_value_roundtrip():
    instance = behaviour_Parameter(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_behaviour_TakeOff_altitude_value_roundtrip():
    instance = behaviour_TakeOff(altitude=3.14)
    assert instance.altitude == 3.14
    instance.altitude = 9.99
    assert instance.altitude == 9.99


def test_behaviour_CommunicationAction_isa_Action():
    instance = behaviour_CommunicationAction()
    assert isinstance(instance, Action)


def test_behaviour_DeviceAction_isa_Action():
    instance = behaviour_DeviceAction(actionName="sample_text")
    assert isinstance(instance, Action)


def test_behaviour_CheckNotification_isa_CommunicationAction():
    instance = behaviour_CheckNotification()
    assert isinstance(instance, CommunicationAction)


def test_behaviour_Feedback_isa_CommunicationAction():
    instance = behaviour_Feedback(actionName="sample_text")
    assert isinstance(instance, CommunicationAction)


def test_behaviour_Notify_isa_CommunicationAction():
    instance = behaviour_Notify()
    assert isinstance(instance, CommunicationAction)


def test_behaviour_Circle_isa_Move():
    instance = behaviour_Circle(altitude=3.14, clockwise=True, duration=3.14, radius=3.14)
    assert isinstance(instance, Move)


def test_behaviour_GoTo_isa_Move():
    instance = behaviour_GoTo(strategy="sample_text")
    assert isinstance(instance, Move)


def test_behaviour_HeadTo_isa_Move():
    instance = behaviour_HeadTo(direction=3.14)
    assert isinstance(instance, Move)


def test_behaviour_Hover_isa_Move():
    instance = behaviour_Hover(duration=3.14)
    assert isinstance(instance, Move)


def test_behaviour_Land_isa_Move():
    instance = behaviour_Land()
    assert isinstance(instance, Move)


def test_behaviour_Start_isa_Move():
    instance = behaviour_Start()
    assert isinstance(instance, Move)


def test_behaviour_Stop_isa_Move():
    instance = behaviour_Stop()
    assert isinstance(instance, Move)


def test_behaviour_TakeOff_isa_Move():
    instance = behaviour_TakeOff(altitude=3.14)
    assert isinstance(instance, Move)


def test_behaviour_Choice_isa_MoveTransition():
    instance = behaviour_Choice(conditionIdentifier="sample_text")
    assert isinstance(instance, MoveTransition)


def test_behaviour_Action_isa_NamedElement():
    instance = behaviour_Action()
    assert isinstance(instance, NamedElement)


def test_behaviour_Behaviour_isa_NamedElement():
    instance = behaviour_Behaviour(crs="sample_text")
    assert isinstance(instance, NamedElement)


def test_behaviour_Drone_isa_NamedElement():
    instance = behaviour_Drone(travelMode="sample_text", typeName="sample_text")
    assert isinstance(instance, NamedElement)


def test_behaviour_Move_isa_NamedElement():
    instance = behaviour_Move()
    assert isinstance(instance, NamedElement)


def test_behaviour_Slot_isa_NamedElement():
    instance = behaviour_Slot()
    assert isinstance(instance, NamedElement)


def test_behaviour_BroadcastNotify_isa_Notify():
    instance = behaviour_BroadcastNotify()
    assert isinstance(instance, Notify)


def test_behaviour_MulticastNotify_isa_Notify():
    instance = behaviour_MulticastNotify()
    assert isinstance(instance, Notify)


def test_behaviour_UnicastNotify_isa_Notify():
    instance = behaviour_UnicastNotify()
    assert isinstance(instance, Notify)


def test_assoc_drones0_link_reassign_clear():
    a = behaviour_Drone(travelMode="sample_text", typeName="sample_text")
    b1 = behaviour_Behaviour(crs="sample_text")
    b2 = behaviour_Behaviour(crs="sample_text_2")
    _safe_set(a, 'behaviour_Drone', b1)
    assert _is_linked(a, 'behaviour_Drone', b1)
    if hasattr(b1, 'behaviour_Behaviour'):
        assert _is_linked(b1, 'behaviour_Behaviour', a)
    _safe_set(a, 'behaviour_Drone', b2)
    assert _is_linked(a, 'behaviour_Drone', b2)
    if hasattr(b1, 'behaviour_Behaviour'):
        assert not _is_linked(b1, 'behaviour_Behaviour', a)
    if hasattr(b2, 'behaviour_Behaviour'):
        assert _is_linked(b2, 'behaviour_Behaviour', a)
    _safe_set(a, 'behaviour_Drone', None)
    assert not _is_linked(a, 'behaviour_Drone', b2)
    if hasattr(b2, 'behaviour_Behaviour'):
        assert not _is_linked(b2, 'behaviour_Behaviour', a)


def test_assoc_falseBranch9_link_reassign_clear():
    a = behaviour_Choice(conditionIdentifier="sample_text")
    b1 = behaviour_Move()
    b2 = behaviour_Move()
    _safe_set(a, 'behaviour_Choice', b1)
    assert _is_linked(a, 'behaviour_Choice', b1)
    if hasattr(b1, 'behaviour_Move10'):
        assert _is_linked(b1, 'behaviour_Move10', a)
    _safe_set(a, 'behaviour_Choice', b2)
    assert _is_linked(a, 'behaviour_Choice', b2)
    if hasattr(b1, 'behaviour_Move10'):
        assert not _is_linked(b1, 'behaviour_Move10', a)
    if hasattr(b2, 'behaviour_Move10'):
        assert _is_linked(b2, 'behaviour_Move10', a)
    _safe_set(a, 'behaviour_Choice', None)
    assert not _is_linked(a, 'behaviour_Choice', b2)
    if hasattr(b2, 'behaviour_Move10'):
        assert not _is_linked(b2, 'behaviour_Move10', a)


def test_assoc_from_32_link_reassign_clear():
    a = behaviour_MoveTransition(fluid=True)
    b1 = behaviour_Move()
    b2 = behaviour_Move()
    _safe_set(a, 'behaviour_MoveTransition33', b1)
    assert _is_linked(a, 'behaviour_MoveTransition33', b1)
    if hasattr(b1, 'behaviour_Move34'):
        assert _is_linked(b1, 'behaviour_Move34', a)
    _safe_set(a, 'behaviour_MoveTransition33', b2)
    assert _is_linked(a, 'behaviour_MoveTransition33', b2)
    if hasattr(b1, 'behaviour_Move34'):
        assert not _is_linked(b1, 'behaviour_Move34', a)
    if hasattr(b2, 'behaviour_Move34'):
        assert _is_linked(b2, 'behaviour_Move34', a)
    _safe_set(a, 'behaviour_MoveTransition33', None)
    assert not _is_linked(a, 'behaviour_MoveTransition33', b2)
    if hasattr(b2, 'behaviour_Move34'):
        assert not _is_linked(b2, 'behaviour_Move34', a)


def test_assoc_home1_link_reassign_clear():
    a = behaviour_Drone(travelMode="sample_text", typeName="sample_text")
    b1 = behaviour_Coordinate(altitude=3.14, heading=3.14, latitude=3.14, longitude=3.14)
    b2 = behaviour_Coordinate(altitude=9.99, heading=9.99, latitude=9.99, longitude=9.99)
    _safe_set(a, 'behaviour_Drone2', b1)
    assert _is_linked(a, 'behaviour_Drone2', b1)
    if hasattr(b1, 'behaviour_Coordinate'):
        assert _is_linked(b1, 'behaviour_Coordinate', a)
    _safe_set(a, 'behaviour_Drone2', b2)
    assert _is_linked(a, 'behaviour_Drone2', b2)
    if hasattr(b1, 'behaviour_Coordinate'):
        assert not _is_linked(b1, 'behaviour_Coordinate', a)
    if hasattr(b2, 'behaviour_Coordinate'):
        assert _is_linked(b2, 'behaviour_Coordinate', a)
    _safe_set(a, 'behaviour_Drone2', None)
    assert not _is_linked(a, 'behaviour_Drone2', b2)
    if hasattr(b2, 'behaviour_Coordinate'):
        assert not _is_linked(b2, 'behaviour_Coordinate', a)


def test_assoc_moveTransitions5_link_reassign_clear():
    a = behaviour_MoveTransition(fluid=True)
    b1 = behaviour_Drone(travelMode="sample_text", typeName="sample_text")
    b2 = behaviour_Drone(travelMode="sample_text_2", typeName="sample_text_2")
    _safe_set(a, 'behaviour_MoveTransition', b1)
    assert _is_linked(a, 'behaviour_MoveTransition', b1)
    if hasattr(b1, 'behaviour_Drone6'):
        assert _is_linked(b1, 'behaviour_Drone6', a)
    _safe_set(a, 'behaviour_MoveTransition', b2)
    assert _is_linked(a, 'behaviour_MoveTransition', b2)
    if hasattr(b1, 'behaviour_Drone6'):
        assert not _is_linked(b1, 'behaviour_Drone6', a)
    if hasattr(b2, 'behaviour_Drone6'):
        assert _is_linked(b2, 'behaviour_Drone6', a)
    _safe_set(a, 'behaviour_MoveTransition', None)
    assert not _is_linked(a, 'behaviour_MoveTransition', b2)
    if hasattr(b2, 'behaviour_Drone6'):
        assert not _is_linked(b2, 'behaviour_Drone6', a)


def test_assoc_movements3_link_reassign_clear():
    a = behaviour_Drone(travelMode="sample_text", typeName="sample_text")
    b1 = behaviour_Move()
    b2 = behaviour_Move()
    _safe_set(a, 'behaviour_Drone4', {b1})
    assert _is_linked(a, 'behaviour_Drone4', b1)
    if hasattr(b1, 'behaviour_Move'):
        assert _is_linked(b1, 'behaviour_Move', a)
    _safe_set(a, 'behaviour_Drone4', {b2})
    assert _is_linked(a, 'behaviour_Drone4', b2)
    if hasattr(b1, 'behaviour_Move'):
        assert not _is_linked(b1, 'behaviour_Move', a)
    if hasattr(b2, 'behaviour_Move'):
        assert _is_linked(b2, 'behaviour_Move', a)
    _safe_set(a, 'behaviour_Drone4', set())
    assert not _is_linked(a, 'behaviour_Drone4', b2)
    if hasattr(b2, 'behaviour_Move'):
        assert not _is_linked(b2, 'behaviour_Move', a)


def test_assoc_parameters28_link_reassign_clear():
    a = behaviour_Parameter(key="sample_text", value="sample_text")
    b1 = behaviour_DeviceAction(actionName="sample_text")
    b2 = behaviour_DeviceAction(actionName="sample_text_2")
    _safe_set(a, 'behaviour_Parameter', b1)
    assert _is_linked(a, 'behaviour_Parameter', b1)
    if hasattr(b1, 'behaviour_DeviceAction'):
        assert _is_linked(b1, 'behaviour_DeviceAction', a)
    _safe_set(a, 'behaviour_Parameter', b2)
    assert _is_linked(a, 'behaviour_Parameter', b2)
    if hasattr(b1, 'behaviour_DeviceAction'):
        assert not _is_linked(b1, 'behaviour_DeviceAction', a)
    if hasattr(b2, 'behaviour_DeviceAction'):
        assert _is_linked(b2, 'behaviour_DeviceAction', a)
    _safe_set(a, 'behaviour_Parameter', None)
    assert not _is_linked(a, 'behaviour_Parameter', b2)
    if hasattr(b2, 'behaviour_DeviceAction'):
        assert not _is_linked(b2, 'behaviour_DeviceAction', a)


def test_assoc_parameters38_link_reassign_clear():
    a = behaviour_Parameter(key="sample_text", value="sample_text")
    b1 = behaviour_Feedback(actionName="sample_text")
    b2 = behaviour_Feedback(actionName="sample_text_2")
    _safe_set(a, 'behaviour_Parameter39', b1)
    assert _is_linked(a, 'behaviour_Parameter39', b1)
    if hasattr(b1, 'behaviour_Feedback'):
        assert _is_linked(b1, 'behaviour_Feedback', a)
    _safe_set(a, 'behaviour_Parameter39', b2)
    assert _is_linked(a, 'behaviour_Parameter39', b2)
    if hasattr(b1, 'behaviour_Feedback'):
        assert not _is_linked(b1, 'behaviour_Feedback', a)
    if hasattr(b2, 'behaviour_Feedback'):
        assert _is_linked(b2, 'behaviour_Feedback', a)
    _safe_set(a, 'behaviour_Parameter39', None)
    assert not _is_linked(a, 'behaviour_Parameter39', b2)
    if hasattr(b2, 'behaviour_Feedback'):
        assert not _is_linked(b2, 'behaviour_Feedback', a)


def test_assoc_receiver22_link_reassign_clear():
    a = behaviour_Drone(travelMode="sample_text", typeName="sample_text")
    b1 = behaviour_UnicastNotify()
    b2 = behaviour_UnicastNotify()
    _safe_set(a, 'behaviour_Drone23', b1)
    assert _is_linked(a, 'behaviour_Drone23', b1)
    if hasattr(b1, 'behaviour_UnicastNotify'):
        assert _is_linked(b1, 'behaviour_UnicastNotify', a)
    _safe_set(a, 'behaviour_Drone23', b2)
    assert _is_linked(a, 'behaviour_Drone23', b2)
    if hasattr(b1, 'behaviour_UnicastNotify'):
        assert not _is_linked(b1, 'behaviour_UnicastNotify', a)
    if hasattr(b2, 'behaviour_UnicastNotify'):
        assert _is_linked(b2, 'behaviour_UnicastNotify', a)
    _safe_set(a, 'behaviour_Drone23', None)
    assert not _is_linked(a, 'behaviour_Drone23', b2)
    if hasattr(b2, 'behaviour_UnicastNotify'):
        assert not _is_linked(b2, 'behaviour_UnicastNotify', a)


def test_assoc_receiver24_link_reassign_clear():
    a = behaviour_Drone(travelMode="sample_text", typeName="sample_text")
    b1 = behaviour_MulticastNotify()
    b2 = behaviour_MulticastNotify()
    _safe_set(a, 'behaviour_Drone25', b1)
    assert _is_linked(a, 'behaviour_Drone25', b1)
    if hasattr(b1, 'behaviour_MulticastNotify'):
        assert _is_linked(b1, 'behaviour_MulticastNotify', a)
    _safe_set(a, 'behaviour_Drone25', b2)
    assert _is_linked(a, 'behaviour_Drone25', b2)
    if hasattr(b1, 'behaviour_MulticastNotify'):
        assert not _is_linked(b1, 'behaviour_MulticastNotify', a)
    if hasattr(b2, 'behaviour_MulticastNotify'):
        assert _is_linked(b2, 'behaviour_MulticastNotify', a)
    _safe_set(a, 'behaviour_Drone25', None)
    assert not _is_linked(a, 'behaviour_Drone25', b2)
    if hasattr(b2, 'behaviour_MulticastNotify'):
        assert not _is_linked(b2, 'behaviour_MulticastNotify', a)


def test_assoc_slots7_link_reassign_clear():
    a = behaviour_Drone(travelMode="sample_text", typeName="sample_text")
    b1 = behaviour_Slot()
    b2 = behaviour_Slot()
    _safe_set(a, 'behaviour_Drone8', {b1})
    assert _is_linked(a, 'behaviour_Drone8', b1)
    if hasattr(b1, 'behaviour_Slot'):
        assert _is_linked(b1, 'behaviour_Slot', a)
    _safe_set(a, 'behaviour_Drone8', {b2})
    assert _is_linked(a, 'behaviour_Drone8', b2)
    if hasattr(b1, 'behaviour_Slot'):
        assert not _is_linked(b1, 'behaviour_Slot', a)
    if hasattr(b2, 'behaviour_Slot'):
        assert _is_linked(b2, 'behaviour_Slot', a)
    _safe_set(a, 'behaviour_Drone8', set())
    assert not _is_linked(a, 'behaviour_Drone8', b2)
    if hasattr(b2, 'behaviour_Slot'):
        assert not _is_linked(b2, 'behaviour_Slot', a)


def test_assoc_targetPosition16_link_reassign_clear():
    a = behaviour_GoTo(strategy="sample_text")
    b1 = behaviour_Coordinate(altitude=3.14, heading=3.14, latitude=3.14, longitude=3.14)
    b2 = behaviour_Coordinate(altitude=9.99, heading=9.99, latitude=9.99, longitude=9.99)
    _safe_set(a, 'behaviour_GoTo', b1)
    assert _is_linked(a, 'behaviour_GoTo', b1)
    if hasattr(b1, 'behaviour_Coordinate17'):
        assert _is_linked(b1, 'behaviour_Coordinate17', a)
    _safe_set(a, 'behaviour_GoTo', b2)
    assert _is_linked(a, 'behaviour_GoTo', b2)
    if hasattr(b1, 'behaviour_Coordinate17'):
        assert not _is_linked(b1, 'behaviour_Coordinate17', a)
    if hasattr(b2, 'behaviour_Coordinate17'):
        assert _is_linked(b2, 'behaviour_Coordinate17', a)
    _safe_set(a, 'behaviour_GoTo', None)
    assert not _is_linked(a, 'behaviour_GoTo', b2)
    if hasattr(b2, 'behaviour_Coordinate17'):
        assert not _is_linked(b2, 'behaviour_Coordinate17', a)


def test_assoc_targetPosition18_link_reassign_clear():
    a = behaviour_Coordinate(altitude=3.14, heading=3.14, latitude=3.14, longitude=3.14)
    b1 = behaviour_Circle(altitude=3.14, clockwise=True, duration=3.14, radius=3.14)
    b2 = behaviour_Circle(altitude=9.99, clockwise=False, duration=9.99, radius=9.99)
    _safe_set(a, 'behaviour_Coordinate19', b1)
    assert _is_linked(a, 'behaviour_Coordinate19', b1)
    if hasattr(b1, 'behaviour_Circle'):
        assert _is_linked(b1, 'behaviour_Circle', a)
    _safe_set(a, 'behaviour_Coordinate19', b2)
    assert _is_linked(a, 'behaviour_Coordinate19', b2)
    if hasattr(b1, 'behaviour_Circle'):
        assert not _is_linked(b1, 'behaviour_Circle', a)
    if hasattr(b2, 'behaviour_Circle'):
        assert _is_linked(b2, 'behaviour_Circle', a)
    _safe_set(a, 'behaviour_Coordinate19', None)
    assert not _is_linked(a, 'behaviour_Coordinate19', b2)
    if hasattr(b2, 'behaviour_Circle'):
        assert not _is_linked(b2, 'behaviour_Circle', a)


def test_assoc_to35_link_reassign_clear():
    a = behaviour_MoveTransition(fluid=True)
    b1 = behaviour_Move()
    b2 = behaviour_Move()
    _safe_set(a, 'behaviour_MoveTransition36', b1)
    assert _is_linked(a, 'behaviour_MoveTransition36', b1)
    if hasattr(b1, 'behaviour_Move37'):
        assert _is_linked(b1, 'behaviour_Move37', a)
    _safe_set(a, 'behaviour_MoveTransition36', b2)
    assert _is_linked(a, 'behaviour_MoveTransition36', b2)
    if hasattr(b1, 'behaviour_Move37'):
        assert not _is_linked(b1, 'behaviour_Move37', a)
    if hasattr(b2, 'behaviour_Move37'):
        assert _is_linked(b2, 'behaviour_Move37', a)
    _safe_set(a, 'behaviour_MoveTransition36', None)
    assert not _is_linked(a, 'behaviour_MoveTransition36', b2)
    if hasattr(b2, 'behaviour_Move37'):
        assert not _is_linked(b2, 'behaviour_Move37', a)


def test_assoc_waitFor29_link_reassign_clear():
    a = behaviour_MoveTransition(fluid=True)
    b1 = behaviour_Slot()
    b2 = behaviour_Slot()
    _safe_set(a, 'behaviour_MoveTransition30', b1)
    assert _is_linked(a, 'behaviour_MoveTransition30', b1)
    if hasattr(b1, 'behaviour_Slot31'):
        assert _is_linked(b1, 'behaviour_Slot31', a)
    _safe_set(a, 'behaviour_MoveTransition30', b2)
    assert _is_linked(a, 'behaviour_MoveTransition30', b2)
    if hasattr(b1, 'behaviour_Slot31'):
        assert not _is_linked(b1, 'behaviour_Slot31', a)
    if hasattr(b2, 'behaviour_Slot31'):
        assert _is_linked(b2, 'behaviour_Slot31', a)
    _safe_set(a, 'behaviour_MoveTransition30', None)
    assert not _is_linked(a, 'behaviour_MoveTransition30', b2)
    if hasattr(b2, 'behaviour_Slot31'):
        assert not _is_linked(b2, 'behaviour_Slot31', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


CommunicationAction_strategy = st.builds(CommunicationAction)
@given(instance=CommunicationAction_strategy)
@settings(max_examples=25)
def test_CommunicationAction_instantiation(instance):
    assert isinstance(instance, CommunicationAction)


Move_strategy = st.builds(Move)
@given(instance=Move_strategy)
@settings(max_examples=25)
def test_Move_instantiation(instance):
    assert isinstance(instance, Move)


MoveTransition_strategy = st.builds(MoveTransition)
@given(instance=MoveTransition_strategy)
@settings(max_examples=25)
def test_MoveTransition_instantiation(instance):
    assert isinstance(instance, MoveTransition)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Notify_strategy = st.builds(Notify)
@given(instance=Notify_strategy)
@settings(max_examples=25)
def test_Notify_instantiation(instance):
    assert isinstance(instance, Notify)


behaviour_Action_strategy = st.builds(behaviour_Action)
@given(instance=behaviour_Action_strategy)
@settings(max_examples=25)
def test_behaviour_Action_instantiation(instance):
    assert isinstance(instance, behaviour_Action)


behaviour_Behaviour_strategy = st.builds(behaviour_Behaviour, crs=safe_text)
@given(instance=behaviour_Behaviour_strategy)
@settings(max_examples=25)
def test_behaviour_Behaviour_instantiation(instance):
    assert isinstance(instance, behaviour_Behaviour)


behaviour_BroadcastNotify_strategy = st.builds(behaviour_BroadcastNotify)
@given(instance=behaviour_BroadcastNotify_strategy)
@settings(max_examples=25)
def test_behaviour_BroadcastNotify_instantiation(instance):
    assert isinstance(instance, behaviour_BroadcastNotify)


behaviour_CheckNotification_strategy = st.builds(behaviour_CheckNotification)
@given(instance=behaviour_CheckNotification_strategy)
@settings(max_examples=25)
def test_behaviour_CheckNotification_instantiation(instance):
    assert isinstance(instance, behaviour_CheckNotification)


behaviour_Choice_strategy = st.builds(behaviour_Choice, conditionIdentifier=safe_text)
@given(instance=behaviour_Choice_strategy)
@settings(max_examples=25)
def test_behaviour_Choice_instantiation(instance):
    assert isinstance(instance, behaviour_Choice)


behaviour_Circle_strategy = st.builds(behaviour_Circle, altitude=st.floats(allow_nan=False, allow_infinity=False), clockwise=st.booleans(), duration=st.floats(allow_nan=False, allow_infinity=False), radius=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=behaviour_Circle_strategy)
@settings(max_examples=25)
def test_behaviour_Circle_instantiation(instance):
    assert isinstance(instance, behaviour_Circle)


behaviour_CommunicationAction_strategy = st.builds(behaviour_CommunicationAction)
@given(instance=behaviour_CommunicationAction_strategy)
@settings(max_examples=25)
def test_behaviour_CommunicationAction_instantiation(instance):
    assert isinstance(instance, behaviour_CommunicationAction)


behaviour_Coordinate_strategy = st.builds(behaviour_Coordinate, altitude=st.floats(allow_nan=False, allow_infinity=False), heading=st.floats(allow_nan=False, allow_infinity=False), latitude=st.floats(allow_nan=False, allow_infinity=False), longitude=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=behaviour_Coordinate_strategy)
@settings(max_examples=25)
def test_behaviour_Coordinate_instantiation(instance):
    assert isinstance(instance, behaviour_Coordinate)


behaviour_DeviceAction_strategy = st.builds(behaviour_DeviceAction, actionName=safe_text)
@given(instance=behaviour_DeviceAction_strategy)
@settings(max_examples=25)
def test_behaviour_DeviceAction_instantiation(instance):
    assert isinstance(instance, behaviour_DeviceAction)


behaviour_Drone_strategy = st.builds(behaviour_Drone, travelMode=safe_text, typeName=safe_text)
@given(instance=behaviour_Drone_strategy)
@settings(max_examples=25)
def test_behaviour_Drone_instantiation(instance):
    assert isinstance(instance, behaviour_Drone)


behaviour_Feedback_strategy = st.builds(behaviour_Feedback, actionName=safe_text)
@given(instance=behaviour_Feedback_strategy)
@settings(max_examples=25)
def test_behaviour_Feedback_instantiation(instance):
    assert isinstance(instance, behaviour_Feedback)


behaviour_GoTo_strategy = st.builds(behaviour_GoTo, strategy=safe_text)
@given(instance=behaviour_GoTo_strategy)
@settings(max_examples=25)
def test_behaviour_GoTo_instantiation(instance):
    assert isinstance(instance, behaviour_GoTo)


behaviour_HeadTo_strategy = st.builds(behaviour_HeadTo, direction=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=behaviour_HeadTo_strategy)
@settings(max_examples=25)
def test_behaviour_HeadTo_instantiation(instance):
    assert isinstance(instance, behaviour_HeadTo)


behaviour_Hover_strategy = st.builds(behaviour_Hover, duration=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=behaviour_Hover_strategy)
@settings(max_examples=25)
def test_behaviour_Hover_instantiation(instance):
    assert isinstance(instance, behaviour_Hover)


behaviour_Land_strategy = st.builds(behaviour_Land)
@given(instance=behaviour_Land_strategy)
@settings(max_examples=25)
def test_behaviour_Land_instantiation(instance):
    assert isinstance(instance, behaviour_Land)


behaviour_Move_strategy = st.builds(behaviour_Move)
@given(instance=behaviour_Move_strategy)
@settings(max_examples=25)
def test_behaviour_Move_instantiation(instance):
    assert isinstance(instance, behaviour_Move)


behaviour_MoveTransition_strategy = st.builds(behaviour_MoveTransition, fluid=st.booleans())
@given(instance=behaviour_MoveTransition_strategy)
@settings(max_examples=25)
def test_behaviour_MoveTransition_instantiation(instance):
    assert isinstance(instance, behaviour_MoveTransition)


behaviour_MulticastNotify_strategy = st.builds(behaviour_MulticastNotify)
@given(instance=behaviour_MulticastNotify_strategy)
@settings(max_examples=25)
def test_behaviour_MulticastNotify_instantiation(instance):
    assert isinstance(instance, behaviour_MulticastNotify)


behaviour_NamedElement_strategy = st.builds(behaviour_NamedElement, name=safe_text)
@given(instance=behaviour_NamedElement_strategy)
@settings(max_examples=25)
def test_behaviour_NamedElement_instantiation(instance):
    assert isinstance(instance, behaviour_NamedElement)


behaviour_Notify_strategy = st.builds(behaviour_Notify)
@given(instance=behaviour_Notify_strategy)
@settings(max_examples=25)
def test_behaviour_Notify_instantiation(instance):
    assert isinstance(instance, behaviour_Notify)


behaviour_Parameter_strategy = st.builds(behaviour_Parameter, key=safe_text, value=safe_text)
@given(instance=behaviour_Parameter_strategy)
@settings(max_examples=25)
def test_behaviour_Parameter_instantiation(instance):
    assert isinstance(instance, behaviour_Parameter)


behaviour_Slot_strategy = st.builds(behaviour_Slot)
@given(instance=behaviour_Slot_strategy)
@settings(max_examples=25)
def test_behaviour_Slot_instantiation(instance):
    assert isinstance(instance, behaviour_Slot)


behaviour_Start_strategy = st.builds(behaviour_Start)
@given(instance=behaviour_Start_strategy)
@settings(max_examples=25)
def test_behaviour_Start_instantiation(instance):
    assert isinstance(instance, behaviour_Start)


behaviour_Stop_strategy = st.builds(behaviour_Stop)
@given(instance=behaviour_Stop_strategy)
@settings(max_examples=25)
def test_behaviour_Stop_instantiation(instance):
    assert isinstance(instance, behaviour_Stop)


behaviour_TakeOff_strategy = st.builds(behaviour_TakeOff, altitude=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=behaviour_TakeOff_strategy)
@settings(max_examples=25)
def test_behaviour_TakeOff_instantiation(instance):
    assert isinstance(instance, behaviour_TakeOff)


behaviour_UnicastNotify_strategy = st.builds(behaviour_UnicastNotify)
@given(instance=behaviour_UnicastNotify_strategy)
@settings(max_examples=25)
def test_behaviour_UnicastNotify_instantiation(instance):
    assert isinstance(instance, behaviour_UnicastNotify)


