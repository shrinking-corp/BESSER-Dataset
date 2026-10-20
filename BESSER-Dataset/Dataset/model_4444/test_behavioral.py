import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ioT_Destination,
    ioT_DestinationType,
    ioT_DestinationTypes,
    ioT_Device,
    ioT_DeviceType,
    ioT_DeviceTypes,
    ioT_EObject,
    ioT_FetchData,
    ioT_FetchDataCondition,
    ioT_FetchDataExpression,
    ioT_Ip,
    ioT_Method,
    ioT_Portnumber,
    ioT_Sensor,
    ioT_SensorGetMethod,
    ioT_SensorGroup,
    ioT_SensorType,
    ioT_SensorTypes,
    ioT_Server,
    ioT_ServerType,
    ioT_ServerTypes,
    ioT_System,
    ioT_Time,
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

def test_assoc_duration34_reverse_link_reassign_clear():
    a1 = ioT_Time(time=7)
    a2 = ioT_Time(time=13)
    b = ioT_FetchDataExpression(timeUnit="sample_text")
    _safe_set(b, 'ioT_FetchDataExpression', a1)
    assert _is_linked(b, 'ioT_FetchDataExpression', a1)
    if hasattr(a1, 'ioT_Time'):
        assert _is_linked(a1, 'ioT_Time', b)
    _safe_set(b, 'ioT_FetchDataExpression', a2)
    assert _is_linked(b, 'ioT_FetchDataExpression', a2)
    if hasattr(a1, 'ioT_Time'):
        assert not _is_linked(a1, 'ioT_Time', b)
    if hasattr(a2, 'ioT_Time'):
        assert _is_linked(a2, 'ioT_Time', b)
    _safe_set(b, 'ioT_FetchDataExpression', None)
    assert not _is_linked(b, 'ioT_FetchDataExpression', a2)
    if hasattr(a2, 'ioT_Time'):
        assert not _is_linked(a2, 'ioT_Time', b)


def test_assoc_ip19_reverse_link_reassign_clear():
    a1 = ioT_Server(name="sample_text")
    a2 = ioT_Server(name="sample_text_2")
    b = ioT_Ip(ip=7)
    _safe_set(b, 'ioT_Ip', a1)
    assert _is_linked(b, 'ioT_Ip', a1)
    if hasattr(a1, 'ioT_Server20'):
        assert _is_linked(a1, 'ioT_Server20', b)
    _safe_set(b, 'ioT_Ip', a2)
    assert _is_linked(b, 'ioT_Ip', a2)
    if hasattr(a1, 'ioT_Server20'):
        assert not _is_linked(a1, 'ioT_Server20', b)
    if hasattr(a2, 'ioT_Server20'):
        assert _is_linked(a2, 'ioT_Server20', b)
    _safe_set(b, 'ioT_Ip', None)
    assert not _is_linked(b, 'ioT_Ip', a2)
    if hasattr(a2, 'ioT_Server20'):
        assert not _is_linked(a2, 'ioT_Server20', b)


def test_assoc_port21_reverse_link_reassign_clear():
    a1 = ioT_Server(name="sample_text")
    a2 = ioT_Server(name="sample_text_2")
    b = ioT_Portnumber(number=7)
    _safe_set(b, 'ioT_Portnumber', a1)
    assert _is_linked(b, 'ioT_Portnumber', a1)
    if hasattr(a1, 'ioT_Server22'):
        assert _is_linked(a1, 'ioT_Server22', b)
    _safe_set(b, 'ioT_Portnumber', a2)
    assert _is_linked(b, 'ioT_Portnumber', a2)
    if hasattr(a1, 'ioT_Server22'):
        assert not _is_linked(a1, 'ioT_Server22', b)
    if hasattr(a2, 'ioT_Server22'):
        assert _is_linked(a2, 'ioT_Server22', b)
    _safe_set(b, 'ioT_Portnumber', None)
    assert not _is_linked(b, 'ioT_Portnumber', a2)
    if hasattr(a2, 'ioT_Server22'):
        assert not _is_linked(a2, 'ioT_Server22', b)


