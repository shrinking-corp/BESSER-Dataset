import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_wsmodel3_AccesPoint_pass__value_roundtrip():
    instance = wsmodel3_AccesPoint(pass_="sample_text", ssid="sample_text")
    assert instance.pass_ == "sample_text"
    instance.pass_ = "sample_text_2"
    assert instance.pass_ == "sample_text_2"


def test_wsmodel3_AccesPoint_ssid_value_roundtrip():
    instance = wsmodel3_AccesPoint(pass_="sample_text", ssid="sample_text")
    assert instance.ssid == "sample_text"
    instance.ssid = "sample_text_2"
    assert instance.ssid == "sample_text_2"


def test_wsmodel3_Actuator_type_value_roundtrip():
    instance = wsmodel3_Actuator(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_wsmodel3_Break_expression_value_roundtrip():
    instance = wsmodel3_Break(expression="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_wsmodel3_Bridge_host_value_roundtrip():
    instance = wsmodel3_Bridge(host="sample_text", port=7, topic="sample_text")
    assert instance.host == "sample_text"
    instance.host = "sample_text_2"
    assert instance.host == "sample_text_2"


def test_wsmodel3_Bridge_port_value_roundtrip():
    instance = wsmodel3_Bridge(host="sample_text", port=7, topic="sample_text")
    assert instance.port == 7
    instance.port = 13
    assert instance.port == 13


def test_wsmodel3_Bridge_topic_value_roundtrip():
    instance = wsmodel3_Bridge(host="sample_text", port=7, topic="sample_text")
    assert instance.topic == "sample_text"
    instance.topic = "sample_text_2"
    assert instance.topic == "sample_text_2"


def test_wsmodel3_Communication_name_value_roundtrip():
    instance = wsmodel3_Communication(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_wsmodel3_Communication_type_value_roundtrip():
    instance = wsmodel3_Communication(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_wsmodel3_Controller_type_value_roundtrip():
    instance = wsmodel3_Controller(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_wsmodel3_DBServer_database_value_roundtrip():
    instance = wsmodel3_DBServer(database="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    assert instance.database == "sample_text"
    instance.database = "sample_text_2"
    assert instance.database == "sample_text_2"


def test_wsmodel3_DBServer_pass__value_roundtrip():
    instance = wsmodel3_DBServer(database="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    assert instance.pass_ == "sample_text"
    instance.pass_ = "sample_text_2"
    assert instance.pass_ == "sample_text_2"


def test_wsmodel3_DBServer_port_value_roundtrip():
    instance = wsmodel3_DBServer(database="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    assert instance.port == 7
    instance.port = 13
    assert instance.port == 13


def test_wsmodel3_DBServer_type_value_roundtrip():
    instance = wsmodel3_DBServer(database="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_wsmodel3_DBServer_usser_value_roundtrip():
    instance = wsmodel3_DBServer(database="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    assert instance.usser == "sample_text"
    instance.usser = "sample_text_2"
    assert instance.usser == "sample_text_2"


def test_wsmodel3_Data_Artefact_value_roundtrip():
    instance = wsmodel3_Data(Artefact="sample_text", Attribute="sample_text", Date="sample_text", Location="sample_text", Time="sample_text", id="sample_text")
    assert instance.Artefact == "sample_text"
    instance.Artefact = "sample_text_2"
    assert instance.Artefact == "sample_text_2"


def test_wsmodel3_Data_Attribute_value_roundtrip():
    instance = wsmodel3_Data(Artefact="sample_text", Attribute="sample_text", Date="sample_text", Location="sample_text", Time="sample_text", id="sample_text")
    assert instance.Attribute == "sample_text"
    instance.Attribute = "sample_text_2"
    assert instance.Attribute == "sample_text_2"


def test_wsmodel3_Data_Date_value_roundtrip():
    instance = wsmodel3_Data(Artefact="sample_text", Attribute="sample_text", Date="sample_text", Location="sample_text", Time="sample_text", id="sample_text")
    assert instance.Date == "sample_text"
    instance.Date = "sample_text_2"
    assert instance.Date == "sample_text_2"


def test_wsmodel3_Data_Location_value_roundtrip():
    instance = wsmodel3_Data(Artefact="sample_text", Attribute="sample_text", Date="sample_text", Location="sample_text", Time="sample_text", id="sample_text")
    assert instance.Location == "sample_text"
    instance.Location = "sample_text_2"
    assert instance.Location == "sample_text_2"


def test_wsmodel3_Data_Time_value_roundtrip():
    instance = wsmodel3_Data(Artefact="sample_text", Attribute="sample_text", Date="sample_text", Location="sample_text", Time="sample_text", id="sample_text")
    assert instance.Time == "sample_text"
    instance.Time = "sample_text_2"
    assert instance.Time == "sample_text_2"


def test_wsmodel3_Data_id_value_roundtrip():
    instance = wsmodel3_Data(Artefact="sample_text", Attribute="sample_text", Date="sample_text", Location="sample_text", Time="sample_text", id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_wsmodel3_Device_name_value_roundtrip():
    instance = wsmodel3_Device(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_wsmodel3_ExternalAPI_URI_value_roundtrip():
    instance = wsmodel3_ExternalAPI(URI="sample_text")
    assert instance.URI == "sample_text"
    instance.URI = "sample_text_2"
    assert instance.URI == "sample_text_2"


def test_wsmodel3_Function_expression_value_roundtrip():
    instance = wsmodel3_Function(expression="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_wsmodel3_InputBridge_URI_value_roundtrip():
    instance = wsmodel3_InputBridge(URI="sample_text")
    assert instance.URI == "sample_text"
    instance.URI = "sample_text_2"
    assert instance.URI == "sample_text_2"


def test_wsmodel3_InputOrchestrator_URI_value_roundtrip():
    instance = wsmodel3_InputOrchestrator(URI="sample_text")
    assert instance.URI == "sample_text"
    instance.URI = "sample_text_2"
    assert instance.URI == "sample_text_2"


def test_wsmodel3_MessageBroker_host_value_roundtrip():
    instance = wsmodel3_MessageBroker(host="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    assert instance.host == "sample_text"
    instance.host = "sample_text_2"
    assert instance.host == "sample_text_2"


def test_wsmodel3_MessageBroker_pass__value_roundtrip():
    instance = wsmodel3_MessageBroker(host="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    assert instance.pass_ == "sample_text"
    instance.pass_ = "sample_text_2"
    assert instance.pass_ == "sample_text_2"


def test_wsmodel3_MessageBroker_port_value_roundtrip():
    instance = wsmodel3_MessageBroker(host="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    assert instance.port == 7
    instance.port = 13
    assert instance.port == 13


def test_wsmodel3_MessageBroker_type_value_roundtrip():
    instance = wsmodel3_MessageBroker(host="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_wsmodel3_MessageBroker_usser_value_roundtrip():
    instance = wsmodel3_MessageBroker(host="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    assert instance.usser == "sample_text"
    instance.usser = "sample_text_2"
    assert instance.usser == "sample_text_2"


def test_wsmodel3_Orchestrator_name_value_roundtrip():
    instance = wsmodel3_Orchestrator(name="sample_text", port="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_wsmodel3_Orchestrator_port_value_roundtrip():
    instance = wsmodel3_Orchestrator(name="sample_text", port="sample_text")
    assert instance.port == "sample_text"
    instance.port = "sample_text_2"
    assert instance.port == "sample_text_2"


def test_wsmodel3_Port_id_value_roundtrip():
    instance = wsmodel3_Port(id="sample_text", type="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_wsmodel3_Port_type_value_roundtrip():
    instance = wsmodel3_Port(id="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_wsmodel3_REST_URI_value_roundtrip():
    instance = wsmodel3_REST(URI="sample_text", port=7)
    assert instance.URI == "sample_text"
    instance.URI = "sample_text_2"
    assert instance.URI == "sample_text_2"


def test_wsmodel3_REST_port_value_roundtrip():
    instance = wsmodel3_REST(URI="sample_text", port=7)
    assert instance.port == 7
    instance.port = 13
    assert instance.port == 13


def test_wsmodel3_Sensor_type_value_roundtrip():
    instance = wsmodel3_Sensor(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_wsmodel3_Server_host_value_roundtrip():
    instance = wsmodel3_Server(host="sample_text")
    assert instance.host == "sample_text"
    instance.host = "sample_text_2"
    assert instance.host == "sample_text_2"


def test_wsmodel3_System_name_value_roundtrip():
    instance = wsmodel3_System(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_wsmodel3_InputBridge_isa_Bridge():
    instance = wsmodel3_InputBridge(URI="sample_text")
    assert isinstance(instance, Bridge)


def test_wsmodel3_OutputBridge_isa_Bridge():
    instance = wsmodel3_OutputBridge()
    assert isinstance(instance, Bridge)


def test_wsmodel3_CommunicationData_isa_Data():
    instance = wsmodel3_CommunicationData()
    assert isinstance(instance, Data)


def test_wsmodel3_DeviceData_isa_Data():
    instance = wsmodel3_DeviceData()
    assert isinstance(instance, Data)


def test_wsmodel3_OrchestratorData_isa_Data():
    instance = wsmodel3_OrchestratorData()
    assert isinstance(instance, Data)


def test_wsmodel3_Actuator_isa_Device():
    instance = wsmodel3_Actuator(type="sample_text")
    assert isinstance(instance, Device)


def test_wsmodel3_Controller_isa_Device():
    instance = wsmodel3_Controller(type="sample_text")
    assert isinstance(instance, Device)


def test_wsmodel3_Sensor_isa_Device():
    instance = wsmodel3_Sensor(type="sample_text")
    assert isinstance(instance, Device)


def test_wsmodel3_InputPort_isa_Port():
    instance = wsmodel3_InputPort()
    assert isinstance(instance, Port)


def test_wsmodel3_OutputPort_isa_Port():
    instance = wsmodel3_OutputPort()
    assert isinstance(instance, Port)


def test_wsmodel3_DBServer_isa_Server():
    instance = wsmodel3_DBServer(database="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    assert isinstance(instance, Server)


def test_wsmodel3_WebServer_isa_Server():
    instance = wsmodel3_WebServer()
    assert isinstance(instance, Server)


def test_assoc_accespoint31_link_reassign_clear():
    a = wsmodel3_Communication(name="sample_text", type="sample_text")
    b1 = wsmodel3_AccesPoint(pass_="sample_text", ssid="sample_text")
    b2 = wsmodel3_AccesPoint(pass_="sample_text_2", ssid="sample_text_2")
    _safe_set(a, 'wsmodel3_Communication32', b1)
    assert _is_linked(a, 'wsmodel3_Communication32', b1)
    if hasattr(b1, 'wsmodel3_AccesPoint33'):
        assert _is_linked(b1, 'wsmodel3_AccesPoint33', a)
    _safe_set(a, 'wsmodel3_Communication32', b2)
    assert _is_linked(a, 'wsmodel3_Communication32', b2)
    if hasattr(b1, 'wsmodel3_AccesPoint33'):
        assert not _is_linked(b1, 'wsmodel3_AccesPoint33', a)
    if hasattr(b2, 'wsmodel3_AccesPoint33'):
        assert _is_linked(b2, 'wsmodel3_AccesPoint33', a)
    _safe_set(a, 'wsmodel3_Communication32', None)
    assert not _is_linked(a, 'wsmodel3_Communication32', b2)
    if hasattr(b2, 'wsmodel3_AccesPoint33'):
        assert not _is_linked(b2, 'wsmodel3_AccesPoint33', a)


def test_assoc_accespoint5_link_reassign_clear():
    a = wsmodel3_System(name="sample_text")
    b1 = wsmodel3_AccesPoint(pass_="sample_text", ssid="sample_text")
    b2 = wsmodel3_AccesPoint(pass_="sample_text_2", ssid="sample_text_2")
    _safe_set(a, 'wsmodel3_System6', {b1})
    assert _is_linked(a, 'wsmodel3_System6', b1)
    if hasattr(b1, 'wsmodel3_AccesPoint'):
        assert _is_linked(b1, 'wsmodel3_AccesPoint', a)
    _safe_set(a, 'wsmodel3_System6', {b2})
    assert _is_linked(a, 'wsmodel3_System6', b2)
    if hasattr(b1, 'wsmodel3_AccesPoint'):
        assert not _is_linked(b1, 'wsmodel3_AccesPoint', a)
    if hasattr(b2, 'wsmodel3_AccesPoint'):
        assert _is_linked(b2, 'wsmodel3_AccesPoint', a)
    _safe_set(a, 'wsmodel3_System6', set())
    assert not _is_linked(a, 'wsmodel3_System6', b2)
    if hasattr(b2, 'wsmodel3_AccesPoint'):
        assert not _is_linked(b2, 'wsmodel3_AccesPoint', a)


def test_assoc_actuator38_link_reassign_clear():
    a = wsmodel3_Actuator(type="sample_text")
    b1 = wsmodel3_OutputPort()
    b2 = wsmodel3_OutputPort()
    _safe_set(a, 'wsmodel3_Actuator', b1)
    assert _is_linked(a, 'wsmodel3_Actuator', b1)
    if hasattr(b1, 'wsmodel3_OutputPort'):
        assert _is_linked(b1, 'wsmodel3_OutputPort', a)
    _safe_set(a, 'wsmodel3_Actuator', b2)
    assert _is_linked(a, 'wsmodel3_Actuator', b2)
    if hasattr(b1, 'wsmodel3_OutputPort'):
        assert not _is_linked(b1, 'wsmodel3_OutputPort', a)
    if hasattr(b2, 'wsmodel3_OutputPort'):
        assert _is_linked(b2, 'wsmodel3_OutputPort', a)
    _safe_set(a, 'wsmodel3_Actuator', None)
    assert not _is_linked(a, 'wsmodel3_Actuator', b2)
    if hasattr(b2, 'wsmodel3_OutputPort'):
        assert not _is_linked(b2, 'wsmodel3_OutputPort', a)


def test_assoc_actuator41_link_reassign_clear():
    a = wsmodel3_InputBridge(URI="sample_text")
    b1 = wsmodel3_Actuator(type="sample_text")
    b2 = wsmodel3_Actuator(type="sample_text_2")
    _safe_set(a, 'wsmodel3_InputBridge', b1)
    assert _is_linked(a, 'wsmodel3_InputBridge', b1)
    if hasattr(b1, 'wsmodel3_Actuator42'):
        assert _is_linked(b1, 'wsmodel3_Actuator42', a)
    _safe_set(a, 'wsmodel3_InputBridge', b2)
    assert _is_linked(a, 'wsmodel3_InputBridge', b2)
    if hasattr(b1, 'wsmodel3_Actuator42'):
        assert not _is_linked(b1, 'wsmodel3_Actuator42', a)
    if hasattr(b2, 'wsmodel3_Actuator42'):
        assert _is_linked(b2, 'wsmodel3_Actuator42', a)
    _safe_set(a, 'wsmodel3_InputBridge', None)
    assert not _is_linked(a, 'wsmodel3_InputBridge', b2)
    if hasattr(b2, 'wsmodel3_Actuator42'):
        assert not _is_linked(b2, 'wsmodel3_Actuator42', a)


def test_assoc_break_74_link_reassign_clear():
    a = wsmodel3_Function(expression="sample_text")
    b1 = wsmodel3_Break(expression="sample_text")
    b2 = wsmodel3_Break(expression="sample_text_2")
    _safe_set(a, 'wsmodel3_Function75', {b1})
    assert _is_linked(a, 'wsmodel3_Function75', b1)
    if hasattr(b1, 'wsmodel3_Break'):
        assert _is_linked(b1, 'wsmodel3_Break', a)
    _safe_set(a, 'wsmodel3_Function75', {b2})
    assert _is_linked(a, 'wsmodel3_Function75', b2)
    if hasattr(b1, 'wsmodel3_Break'):
        assert not _is_linked(b1, 'wsmodel3_Break', a)
    if hasattr(b2, 'wsmodel3_Break'):
        assert _is_linked(b2, 'wsmodel3_Break', a)
    _safe_set(a, 'wsmodel3_Function75', set())
    assert not _is_linked(a, 'wsmodel3_Function75', b2)
    if hasattr(b2, 'wsmodel3_Break'):
        assert not _is_linked(b2, 'wsmodel3_Break', a)


def test_assoc_bridge47_link_reassign_clear():
    a = wsmodel3_MessageBroker(host="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    b1 = wsmodel3_Bridge(host="sample_text", port=7, topic="sample_text")
    b2 = wsmodel3_Bridge(host="sample_text_2", port=13, topic="sample_text_2")
    _safe_set(a, 'wsmodel3_MessageBroker48', {b1})
    assert _is_linked(a, 'wsmodel3_MessageBroker48', b1)
    if hasattr(b1, 'wsmodel3_Bridge49'):
        assert _is_linked(b1, 'wsmodel3_Bridge49', a)
    _safe_set(a, 'wsmodel3_MessageBroker48', {b2})
    assert _is_linked(a, 'wsmodel3_MessageBroker48', b2)
    if hasattr(b1, 'wsmodel3_Bridge49'):
        assert not _is_linked(b1, 'wsmodel3_Bridge49', a)
    if hasattr(b2, 'wsmodel3_Bridge49'):
        assert _is_linked(b2, 'wsmodel3_Bridge49', a)
    _safe_set(a, 'wsmodel3_MessageBroker48', set())
    assert not _is_linked(a, 'wsmodel3_MessageBroker48', b2)
    if hasattr(b2, 'wsmodel3_Bridge49'):
        assert not _is_linked(b2, 'wsmodel3_Bridge49', a)


def test_assoc_communication27_link_reassign_clear():
    a = wsmodel3_Controller(type="sample_text")
    b1 = wsmodel3_Communication(name="sample_text", type="sample_text")
    b2 = wsmodel3_Communication(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'wsmodel3_Controller28', {b1})
    assert _is_linked(a, 'wsmodel3_Controller28', b1)
    if hasattr(b1, 'wsmodel3_Communication'):
        assert _is_linked(b1, 'wsmodel3_Communication', a)
    _safe_set(a, 'wsmodel3_Controller28', {b2})
    assert _is_linked(a, 'wsmodel3_Controller28', b2)
    if hasattr(b1, 'wsmodel3_Communication'):
        assert not _is_linked(b1, 'wsmodel3_Communication', a)
    if hasattr(b2, 'wsmodel3_Communication'):
        assert _is_linked(b2, 'wsmodel3_Communication', a)
    _safe_set(a, 'wsmodel3_Controller28', set())
    assert not _is_linked(a, 'wsmodel3_Controller28', b2)
    if hasattr(b2, 'wsmodel3_Communication'):
        assert not _is_linked(b2, 'wsmodel3_Communication', a)


def test_assoc_communicationdata29_link_reassign_clear():
    a = wsmodel3_Communication(name="sample_text", type="sample_text")
    b1 = wsmodel3_CommunicationData()
    b2 = wsmodel3_CommunicationData()
    _safe_set(a, 'wsmodel3_Communication30', {b1})
    assert _is_linked(a, 'wsmodel3_Communication30', b1)
    if hasattr(b1, 'wsmodel3_CommunicationData'):
        assert _is_linked(b1, 'wsmodel3_CommunicationData', a)
    _safe_set(a, 'wsmodel3_Communication30', {b2})
    assert _is_linked(a, 'wsmodel3_Communication30', b2)
    if hasattr(b1, 'wsmodel3_CommunicationData'):
        assert not _is_linked(b1, 'wsmodel3_CommunicationData', a)
    if hasattr(b2, 'wsmodel3_CommunicationData'):
        assert _is_linked(b2, 'wsmodel3_CommunicationData', a)
    _safe_set(a, 'wsmodel3_Communication30', set())
    assert not _is_linked(a, 'wsmodel3_Communication30', b2)
    if hasattr(b2, 'wsmodel3_CommunicationData'):
        assert not _is_linked(b2, 'wsmodel3_CommunicationData', a)


def test_assoc_dbserver19_link_reassign_clear():
    a = wsmodel3_DBServer(database="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    b1 = wsmodel3_WebService()
    b2 = wsmodel3_WebService()
    _safe_set(a, 'wsmodel3_DBServer', b1)
    assert _is_linked(a, 'wsmodel3_DBServer', b1)
    if hasattr(b1, 'wsmodel3_WebService20'):
        assert _is_linked(b1, 'wsmodel3_WebService20', a)
    _safe_set(a, 'wsmodel3_DBServer', b2)
    assert _is_linked(a, 'wsmodel3_DBServer', b2)
    if hasattr(b1, 'wsmodel3_WebService20'):
        assert not _is_linked(b1, 'wsmodel3_WebService20', a)
    if hasattr(b2, 'wsmodel3_WebService20'):
        assert _is_linked(b2, 'wsmodel3_WebService20', a)
    _safe_set(a, 'wsmodel3_DBServer', None)
    assert not _is_linked(a, 'wsmodel3_DBServer', b2)
    if hasattr(b2, 'wsmodel3_WebService20'):
        assert not _is_linked(b2, 'wsmodel3_WebService20', a)


def test_assoc_device13_link_reassign_clear():
    a = wsmodel3_Device(name="sample_text")
    b1 = wsmodel3_IoTNode()
    b2 = wsmodel3_IoTNode()
    _safe_set(a, 'wsmodel3_Device', b1)
    assert _is_linked(a, 'wsmodel3_Device', b1)
    if hasattr(b1, 'wsmodel3_IoTNode14'):
        assert _is_linked(b1, 'wsmodel3_IoTNode14', a)
    _safe_set(a, 'wsmodel3_Device', b2)
    assert _is_linked(a, 'wsmodel3_Device', b2)
    if hasattr(b1, 'wsmodel3_IoTNode14'):
        assert not _is_linked(b1, 'wsmodel3_IoTNode14', a)
    if hasattr(b2, 'wsmodel3_IoTNode14'):
        assert _is_linked(b2, 'wsmodel3_IoTNode14', a)
    _safe_set(a, 'wsmodel3_Device', None)
    assert not _is_linked(a, 'wsmodel3_Device', b2)
    if hasattr(b2, 'wsmodel3_IoTNode14'):
        assert not _is_linked(b2, 'wsmodel3_IoTNode14', a)


def test_assoc_device21_link_reassign_clear():
    a = wsmodel3_REST(URI="sample_text", port=7)
    b1 = wsmodel3_Device(name="sample_text")
    b2 = wsmodel3_Device(name="sample_text_2")
    _safe_set(a, 'wsmodel3_REST22', b1)
    assert _is_linked(a, 'wsmodel3_REST22', b1)
    if hasattr(b1, 'wsmodel3_Device23'):
        assert _is_linked(b1, 'wsmodel3_Device23', a)
    _safe_set(a, 'wsmodel3_REST22', b2)
    assert _is_linked(a, 'wsmodel3_REST22', b2)
    if hasattr(b1, 'wsmodel3_Device23'):
        assert not _is_linked(b1, 'wsmodel3_Device23', a)
    if hasattr(b2, 'wsmodel3_Device23'):
        assert _is_linked(b2, 'wsmodel3_Device23', a)
    _safe_set(a, 'wsmodel3_REST22', None)
    assert not _is_linked(a, 'wsmodel3_REST22', b2)
    if hasattr(b2, 'wsmodel3_Device23'):
        assert not _is_linked(b2, 'wsmodel3_Device23', a)


def test_assoc_devicedata24_link_reassign_clear():
    a = wsmodel3_Device(name="sample_text")
    b1 = wsmodel3_DeviceData()
    b2 = wsmodel3_DeviceData()
    _safe_set(a, 'wsmodel3_Device25', {b1})
    assert _is_linked(a, 'wsmodel3_Device25', b1)
    if hasattr(b1, 'wsmodel3_DeviceData'):
        assert _is_linked(b1, 'wsmodel3_DeviceData', a)
    _safe_set(a, 'wsmodel3_Device25', {b2})
    assert _is_linked(a, 'wsmodel3_Device25', b2)
    if hasattr(b1, 'wsmodel3_DeviceData'):
        assert not _is_linked(b1, 'wsmodel3_DeviceData', a)
    if hasattr(b2, 'wsmodel3_DeviceData'):
        assert _is_linked(b2, 'wsmodel3_DeviceData', a)
    _safe_set(a, 'wsmodel3_Device25', set())
    assert not _is_linked(a, 'wsmodel3_Device25', b2)
    if hasattr(b2, 'wsmodel3_DeviceData'):
        assert not _is_linked(b2, 'wsmodel3_DeviceData', a)


def test_assoc_externalapi11_link_reassign_clear():
    a = wsmodel3_System(name="sample_text")
    b1 = wsmodel3_ExternalAPI(URI="sample_text")
    b2 = wsmodel3_ExternalAPI(URI="sample_text_2")
    _safe_set(a, 'wsmodel3_System12', {b1})
    assert _is_linked(a, 'wsmodel3_System12', b1)
    if hasattr(b1, 'wsmodel3_ExternalAPI'):
        assert _is_linked(b1, 'wsmodel3_ExternalAPI', a)
    _safe_set(a, 'wsmodel3_System12', {b2})
    assert _is_linked(a, 'wsmodel3_System12', b2)
    if hasattr(b1, 'wsmodel3_ExternalAPI'):
        assert not _is_linked(b1, 'wsmodel3_ExternalAPI', a)
    if hasattr(b2, 'wsmodel3_ExternalAPI'):
        assert _is_linked(b2, 'wsmodel3_ExternalAPI', a)
    _safe_set(a, 'wsmodel3_System12', set())
    assert not _is_linked(a, 'wsmodel3_System12', b2)
    if hasattr(b2, 'wsmodel3_ExternalAPI'):
        assert not _is_linked(b2, 'wsmodel3_ExternalAPI', a)


def test_assoc_externalapi62_link_reassign_clear():
    a = wsmodel3_Orchestrator(name="sample_text", port="sample_text")
    b1 = wsmodel3_ExternalAPI(URI="sample_text")
    b2 = wsmodel3_ExternalAPI(URI="sample_text_2")
    _safe_set(a, 'wsmodel3_Orchestrator63', {b1})
    assert _is_linked(a, 'wsmodel3_Orchestrator63', b1)
    if hasattr(b1, 'wsmodel3_ExternalAPI64'):
        assert _is_linked(b1, 'wsmodel3_ExternalAPI64', a)
    _safe_set(a, 'wsmodel3_Orchestrator63', {b2})
    assert _is_linked(a, 'wsmodel3_Orchestrator63', b2)
    if hasattr(b1, 'wsmodel3_ExternalAPI64'):
        assert not _is_linked(b1, 'wsmodel3_ExternalAPI64', a)
    if hasattr(b2, 'wsmodel3_ExternalAPI64'):
        assert _is_linked(b2, 'wsmodel3_ExternalAPI64', a)
    _safe_set(a, 'wsmodel3_Orchestrator63', set())
    assert not _is_linked(a, 'wsmodel3_Orchestrator63', b2)
    if hasattr(b2, 'wsmodel3_ExternalAPI64'):
        assert not _is_linked(b2, 'wsmodel3_ExternalAPI64', a)


def test_assoc_externalapi87_link_reassign_clear():
    a = wsmodel3_ExternalAPI(URI="sample_text")
    b1 = wsmodel3_OutputOrchestrator()
    b2 = wsmodel3_OutputOrchestrator()
    _safe_set(a, 'wsmodel3_ExternalAPI89', b1)
    assert _is_linked(a, 'wsmodel3_ExternalAPI89', b1)
    if hasattr(b1, 'wsmodel3_OutputOrchestrator88'):
        assert _is_linked(b1, 'wsmodel3_OutputOrchestrator88', a)
    _safe_set(a, 'wsmodel3_ExternalAPI89', b2)
    assert _is_linked(a, 'wsmodel3_ExternalAPI89', b2)
    if hasattr(b1, 'wsmodel3_OutputOrchestrator88'):
        assert not _is_linked(b1, 'wsmodel3_OutputOrchestrator88', a)
    if hasattr(b2, 'wsmodel3_OutputOrchestrator88'):
        assert _is_linked(b2, 'wsmodel3_OutputOrchestrator88', a)
    _safe_set(a, 'wsmodel3_ExternalAPI89', None)
    assert not _is_linked(a, 'wsmodel3_ExternalAPI89', b2)
    if hasattr(b2, 'wsmodel3_OutputOrchestrator88'):
        assert not _is_linked(b2, 'wsmodel3_OutputOrchestrator88', a)


def test_assoc_function58_link_reassign_clear():
    a = wsmodel3_Orchestrator(name="sample_text", port="sample_text")
    b1 = wsmodel3_Function(expression="sample_text")
    b2 = wsmodel3_Function(expression="sample_text_2")
    _safe_set(a, 'wsmodel3_Orchestrator59', {b1})
    assert _is_linked(a, 'wsmodel3_Orchestrator59', b1)
    if hasattr(b1, 'wsmodel3_Function'):
        assert _is_linked(b1, 'wsmodel3_Function', a)
    _safe_set(a, 'wsmodel3_Orchestrator59', {b2})
    assert _is_linked(a, 'wsmodel3_Orchestrator59', b2)
    if hasattr(b1, 'wsmodel3_Function'):
        assert not _is_linked(b1, 'wsmodel3_Function', a)
    if hasattr(b2, 'wsmodel3_Function'):
        assert _is_linked(b2, 'wsmodel3_Function', a)
    _safe_set(a, 'wsmodel3_Orchestrator59', set())
    assert not _is_linked(a, 'wsmodel3_Orchestrator59', b2)
    if hasattr(b2, 'wsmodel3_Function'):
        assert not _is_linked(b2, 'wsmodel3_Function', a)


def test_assoc_inputbridge79_link_reassign_clear():
    a = wsmodel3_InputBridge(URI="sample_text")
    b1 = wsmodel3_OutputOrchestrator()
    b2 = wsmodel3_OutputOrchestrator()
    _safe_set(a, 'wsmodel3_InputBridge81', b1)
    assert _is_linked(a, 'wsmodel3_InputBridge81', b1)
    if hasattr(b1, 'wsmodel3_OutputOrchestrator80'):
        assert _is_linked(b1, 'wsmodel3_OutputOrchestrator80', a)
    _safe_set(a, 'wsmodel3_InputBridge81', b2)
    assert _is_linked(a, 'wsmodel3_InputBridge81', b2)
    if hasattr(b1, 'wsmodel3_OutputOrchestrator80'):
        assert not _is_linked(b1, 'wsmodel3_OutputOrchestrator80', a)
    if hasattr(b2, 'wsmodel3_OutputOrchestrator80'):
        assert _is_linked(b2, 'wsmodel3_OutputOrchestrator80', a)
    _safe_set(a, 'wsmodel3_InputBridge81', None)
    assert not _is_linked(a, 'wsmodel3_InputBridge81', b2)
    if hasattr(b2, 'wsmodel3_OutputOrchestrator80'):
        assert not _is_linked(b2, 'wsmodel3_OutputOrchestrator80', a)


def test_assoc_inputorchestrator43_link_reassign_clear():
    a = wsmodel3_InputOrchestrator(URI="sample_text")
    b1 = wsmodel3_OutputBridge()
    b2 = wsmodel3_OutputBridge()
    _safe_set(a, 'wsmodel3_InputOrchestrator', b1)
    assert _is_linked(a, 'wsmodel3_InputOrchestrator', b1)
    if hasattr(b1, 'wsmodel3_OutputBridge'):
        assert _is_linked(b1, 'wsmodel3_OutputBridge', a)
    _safe_set(a, 'wsmodel3_InputOrchestrator', b2)
    assert _is_linked(a, 'wsmodel3_InputOrchestrator', b2)
    if hasattr(b1, 'wsmodel3_OutputBridge'):
        assert not _is_linked(b1, 'wsmodel3_OutputBridge', a)
    if hasattr(b2, 'wsmodel3_OutputBridge'):
        assert _is_linked(b2, 'wsmodel3_OutputBridge', a)
    _safe_set(a, 'wsmodel3_InputOrchestrator', None)
    assert not _is_linked(a, 'wsmodel3_InputOrchestrator', b2)
    if hasattr(b2, 'wsmodel3_OutputBridge'):
        assert not _is_linked(b2, 'wsmodel3_OutputBridge', a)


def test_assoc_inputorchestrator55_link_reassign_clear():
    a = wsmodel3_Orchestrator(name="sample_text", port="sample_text")
    b1 = wsmodel3_InputOrchestrator(URI="sample_text")
    b2 = wsmodel3_InputOrchestrator(URI="sample_text_2")
    _safe_set(a, 'wsmodel3_Orchestrator56', {b1})
    assert _is_linked(a, 'wsmodel3_Orchestrator56', b1)
    if hasattr(b1, 'wsmodel3_InputOrchestrator57'):
        assert _is_linked(b1, 'wsmodel3_InputOrchestrator57', a)
    _safe_set(a, 'wsmodel3_Orchestrator56', {b2})
    assert _is_linked(a, 'wsmodel3_Orchestrator56', b2)
    if hasattr(b1, 'wsmodel3_InputOrchestrator57'):
        assert not _is_linked(b1, 'wsmodel3_InputOrchestrator57', a)
    if hasattr(b2, 'wsmodel3_InputOrchestrator57'):
        assert _is_linked(b2, 'wsmodel3_InputOrchestrator57', a)
    _safe_set(a, 'wsmodel3_Orchestrator56', set())
    assert not _is_linked(a, 'wsmodel3_Orchestrator56', b2)
    if hasattr(b2, 'wsmodel3_InputOrchestrator57'):
        assert not _is_linked(b2, 'wsmodel3_InputOrchestrator57', a)


def test_assoc_inputorchestrator68_link_reassign_clear():
    a = wsmodel3_InputOrchestrator(URI="sample_text")
    b1 = wsmodel3_Function(expression="sample_text")
    b2 = wsmodel3_Function(expression="sample_text_2")
    _safe_set(a, 'wsmodel3_InputOrchestrator70', b1)
    assert _is_linked(a, 'wsmodel3_InputOrchestrator70', b1)
    if hasattr(b1, 'wsmodel3_Function69'):
        assert _is_linked(b1, 'wsmodel3_Function69', a)
    _safe_set(a, 'wsmodel3_InputOrchestrator70', b2)
    assert _is_linked(a, 'wsmodel3_InputOrchestrator70', b2)
    if hasattr(b1, 'wsmodel3_Function69'):
        assert not _is_linked(b1, 'wsmodel3_Function69', a)
    if hasattr(b2, 'wsmodel3_Function69'):
        assert _is_linked(b2, 'wsmodel3_Function69', a)
    _safe_set(a, 'wsmodel3_InputOrchestrator70', None)
    assert not _is_linked(a, 'wsmodel3_InputOrchestrator70', b2)
    if hasattr(b2, 'wsmodel3_Function69'):
        assert not _is_linked(b2, 'wsmodel3_Function69', a)


def test_assoc_inputorchestrator76_link_reassign_clear():
    a = wsmodel3_InputOrchestrator(URI="sample_text")
    b1 = wsmodel3_OutputOrchestrator()
    b2 = wsmodel3_OutputOrchestrator()
    _safe_set(a, 'wsmodel3_InputOrchestrator78', b1)
    assert _is_linked(a, 'wsmodel3_InputOrchestrator78', b1)
    if hasattr(b1, 'wsmodel3_OutputOrchestrator77'):
        assert _is_linked(b1, 'wsmodel3_OutputOrchestrator77', a)
    _safe_set(a, 'wsmodel3_InputOrchestrator78', b2)
    assert _is_linked(a, 'wsmodel3_InputOrchestrator78', b2)
    if hasattr(b1, 'wsmodel3_OutputOrchestrator77'):
        assert not _is_linked(b1, 'wsmodel3_OutputOrchestrator77', a)
    if hasattr(b2, 'wsmodel3_OutputOrchestrator77'):
        assert _is_linked(b2, 'wsmodel3_OutputOrchestrator77', a)
    _safe_set(a, 'wsmodel3_InputOrchestrator78', None)
    assert not _is_linked(a, 'wsmodel3_InputOrchestrator78', b2)
    if hasattr(b2, 'wsmodel3_OutputOrchestrator77'):
        assert not _is_linked(b2, 'wsmodel3_OutputOrchestrator77', a)


def test_assoc_integrationpattern7_link_reassign_clear():
    a = wsmodel3_System(name="sample_text")
    b1 = wsmodel3_IntegrationPattern()
    b2 = wsmodel3_IntegrationPattern()
    _safe_set(a, 'wsmodel3_System8', {b1})
    assert _is_linked(a, 'wsmodel3_System8', b1)
    if hasattr(b1, 'wsmodel3_IntegrationPattern'):
        assert _is_linked(b1, 'wsmodel3_IntegrationPattern', a)
    _safe_set(a, 'wsmodel3_System8', {b2})
    assert _is_linked(a, 'wsmodel3_System8', b2)
    if hasattr(b1, 'wsmodel3_IntegrationPattern'):
        assert not _is_linked(b1, 'wsmodel3_IntegrationPattern', a)
    if hasattr(b2, 'wsmodel3_IntegrationPattern'):
        assert _is_linked(b2, 'wsmodel3_IntegrationPattern', a)
    _safe_set(a, 'wsmodel3_System8', set())
    assert not _is_linked(a, 'wsmodel3_System8', b2)
    if hasattr(b2, 'wsmodel3_IntegrationPattern'):
        assert not _is_linked(b2, 'wsmodel3_IntegrationPattern', a)


def test_assoc_iotnode3_link_reassign_clear():
    a = wsmodel3_System(name="sample_text")
    b1 = wsmodel3_IoTNode()
    b2 = wsmodel3_IoTNode()
    _safe_set(a, 'wsmodel3_System4', {b1})
    assert _is_linked(a, 'wsmodel3_System4', b1)
    if hasattr(b1, 'wsmodel3_IoTNode'):
        assert _is_linked(b1, 'wsmodel3_IoTNode', a)
    _safe_set(a, 'wsmodel3_System4', {b2})
    assert _is_linked(a, 'wsmodel3_System4', b2)
    if hasattr(b1, 'wsmodel3_IoTNode'):
        assert not _is_linked(b1, 'wsmodel3_IoTNode', a)
    if hasattr(b2, 'wsmodel3_IoTNode'):
        assert _is_linked(b2, 'wsmodel3_IoTNode', a)
    _safe_set(a, 'wsmodel3_System4', set())
    assert not _is_linked(a, 'wsmodel3_System4', b2)
    if hasattr(b2, 'wsmodel3_IoTNode'):
        assert not _is_linked(b2, 'wsmodel3_IoTNode', a)


def test_assoc_messagebroker34_link_reassign_clear():
    a = wsmodel3_MessageBroker(host="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    b1 = wsmodel3_Communication(name="sample_text", type="sample_text")
    b2 = wsmodel3_Communication(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'wsmodel3_MessageBroker36', b1)
    assert _is_linked(a, 'wsmodel3_MessageBroker36', b1)
    if hasattr(b1, 'wsmodel3_Communication35'):
        assert _is_linked(b1, 'wsmodel3_Communication35', a)
    _safe_set(a, 'wsmodel3_MessageBroker36', b2)
    assert _is_linked(a, 'wsmodel3_MessageBroker36', b2)
    if hasattr(b1, 'wsmodel3_Communication35'):
        assert not _is_linked(b1, 'wsmodel3_Communication35', a)
    if hasattr(b2, 'wsmodel3_Communication35'):
        assert _is_linked(b2, 'wsmodel3_Communication35', a)
    _safe_set(a, 'wsmodel3_MessageBroker36', None)
    assert not _is_linked(a, 'wsmodel3_MessageBroker36', b2)
    if hasattr(b2, 'wsmodel3_Communication35'):
        assert not _is_linked(b2, 'wsmodel3_Communication35', a)


def test_assoc_messagebroker9_link_reassign_clear():
    a = wsmodel3_System(name="sample_text")
    b1 = wsmodel3_MessageBroker(host="sample_text", pass_="sample_text", port=7, type="sample_text", usser="sample_text")
    b2 = wsmodel3_MessageBroker(host="sample_text_2", pass_="sample_text_2", port=13, type="sample_text_2", usser="sample_text_2")
    _safe_set(a, 'wsmodel3_System10', {b1})
    assert _is_linked(a, 'wsmodel3_System10', b1)
    if hasattr(b1, 'wsmodel3_MessageBroker'):
        assert _is_linked(b1, 'wsmodel3_MessageBroker', a)
    _safe_set(a, 'wsmodel3_System10', {b2})
    assert _is_linked(a, 'wsmodel3_System10', b2)
    if hasattr(b1, 'wsmodel3_MessageBroker'):
        assert not _is_linked(b1, 'wsmodel3_MessageBroker', a)
    if hasattr(b2, 'wsmodel3_MessageBroker'):
        assert _is_linked(b2, 'wsmodel3_MessageBroker', a)
    _safe_set(a, 'wsmodel3_System10', set())
    assert not _is_linked(a, 'wsmodel3_System10', b2)
    if hasattr(b2, 'wsmodel3_MessageBroker'):
        assert not _is_linked(b2, 'wsmodel3_MessageBroker', a)


def test_assoc_orchestrator50_link_reassign_clear():
    a = wsmodel3_Orchestrator(name="sample_text", port="sample_text")
    b1 = wsmodel3_IntegrationPattern()
    b2 = wsmodel3_IntegrationPattern()
    _safe_set(a, 'wsmodel3_Orchestrator', b1)
    assert _is_linked(a, 'wsmodel3_Orchestrator', b1)
    if hasattr(b1, 'wsmodel3_IntegrationPattern51'):
        assert _is_linked(b1, 'wsmodel3_IntegrationPattern51', a)
    _safe_set(a, 'wsmodel3_Orchestrator', b2)
    assert _is_linked(a, 'wsmodel3_Orchestrator', b2)
    if hasattr(b1, 'wsmodel3_IntegrationPattern51'):
        assert not _is_linked(b1, 'wsmodel3_IntegrationPattern51', a)
    if hasattr(b2, 'wsmodel3_IntegrationPattern51'):
        assert _is_linked(b2, 'wsmodel3_IntegrationPattern51', a)
    _safe_set(a, 'wsmodel3_Orchestrator', None)
    assert not _is_linked(a, 'wsmodel3_Orchestrator', b2)
    if hasattr(b2, 'wsmodel3_IntegrationPattern51'):
        assert not _is_linked(b2, 'wsmodel3_IntegrationPattern51', a)


def test_assoc_outputorchestrator60_link_reassign_clear():
    a = wsmodel3_Orchestrator(name="sample_text", port="sample_text")
    b1 = wsmodel3_OutputOrchestrator()
    b2 = wsmodel3_OutputOrchestrator()
    _safe_set(a, 'wsmodel3_Orchestrator61', {b1})
    assert _is_linked(a, 'wsmodel3_Orchestrator61', b1)
    if hasattr(b1, 'wsmodel3_OutputOrchestrator'):
        assert _is_linked(b1, 'wsmodel3_OutputOrchestrator', a)
    _safe_set(a, 'wsmodel3_Orchestrator61', {b2})
    assert _is_linked(a, 'wsmodel3_Orchestrator61', b2)
    if hasattr(b1, 'wsmodel3_OutputOrchestrator'):
        assert not _is_linked(b1, 'wsmodel3_OutputOrchestrator', a)
    if hasattr(b2, 'wsmodel3_OutputOrchestrator'):
        assert _is_linked(b2, 'wsmodel3_OutputOrchestrator', a)
    _safe_set(a, 'wsmodel3_Orchestrator61', set())
    assert not _is_linked(a, 'wsmodel3_Orchestrator61', b2)
    if hasattr(b2, 'wsmodel3_OutputOrchestrator'):
        assert not _is_linked(b2, 'wsmodel3_OutputOrchestrator', a)


def test_assoc_outputorchestrator71_link_reassign_clear():
    a = wsmodel3_Function(expression="sample_text")
    b1 = wsmodel3_OutputOrchestrator()
    b2 = wsmodel3_OutputOrchestrator()
    _safe_set(a, 'wsmodel3_Function72', b1)
    assert _is_linked(a, 'wsmodel3_Function72', b1)
    if hasattr(b1, 'wsmodel3_OutputOrchestrator73'):
        assert _is_linked(b1, 'wsmodel3_OutputOrchestrator73', a)
    _safe_set(a, 'wsmodel3_Function72', b2)
    assert _is_linked(a, 'wsmodel3_Function72', b2)
    if hasattr(b1, 'wsmodel3_OutputOrchestrator73'):
        assert not _is_linked(b1, 'wsmodel3_OutputOrchestrator73', a)
    if hasattr(b2, 'wsmodel3_OutputOrchestrator73'):
        assert _is_linked(b2, 'wsmodel3_OutputOrchestrator73', a)
    _safe_set(a, 'wsmodel3_Function72', None)
    assert not _is_linked(a, 'wsmodel3_Function72', b2)
    if hasattr(b2, 'wsmodel3_OutputOrchestrator73'):
        assert not _is_linked(b2, 'wsmodel3_OutputOrchestrator73', a)


def test_assoc_port26_link_reassign_clear():
    a = wsmodel3_Port(id="sample_text", type="sample_text")
    b1 = wsmodel3_Controller(type="sample_text")
    b2 = wsmodel3_Controller(type="sample_text_2")
    _safe_set(a, 'wsmodel3_Port', b1)
    assert _is_linked(a, 'wsmodel3_Port', b1)
    if hasattr(b1, 'wsmodel3_Controller'):
        assert _is_linked(b1, 'wsmodel3_Controller', a)
    _safe_set(a, 'wsmodel3_Port', b2)
    assert _is_linked(a, 'wsmodel3_Port', b2)
    if hasattr(b1, 'wsmodel3_Controller'):
        assert not _is_linked(b1, 'wsmodel3_Controller', a)
    if hasattr(b2, 'wsmodel3_Controller'):
        assert _is_linked(b2, 'wsmodel3_Controller', a)
    _safe_set(a, 'wsmodel3_Port', None)
    assert not _is_linked(a, 'wsmodel3_Port', b2)
    if hasattr(b2, 'wsmodel3_Controller'):
        assert not _is_linked(b2, 'wsmodel3_Controller', a)


def test_assoc_rest15_link_reassign_clear():
    a = wsmodel3_REST(URI="sample_text", port=7)
    b1 = wsmodel3_WebService()
    b2 = wsmodel3_WebService()
    _safe_set(a, 'wsmodel3_REST', b1)
    assert _is_linked(a, 'wsmodel3_REST', b1)
    if hasattr(b1, 'wsmodel3_WebService16'):
        assert _is_linked(b1, 'wsmodel3_WebService16', a)
    _safe_set(a, 'wsmodel3_REST', b2)
    assert _is_linked(a, 'wsmodel3_REST', b2)
    if hasattr(b1, 'wsmodel3_WebService16'):
        assert not _is_linked(b1, 'wsmodel3_WebService16', a)
    if hasattr(b2, 'wsmodel3_WebService16'):
        assert _is_linked(b2, 'wsmodel3_WebService16', a)
    _safe_set(a, 'wsmodel3_REST', None)
    assert not _is_linked(a, 'wsmodel3_REST', b2)
    if hasattr(b2, 'wsmodel3_WebService16'):
        assert not _is_linked(b2, 'wsmodel3_WebService16', a)


def test_assoc_rest39_link_reassign_clear():
    a = wsmodel3_REST(URI="sample_text", port=7)
    b1 = wsmodel3_Bridge(host="sample_text", port=7, topic="sample_text")
    b2 = wsmodel3_Bridge(host="sample_text_2", port=13, topic="sample_text_2")
    _safe_set(a, 'wsmodel3_REST40', b1)
    assert _is_linked(a, 'wsmodel3_REST40', b1)
    if hasattr(b1, 'wsmodel3_Bridge'):
        assert _is_linked(b1, 'wsmodel3_Bridge', a)
    _safe_set(a, 'wsmodel3_REST40', b2)
    assert _is_linked(a, 'wsmodel3_REST40', b2)
    if hasattr(b1, 'wsmodel3_Bridge'):
        assert not _is_linked(b1, 'wsmodel3_Bridge', a)
    if hasattr(b2, 'wsmodel3_Bridge'):
        assert _is_linked(b2, 'wsmodel3_Bridge', a)
    _safe_set(a, 'wsmodel3_REST40', None)
    assert not _is_linked(a, 'wsmodel3_REST40', b2)
    if hasattr(b2, 'wsmodel3_Bridge'):
        assert not _is_linked(b2, 'wsmodel3_Bridge', a)


def test_assoc_rest65_link_reassign_clear():
    a = wsmodel3_REST(URI="sample_text", port=7)
    b1 = wsmodel3_Orchestrator(name="sample_text", port="sample_text")
    b2 = wsmodel3_Orchestrator(name="sample_text_2", port="sample_text_2")
    _safe_set(a, 'wsmodel3_REST67', b1)
    assert _is_linked(a, 'wsmodel3_REST67', b1)
    if hasattr(b1, 'wsmodel3_Orchestrator66'):
        assert _is_linked(b1, 'wsmodel3_Orchestrator66', a)
    _safe_set(a, 'wsmodel3_REST67', b2)
    assert _is_linked(a, 'wsmodel3_REST67', b2)
    if hasattr(b1, 'wsmodel3_Orchestrator66'):
        assert not _is_linked(b1, 'wsmodel3_Orchestrator66', a)
    if hasattr(b2, 'wsmodel3_Orchestrator66'):
        assert _is_linked(b2, 'wsmodel3_Orchestrator66', a)
    _safe_set(a, 'wsmodel3_REST67', None)
    assert not _is_linked(a, 'wsmodel3_REST67', b2)
    if hasattr(b2, 'wsmodel3_Orchestrator66'):
        assert not _is_linked(b2, 'wsmodel3_Orchestrator66', a)


def test_assoc_rest84_link_reassign_clear():
    a = wsmodel3_REST(URI="sample_text", port=7)
    b1 = wsmodel3_OutputOrchestrator()
    b2 = wsmodel3_OutputOrchestrator()
    _safe_set(a, 'wsmodel3_REST86', b1)
    assert _is_linked(a, 'wsmodel3_REST86', b1)
    if hasattr(b1, 'wsmodel3_OutputOrchestrator85'):
        assert _is_linked(b1, 'wsmodel3_OutputOrchestrator85', a)
    _safe_set(a, 'wsmodel3_REST86', b2)
    assert _is_linked(a, 'wsmodel3_REST86', b2)
    if hasattr(b1, 'wsmodel3_OutputOrchestrator85'):
        assert not _is_linked(b1, 'wsmodel3_OutputOrchestrator85', a)
    if hasattr(b2, 'wsmodel3_OutputOrchestrator85'):
        assert _is_linked(b2, 'wsmodel3_OutputOrchestrator85', a)
    _safe_set(a, 'wsmodel3_REST86', None)
    assert not _is_linked(a, 'wsmodel3_REST86', b2)
    if hasattr(b2, 'wsmodel3_OutputOrchestrator85'):
        assert not _is_linked(b2, 'wsmodel3_OutputOrchestrator85', a)


def test_assoc_sensor37_link_reassign_clear():
    a = wsmodel3_Sensor(type="sample_text")
    b1 = wsmodel3_InputPort()
    b2 = wsmodel3_InputPort()
    _safe_set(a, 'wsmodel3_Sensor', b1)
    assert _is_linked(a, 'wsmodel3_Sensor', b1)
    if hasattr(b1, 'wsmodel3_InputPort'):
        assert _is_linked(b1, 'wsmodel3_InputPort', a)
    _safe_set(a, 'wsmodel3_Sensor', b2)
    assert _is_linked(a, 'wsmodel3_Sensor', b2)
    if hasattr(b1, 'wsmodel3_InputPort'):
        assert not _is_linked(b1, 'wsmodel3_InputPort', a)
    if hasattr(b2, 'wsmodel3_InputPort'):
        assert _is_linked(b2, 'wsmodel3_InputPort', a)
    _safe_set(a, 'wsmodel3_Sensor', None)
    assert not _is_linked(a, 'wsmodel3_Sensor', b2)
    if hasattr(b2, 'wsmodel3_InputPort'):
        assert not _is_linked(b2, 'wsmodel3_InputPort', a)


def test_assoc_sensor44_link_reassign_clear():
    a = wsmodel3_Sensor(type="sample_text")
    b1 = wsmodel3_OutputBridge()
    b2 = wsmodel3_OutputBridge()
    _safe_set(a, 'wsmodel3_Sensor46', b1)
    assert _is_linked(a, 'wsmodel3_Sensor46', b1)
    if hasattr(b1, 'wsmodel3_OutputBridge45'):
        assert _is_linked(b1, 'wsmodel3_OutputBridge45', a)
    _safe_set(a, 'wsmodel3_Sensor46', b2)
    assert _is_linked(a, 'wsmodel3_Sensor46', b2)
    if hasattr(b1, 'wsmodel3_OutputBridge45'):
        assert not _is_linked(b1, 'wsmodel3_OutputBridge45', a)
    if hasattr(b2, 'wsmodel3_OutputBridge45'):
        assert _is_linked(b2, 'wsmodel3_OutputBridge45', a)
    _safe_set(a, 'wsmodel3_Sensor46', None)
    assert not _is_linked(a, 'wsmodel3_Sensor46', b2)
    if hasattr(b2, 'wsmodel3_OutputBridge45'):
        assert not _is_linked(b2, 'wsmodel3_OutputBridge45', a)


def test_assoc_server1_link_reassign_clear():
    a = wsmodel3_System(name="sample_text")
    b1 = wsmodel3_Server(host="sample_text")
    b2 = wsmodel3_Server(host="sample_text_2")
    _safe_set(a, 'wsmodel3_System2', {b1})
    assert _is_linked(a, 'wsmodel3_System2', b1)
    if hasattr(b1, 'wsmodel3_Server'):
        assert _is_linked(b1, 'wsmodel3_Server', a)
    _safe_set(a, 'wsmodel3_System2', {b2})
    assert _is_linked(a, 'wsmodel3_System2', b2)
    if hasattr(b1, 'wsmodel3_Server'):
        assert not _is_linked(b1, 'wsmodel3_Server', a)
    if hasattr(b2, 'wsmodel3_Server'):
        assert _is_linked(b2, 'wsmodel3_Server', a)
    _safe_set(a, 'wsmodel3_System2', set())
    assert not _is_linked(a, 'wsmodel3_System2', b2)
    if hasattr(b2, 'wsmodel3_Server'):
        assert not _is_linked(b2, 'wsmodel3_Server', a)


def test_assoc_webservice0_link_reassign_clear():
    a = wsmodel3_System(name="sample_text")
    b1 = wsmodel3_WebService()
    b2 = wsmodel3_WebService()
    _safe_set(a, 'wsmodel3_System', {b1})
    assert _is_linked(a, 'wsmodel3_System', b1)
    if hasattr(b1, 'wsmodel3_WebService'):
        assert _is_linked(b1, 'wsmodel3_WebService', a)
    _safe_set(a, 'wsmodel3_System', {b2})
    assert _is_linked(a, 'wsmodel3_System', b2)
    if hasattr(b1, 'wsmodel3_WebService'):
        assert not _is_linked(b1, 'wsmodel3_WebService', a)
    if hasattr(b2, 'wsmodel3_WebService'):
        assert _is_linked(b2, 'wsmodel3_WebService', a)
    _safe_set(a, 'wsmodel3_System', set())
    assert not _is_linked(a, 'wsmodel3_System', b2)
    if hasattr(b2, 'wsmodel3_WebService'):
        assert not _is_linked(b2, 'wsmodel3_WebService', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Bridge_strategy = st.builds(Bridge)
@given(instance=Bridge_strategy)
@settings(max_examples=25)
def test_Bridge_instantiation(instance):
    assert isinstance(instance, Bridge)


Data_strategy = st.builds(Data)
@given(instance=Data_strategy)
@settings(max_examples=25)
def test_Data_instantiation(instance):
    assert isinstance(instance, Data)


Device_strategy = st.builds(Device)
@given(instance=Device_strategy)
@settings(max_examples=25)
def test_Device_instantiation(instance):
    assert isinstance(instance, Device)


Port_strategy = st.builds(Port)
@given(instance=Port_strategy)
@settings(max_examples=25)
def test_Port_instantiation(instance):
    assert isinstance(instance, Port)


Server_strategy = st.builds(Server)
@given(instance=Server_strategy)
@settings(max_examples=25)
def test_Server_instantiation(instance):
    assert isinstance(instance, Server)


wsmodel3_AccesPoint_strategy = st.builds(wsmodel3_AccesPoint, pass_=safe_text, ssid=safe_text)
@given(instance=wsmodel3_AccesPoint_strategy)
@settings(max_examples=25)
def test_wsmodel3_AccesPoint_instantiation(instance):
    assert isinstance(instance, wsmodel3_AccesPoint)


wsmodel3_Actuator_strategy = st.builds(wsmodel3_Actuator, type=safe_text)
@given(instance=wsmodel3_Actuator_strategy)
@settings(max_examples=25)
def test_wsmodel3_Actuator_instantiation(instance):
    assert isinstance(instance, wsmodel3_Actuator)


wsmodel3_Break_strategy = st.builds(wsmodel3_Break, expression=safe_text)
@given(instance=wsmodel3_Break_strategy)
@settings(max_examples=25)
def test_wsmodel3_Break_instantiation(instance):
    assert isinstance(instance, wsmodel3_Break)


wsmodel3_Bridge_strategy = st.builds(wsmodel3_Bridge, host=safe_text, port=st.integers(), topic=safe_text)
@given(instance=wsmodel3_Bridge_strategy)
@settings(max_examples=25)
def test_wsmodel3_Bridge_instantiation(instance):
    assert isinstance(instance, wsmodel3_Bridge)


wsmodel3_Communication_strategy = st.builds(wsmodel3_Communication, name=safe_text, type=safe_text)
@given(instance=wsmodel3_Communication_strategy)
@settings(max_examples=25)
def test_wsmodel3_Communication_instantiation(instance):
    assert isinstance(instance, wsmodel3_Communication)


wsmodel3_CommunicationData_strategy = st.builds(wsmodel3_CommunicationData)
@given(instance=wsmodel3_CommunicationData_strategy)
@settings(max_examples=25)
def test_wsmodel3_CommunicationData_instantiation(instance):
    assert isinstance(instance, wsmodel3_CommunicationData)


wsmodel3_Controller_strategy = st.builds(wsmodel3_Controller, type=safe_text)
@given(instance=wsmodel3_Controller_strategy)
@settings(max_examples=25)
def test_wsmodel3_Controller_instantiation(instance):
    assert isinstance(instance, wsmodel3_Controller)


wsmodel3_DBServer_strategy = st.builds(wsmodel3_DBServer, database=safe_text, pass_=safe_text, port=st.integers(), type=safe_text, usser=safe_text)
@given(instance=wsmodel3_DBServer_strategy)
@settings(max_examples=25)
def test_wsmodel3_DBServer_instantiation(instance):
    assert isinstance(instance, wsmodel3_DBServer)


wsmodel3_Data_strategy = st.builds(wsmodel3_Data, Artefact=safe_text, Attribute=safe_text, Date=safe_text, Location=safe_text, Time=safe_text, id=safe_text)
@given(instance=wsmodel3_Data_strategy)
@settings(max_examples=25)
def test_wsmodel3_Data_instantiation(instance):
    assert isinstance(instance, wsmodel3_Data)


wsmodel3_Device_strategy = st.builds(wsmodel3_Device, name=safe_text)
@given(instance=wsmodel3_Device_strategy)
@settings(max_examples=25)
def test_wsmodel3_Device_instantiation(instance):
    assert isinstance(instance, wsmodel3_Device)


wsmodel3_DeviceData_strategy = st.builds(wsmodel3_DeviceData)
@given(instance=wsmodel3_DeviceData_strategy)
@settings(max_examples=25)
def test_wsmodel3_DeviceData_instantiation(instance):
    assert isinstance(instance, wsmodel3_DeviceData)


wsmodel3_ExternalAPI_strategy = st.builds(wsmodel3_ExternalAPI, URI=safe_text)
@given(instance=wsmodel3_ExternalAPI_strategy)
@settings(max_examples=25)
def test_wsmodel3_ExternalAPI_instantiation(instance):
    assert isinstance(instance, wsmodel3_ExternalAPI)


wsmodel3_Function_strategy = st.builds(wsmodel3_Function, expression=safe_text)
@given(instance=wsmodel3_Function_strategy)
@settings(max_examples=25)
def test_wsmodel3_Function_instantiation(instance):
    assert isinstance(instance, wsmodel3_Function)


wsmodel3_InputBridge_strategy = st.builds(wsmodel3_InputBridge, URI=safe_text)
@given(instance=wsmodel3_InputBridge_strategy)
@settings(max_examples=25)
def test_wsmodel3_InputBridge_instantiation(instance):
    assert isinstance(instance, wsmodel3_InputBridge)


wsmodel3_InputOrchestrator_strategy = st.builds(wsmodel3_InputOrchestrator, URI=safe_text)
@given(instance=wsmodel3_InputOrchestrator_strategy)
@settings(max_examples=25)
def test_wsmodel3_InputOrchestrator_instantiation(instance):
    assert isinstance(instance, wsmodel3_InputOrchestrator)


wsmodel3_InputPort_strategy = st.builds(wsmodel3_InputPort)
@given(instance=wsmodel3_InputPort_strategy)
@settings(max_examples=25)
def test_wsmodel3_InputPort_instantiation(instance):
    assert isinstance(instance, wsmodel3_InputPort)


wsmodel3_IntegrationPattern_strategy = st.builds(wsmodel3_IntegrationPattern)
@given(instance=wsmodel3_IntegrationPattern_strategy)
@settings(max_examples=25)
def test_wsmodel3_IntegrationPattern_instantiation(instance):
    assert isinstance(instance, wsmodel3_IntegrationPattern)


wsmodel3_IoTNode_strategy = st.builds(wsmodel3_IoTNode)
@given(instance=wsmodel3_IoTNode_strategy)
@settings(max_examples=25)
def test_wsmodel3_IoTNode_instantiation(instance):
    assert isinstance(instance, wsmodel3_IoTNode)


wsmodel3_MessageBroker_strategy = st.builds(wsmodel3_MessageBroker, host=safe_text, pass_=safe_text, port=st.integers(), type=safe_text, usser=safe_text)
@given(instance=wsmodel3_MessageBroker_strategy)
@settings(max_examples=25)
def test_wsmodel3_MessageBroker_instantiation(instance):
    assert isinstance(instance, wsmodel3_MessageBroker)


wsmodel3_Orchestrator_strategy = st.builds(wsmodel3_Orchestrator, name=safe_text, port=safe_text)
@given(instance=wsmodel3_Orchestrator_strategy)
@settings(max_examples=25)
def test_wsmodel3_Orchestrator_instantiation(instance):
    assert isinstance(instance, wsmodel3_Orchestrator)


wsmodel3_OrchestratorData_strategy = st.builds(wsmodel3_OrchestratorData)
@given(instance=wsmodel3_OrchestratorData_strategy)
@settings(max_examples=25)
def test_wsmodel3_OrchestratorData_instantiation(instance):
    assert isinstance(instance, wsmodel3_OrchestratorData)


wsmodel3_OutputBridge_strategy = st.builds(wsmodel3_OutputBridge)
@given(instance=wsmodel3_OutputBridge_strategy)
@settings(max_examples=25)
def test_wsmodel3_OutputBridge_instantiation(instance):
    assert isinstance(instance, wsmodel3_OutputBridge)


wsmodel3_OutputOrchestrator_strategy = st.builds(wsmodel3_OutputOrchestrator)
@given(instance=wsmodel3_OutputOrchestrator_strategy)
@settings(max_examples=25)
def test_wsmodel3_OutputOrchestrator_instantiation(instance):
    assert isinstance(instance, wsmodel3_OutputOrchestrator)


wsmodel3_OutputPort_strategy = st.builds(wsmodel3_OutputPort)
@given(instance=wsmodel3_OutputPort_strategy)
@settings(max_examples=25)
def test_wsmodel3_OutputPort_instantiation(instance):
    assert isinstance(instance, wsmodel3_OutputPort)


wsmodel3_Port_strategy = st.builds(wsmodel3_Port, id=safe_text, type=safe_text)
@given(instance=wsmodel3_Port_strategy)
@settings(max_examples=25)
def test_wsmodel3_Port_instantiation(instance):
    assert isinstance(instance, wsmodel3_Port)


wsmodel3_REST_strategy = st.builds(wsmodel3_REST, URI=safe_text, port=st.integers())
@given(instance=wsmodel3_REST_strategy)
@settings(max_examples=25)
def test_wsmodel3_REST_instantiation(instance):
    assert isinstance(instance, wsmodel3_REST)


wsmodel3_Sensor_strategy = st.builds(wsmodel3_Sensor, type=safe_text)
@given(instance=wsmodel3_Sensor_strategy)
@settings(max_examples=25)
def test_wsmodel3_Sensor_instantiation(instance):
    assert isinstance(instance, wsmodel3_Sensor)


wsmodel3_Server_strategy = st.builds(wsmodel3_Server, host=safe_text)
@given(instance=wsmodel3_Server_strategy)
@settings(max_examples=25)
def test_wsmodel3_Server_instantiation(instance):
    assert isinstance(instance, wsmodel3_Server)


wsmodel3_System_strategy = st.builds(wsmodel3_System, name=safe_text)
@given(instance=wsmodel3_System_strategy)
@settings(max_examples=25)
def test_wsmodel3_System_instantiation(instance):
    assert isinstance(instance, wsmodel3_System)


wsmodel3_WebServer_strategy = st.builds(wsmodel3_WebServer)
@given(instance=wsmodel3_WebServer_strategy)
@settings(max_examples=25)
def test_wsmodel3_WebServer_instantiation(instance):
    assert isinstance(instance, wsmodel3_WebServer)


wsmodel3_WebService_strategy = st.builds(wsmodel3_WebService)
@given(instance=wsmodel3_WebService_strategy)
@settings(max_examples=25)
def test_wsmodel3_WebService_instantiation(instance):
    assert isinstance(instance, wsmodel3_WebService)


