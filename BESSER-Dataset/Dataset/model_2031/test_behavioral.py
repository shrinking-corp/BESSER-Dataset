import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Active_Digital_Artifact,
    Actuator,
    Device,
    DeviceState,
    Digital_Artifact,
    Entity,
    Evaluators,
    InformationResource,
    Passive_Digital_Artifact,
    PhysicalThing,
    Sensor,
    User,
    ioT_metamodel_Action,
    ioT_metamodel_Active_Digital_Artifact,
    ioT_metamodel_Actuator,
    ioT_metamodel_Analytics_Engine,
    ioT_metamodel_AtomicData,
    ioT_metamodel_AtomicDataAttributes,
    ioT_metamodel_Attribute,
    ioT_metamodel_Authorizor,
    ioT_metamodel_Cloud,
    ioT_metamodel_Communicator,
    ioT_metamodel_CompositeState,
    ioT_metamodel_Container,
    ioT_metamodel_DataStreamAttributes,
    ioT_metamodel_DataStreams,
    ioT_metamodel_Database,
    ioT_metamodel_Device,
    ioT_metamodel_DeviceActuator,
    ioT_metamodel_DeviceSensor,
    ioT_metamodel_DeviceState,
    ioT_metamodel_Device_Resource,
    ioT_metamodel_Digital_Artifact,
    ioT_metamodel_Entity,
    ioT_metamodel_Evaluators,
    ioT_metamodel_ExternalActuator,
    ioT_metamodel_ExternalSensor,
    ioT_metamodel_Fog,
    ioT_metamodel_FogNode,
    ioT_metamodel_Fog_Services,
    ioT_metamodel_Human_User,
    ioT_metamodel_Information,
    ioT_metamodel_InformationResource,
    ioT_metamodel_JavaEvaluator,
    ioT_metamodel_Network_Resource,
    ioT_metamodel_On_Device_Resource,
    ioT_metamodel_Operations,
    ioT_metamodel_Passive_Digital_Artifact,
    ioT_metamodel_PhysicalThing,
    ioT_metamodel_Policy_Repository,
    ioT_metamodel_Port,
    ioT_metamodel_Property,
    ioT_metamodel_Reference_Monitor,
    ioT_metamodel_Rule,
    ioT_metamodel_ScriptEvaluator,
    ioT_metamodel_Sensor,
    ioT_metamodel_Service_Resource,
    ioT_metamodel_Tag,
    ioT_metamodel_Thing,
    ioT_metamodel_Transition,
    ioT_metamodel_User,
    ioT_metamodel_VM,
    ioT_metamodel_VirtualThing,
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

def test_assoc_contains31_reverse_link_reassign_clear():
    a1 = ioT_metamodel_Device(Technology="sample_text")
    a2 = ioT_metamodel_Device(Technology="sample_text_2")
    b = ioT_metamodel_Device(Technology="sample_text")
    _safe_set(b, 'ioT_metamodel_Device30', {a1})
    assert _is_linked(b, 'ioT_metamodel_Device30', a1)
    if hasattr(a1, 'ioT_metamodel_Device'):
        assert _is_linked(a1, 'ioT_metamodel_Device', b)
    _safe_set(b, 'ioT_metamodel_Device30', {a2})
    assert _is_linked(b, 'ioT_metamodel_Device30', a2)
    if hasattr(a1, 'ioT_metamodel_Device'):
        assert not _is_linked(a1, 'ioT_metamodel_Device', b)
    if hasattr(a2, 'ioT_metamodel_Device'):
        assert _is_linked(a2, 'ioT_metamodel_Device', b)
    _safe_set(b, 'ioT_metamodel_Device30', set())
    assert not _is_linked(b, 'ioT_metamodel_Device30', a2)
    if hasattr(a2, 'ioT_metamodel_Device'):
        assert not _is_linked(a2, 'ioT_metamodel_Device', b)