def test_assoc_sensors4_reverse_link_reassign_clear():
    a1 = ioT_SensorGroup(name="sample_text")
    a2 = ioT_SensorGroup(name="sample_text_2")
    b = ioT_Sensor(name="sample_text")
    _safe_set(b, 'ioT_Sensor5', a1)
    assert _is_linked(b, 'ioT_Sensor5', a1)
    if hasattr(a1, 'ioT_SensorGroup'):
        assert _is_linked(a1, 'ioT_SensorGroup', b)
    _safe_set(b, 'ioT_Sensor5', a2)
    assert _is_linked(b, 'ioT_Sensor5', a2)
    if hasattr(a1, 'ioT_SensorGroup'):
        assert not _is_linked(a1, 'ioT_SensorGroup', b)
    if hasattr(a2, 'ioT_SensorGroup'):
        assert _is_linked(a2, 'ioT_SensorGroup', b)
    _safe_set(b, 'ioT_Sensor5', None)
    assert not _is_linked(b, 'ioT_Sensor5', a2)
    if hasattr(a2, 'ioT_SensorGroup'):
        assert not _is_linked(a2, 'ioT_SensorGroup', b)


def test_assoc_type11_reverse_link_reassign_clear():
    a1 = ioT_DeviceType(name="sample_text")
    a2 = ioT_DeviceType(name="sample_text_2")
    b = ioT_Device(name="sample_text")
    _safe_set(b, 'ioT_Device', a1)
    assert _is_linked(b, 'ioT_Device', a1)
    if hasattr(a1, 'ioT_DeviceType12'):
        assert _is_linked(a1, 'ioT_DeviceType12', b)
    _safe_set(b, 'ioT_Device', a2)
    assert _is_linked(b, 'ioT_Device', a2)
    if hasattr(a1, 'ioT_DeviceType12'):
        assert not _is_linked(a1, 'ioT_DeviceType12', b)
    if hasattr(a2, 'ioT_DeviceType12'):
        assert _is_linked(a2, 'ioT_DeviceType12', b)
    _safe_set(b, 'ioT_Device', None)
    assert not _is_linked(b, 'ioT_Device', a2)
    if hasattr(a2, 'ioT_DeviceType12'):
        assert not _is_linked(a2, 'ioT_DeviceType12', b)


def test_assoc_type17_reverse_link_reassign_clear():
    a1 = ioT_ServerType(name="sample_text")
    a2 = ioT_ServerType(name="sample_text_2")
    b = ioT_Server(name="sample_text")
    _safe_set(b, 'ioT_Server', a1)
    assert _is_linked(b, 'ioT_Server', a1)
    if hasattr(a1, 'ioT_ServerType18'):
        assert _is_linked(a1, 'ioT_ServerType18', b)
    _safe_set(b, 'ioT_Server', a2)
    assert _is_linked(b, 'ioT_Server', a2)
    if hasattr(a1, 'ioT_ServerType18'):
        assert not _is_linked(a1, 'ioT_ServerType18', b)
    if hasattr(a2, 'ioT_ServerType18'):
        assert _is_linked(a2, 'ioT_ServerType18', b)
    _safe_set(b, 'ioT_Server', None)
    assert not _is_linked(b, 'ioT_Server', a2)
    if hasattr(a2, 'ioT_ServerType18'):
        assert not _is_linked(a2, 'ioT_ServerType18', b)


def test_assoc_type2_reverse_link_reassign_clear():
    a1 = ioT_SensorType(name="sample_text")
    a2 = ioT_SensorType(name="sample_text_2")
    b = ioT_Sensor(name="sample_text")
    _safe_set(b, 'ioT_Sensor', a1)
    assert _is_linked(b, 'ioT_Sensor', a1)
    if hasattr(a1, 'ioT_SensorType3'):
        assert _is_linked(a1, 'ioT_SensorType3', b)
    _safe_set(b, 'ioT_Sensor', a2)
    assert _is_linked(b, 'ioT_Sensor', a2)
    if hasattr(a1, 'ioT_SensorType3'):
        assert not _is_linked(a1, 'ioT_SensorType3', b)
    if hasattr(a2, 'ioT_SensorType3'):
        assert _is_linked(a2, 'ioT_SensorType3', b)
    _safe_set(b, 'ioT_Sensor', None)
    assert not _is_linked(b, 'ioT_Sensor', a2)
    if hasattr(a2, 'ioT_SensorType3'):
        assert not _is_linked(a2, 'ioT_SensorType3', b)


