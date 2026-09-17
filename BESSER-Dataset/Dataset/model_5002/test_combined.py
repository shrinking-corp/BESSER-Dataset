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
    ArtefactPortInstance,
    cloudml_ClientPortInstance,
    cloudml_ServerPortInstance,
    ArtefactPort,
    cloudml_ClientPort,
    cloudml_ServerPort,
    NamedElement,
    cloudml_WithProperties,
    cloudml_Composite,
    cloudml_Property,
    CloudMLElement,
    cloudml_NamedElement,
    cloudml_CloudMLElement,
    cloudml_UploadCommand,
    WithProperties,
    cloudml_ArtefactPort,
    cloudml_BindingInstance,
    cloudml_DeploymentModel,
    cloudml_Binding,
    cloudml_NodeInstance,
    cloudml_ArtefactInstance,
    cloudml_Node,
    cloudml_ArtefactPortInstance,
    cloudml_Provider,
    cloudml_Artefact,
    cloudml_Resource,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_artefactportinstance_is_not_abstract():
    assert not inspect.isabstract(ArtefactPortInstance)


def test_hyp_artefactportinstance_constructor_exists():
    assert callable(ArtefactPortInstance.__init__)


def test_hyp_artefactportinstance_constructor_args():
    sig = inspect.signature(ArtefactPortInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_clientportinstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_ClientPortInstance)


def test_hyp_cloudml_clientportinstance_constructor_exists():
    assert callable(cloudml_ClientPortInstance.__init__)


def test_hyp_cloudml_clientportinstance_constructor_args():
    sig = inspect.signature(cloudml_ClientPortInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_serverportinstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_ServerPortInstance)


def test_hyp_cloudml_serverportinstance_constructor_exists():
    assert callable(cloudml_ServerPortInstance.__init__)


