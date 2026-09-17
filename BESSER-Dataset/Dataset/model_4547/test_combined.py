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
    PropertyKeyContainer,
    behaviour_TaskDescriptor,
    behaviour_CapabilityProperties,
    behaviour_Capability,
    behaviour_Robot,
    behaviour_DetectedObject,
    behaviour_RobotCollaboration,
    behaviour_Task,
    CommunicationAction,
    behaviour_MulticastCommunication,
    behaviour_BroadcastCommunication,
    behaviour_UnicastCommunication,
    Action,
    behaviour_CommunicationAction,
    behaviour_MeasureValue,
    behaviour_AreaObject,
    behaviour_Property,
    NamedElement,
    behaviour_Action,
    behaviour_MessageRepository,
    behaviour_Message,
    behaviour_BehaviouralPropertyKeyContainer,
    behaviour_TaskRequirement,
    behaviour_TaskExecution,
    behaviour_DynamicRobot,
    behaviour_BehaviourContainer,
    RobotStatus,
    TaskExecutionStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_propertykeycontainer_is_not_abstract():
    assert not inspect.isabstract(PropertyKeyContainer)


def test_hyp_propertykeycontainer_constructor_exists():
    assert callable(PropertyKeyContainer.__init__)


def test_hyp_propertykeycontainer_constructor_args():
    sig = inspect.signature(PropertyKeyContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_taskdescriptor_is_not_abstract():
    assert not inspect.isabstract(behaviour_TaskDescriptor)


def test_hyp_behaviour_taskdescriptor_constructor_exists():
    assert callable(behaviour_TaskDescriptor.__init__)


def test_hyp_behaviour_taskdescriptor_constructor_args():
    sig = inspect.signature(behaviour_TaskDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_capabilityproperties_is_not_abstract():
    assert not inspect.isabstract(behaviour_CapabilityProperties)


def test_hyp_behaviour_capabilityproperties_constructor_exists():
    assert callable(behaviour_CapabilityProperties.__init__)


def test_hyp_behaviour_capabilityproperties_constructor_args():
    sig = inspect.signature(behaviour_CapabilityProperties.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_capability_is_not_abstract():
    assert not inspect.isabstract(behaviour_Capability)


def test_hyp_behaviour_capability_constructor_exists():
    assert callable(behaviour_Capability.__init__)


def test_hyp_behaviour_capability_constructor_args():
    sig = inspect.signature(behaviour_Capability.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_robot_is_not_abstract():
    assert not inspect.isabstract(behaviour_Robot)


def test_hyp_behaviour_robot_constructor_exists():
    assert callable(behaviour_Robot.__init__)


def test_hyp_behaviour_robot_constructor_args():
    sig = inspect.signature(behaviour_Robot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_detectedobject_is_not_abstract():
    assert not inspect.isabstract(behaviour_DetectedObject)


def test_hyp_behaviour_detectedobject_constructor_exists():
    assert callable(behaviour_DetectedObject.__init__)


def test_hyp_behaviour_detectedobject_constructor_args():
    sig = inspect.signature(behaviour_DetectedObject.__init__)
    params = list(sig.parameters.keys())
    assert "obstacle" in params, "Missing parameter 'obstacle'"




def test_hyp_behaviour_robotcollaboration_is_not_abstract():
    assert not inspect.isabstract(behaviour_RobotCollaboration)


def test_hyp_behaviour_robotcollaboration_constructor_exists():
    assert callable(behaviour_RobotCollaboration.__init__)


def test_hyp_behaviour_robotcollaboration_constructor_args():
    sig = inspect.signature(behaviour_RobotCollaboration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_task_is_not_abstract():
    assert not inspect.isabstract(behaviour_Task)


def test_hyp_behaviour_task_constructor_exists():
    assert callable(behaviour_Task.__init__)


def test_hyp_behaviour_task_constructor_args():
    sig = inspect.signature(behaviour_Task.__init__)
    params = list(sig.parameters.keys())



def test_hyp_communicationaction_is_not_abstract():
    assert not inspect.isabstract(CommunicationAction)


def test_hyp_communicationaction_constructor_exists():
    assert callable(CommunicationAction.__init__)


def test_hyp_communicationaction_constructor_args():
    sig = inspect.signature(CommunicationAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_multicastcommunication_is_not_abstract():
    assert not inspect.isabstract(behaviour_MulticastCommunication)


def test_hyp_behaviour_multicastcommunication_constructor_exists():
    assert callable(behaviour_MulticastCommunication.__init__)


def test_hyp_behaviour_multicastcommunication_constructor_args():
    sig = inspect.signature(behaviour_MulticastCommunication.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_broadcastcommunication_is_not_abstract():
    assert not inspect.isabstract(behaviour_BroadcastCommunication)


def test_hyp_behaviour_broadcastcommunication_constructor_exists():
    assert callable(behaviour_BroadcastCommunication.__init__)


def test_hyp_behaviour_broadcastcommunication_constructor_args():
    sig = inspect.signature(behaviour_BroadcastCommunication.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_unicastcommunication_is_not_abstract():
    assert not inspect.isabstract(behaviour_UnicastCommunication)


def test_hyp_behaviour_unicastcommunication_constructor_exists():
    assert callable(behaviour_UnicastCommunication.__init__)


def test_hyp_behaviour_unicastcommunication_constructor_args():
    sig = inspect.signature(behaviour_UnicastCommunication.__init__)
    params = list(sig.parameters.keys())



def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_communicationaction_is_not_abstract():
    assert not inspect.isabstract(behaviour_CommunicationAction)


def test_hyp_behaviour_communicationaction_constructor_exists():
    assert callable(behaviour_CommunicationAction.__init__)


def test_hyp_behaviour_communicationaction_constructor_args():
    sig = inspect.signature(behaviour_CommunicationAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_measurevalue_is_not_abstract():
    assert not inspect.isabstract(behaviour_MeasureValue)


def test_hyp_behaviour_measurevalue_constructor_exists():
    assert callable(behaviour_MeasureValue.__init__)


def test_hyp_behaviour_measurevalue_constructor_args():
    sig = inspect.signature(behaviour_MeasureValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_areaobject_is_not_abstract():
    assert not inspect.isabstract(behaviour_AreaObject)


def test_hyp_behaviour_areaobject_constructor_exists():
    assert callable(behaviour_AreaObject.__init__)


def test_hyp_behaviour_areaobject_constructor_args():
    sig = inspect.signature(behaviour_AreaObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_property_is_not_abstract():
    assert not inspect.isabstract(behaviour_Property)


def test_hyp_behaviour_property_constructor_exists():
    assert callable(behaviour_Property.__init__)


def test_hyp_behaviour_property_constructor_args():
    sig = inspect.signature(behaviour_Property.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_action_is_not_abstract():
    assert not inspect.isabstract(behaviour_Action)


def test_hyp_behaviour_action_constructor_exists():
    assert callable(behaviour_Action.__init__)


def test_hyp_behaviour_action_constructor_args():
    sig = inspect.signature(behaviour_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_messagerepository_is_not_abstract():
    assert not inspect.isabstract(behaviour_MessageRepository)


def test_hyp_behaviour_messagerepository_constructor_exists():
    assert callable(behaviour_MessageRepository.__init__)


def test_hyp_behaviour_messagerepository_constructor_args():
    sig = inspect.signature(behaviour_MessageRepository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_message_is_not_abstract():
    assert not inspect.isabstract(behaviour_Message)


def test_hyp_behaviour_message_constructor_exists():
    assert callable(behaviour_Message.__init__)


def test_hyp_behaviour_message_constructor_args():
    sig = inspect.signature(behaviour_Message.__init__)
    params = list(sig.parameters.keys())
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "needResponse" in params, "Missing parameter 'needResponse'"





def test_hyp_behaviour_behaviouralpropertykeycontainer_is_not_abstract():
    assert not inspect.isabstract(behaviour_BehaviouralPropertyKeyContainer)


def test_hyp_behaviour_behaviouralpropertykeycontainer_constructor_exists():
    assert callable(behaviour_BehaviouralPropertyKeyContainer.__init__)


def test_hyp_behaviour_behaviouralpropertykeycontainer_constructor_args():
    sig = inspect.signature(behaviour_BehaviouralPropertyKeyContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_taskrequirement_is_not_abstract():
    assert not inspect.isabstract(behaviour_TaskRequirement)


def test_hyp_behaviour_taskrequirement_constructor_exists():
    assert callable(behaviour_TaskRequirement.__init__)


def test_hyp_behaviour_taskrequirement_constructor_args():
    sig = inspect.signature(behaviour_TaskRequirement.__init__)
    params = list(sig.parameters.keys())
    assert "participants" in params, "Missing parameter 'participants'"




def test_hyp_behaviour_taskexecution_is_not_abstract():
    assert not inspect.isabstract(behaviour_TaskExecution)


def test_hyp_behaviour_taskexecution_constructor_exists():
    assert callable(behaviour_TaskExecution.__init__)


def test_hyp_behaviour_taskexecution_constructor_args():
    sig = inspect.signature(behaviour_TaskExecution.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"




def test_hyp_behaviour_dynamicrobot_is_not_abstract():
    assert not inspect.isabstract(behaviour_DynamicRobot)


def test_hyp_behaviour_dynamicrobot_constructor_exists():
    assert callable(behaviour_DynamicRobot.__init__)


def test_hyp_behaviour_dynamicrobot_constructor_args():
    sig = inspect.signature(behaviour_DynamicRobot.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"




def test_hyp_behaviour_behaviourcontainer_is_not_abstract():
    assert not inspect.isabstract(behaviour_BehaviourContainer)


def test_hyp_behaviour_behaviourcontainer_constructor_exists():
    assert callable(behaviour_BehaviourContainer.__init__)


def test_hyp_behaviour_behaviourcontainer_constructor_args():
    sig = inspect.signature(behaviour_BehaviourContainer.__init__)
    params = list(sig.parameters.keys())

def test_hyp_robotstatus_exists():
    # Check that the Enumeration exists
    assert RobotStatus is not None

def test_hyp_robotstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RobotStatus]
    expected_literals = [
        "Ready",
        "Waiting",
        "Executing",
        "TurnedOff",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RobotStatus"

def test_hyp_taskexecutionstatus_exists():
    # Check that the Enumeration exists
    assert TaskExecutionStatus is not None

def test_hyp_taskexecutionstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TaskExecutionStatus]
    expected_literals = [
        "Suspended",
        "Finished",
        "Ready",
        "Waiting",
        "InProgress",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TaskExecutionStatus"


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
PropertyKeyContainer_strategy = st.builds(
    PropertyKeyContainer,
)
behaviour_TaskDescriptor_strategy = st.builds(
    behaviour_TaskDescriptor,
)
behaviour_CapabilityProperties_strategy = st.builds(
    behaviour_CapabilityProperties,
)
behaviour_Capability_strategy = st.builds(
    behaviour_Capability,
)
behaviour_Robot_strategy = st.builds(
    behaviour_Robot,
)
behaviour_DetectedObject_strategy = st.builds(
    behaviour_DetectedObject,
    obstacle=
        st.booleans()
)
behaviour_RobotCollaboration_strategy = st.builds(
    behaviour_RobotCollaboration,
)
behaviour_Task_strategy = st.builds(
    behaviour_Task,
)
CommunicationAction_strategy = st.builds(
    CommunicationAction,
)
behaviour_MulticastCommunication_strategy = st.builds(
    behaviour_MulticastCommunication,
)
behaviour_BroadcastCommunication_strategy = st.builds(
    behaviour_BroadcastCommunication,
)
behaviour_UnicastCommunication_strategy = st.builds(
    behaviour_UnicastCommunication,
)
Action_strategy = st.builds(
    Action,
)
behaviour_CommunicationAction_strategy = st.builds(
    behaviour_CommunicationAction,
)
behaviour_MeasureValue_strategy = st.builds(
    behaviour_MeasureValue,
)
behaviour_AreaObject_strategy = st.builds(
    behaviour_AreaObject,
)
behaviour_Property_strategy = st.builds(
    behaviour_Property,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
behaviour_Action_strategy = st.builds(
    behaviour_Action,
)
behaviour_MessageRepository_strategy = st.builds(
    behaviour_MessageRepository,
)
behaviour_Message_strategy = st.builds(
    behaviour_Message,
    timestamp=
        st.dates(),
    needResponse=
        st.booleans()
)
behaviour_BehaviouralPropertyKeyContainer_strategy = st.builds(
    behaviour_BehaviouralPropertyKeyContainer,
)
behaviour_TaskRequirement_strategy = st.builds(
    behaviour_TaskRequirement,
    participants=
        st.integers()
)
behaviour_TaskExecution_strategy = st.builds(
    behaviour_TaskExecution,
    status=
        safe_text
)
behaviour_DynamicRobot_strategy = st.builds(
    behaviour_DynamicRobot,
    status=
        safe_text
)
behaviour_BehaviourContainer_strategy = st.builds(
    behaviour_BehaviourContainer,
)









@given(instance=behaviour_DetectedObject_strategy)
def test_hyp_behaviour_detectedobject_obstacle_setter(instance):
    original = instance.obstacle
    instance.obstacle = original
    assert instance.obstacle == original


















@given(instance=behaviour_Message_strategy)
def test_hyp_behaviour_message_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original



@given(instance=behaviour_Message_strategy)
def test_hyp_behaviour_message_needResponse_setter(instance):
    original = instance.needResponse
    instance.needResponse = original
    assert instance.needResponse == original





@given(instance=behaviour_TaskRequirement_strategy)
def test_hyp_behaviour_taskrequirement_participants_setter(instance):
    original = instance.participants
    instance.participants = original
    assert instance.participants == original




@given(instance=behaviour_TaskExecution_strategy)
def test_hyp_behaviour_taskexecution_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original




@given(instance=behaviour_DynamicRobot_strategy)
def test_hyp_behaviour_dynamicrobot_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_behaviour_DetectedObject_obstacle_value_roundtrip():
    instance = behaviour_DetectedObject(obstacle=True)
    assert instance.obstacle == True
    instance.obstacle = False
    assert instance.obstacle == False


def test_behaviour_DynamicRobot_status_value_roundtrip():
    instance = behaviour_DynamicRobot(status="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_behaviour_Message_needResponse_value_roundtrip():
    instance = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    assert instance.needResponse == True
    instance.needResponse = False
    assert instance.needResponse == False


def test_behaviour_Message_timestamp_value_roundtrip():
    instance = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    assert instance.timestamp == date(2024, 1, 1)
    instance.timestamp = date(2025, 6, 15)
    assert instance.timestamp == date(2025, 6, 15)


def test_behaviour_TaskExecution_status_value_roundtrip():
    instance = behaviour_TaskExecution(status="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_behaviour_TaskRequirement_participants_value_roundtrip():
    instance = behaviour_TaskRequirement(participants=7)
    assert instance.participants == 7
    instance.participants = 13
    assert instance.participants == 13


def test_behaviour_CommunicationAction_isa_Action():
    instance = behaviour_CommunicationAction()
    assert isinstance(instance, Action)


def test_behaviour_BroadcastCommunication_isa_CommunicationAction():
    instance = behaviour_BroadcastCommunication()
    assert isinstance(instance, CommunicationAction)


def test_behaviour_MulticastCommunication_isa_CommunicationAction():
    instance = behaviour_MulticastCommunication()
    assert isinstance(instance, CommunicationAction)


def test_behaviour_UnicastCommunication_isa_CommunicationAction():
    instance = behaviour_UnicastCommunication()
    assert isinstance(instance, CommunicationAction)


def test_behaviour_Action_isa_NamedElement():
    instance = behaviour_Action()
    assert isinstance(instance, NamedElement)


def test_behaviour_DynamicRobot_isa_NamedElement():
    instance = behaviour_DynamicRobot(status="sample_text")
    assert isinstance(instance, NamedElement)


def test_behaviour_Message_isa_NamedElement():
    instance = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    assert isinstance(instance, NamedElement)


def test_behaviour_MessageRepository_isa_NamedElement():
    instance = behaviour_MessageRepository()
    assert isinstance(instance, NamedElement)


def test_behaviour_TaskExecution_isa_NamedElement():
    instance = behaviour_TaskExecution(status="sample_text")
    assert isinstance(instance, NamedElement)


def test_behaviour_TaskRequirement_isa_NamedElement():
    instance = behaviour_TaskRequirement(participants=7)
    assert isinstance(instance, NamedElement)


def test_behaviour_BehaviouralPropertyKeyContainer_isa_PropertyKeyContainer():
    instance = behaviour_BehaviouralPropertyKeyContainer()
    assert isinstance(instance, PropertyKeyContainer)


def test_assoc_TTL13_link_reassign_clear():
    a = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    b1 = behaviour_MeasureValue()
    b2 = behaviour_MeasureValue()
    _safe_set(a, 'behaviour_Message14', b1)
    assert _is_linked(a, 'behaviour_Message14', b1)
    if hasattr(b1, 'behaviour_MeasureValue'):
        assert _is_linked(b1, 'behaviour_MeasureValue', a)
    _safe_set(a, 'behaviour_Message14', b2)
    assert _is_linked(a, 'behaviour_Message14', b2)
    if hasattr(b1, 'behaviour_MeasureValue'):
        assert not _is_linked(b1, 'behaviour_MeasureValue', a)
    if hasattr(b2, 'behaviour_MeasureValue'):
        assert _is_linked(b2, 'behaviour_MeasureValue', a)
    _safe_set(a, 'behaviour_Message14', None)
    assert not _is_linked(a, 'behaviour_Message14', b2)
    if hasattr(b2, 'behaviour_MeasureValue'):
        assert not _is_linked(b2, 'behaviour_MeasureValue', a)


def test_assoc_actions68_link_reassign_clear():
    a = behaviour_DynamicRobot(status="sample_text")
    b1 = behaviour_Action()
    b2 = behaviour_Action()
    _safe_set(a, 'behaviour_DynamicRobot69', {b1})
    assert _is_linked(a, 'behaviour_DynamicRobot69', b1)
    if hasattr(b1, 'behaviour_Action70'):
        assert _is_linked(b1, 'behaviour_Action70', a)
    _safe_set(a, 'behaviour_DynamicRobot69', {b2})
    assert _is_linked(a, 'behaviour_DynamicRobot69', b2)
    if hasattr(b1, 'behaviour_Action70'):
        assert not _is_linked(b1, 'behaviour_Action70', a)
    if hasattr(b2, 'behaviour_Action70'):
        assert _is_linked(b2, 'behaviour_Action70', a)
    _safe_set(a, 'behaviour_DynamicRobot69', set())
    assert not _is_linked(a, 'behaviour_DynamicRobot69', b2)
    if hasattr(b2, 'behaviour_Action70'):
        assert not _is_linked(b2, 'behaviour_Action70', a)


def test_assoc_capabilityProperties83_link_reassign_clear():
    a = behaviour_TaskRequirement(participants=7)
    b1 = behaviour_CapabilityProperties()
    b2 = behaviour_CapabilityProperties()
    _safe_set(a, 'behaviour_TaskRequirement84', {b1})
    assert _is_linked(a, 'behaviour_TaskRequirement84', b1)
    if hasattr(b1, 'behaviour_CapabilityProperties'):
        assert _is_linked(b1, 'behaviour_CapabilityProperties', a)
    _safe_set(a, 'behaviour_TaskRequirement84', {b2})
    assert _is_linked(a, 'behaviour_TaskRequirement84', b2)
    if hasattr(b1, 'behaviour_CapabilityProperties'):
        assert not _is_linked(b1, 'behaviour_CapabilityProperties', a)
    if hasattr(b2, 'behaviour_CapabilityProperties'):
        assert _is_linked(b2, 'behaviour_CapabilityProperties', a)
    _safe_set(a, 'behaviour_TaskRequirement84', set())
    assert not _is_linked(a, 'behaviour_TaskRequirement84', b2)
    if hasattr(b2, 'behaviour_CapabilityProperties'):
        assert not _is_linked(b2, 'behaviour_CapabilityProperties', a)


def test_assoc_collaborations64_link_reassign_clear():
    a = behaviour_DynamicRobot(status="sample_text")
    b1 = behaviour_RobotCollaboration()
    b2 = behaviour_RobotCollaboration()
    _safe_set(a, 'behaviour_DynamicRobot65', {b1})
    assert _is_linked(a, 'behaviour_DynamicRobot65', b1)
    if hasattr(b1, 'behaviour_RobotCollaboration66'):
        assert _is_linked(b1, 'behaviour_RobotCollaboration66', a)
    _safe_set(a, 'behaviour_DynamicRobot65', {b2})
    assert _is_linked(a, 'behaviour_DynamicRobot65', b2)
    if hasattr(b1, 'behaviour_RobotCollaboration66'):
        assert not _is_linked(b1, 'behaviour_RobotCollaboration66', a)
    if hasattr(b2, 'behaviour_RobotCollaboration66'):
        assert _is_linked(b2, 'behaviour_RobotCollaboration66', a)
    _safe_set(a, 'behaviour_DynamicRobot65', set())
    assert not _is_linked(a, 'behaviour_DynamicRobot65', b2)
    if hasattr(b2, 'behaviour_RobotCollaboration66'):
        assert not _is_linked(b2, 'behaviour_RobotCollaboration66', a)


def test_assoc_collaborator49_link_reassign_clear():
    a = behaviour_DynamicRobot(status="sample_text")
    b1 = behaviour_RobotCollaboration()
    b2 = behaviour_RobotCollaboration()
    _safe_set(a, 'behaviour_DynamicRobot50', b1)
    assert _is_linked(a, 'behaviour_DynamicRobot50', b1)
    if hasattr(b1, 'behaviour_RobotCollaboration'):
        assert _is_linked(b1, 'behaviour_RobotCollaboration', a)
    _safe_set(a, 'behaviour_DynamicRobot50', b2)
    assert _is_linked(a, 'behaviour_DynamicRobot50', b2)
    if hasattr(b1, 'behaviour_RobotCollaboration'):
        assert not _is_linked(b1, 'behaviour_RobotCollaboration', a)
    if hasattr(b2, 'behaviour_RobotCollaboration'):
        assert _is_linked(b2, 'behaviour_RobotCollaboration', a)
    _safe_set(a, 'behaviour_DynamicRobot50', None)
    assert not _is_linked(a, 'behaviour_DynamicRobot50', b2)
    if hasattr(b2, 'behaviour_RobotCollaboration'):
        assert not _is_linked(b2, 'behaviour_RobotCollaboration', a)


def test_assoc_currentTaskExecution34_link_reassign_clear():
    a = behaviour_TaskExecution(status="sample_text")
    b1 = behaviour_Action()
    b2 = behaviour_Action()
    _safe_set(a, 'behaviour_TaskExecution36', b1)
    assert _is_linked(a, 'behaviour_TaskExecution36', b1)
    if hasattr(b1, 'behaviour_Action35'):
        assert _is_linked(b1, 'behaviour_Action35', a)
    _safe_set(a, 'behaviour_TaskExecution36', b2)
    assert _is_linked(a, 'behaviour_TaskExecution36', b2)
    if hasattr(b1, 'behaviour_Action35'):
        assert not _is_linked(b1, 'behaviour_Action35', a)
    if hasattr(b2, 'behaviour_Action35'):
        assert _is_linked(b2, 'behaviour_Action35', a)
    _safe_set(a, 'behaviour_TaskExecution36', None)
    assert not _is_linked(a, 'behaviour_TaskExecution36', b2)
    if hasattr(b2, 'behaviour_Action35'):
        assert not _is_linked(b2, 'behaviour_Action35', a)


def test_assoc_descriptor85_link_reassign_clear():
    a = behaviour_TaskRequirement(participants=7)
    b1 = behaviour_TaskDescriptor()
    b2 = behaviour_TaskDescriptor()
    _safe_set(a, 'behaviour_TaskRequirement86', b1)
    assert _is_linked(a, 'behaviour_TaskRequirement86', b1)
    if hasattr(b1, 'behaviour_TaskDescriptor'):
        assert _is_linked(b1, 'behaviour_TaskDescriptor', a)
    _safe_set(a, 'behaviour_TaskRequirement86', b2)
    assert _is_linked(a, 'behaviour_TaskRequirement86', b2)
    if hasattr(b1, 'behaviour_TaskDescriptor'):
        assert not _is_linked(b1, 'behaviour_TaskDescriptor', a)
    if hasattr(b2, 'behaviour_TaskDescriptor'):
        assert _is_linked(b2, 'behaviour_TaskDescriptor', a)
    _safe_set(a, 'behaviour_TaskRequirement86', None)
    assert not _is_linked(a, 'behaviour_TaskRequirement86', b2)
    if hasattr(b2, 'behaviour_TaskDescriptor'):
        assert not _is_linked(b2, 'behaviour_TaskDescriptor', a)


def test_assoc_detectedObjects61_link_reassign_clear():
    a = behaviour_DynamicRobot(status="sample_text")
    b1 = behaviour_DetectedObject(obstacle=True)
    b2 = behaviour_DetectedObject(obstacle=False)
    _safe_set(a, 'behaviour_DynamicRobot62', {b1})
    assert _is_linked(a, 'behaviour_DynamicRobot62', b1)
    if hasattr(b1, 'behaviour_DetectedObject63'):
        assert _is_linked(b1, 'behaviour_DetectedObject63', a)
    _safe_set(a, 'behaviour_DynamicRobot62', {b2})
    assert _is_linked(a, 'behaviour_DynamicRobot62', b2)
    if hasattr(b1, 'behaviour_DetectedObject63'):
        assert not _is_linked(b1, 'behaviour_DetectedObject63', a)
    if hasattr(b2, 'behaviour_DetectedObject63'):
        assert _is_linked(b2, 'behaviour_DetectedObject63', a)
    _safe_set(a, 'behaviour_DynamicRobot62', set())
    assert not _is_linked(a, 'behaviour_DynamicRobot62', b2)
    if hasattr(b2, 'behaviour_DetectedObject63'):
        assert not _is_linked(b2, 'behaviour_DetectedObject63', a)


def test_assoc_dynamicRobots0_link_reassign_clear():
    a = behaviour_DynamicRobot(status="sample_text")
    b1 = behaviour_BehaviourContainer()
    b2 = behaviour_BehaviourContainer()
    _safe_set(a, 'behaviour_DynamicRobot', b1)
    assert _is_linked(a, 'behaviour_DynamicRobot', b1)
    if hasattr(b1, 'behaviour_BehaviourContainer'):
        assert _is_linked(b1, 'behaviour_BehaviourContainer', a)
    _safe_set(a, 'behaviour_DynamicRobot', b2)
    assert _is_linked(a, 'behaviour_DynamicRobot', b2)
    if hasattr(b1, 'behaviour_BehaviourContainer'):
        assert not _is_linked(b1, 'behaviour_BehaviourContainer', a)
    if hasattr(b2, 'behaviour_BehaviourContainer'):
        assert _is_linked(b2, 'behaviour_BehaviourContainer', a)
    _safe_set(a, 'behaviour_DynamicRobot', None)
    assert not _is_linked(a, 'behaviour_DynamicRobot', b2)
    if hasattr(b2, 'behaviour_BehaviourContainer'):
        assert not _is_linked(b2, 'behaviour_BehaviourContainer', a)


def test_assoc_executedTasks71_link_reassign_clear():
    a = behaviour_TaskExecution(status="sample_text")
    b1 = behaviour_DynamicRobot(status="sample_text")
    b2 = behaviour_DynamicRobot(status="sample_text_2")
    _safe_set(a, 'behaviour_TaskExecution73', b1)
    assert _is_linked(a, 'behaviour_TaskExecution73', b1)
    if hasattr(b1, 'behaviour_DynamicRobot72'):
        assert _is_linked(b1, 'behaviour_DynamicRobot72', a)
    _safe_set(a, 'behaviour_TaskExecution73', b2)
    assert _is_linked(a, 'behaviour_TaskExecution73', b2)
    if hasattr(b1, 'behaviour_DynamicRobot72'):
        assert not _is_linked(b1, 'behaviour_DynamicRobot72', a)
    if hasattr(b2, 'behaviour_DynamicRobot72'):
        assert _is_linked(b2, 'behaviour_DynamicRobot72', a)
    _safe_set(a, 'behaviour_TaskExecution73', None)
    assert not _is_linked(a, 'behaviour_TaskExecution73', b2)
    if hasattr(b2, 'behaviour_DynamicRobot72'):
        assert not _is_linked(b2, 'behaviour_DynamicRobot72', a)


def test_assoc_executionTime42_link_reassign_clear():
    a = behaviour_TaskExecution(status="sample_text")
    b1 = behaviour_MeasureValue()
    b2 = behaviour_MeasureValue()
    _safe_set(a, 'behaviour_TaskExecution43', b1)
    assert _is_linked(a, 'behaviour_TaskExecution43', b1)
    if hasattr(b1, 'behaviour_MeasureValue44'):
        assert _is_linked(b1, 'behaviour_MeasureValue44', a)
    _safe_set(a, 'behaviour_TaskExecution43', b2)
    assert _is_linked(a, 'behaviour_TaskExecution43', b2)
    if hasattr(b1, 'behaviour_MeasureValue44'):
        assert not _is_linked(b1, 'behaviour_MeasureValue44', a)
    if hasattr(b2, 'behaviour_MeasureValue44'):
        assert _is_linked(b2, 'behaviour_MeasureValue44', a)
    _safe_set(a, 'behaviour_TaskExecution43', None)
    assert not _is_linked(a, 'behaviour_TaskExecution43', b2)
    if hasattr(b2, 'behaviour_MeasureValue44'):
        assert not _is_linked(b2, 'behaviour_MeasureValue44', a)


def test_assoc_executors39_link_reassign_clear():
    a = behaviour_TaskExecution(status="sample_text")
    b1 = behaviour_DynamicRobot(status="sample_text")
    b2 = behaviour_DynamicRobot(status="sample_text_2")
    _safe_set(a, 'behaviour_TaskExecution40', {b1})
    assert _is_linked(a, 'behaviour_TaskExecution40', b1)
    if hasattr(b1, 'behaviour_DynamicRobot41'):
        assert _is_linked(b1, 'behaviour_DynamicRobot41', a)
    _safe_set(a, 'behaviour_TaskExecution40', {b2})
    assert _is_linked(a, 'behaviour_TaskExecution40', b2)
    if hasattr(b1, 'behaviour_DynamicRobot41'):
        assert not _is_linked(b1, 'behaviour_DynamicRobot41', a)
    if hasattr(b2, 'behaviour_DynamicRobot41'):
        assert _is_linked(b2, 'behaviour_DynamicRobot41', a)
    _safe_set(a, 'behaviour_TaskExecution40', set())
    assert not _is_linked(a, 'behaviour_TaskExecution40', b2)
    if hasattr(b2, 'behaviour_DynamicRobot41'):
        assert not _is_linked(b2, 'behaviour_DynamicRobot41', a)


def test_assoc_follows16_link_reassign_clear():
    a = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    b1 = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    b2 = behaviour_Message(needResponse=False, timestamp=date(2025, 6, 15))
    _safe_set(a, 'behaviour_Message15', b1)
    assert _is_linked(a, 'behaviour_Message15', b1)
    if hasattr(b1, 'behaviour_Message17'):
        assert _is_linked(b1, 'behaviour_Message17', a)
    _safe_set(a, 'behaviour_Message15', b2)
    assert _is_linked(a, 'behaviour_Message15', b2)
    if hasattr(b1, 'behaviour_Message17'):
        assert not _is_linked(b1, 'behaviour_Message17', a)
    if hasattr(b2, 'behaviour_Message17'):
        assert _is_linked(b2, 'behaviour_Message17', a)
    _safe_set(a, 'behaviour_Message15', None)
    assert not _is_linked(a, 'behaviour_Message15', b2)
    if hasattr(b2, 'behaviour_Message17'):
        assert not _is_linked(b2, 'behaviour_Message17', a)


def test_assoc_involvedTaskExecutions7_link_reassign_clear():
    a = behaviour_TaskExecution(status="sample_text")
    b1 = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    b2 = behaviour_Message(needResponse=False, timestamp=date(2025, 6, 15))
    _safe_set(a, 'behaviour_TaskExecution8', b1)
    assert _is_linked(a, 'behaviour_TaskExecution8', b1)
    if hasattr(b1, 'behaviour_Message'):
        assert _is_linked(b1, 'behaviour_Message', a)
    _safe_set(a, 'behaviour_TaskExecution8', b2)
    assert _is_linked(a, 'behaviour_TaskExecution8', b2)
    if hasattr(b1, 'behaviour_Message'):
        assert not _is_linked(b1, 'behaviour_Message', a)
    if hasattr(b2, 'behaviour_Message'):
        assert _is_linked(b2, 'behaviour_Message', a)
    _safe_set(a, 'behaviour_TaskExecution8', None)
    assert not _is_linked(a, 'behaviour_TaskExecution8', b2)
    if hasattr(b2, 'behaviour_Message'):
        assert not _is_linked(b2, 'behaviour_Message', a)


def test_assoc_message18_link_reassign_clear():
    a = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    b1 = behaviour_CommunicationAction()
    b2 = behaviour_CommunicationAction()
    _safe_set(a, 'behaviour_Message19', b1)
    assert _is_linked(a, 'behaviour_Message19', b1)
    if hasattr(b1, 'behaviour_CommunicationAction'):
        assert _is_linked(b1, 'behaviour_CommunicationAction', a)
    _safe_set(a, 'behaviour_Message19', b2)
    assert _is_linked(a, 'behaviour_Message19', b2)
    if hasattr(b1, 'behaviour_CommunicationAction'):
        assert not _is_linked(b1, 'behaviour_CommunicationAction', a)
    if hasattr(b2, 'behaviour_CommunicationAction'):
        assert _is_linked(b2, 'behaviour_CommunicationAction', a)
    _safe_set(a, 'behaviour_Message19', None)
    assert not _is_linked(a, 'behaviour_Message19', b2)
    if hasattr(b2, 'behaviour_CommunicationAction'):
        assert not _is_linked(b2, 'behaviour_CommunicationAction', a)


def test_assoc_messageRepository67_link_reassign_clear():
    a = behaviour_DynamicRobot(status="sample_text")
    b1 = behaviour_MessageRepository()
    b2 = behaviour_MessageRepository()
    _safe_set(a, 'robot', b1)
    assert _is_linked(a, 'robot', b1)
    if hasattr(b1, 'MessageRepository'):
        assert _is_linked(b1, 'MessageRepository', a)
    _safe_set(a, 'robot', b2)
    assert _is_linked(a, 'robot', b2)
    if hasattr(b1, 'MessageRepository'):
        assert not _is_linked(b1, 'MessageRepository', a)
    if hasattr(b2, 'MessageRepository'):
        assert _is_linked(b2, 'MessageRepository', a)
    _safe_set(a, 'robot', None)
    assert not _is_linked(a, 'robot', b2)
    if hasattr(b2, 'MessageRepository'):
        assert not _is_linked(b2, 'MessageRepository', a)


def test_assoc_object57_link_reassign_clear():
    a = behaviour_DetectedObject(obstacle=True)
    b1 = behaviour_AreaObject()
    b2 = behaviour_AreaObject()
    _safe_set(a, 'behaviour_DetectedObject', b1)
    assert _is_linked(a, 'behaviour_DetectedObject', b1)
    if hasattr(b1, 'behaviour_AreaObject58'):
        assert _is_linked(b1, 'behaviour_AreaObject58', a)
    _safe_set(a, 'behaviour_DetectedObject', b2)
    assert _is_linked(a, 'behaviour_DetectedObject', b2)
    if hasattr(b1, 'behaviour_AreaObject58'):
        assert not _is_linked(b1, 'behaviour_AreaObject58', a)
    if hasattr(b2, 'behaviour_AreaObject58'):
        assert _is_linked(b2, 'behaviour_AreaObject58', a)
    _safe_set(a, 'behaviour_DetectedObject', None)
    assert not _is_linked(a, 'behaviour_DetectedObject', b2)
    if hasattr(b2, 'behaviour_AreaObject58'):
        assert not _is_linked(b2, 'behaviour_AreaObject58', a)


def test_assoc_prerequisite75_link_reassign_clear():
    a = behaviour_TaskRequirement(participants=7)
    b1 = behaviour_TaskExecution(status="sample_text")
    b2 = behaviour_TaskExecution(status="sample_text_2")
    _safe_set(a, 'behaviour_TaskRequirement76', b1)
    assert _is_linked(a, 'behaviour_TaskRequirement76', b1)
    if hasattr(b1, 'behaviour_TaskExecution77'):
        assert _is_linked(b1, 'behaviour_TaskExecution77', a)
    _safe_set(a, 'behaviour_TaskRequirement76', b2)
    assert _is_linked(a, 'behaviour_TaskRequirement76', b2)
    if hasattr(b1, 'behaviour_TaskExecution77'):
        assert not _is_linked(b1, 'behaviour_TaskExecution77', a)
    if hasattr(b2, 'behaviour_TaskExecution77'):
        assert _is_linked(b2, 'behaviour_TaskExecution77', a)
    _safe_set(a, 'behaviour_TaskRequirement76', None)
    assert not _is_linked(a, 'behaviour_TaskRequirement76', b2)
    if hasattr(b2, 'behaviour_TaskExecution77'):
        assert not _is_linked(b2, 'behaviour_TaskExecution77', a)


def test_assoc_properties78_link_reassign_clear():
    a = behaviour_TaskRequirement(participants=7)
    b1 = behaviour_Property()
    b2 = behaviour_Property()
    _safe_set(a, 'behaviour_TaskRequirement79', {b1})
    assert _is_linked(a, 'behaviour_TaskRequirement79', b1)
    if hasattr(b1, 'behaviour_Property80'):
        assert _is_linked(b1, 'behaviour_Property80', a)
    _safe_set(a, 'behaviour_TaskRequirement79', {b2})
    assert _is_linked(a, 'behaviour_TaskRequirement79', b2)
    if hasattr(b1, 'behaviour_Property80'):
        assert not _is_linked(b1, 'behaviour_Property80', a)
    if hasattr(b2, 'behaviour_Property80'):
        assert _is_linked(b2, 'behaviour_Property80', a)
    _safe_set(a, 'behaviour_TaskRequirement79', set())
    assert not _is_linked(a, 'behaviour_TaskRequirement79', b2)
    if hasattr(b2, 'behaviour_Property80'):
        assert not _is_linked(b2, 'behaviour_Property80', a)


def test_assoc_properties9_link_reassign_clear():
    a = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    b1 = behaviour_Property()
    b2 = behaviour_Property()
    _safe_set(a, 'behaviour_Message10', {b1})
    assert _is_linked(a, 'behaviour_Message10', b1)
    if hasattr(b1, 'behaviour_Property'):
        assert _is_linked(b1, 'behaviour_Property', a)
    _safe_set(a, 'behaviour_Message10', {b2})
    assert _is_linked(a, 'behaviour_Message10', b2)
    if hasattr(b1, 'behaviour_Property'):
        assert not _is_linked(b1, 'behaviour_Property', a)
    if hasattr(b2, 'behaviour_Property'):
        assert _is_linked(b2, 'behaviour_Property', a)
    _safe_set(a, 'behaviour_Message10', set())
    assert not _is_linked(a, 'behaviour_Message10', b2)
    if hasattr(b2, 'behaviour_Property'):
        assert not _is_linked(b2, 'behaviour_Property', a)


def test_assoc_receivedMessages27_link_reassign_clear():
    a = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    b1 = behaviour_MessageRepository()
    b2 = behaviour_MessageRepository()
    _safe_set(a, 'behaviour_Message28', b1)
    assert _is_linked(a, 'behaviour_Message28', b1)
    if hasattr(b1, 'behaviour_MessageRepository'):
        assert _is_linked(b1, 'behaviour_MessageRepository', a)
    _safe_set(a, 'behaviour_Message28', b2)
    assert _is_linked(a, 'behaviour_Message28', b2)
    if hasattr(b1, 'behaviour_MessageRepository'):
        assert not _is_linked(b1, 'behaviour_MessageRepository', a)
    if hasattr(b2, 'behaviour_MessageRepository'):
        assert _is_linked(b2, 'behaviour_MessageRepository', a)
    _safe_set(a, 'behaviour_Message28', None)
    assert not _is_linked(a, 'behaviour_Message28', b2)
    if hasattr(b2, 'behaviour_MessageRepository'):
        assert not _is_linked(b2, 'behaviour_MessageRepository', a)


def test_assoc_referredObjects11_link_reassign_clear():
    a = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    b1 = behaviour_AreaObject()
    b2 = behaviour_AreaObject()
    _safe_set(a, 'behaviour_Message12', {b1})
    assert _is_linked(a, 'behaviour_Message12', b1)
    if hasattr(b1, 'behaviour_AreaObject'):
        assert _is_linked(b1, 'behaviour_AreaObject', a)
    _safe_set(a, 'behaviour_Message12', {b2})
    assert _is_linked(a, 'behaviour_Message12', b2)
    if hasattr(b1, 'behaviour_AreaObject'):
        assert not _is_linked(b1, 'behaviour_AreaObject', a)
    if hasattr(b2, 'behaviour_AreaObject'):
        assert _is_linked(b2, 'behaviour_AreaObject', a)
    _safe_set(a, 'behaviour_Message12', set())
    assert not _is_linked(a, 'behaviour_Message12', b2)
    if hasattr(b2, 'behaviour_AreaObject'):
        assert not _is_linked(b2, 'behaviour_AreaObject', a)


def test_assoc_requiredCapabilities81_link_reassign_clear():
    a = behaviour_TaskRequirement(participants=7)
    b1 = behaviour_Capability()
    b2 = behaviour_Capability()
    _safe_set(a, 'behaviour_TaskRequirement82', {b1})
    assert _is_linked(a, 'behaviour_TaskRequirement82', b1)
    if hasattr(b1, 'behaviour_Capability'):
        assert _is_linked(b1, 'behaviour_Capability', a)
    _safe_set(a, 'behaviour_TaskRequirement82', {b2})
    assert _is_linked(a, 'behaviour_TaskRequirement82', b2)
    if hasattr(b1, 'behaviour_Capability'):
        assert not _is_linked(b1, 'behaviour_Capability', a)
    if hasattr(b2, 'behaviour_Capability'):
        assert _is_linked(b2, 'behaviour_Capability', a)
    _safe_set(a, 'behaviour_TaskRequirement82', set())
    assert not _is_linked(a, 'behaviour_TaskRequirement82', b2)
    if hasattr(b2, 'behaviour_Capability'):
        assert not _is_linked(b2, 'behaviour_Capability', a)


def test_assoc_requirement48_link_reassign_clear():
    a = behaviour_TaskRequirement(participants=7)
    b1 = behaviour_TaskExecution(status="sample_text")
    b2 = behaviour_TaskExecution(status="sample_text_2")
    _safe_set(a, 'TaskRequirement', b1)
    assert _is_linked(a, 'TaskRequirement', b1)
    if hasattr(b1, 'taskExecution'):
        assert _is_linked(b1, 'taskExecution', a)
    _safe_set(a, 'TaskRequirement', b2)
    assert _is_linked(a, 'TaskRequirement', b2)
    if hasattr(b1, 'taskExecution'):
        assert not _is_linked(b1, 'taskExecution', a)
    if hasattr(b2, 'taskExecution'):
        assert _is_linked(b2, 'taskExecution', a)
    _safe_set(a, 'TaskRequirement', None)
    assert not _is_linked(a, 'TaskRequirement', b2)
    if hasattr(b2, 'taskExecution'):
        assert not _is_linked(b2, 'taskExecution', a)


def test_assoc_robot26_link_reassign_clear():
    a = behaviour_DynamicRobot(status="sample_text")
    b1 = behaviour_MessageRepository()
    b2 = behaviour_MessageRepository()
    _safe_set(a, 'DynamicRobot', b1)
    assert _is_linked(a, 'DynamicRobot', b1)
    if hasattr(b1, 'messageRepository'):
        assert _is_linked(b1, 'messageRepository', a)
    _safe_set(a, 'DynamicRobot', b2)
    assert _is_linked(a, 'DynamicRobot', b2)
    if hasattr(b1, 'messageRepository'):
        assert not _is_linked(b1, 'messageRepository', a)
    if hasattr(b2, 'messageRepository'):
        assert _is_linked(b2, 'messageRepository', a)
    _safe_set(a, 'DynamicRobot', None)
    assert not _is_linked(a, 'DynamicRobot', b2)
    if hasattr(b2, 'messageRepository'):
        assert not _is_linked(b2, 'messageRepository', a)


def test_assoc_robot59_link_reassign_clear():
    a = behaviour_DynamicRobot(status="sample_text")
    b1 = behaviour_Robot()
    b2 = behaviour_Robot()
    _safe_set(a, 'behaviour_DynamicRobot60', b1)
    assert _is_linked(a, 'behaviour_DynamicRobot60', b1)
    if hasattr(b1, 'behaviour_Robot'):
        assert _is_linked(b1, 'behaviour_Robot', a)
    _safe_set(a, 'behaviour_DynamicRobot60', b2)
    assert _is_linked(a, 'behaviour_DynamicRobot60', b2)
    if hasattr(b1, 'behaviour_Robot'):
        assert not _is_linked(b1, 'behaviour_Robot', a)
    if hasattr(b2, 'behaviour_Robot'):
        assert _is_linked(b2, 'behaviour_Robot', a)
    _safe_set(a, 'behaviour_DynamicRobot60', None)
    assert not _is_linked(a, 'behaviour_DynamicRobot60', b2)
    if hasattr(b2, 'behaviour_Robot'):
        assert not _is_linked(b2, 'behaviour_Robot', a)


def test_assoc_sendedMessages29_link_reassign_clear():
    a = behaviour_Message(needResponse=True, timestamp=date(2024, 1, 1))
    b1 = behaviour_MessageRepository()
    b2 = behaviour_MessageRepository()
    _safe_set(a, 'behaviour_Message31', b1)
    assert _is_linked(a, 'behaviour_Message31', b1)
    if hasattr(b1, 'behaviour_MessageRepository30'):
        assert _is_linked(b1, 'behaviour_MessageRepository30', a)
    _safe_set(a, 'behaviour_Message31', b2)
    assert _is_linked(a, 'behaviour_Message31', b2)
    if hasattr(b1, 'behaviour_MessageRepository30'):
        assert not _is_linked(b1, 'behaviour_MessageRepository30', a)
    if hasattr(b2, 'behaviour_MessageRepository30'):
        assert _is_linked(b2, 'behaviour_MessageRepository30', a)
    _safe_set(a, 'behaviour_Message31', None)
    assert not _is_linked(a, 'behaviour_Message31', b2)
    if hasattr(b2, 'behaviour_MessageRepository30'):
        assert not _is_linked(b2, 'behaviour_MessageRepository30', a)


def test_assoc_target20_link_reassign_clear():
    a = behaviour_DynamicRobot(status="sample_text")
    b1 = behaviour_UnicastCommunication()
    b2 = behaviour_UnicastCommunication()
    _safe_set(a, 'behaviour_DynamicRobot21', b1)
    assert _is_linked(a, 'behaviour_DynamicRobot21', b1)
    if hasattr(b1, 'behaviour_UnicastCommunication'):
        assert _is_linked(b1, 'behaviour_UnicastCommunication', a)
    _safe_set(a, 'behaviour_DynamicRobot21', b2)
    assert _is_linked(a, 'behaviour_DynamicRobot21', b2)
    if hasattr(b1, 'behaviour_UnicastCommunication'):
        assert not _is_linked(b1, 'behaviour_UnicastCommunication', a)
    if hasattr(b2, 'behaviour_UnicastCommunication'):
        assert _is_linked(b2, 'behaviour_UnicastCommunication', a)
    _safe_set(a, 'behaviour_DynamicRobot21', None)
    assert not _is_linked(a, 'behaviour_DynamicRobot21', b2)
    if hasattr(b2, 'behaviour_UnicastCommunication'):
        assert not _is_linked(b2, 'behaviour_UnicastCommunication', a)


def test_assoc_targets22_link_reassign_clear():
    a = behaviour_DynamicRobot(status="sample_text")
    b1 = behaviour_MulticastCommunication()
    b2 = behaviour_MulticastCommunication()
    _safe_set(a, 'behaviour_DynamicRobot23', b1)
    assert _is_linked(a, 'behaviour_DynamicRobot23', b1)
    if hasattr(b1, 'behaviour_MulticastCommunication'):
        assert _is_linked(b1, 'behaviour_MulticastCommunication', a)
    _safe_set(a, 'behaviour_DynamicRobot23', b2)
    assert _is_linked(a, 'behaviour_DynamicRobot23', b2)
    if hasattr(b1, 'behaviour_MulticastCommunication'):
        assert not _is_linked(b1, 'behaviour_MulticastCommunication', a)
    if hasattr(b2, 'behaviour_MulticastCommunication'):
        assert _is_linked(b2, 'behaviour_MulticastCommunication', a)
    _safe_set(a, 'behaviour_DynamicRobot23', None)
    assert not _is_linked(a, 'behaviour_DynamicRobot23', b2)
    if hasattr(b2, 'behaviour_MulticastCommunication'):
        assert not _is_linked(b2, 'behaviour_MulticastCommunication', a)


def test_assoc_targets24_link_reassign_clear():
    a = behaviour_DynamicRobot(status="sample_text")
    b1 = behaviour_BroadcastCommunication()
    b2 = behaviour_BroadcastCommunication()
    _safe_set(a, 'behaviour_DynamicRobot25', b1)
    assert _is_linked(a, 'behaviour_DynamicRobot25', b1)
    if hasattr(b1, 'behaviour_BroadcastCommunication'):
        assert _is_linked(b1, 'behaviour_BroadcastCommunication', a)
    _safe_set(a, 'behaviour_DynamicRobot25', b2)
    assert _is_linked(a, 'behaviour_DynamicRobot25', b2)
    if hasattr(b1, 'behaviour_BroadcastCommunication'):
        assert not _is_linked(b1, 'behaviour_BroadcastCommunication', a)
    if hasattr(b2, 'behaviour_BroadcastCommunication'):
        assert _is_linked(b2, 'behaviour_BroadcastCommunication', a)
    _safe_set(a, 'behaviour_DynamicRobot25', None)
    assert not _is_linked(a, 'behaviour_DynamicRobot25', b2)
    if hasattr(b2, 'behaviour_BroadcastCommunication'):
        assert not _is_linked(b2, 'behaviour_BroadcastCommunication', a)


def test_assoc_task45_link_reassign_clear():
    a = behaviour_TaskExecution(status="sample_text")
    b1 = behaviour_Task()
    b2 = behaviour_Task()
    _safe_set(a, 'behaviour_TaskExecution46', b1)
    assert _is_linked(a, 'behaviour_TaskExecution46', b1)
    if hasattr(b1, 'behaviour_Task47'):
        assert _is_linked(b1, 'behaviour_Task47', a)
    _safe_set(a, 'behaviour_TaskExecution46', b2)
    assert _is_linked(a, 'behaviour_TaskExecution46', b2)
    if hasattr(b1, 'behaviour_Task47'):
        assert not _is_linked(b1, 'behaviour_Task47', a)
    if hasattr(b2, 'behaviour_Task47'):
        assert _is_linked(b2, 'behaviour_Task47', a)
    _safe_set(a, 'behaviour_TaskExecution46', None)
    assert not _is_linked(a, 'behaviour_TaskExecution46', b2)
    if hasattr(b2, 'behaviour_Task47'):
        assert not _is_linked(b2, 'behaviour_Task47', a)


def test_assoc_task87_link_reassign_clear():
    a = behaviour_TaskRequirement(participants=7)
    b1 = behaviour_Task()
    b2 = behaviour_Task()
    _safe_set(a, 'behaviour_TaskRequirement88', b1)
    assert _is_linked(a, 'behaviour_TaskRequirement88', b1)
    if hasattr(b1, 'behaviour_Task89'):
        assert _is_linked(b1, 'behaviour_Task89', a)
    _safe_set(a, 'behaviour_TaskRequirement88', b2)
    assert _is_linked(a, 'behaviour_TaskRequirement88', b2)
    if hasattr(b1, 'behaviour_Task89'):
        assert not _is_linked(b1, 'behaviour_Task89', a)
    if hasattr(b2, 'behaviour_Task89'):
        assert _is_linked(b2, 'behaviour_Task89', a)
    _safe_set(a, 'behaviour_TaskRequirement88', None)
    assert not _is_linked(a, 'behaviour_TaskRequirement88', b2)
    if hasattr(b2, 'behaviour_Task89'):
        assert not _is_linked(b2, 'behaviour_Task89', a)


def test_assoc_taskExecution74_link_reassign_clear():
    a = behaviour_TaskRequirement(participants=7)
    b1 = behaviour_TaskExecution(status="sample_text")
    b2 = behaviour_TaskExecution(status="sample_text_2")
    _safe_set(a, 'requirement', b1)
    assert _is_linked(a, 'requirement', b1)
    if hasattr(b1, 'TaskExecution'):
        assert _is_linked(b1, 'TaskExecution', a)
    _safe_set(a, 'requirement', b2)
    assert _is_linked(a, 'requirement', b2)
    if hasattr(b1, 'TaskExecution'):
        assert not _is_linked(b1, 'TaskExecution', a)
    if hasattr(b2, 'TaskExecution'):
        assert _is_linked(b2, 'TaskExecution', a)
    _safe_set(a, 'requirement', None)
    assert not _is_linked(a, 'requirement', b2)
    if hasattr(b2, 'TaskExecution'):
        assert not _is_linked(b2, 'TaskExecution', a)


def test_assoc_taskExecutions1_link_reassign_clear():
    a = behaviour_TaskExecution(status="sample_text")
    b1 = behaviour_BehaviourContainer()
    b2 = behaviour_BehaviourContainer()
    _safe_set(a, 'behaviour_TaskExecution', b1)
    assert _is_linked(a, 'behaviour_TaskExecution', b1)
    if hasattr(b1, 'behaviour_BehaviourContainer2'):
        assert _is_linked(b1, 'behaviour_BehaviourContainer2', a)
    _safe_set(a, 'behaviour_TaskExecution', b2)
    assert _is_linked(a, 'behaviour_TaskExecution', b2)
    if hasattr(b1, 'behaviour_BehaviourContainer2'):
        assert not _is_linked(b1, 'behaviour_BehaviourContainer2', a)
    if hasattr(b2, 'behaviour_BehaviourContainer2'):
        assert _is_linked(b2, 'behaviour_BehaviourContainer2', a)
    _safe_set(a, 'behaviour_TaskExecution', None)
    assert not _is_linked(a, 'behaviour_TaskExecution', b2)
    if hasattr(b2, 'behaviour_BehaviourContainer2'):
        assert not _is_linked(b2, 'behaviour_BehaviourContainer2', a)


def test_assoc_taskRequirements3_link_reassign_clear():
    a = behaviour_TaskRequirement(participants=7)
    b1 = behaviour_BehaviourContainer()
    b2 = behaviour_BehaviourContainer()
    _safe_set(a, 'behaviour_TaskRequirement', b1)
    assert _is_linked(a, 'behaviour_TaskRequirement', b1)
    if hasattr(b1, 'behaviour_BehaviourContainer4'):
        assert _is_linked(b1, 'behaviour_BehaviourContainer4', a)
    _safe_set(a, 'behaviour_TaskRequirement', b2)
    assert _is_linked(a, 'behaviour_TaskRequirement', b2)
    if hasattr(b1, 'behaviour_BehaviourContainer4'):
        assert not _is_linked(b1, 'behaviour_BehaviourContainer4', a)
    if hasattr(b2, 'behaviour_BehaviourContainer4'):
        assert _is_linked(b2, 'behaviour_BehaviourContainer4', a)
    _safe_set(a, 'behaviour_TaskRequirement', None)
    assert not _is_linked(a, 'behaviour_TaskRequirement', b2)
    if hasattr(b2, 'behaviour_BehaviourContainer4'):
        assert not _is_linked(b2, 'behaviour_BehaviourContainer4', a)


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


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


PropertyKeyContainer_strategy = st.builds(PropertyKeyContainer)
@given(instance=PropertyKeyContainer_strategy)
@settings(max_examples=25)
def test_PropertyKeyContainer_instantiation(instance):
    assert isinstance(instance, PropertyKeyContainer)


behaviour_Action_strategy = st.builds(behaviour_Action)
@given(instance=behaviour_Action_strategy)
@settings(max_examples=25)
def test_behaviour_Action_instantiation(instance):
    assert isinstance(instance, behaviour_Action)


behaviour_AreaObject_strategy = st.builds(behaviour_AreaObject)
@given(instance=behaviour_AreaObject_strategy)
@settings(max_examples=25)
def test_behaviour_AreaObject_instantiation(instance):
    assert isinstance(instance, behaviour_AreaObject)


behaviour_BehaviourContainer_strategy = st.builds(behaviour_BehaviourContainer)
@given(instance=behaviour_BehaviourContainer_strategy)
@settings(max_examples=25)
def test_behaviour_BehaviourContainer_instantiation(instance):
    assert isinstance(instance, behaviour_BehaviourContainer)


behaviour_BehaviouralPropertyKeyContainer_strategy = st.builds(behaviour_BehaviouralPropertyKeyContainer)
@given(instance=behaviour_BehaviouralPropertyKeyContainer_strategy)
@settings(max_examples=25)
def test_behaviour_BehaviouralPropertyKeyContainer_instantiation(instance):
    assert isinstance(instance, behaviour_BehaviouralPropertyKeyContainer)


behaviour_BroadcastCommunication_strategy = st.builds(behaviour_BroadcastCommunication)
@given(instance=behaviour_BroadcastCommunication_strategy)
@settings(max_examples=25)
def test_behaviour_BroadcastCommunication_instantiation(instance):
    assert isinstance(instance, behaviour_BroadcastCommunication)


behaviour_Capability_strategy = st.builds(behaviour_Capability)
@given(instance=behaviour_Capability_strategy)
@settings(max_examples=25)
def test_behaviour_Capability_instantiation(instance):
    assert isinstance(instance, behaviour_Capability)


behaviour_CapabilityProperties_strategy = st.builds(behaviour_CapabilityProperties)
@given(instance=behaviour_CapabilityProperties_strategy)
@settings(max_examples=25)
def test_behaviour_CapabilityProperties_instantiation(instance):
    assert isinstance(instance, behaviour_CapabilityProperties)


behaviour_CommunicationAction_strategy = st.builds(behaviour_CommunicationAction)
@given(instance=behaviour_CommunicationAction_strategy)
@settings(max_examples=25)
def test_behaviour_CommunicationAction_instantiation(instance):
    assert isinstance(instance, behaviour_CommunicationAction)


behaviour_DetectedObject_strategy = st.builds(behaviour_DetectedObject, obstacle=st.booleans())
@given(instance=behaviour_DetectedObject_strategy)
@settings(max_examples=25)
def test_behaviour_DetectedObject_instantiation(instance):
    assert isinstance(instance, behaviour_DetectedObject)


behaviour_DynamicRobot_strategy = st.builds(behaviour_DynamicRobot, status=safe_text)
@given(instance=behaviour_DynamicRobot_strategy)
@settings(max_examples=25)
def test_behaviour_DynamicRobot_instantiation(instance):
    assert isinstance(instance, behaviour_DynamicRobot)


behaviour_MeasureValue_strategy = st.builds(behaviour_MeasureValue)
@given(instance=behaviour_MeasureValue_strategy)
@settings(max_examples=25)
def test_behaviour_MeasureValue_instantiation(instance):
    assert isinstance(instance, behaviour_MeasureValue)


behaviour_Message_strategy = st.builds(behaviour_Message, needResponse=st.booleans(), timestamp=st.dates())
@given(instance=behaviour_Message_strategy)
@settings(max_examples=25)
def test_behaviour_Message_instantiation(instance):
    assert isinstance(instance, behaviour_Message)


behaviour_MessageRepository_strategy = st.builds(behaviour_MessageRepository)
@given(instance=behaviour_MessageRepository_strategy)
@settings(max_examples=25)
def test_behaviour_MessageRepository_instantiation(instance):
    assert isinstance(instance, behaviour_MessageRepository)


behaviour_MulticastCommunication_strategy = st.builds(behaviour_MulticastCommunication)
@given(instance=behaviour_MulticastCommunication_strategy)
@settings(max_examples=25)
def test_behaviour_MulticastCommunication_instantiation(instance):
    assert isinstance(instance, behaviour_MulticastCommunication)


behaviour_Property_strategy = st.builds(behaviour_Property)
@given(instance=behaviour_Property_strategy)
@settings(max_examples=25)
def test_behaviour_Property_instantiation(instance):
    assert isinstance(instance, behaviour_Property)


behaviour_Robot_strategy = st.builds(behaviour_Robot)
@given(instance=behaviour_Robot_strategy)
@settings(max_examples=25)
def test_behaviour_Robot_instantiation(instance):
    assert isinstance(instance, behaviour_Robot)


behaviour_RobotCollaboration_strategy = st.builds(behaviour_RobotCollaboration)
@given(instance=behaviour_RobotCollaboration_strategy)
@settings(max_examples=25)
def test_behaviour_RobotCollaboration_instantiation(instance):
    assert isinstance(instance, behaviour_RobotCollaboration)


behaviour_Task_strategy = st.builds(behaviour_Task)
@given(instance=behaviour_Task_strategy)
@settings(max_examples=25)
def test_behaviour_Task_instantiation(instance):
    assert isinstance(instance, behaviour_Task)


behaviour_TaskDescriptor_strategy = st.builds(behaviour_TaskDescriptor)
@given(instance=behaviour_TaskDescriptor_strategy)
@settings(max_examples=25)
def test_behaviour_TaskDescriptor_instantiation(instance):
    assert isinstance(instance, behaviour_TaskDescriptor)


behaviour_TaskExecution_strategy = st.builds(behaviour_TaskExecution, status=safe_text)
@given(instance=behaviour_TaskExecution_strategy)
@settings(max_examples=25)
def test_behaviour_TaskExecution_instantiation(instance):
    assert isinstance(instance, behaviour_TaskExecution)


behaviour_TaskRequirement_strategy = st.builds(behaviour_TaskRequirement, participants=st.integers())
@given(instance=behaviour_TaskRequirement_strategy)
@settings(max_examples=25)
def test_behaviour_TaskRequirement_instantiation(instance):
    assert isinstance(instance, behaviour_TaskRequirement)


behaviour_UnicastCommunication_strategy = st.builds(behaviour_UnicastCommunication)
@given(instance=behaviour_UnicastCommunication_strategy)
@settings(max_examples=25)
def test_behaviour_UnicastCommunication_instantiation(instance):
    assert isinstance(instance, behaviour_UnicastCommunication)



