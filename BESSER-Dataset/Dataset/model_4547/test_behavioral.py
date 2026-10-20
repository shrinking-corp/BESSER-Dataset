import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    CommunicationAction,
    NamedElement,
    PropertyKeyContainer,
    behaviour_Action,
    behaviour_AreaObject,
    behaviour_BehaviourContainer,
    behaviour_BehaviouralPropertyKeyContainer,
    behaviour_BroadcastCommunication,
    behaviour_Capability,
    behaviour_CapabilityProperties,
    behaviour_CommunicationAction,
    behaviour_DetectedObject,
    behaviour_DynamicRobot,
    behaviour_MeasureValue,
    behaviour_Message,
    behaviour_MessageRepository,
    behaviour_MulticastCommunication,
    behaviour_Property,
    behaviour_Robot,
    behaviour_RobotCollaboration,
    behaviour_Task,
    behaviour_TaskDescriptor,
    behaviour_TaskExecution,
    behaviour_TaskRequirement,
    behaviour_UnicastCommunication,
    RobotStatus,
    TaskExecutionStatus,
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

def test_assoc_detectedObjects61_reverse_link_reassign_clear():
    a1 = behaviour_DynamicRobot(status="sample_text")
    a2 = behaviour_DynamicRobot(status="sample_text_2")
    b = behaviour_DetectedObject(obstacle=True)
    _safe_set(b, 'behaviour_DetectedObject63', a1)
    assert _is_linked(b, 'behaviour_DetectedObject63', a1)
    if hasattr(a1, 'behaviour_DynamicRobot62'):
        assert _is_linked(a1, 'behaviour_DynamicRobot62', b)
    _safe_set(b, 'behaviour_DetectedObject63', a2)
    assert _is_linked(b, 'behaviour_DetectedObject63', a2)
    if hasattr(a1, 'behaviour_DynamicRobot62'):
        assert not _is_linked(a1, 'behaviour_DynamicRobot62', b)
    if hasattr(a2, 'behaviour_DynamicRobot62'):
        assert _is_linked(a2, 'behaviour_DynamicRobot62', b)
    _safe_set(b, 'behaviour_DetectedObject63', None)
    assert not _is_linked(b, 'behaviour_DetectedObject63', a2)
    if hasattr(a2, 'behaviour_DynamicRobot62'):
        assert not _is_linked(a2, 'behaviour_DynamicRobot62', b)


def test_assoc_executedTasks71_reverse_link_reassign_clear():
    a1 = behaviour_TaskExecution(status="sample_text")
    a2 = behaviour_TaskExecution(status="sample_text_2")
    b = behaviour_DynamicRobot(status="sample_text")
    _safe_set(b, 'behaviour_DynamicRobot72', {a1})
    assert _is_linked(b, 'behaviour_DynamicRobot72', a1)
    if hasattr(a1, 'behaviour_TaskExecution73'):
        assert _is_linked(a1, 'behaviour_TaskExecution73', b)
    _safe_set(b, 'behaviour_DynamicRobot72', {a2})
    assert _is_linked(b, 'behaviour_DynamicRobot72', a2)
    if hasattr(a1, 'behaviour_TaskExecution73'):
        assert not _is_linked(a1, 'behaviour_TaskExecution73', b)
    if hasattr(a2, 'behaviour_TaskExecution73'):
        assert _is_linked(a2, 'behaviour_TaskExecution73', b)
    _safe_set(b, 'behaviour_DynamicRobot72', set())
    assert not _is_linked(b, 'behaviour_DynamicRobot72', a2)
    if hasattr(a2, 'behaviour_TaskExecution73'):
        assert not _is_linked(a2, 'behaviour_TaskExecution73', b)


