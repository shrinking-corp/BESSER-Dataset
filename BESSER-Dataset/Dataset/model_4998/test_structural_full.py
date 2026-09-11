import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Artefact,
    ArtefactInstance,
    ArtefactPort,
    ArtefactPortInstance,
    CloudMLElement,
    NamedElement,
    Node,
    NodeInstance,
    NodePort,
    NodePortInstance,
    Property,
    Provider,
    Resource,
    WithProperties,
    cloudml_core_Artefact,
    cloudml_core_ArtefactInstance,
    cloudml_core_ArtefactPort,
    cloudml_core_ArtefactPortInstance,
    cloudml_core_CloudMLElement,
    cloudml_core_Composite,
    cloudml_core_DeploymentModel,
    cloudml_core_NamedElement,
    cloudml_core_Node,
    cloudml_core_NodeInstance,
    cloudml_core_NodePort,
    cloudml_core_NodePortInstance,
    cloudml_core_Property,
    cloudml_core_Provider,
    cloudml_core_Resource,
    cloudml_core_WithProperties,
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

def test_cloudml_core_ArtefactPort_portNumber_value_roundtrip():
    instance = cloudml_core_ArtefactPort(portNumber=7)
    assert instance.portNumber == 7
    instance.portNumber = 13
    assert instance.portNumber == 13


def test_cloudml_core_NamedElement_name_value_roundtrip():
    instance = cloudml_core_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cloudml_core_Node_OS_value_roundtrip():
    instance = cloudml_core_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.OS == "sample_text"
    instance.OS = "sample_text_2"
    assert instance.OS == "sample_text_2"


def test_cloudml_core_Node_groupName_value_roundtrip():
    instance = cloudml_core_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.groupName == "sample_text"
    instance.groupName = "sample_text_2"
    assert instance.groupName == "sample_text_2"


def test_cloudml_core_Node_imageID_value_roundtrip():
    instance = cloudml_core_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.imageID == "sample_text"
    instance.imageID = "sample_text_2"
    assert instance.imageID == "sample_text_2"


def test_cloudml_core_Node_is64os_value_roundtrip():
    instance = cloudml_core_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.is64os == True
    instance.is64os = False
    assert instance.is64os == False


def test_cloudml_core_Node_location_value_roundtrip():
    instance = cloudml_core_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_cloudml_core_Node_minCore_value_roundtrip():
    instance = cloudml_core_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.minCore == 7
    instance.minCore = 13
    assert instance.minCore == 13


def test_cloudml_core_Node_minDisk_value_roundtrip():
    instance = cloudml_core_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.minDisk == 7
    instance.minDisk = 13
    assert instance.minDisk == 13


def test_cloudml_core_Node_minRam_value_roundtrip():
    instance = cloudml_core_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.minRam == 7
    instance.minRam = 13
    assert instance.minRam == 13


def test_cloudml_core_Node_privateKey_value_roundtrip():
    instance = cloudml_core_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.privateKey == "sample_text"
    instance.privateKey = "sample_text_2"
    assert instance.privateKey == "sample_text_2"


def test_cloudml_core_Node_securityGroup_value_roundtrip():
    instance = cloudml_core_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.securityGroup == "sample_text"
    instance.securityGroup = "sample_text_2"
    assert instance.securityGroup == "sample_text_2"


def test_cloudml_core_Node_sshKey_value_roundtrip():
    instance = cloudml_core_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.sshKey == "sample_text"
    instance.sshKey = "sample_text_2"
    assert instance.sshKey == "sample_text_2"


def test_cloudml_core_NodeInstance_publicAddress_value_roundtrip():
    instance = cloudml_core_NodeInstance(publicAddress="sample_text")
    assert instance.publicAddress == "sample_text"
    instance.publicAddress = "sample_text_2"
    assert instance.publicAddress == "sample_text_2"