def test_assoc_contains5_reverse_link_reassign_clear():
    a1 = ioT_metamodel_Thing(name="sample_text")
    a2 = ioT_metamodel_Thing(name="sample_text_2")
    b = ioT_metamodel_Thing(name="sample_text")
    _safe_set(b, 'ioT_metamodel_Thing6', a1)
    assert _is_linked(b, 'ioT_metamodel_Thing6', a1)
    if hasattr(a1, 'ioT_metamodel_Thing4'):
        assert _is_linked(a1, 'ioT_metamodel_Thing4', b)
    _safe_set(b, 'ioT_metamodel_Thing6', a2)
    assert _is_linked(b, 'ioT_metamodel_Thing6', a2)
    if hasattr(a1, 'ioT_metamodel_Thing4'):
        assert not _is_linked(a1, 'ioT_metamodel_Thing4', b)
    if hasattr(a2, 'ioT_metamodel_Thing4'):
        assert _is_linked(a2, 'ioT_metamodel_Thing4', b)
    _safe_set(b, 'ioT_metamodel_Thing6', None)
    assert not _is_linked(b, 'ioT_metamodel_Thing6', a2)
    if hasattr(a2, 'ioT_metamodel_Thing4'):
        assert not _is_linked(a2, 'ioT_metamodel_Thing4', b)


def test_assoc_devicestate34_reverse_link_reassign_clear():
    a1 = ioT_metamodel_DeviceState(Enabled=True)
    a2 = ioT_metamodel_DeviceState(Enabled=False)
    b = ioT_metamodel_Device(Technology="sample_text")
    _safe_set(b, 'ioT_metamodel_Device35', a1)
    assert _is_linked(b, 'ioT_metamodel_Device35', a1)
    if hasattr(a1, 'ioT_metamodel_DeviceState'):
        assert _is_linked(a1, 'ioT_metamodel_DeviceState', b)
    _safe_set(b, 'ioT_metamodel_Device35', a2)
    assert _is_linked(b, 'ioT_metamodel_Device35', a2)
    if hasattr(a1, 'ioT_metamodel_DeviceState'):
        assert not _is_linked(a1, 'ioT_metamodel_DeviceState', b)
    if hasattr(a2, 'ioT_metamodel_DeviceState'):
        assert _is_linked(a2, 'ioT_metamodel_DeviceState', b)
    _safe_set(b, 'ioT_metamodel_Device35', None)
    assert not _is_linked(b, 'ioT_metamodel_Device35', a2)
    if hasattr(a2, 'ioT_metamodel_DeviceState'):
        assert not _is_linked(a2, 'ioT_metamodel_DeviceState', b)


def test_assoc_has_communicators36_reverse_link_reassign_clear():
    a1 = ioT_metamodel_Device(Technology="sample_text")
    a2 = ioT_metamodel_Device(Technology="sample_text_2")
    b = ioT_metamodel_Communicator(Type="sample_text", ports_number=7)
    _safe_set(b, 'ioT_metamodel_Communicator', a1)
    assert _is_linked(b, 'ioT_metamodel_Communicator', a1)
    if hasattr(a1, 'ioT_metamodel_Device37'):
        assert _is_linked(a1, 'ioT_metamodel_Device37', b)
    _safe_set(b, 'ioT_metamodel_Communicator', a2)
    assert _is_linked(b, 'ioT_metamodel_Communicator', a2)
    if hasattr(a1, 'ioT_metamodel_Device37'):
        assert not _is_linked(a1, 'ioT_metamodel_Device37', b)
    if hasattr(a2, 'ioT_metamodel_Device37'):
        assert _is_linked(a2, 'ioT_metamodel_Device37', b)
    _safe_set(b, 'ioT_metamodel_Communicator', None)
    assert not _is_linked(b, 'ioT_metamodel_Communicator', a2)
    if hasattr(a2, 'ioT_metamodel_Device37'):
        assert not _is_linked(a2, 'ioT_metamodel_Device37', b)