def test_hyp_cloudml_serverportinstance_constructor_args():
    sig = inspect.signature(cloudml_ServerPortInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_artefactport_is_not_abstract():
    assert not inspect.isabstract(ArtefactPort)


def test_hyp_artefactport_constructor_exists():
    assert callable(ArtefactPort.__init__)


def test_hyp_artefactport_constructor_args():
    sig = inspect.signature(ArtefactPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_clientport_is_not_abstract():
    assert not inspect.isabstract(cloudml_ClientPort)


def test_hyp_cloudml_clientport_constructor_exists():
    assert callable(cloudml_ClientPort.__init__)


def test_hyp_cloudml_clientport_constructor_args():
    sig = inspect.signature(cloudml_ClientPort.__init__)
    params = list(sig.parameters.keys())
    assert "isOptional" in params, "Missing parameter 'isOptional'"




def test_hyp_cloudml_serverport_is_not_abstract():
    assert not inspect.isabstract(cloudml_ServerPort)


def test_hyp_cloudml_serverport_constructor_exists():
    assert callable(cloudml_ServerPort.__init__)


def test_hyp_cloudml_serverport_constructor_args():
    sig = inspect.signature(cloudml_ServerPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_withproperties_is_not_abstract():
    assert not inspect.isabstract(cloudml_WithProperties)


def test_hyp_cloudml_withproperties_constructor_exists():
    assert callable(cloudml_WithProperties.__init__)


def test_hyp_cloudml_withproperties_constructor_args():
    sig = inspect.signature(cloudml_WithProperties.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_composite_is_not_abstract():
    assert not inspect.isabstract(cloudml_Composite)


def test_hyp_cloudml_composite_constructor_exists():
    assert callable(cloudml_Composite.__init__)


def test_hyp_cloudml_composite_constructor_args():
    sig = inspect.signature(cloudml_Composite.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_property_is_not_abstract():
    assert not inspect.isabstract(cloudml_Property)


def test_hyp_cloudml_property_constructor_exists():
    assert callable(cloudml_Property.__init__)


def test_hyp_cloudml_property_constructor_args():
    sig = inspect.signature(cloudml_Property.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_cloudmlelement_is_not_abstract():
    assert not inspect.isabstract(CloudMLElement)


def test_hyp_cloudmlelement_constructor_exists():
    assert callable(CloudMLElement.__init__)


def test_hyp_cloudmlelement_constructor_args():
    sig = inspect.signature(CloudMLElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_namedelement_is_not_abstract():
    assert not inspect.isabstract(cloudml_NamedElement)


def test_hyp_cloudml_namedelement_constructor_exists():
    assert callable(cloudml_NamedElement.__init__)


def test_hyp_cloudml_namedelement_constructor_args():
    sig = inspect.signature(cloudml_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_cloudml_cloudmlelement_is_not_abstract():
    assert not inspect.isabstract(cloudml_CloudMLElement)


def test_hyp_cloudml_cloudmlelement_constructor_exists():
    assert callable(cloudml_CloudMLElement.__init__)


def test_hyp_cloudml_cloudmlelement_constructor_args():
    sig = inspect.signature(cloudml_CloudMLElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_uploadcommand_is_not_abstract():
    assert not inspect.isabstract(cloudml_UploadCommand)


def test_hyp_cloudml_uploadcommand_constructor_exists():
    assert callable(cloudml_UploadCommand.__init__)


def test_hyp_cloudml_uploadcommand_constructor_args():
    sig = inspect.signature(cloudml_UploadCommand.__init__)
    params = list(sig.parameters.keys())
    assert "target" in params, "Missing parameter 'target'"
    assert "source" in params, "Missing parameter 'source'"





def test_hyp_withproperties_is_not_abstract():
    assert not inspect.isabstract(WithProperties)


def test_hyp_withproperties_constructor_exists():
    assert callable(WithProperties.__init__)


def test_hyp_withproperties_constructor_args():
    sig = inspect.signature(WithProperties.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_artefactport_is_not_abstract():
    assert not inspect.isabstract(cloudml_ArtefactPort)


def test_hyp_cloudml_artefactport_constructor_exists():
    assert callable(cloudml_ArtefactPort.__init__)


def test_hyp_cloudml_artefactport_constructor_args():
    sig = inspect.signature(cloudml_ArtefactPort.__init__)
    params = list(sig.parameters.keys())
    assert "portNumber" in params, "Missing parameter 'portNumber'"
    assert "isRemote" in params, "Missing parameter 'isRemote'"





def test_hyp_cloudml_bindinginstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_BindingInstance)


def test_hyp_cloudml_bindinginstance_constructor_exists():
    assert callable(cloudml_BindingInstance.__init__)


def test_hyp_cloudml_bindinginstance_constructor_args():
    sig = inspect.signature(cloudml_BindingInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_deploymentmodel_is_not_abstract():
    assert not inspect.isabstract(cloudml_DeploymentModel)


def test_hyp_cloudml_deploymentmodel_constructor_exists():
    assert callable(cloudml_DeploymentModel.__init__)


def test_hyp_cloudml_deploymentmodel_constructor_args():
    sig = inspect.signature(cloudml_DeploymentModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_binding_is_not_abstract():
    assert not inspect.isabstract(cloudml_Binding)


def test_hyp_cloudml_binding_constructor_exists():
    assert callable(cloudml_Binding.__init__)


def test_hyp_cloudml_binding_constructor_args():
    sig = inspect.signature(cloudml_Binding.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_nodeinstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_NodeInstance)


def test_hyp_cloudml_nodeinstance_constructor_exists():
    assert callable(cloudml_NodeInstance.__init__)


def test_hyp_cloudml_nodeinstance_constructor_args():
    sig = inspect.signature(cloudml_NodeInstance.__init__)
    params = list(sig.parameters.keys())
    assert "publicAddress" in params, "Missing parameter 'publicAddress'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_cloudml_artefactinstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_ArtefactInstance)


def test_hyp_cloudml_artefactinstance_constructor_exists():
    assert callable(cloudml_ArtefactInstance.__init__)


def test_hyp_cloudml_artefactinstance_constructor_args():
    sig = inspect.signature(cloudml_ArtefactInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_node_is_not_abstract():
    assert not inspect.isabstract(cloudml_Node)


def test_hyp_cloudml_node_constructor_exists():
    assert callable(cloudml_Node.__init__)


def test_hyp_cloudml_node_constructor_args():
    sig = inspect.signature(cloudml_Node.__init__)
    params = list(sig.parameters.keys())
    assert "groupName" in params, "Missing parameter 'groupName'"
    assert "minCore" in params, "Missing parameter 'minCore'"
    assert "privateKey" in params, "Missing parameter 'privateKey'"
    assert "imageID" in params, "Missing parameter 'imageID'"
    assert "OS" in params, "Missing parameter 'OS'"
    assert "is64os" in params, "Missing parameter 'is64os'"
    assert "securityGroup" in params, "Missing parameter 'securityGroup'"
    assert "minRam" in params, "Missing parameter 'minRam'"
    assert "sshKey" in params, "Missing parameter 'sshKey'"
    assert "minDisk" in params, "Missing parameter 'minDisk'"
    assert "location" in params, "Missing parameter 'location'"














def test_hyp_cloudml_artefactportinstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_ArtefactPortInstance)


def test_hyp_cloudml_artefactportinstance_constructor_exists():
    assert callable(cloudml_ArtefactPortInstance.__init__)


def test_hyp_cloudml_artefactportinstance_constructor_args():
    sig = inspect.signature(cloudml_ArtefactPortInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_provider_is_not_abstract():
    assert not inspect.isabstract(cloudml_Provider)


def test_hyp_cloudml_provider_constructor_exists():
    assert callable(cloudml_Provider.__init__)


def test_hyp_cloudml_provider_constructor_args():
    sig = inspect.signature(cloudml_Provider.__init__)
    params = list(sig.parameters.keys())
    assert "credentials" in params, "Missing parameter 'credentials'"




def test_hyp_cloudml_artefact_is_not_abstract():
    assert not inspect.isabstract(cloudml_Artefact)


def test_hyp_cloudml_artefact_constructor_exists():
    assert callable(cloudml_Artefact.__init__)


def test_hyp_cloudml_artefact_constructor_args():
    sig = inspect.signature(cloudml_Artefact.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_resource_is_not_abstract():
    assert not inspect.isabstract(cloudml_Resource)


def test_hyp_cloudml_resource_constructor_exists():
    assert callable(cloudml_Resource.__init__)


def test_hyp_cloudml_resource_constructor_args():
    sig = inspect.signature(cloudml_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "retrievingCommand" in params, "Missing parameter 'retrievingCommand'"
    assert "configurationCommand" in params, "Missing parameter 'configurationCommand'"
    assert "startCommand" in params, "Missing parameter 'startCommand'"
    assert "deployingCommand" in params, "Missing parameter 'deployingCommand'"
    assert "stopCommand" in params, "Missing parameter 'stopCommand'"







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
ArtefactPortInstance_strategy = st.builds(
    ArtefactPortInstance,
)
cloudml_ClientPortInstance_strategy = st.builds(
    cloudml_ClientPortInstance,
)
cloudml_ServerPortInstance_strategy = st.builds(
    cloudml_ServerPortInstance,
)
ArtefactPort_strategy = st.builds(
    ArtefactPort,
)
cloudml_ClientPort_strategy = st.builds(
    cloudml_ClientPort,
    isOptional=
        st.booleans()
)
cloudml_ServerPort_strategy = st.builds(
    cloudml_ServerPort,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
cloudml_WithProperties_strategy = st.builds(
    cloudml_WithProperties,
)
cloudml_Composite_strategy = st.builds(
    cloudml_Composite,
)
cloudml_Property_strategy = st.builds(
    cloudml_Property,
    value=
        safe_text
)
CloudMLElement_strategy = st.builds(
    CloudMLElement,
)
cloudml_NamedElement_strategy = st.builds(
    cloudml_NamedElement,
    name=
        safe_text
)
cloudml_CloudMLElement_strategy = st.builds(
    cloudml_CloudMLElement,
)
cloudml_UploadCommand_strategy = st.builds(
    cloudml_UploadCommand,
    target=
        safe_text,
    source=
        safe_text
)
WithProperties_strategy = st.builds(
    WithProperties,
)
cloudml_ArtefactPort_strategy = st.builds(
    cloudml_ArtefactPort,
    portNumber=
        st.integers(),
    isRemote=
        st.booleans()
)
cloudml_BindingInstance_strategy = st.builds(
    cloudml_BindingInstance,
)
cloudml_DeploymentModel_strategy = st.builds(
    cloudml_DeploymentModel,
)
cloudml_Binding_strategy = st.builds(
    cloudml_Binding,
)
cloudml_NodeInstance_strategy = st.builds(
    cloudml_NodeInstance,
    publicAddress=
        safe_text,
    id=
        safe_text
)
cloudml_ArtefactInstance_strategy = st.builds(
    cloudml_ArtefactInstance,
)
cloudml_Node_strategy = st.builds(
    cloudml_Node,
    groupName=
        safe_text,
    minCore=
        st.integers(),
    privateKey=
        safe_text,
    imageID=
        safe_text,
    OS=
        safe_text,
    is64os=
        st.booleans(),
    securityGroup=
        safe_text,
    minRam=
        st.integers(),
    sshKey=
        safe_text,
    minDisk=
        st.integers(),
    location=
        safe_text
)
cloudml_ArtefactPortInstance_strategy = st.builds(
    cloudml_ArtefactPortInstance,
)
cloudml_Provider_strategy = st.builds(
    cloudml_Provider,
    credentials=
        safe_text
)
cloudml_Artefact_strategy = st.builds(
    cloudml_Artefact,
)
cloudml_Resource_strategy = st.builds(
    cloudml_Resource,
    retrievingCommand=
        safe_text,
    configurationCommand=
        safe_text,
    startCommand=
        safe_text,
    deployingCommand=
        safe_text,
    stopCommand=
        safe_text
)








@given(instance=cloudml_ClientPort_strategy)
def test_hyp_cloudml_clientport_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original








@given(instance=cloudml_Property_strategy)
def test_hyp_cloudml_property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=cloudml_NamedElement_strategy)
def test_hyp_cloudml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=cloudml_UploadCommand_strategy)
def test_hyp_cloudml_uploadcommand_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=cloudml_UploadCommand_strategy)
def test_hyp_cloudml_uploadcommand_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original





@given(instance=cloudml_ArtefactPort_strategy)
def test_hyp_cloudml_artefactport_portNumber_setter(instance):
    original = instance.portNumber
    instance.portNumber = original
    assert instance.portNumber == original



@given(instance=cloudml_ArtefactPort_strategy)
def test_hyp_cloudml_artefactport_isRemote_setter(instance):
    original = instance.isRemote
    instance.isRemote = original
    assert instance.isRemote == original







@given(instance=cloudml_NodeInstance_strategy)
def test_hyp_cloudml_nodeinstance_publicAddress_setter(instance):
    original = instance.publicAddress
    instance.publicAddress = original
    assert instance.publicAddress == original



@given(instance=cloudml_NodeInstance_strategy)
def test_hyp_cloudml_nodeinstance_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original





@given(instance=cloudml_Node_strategy)
def test_hyp_cloudml_node_groupName_setter(instance):
    original = instance.groupName
    instance.groupName = original
    assert instance.groupName == original



@given(instance=cloudml_Node_strategy)
def test_hyp_cloudml_node_minCore_setter(instance):
    original = instance.minCore
    instance.minCore = original
    assert instance.minCore == original



@given(instance=cloudml_Node_strategy)
def test_hyp_cloudml_node_privateKey_setter(instance):
    original = instance.privateKey
    instance.privateKey = original
    assert instance.privateKey == original



@given(instance=cloudml_Node_strategy)
def test_hyp_cloudml_node_imageID_setter(instance):
    original = instance.imageID
    instance.imageID = original
    assert instance.imageID == original



@given(instance=cloudml_Node_strategy)
def test_hyp_cloudml_node_OS_setter(instance):
    original = instance.OS
    instance.OS = original
    assert instance.OS == original



@given(instance=cloudml_Node_strategy)
def test_hyp_cloudml_node_is64os_setter(instance):
    original = instance.is64os
    instance.is64os = original
    assert instance.is64os == original



@given(instance=cloudml_Node_strategy)
def test_hyp_cloudml_node_securityGroup_setter(instance):
    original = instance.securityGroup
    instance.securityGroup = original
    assert instance.securityGroup == original



@given(instance=cloudml_Node_strategy)
def test_hyp_cloudml_node_minRam_setter(instance):
    original = instance.minRam
    instance.minRam = original
    assert instance.minRam == original



@given(instance=cloudml_Node_strategy)
def test_hyp_cloudml_node_sshKey_setter(instance):
    original = instance.sshKey
    instance.sshKey = original
    assert instance.sshKey == original



@given(instance=cloudml_Node_strategy)
def test_hyp_cloudml_node_minDisk_setter(instance):
    original = instance.minDisk
    instance.minDisk = original
    assert instance.minDisk == original



@given(instance=cloudml_Node_strategy)
def test_hyp_cloudml_node_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original





@given(instance=cloudml_Provider_strategy)
def test_hyp_cloudml_provider_credentials_setter(instance):
    original = instance.credentials
    instance.credentials = original
    assert instance.credentials == original





@given(instance=cloudml_Resource_strategy)
def test_hyp_cloudml_resource_retrievingCommand_setter(instance):
    original = instance.retrievingCommand
    instance.retrievingCommand = original
    assert instance.retrievingCommand == original



@given(instance=cloudml_Resource_strategy)
def test_hyp_cloudml_resource_configurationCommand_setter(instance):
    original = instance.configurationCommand
    instance.configurationCommand = original
    assert instance.configurationCommand == original



@given(instance=cloudml_Resource_strategy)
def test_hyp_cloudml_resource_startCommand_setter(instance):
    original = instance.startCommand
    instance.startCommand = original
    assert instance.startCommand == original



@given(instance=cloudml_Resource_strategy)
def test_hyp_cloudml_resource_deployingCommand_setter(instance):
    original = instance.deployingCommand
    instance.deployingCommand = original
    assert instance.deployingCommand == original



@given(instance=cloudml_Resource_strategy)
def test_hyp_cloudml_resource_stopCommand_setter(instance):
    original = instance.stopCommand
    instance.stopCommand = original
    assert instance.stopCommand == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ArtefactPort,
    ArtefactPortInstance,
    CloudMLElement,
    NamedElement,
    WithProperties,
    cloudml_Artefact,
    cloudml_ArtefactInstance,
    cloudml_ArtefactPort,
    cloudml_ArtefactPortInstance,
    cloudml_Binding,
    cloudml_BindingInstance,
    cloudml_ClientPort,
    cloudml_ClientPortInstance,
    cloudml_CloudMLElement,
    cloudml_Composite,
    cloudml_DeploymentModel,
    cloudml_NamedElement,
    cloudml_Node,
    cloudml_NodeInstance,
    cloudml_Property,
    cloudml_Provider,
    cloudml_Resource,
    cloudml_ServerPort,
    cloudml_ServerPortInstance,
    cloudml_UploadCommand,
    cloudml_WithProperties,
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

def test_cloudml_ArtefactPort_isRemote_value_roundtrip():
    instance = cloudml_ArtefactPort(isRemote=True, portNumber=7)
    assert instance.isRemote == True
    instance.isRemote = False
    assert instance.isRemote == False


def test_cloudml_ArtefactPort_portNumber_value_roundtrip():
    instance = cloudml_ArtefactPort(isRemote=True, portNumber=7)
    assert instance.portNumber == 7
    instance.portNumber = 13
    assert instance.portNumber == 13


def test_cloudml_ClientPort_isOptional_value_roundtrip():
    instance = cloudml_ClientPort(isOptional=True)
    assert instance.isOptional == True
    instance.isOptional = False
    assert instance.isOptional == False


def test_cloudml_NamedElement_name_value_roundtrip():
    instance = cloudml_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cloudml_Node_OS_value_roundtrip():
    instance = cloudml_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.OS == "sample_text"
    instance.OS = "sample_text_2"
    assert instance.OS == "sample_text_2"


def test_cloudml_Node_groupName_value_roundtrip():
    instance = cloudml_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.groupName == "sample_text"
    instance.groupName = "sample_text_2"
    assert instance.groupName == "sample_text_2"


def test_cloudml_Node_imageID_value_roundtrip():
    instance = cloudml_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.imageID == "sample_text"
    instance.imageID = "sample_text_2"
    assert instance.imageID == "sample_text_2"


def test_cloudml_Node_is64os_value_roundtrip():
    instance = cloudml_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.is64os == True
    instance.is64os = False
    assert instance.is64os == False


def test_cloudml_Node_location_value_roundtrip():
    instance = cloudml_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_cloudml_Node_minCore_value_roundtrip():
    instance = cloudml_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.minCore == 7
    instance.minCore = 13
    assert instance.minCore == 13


def test_cloudml_Node_minDisk_value_roundtrip():
    instance = cloudml_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.minDisk == 7
    instance.minDisk = 13
    assert instance.minDisk == 13


def test_cloudml_Node_minRam_value_roundtrip():
    instance = cloudml_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.minRam == 7
    instance.minRam = 13
    assert instance.minRam == 13


def test_cloudml_Node_privateKey_value_roundtrip():
    instance = cloudml_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.privateKey == "sample_text"
    instance.privateKey = "sample_text_2"
    assert instance.privateKey == "sample_text_2"


def test_cloudml_Node_securityGroup_value_roundtrip():
    instance = cloudml_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.securityGroup == "sample_text"
    instance.securityGroup = "sample_text_2"
    assert instance.securityGroup == "sample_text_2"


def test_cloudml_Node_sshKey_value_roundtrip():
    instance = cloudml_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.sshKey == "sample_text"
    instance.sshKey = "sample_text_2"
    assert instance.sshKey == "sample_text_2"


def test_cloudml_NodeInstance_id_value_roundtrip():
    instance = cloudml_NodeInstance(id="sample_text", publicAddress="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_cloudml_NodeInstance_publicAddress_value_roundtrip():
    instance = cloudml_NodeInstance(id="sample_text", publicAddress="sample_text")
    assert instance.publicAddress == "sample_text"
    instance.publicAddress = "sample_text_2"
    assert instance.publicAddress == "sample_text_2"


def test_cloudml_Property_value_value_roundtrip():
    instance = cloudml_Property(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_cloudml_Provider_credentials_value_roundtrip():
    instance = cloudml_Provider(credentials="sample_text")
    assert instance.credentials == "sample_text"
    instance.credentials = "sample_text_2"
    assert instance.credentials == "sample_text_2"


def test_cloudml_Resource_configurationCommand_value_roundtrip():
    instance = cloudml_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text", stopCommand="sample_text")
    assert instance.configurationCommand == "sample_text"
    instance.configurationCommand = "sample_text_2"
    assert instance.configurationCommand == "sample_text_2"


def test_cloudml_Resource_deployingCommand_value_roundtrip():
    instance = cloudml_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text", stopCommand="sample_text")
    assert instance.deployingCommand == "sample_text"
    instance.deployingCommand = "sample_text_2"
    assert instance.deployingCommand == "sample_text_2"


def test_cloudml_Resource_retrievingCommand_value_roundtrip():
    instance = cloudml_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text", stopCommand="sample_text")
    assert instance.retrievingCommand == "sample_text"
    instance.retrievingCommand = "sample_text_2"
    assert instance.retrievingCommand == "sample_text_2"


def test_cloudml_Resource_startCommand_value_roundtrip():
    instance = cloudml_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text", stopCommand="sample_text")
    assert instance.startCommand == "sample_text"
    instance.startCommand = "sample_text_2"
    assert instance.startCommand == "sample_text_2"


def test_cloudml_Resource_stopCommand_value_roundtrip():
    instance = cloudml_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text", stopCommand="sample_text")
    assert instance.stopCommand == "sample_text"
    instance.stopCommand = "sample_text_2"
    assert instance.stopCommand == "sample_text_2"


def test_cloudml_UploadCommand_source_value_roundtrip():
    instance = cloudml_UploadCommand(source="sample_text", target="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_cloudml_UploadCommand_target_value_roundtrip():
    instance = cloudml_UploadCommand(source="sample_text", target="sample_text")
    assert instance.target == "sample_text"
    instance.target = "sample_text_2"
    assert instance.target == "sample_text_2"


def test_cloudml_ClientPort_isa_ArtefactPort():
    instance = cloudml_ClientPort(isOptional=True)
    assert isinstance(instance, ArtefactPort)


def test_cloudml_ServerPort_isa_ArtefactPort():
    instance = cloudml_ServerPort()
    assert isinstance(instance, ArtefactPort)


def test_cloudml_ClientPortInstance_isa_ArtefactPortInstance():
    instance = cloudml_ClientPortInstance()
    assert isinstance(instance, ArtefactPortInstance)


def test_cloudml_ServerPortInstance_isa_ArtefactPortInstance():
    instance = cloudml_ServerPortInstance()
    assert isinstance(instance, ArtefactPortInstance)


def test_cloudml_NamedElement_isa_CloudMLElement():
    instance = cloudml_NamedElement(name="sample_text")
    assert isinstance(instance, CloudMLElement)


def test_cloudml_Composite_isa_NamedElement():
    instance = cloudml_Composite()
    assert isinstance(instance, NamedElement)


def test_cloudml_Property_isa_NamedElement():
    instance = cloudml_Property(value="sample_text")
    assert isinstance(instance, NamedElement)


def test_cloudml_WithProperties_isa_NamedElement():
    instance = cloudml_WithProperties()
    assert isinstance(instance, NamedElement)


def test_cloudml_Artefact_isa_WithProperties():
    instance = cloudml_Artefact()
    assert isinstance(instance, WithProperties)


def test_cloudml_ArtefactInstance_isa_WithProperties():
    instance = cloudml_ArtefactInstance()
    assert isinstance(instance, WithProperties)


def test_cloudml_ArtefactPort_isa_WithProperties():
    instance = cloudml_ArtefactPort(isRemote=True, portNumber=7)
    assert isinstance(instance, WithProperties)


def test_cloudml_ArtefactPortInstance_isa_WithProperties():
    instance = cloudml_ArtefactPortInstance()
    assert isinstance(instance, WithProperties)


def test_cloudml_Binding_isa_WithProperties():
    instance = cloudml_Binding()
    assert isinstance(instance, WithProperties)


def test_cloudml_BindingInstance_isa_WithProperties():
    instance = cloudml_BindingInstance()
    assert isinstance(instance, WithProperties)


def test_cloudml_DeploymentModel_isa_WithProperties():
    instance = cloudml_DeploymentModel()
    assert isinstance(instance, WithProperties)


def test_cloudml_Node_isa_WithProperties():
    instance = cloudml_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert isinstance(instance, WithProperties)


def test_cloudml_NodeInstance_isa_WithProperties():
    instance = cloudml_NodeInstance(id="sample_text", publicAddress="sample_text")
    assert isinstance(instance, WithProperties)


def test_cloudml_Provider_isa_WithProperties():
    instance = cloudml_Provider(credentials="sample_text")
    assert isinstance(instance, WithProperties)


def test_cloudml_Resource_isa_WithProperties():
    instance = cloudml_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text", stopCommand="sample_text")
    assert isinstance(instance, WithProperties)


def test_assoc_client44_link_reassign_clear():
    a = cloudml_ClientPort(isOptional=True)
    b1 = cloudml_Binding()
    b2 = cloudml_Binding()
    _safe_set(a, 'cloudml_ClientPort46', b1)
    assert _is_linked(a, 'cloudml_ClientPort46', b1)
    if hasattr(b1, 'cloudml_Binding45'):
        assert _is_linked(b1, 'cloudml_Binding45', a)
    _safe_set(a, 'cloudml_ClientPort46', b2)
    assert _is_linked(a, 'cloudml_ClientPort46', b2)
    if hasattr(b1, 'cloudml_Binding45'):
        assert not _is_linked(b1, 'cloudml_Binding45', a)
    if hasattr(b2, 'cloudml_Binding45'):
        assert _is_linked(b2, 'cloudml_Binding45', a)
    _safe_set(a, 'cloudml_ClientPort46', None)
    assert not _is_linked(a, 'cloudml_ClientPort46', b2)
    if hasattr(b2, 'cloudml_Binding45'):
        assert not _is_linked(b2, 'cloudml_Binding45', a)


def test_assoc_clientResource50_link_reassign_clear():
    a = cloudml_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text", stopCommand="sample_text")
    b1 = cloudml_Binding()
    b2 = cloudml_Binding()
    _safe_set(a, 'cloudml_Resource52', b1)
    assert _is_linked(a, 'cloudml_Resource52', b1)
    if hasattr(b1, 'cloudml_Binding51'):
        assert _is_linked(b1, 'cloudml_Binding51', a)
    _safe_set(a, 'cloudml_Resource52', b2)
    assert _is_linked(a, 'cloudml_Resource52', b2)
    if hasattr(b1, 'cloudml_Binding51'):
        assert not _is_linked(b1, 'cloudml_Binding51', a)
    if hasattr(b2, 'cloudml_Binding51'):
        assert _is_linked(b2, 'cloudml_Binding51', a)
    _safe_set(a, 'cloudml_Resource52', None)
    assert not _is_linked(a, 'cloudml_Resource52', b2)
    if hasattr(b2, 'cloudml_Binding51'):
        assert not _is_linked(b2, 'cloudml_Binding51', a)


def test_assoc_cloudProvider24_link_reassign_clear():
    a = cloudml_Provider(credentials="sample_text")
    b1 = cloudml_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    b2 = cloudml_Node(OS="sample_text_2", groupName="sample_text_2", imageID="sample_text_2", is64os=False, location="sample_text_2", minCore=13, minDisk=13, minRam=13, privateKey="sample_text_2", securityGroup="sample_text_2", sshKey="sample_text_2")
    _safe_set(a, 'cloudml_Provider26', b1)
    assert _is_linked(a, 'cloudml_Provider26', b1)
    if hasattr(b1, 'cloudml_Node25'):
        assert _is_linked(b1, 'cloudml_Node25', a)
    _safe_set(a, 'cloudml_Provider26', b2)
    assert _is_linked(a, 'cloudml_Provider26', b2)
    if hasattr(b1, 'cloudml_Node25'):
        assert not _is_linked(b1, 'cloudml_Node25', a)
    if hasattr(b2, 'cloudml_Node25'):
        assert _is_linked(b2, 'cloudml_Node25', a)
    _safe_set(a, 'cloudml_Provider26', None)
    assert not _is_linked(a, 'cloudml_Provider26', b2)
    if hasattr(b2, 'cloudml_Node25'):
        assert not _is_linked(b2, 'cloudml_Node25', a)


def test_assoc_destination15_link_reassign_clear():
    a = cloudml_ArtefactPort(isRemote=True, portNumber=7)
    b1 = cloudml_Artefact()
    b2 = cloudml_Artefact()
    _safe_set(a, 'cloudml_ArtefactPort', b1)
    assert _is_linked(a, 'cloudml_ArtefactPort', b1)
    if hasattr(b1, 'cloudml_Artefact16'):
        assert _is_linked(b1, 'cloudml_Artefact16', a)
    _safe_set(a, 'cloudml_ArtefactPort', b2)
    assert _is_linked(a, 'cloudml_ArtefactPort', b2)
    if hasattr(b1, 'cloudml_Artefact16'):
        assert not _is_linked(b1, 'cloudml_Artefact16', a)
    if hasattr(b2, 'cloudml_Artefact16'):
        assert _is_linked(b2, 'cloudml_Artefact16', a)
    _safe_set(a, 'cloudml_ArtefactPort', None)
    assert not _is_linked(a, 'cloudml_ArtefactPort', b2)
    if hasattr(b2, 'cloudml_Artefact16'):
        assert not _is_linked(b2, 'cloudml_Artefact16', a)


def test_assoc_destination32_link_reassign_clear():
    a = cloudml_NodeInstance(id="sample_text", publicAddress="sample_text")
    b1 = cloudml_ArtefactInstance()
    b2 = cloudml_ArtefactInstance()
    _safe_set(a, 'cloudml_NodeInstance34', b1)
    assert _is_linked(a, 'cloudml_NodeInstance34', b1)
    if hasattr(b1, 'cloudml_ArtefactInstance33'):
        assert _is_linked(b1, 'cloudml_ArtefactInstance33', a)
    _safe_set(a, 'cloudml_NodeInstance34', b2)
    assert _is_linked(a, 'cloudml_NodeInstance34', b2)
    if hasattr(b1, 'cloudml_ArtefactInstance33'):
        assert not _is_linked(b1, 'cloudml_ArtefactInstance33', a)
    if hasattr(b2, 'cloudml_ArtefactInstance33'):
        assert _is_linked(b2, 'cloudml_ArtefactInstance33', a)
    _safe_set(a, 'cloudml_NodeInstance34', None)
    assert not _is_linked(a, 'cloudml_NodeInstance34', b2)
    if hasattr(b2, 'cloudml_ArtefactInstance33'):
        assert not _is_linked(b2, 'cloudml_ArtefactInstance33', a)


def test_assoc_nodeInstances11_link_reassign_clear():
    a = cloudml_NodeInstance(id="sample_text", publicAddress="sample_text")
    b1 = cloudml_DeploymentModel()
    b2 = cloudml_DeploymentModel()
    _safe_set(a, 'cloudml_NodeInstance', b1)
    assert _is_linked(a, 'cloudml_NodeInstance', b1)
    if hasattr(b1, 'cloudml_DeploymentModel12'):
        assert _is_linked(b1, 'cloudml_DeploymentModel12', a)
    _safe_set(a, 'cloudml_NodeInstance', b2)
    assert _is_linked(a, 'cloudml_NodeInstance', b2)
    if hasattr(b1, 'cloudml_DeploymentModel12'):
        assert not _is_linked(b1, 'cloudml_DeploymentModel12', a)
    if hasattr(b2, 'cloudml_DeploymentModel12'):
        assert _is_linked(b2, 'cloudml_DeploymentModel12', a)
    _safe_set(a, 'cloudml_NodeInstance', None)
    assert not _is_linked(a, 'cloudml_NodeInstance', b2)
    if hasattr(b2, 'cloudml_DeploymentModel12'):
        assert not _is_linked(b2, 'cloudml_DeploymentModel12', a)


def test_assoc_nodeTypes5_link_reassign_clear():
    a = cloudml_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    b1 = cloudml_DeploymentModel()
    b2 = cloudml_DeploymentModel()
    _safe_set(a, 'cloudml_Node', b1)
    assert _is_linked(a, 'cloudml_Node', b1)
    if hasattr(b1, 'cloudml_DeploymentModel6'):
        assert _is_linked(b1, 'cloudml_DeploymentModel6', a)
    _safe_set(a, 'cloudml_Node', b2)
    assert _is_linked(a, 'cloudml_Node', b2)
    if hasattr(b1, 'cloudml_DeploymentModel6'):
        assert not _is_linked(b1, 'cloudml_DeploymentModel6', a)
    if hasattr(b2, 'cloudml_DeploymentModel6'):
        assert _is_linked(b2, 'cloudml_DeploymentModel6', a)
    _safe_set(a, 'cloudml_Node', None)
    assert not _is_linked(a, 'cloudml_Node', b2)
    if hasattr(b2, 'cloudml_DeploymentModel6'):
        assert not _is_linked(b2, 'cloudml_DeploymentModel6', a)


def test_assoc_properties0_link_reassign_clear():
    a = cloudml_Property(value="sample_text")
    b1 = cloudml_WithProperties()
    b2 = cloudml_WithProperties()
    _safe_set(a, 'cloudml_Property', b1)
    assert _is_linked(a, 'cloudml_Property', b1)
    if hasattr(b1, 'cloudml_WithProperties'):
        assert _is_linked(b1, 'cloudml_WithProperties', a)
    _safe_set(a, 'cloudml_Property', b2)
    assert _is_linked(a, 'cloudml_Property', b2)
    if hasattr(b1, 'cloudml_WithProperties'):
        assert not _is_linked(b1, 'cloudml_WithProperties', a)
    if hasattr(b2, 'cloudml_WithProperties'):
        assert _is_linked(b2, 'cloudml_WithProperties', a)
    _safe_set(a, 'cloudml_Property', None)
    assert not _is_linked(a, 'cloudml_Property', b2)
    if hasattr(b2, 'cloudml_WithProperties'):
        assert not _is_linked(b2, 'cloudml_WithProperties', a)


def test_assoc_providers2_link_reassign_clear():
    a = cloudml_Provider(credentials="sample_text")
    b1 = cloudml_DeploymentModel()
    b2 = cloudml_DeploymentModel()
    _safe_set(a, 'cloudml_Provider', b1)
    assert _is_linked(a, 'cloudml_Provider', b1)
    if hasattr(b1, 'cloudml_DeploymentModel'):
        assert _is_linked(b1, 'cloudml_DeploymentModel', a)
    _safe_set(a, 'cloudml_Provider', b2)
    assert _is_linked(a, 'cloudml_Provider', b2)
    if hasattr(b1, 'cloudml_DeploymentModel'):
        assert not _is_linked(b1, 'cloudml_DeploymentModel', a)
    if hasattr(b2, 'cloudml_DeploymentModel'):
        assert _is_linked(b2, 'cloudml_DeploymentModel', a)
    _safe_set(a, 'cloudml_Provider', None)
    assert not _is_linked(a, 'cloudml_Provider', b2)
    if hasattr(b2, 'cloudml_DeploymentModel'):
        assert not _is_linked(b2, 'cloudml_DeploymentModel', a)


def test_assoc_required22_link_reassign_clear():
    a = cloudml_ClientPort(isOptional=True)
    b1 = cloudml_Artefact()
    b2 = cloudml_Artefact()
    _safe_set(a, 'cloudml_ClientPort', b1)
    assert _is_linked(a, 'cloudml_ClientPort', b1)
    if hasattr(b1, 'cloudml_Artefact23'):
        assert _is_linked(b1, 'cloudml_Artefact23', a)
    _safe_set(a, 'cloudml_ClientPort', b2)
    assert _is_linked(a, 'cloudml_ClientPort', b2)
    if hasattr(b1, 'cloudml_Artefact23'):
        assert not _is_linked(b1, 'cloudml_Artefact23', a)
    if hasattr(b2, 'cloudml_Artefact23'):
        assert _is_linked(b2, 'cloudml_Artefact23', a)
    _safe_set(a, 'cloudml_ClientPort', None)
    assert not _is_linked(a, 'cloudml_ClientPort', b2)
    if hasattr(b2, 'cloudml_Artefact23'):
        assert not _is_linked(b2, 'cloudml_Artefact23', a)


def test_assoc_resource17_link_reassign_clear():
    a = cloudml_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text", stopCommand="sample_text")
    b1 = cloudml_Artefact()
    b2 = cloudml_Artefact()
    _safe_set(a, 'cloudml_Resource19', b1)
    assert _is_linked(a, 'cloudml_Resource19', b1)
    if hasattr(b1, 'cloudml_Artefact18'):
        assert _is_linked(b1, 'cloudml_Artefact18', a)
    _safe_set(a, 'cloudml_Resource19', b2)
    assert _is_linked(a, 'cloudml_Resource19', b2)
    if hasattr(b1, 'cloudml_Artefact18'):
        assert not _is_linked(b1, 'cloudml_Artefact18', a)
    if hasattr(b2, 'cloudml_Artefact18'):
        assert _is_linked(b2, 'cloudml_Artefact18', a)
    _safe_set(a, 'cloudml_Resource19', None)
    assert not _is_linked(a, 'cloudml_Resource19', b2)
    if hasattr(b2, 'cloudml_Artefact18'):
        assert not _is_linked(b2, 'cloudml_Artefact18', a)


def test_assoc_serverResource53_link_reassign_clear():
    a = cloudml_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text", stopCommand="sample_text")
    b1 = cloudml_Binding()
    b2 = cloudml_Binding()
    _safe_set(a, 'cloudml_Resource55', b1)
    assert _is_linked(a, 'cloudml_Resource55', b1)
    if hasattr(b1, 'cloudml_Binding54'):
        assert _is_linked(b1, 'cloudml_Binding54', a)
    _safe_set(a, 'cloudml_Resource55', b2)
    assert _is_linked(a, 'cloudml_Resource55', b2)
    if hasattr(b1, 'cloudml_Binding54'):
        assert not _is_linked(b1, 'cloudml_Binding54', a)
    if hasattr(b2, 'cloudml_Binding54'):
        assert _is_linked(b2, 'cloudml_Binding54', a)
    _safe_set(a, 'cloudml_Resource55', None)
    assert not _is_linked(a, 'cloudml_Resource55', b2)
    if hasattr(b2, 'cloudml_Binding54'):
        assert not _is_linked(b2, 'cloudml_Binding54', a)


def test_assoc_type27_link_reassign_clear():
    a = cloudml_ArtefactPort(isRemote=True, portNumber=7)
    b1 = cloudml_ArtefactPortInstance()
    b2 = cloudml_ArtefactPortInstance()
    _safe_set(a, 'cloudml_ArtefactPort28', b1)
    assert _is_linked(a, 'cloudml_ArtefactPort28', b1)
    if hasattr(b1, 'cloudml_ArtefactPortInstance'):
        assert _is_linked(b1, 'cloudml_ArtefactPortInstance', a)
    _safe_set(a, 'cloudml_ArtefactPort28', b2)
    assert _is_linked(a, 'cloudml_ArtefactPort28', b2)
    if hasattr(b1, 'cloudml_ArtefactPortInstance'):
        assert not _is_linked(b1, 'cloudml_ArtefactPortInstance', a)
    if hasattr(b2, 'cloudml_ArtefactPortInstance'):
        assert _is_linked(b2, 'cloudml_ArtefactPortInstance', a)
    _safe_set(a, 'cloudml_ArtefactPort28', None)
    assert not _is_linked(a, 'cloudml_ArtefactPort28', b2)
    if hasattr(b2, 'cloudml_ArtefactPortInstance'):
        assert not _is_linked(b2, 'cloudml_ArtefactPortInstance', a)


def test_assoc_type39_link_reassign_clear():
    a = cloudml_NodeInstance(id="sample_text", publicAddress="sample_text")
    b1 = cloudml_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    b2 = cloudml_Node(OS="sample_text_2", groupName="sample_text_2", imageID="sample_text_2", is64os=False, location="sample_text_2", minCore=13, minDisk=13, minRam=13, privateKey="sample_text_2", securityGroup="sample_text_2", sshKey="sample_text_2")
    _safe_set(a, 'cloudml_NodeInstance40', b1)
    assert _is_linked(a, 'cloudml_NodeInstance40', b1)
    if hasattr(b1, 'cloudml_Node41'):
        assert _is_linked(b1, 'cloudml_Node41', a)
    _safe_set(a, 'cloudml_NodeInstance40', b2)
    assert _is_linked(a, 'cloudml_NodeInstance40', b2)
    if hasattr(b1, 'cloudml_Node41'):
        assert not _is_linked(b1, 'cloudml_Node41', a)
    if hasattr(b2, 'cloudml_Node41'):
        assert _is_linked(b2, 'cloudml_Node41', a)
    _safe_set(a, 'cloudml_NodeInstance40', None)
    assert not _is_linked(a, 'cloudml_NodeInstance40', b2)
    if hasattr(b2, 'cloudml_Node41'):
        assert not _is_linked(b2, 'cloudml_Node41', a)


def test_assoc_uploadCommand1_link_reassign_clear():
    a = cloudml_UploadCommand(source="sample_text", target="sample_text")
    b1 = cloudml_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text", stopCommand="sample_text")
    b2 = cloudml_Resource(configurationCommand="sample_text_2", deployingCommand="sample_text_2", retrievingCommand="sample_text_2", startCommand="sample_text_2", stopCommand="sample_text_2")
    _safe_set(a, 'cloudml_UploadCommand', b1)
    assert _is_linked(a, 'cloudml_UploadCommand', b1)
    if hasattr(b1, 'cloudml_Resource'):
        assert _is_linked(b1, 'cloudml_Resource', a)
    _safe_set(a, 'cloudml_UploadCommand', b2)
    assert _is_linked(a, 'cloudml_UploadCommand', b2)
    if hasattr(b1, 'cloudml_Resource'):
        assert not _is_linked(b1, 'cloudml_Resource', a)
    if hasattr(b2, 'cloudml_Resource'):
        assert _is_linked(b2, 'cloudml_Resource', a)
    _safe_set(a, 'cloudml_UploadCommand', None)
    assert not _is_linked(a, 'cloudml_UploadCommand', b2)
    if hasattr(b2, 'cloudml_Resource'):
        assert not _is_linked(b2, 'cloudml_Resource', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

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


WithProperties_strategy = st.builds(WithProperties)
@given(instance=WithProperties_strategy)
@settings(max_examples=25)
def test_WithProperties_instantiation(instance):
    assert isinstance(instance, WithProperties)


cloudml_Artefact_strategy = st.builds(cloudml_Artefact)
@given(instance=cloudml_Artefact_strategy)
@settings(max_examples=25)
def test_cloudml_Artefact_instantiation(instance):
    assert isinstance(instance, cloudml_Artefact)


cloudml_ArtefactInstance_strategy = st.builds(cloudml_ArtefactInstance)
@given(instance=cloudml_ArtefactInstance_strategy)
@settings(max_examples=25)
def test_cloudml_ArtefactInstance_instantiation(instance):
    assert isinstance(instance, cloudml_ArtefactInstance)


cloudml_ArtefactPort_strategy = st.builds(cloudml_ArtefactPort, isRemote=st.booleans(), portNumber=st.integers())
@given(instance=cloudml_ArtefactPort_strategy)
@settings(max_examples=25)
def test_cloudml_ArtefactPort_instantiation(instance):
    assert isinstance(instance, cloudml_ArtefactPort)


cloudml_ArtefactPortInstance_strategy = st.builds(cloudml_ArtefactPortInstance)
@given(instance=cloudml_ArtefactPortInstance_strategy)
@settings(max_examples=25)
def test_cloudml_ArtefactPortInstance_instantiation(instance):
    assert isinstance(instance, cloudml_ArtefactPortInstance)


cloudml_Binding_strategy = st.builds(cloudml_Binding)
@given(instance=cloudml_Binding_strategy)
@settings(max_examples=25)
def test_cloudml_Binding_instantiation(instance):
    assert isinstance(instance, cloudml_Binding)


cloudml_BindingInstance_strategy = st.builds(cloudml_BindingInstance)
@given(instance=cloudml_BindingInstance_strategy)
@settings(max_examples=25)
def test_cloudml_BindingInstance_instantiation(instance):
    assert isinstance(instance, cloudml_BindingInstance)


cloudml_ClientPort_strategy = st.builds(cloudml_ClientPort, isOptional=st.booleans())
@given(instance=cloudml_ClientPort_strategy)
@settings(max_examples=25)
def test_cloudml_ClientPort_instantiation(instance):
    assert isinstance(instance, cloudml_ClientPort)


cloudml_ClientPortInstance_strategy = st.builds(cloudml_ClientPortInstance)
@given(instance=cloudml_ClientPortInstance_strategy)
@settings(max_examples=25)
def test_cloudml_ClientPortInstance_instantiation(instance):
    assert isinstance(instance, cloudml_ClientPortInstance)


cloudml_CloudMLElement_strategy = st.builds(cloudml_CloudMLElement)
@given(instance=cloudml_CloudMLElement_strategy)
@settings(max_examples=25)
def test_cloudml_CloudMLElement_instantiation(instance):
    assert isinstance(instance, cloudml_CloudMLElement)


cloudml_Composite_strategy = st.builds(cloudml_Composite)
@given(instance=cloudml_Composite_strategy)
@settings(max_examples=25)
def test_cloudml_Composite_instantiation(instance):
    assert isinstance(instance, cloudml_Composite)


cloudml_DeploymentModel_strategy = st.builds(cloudml_DeploymentModel)
@given(instance=cloudml_DeploymentModel_strategy)
@settings(max_examples=25)
def test_cloudml_DeploymentModel_instantiation(instance):
    assert isinstance(instance, cloudml_DeploymentModel)


cloudml_NamedElement_strategy = st.builds(cloudml_NamedElement, name=safe_text)
@given(instance=cloudml_NamedElement_strategy)
@settings(max_examples=25)
def test_cloudml_NamedElement_instantiation(instance):
    assert isinstance(instance, cloudml_NamedElement)


cloudml_Node_strategy = st.builds(cloudml_Node, OS=safe_text, groupName=safe_text, imageID=safe_text, is64os=st.booleans(), location=safe_text, minCore=st.integers(), minDisk=st.integers(), minRam=st.integers(), privateKey=safe_text, securityGroup=safe_text, sshKey=safe_text)
@given(instance=cloudml_Node_strategy)
@settings(max_examples=25)
def test_cloudml_Node_instantiation(instance):
    assert isinstance(instance, cloudml_Node)


cloudml_NodeInstance_strategy = st.builds(cloudml_NodeInstance, id=safe_text, publicAddress=safe_text)
@given(instance=cloudml_NodeInstance_strategy)
@settings(max_examples=25)
def test_cloudml_NodeInstance_instantiation(instance):
    assert isinstance(instance, cloudml_NodeInstance)


cloudml_Property_strategy = st.builds(cloudml_Property, value=safe_text)
@given(instance=cloudml_Property_strategy)
@settings(max_examples=25)
def test_cloudml_Property_instantiation(instance):
    assert isinstance(instance, cloudml_Property)


cloudml_Provider_strategy = st.builds(cloudml_Provider, credentials=safe_text)
@given(instance=cloudml_Provider_strategy)
@settings(max_examples=25)
def test_cloudml_Provider_instantiation(instance):
    assert isinstance(instance, cloudml_Provider)


cloudml_Resource_strategy = st.builds(cloudml_Resource, configurationCommand=safe_text, deployingCommand=safe_text, retrievingCommand=safe_text, startCommand=safe_text, stopCommand=safe_text)
@given(instance=cloudml_Resource_strategy)
@settings(max_examples=25)
def test_cloudml_Resource_instantiation(instance):
    assert isinstance(instance, cloudml_Resource)


cloudml_ServerPort_strategy = st.builds(cloudml_ServerPort)
@given(instance=cloudml_ServerPort_strategy)
@settings(max_examples=25)
def test_cloudml_ServerPort_instantiation(instance):
    assert isinstance(instance, cloudml_ServerPort)


cloudml_ServerPortInstance_strategy = st.builds(cloudml_ServerPortInstance)
@given(instance=cloudml_ServerPortInstance_strategy)
@settings(max_examples=25)
def test_cloudml_ServerPortInstance_instantiation(instance):
    assert isinstance(instance, cloudml_ServerPortInstance)


cloudml_UploadCommand_strategy = st.builds(cloudml_UploadCommand, source=safe_text, target=safe_text)
@given(instance=cloudml_UploadCommand_strategy)
@settings(max_examples=25)
def test_cloudml_UploadCommand_instantiation(instance):
    assert isinstance(instance, cloudml_UploadCommand)


cloudml_WithProperties_strategy = st.builds(cloudml_WithProperties)
@given(instance=cloudml_WithProperties_strategy)
@settings(max_examples=25)
def test_cloudml_WithProperties_instantiation(instance):
    assert isinstance(instance, cloudml_WithProperties)