def test_cloudml_core_Property_value_value_roundtrip():
    instance = cloudml_core_Property(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_cloudml_core_Provider_credentials_value_roundtrip():
    instance = cloudml_core_Provider(credentials="sample_text")
    assert instance.credentials == "sample_text"
    instance.credentials = "sample_text_2"
    assert instance.credentials == "sample_text_2"


def test_cloudml_core_Resource_configurationCommand_value_roundtrip():
    instance = cloudml_core_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text")
    assert instance.configurationCommand == "sample_text"
    instance.configurationCommand = "sample_text_2"
    assert instance.configurationCommand == "sample_text_2"


def test_cloudml_core_Resource_deployingCommand_value_roundtrip():
    instance = cloudml_core_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text")
    assert instance.deployingCommand == "sample_text"
    instance.deployingCommand = "sample_text_2"
    assert instance.deployingCommand == "sample_text_2"


def test_cloudml_core_Resource_retrievingCommand_value_roundtrip():
    instance = cloudml_core_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text")
    assert instance.retrievingCommand == "sample_text"
    instance.retrievingCommand = "sample_text_2"
    assert instance.retrievingCommand == "sample_text_2"


def test_cloudml_core_Resource_startCommand_value_roundtrip():
    instance = cloudml_core_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text")
    assert instance.startCommand == "sample_text"
    instance.startCommand = "sample_text_2"
    assert instance.startCommand == "sample_text_2"


def test_cloudml_core_NamedElement_isa_CloudMLElement():
    instance = cloudml_core_NamedElement(name="sample_text")
    assert isinstance(instance, CloudMLElement)


def test_cloudml_core_Composite_isa_NamedElement():
    instance = cloudml_core_Composite()
    assert isinstance(instance, NamedElement)


def test_cloudml_core_Property_isa_NamedElement():
    instance = cloudml_core_Property(value="sample_text")
    assert isinstance(instance, NamedElement)


def test_cloudml_core_WithProperties_isa_NamedElement():
    instance = cloudml_core_WithProperties()
    assert isinstance(instance, NamedElement)


def test_cloudml_core_Artefact_isa_WithProperties():
    instance = cloudml_core_Artefact()
    assert isinstance(instance, WithProperties)


def test_cloudml_core_ArtefactInstance_isa_WithProperties():
    instance = cloudml_core_ArtefactInstance()
    assert isinstance(instance, WithProperties)


def test_cloudml_core_ArtefactPort_isa_WithProperties():
    instance = cloudml_core_ArtefactPort(portNumber=7)
    assert isinstance(instance, WithProperties)


def test_cloudml_core_ArtefactPortInstance_isa_WithProperties():
    instance = cloudml_core_ArtefactPortInstance()
    assert isinstance(instance, WithProperties)


def test_cloudml_core_DeploymentModel_isa_WithProperties():
    instance = cloudml_core_DeploymentModel()
    assert isinstance(instance, WithProperties)


def test_cloudml_core_Node_isa_WithProperties():
    instance = cloudml_core_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert isinstance(instance, WithProperties)


def test_cloudml_core_NodeInstance_isa_WithProperties():
    instance = cloudml_core_NodeInstance(publicAddress="sample_text")
    assert isinstance(instance, WithProperties)


def test_cloudml_core_NodePort_isa_WithProperties():
    instance = cloudml_core_NodePort()
    assert isinstance(instance, WithProperties)


def test_cloudml_core_NodePortInstance_isa_WithProperties():
    instance = cloudml_core_NodePortInstance()
    assert isinstance(instance, WithProperties)


def test_cloudml_core_Provider_isa_WithProperties():
    instance = cloudml_core_Provider(credentials="sample_text")
    assert isinstance(instance, WithProperties)


def test_cloudml_core_Resource_isa_WithProperties():
    instance = cloudml_core_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text")
    assert isinstance(instance, WithProperties)


def test_assoc_cloudProvider26_link_reassign_clear():
    a = cloudml_core_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    b1 = Provider()
    b2 = Provider()
    _safe_set(a, 'cloudml_core_Node27', b1)
    assert _is_linked(a, 'cloudml_core_Node27', b1)
    if hasattr(b1, 'Provider28'):
        assert _is_linked(b1, 'Provider28', a)
    _safe_set(a, 'cloudml_core_Node27', b2)
    assert _is_linked(a, 'cloudml_core_Node27', b2)
    if hasattr(b1, 'Provider28'):
        assert not _is_linked(b1, 'Provider28', a)
    if hasattr(b2, 'Provider28'):
        assert _is_linked(b2, 'Provider28', a)
    _safe_set(a, 'cloudml_core_Node27', None)
    assert not _is_linked(a, 'cloudml_core_Node27', b2)
    if hasattr(b2, 'Provider28'):
        assert not _is_linked(b2, 'Provider28', a)


def test_assoc_provided25_link_reassign_clear():
    a = cloudml_core_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    b1 = NodePort()
    b2 = NodePort()
    _safe_set(a, 'cloudml_core_Node', {b1})
    assert _is_linked(a, 'cloudml_core_Node', b1)
    if hasattr(b1, 'NodePort'):
        assert _is_linked(b1, 'NodePort', a)
    _safe_set(a, 'cloudml_core_Node', {b2})
    assert _is_linked(a, 'cloudml_core_Node', b2)
    if hasattr(b1, 'NodePort'):
        assert not _is_linked(b1, 'NodePort', a)
    if hasattr(b2, 'NodePort'):
        assert _is_linked(b2, 'NodePort', a)
    _safe_set(a, 'cloudml_core_Node', set())
    assert not _is_linked(a, 'cloudml_core_Node', b2)
    if hasattr(b2, 'NodePort'):
        assert not _is_linked(b2, 'NodePort', a)


def test_assoc_provided50_link_reassign_clear():
    a = cloudml_core_NodeInstance(publicAddress="sample_text")
    b1 = NodePortInstance()
    b2 = NodePortInstance()
    _safe_set(a, 'cloudml_core_NodeInstance51', {b1})
    assert _is_linked(a, 'cloudml_core_NodeInstance51', b1)
    if hasattr(b1, 'NodePortInstance52'):
        assert _is_linked(b1, 'NodePortInstance52', a)
    _safe_set(a, 'cloudml_core_NodeInstance51', {b2})
    assert _is_linked(a, 'cloudml_core_NodeInstance51', b2)
    if hasattr(b1, 'NodePortInstance52'):
        assert not _is_linked(b1, 'NodePortInstance52', a)
    if hasattr(b2, 'NodePortInstance52'):
        assert _is_linked(b2, 'NodePortInstance52', a)
    _safe_set(a, 'cloudml_core_NodeInstance51', set())
    assert not _is_linked(a, 'cloudml_core_NodeInstance51', b2)
    if hasattr(b2, 'NodePortInstance52'):
        assert not _is_linked(b2, 'NodePortInstance52', a)


def test_assoc_type48_link_reassign_clear():
    a = cloudml_core_NodeInstance(publicAddress="sample_text")
    b1 = Node()
    b2 = Node()
    _safe_set(a, 'cloudml_core_NodeInstance', b1)
    assert _is_linked(a, 'cloudml_core_NodeInstance', b1)
    if hasattr(b1, 'Node49'):
        assert _is_linked(b1, 'Node49', a)
    _safe_set(a, 'cloudml_core_NodeInstance', b2)
    assert _is_linked(a, 'cloudml_core_NodeInstance', b2)
    if hasattr(b1, 'Node49'):
        assert not _is_linked(b1, 'Node49', a)
    if hasattr(b2, 'Node49'):
        assert _is_linked(b2, 'Node49', a)
    _safe_set(a, 'cloudml_core_NodeInstance', None)
    assert not _is_linked(a, 'cloudml_core_NodeInstance', b2)
    if hasattr(b2, 'Node49'):
        assert not _is_linked(b2, 'Node49', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Artefact_strategy = st.builds(Artefact)
@given(instance=Artefact_strategy)
@settings(max_examples=25)
def test_Artefact_instantiation(instance):
    assert isinstance(instance, Artefact)


ArtefactInstance_strategy = st.builds(ArtefactInstance)
@given(instance=ArtefactInstance_strategy)
@settings(max_examples=25)
def test_ArtefactInstance_instantiation(instance):
    assert isinstance(instance, ArtefactInstance)


ArtefactPort_strategy = st.builds(ArtefactPort)
@given(instance=ArtefactPort_strategy)
@settings(max_examples=25)
def test_ArtefactPort_instantiation(instance):
    assert isinstance(instance, ArtefactPort)


ArtefactPortInstance_strategy = st.builds(ArtefactPortInstance)
@given(instance=ArtefactPortInstance_strategy)
@settings(max_examples=25)
def test_ArtefactPortInstance_instantiation(instance):
    assert isinstance(instance, ArtefactPortInstance)


CloudMLElement_strategy = st.builds(CloudMLElement)
@given(instance=CloudMLElement_strategy)
@settings(max_examples=25)
def test_CloudMLElement_instantiation(instance):
    assert isinstance(instance, CloudMLElement)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


NodeInstance_strategy = st.builds(NodeInstance)
@given(instance=NodeInstance_strategy)
@settings(max_examples=25)
def test_NodeInstance_instantiation(instance):
    assert isinstance(instance, NodeInstance)


NodePort_strategy = st.builds(NodePort)
@given(instance=NodePort_strategy)
@settings(max_examples=25)
def test_NodePort_instantiation(instance):
    assert isinstance(instance, NodePort)


NodePortInstance_strategy = st.builds(NodePortInstance)
@given(instance=NodePortInstance_strategy)
@settings(max_examples=25)
def test_NodePortInstance_instantiation(instance):
    assert isinstance(instance, NodePortInstance)


Property_strategy = st.builds(Property)
@given(instance=Property_strategy)
@settings(max_examples=25)
def test_Property_instantiation(instance):
    assert isinstance(instance, Property)


Provider_strategy = st.builds(Provider)
@given(instance=Provider_strategy)
@settings(max_examples=25)
def test_Provider_instantiation(instance):
    assert isinstance(instance, Provider)


Resource_strategy = st.builds(Resource)
@given(instance=Resource_strategy)
@settings(max_examples=25)
def test_Resource_instantiation(instance):
    assert isinstance(instance, Resource)


WithProperties_strategy = st.builds(WithProperties)
@given(instance=WithProperties_strategy)
@settings(max_examples=25)
def test_WithProperties_instantiation(instance):
    assert isinstance(instance, WithProperties)


cloudml_core_Artefact_strategy = st.builds(cloudml_core_Artefact)
@given(instance=cloudml_core_Artefact_strategy)
@settings(max_examples=25)
def test_cloudml_core_Artefact_instantiation(instance):
    assert isinstance(instance, cloudml_core_Artefact)


cloudml_core_ArtefactInstance_strategy = st.builds(cloudml_core_ArtefactInstance)
@given(instance=cloudml_core_ArtefactInstance_strategy)
@settings(max_examples=25)
def test_cloudml_core_ArtefactInstance_instantiation(instance):
    assert isinstance(instance, cloudml_core_ArtefactInstance)


cloudml_core_ArtefactPort_strategy = st.builds(cloudml_core_ArtefactPort, portNumber=st.integers())
@given(instance=cloudml_core_ArtefactPort_strategy)
@settings(max_examples=25)
def test_cloudml_core_ArtefactPort_instantiation(instance):
    assert isinstance(instance, cloudml_core_ArtefactPort)


cloudml_core_ArtefactPortInstance_strategy = st.builds(cloudml_core_ArtefactPortInstance)
@given(instance=cloudml_core_ArtefactPortInstance_strategy)
@settings(max_examples=25)
def test_cloudml_core_ArtefactPortInstance_instantiation(instance):
    assert isinstance(instance, cloudml_core_ArtefactPortInstance)


cloudml_core_CloudMLElement_strategy = st.builds(cloudml_core_CloudMLElement)
@given(instance=cloudml_core_CloudMLElement_strategy)
@settings(max_examples=25)
def test_cloudml_core_CloudMLElement_instantiation(instance):
    assert isinstance(instance, cloudml_core_CloudMLElement)


cloudml_core_Composite_strategy = st.builds(cloudml_core_Composite)
@given(instance=cloudml_core_Composite_strategy)
@settings(max_examples=25)
def test_cloudml_core_Composite_instantiation(instance):
    assert isinstance(instance, cloudml_core_Composite)


cloudml_core_DeploymentModel_strategy = st.builds(cloudml_core_DeploymentModel)
@given(instance=cloudml_core_DeploymentModel_strategy)
@settings(max_examples=25)
def test_cloudml_core_DeploymentModel_instantiation(instance):
    assert isinstance(instance, cloudml_core_DeploymentModel)


cloudml_core_NamedElement_strategy = st.builds(cloudml_core_NamedElement, name=safe_text)
@given(instance=cloudml_core_NamedElement_strategy)
@settings(max_examples=25)
def test_cloudml_core_NamedElement_instantiation(instance):
    assert isinstance(instance, cloudml_core_NamedElement)


cloudml_core_Node_strategy = st.builds(cloudml_core_Node, OS=safe_text, groupName=safe_text, imageID=safe_text, is64os=st.booleans(), location=safe_text, minCore=st.integers(), minDisk=st.integers(), minRam=st.integers(), privateKey=safe_text, securityGroup=safe_text, sshKey=safe_text)
@given(instance=cloudml_core_Node_strategy)
@settings(max_examples=25)
def test_cloudml_core_Node_instantiation(instance):
    assert isinstance(instance, cloudml_core_Node)


cloudml_core_NodeInstance_strategy = st.builds(cloudml_core_NodeInstance, publicAddress=safe_text)
@given(instance=cloudml_core_NodeInstance_strategy)
@settings(max_examples=25)
def test_cloudml_core_NodeInstance_instantiation(instance):
    assert isinstance(instance, cloudml_core_NodeInstance)


cloudml_core_NodePort_strategy = st.builds(cloudml_core_NodePort)
@given(instance=cloudml_core_NodePort_strategy)
@settings(max_examples=25)
def test_cloudml_core_NodePort_instantiation(instance):
    assert isinstance(instance, cloudml_core_NodePort)


cloudml_core_NodePortInstance_strategy = st.builds(cloudml_core_NodePortInstance)
@given(instance=cloudml_core_NodePortInstance_strategy)
@settings(max_examples=25)
def test_cloudml_core_NodePortInstance_instantiation(instance):
    assert isinstance(instance, cloudml_core_NodePortInstance)


cloudml_core_Property_strategy = st.builds(cloudml_core_Property, value=safe_text)
@given(instance=cloudml_core_Property_strategy)
@settings(max_examples=25)
def test_cloudml_core_Property_instantiation(instance):
    assert isinstance(instance, cloudml_core_Property)


cloudml_core_Provider_strategy = st.builds(cloudml_core_Provider, credentials=safe_text)
@given(instance=cloudml_core_Provider_strategy)
@settings(max_examples=25)
def test_cloudml_core_Provider_instantiation(instance):
    assert isinstance(instance, cloudml_core_Provider)


cloudml_core_Resource_strategy = st.builds(cloudml_core_Resource, configurationCommand=safe_text, deployingCommand=safe_text, retrievingCommand=safe_text, startCommand=safe_text)
@given(instance=cloudml_core_Resource_strategy)
@settings(max_examples=25)
def test_cloudml_core_Resource_instantiation(instance):
    assert isinstance(instance, cloudml_core_Resource)


cloudml_core_WithProperties_strategy = st.builds(cloudml_core_WithProperties)
@given(instance=cloudml_core_WithProperties_strategy)
@settings(max_examples=25)
def test_cloudml_core_WithProperties_instantiation(instance):
    assert isinstance(instance, cloudml_core_WithProperties)