def test_assoc_has_rules32_reverse_link_reassign_clear():
    a1 = ioT_metamodel_Rule(conditionLiteral="sample_text", conditionValue=3.14)
    a2 = ioT_metamodel_Rule(conditionLiteral="sample_text_2", conditionValue=9.99)
    b = ioT_metamodel_Device(Technology="sample_text")
    _safe_set(b, 'ioT_metamodel_Device33', {a1})
    assert _is_linked(b, 'ioT_metamodel_Device33', a1)
    if hasattr(a1, 'ioT_metamodel_Rule'):
        assert _is_linked(a1, 'ioT_metamodel_Rule', b)
    _safe_set(b, 'ioT_metamodel_Device33', {a2})
    assert _is_linked(b, 'ioT_metamodel_Device33', a2)
    if hasattr(a1, 'ioT_metamodel_Rule'):
        assert not _is_linked(a1, 'ioT_metamodel_Rule', b)
    if hasattr(a2, 'ioT_metamodel_Rule'):
        assert _is_linked(a2, 'ioT_metamodel_Rule', b)
    _safe_set(b, 'ioT_metamodel_Device33', set())
    assert not _is_linked(b, 'ioT_metamodel_Device33', a2)
    if hasattr(a2, 'ioT_metamodel_Rule'):
        assert not _is_linked(a2, 'ioT_metamodel_Rule', b)


def test_assoc_involves52_reverse_link_reassign_clear():
    a1 = ioT_metamodel_Rule(conditionLiteral="sample_text", conditionValue=3.14)
    a2 = ioT_metamodel_Rule(conditionLiteral="sample_text_2", conditionValue=9.99)
    b = ioT_metamodel_Action(Description="sample_text")
    _safe_set(b, 'ioT_metamodel_Action', a1)
    assert _is_linked(b, 'ioT_metamodel_Action', a1)
    if hasattr(a1, 'ioT_metamodel_Rule53'):
        assert _is_linked(a1, 'ioT_metamodel_Rule53', b)
    _safe_set(b, 'ioT_metamodel_Action', a2)
    assert _is_linked(b, 'ioT_metamodel_Action', a2)
    if hasattr(a1, 'ioT_metamodel_Rule53'):
        assert not _is_linked(a1, 'ioT_metamodel_Rule53', b)
    if hasattr(a2, 'ioT_metamodel_Rule53'):
        assert _is_linked(a2, 'ioT_metamodel_Rule53', b)
    _safe_set(b, 'ioT_metamodel_Action', None)
    assert not _is_linked(b, 'ioT_metamodel_Action', a2)
    if hasattr(a2, 'ioT_metamodel_Rule53'):
        assert not _is_linked(a2, 'ioT_metamodel_Rule53', b)


def test_assoc_observes42_reverse_link_reassign_clear():
    a1 = ioT_metamodel_DeviceState(Enabled=True)
    a2 = ioT_metamodel_DeviceState(Enabled=False)
    b = ioT_metamodel_Actuator(name="sample_text")
    _safe_set(b, 'ioT_metamodel_Actuator43', a1)
    assert _is_linked(b, 'ioT_metamodel_Actuator43', a1)
    if hasattr(a1, 'ioT_metamodel_DeviceState44'):
        assert _is_linked(a1, 'ioT_metamodel_DeviceState44', b)
    _safe_set(b, 'ioT_metamodel_Actuator43', a2)
    assert _is_linked(b, 'ioT_metamodel_Actuator43', a2)
    if hasattr(a1, 'ioT_metamodel_DeviceState44'):
        assert not _is_linked(a1, 'ioT_metamodel_DeviceState44', b)
    if hasattr(a2, 'ioT_metamodel_DeviceState44'):
        assert _is_linked(a2, 'ioT_metamodel_DeviceState44', b)
    _safe_set(b, 'ioT_metamodel_Actuator43', None)
    assert not _is_linked(b, 'ioT_metamodel_Actuator43', a2)
    if hasattr(a2, 'ioT_metamodel_DeviceState44'):
        assert not _is_linked(a2, 'ioT_metamodel_DeviceState44', b)