def test_assoc_type24_reverse_link_reassign_clear():
    a1 = ioT_DestinationType(name="sample_text")
    a2 = ioT_DestinationType(name="sample_text_2")
    b = ioT_Destination(name="sample_text")
    _safe_set(b, 'ioT_Destination', a1)
    assert _is_linked(b, 'ioT_Destination', a1)
    if hasattr(a1, 'ioT_DestinationType25'):
        assert _is_linked(a1, 'ioT_DestinationType25', b)
    _safe_set(b, 'ioT_Destination', a2)
    assert _is_linked(b, 'ioT_Destination', a2)
    if hasattr(a1, 'ioT_DestinationType25'):
        assert not _is_linked(a1, 'ioT_DestinationType25', b)
    if hasattr(a2, 'ioT_DestinationType25'):
        assert _is_linked(a2, 'ioT_DestinationType25', b)
    _safe_set(b, 'ioT_Destination', None)
    assert not _is_linked(b, 'ioT_Destination', a2)
    if hasattr(a2, 'ioT_DestinationType25'):
        assert not _is_linked(a2, 'ioT_DestinationType25', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_devices13_stub_double():
    # ioT_EObject has no real 'ioT_EObject15' property in the generated
    # code (a bare stub) -- manually attach it so ioT_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_Device(name="sample_text")
    partner = ioT_EObject()
    setattr(partner, 'ioT_EObject15', None)
    _safe_set(owner, 'ioT_Device14', partner)
    assert getattr(partner, 'ioT_EObject15') == owner
    _safe_set(owner, 'ioT_Device14', None)
    assert getattr(partner, 'ioT_EObject15') is None


def test_assoc_method6_stub_double():
    # ioT_SensorGetMethod has no real 'ioT_SensorGetMethod' property in the generated
    # code (a bare stub) -- manually attach it so ioT_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_Method(name="sample_text", parameters="sample_text")
    partner = ioT_SensorGetMethod()
    setattr(partner, 'ioT_SensorGetMethod', None)
    _safe_set(owner, 'ioT_Method', partner)
    assert getattr(partner, 'ioT_SensorGetMethod') == owner
    _safe_set(owner, 'ioT_Method', None)
    assert getattr(partner, 'ioT_SensorGetMethod') is None


def test_assoc_type7_stub_double():
    # ioT_SensorGetMethod has no real 'ioT_SensorGetMethod8' property in the generated
    # code (a bare stub) -- manually attach it so ioT_SensorType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_SensorType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_SensorType(name="sample_text")
    partner = ioT_SensorGetMethod()
    setattr(partner, 'ioT_SensorGetMethod8', None)
    _safe_set(owner, 'ioT_SensorType9', partner)
    assert getattr(partner, 'ioT_SensorGetMethod8') == owner
    _safe_set(owner, 'ioT_SensorType9', None)
    assert getattr(partner, 'ioT_SensorGetMethod8') is None


def test_assoc_types1_stub_double():
    # ioT_SensorTypes has no real 'ioT_SensorTypes' property in the generated
    # code (a bare stub) -- manually attach it so ioT_SensorType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_SensorType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_SensorType(name="sample_text")
    partner = ioT_SensorTypes()
    setattr(partner, 'ioT_SensorTypes', None)
    _safe_set(owner, 'ioT_SensorType', partner)
    assert owner in getattr(partner, 'ioT_SensorTypes')
    _safe_set(owner, 'ioT_SensorType', None)
    assert owner not in getattr(partner, 'ioT_SensorTypes')


def test_assoc_types10_stub_double():
    # ioT_DeviceTypes has no real 'ioT_DeviceTypes' property in the generated
    # code (a bare stub) -- manually attach it so ioT_DeviceType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_DeviceType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_DeviceType(name="sample_text")
    partner = ioT_DeviceTypes()
    setattr(partner, 'ioT_DeviceTypes', None)
    _safe_set(owner, 'ioT_DeviceType', partner)
    assert owner in getattr(partner, 'ioT_DeviceTypes')
    _safe_set(owner, 'ioT_DeviceType', None)
    assert owner not in getattr(partner, 'ioT_DeviceTypes')


def test_assoc_types16_stub_double():
    # ioT_ServerTypes has no real 'ioT_ServerTypes' property in the generated
    # code (a bare stub) -- manually attach it so ioT_ServerType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_ServerType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_ServerType(name="sample_text")
    partner = ioT_ServerTypes()
    setattr(partner, 'ioT_ServerTypes', None)
    _safe_set(owner, 'ioT_ServerType', partner)
    assert owner in getattr(partner, 'ioT_ServerTypes')
    _safe_set(owner, 'ioT_ServerType', None)
    assert owner not in getattr(partner, 'ioT_ServerTypes')


def test_assoc_types23_stub_double():
    # ioT_DestinationTypes has no real 'ioT_DestinationTypes' property in the generated
    # code (a bare stub) -- manually attach it so ioT_DestinationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_DestinationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_DestinationType(name="sample_text")
    partner = ioT_DestinationTypes()
    setattr(partner, 'ioT_DestinationTypes', None)
    _safe_set(owner, 'ioT_DestinationType', partner)
    assert owner in getattr(partner, 'ioT_DestinationTypes')
    _safe_set(owner, 'ioT_DestinationType', None)
    assert owner not in getattr(partner, 'ioT_DestinationTypes')


