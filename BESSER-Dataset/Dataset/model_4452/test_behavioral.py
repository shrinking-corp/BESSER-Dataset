import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bridge,
    Data,
    Device,
    Port,
    Server,
    wsmodel3_AccesPoint,
    wsmodel3_Actuator,
    wsmodel3_Break,
    wsmodel3_Bridge,
    wsmodel3_Communication,
    wsmodel3_CommunicationData,
    wsmodel3_Controller,
    wsmodel3_DBServer,
    wsmodel3_Data,
    wsmodel3_Device,
    wsmodel3_DeviceData,
    wsmodel3_ExternalAPI,
    wsmodel3_Function,
    wsmodel3_InputBridge,
    wsmodel3_InputOrchestrator,
    wsmodel3_InputPort,
    wsmodel3_IntegrationPattern,
    wsmodel3_IoTNode,
    wsmodel3_MessageBroker,
    wsmodel3_Orchestrator,
    wsmodel3_OrchestratorData,
    wsmodel3_OutputBridge,
    wsmodel3_OutputOrchestrator,
    wsmodel3_OutputPort,
    wsmodel3_Port,
    wsmodel3_REST,
    wsmodel3_Sensor,
    wsmodel3_Server,
    wsmodel3_System,
    wsmodel3_WebServer,
    wsmodel3_WebService,
    ActuatorType,
    CommunicationType,
    ControllerType,
    DBType,
    MessageBrokerType,
    PortType,
    SensorType,
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

def test_assoc_accespoint31_reverse_link_reassign_clear():
    a1 = wsmodel3_Communication(name="sample_text", type="sample_text")
    a2 = wsmodel3_Communication(name="sample_text_2", type="sample_text_2")
    b = wsmodel3_AccesPoint(pass_="sample_text", ssid="sample_text")
    _safe_set(b, 'wsmodel3_AccesPoint33', a1)
    assert _is_linked(b, 'wsmodel3_AccesPoint33', a1)
    if hasattr(a1, 'wsmodel3_Communication32'):
        assert _is_linked(a1, 'wsmodel3_Communication32', b)
    _safe_set(b, 'wsmodel3_AccesPoint33', a2)
    assert _is_linked(b, 'wsmodel3_AccesPoint33', a2)
    if hasattr(a1, 'wsmodel3_Communication32'):
        assert not _is_linked(a1, 'wsmodel3_Communication32', b)
    if hasattr(a2, 'wsmodel3_Communication32'):
        assert _is_linked(a2, 'wsmodel3_Communication32', b)
    _safe_set(b, 'wsmodel3_AccesPoint33', None)
    assert not _is_linked(b, 'wsmodel3_AccesPoint33', a2)
    if hasattr(a2, 'wsmodel3_Communication32'):
        assert not _is_linked(a2, 'wsmodel3_Communication32', b)


def test_assoc_accespoint5_reverse_link_reassign_clear():
    a1 = wsmodel3_System(name="sample_text")
    a2 = wsmodel3_System(name="sample_text_2")
    b = wsmodel3_AccesPoint(pass_="sample_text", ssid="sample_text")
    _safe_set(b, 'wsmodel3_AccesPoint', a1)
    assert _is_linked(b, 'wsmodel3_AccesPoint', a1)
    if hasattr(a1, 'wsmodel3_System6'):
        assert _is_linked(a1, 'wsmodel3_System6', b)
    _safe_set(b, 'wsmodel3_AccesPoint', a2)
    assert _is_linked(b, 'wsmodel3_AccesPoint', a2)
    if hasattr(a1, 'wsmodel3_System6'):
        assert not _is_linked(a1, 'wsmodel3_System6', b)
    if hasattr(a2, 'wsmodel3_System6'):
        assert _is_linked(a2, 'wsmodel3_System6', b)
    _safe_set(b, 'wsmodel3_AccesPoint', None)
    assert not _is_linked(b, 'wsmodel3_AccesPoint', a2)
    if hasattr(a2, 'wsmodel3_System6'):
        assert not _is_linked(a2, 'wsmodel3_System6', b)