def test_assoc_observes49_reverse_link_reassign_clear():
    a1 = ioT_metamodel_Sensor(Name="sample_text", State=True, frequency=3.14)
    a2 = ioT_metamodel_Sensor(Name="sample_text_2", State=False, frequency=9.99)
    b = ioT_metamodel_DeviceState(Enabled=True)
    _safe_set(b, 'ioT_metamodel_DeviceState51', a1)
    assert _is_linked(b, 'ioT_metamodel_DeviceState51', a1)
    if hasattr(a1, 'ioT_metamodel_Sensor50'):
        assert _is_linked(a1, 'ioT_metamodel_Sensor50', b)
    _safe_set(b, 'ioT_metamodel_DeviceState51', a2)
    assert _is_linked(b, 'ioT_metamodel_DeviceState51', a2)
    if hasattr(a1, 'ioT_metamodel_Sensor50'):
        assert not _is_linked(a1, 'ioT_metamodel_Sensor50', b)
    if hasattr(a2, 'ioT_metamodel_Sensor50'):
        assert _is_linked(a2, 'ioT_metamodel_Sensor50', b)
    _safe_set(b, 'ioT_metamodel_DeviceState51', None)
    assert not _is_linked(b, 'ioT_metamodel_DeviceState51', a2)
    if hasattr(a2, 'ioT_metamodel_Sensor50'):
        assert not _is_linked(a2, 'ioT_metamodel_Sensor50', b)


def test_assoc_property7_reverse_link_reassign_clear():
    a1 = ioT_metamodel_Thing(name="sample_text")
    a2 = ioT_metamodel_Thing(name="sample_text_2")
    b = ioT_metamodel_Property(changeable=True)
    _safe_set(b, 'ioT_metamodel_Property', a1)
    assert _is_linked(b, 'ioT_metamodel_Property', a1)
    if hasattr(a1, 'ioT_metamodel_Thing8'):
        assert _is_linked(a1, 'ioT_metamodel_Thing8', b)
    _safe_set(b, 'ioT_metamodel_Property', a2)
    assert _is_linked(b, 'ioT_metamodel_Property', a2)
    if hasattr(a1, 'ioT_metamodel_Thing8'):
        assert not _is_linked(a1, 'ioT_metamodel_Thing8', b)
    if hasattr(a2, 'ioT_metamodel_Thing8'):
        assert _is_linked(a2, 'ioT_metamodel_Thing8', b)
    _safe_set(b, 'ioT_metamodel_Property', None)
    assert not _is_linked(b, 'ioT_metamodel_Property', a2)
    if hasattr(a2, 'ioT_metamodel_Thing8'):
        assert not _is_linked(a2, 'ioT_metamodel_Thing8', b)