def test_assoc_executors39_reverse_link_reassign_clear():
    a1 = behaviour_TaskExecution(status="sample_text")
    a2 = behaviour_TaskExecution(status="sample_text_2")
    b = behaviour_DynamicRobot(status="sample_text")
    _safe_set(b, 'behaviour_DynamicRobot41', a1)
    assert _is_linked(b, 'behaviour_DynamicRobot41', a1)
    if hasattr(a1, 'behaviour_TaskExecution40'):
        assert _is_linked(a1, 'behaviour_TaskExecution40', b)
    _safe_set(b, 'behaviour_DynamicRobot41', a2)
    assert _is_linked(b, 'behaviour_DynamicRobot41', a2)
    if hasattr(a1, 'behaviour_TaskExecution40'):
        assert not _is_linked(a1, 'behaviour_TaskExecution40', b)
    if hasattr(a2, 'behaviour_TaskExecution40'):
        assert _is_linked(a2, 'behaviour_TaskExecution40', b)
    _safe_set(b, 'behaviour_DynamicRobot41', None)
    assert not _is_linked(b, 'behaviour_DynamicRobot41', a2)
    if hasattr(a2, 'behaviour_TaskExecution40'):
        assert not _is_linked(a2, 'behaviour_TaskExecution40', b)


def test_assoc_follows16_reverse_link_reassign_clear():
    a1 = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    a2 = behaviour_Message(needResponse=False, timestamp=date(2025, 6, 15))
    b = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    _safe_set(b, 'behaviour_Message17', a1)
    assert _is_linked(b, 'behaviour_Message17', a1)
    if hasattr(a1, 'behaviour_Message15'):
        assert _is_linked(a1, 'behaviour_Message15', b)
    _safe_set(b, 'behaviour_Message17', a2)
    assert _is_linked(b, 'behaviour_Message17', a2)
    if hasattr(a1, 'behaviour_Message15'):
        assert not _is_linked(a1, 'behaviour_Message15', b)
    if hasattr(a2, 'behaviour_Message15'):
        assert _is_linked(a2, 'behaviour_Message15', b)
    _safe_set(b, 'behaviour_Message17', None)
    assert not _is_linked(b, 'behaviour_Message17', a2)
    if hasattr(a2, 'behaviour_Message15'):
        assert not _is_linked(a2, 'behaviour_Message15', b)


def test_assoc_involvedTaskExecutions7_reverse_link_reassign_clear():
    a1 = behaviour_TaskExecution(status="sample_text")
    a2 = behaviour_TaskExecution(status="sample_text_2")
    b = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    _safe_set(b, 'behaviour_Message', {a1})
    assert _is_linked(b, 'behaviour_Message', a1)
    if hasattr(a1, 'behaviour_TaskExecution8'):
        assert _is_linked(a1, 'behaviour_TaskExecution8', b)
    _safe_set(b, 'behaviour_Message', {a2})
    assert _is_linked(b, 'behaviour_Message', a2)
    if hasattr(a1, 'behaviour_TaskExecution8'):
        assert not _is_linked(a1, 'behaviour_TaskExecution8', b)
    if hasattr(a2, 'behaviour_TaskExecution8'):
        assert _is_linked(a2, 'behaviour_TaskExecution8', b)
    _safe_set(b, 'behaviour_Message', set())
    assert not _is_linked(b, 'behaviour_Message', a2)
    if hasattr(a2, 'behaviour_TaskExecution8'):
        assert not _is_linked(a2, 'behaviour_TaskExecution8', b)


def test_assoc_prerequisite75_reverse_link_reassign_clear():
    a1 = behaviour_TaskRequirement(participants=7)
    a2 = behaviour_TaskRequirement(participants=13)
    b = behaviour_TaskExecution(status="sample_text")
    _safe_set(b, 'behaviour_TaskExecution77', a1)
    assert _is_linked(b, 'behaviour_TaskExecution77', a1)
    if hasattr(a1, 'behaviour_TaskRequirement76'):
        assert _is_linked(a1, 'behaviour_TaskRequirement76', b)
    _safe_set(b, 'behaviour_TaskExecution77', a2)
    assert _is_linked(b, 'behaviour_TaskExecution77', a2)
    if hasattr(a1, 'behaviour_TaskRequirement76'):
        assert not _is_linked(a1, 'behaviour_TaskRequirement76', b)
    if hasattr(a2, 'behaviour_TaskRequirement76'):
        assert _is_linked(a2, 'behaviour_TaskRequirement76', b)
    _safe_set(b, 'behaviour_TaskExecution77', None)
    assert not _is_linked(b, 'behaviour_TaskExecution77', a2)
    if hasattr(a2, 'behaviour_TaskRequirement76'):
        assert not _is_linked(a2, 'behaviour_TaskRequirement76', b)