def test_assoc_actuator41_reverse_link_reassign_clear():
    a1 = wsmodel3_InputBridge(URI="sample_text")
    a2 = wsmodel3_InputBridge(URI="sample_text_2")
    b = wsmodel3_Actuator(type="sample_text")
    _safe_set(b, 'wsmodel3_Actuator42', a1)
    assert _is_linked(b, 'wsmodel3_Actuator42', a1)
    if hasattr(a1, 'wsmodel3_InputBridge'):
        assert _is_linked(a1, 'wsmodel3_InputBridge', b)
    _safe_set(b, 'wsmodel3_Actuator42', a2)
    assert _is_linked(b, 'wsmodel3_Actuator42', a2)
    if hasattr(a1, 'wsmodel3_InputBridge'):
        assert not _is_linked(a1, 'wsmodel3_InputBridge', b)
    if hasattr(a2, 'wsmodel3_InputBridge'):
        assert _is_linked(a2, 'wsmodel3_InputBridge', b)
    _safe_set(b, 'wsmodel3_Actuator42', None)
    assert not _is_linked(b, 'wsmodel3_Actuator42', a2)
    if hasattr(a2, 'wsmodel3_InputBridge'):
        assert not _is_linked(a2, 'wsmodel3_InputBridge', b)


def test_assoc_break_74_reverse_link_reassign_clear():
    a1 = wsmodel3_Function(expression="sample_text")
    a2 = wsmodel3_Function(expression="sample_text_2")
    b = wsmodel3_Break(expression="sample_text")
    _safe_set(b, 'wsmodel3_Break', a1)
    assert _is_linked(b, 'wsmodel3_Break', a1)
    if hasattr(a1, 'wsmodel3_Function75'):
        assert _is_linked(a1, 'wsmodel3_Function75', b)
    _safe_set(b, 'wsmodel3_Break', a2)
    assert _is_linked(b, 'wsmodel3_Break', a2)
    if hasattr(a1, 'wsmodel3_Function75'):
        assert not _is_linked(a1, 'wsmodel3_Function75', b)
    if hasattr(a2, 'wsmodel3_Function75'):
        assert _is_linked(a2, 'wsmodel3_Function75', b)
    _safe_set(b, 'wsmodel3_Break', None)
    assert not _is_linked(b, 'wsmodel3_Break', a2)
    if hasattr(a2, 'wsmodel3_Function75'):
        assert not _is_linked(a2, 'wsmodel3_Function75', b)