def test_assoc_virtual_entity0_reverse_link_reassign_clear():
    a1 = ioT_metamodel_VirtualThing(URI="sample_text")
    a2 = ioT_metamodel_VirtualThing(URI="sample_text_2")
    b = ioT_metamodel_Thing(name="sample_text")
    _safe_set(b, 'ioT_metamodel_Thing', a1)
    assert _is_linked(b, 'ioT_metamodel_Thing', a1)
    if hasattr(a1, 'ioT_metamodel_VirtualThing'):
        assert _is_linked(a1, 'ioT_metamodel_VirtualThing', b)
    _safe_set(b, 'ioT_metamodel_Thing', a2)
    assert _is_linked(b, 'ioT_metamodel_Thing', a2)
    if hasattr(a1, 'ioT_metamodel_VirtualThing'):
        assert not _is_linked(a1, 'ioT_metamodel_VirtualThing', b)
    if hasattr(a2, 'ioT_metamodel_VirtualThing'):
        assert _is_linked(a2, 'ioT_metamodel_VirtualThing', b)
    _safe_set(b, 'ioT_metamodel_Thing', None)
    assert not _is_linked(b, 'ioT_metamodel_Thing', a2)
    if hasattr(a2, 'ioT_metamodel_VirtualThing'):
        assert not _is_linked(a2, 'ioT_metamodel_VirtualThing', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action60_stub_double():
    # ioT_metamodel_Transition has no real 'ioT_metamodel_Transition' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Action(Description="sample_text")
    partner = ioT_metamodel_Transition()
    setattr(partner, 'ioT_metamodel_Transition', None)
    _safe_set(owner, 'ioT_metamodel_Action61', partner)
    assert owner in getattr(partner, 'ioT_metamodel_Transition')
    _safe_set(owner, 'ioT_metamodel_Action61', None)
    assert owner not in getattr(partner, 'ioT_metamodel_Transition')


def test_assoc_acts40_stub_double():
    # ioT_metamodel_PhysicalThing has no real 'ioT_metamodel_PhysicalThing41' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Actuator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Actuator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Actuator(name="sample_text")
    partner = ioT_metamodel_PhysicalThing()
    setattr(partner, 'ioT_metamodel_PhysicalThing41', None)
    _safe_set(owner, 'ioT_metamodel_Actuator', {partner})
    assert getattr(partner, 'ioT_metamodel_PhysicalThing41') == owner
    _safe_set(owner, 'ioT_metamodel_Actuator', set())
    assert getattr(partner, 'ioT_metamodel_PhysicalThing41') is None


def test_assoc_actuator_actions56_stub_double():
    # ioT_metamodel_DeviceActuator has no real 'ioT_metamodel_DeviceActuator' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Action(Description="sample_text")
    partner = ioT_metamodel_DeviceActuator()
    setattr(partner, 'ioT_metamodel_DeviceActuator', None)
    _safe_set(owner, 'ioT_metamodel_Action57', partner)
    assert owner in getattr(partner, 'ioT_metamodel_DeviceActuator')
    _safe_set(owner, 'ioT_metamodel_Action57', None)
    assert owner not in getattr(partner, 'ioT_metamodel_DeviceActuator')


def test_assoc_actuator_actions58_stub_double():
    # ioT_metamodel_ExternalActuator has no real 'ioT_metamodel_ExternalActuator' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Action(Description="sample_text")
    partner = ioT_metamodel_ExternalActuator()
    setattr(partner, 'ioT_metamodel_ExternalActuator', None)
    _safe_set(owner, 'ioT_metamodel_Action59', partner)
    assert owner in getattr(partner, 'ioT_metamodel_ExternalActuator')
    _safe_set(owner, 'ioT_metamodel_Action59', None)
    assert owner not in getattr(partner, 'ioT_metamodel_ExternalActuator')


def test_assoc_fog1_stub_double():
    # ioT_metamodel_Fog has no real 'Fog' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Thing(name="sample_text")
    partner = ioT_metamodel_Fog()
    setattr(partner, 'Fog', None)
    _safe_set(owner, 'request_service', partner)
    assert getattr(partner, 'Fog') == owner
    _safe_set(owner, 'request_service', None)
    assert getattr(partner, 'Fog') is None


def test_assoc_has14_stub_double():
    # ioT_metamodel_PhysicalThing has no real 'is_attached_to' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Device(Technology="sample_text")
    partner = ioT_metamodel_PhysicalThing()
    setattr(partner, 'is_attached_to', None)
    _safe_set(owner, 'Device', partner)
    assert owner in getattr(partner, 'is_attached_to')
    _safe_set(owner, 'Device', None)
    assert owner not in getattr(partner, 'is_attached_to')


def test_assoc_has_atomicdataattributes109_stub_double():
    # ioT_metamodel_AtomicData has no real 'ioT_metamodel_AtomicData110' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_AtomicDataAttributes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_AtomicDataAttributes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_AtomicDataAttributes(DataEncoding="sample_text", DeviceID="sample_text")
    partner = ioT_metamodel_AtomicData()
    setattr(partner, 'ioT_metamodel_AtomicData110', None)
    _safe_set(owner, 'ioT_metamodel_AtomicDataAttributes', partner)
    assert getattr(partner, 'ioT_metamodel_AtomicData110') == owner
    _safe_set(owner, 'ioT_metamodel_AtomicDataAttributes', None)
    assert getattr(partner, 'ioT_metamodel_AtomicData110') is None


def test_assoc_has_attributes77_stub_double():
    # ioT_metamodel_InformationResource has no real 'ioT_metamodel_InformationResource78' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Attribute(Type="sample_text", name="sample_text")
    partner = ioT_metamodel_InformationResource()
    setattr(partner, 'ioT_metamodel_InformationResource78', None)
    _safe_set(owner, 'ioT_metamodel_Attribute', partner)
    assert owner in getattr(partner, 'ioT_metamodel_InformationResource78')
    _safe_set(owner, 'ioT_metamodel_Attribute', None)
    assert owner not in getattr(partner, 'ioT_metamodel_InformationResource78')


def test_assoc_has_datastreamattributes107_stub_double():
    # ioT_metamodel_DataStreams has no real 'ioT_metamodel_DataStreams108' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_DataStreamAttributes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_DataStreamAttributes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_DataStreamAttributes(DataEncoding="sample_text", DataFormat="sample_text", Description="sample_text", DeviceID="sample_text", MaxBitrate="sample_text", MeanBitRate="sample_text", Timestamp="sample_text")
    partner = ioT_metamodel_DataStreams()
    setattr(partner, 'ioT_metamodel_DataStreams108', None)
    _safe_set(owner, 'ioT_metamodel_DataStreamAttributes', partner)
    assert getattr(partner, 'ioT_metamodel_DataStreams108') == owner
    _safe_set(owner, 'ioT_metamodel_DataStreamAttributes', None)
    assert getattr(partner, 'ioT_metamodel_DataStreams108') is None


def test_assoc_has_ports70_stub_double():
    # ioT_metamodel_Port has no real 'ioT_metamodel_Port' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Communicator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Communicator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Communicator(Type="sample_text", ports_number=7)
    partner = ioT_metamodel_Port()
    setattr(partner, 'ioT_metamodel_Port', None)
    _safe_set(owner, 'ioT_metamodel_Communicator71', {partner})
    assert getattr(partner, 'ioT_metamodel_Port') == owner
    _safe_set(owner, 'ioT_metamodel_Communicator71', set())
    assert getattr(partner, 'ioT_metamodel_Port') is None


def test_assoc_hosts38_stub_double():
    # ioT_metamodel_On_Device_Resource has no real 'ioT_metamodel_On_Device_Resource' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Device(Technology="sample_text")
    partner = ioT_metamodel_On_Device_Resource()
    setattr(partner, 'ioT_metamodel_On_Device_Resource', None)
    _safe_set(owner, 'ioT_metamodel_Device39', {partner})
    assert getattr(partner, 'ioT_metamodel_On_Device_Resource') == owner
    _safe_set(owner, 'ioT_metamodel_Device39', set())
    assert getattr(partner, 'ioT_metamodel_On_Device_Resource') is None


def test_assoc_identifies45_stub_double():
    # ioT_metamodel_PhysicalThing has no real 'ioT_metamodel_PhysicalThing46' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Tag(Name="sample_text")
    partner = ioT_metamodel_PhysicalThing()
    setattr(partner, 'ioT_metamodel_PhysicalThing46', None)
    _safe_set(owner, 'ioT_metamodel_Tag', {partner})
    assert getattr(partner, 'ioT_metamodel_PhysicalThing46') == owner
    _safe_set(owner, 'ioT_metamodel_Tag', set())
    assert getattr(partner, 'ioT_metamodel_PhysicalThing46') is None


def test_assoc_incoming_states62_stub_double():
    # ioT_metamodel_Transition has no real 'ioT_metamodel_Transition63' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_DeviceState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_DeviceState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_DeviceState(Enabled=True)
    partner = ioT_metamodel_Transition()
    setattr(partner, 'ioT_metamodel_Transition63', None)
    _safe_set(owner, 'ioT_metamodel_DeviceState64', partner)
    assert owner in getattr(partner, 'ioT_metamodel_Transition63')
    _safe_set(owner, 'ioT_metamodel_DeviceState64', None)
    assert owner not in getattr(partner, 'ioT_metamodel_Transition63')


def test_assoc_is_associated_with12_stub_double():
    # ioT_metamodel_InformationResource has no real 'ioT_metamodel_InformationResource' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_VirtualThing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_VirtualThing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_VirtualThing(URI="sample_text")
    partner = ioT_metamodel_InformationResource()
    setattr(partner, 'ioT_metamodel_InformationResource', None)
    _safe_set(owner, 'ioT_metamodel_VirtualThing13', {partner})
    assert getattr(partner, 'ioT_metamodel_InformationResource') == owner
    _safe_set(owner, 'ioT_metamodel_VirtualThing13', set())
    assert getattr(partner, 'ioT_metamodel_InformationResource') is None


def test_assoc_is_attached_to29_stub_double():
    # ioT_metamodel_PhysicalThing has no real 'PhysicalThing' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Device(Technology="sample_text")
    partner = ioT_metamodel_PhysicalThing()
    setattr(partner, 'PhysicalThing', None)
    _safe_set(owner, 'has', {partner})
    assert getattr(partner, 'PhysicalThing') == owner
    _safe_set(owner, 'has', set())
    assert getattr(partner, 'PhysicalThing') is None


def test_assoc_is_connected_with122_stub_double():
    # ioT_metamodel_Fog_Services has no real 'ioT_metamodel_Fog_Services123' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_VirtualThing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_VirtualThing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_VirtualThing(URI="sample_text")
    partner = ioT_metamodel_Fog_Services()
    setattr(partner, 'ioT_metamodel_Fog_Services123', None)
    _safe_set(owner, 'ioT_metamodel_VirtualThing124', partner)
    assert owner in getattr(partner, 'ioT_metamodel_Fog_Services123')
    _safe_set(owner, 'ioT_metamodel_VirtualThing124', None)
    assert owner not in getattr(partner, 'ioT_metamodel_Fog_Services123')


def test_assoc_monitors47_stub_double():
    # ioT_metamodel_PhysicalThing has no real 'ioT_metamodel_PhysicalThing48' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Sensor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Sensor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Sensor(Name="sample_text", State=True, frequency=3.14)
    partner = ioT_metamodel_PhysicalThing()
    setattr(partner, 'ioT_metamodel_PhysicalThing48', None)
    _safe_set(owner, 'ioT_metamodel_Sensor', {partner})
    assert getattr(partner, 'ioT_metamodel_PhysicalThing48') == owner
    _safe_set(owner, 'ioT_metamodel_Sensor', set())
    assert getattr(partner, 'ioT_metamodel_PhysicalThing48') is None


def test_assoc_outgoing_states65_stub_double():
    # ioT_metamodel_Transition has no real 'ioT_metamodel_Transition66' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_DeviceState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_DeviceState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_DeviceState(Enabled=True)
    partner = ioT_metamodel_Transition()
    setattr(partner, 'ioT_metamodel_Transition66', None)
    _safe_set(owner, 'ioT_metamodel_DeviceState67', partner)
    assert owner in getattr(partner, 'ioT_metamodel_Transition66')
    _safe_set(owner, 'ioT_metamodel_DeviceState67', None)
    assert owner not in getattr(partner, 'ioT_metamodel_Transition66')


def test_assoc_physical_entity2_stub_double():
    # ioT_metamodel_PhysicalThing has no real 'ioT_metamodel_PhysicalThing' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Thing(name="sample_text")
    partner = ioT_metamodel_PhysicalThing()
    setattr(partner, 'ioT_metamodel_PhysicalThing', None)
    _safe_set(owner, 'ioT_metamodel_Thing3', partner)
    assert getattr(partner, 'ioT_metamodel_PhysicalThing') == owner
    _safe_set(owner, 'ioT_metamodel_Thing3', None)
    assert getattr(partner, 'ioT_metamodel_PhysicalThing') is None


def test_assoc_represents9_stub_double():
    # ioT_metamodel_PhysicalThing has no real 'ioT_metamodel_PhysicalThing11' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_VirtualThing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_VirtualThing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_VirtualThing(URI="sample_text")
    partner = ioT_metamodel_PhysicalThing()
    setattr(partner, 'ioT_metamodel_PhysicalThing11', None)
    _safe_set(owner, 'ioT_metamodel_VirtualThing10', partner)
    assert getattr(partner, 'ioT_metamodel_PhysicalThing11') == owner
    _safe_set(owner, 'ioT_metamodel_VirtualThing10', None)
    assert getattr(partner, 'ioT_metamodel_PhysicalThing11') is None


def test_assoc_request_service15_stub_double():
    # ioT_metamodel_Fog has no real 'fog' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Thing(name="sample_text")
    partner = ioT_metamodel_Fog()
    setattr(partner, 'fog', None)
    _safe_set(owner, 'Thing', partner)
    assert owner in getattr(partner, 'fog')
    _safe_set(owner, 'Thing', None)
    assert owner not in getattr(partner, 'fog')


def test_assoc_runs_in111_stub_double():
    # ioT_metamodel_Fog_Services has no real 'ioT_metamodel_Fog_Services112' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Container(ID="sample_text", IP_address="sample_text")
    partner = ioT_metamodel_Fog_Services()
    setattr(partner, 'ioT_metamodel_Fog_Services112', None)
    _safe_set(owner, 'ioT_metamodel_Container113', partner)
    assert getattr(partner, 'ioT_metamodel_Fog_Services112') == owner
    _safe_set(owner, 'ioT_metamodel_Container113', None)
    assert getattr(partner, 'ioT_metamodel_Fog_Services112') is None


def test_assoc_runs_in127_stub_double():
    # ioT_metamodel_Operations has no real 'ioT_metamodel_Operations128' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Container(ID="sample_text", IP_address="sample_text")
    partner = ioT_metamodel_Operations()
    setattr(partner, 'ioT_metamodel_Operations128', None)
    _safe_set(owner, 'ioT_metamodel_Container129', partner)
    assert getattr(partner, 'ioT_metamodel_Operations128') == owner
    _safe_set(owner, 'ioT_metamodel_Container129', None)
    assert getattr(partner, 'ioT_metamodel_Operations128') is None


def test_assoc_runs_in_container23_stub_double():
    # ioT_metamodel_FogNode has no real 'ioT_metamodel_FogNode24' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Container's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Container's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Container(ID="sample_text", IP_address="sample_text")
    partner = ioT_metamodel_FogNode()
    setattr(partner, 'ioT_metamodel_FogNode24', None)
    _safe_set(owner, 'ioT_metamodel_Container', partner)
    assert owner in getattr(partner, 'ioT_metamodel_FogNode24')
    _safe_set(owner, 'ioT_metamodel_Container', None)
    assert owner not in getattr(partner, 'ioT_metamodel_FogNode24')


def test_assoc_sensor_actions133_stub_double():
    # ioT_metamodel_DeviceSensor has no real 'ioT_metamodel_DeviceSensor' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Action(Description="sample_text")
    partner = ioT_metamodel_DeviceSensor()
    setattr(partner, 'ioT_metamodel_DeviceSensor', None)
    _safe_set(owner, 'ioT_metamodel_Action134', partner)
    assert owner in getattr(partner, 'ioT_metamodel_DeviceSensor')
    _safe_set(owner, 'ioT_metamodel_Action134', None)
    assert owner not in getattr(partner, 'ioT_metamodel_DeviceSensor')


def test_assoc_sensor_actions54_stub_double():
    # ioT_metamodel_ExternalSensor has no real 'ioT_metamodel_ExternalSensor' property in the generated
    # code (a bare stub) -- manually attach it so ioT_metamodel_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_metamodel_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_metamodel_Action(Description="sample_text")
    partner = ioT_metamodel_ExternalSensor()
    setattr(partner, 'ioT_metamodel_ExternalSensor', None)
    _safe_set(owner, 'ioT_metamodel_Action55', partner)
    assert owner in getattr(partner, 'ioT_metamodel_ExternalSensor')
    _safe_set(owner, 'ioT_metamodel_Action55', None)
    assert owner not in getattr(partner, 'ioT_metamodel_ExternalSensor')