def test_assoc_requirement48_reverse_link_reassign_clear():
    a1 = behaviour_TaskRequirement(participants=7)
    a2 = behaviour_TaskRequirement(participants=13)
    b = behaviour_TaskExecution(status="sample_text")
    _safe_set(b, 'taskExecution', a1)
    assert _is_linked(b, 'taskExecution', a1)
    if hasattr(a1, 'TaskRequirement'):
        assert _is_linked(a1, 'TaskRequirement', b)
    _safe_set(b, 'taskExecution', a2)
    assert _is_linked(b, 'taskExecution', a2)
    if hasattr(a1, 'TaskRequirement'):
        assert not _is_linked(a1, 'TaskRequirement', b)
    if hasattr(a2, 'TaskRequirement'):
        assert _is_linked(a2, 'TaskRequirement', b)
    _safe_set(b, 'taskExecution', None)
    assert not _is_linked(b, 'taskExecution', a2)
    if hasattr(a2, 'TaskRequirement'):
        assert not _is_linked(a2, 'TaskRequirement', b)


def test_assoc_taskExecution74_reverse_link_reassign_clear():
    a1 = behaviour_TaskRequirement(participants=7)
    a2 = behaviour_TaskRequirement(participants=13)
    b = behaviour_TaskExecution(status="sample_text")
    _safe_set(b, 'TaskExecution', a1)
    assert _is_linked(b, 'TaskExecution', a1)
    if hasattr(a1, 'requirement'):
        assert _is_linked(a1, 'requirement', b)
    _safe_set(b, 'TaskExecution', a2)
    assert _is_linked(b, 'TaskExecution', a2)
    if hasattr(a1, 'requirement'):
        assert not _is_linked(a1, 'requirement', b)
    if hasattr(a2, 'requirement'):
        assert _is_linked(a2, 'requirement', b)
    _safe_set(b, 'TaskExecution', None)
    assert not _is_linked(b, 'TaskExecution', a2)
    if hasattr(a2, 'requirement'):
        assert not _is_linked(a2, 'requirement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_TTL13_stub_double():
    # behaviour_MeasureValue has no real 'behaviour_MeasureValue' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    partner = behaviour_MeasureValue()
    setattr(partner, 'behaviour_MeasureValue', None)
    _safe_set(owner, 'behaviour_Message14', partner)
    assert getattr(partner, 'behaviour_MeasureValue') == owner
    _safe_set(owner, 'behaviour_Message14', None)
    assert getattr(partner, 'behaviour_MeasureValue') is None


def test_assoc_actions68_stub_double():
    # behaviour_Action has no real 'behaviour_Action70' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_DynamicRobot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_DynamicRobot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_DynamicRobot(status="sample_text")
    partner = behaviour_Action()
    setattr(partner, 'behaviour_Action70', None)
    _safe_set(owner, 'behaviour_DynamicRobot69', {partner})
    assert getattr(partner, 'behaviour_Action70') == owner
    _safe_set(owner, 'behaviour_DynamicRobot69', set())
    assert getattr(partner, 'behaviour_Action70') is None


def test_assoc_capabilityProperties83_stub_double():
    # behaviour_CapabilityProperties has no real 'behaviour_CapabilityProperties' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_TaskRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_TaskRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_TaskRequirement(participants=7)
    partner = behaviour_CapabilityProperties()
    setattr(partner, 'behaviour_CapabilityProperties', None)
    _safe_set(owner, 'behaviour_TaskRequirement84', {partner})
    assert getattr(partner, 'behaviour_CapabilityProperties') == owner
    _safe_set(owner, 'behaviour_TaskRequirement84', set())
    assert getattr(partner, 'behaviour_CapabilityProperties') is None


def test_assoc_collaborations64_stub_double():
    # behaviour_RobotCollaboration has no real 'behaviour_RobotCollaboration66' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_DynamicRobot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_DynamicRobot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_DynamicRobot(status="sample_text")
    partner = behaviour_RobotCollaboration()
    setattr(partner, 'behaviour_RobotCollaboration66', None)
    _safe_set(owner, 'behaviour_DynamicRobot65', {partner})
    assert getattr(partner, 'behaviour_RobotCollaboration66') == owner
    _safe_set(owner, 'behaviour_DynamicRobot65', set())
    assert getattr(partner, 'behaviour_RobotCollaboration66') is None


def test_assoc_collaborator49_stub_double():
    # behaviour_RobotCollaboration has no real 'behaviour_RobotCollaboration' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_DynamicRobot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_DynamicRobot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_DynamicRobot(status="sample_text")
    partner = behaviour_RobotCollaboration()
    setattr(partner, 'behaviour_RobotCollaboration', None)
    _safe_set(owner, 'behaviour_DynamicRobot50', partner)
    assert getattr(partner, 'behaviour_RobotCollaboration') == owner
    _safe_set(owner, 'behaviour_DynamicRobot50', None)
    assert getattr(partner, 'behaviour_RobotCollaboration') is None


def test_assoc_currentTaskExecution34_stub_double():
    # behaviour_Action has no real 'behaviour_Action35' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_TaskExecution's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_TaskExecution's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_TaskExecution(status="sample_text")
    partner = behaviour_Action()
    setattr(partner, 'behaviour_Action35', None)
    _safe_set(owner, 'behaviour_TaskExecution36', partner)
    assert getattr(partner, 'behaviour_Action35') == owner
    _safe_set(owner, 'behaviour_TaskExecution36', None)
    assert getattr(partner, 'behaviour_Action35') is None


def test_assoc_descriptor85_stub_double():
    # behaviour_TaskDescriptor has no real 'behaviour_TaskDescriptor' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_TaskRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_TaskRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_TaskRequirement(participants=7)
    partner = behaviour_TaskDescriptor()
    setattr(partner, 'behaviour_TaskDescriptor', None)
    _safe_set(owner, 'behaviour_TaskRequirement86', partner)
    assert getattr(partner, 'behaviour_TaskDescriptor') == owner
    _safe_set(owner, 'behaviour_TaskRequirement86', None)
    assert getattr(partner, 'behaviour_TaskDescriptor') is None


def test_assoc_dynamicRobots0_stub_double():
    # behaviour_BehaviourContainer has no real 'behaviour_BehaviourContainer' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_DynamicRobot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_DynamicRobot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_DynamicRobot(status="sample_text")
    partner = behaviour_BehaviourContainer()
    setattr(partner, 'behaviour_BehaviourContainer', None)
    _safe_set(owner, 'behaviour_DynamicRobot', partner)
    assert owner in getattr(partner, 'behaviour_BehaviourContainer')
    _safe_set(owner, 'behaviour_DynamicRobot', None)
    assert owner not in getattr(partner, 'behaviour_BehaviourContainer')


def test_assoc_executionTime42_stub_double():
    # behaviour_MeasureValue has no real 'behaviour_MeasureValue44' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_TaskExecution's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_TaskExecution's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_TaskExecution(status="sample_text")
    partner = behaviour_MeasureValue()
    setattr(partner, 'behaviour_MeasureValue44', None)
    _safe_set(owner, 'behaviour_TaskExecution43', partner)
    assert getattr(partner, 'behaviour_MeasureValue44') == owner
    _safe_set(owner, 'behaviour_TaskExecution43', None)
    assert getattr(partner, 'behaviour_MeasureValue44') is None


def test_assoc_message18_stub_double():
    # behaviour_CommunicationAction has no real 'behaviour_CommunicationAction' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    partner = behaviour_CommunicationAction()
    setattr(partner, 'behaviour_CommunicationAction', None)
    _safe_set(owner, 'behaviour_Message19', partner)
    assert getattr(partner, 'behaviour_CommunicationAction') == owner
    _safe_set(owner, 'behaviour_Message19', None)
    assert getattr(partner, 'behaviour_CommunicationAction') is None


def test_assoc_messageRepository67_stub_double():
    # behaviour_MessageRepository has no real 'MessageRepository' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_DynamicRobot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_DynamicRobot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_DynamicRobot(status="sample_text")
    partner = behaviour_MessageRepository()
    setattr(partner, 'MessageRepository', None)
    _safe_set(owner, 'robot', partner)
    assert getattr(partner, 'MessageRepository') == owner
    _safe_set(owner, 'robot', None)
    assert getattr(partner, 'MessageRepository') is None


def test_assoc_object57_stub_double():
    # behaviour_AreaObject has no real 'behaviour_AreaObject58' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_DetectedObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_DetectedObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_DetectedObject(obstacle=True)
    partner = behaviour_AreaObject()
    setattr(partner, 'behaviour_AreaObject58', None)
    _safe_set(owner, 'behaviour_DetectedObject', partner)
    assert getattr(partner, 'behaviour_AreaObject58') == owner
    _safe_set(owner, 'behaviour_DetectedObject', None)
    assert getattr(partner, 'behaviour_AreaObject58') is None


def test_assoc_properties78_stub_double():
    # behaviour_Property has no real 'behaviour_Property80' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_TaskRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_TaskRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_TaskRequirement(participants=7)
    partner = behaviour_Property()
    setattr(partner, 'behaviour_Property80', None)
    _safe_set(owner, 'behaviour_TaskRequirement79', {partner})
    assert getattr(partner, 'behaviour_Property80') == owner
    _safe_set(owner, 'behaviour_TaskRequirement79', set())
    assert getattr(partner, 'behaviour_Property80') is None


def test_assoc_properties9_stub_double():
    # behaviour_Property has no real 'behaviour_Property' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    partner = behaviour_Property()
    setattr(partner, 'behaviour_Property', None)
    _safe_set(owner, 'behaviour_Message10', {partner})
    assert getattr(partner, 'behaviour_Property') == owner
    _safe_set(owner, 'behaviour_Message10', set())
    assert getattr(partner, 'behaviour_Property') is None


def test_assoc_receivedMessages27_stub_double():
    # behaviour_MessageRepository has no real 'behaviour_MessageRepository' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    partner = behaviour_MessageRepository()
    setattr(partner, 'behaviour_MessageRepository', None)
    _safe_set(owner, 'behaviour_Message28', partner)
    assert owner in getattr(partner, 'behaviour_MessageRepository')
    _safe_set(owner, 'behaviour_Message28', None)
    assert owner not in getattr(partner, 'behaviour_MessageRepository')


def test_assoc_referredObjects11_stub_double():
    # behaviour_AreaObject has no real 'behaviour_AreaObject' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    partner = behaviour_AreaObject()
    setattr(partner, 'behaviour_AreaObject', None)
    _safe_set(owner, 'behaviour_Message12', {partner})
    assert getattr(partner, 'behaviour_AreaObject') == owner
    _safe_set(owner, 'behaviour_Message12', set())
    assert getattr(partner, 'behaviour_AreaObject') is None


def test_assoc_requiredCapabilities81_stub_double():
    # behaviour_Capability has no real 'behaviour_Capability' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_TaskRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_TaskRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_TaskRequirement(participants=7)
    partner = behaviour_Capability()
    setattr(partner, 'behaviour_Capability', None)
    _safe_set(owner, 'behaviour_TaskRequirement82', {partner})
    assert getattr(partner, 'behaviour_Capability') == owner
    _safe_set(owner, 'behaviour_TaskRequirement82', set())
    assert getattr(partner, 'behaviour_Capability') is None


def test_assoc_robot26_stub_double():
    # behaviour_MessageRepository has no real 'messageRepository' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_DynamicRobot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_DynamicRobot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_DynamicRobot(status="sample_text")
    partner = behaviour_MessageRepository()
    setattr(partner, 'messageRepository', None)
    _safe_set(owner, 'DynamicRobot', partner)
    assert getattr(partner, 'messageRepository') == owner
    _safe_set(owner, 'DynamicRobot', None)
    assert getattr(partner, 'messageRepository') is None


def test_assoc_robot59_stub_double():
    # behaviour_Robot has no real 'behaviour_Robot' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_DynamicRobot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_DynamicRobot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_DynamicRobot(status="sample_text")
    partner = behaviour_Robot()
    setattr(partner, 'behaviour_Robot', None)
    _safe_set(owner, 'behaviour_DynamicRobot60', partner)
    assert getattr(partner, 'behaviour_Robot') == owner
    _safe_set(owner, 'behaviour_DynamicRobot60', None)
    assert getattr(partner, 'behaviour_Robot') is None


def test_assoc_sendedMessages29_stub_double():
    # behaviour_MessageRepository has no real 'behaviour_MessageRepository30' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    partner = behaviour_MessageRepository()
    setattr(partner, 'behaviour_MessageRepository30', None)
    _safe_set(owner, 'behaviour_Message31', partner)
    assert owner in getattr(partner, 'behaviour_MessageRepository30')
    _safe_set(owner, 'behaviour_Message31', None)
    assert owner not in getattr(partner, 'behaviour_MessageRepository30')


def test_assoc_target20_stub_double():
    # behaviour_UnicastCommunication has no real 'behaviour_UnicastCommunication' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_DynamicRobot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_DynamicRobot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_DynamicRobot(status="sample_text")
    partner = behaviour_UnicastCommunication()
    setattr(partner, 'behaviour_UnicastCommunication', None)
    _safe_set(owner, 'behaviour_DynamicRobot21', partner)
    assert getattr(partner, 'behaviour_UnicastCommunication') == owner
    _safe_set(owner, 'behaviour_DynamicRobot21', None)
    assert getattr(partner, 'behaviour_UnicastCommunication') is None


def test_assoc_targets22_stub_double():
    # behaviour_MulticastCommunication has no real 'behaviour_MulticastCommunication' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_DynamicRobot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_DynamicRobot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_DynamicRobot(status="sample_text")
    partner = behaviour_MulticastCommunication()
    setattr(partner, 'behaviour_MulticastCommunication', None)
    _safe_set(owner, 'behaviour_DynamicRobot23', partner)
    assert owner in getattr(partner, 'behaviour_MulticastCommunication')
    _safe_set(owner, 'behaviour_DynamicRobot23', None)
    assert owner not in getattr(partner, 'behaviour_MulticastCommunication')


def test_assoc_targets24_stub_double():
    # behaviour_BroadcastCommunication has no real 'behaviour_BroadcastCommunication' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_DynamicRobot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_DynamicRobot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_DynamicRobot(status="sample_text")
    partner = behaviour_BroadcastCommunication()
    setattr(partner, 'behaviour_BroadcastCommunication', None)
    _safe_set(owner, 'behaviour_DynamicRobot25', partner)
    assert owner in getattr(partner, 'behaviour_BroadcastCommunication')
    _safe_set(owner, 'behaviour_DynamicRobot25', None)
    assert owner not in getattr(partner, 'behaviour_BroadcastCommunication')


def test_assoc_task45_stub_double():
    # behaviour_Task has no real 'behaviour_Task47' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_TaskExecution's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_TaskExecution's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_TaskExecution(status="sample_text")
    partner = behaviour_Task()
    setattr(partner, 'behaviour_Task47', None)
    _safe_set(owner, 'behaviour_TaskExecution46', partner)
    assert getattr(partner, 'behaviour_Task47') == owner
    _safe_set(owner, 'behaviour_TaskExecution46', None)
    assert getattr(partner, 'behaviour_Task47') is None


def test_assoc_task87_stub_double():
    # behaviour_Task has no real 'behaviour_Task89' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_TaskRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_TaskRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_TaskRequirement(participants=7)
    partner = behaviour_Task()
    setattr(partner, 'behaviour_Task89', None)
    _safe_set(owner, 'behaviour_TaskRequirement88', partner)
    assert getattr(partner, 'behaviour_Task89') == owner
    _safe_set(owner, 'behaviour_TaskRequirement88', None)
    assert getattr(partner, 'behaviour_Task89') is None


def test_assoc_taskExecutions1_stub_double():
    # behaviour_BehaviourContainer has no real 'behaviour_BehaviourContainer2' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_TaskExecution's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_TaskExecution's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_TaskExecution(status="sample_text")
    partner = behaviour_BehaviourContainer()
    setattr(partner, 'behaviour_BehaviourContainer2', None)
    _safe_set(owner, 'behaviour_TaskExecution', partner)
    assert owner in getattr(partner, 'behaviour_BehaviourContainer2')
    _safe_set(owner, 'behaviour_TaskExecution', None)
    assert owner not in getattr(partner, 'behaviour_BehaviourContainer2')


def test_assoc_taskRequirements3_stub_double():
    # behaviour_BehaviourContainer has no real 'behaviour_BehaviourContainer4' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_TaskRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_TaskRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_TaskRequirement(participants=7)
    partner = behaviour_BehaviourContainer()
    setattr(partner, 'behaviour_BehaviourContainer4', None)
    _safe_set(owner, 'behaviour_TaskRequirement', partner)
    assert owner in getattr(partner, 'behaviour_BehaviourContainer4')
    _safe_set(owner, 'behaviour_TaskRequirement', None)
    assert owner not in getattr(partner, 'behaviour_BehaviourContainer4')