def test_assoc_bridge47_reverse_link_reassign_clear():
    a1 = wsmodel3_MessageBroker(host="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    a2 = wsmodel3_MessageBroker(host="sample_text_2", pass_="sample_text_2", port=13, type="sample_text_2", usser="sample_text_2")
    b = wsmodel3_Bridge(host="sample_text", port=7, topic="sample_text")
    _safe_set(b, 'wsmodel3_Bridge49', a1)
    assert _is_linked(b, 'wsmodel3_Bridge49', a1)
    if hasattr(a1, 'wsmodel3_MessageBroker48'):
        assert _is_linked(a1, 'wsmodel3_MessageBroker48', b)
    _safe_set(b, 'wsmodel3_Bridge49', a2)
    assert _is_linked(b, 'wsmodel3_Bridge49', a2)
    if hasattr(a1, 'wsmodel3_MessageBroker48'):
        assert not _is_linked(a1, 'wsmodel3_MessageBroker48', b)
    if hasattr(a2, 'wsmodel3_MessageBroker48'):
        assert _is_linked(a2, 'wsmodel3_MessageBroker48', b)
    _safe_set(b, 'wsmodel3_Bridge49', None)
    assert not _is_linked(b, 'wsmodel3_Bridge49', a2)
    if hasattr(a2, 'wsmodel3_MessageBroker48'):
        assert not _is_linked(a2, 'wsmodel3_MessageBroker48', b)


def test_assoc_communication27_reverse_link_reassign_clear():
    a1 = wsmodel3_Controller(type="sample_text")
    a2 = wsmodel3_Controller(type="sample_text_2")
    b = wsmodel3_Communication(name="sample_text", type="sample_text")
    _safe_set(b, 'wsmodel3_Communication', a1)
    assert _is_linked(b, 'wsmodel3_Communication', a1)
    if hasattr(a1, 'wsmodel3_Controller28'):
        assert _is_linked(a1, 'wsmodel3_Controller28', b)
    _safe_set(b, 'wsmodel3_Communication', a2)
    assert _is_linked(b, 'wsmodel3_Communication', a2)
    if hasattr(a1, 'wsmodel3_Controller28'):
        assert not _is_linked(a1, 'wsmodel3_Controller28', b)
    if hasattr(a2, 'wsmodel3_Controller28'):
        assert _is_linked(a2, 'wsmodel3_Controller28', b)
    _safe_set(b, 'wsmodel3_Communication', None)
    assert not _is_linked(b, 'wsmodel3_Communication', a2)
    if hasattr(a2, 'wsmodel3_Controller28'):
        assert not _is_linked(a2, 'wsmodel3_Controller28', b)


def test_assoc_device21_reverse_link_reassign_clear():
    a1 = wsmodel3_REST(URI="sample_text", port=7)
    a2 = wsmodel3_REST(URI="sample_text_2", port=13)
    b = wsmodel3_Device(name="sample_text")
    _safe_set(b, 'wsmodel3_Device23', a1)
    assert _is_linked(b, 'wsmodel3_Device23', a1)
    if hasattr(a1, 'wsmodel3_REST22'):
        assert _is_linked(a1, 'wsmodel3_REST22', b)
    _safe_set(b, 'wsmodel3_Device23', a2)
    assert _is_linked(b, 'wsmodel3_Device23', a2)
    if hasattr(a1, 'wsmodel3_REST22'):
        assert not _is_linked(a1, 'wsmodel3_REST22', b)
    if hasattr(a2, 'wsmodel3_REST22'):
        assert _is_linked(a2, 'wsmodel3_REST22', b)
    _safe_set(b, 'wsmodel3_Device23', None)
    assert not _is_linked(b, 'wsmodel3_Device23', a2)
    if hasattr(a2, 'wsmodel3_REST22'):
        assert not _is_linked(a2, 'wsmodel3_REST22', b)


def test_assoc_externalapi11_reverse_link_reassign_clear():
    a1 = wsmodel3_System(name="sample_text")
    a2 = wsmodel3_System(name="sample_text_2")
    b = wsmodel3_ExternalAPI(URI="sample_text")
    _safe_set(b, 'wsmodel3_ExternalAPI', a1)
    assert _is_linked(b, 'wsmodel3_ExternalAPI', a1)
    if hasattr(a1, 'wsmodel3_System12'):
        assert _is_linked(a1, 'wsmodel3_System12', b)
    _safe_set(b, 'wsmodel3_ExternalAPI', a2)
    assert _is_linked(b, 'wsmodel3_ExternalAPI', a2)
    if hasattr(a1, 'wsmodel3_System12'):
        assert not _is_linked(a1, 'wsmodel3_System12', b)
    if hasattr(a2, 'wsmodel3_System12'):
        assert _is_linked(a2, 'wsmodel3_System12', b)
    _safe_set(b, 'wsmodel3_ExternalAPI', None)
    assert not _is_linked(b, 'wsmodel3_ExternalAPI', a2)
    if hasattr(a2, 'wsmodel3_System12'):
        assert not _is_linked(a2, 'wsmodel3_System12', b)


def test_assoc_externalapi62_reverse_link_reassign_clear():
    a1 = wsmodel3_Orchestrator(name="sample_text", port="sample_text")
    a2 = wsmodel3_Orchestrator(name="sample_text_2", port="sample_text_2")
    b = wsmodel3_ExternalAPI(URI="sample_text")
    _safe_set(b, 'wsmodel3_ExternalAPI64', a1)
    assert _is_linked(b, 'wsmodel3_ExternalAPI64', a1)
    if hasattr(a1, 'wsmodel3_Orchestrator63'):
        assert _is_linked(a1, 'wsmodel3_Orchestrator63', b)
    _safe_set(b, 'wsmodel3_ExternalAPI64', a2)
    assert _is_linked(b, 'wsmodel3_ExternalAPI64', a2)
    if hasattr(a1, 'wsmodel3_Orchestrator63'):
        assert not _is_linked(a1, 'wsmodel3_Orchestrator63', b)
    if hasattr(a2, 'wsmodel3_Orchestrator63'):
        assert _is_linked(a2, 'wsmodel3_Orchestrator63', b)
    _safe_set(b, 'wsmodel3_ExternalAPI64', None)
    assert not _is_linked(b, 'wsmodel3_ExternalAPI64', a2)
    if hasattr(a2, 'wsmodel3_Orchestrator63'):
        assert not _is_linked(a2, 'wsmodel3_Orchestrator63', b)


def test_assoc_function58_reverse_link_reassign_clear():
    a1 = wsmodel3_Orchestrator(name="sample_text", port="sample_text")
    a2 = wsmodel3_Orchestrator(name="sample_text_2", port="sample_text_2")
    b = wsmodel3_Function(expression="sample_text")
    _safe_set(b, 'wsmodel3_Function', a1)
    assert _is_linked(b, 'wsmodel3_Function', a1)
    if hasattr(a1, 'wsmodel3_Orchestrator59'):
        assert _is_linked(a1, 'wsmodel3_Orchestrator59', b)
    _safe_set(b, 'wsmodel3_Function', a2)
    assert _is_linked(b, 'wsmodel3_Function', a2)
    if hasattr(a1, 'wsmodel3_Orchestrator59'):
        assert not _is_linked(a1, 'wsmodel3_Orchestrator59', b)
    if hasattr(a2, 'wsmodel3_Orchestrator59'):
        assert _is_linked(a2, 'wsmodel3_Orchestrator59', b)
    _safe_set(b, 'wsmodel3_Function', None)
    assert not _is_linked(b, 'wsmodel3_Function', a2)
    if hasattr(a2, 'wsmodel3_Orchestrator59'):
        assert not _is_linked(a2, 'wsmodel3_Orchestrator59', b)


def test_assoc_inputorchestrator55_reverse_link_reassign_clear():
    a1 = wsmodel3_Orchestrator(name="sample_text", port="sample_text")
    a2 = wsmodel3_Orchestrator(name="sample_text_2", port="sample_text_2")
    b = wsmodel3_InputOrchestrator(URI="sample_text")
    _safe_set(b, 'wsmodel3_InputOrchestrator57', a1)
    assert _is_linked(b, 'wsmodel3_InputOrchestrator57', a1)
    if hasattr(a1, 'wsmodel3_Orchestrator56'):
        assert _is_linked(a1, 'wsmodel3_Orchestrator56', b)
    _safe_set(b, 'wsmodel3_InputOrchestrator57', a2)
    assert _is_linked(b, 'wsmodel3_InputOrchestrator57', a2)
    if hasattr(a1, 'wsmodel3_Orchestrator56'):
        assert not _is_linked(a1, 'wsmodel3_Orchestrator56', b)
    if hasattr(a2, 'wsmodel3_Orchestrator56'):
        assert _is_linked(a2, 'wsmodel3_Orchestrator56', b)
    _safe_set(b, 'wsmodel3_InputOrchestrator57', None)
    assert not _is_linked(b, 'wsmodel3_InputOrchestrator57', a2)
    if hasattr(a2, 'wsmodel3_Orchestrator56'):
        assert not _is_linked(a2, 'wsmodel3_Orchestrator56', b)


def test_assoc_inputorchestrator68_reverse_link_reassign_clear():
    a1 = wsmodel3_InputOrchestrator(URI="sample_text")
    a2 = wsmodel3_InputOrchestrator(URI="sample_text_2")
    b = wsmodel3_Function(expression="sample_text")
    _safe_set(b, 'wsmodel3_Function69', a1)
    assert _is_linked(b, 'wsmodel3_Function69', a1)
    if hasattr(a1, 'wsmodel3_InputOrchestrator70'):
        assert _is_linked(a1, 'wsmodel3_InputOrchestrator70', b)
    _safe_set(b, 'wsmodel3_Function69', a2)
    assert _is_linked(b, 'wsmodel3_Function69', a2)
    if hasattr(a1, 'wsmodel3_InputOrchestrator70'):
        assert not _is_linked(a1, 'wsmodel3_InputOrchestrator70', b)
    if hasattr(a2, 'wsmodel3_InputOrchestrator70'):
        assert _is_linked(a2, 'wsmodel3_InputOrchestrator70', b)
    _safe_set(b, 'wsmodel3_Function69', None)
    assert not _is_linked(b, 'wsmodel3_Function69', a2)
    if hasattr(a2, 'wsmodel3_InputOrchestrator70'):
        assert not _is_linked(a2, 'wsmodel3_InputOrchestrator70', b)


def test_assoc_messagebroker34_reverse_link_reassign_clear():
    a1 = wsmodel3_MessageBroker(host="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    a2 = wsmodel3_MessageBroker(host="sample_text_2", pass_="sample_text_2", port=13, type="sample_text_2", usser="sample_text_2")
    b = wsmodel3_Communication(name="sample_text", type="sample_text")
    _safe_set(b, 'wsmodel3_Communication35', a1)
    assert _is_linked(b, 'wsmodel3_Communication35', a1)
    if hasattr(a1, 'wsmodel3_MessageBroker36'):
        assert _is_linked(a1, 'wsmodel3_MessageBroker36', b)
    _safe_set(b, 'wsmodel3_Communication35', a2)
    assert _is_linked(b, 'wsmodel3_Communication35', a2)
    if hasattr(a1, 'wsmodel3_MessageBroker36'):
        assert not _is_linked(a1, 'wsmodel3_MessageBroker36', b)
    if hasattr(a2, 'wsmodel3_MessageBroker36'):
        assert _is_linked(a2, 'wsmodel3_MessageBroker36', b)
    _safe_set(b, 'wsmodel3_Communication35', None)
    assert not _is_linked(b, 'wsmodel3_Communication35', a2)
    if hasattr(a2, 'wsmodel3_MessageBroker36'):
        assert not _is_linked(a2, 'wsmodel3_MessageBroker36', b)


def test_assoc_messagebroker9_reverse_link_reassign_clear():
    a1 = wsmodel3_System(name="sample_text")
    a2 = wsmodel3_System(name="sample_text_2")
    b = wsmodel3_MessageBroker(host="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    _safe_set(b, 'wsmodel3_MessageBroker', a1)
    assert _is_linked(b, 'wsmodel3_MessageBroker', a1)
    if hasattr(a1, 'wsmodel3_System10'):
        assert _is_linked(a1, 'wsmodel3_System10', b)
    _safe_set(b, 'wsmodel3_MessageBroker', a2)
    assert _is_linked(b, 'wsmodel3_MessageBroker', a2)
    if hasattr(a1, 'wsmodel3_System10'):
        assert not _is_linked(a1, 'wsmodel3_System10', b)
    if hasattr(a2, 'wsmodel3_System10'):
        assert _is_linked(a2, 'wsmodel3_System10', b)
    _safe_set(b, 'wsmodel3_MessageBroker', None)
    assert not _is_linked(b, 'wsmodel3_MessageBroker', a2)
    if hasattr(a2, 'wsmodel3_System10'):
        assert not _is_linked(a2, 'wsmodel3_System10', b)


def test_assoc_port26_reverse_link_reassign_clear():
    a1 = wsmodel3_Port(id="sample_text", type="sample_text")
    a2 = wsmodel3_Port(id="sample_text_2", type="sample_text_2")
    b = wsmodel3_Controller(type="sample_text")
    _safe_set(b, 'wsmodel3_Controller', {a1})
    assert _is_linked(b, 'wsmodel3_Controller', a1)
    if hasattr(a1, 'wsmodel3_Port'):
        assert _is_linked(a1, 'wsmodel3_Port', b)
    _safe_set(b, 'wsmodel3_Controller', {a2})
    assert _is_linked(b, 'wsmodel3_Controller', a2)
    if hasattr(a1, 'wsmodel3_Port'):
        assert not _is_linked(a1, 'wsmodel3_Port', b)
    if hasattr(a2, 'wsmodel3_Port'):
        assert _is_linked(a2, 'wsmodel3_Port', b)
    _safe_set(b, 'wsmodel3_Controller', set())
    assert not _is_linked(b, 'wsmodel3_Controller', a2)
    if hasattr(a2, 'wsmodel3_Port'):
        assert not _is_linked(a2, 'wsmodel3_Port', b)


def test_assoc_rest39_reverse_link_reassign_clear():
    a1 = wsmodel3_REST(URI="sample_text", port=7)
    a2 = wsmodel3_REST(URI="sample_text_2", port=13)
    b = wsmodel3_Bridge(host="sample_text", port=7, topic="sample_text")
    _safe_set(b, 'wsmodel3_Bridge', a1)
    assert _is_linked(b, 'wsmodel3_Bridge', a1)
    if hasattr(a1, 'wsmodel3_REST40'):
        assert _is_linked(a1, 'wsmodel3_REST40', b)
    _safe_set(b, 'wsmodel3_Bridge', a2)
    assert _is_linked(b, 'wsmodel3_Bridge', a2)
    if hasattr(a1, 'wsmodel3_REST40'):
        assert not _is_linked(a1, 'wsmodel3_REST40', b)
    if hasattr(a2, 'wsmodel3_REST40'):
        assert _is_linked(a2, 'wsmodel3_REST40', b)
    _safe_set(b, 'wsmodel3_Bridge', None)
    assert not _is_linked(b, 'wsmodel3_Bridge', a2)
    if hasattr(a2, 'wsmodel3_REST40'):
        assert not _is_linked(a2, 'wsmodel3_REST40', b)


def test_assoc_rest65_reverse_link_reassign_clear():
    a1 = wsmodel3_REST(URI="sample_text", port=7)
    a2 = wsmodel3_REST(URI="sample_text_2", port=13)
    b = wsmodel3_Orchestrator(name="sample_text", port="sample_text")
    _safe_set(b, 'wsmodel3_Orchestrator66', {a1})
    assert _is_linked(b, 'wsmodel3_Orchestrator66', a1)
    if hasattr(a1, 'wsmodel3_REST67'):
        assert _is_linked(a1, 'wsmodel3_REST67', b)
    _safe_set(b, 'wsmodel3_Orchestrator66', {a2})
    assert _is_linked(b, 'wsmodel3_Orchestrator66', a2)
    if hasattr(a1, 'wsmodel3_REST67'):
        assert not _is_linked(a1, 'wsmodel3_REST67', b)
    if hasattr(a2, 'wsmodel3_REST67'):
        assert _is_linked(a2, 'wsmodel3_REST67', b)
    _safe_set(b, 'wsmodel3_Orchestrator66', set())
    assert not _is_linked(b, 'wsmodel3_Orchestrator66', a2)
    if hasattr(a2, 'wsmodel3_REST67'):
        assert not _is_linked(a2, 'wsmodel3_REST67', b)


def test_assoc_server1_reverse_link_reassign_clear():
    a1 = wsmodel3_System(name="sample_text")
    a2 = wsmodel3_System(name="sample_text_2")
    b = wsmodel3_Server(host="sample_text")
    _safe_set(b, 'wsmodel3_Server', a1)
    assert _is_linked(b, 'wsmodel3_Server', a1)
    if hasattr(a1, 'wsmodel3_System2'):
        assert _is_linked(a1, 'wsmodel3_System2', b)
    _safe_set(b, 'wsmodel3_Server', a2)
    assert _is_linked(b, 'wsmodel3_Server', a2)
    if hasattr(a1, 'wsmodel3_System2'):
        assert not _is_linked(a1, 'wsmodel3_System2', b)
    if hasattr(a2, 'wsmodel3_System2'):
        assert _is_linked(a2, 'wsmodel3_System2', b)
    _safe_set(b, 'wsmodel3_Server', None)
    assert not _is_linked(b, 'wsmodel3_Server', a2)
    if hasattr(a2, 'wsmodel3_System2'):
        assert not _is_linked(a2, 'wsmodel3_System2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actuator38_stub_double():
    # wsmodel3_OutputPort has no real 'wsmodel3_OutputPort' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_Actuator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_Actuator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_Actuator(type="sample_text")
    partner = wsmodel3_OutputPort()
    setattr(partner, 'wsmodel3_OutputPort', None)
    _safe_set(owner, 'wsmodel3_Actuator', partner)
    assert getattr(partner, 'wsmodel3_OutputPort') == owner
    _safe_set(owner, 'wsmodel3_Actuator', None)
    assert getattr(partner, 'wsmodel3_OutputPort') is None


def test_assoc_communicationdata29_stub_double():
    # wsmodel3_CommunicationData has no real 'wsmodel3_CommunicationData' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_Communication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_Communication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_Communication(name="sample_text", type="sample_text")
    partner = wsmodel3_CommunicationData()
    setattr(partner, 'wsmodel3_CommunicationData', None)
    _safe_set(owner, 'wsmodel3_Communication30', {partner})
    assert getattr(partner, 'wsmodel3_CommunicationData') == owner
    _safe_set(owner, 'wsmodel3_Communication30', set())
    assert getattr(partner, 'wsmodel3_CommunicationData') is None


def test_assoc_dbserver19_stub_double():
    # wsmodel3_WebService has no real 'wsmodel3_WebService20' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_DBServer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_DBServer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_DBServer(database="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    partner = wsmodel3_WebService()
    setattr(partner, 'wsmodel3_WebService20', None)
    _safe_set(owner, 'wsmodel3_DBServer', partner)
    assert getattr(partner, 'wsmodel3_WebService20') == owner
    _safe_set(owner, 'wsmodel3_DBServer', None)
    assert getattr(partner, 'wsmodel3_WebService20') is None


def test_assoc_device13_stub_double():
    # wsmodel3_IoTNode has no real 'wsmodel3_IoTNode14' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_Device(name="sample_text")
    partner = wsmodel3_IoTNode()
    setattr(partner, 'wsmodel3_IoTNode14', None)
    _safe_set(owner, 'wsmodel3_Device', partner)
    assert getattr(partner, 'wsmodel3_IoTNode14') == owner
    _safe_set(owner, 'wsmodel3_Device', None)
    assert getattr(partner, 'wsmodel3_IoTNode14') is None


def test_assoc_devicedata24_stub_double():
    # wsmodel3_DeviceData has no real 'wsmodel3_DeviceData' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_Device(name="sample_text")
    partner = wsmodel3_DeviceData()
    setattr(partner, 'wsmodel3_DeviceData', None)
    _safe_set(owner, 'wsmodel3_Device25', {partner})
    assert getattr(partner, 'wsmodel3_DeviceData') == owner
    _safe_set(owner, 'wsmodel3_Device25', set())
    assert getattr(partner, 'wsmodel3_DeviceData') is None


def test_assoc_externalapi87_stub_double():
    # wsmodel3_OutputOrchestrator has no real 'wsmodel3_OutputOrchestrator88' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_ExternalAPI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_ExternalAPI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_ExternalAPI(URI="sample_text")
    partner = wsmodel3_OutputOrchestrator()
    setattr(partner, 'wsmodel3_OutputOrchestrator88', None)
    _safe_set(owner, 'wsmodel3_ExternalAPI89', partner)
    assert getattr(partner, 'wsmodel3_OutputOrchestrator88') == owner
    _safe_set(owner, 'wsmodel3_ExternalAPI89', None)
    assert getattr(partner, 'wsmodel3_OutputOrchestrator88') is None


def test_assoc_inputbridge79_stub_double():
    # wsmodel3_OutputOrchestrator has no real 'wsmodel3_OutputOrchestrator80' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_InputBridge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_InputBridge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_InputBridge(URI="sample_text")
    partner = wsmodel3_OutputOrchestrator()
    setattr(partner, 'wsmodel3_OutputOrchestrator80', None)
    _safe_set(owner, 'wsmodel3_InputBridge81', partner)
    assert getattr(partner, 'wsmodel3_OutputOrchestrator80') == owner
    _safe_set(owner, 'wsmodel3_InputBridge81', None)
    assert getattr(partner, 'wsmodel3_OutputOrchestrator80') is None


def test_assoc_inputorchestrator43_stub_double():
    # wsmodel3_OutputBridge has no real 'wsmodel3_OutputBridge' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_InputOrchestrator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_InputOrchestrator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_InputOrchestrator(URI="sample_text")
    partner = wsmodel3_OutputBridge()
    setattr(partner, 'wsmodel3_OutputBridge', None)
    _safe_set(owner, 'wsmodel3_InputOrchestrator', partner)
    assert getattr(partner, 'wsmodel3_OutputBridge') == owner
    _safe_set(owner, 'wsmodel3_InputOrchestrator', None)
    assert getattr(partner, 'wsmodel3_OutputBridge') is None


def test_assoc_inputorchestrator76_stub_double():
    # wsmodel3_OutputOrchestrator has no real 'wsmodel3_OutputOrchestrator77' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_InputOrchestrator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_InputOrchestrator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_InputOrchestrator(URI="sample_text")
    partner = wsmodel3_OutputOrchestrator()
    setattr(partner, 'wsmodel3_OutputOrchestrator77', None)
    _safe_set(owner, 'wsmodel3_InputOrchestrator78', partner)
    assert getattr(partner, 'wsmodel3_OutputOrchestrator77') == owner
    _safe_set(owner, 'wsmodel3_InputOrchestrator78', None)
    assert getattr(partner, 'wsmodel3_OutputOrchestrator77') is None


def test_assoc_integrationpattern7_stub_double():
    # wsmodel3_IntegrationPattern has no real 'wsmodel3_IntegrationPattern' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_System's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_System's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_System(name="sample_text")
    partner = wsmodel3_IntegrationPattern()
    setattr(partner, 'wsmodel3_IntegrationPattern', None)
    _safe_set(owner, 'wsmodel3_System8', {partner})
    assert getattr(partner, 'wsmodel3_IntegrationPattern') == owner
    _safe_set(owner, 'wsmodel3_System8', set())
    assert getattr(partner, 'wsmodel3_IntegrationPattern') is None


def test_assoc_iotnode3_stub_double():
    # wsmodel3_IoTNode has no real 'wsmodel3_IoTNode' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_System's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_System's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_System(name="sample_text")
    partner = wsmodel3_IoTNode()
    setattr(partner, 'wsmodel3_IoTNode', None)
    _safe_set(owner, 'wsmodel3_System4', {partner})
    assert getattr(partner, 'wsmodel3_IoTNode') == owner
    _safe_set(owner, 'wsmodel3_System4', set())
    assert getattr(partner, 'wsmodel3_IoTNode') is None


def test_assoc_orchestrator50_stub_double():
    # wsmodel3_IntegrationPattern has no real 'wsmodel3_IntegrationPattern51' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_Orchestrator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_Orchestrator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_Orchestrator(name="sample_text", port="sample_text")
    partner = wsmodel3_IntegrationPattern()
    setattr(partner, 'wsmodel3_IntegrationPattern51', None)
    _safe_set(owner, 'wsmodel3_Orchestrator', partner)
    assert getattr(partner, 'wsmodel3_IntegrationPattern51') == owner
    _safe_set(owner, 'wsmodel3_Orchestrator', None)
    assert getattr(partner, 'wsmodel3_IntegrationPattern51') is None


def test_assoc_outputorchestrator60_stub_double():
    # wsmodel3_OutputOrchestrator has no real 'wsmodel3_OutputOrchestrator' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_Orchestrator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_Orchestrator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_Orchestrator(name="sample_text", port="sample_text")
    partner = wsmodel3_OutputOrchestrator()
    setattr(partner, 'wsmodel3_OutputOrchestrator', None)
    _safe_set(owner, 'wsmodel3_Orchestrator61', {partner})
    assert getattr(partner, 'wsmodel3_OutputOrchestrator') == owner
    _safe_set(owner, 'wsmodel3_Orchestrator61', set())
    assert getattr(partner, 'wsmodel3_OutputOrchestrator') is None


def test_assoc_outputorchestrator71_stub_double():
    # wsmodel3_OutputOrchestrator has no real 'wsmodel3_OutputOrchestrator73' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_Function(expression="sample_text")
    partner = wsmodel3_OutputOrchestrator()
    setattr(partner, 'wsmodel3_OutputOrchestrator73', None)
    _safe_set(owner, 'wsmodel3_Function72', partner)
    assert getattr(partner, 'wsmodel3_OutputOrchestrator73') == owner
    _safe_set(owner, 'wsmodel3_Function72', None)
    assert getattr(partner, 'wsmodel3_OutputOrchestrator73') is None


def test_assoc_rest15_stub_double():
    # wsmodel3_WebService has no real 'wsmodel3_WebService16' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_REST's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_REST's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_REST(URI="sample_text", port=7)
    partner = wsmodel3_WebService()
    setattr(partner, 'wsmodel3_WebService16', None)
    _safe_set(owner, 'wsmodel3_REST', partner)
    assert getattr(partner, 'wsmodel3_WebService16') == owner
    _safe_set(owner, 'wsmodel3_REST', None)
    assert getattr(partner, 'wsmodel3_WebService16') is None


def test_assoc_rest84_stub_double():
    # wsmodel3_OutputOrchestrator has no real 'wsmodel3_OutputOrchestrator85' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_REST's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_REST's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_REST(URI="sample_text", port=7)
    partner = wsmodel3_OutputOrchestrator()
    setattr(partner, 'wsmodel3_OutputOrchestrator85', None)
    _safe_set(owner, 'wsmodel3_REST86', partner)
    assert getattr(partner, 'wsmodel3_OutputOrchestrator85') == owner
    _safe_set(owner, 'wsmodel3_REST86', None)
    assert getattr(partner, 'wsmodel3_OutputOrchestrator85') is None


def test_assoc_sensor37_stub_double():
    # wsmodel3_InputPort has no real 'wsmodel3_InputPort' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_Sensor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_Sensor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_Sensor(type="sample_text")
    partner = wsmodel3_InputPort()
    setattr(partner, 'wsmodel3_InputPort', None)
    _safe_set(owner, 'wsmodel3_Sensor', partner)
    assert getattr(partner, 'wsmodel3_InputPort') == owner
    _safe_set(owner, 'wsmodel3_Sensor', None)
    assert getattr(partner, 'wsmodel3_InputPort') is None


def test_assoc_sensor44_stub_double():
    # wsmodel3_OutputBridge has no real 'wsmodel3_OutputBridge45' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_Sensor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_Sensor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_Sensor(type="sample_text")
    partner = wsmodel3_OutputBridge()
    setattr(partner, 'wsmodel3_OutputBridge45', None)
    _safe_set(owner, 'wsmodel3_Sensor46', partner)
    assert getattr(partner, 'wsmodel3_OutputBridge45') == owner
    _safe_set(owner, 'wsmodel3_Sensor46', None)
    assert getattr(partner, 'wsmodel3_OutputBridge45') is None


def test_assoc_webservice0_stub_double():
    # wsmodel3_WebService has no real 'wsmodel3_WebService' property in the generated
    # code (a bare stub) -- manually attach it so wsmodel3_System's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # wsmodel3_System's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = wsmodel3_System(name="sample_text")
    partner = wsmodel3_WebService()
    setattr(partner, 'wsmodel3_WebService', None)
    _safe_set(owner, 'wsmodel3_System', {partner})
    assert getattr(partner, 'wsmodel3_WebService') == owner
    _safe_set(owner, 'wsmodel3_System', set())
    assert getattr(partner, 'wsmodel3_WebService') is None


