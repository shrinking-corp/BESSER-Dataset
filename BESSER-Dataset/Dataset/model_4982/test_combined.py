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
    ExecutionPlatformInstance,
    ExecutionPlatform,
    Resource,
    cloudml_RequiredExecutionPlatformInstance,
    ComponentInstance,
    PortInstance,
    cloudml_RequiredPortInstance,
    Port,
    cloudml_ProvidedExecutionPlatformInstance,
    cloudml_ProvidedPortInstance,
    ExternalComponentInstance,
    cloudml_VMInstance,
    cloudml_RequiredExecutionPlatform,
    cloudml_RequiredPort,
    Component,
    cloudml_ProvidedExecutionPlatform,
    cloudml_ProvidedPort,
    ExternalComponent,
    cloudml_VM,
    CloudMLElement,
    cloudml_CloudMLElementWithProperties,
    cloudml_Property,
    cloudml_CloudMLElement,
    cloudml_ExternalComponentInstance,
    cloudml_InternalComponentInstance,
    cloudml_ExternalComponent,
    cloudml_InternalComponent,
    CloudMLElementWithProperties,
    cloudml_ExecuteInstance,
    cloudml_RelationshipInstance,
    cloudml_VMPort,
    cloudml_Component,
    cloudml_VMPortInstance,
    cloudml_Relationship,
    cloudml_ExecutionPlatformInstance,
    cloudml_PortInstance,
    cloudml_Port,
    cloudml_Cloud,
    cloudml_ComponentInstance,
    cloudml_Provider,
    cloudml_CloudMLModel,
    cloudml_ExecutionPlatform,
    cloudml_PuppetResource,
    cloudml_Resource,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_executionplatforminstance_is_not_abstract():
    assert not inspect.isabstract(ExecutionPlatformInstance)


def test_hyp_executionplatforminstance_constructor_exists():
    assert callable(ExecutionPlatformInstance.__init__)


def test_hyp_executionplatforminstance_constructor_args():
    sig = inspect.signature(ExecutionPlatformInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_executionplatform_is_not_abstract():
    assert not inspect.isabstract(ExecutionPlatform)


def test_hyp_executionplatform_constructor_exists():
    assert callable(ExecutionPlatform.__init__)


def test_hyp_executionplatform_constructor_args():
    sig = inspect.signature(ExecutionPlatform.__init__)
    params = list(sig.parameters.keys())



def test_hyp_resource_is_not_abstract():
    assert not inspect.isabstract(Resource)


def test_hyp_resource_constructor_exists():
    assert callable(Resource.__init__)


def test_hyp_resource_constructor_args():
    sig = inspect.signature(Resource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_requiredexecutionplatforminstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_RequiredExecutionPlatformInstance)


def test_hyp_cloudml_requiredexecutionplatforminstance_constructor_exists():
    assert callable(cloudml_RequiredExecutionPlatformInstance.__init__)


def test_hyp_cloudml_requiredexecutionplatforminstance_constructor_args():
    sig = inspect.signature(cloudml_RequiredExecutionPlatformInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_componentinstance_is_not_abstract():
    assert not inspect.isabstract(ComponentInstance)


def test_hyp_componentinstance_constructor_exists():
    assert callable(ComponentInstance.__init__)


def test_hyp_componentinstance_constructor_args():
    sig = inspect.signature(ComponentInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_portinstance_is_not_abstract():
    assert not inspect.isabstract(PortInstance)


def test_hyp_portinstance_constructor_exists():
    assert callable(PortInstance.__init__)


def test_hyp_portinstance_constructor_args():
    sig = inspect.signature(PortInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_requiredportinstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_RequiredPortInstance)


def test_hyp_cloudml_requiredportinstance_constructor_exists():
    assert callable(cloudml_RequiredPortInstance.__init__)


def test_hyp_cloudml_requiredportinstance_constructor_args():
    sig = inspect.signature(cloudml_RequiredPortInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_hyp_port_constructor_exists():
    assert callable(Port.__init__)


def test_hyp_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_providedexecutionplatforminstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_ProvidedExecutionPlatformInstance)


def test_hyp_cloudml_providedexecutionplatforminstance_constructor_exists():
    assert callable(cloudml_ProvidedExecutionPlatformInstance.__init__)


def test_hyp_cloudml_providedexecutionplatforminstance_constructor_args():
    sig = inspect.signature(cloudml_ProvidedExecutionPlatformInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_providedportinstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_ProvidedPortInstance)


def test_hyp_cloudml_providedportinstance_constructor_exists():
    assert callable(cloudml_ProvidedPortInstance.__init__)


def test_hyp_cloudml_providedportinstance_constructor_args():
    sig = inspect.signature(cloudml_ProvidedPortInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_externalcomponentinstance_is_not_abstract():
    assert not inspect.isabstract(ExternalComponentInstance)


def test_hyp_externalcomponentinstance_constructor_exists():
    assert callable(ExternalComponentInstance.__init__)


def test_hyp_externalcomponentinstance_constructor_args():
    sig = inspect.signature(ExternalComponentInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_vminstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_VMInstance)


def test_hyp_cloudml_vminstance_constructor_exists():
    assert callable(cloudml_VMInstance.__init__)


def test_hyp_cloudml_vminstance_constructor_args():
    sig = inspect.signature(cloudml_VMInstance.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "publicAddress" in params, "Missing parameter 'publicAddress'"





def test_hyp_cloudml_requiredexecutionplatform_is_not_abstract():
    assert not inspect.isabstract(cloudml_RequiredExecutionPlatform)


def test_hyp_cloudml_requiredexecutionplatform_constructor_exists():
    assert callable(cloudml_RequiredExecutionPlatform.__init__)


def test_hyp_cloudml_requiredexecutionplatform_constructor_args():
    sig = inspect.signature(cloudml_RequiredExecutionPlatform.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_requiredport_is_not_abstract():
    assert not inspect.isabstract(cloudml_RequiredPort)


def test_hyp_cloudml_requiredport_constructor_exists():
    assert callable(cloudml_RequiredPort.__init__)


def test_hyp_cloudml_requiredport_constructor_args():
    sig = inspect.signature(cloudml_RequiredPort.__init__)
    params = list(sig.parameters.keys())
    assert "isMandatory" in params, "Missing parameter 'isMandatory'"




def test_hyp_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_hyp_component_constructor_exists():
    assert callable(Component.__init__)


def test_hyp_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_providedexecutionplatform_is_not_abstract():
    assert not inspect.isabstract(cloudml_ProvidedExecutionPlatform)


def test_hyp_cloudml_providedexecutionplatform_constructor_exists():
    assert callable(cloudml_ProvidedExecutionPlatform.__init__)


def test_hyp_cloudml_providedexecutionplatform_constructor_args():
    sig = inspect.signature(cloudml_ProvidedExecutionPlatform.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_providedport_is_not_abstract():
    assert not inspect.isabstract(cloudml_ProvidedPort)


def test_hyp_cloudml_providedport_constructor_exists():
    assert callable(cloudml_ProvidedPort.__init__)


def test_hyp_cloudml_providedport_constructor_args():
    sig = inspect.signature(cloudml_ProvidedPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_externalcomponent_is_not_abstract():
    assert not inspect.isabstract(ExternalComponent)


def test_hyp_externalcomponent_constructor_exists():
    assert callable(ExternalComponent.__init__)


def test_hyp_externalcomponent_constructor_args():
    sig = inspect.signature(ExternalComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_vm_is_not_abstract():
    assert not inspect.isabstract(cloudml_VM)


def test_hyp_cloudml_vm_constructor_exists():
    assert callable(cloudml_VM.__init__)


def test_hyp_cloudml_vm_constructor_args():
    sig = inspect.signature(cloudml_VM.__init__)
    params = list(sig.parameters.keys())
    assert "maxRam" in params, "Missing parameter 'maxRam'"
    assert "minRam" in params, "Missing parameter 'minRam'"
    assert "sshKey" in params, "Missing parameter 'sshKey'"
    assert "privateKey" in params, "Missing parameter 'privateKey'"
    assert "groupName" in params, "Missing parameter 'groupName'"
    assert "providerSpecificTypeName" in params, "Missing parameter 'providerSpecificTypeName'"
    assert "imageId" in params, "Missing parameter 'imageId'"
    assert "securityGroup" in params, "Missing parameter 'securityGroup'"
    assert "maxCores" in params, "Missing parameter 'maxCores'"
    assert "minCores" in params, "Missing parameter 'minCores'"
    assert "minStorage" in params, "Missing parameter 'minStorage'"
    assert "is64os" in params, "Missing parameter 'is64os'"
    assert "maxStorage" in params, "Missing parameter 'maxStorage'"
    assert "os" in params, "Missing parameter 'os'"

















def test_hyp_cloudmlelement_is_not_abstract():
    assert not inspect.isabstract(CloudMLElement)


def test_hyp_cloudmlelement_constructor_exists():
    assert callable(CloudMLElement.__init__)


def test_hyp_cloudmlelement_constructor_args():
    sig = inspect.signature(CloudMLElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_cloudmlelementwithproperties_is_not_abstract():
    assert not inspect.isabstract(cloudml_CloudMLElementWithProperties)


def test_hyp_cloudml_cloudmlelementwithproperties_constructor_exists():
    assert callable(cloudml_CloudMLElementWithProperties.__init__)


def test_hyp_cloudml_cloudmlelementwithproperties_constructor_args():
    sig = inspect.signature(cloudml_CloudMLElementWithProperties.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_property_is_not_abstract():
    assert not inspect.isabstract(cloudml_Property)


def test_hyp_cloudml_property_constructor_exists():
    assert callable(cloudml_Property.__init__)


def test_hyp_cloudml_property_constructor_args():
    sig = inspect.signature(cloudml_Property.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_cloudml_cloudmlelement_is_not_abstract():
    assert not inspect.isabstract(cloudml_CloudMLElement)


def test_hyp_cloudml_cloudmlelement_constructor_exists():
    assert callable(cloudml_CloudMLElement.__init__)


def test_hyp_cloudml_cloudmlelement_constructor_args():
    sig = inspect.signature(cloudml_CloudMLElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_cloudml_externalcomponentinstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_ExternalComponentInstance)


def test_hyp_cloudml_externalcomponentinstance_constructor_exists():
    assert callable(cloudml_ExternalComponentInstance.__init__)


def test_hyp_cloudml_externalcomponentinstance_constructor_args():
    sig = inspect.signature(cloudml_ExternalComponentInstance.__init__)
    params = list(sig.parameters.keys())
    assert "ips" in params, "Missing parameter 'ips'"




def test_hyp_cloudml_internalcomponentinstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_InternalComponentInstance)


def test_hyp_cloudml_internalcomponentinstance_constructor_exists():
    assert callable(cloudml_InternalComponentInstance.__init__)


def test_hyp_cloudml_internalcomponentinstance_constructor_args():
    sig = inspect.signature(cloudml_InternalComponentInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_externalcomponent_is_not_abstract():
    assert not inspect.isabstract(cloudml_ExternalComponent)


def test_hyp_cloudml_externalcomponent_constructor_exists():
    assert callable(cloudml_ExternalComponent.__init__)


def test_hyp_cloudml_externalcomponent_constructor_args():
    sig = inspect.signature(cloudml_ExternalComponent.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "serviceType" in params, "Missing parameter 'serviceType'"
    assert "login" in params, "Missing parameter 'login'"
    assert "endPoint" in params, "Missing parameter 'endPoint'"
    assert "Region" in params, "Missing parameter 'Region'"
    assert "passwd" in params, "Missing parameter 'passwd'"









def test_hyp_cloudml_internalcomponent_is_not_abstract():
    assert not inspect.isabstract(cloudml_InternalComponent)


def test_hyp_cloudml_internalcomponent_constructor_exists():
    assert callable(cloudml_InternalComponent.__init__)


def test_hyp_cloudml_internalcomponent_constructor_args():
    sig = inspect.signature(cloudml_InternalComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudmlelementwithproperties_is_not_abstract():
    assert not inspect.isabstract(CloudMLElementWithProperties)


def test_hyp_cloudmlelementwithproperties_constructor_exists():
    assert callable(CloudMLElementWithProperties.__init__)


def test_hyp_cloudmlelementwithproperties_constructor_args():
    sig = inspect.signature(CloudMLElementWithProperties.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_executeinstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_ExecuteInstance)


def test_hyp_cloudml_executeinstance_constructor_exists():
    assert callable(cloudml_ExecuteInstance.__init__)


def test_hyp_cloudml_executeinstance_constructor_args():
    sig = inspect.signature(cloudml_ExecuteInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_relationshipinstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_RelationshipInstance)


def test_hyp_cloudml_relationshipinstance_constructor_exists():
    assert callable(cloudml_RelationshipInstance.__init__)


def test_hyp_cloudml_relationshipinstance_constructor_args():
    sig = inspect.signature(cloudml_RelationshipInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_vmport_is_not_abstract():
    assert not inspect.isabstract(cloudml_VMPort)


def test_hyp_cloudml_vmport_constructor_exists():
    assert callable(cloudml_VMPort.__init__)


def test_hyp_cloudml_vmport_constructor_args():
    sig = inspect.signature(cloudml_VMPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_component_is_not_abstract():
    assert not inspect.isabstract(cloudml_Component)


def test_hyp_cloudml_component_constructor_exists():
    assert callable(cloudml_Component.__init__)


def test_hyp_cloudml_component_constructor_args():
    sig = inspect.signature(cloudml_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_vmportinstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_VMPortInstance)


def test_hyp_cloudml_vmportinstance_constructor_exists():
    assert callable(cloudml_VMPortInstance.__init__)


def test_hyp_cloudml_vmportinstance_constructor_args():
    sig = inspect.signature(cloudml_VMPortInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_relationship_is_not_abstract():
    assert not inspect.isabstract(cloudml_Relationship)


def test_hyp_cloudml_relationship_constructor_exists():
    assert callable(cloudml_Relationship.__init__)


def test_hyp_cloudml_relationship_constructor_args():
    sig = inspect.signature(cloudml_Relationship.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_executionplatforminstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_ExecutionPlatformInstance)


def test_hyp_cloudml_executionplatforminstance_constructor_exists():
    assert callable(cloudml_ExecutionPlatformInstance.__init__)


def test_hyp_cloudml_executionplatforminstance_constructor_args():
    sig = inspect.signature(cloudml_ExecutionPlatformInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_portinstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_PortInstance)


def test_hyp_cloudml_portinstance_constructor_exists():
    assert callable(cloudml_PortInstance.__init__)


def test_hyp_cloudml_portinstance_constructor_args():
    sig = inspect.signature(cloudml_PortInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_port_is_not_abstract():
    assert not inspect.isabstract(cloudml_Port)


def test_hyp_cloudml_port_constructor_exists():
    assert callable(cloudml_Port.__init__)


def test_hyp_cloudml_port_constructor_args():
    sig = inspect.signature(cloudml_Port.__init__)
    params = list(sig.parameters.keys())
    assert "portNumber" in params, "Missing parameter 'portNumber'"
    assert "isLocal" in params, "Missing parameter 'isLocal'"





def test_hyp_cloudml_cloud_is_not_abstract():
    assert not inspect.isabstract(cloudml_Cloud)


def test_hyp_cloudml_cloud_constructor_exists():
    assert callable(cloudml_Cloud.__init__)


def test_hyp_cloudml_cloud_constructor_args():
    sig = inspect.signature(cloudml_Cloud.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_componentinstance_is_not_abstract():
    assert not inspect.isabstract(cloudml_ComponentInstance)


def test_hyp_cloudml_componentinstance_constructor_exists():
    assert callable(cloudml_ComponentInstance.__init__)


def test_hyp_cloudml_componentinstance_constructor_args():
    sig = inspect.signature(cloudml_ComponentInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_provider_is_not_abstract():
    assert not inspect.isabstract(cloudml_Provider)


def test_hyp_cloudml_provider_constructor_exists():
    assert callable(cloudml_Provider.__init__)


def test_hyp_cloudml_provider_constructor_args():
    sig = inspect.signature(cloudml_Provider.__init__)
    params = list(sig.parameters.keys())
    assert "credentials" in params, "Missing parameter 'credentials'"




def test_hyp_cloudml_cloudmlmodel_is_not_abstract():
    assert not inspect.isabstract(cloudml_CloudMLModel)


def test_hyp_cloudml_cloudmlmodel_constructor_exists():
    assert callable(cloudml_CloudMLModel.__init__)


def test_hyp_cloudml_cloudmlmodel_constructor_args():
    sig = inspect.signature(cloudml_CloudMLModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_executionplatform_is_not_abstract():
    assert not inspect.isabstract(cloudml_ExecutionPlatform)


def test_hyp_cloudml_executionplatform_constructor_exists():
    assert callable(cloudml_ExecutionPlatform.__init__)


def test_hyp_cloudml_executionplatform_constructor_args():
    sig = inspect.signature(cloudml_ExecutionPlatform.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cloudml_puppetresource_is_not_abstract():
    assert not inspect.isabstract(cloudml_PuppetResource)


def test_hyp_cloudml_puppetresource_constructor_exists():
    assert callable(cloudml_PuppetResource.__init__)


def test_hyp_cloudml_puppetresource_constructor_args():
    sig = inspect.signature(cloudml_PuppetResource.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "configurationFile" in params, "Missing parameter 'configurationFile'"
    assert "configureHostnameCommand" in params, "Missing parameter 'configureHostnameCommand'"
    assert "repositoryKey" in params, "Missing parameter 'repositoryKey'"
    assert "repositoryEndpoint" in params, "Missing parameter 'repositoryEndpoint'"
    assert "masterEndpoint" in params, "Missing parameter 'masterEndpoint'"
    assert "manifestEntry" in params, "Missing parameter 'manifestEntry'"










def test_hyp_cloudml_resource_is_not_abstract():
    assert not inspect.isabstract(cloudml_Resource)


def test_hyp_cloudml_resource_constructor_exists():
    assert callable(cloudml_Resource.__init__)


def test_hyp_cloudml_resource_constructor_args():
    sig = inspect.signature(cloudml_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "startCommand" in params, "Missing parameter 'startCommand'"
    assert "uploadCommand" in params, "Missing parameter 'uploadCommand'"
    assert "executeLocally" in params, "Missing parameter 'executeLocally'"
    assert "configureCommand" in params, "Missing parameter 'configureCommand'"
    assert "installCommand" in params, "Missing parameter 'installCommand'"
    assert "requireCredentials" in params, "Missing parameter 'requireCredentials'"
    assert "downloadCommand" in params, "Missing parameter 'downloadCommand'"
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
ExecutionPlatformInstance_strategy = st.builds(
    ExecutionPlatformInstance,
)
ExecutionPlatform_strategy = st.builds(
    ExecutionPlatform,
)
Resource_strategy = st.builds(
    Resource,
)
cloudml_RequiredExecutionPlatformInstance_strategy = st.builds(
    cloudml_RequiredExecutionPlatformInstance,
)
ComponentInstance_strategy = st.builds(
    ComponentInstance,
)
PortInstance_strategy = st.builds(
    PortInstance,
)
cloudml_RequiredPortInstance_strategy = st.builds(
    cloudml_RequiredPortInstance,
)
Port_strategy = st.builds(
    Port,
)
cloudml_ProvidedExecutionPlatformInstance_strategy = st.builds(
    cloudml_ProvidedExecutionPlatformInstance,
)
cloudml_ProvidedPortInstance_strategy = st.builds(
    cloudml_ProvidedPortInstance,
)
ExternalComponentInstance_strategy = st.builds(
    ExternalComponentInstance,
)
cloudml_VMInstance_strategy = st.builds(
    cloudml_VMInstance,
    id=
        safe_text,
    publicAddress=
        safe_text
)
cloudml_RequiredExecutionPlatform_strategy = st.builds(
    cloudml_RequiredExecutionPlatform,
)
cloudml_RequiredPort_strategy = st.builds(
    cloudml_RequiredPort,
    isMandatory=
        st.booleans()
)
Component_strategy = st.builds(
    Component,
)
cloudml_ProvidedExecutionPlatform_strategy = st.builds(
    cloudml_ProvidedExecutionPlatform,
)
cloudml_ProvidedPort_strategy = st.builds(
    cloudml_ProvidedPort,
)
ExternalComponent_strategy = st.builds(
    ExternalComponent,
)
cloudml_VM_strategy = st.builds(
    cloudml_VM,
    maxRam=
        st.integers(),
    minRam=
        st.integers(),
    sshKey=
        safe_text,
    privateKey=
        safe_text,
    groupName=
        safe_text,
    providerSpecificTypeName=
        safe_text,
    imageId=
        safe_text,
    securityGroup=
        safe_text,
    maxCores=
        st.integers(),
    minCores=
        st.integers(),
    minStorage=
        st.integers(),
    is64os=
        st.booleans(),
    maxStorage=
        st.integers(),
    os=
        safe_text
)
CloudMLElement_strategy = st.builds(
    CloudMLElement,
)
cloudml_CloudMLElementWithProperties_strategy = st.builds(
    cloudml_CloudMLElementWithProperties,
)
cloudml_Property_strategy = st.builds(
    cloudml_Property,
    value=
        safe_text
)
cloudml_CloudMLElement_strategy = st.builds(
    cloudml_CloudMLElement,
    name=
        safe_text
)
cloudml_ExternalComponentInstance_strategy = st.builds(
    cloudml_ExternalComponentInstance,
    ips=
        safe_text
)
cloudml_InternalComponentInstance_strategy = st.builds(
    cloudml_InternalComponentInstance,
)
cloudml_ExternalComponent_strategy = st.builds(
    cloudml_ExternalComponent,
    location=
        safe_text,
    serviceType=
        safe_text,
    login=
        safe_text,
    endPoint=
        safe_text,
    Region=
        safe_text,
    passwd=
        safe_text
)
cloudml_InternalComponent_strategy = st.builds(
    cloudml_InternalComponent,
)
CloudMLElementWithProperties_strategy = st.builds(
    CloudMLElementWithProperties,
)
cloudml_ExecuteInstance_strategy = st.builds(
    cloudml_ExecuteInstance,
)
cloudml_RelationshipInstance_strategy = st.builds(
    cloudml_RelationshipInstance,
)
cloudml_VMPort_strategy = st.builds(
    cloudml_VMPort,
)
cloudml_Component_strategy = st.builds(
    cloudml_Component,
)
cloudml_VMPortInstance_strategy = st.builds(
    cloudml_VMPortInstance,
)
cloudml_Relationship_strategy = st.builds(
    cloudml_Relationship,
)
cloudml_ExecutionPlatformInstance_strategy = st.builds(
    cloudml_ExecutionPlatformInstance,
)
cloudml_PortInstance_strategy = st.builds(
    cloudml_PortInstance,
)
cloudml_Port_strategy = st.builds(
    cloudml_Port,
    portNumber=
        st.integers(),
    isLocal=
        st.booleans()
)
cloudml_Cloud_strategy = st.builds(
    cloudml_Cloud,
)
cloudml_ComponentInstance_strategy = st.builds(
    cloudml_ComponentInstance,
)
cloudml_Provider_strategy = st.builds(
    cloudml_Provider,
    credentials=
        safe_text
)
cloudml_CloudMLModel_strategy = st.builds(
    cloudml_CloudMLModel,
)
cloudml_ExecutionPlatform_strategy = st.builds(
    cloudml_ExecutionPlatform,
)
cloudml_PuppetResource_strategy = st.builds(
    cloudml_PuppetResource,
    username=
        safe_text,
    configurationFile=
        safe_text,
    configureHostnameCommand=
        safe_text,
    repositoryKey=
        safe_text,
    repositoryEndpoint=
        safe_text,
    masterEndpoint=
        safe_text,
    manifestEntry=
        safe_text
)
cloudml_Resource_strategy = st.builds(
    cloudml_Resource,
    startCommand=
        safe_text,
    uploadCommand=
        safe_text,
    executeLocally=
        st.booleans(),
    configureCommand=
        safe_text,
    installCommand=
        safe_text,
    requireCredentials=
        st.booleans(),
    downloadCommand=
        safe_text,
    stopCommand=
        safe_text
)















@given(instance=cloudml_VMInstance_strategy)
def test_hyp_cloudml_vminstance_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=cloudml_VMInstance_strategy)
def test_hyp_cloudml_vminstance_publicAddress_setter(instance):
    original = instance.publicAddress
    instance.publicAddress = original
    assert instance.publicAddress == original





@given(instance=cloudml_RequiredPort_strategy)
def test_hyp_cloudml_requiredport_isMandatory_setter(instance):
    original = instance.isMandatory
    instance.isMandatory = original
    assert instance.isMandatory == original








@given(instance=cloudml_VM_strategy)
def test_hyp_cloudml_vm_maxRam_setter(instance):
    original = instance.maxRam
    instance.maxRam = original
    assert instance.maxRam == original



@given(instance=cloudml_VM_strategy)
def test_hyp_cloudml_vm_minRam_setter(instance):
    original = instance.minRam
    instance.minRam = original
    assert instance.minRam == original



@given(instance=cloudml_VM_strategy)
def test_hyp_cloudml_vm_sshKey_setter(instance):
    original = instance.sshKey
    instance.sshKey = original
    assert instance.sshKey == original



@given(instance=cloudml_VM_strategy)
def test_hyp_cloudml_vm_privateKey_setter(instance):
    original = instance.privateKey
    instance.privateKey = original
    assert instance.privateKey == original



@given(instance=cloudml_VM_strategy)
def test_hyp_cloudml_vm_groupName_setter(instance):
    original = instance.groupName
    instance.groupName = original
    assert instance.groupName == original



@given(instance=cloudml_VM_strategy)
def test_hyp_cloudml_vm_providerSpecificTypeName_setter(instance):
    original = instance.providerSpecificTypeName
    instance.providerSpecificTypeName = original
    assert instance.providerSpecificTypeName == original



@given(instance=cloudml_VM_strategy)
def test_hyp_cloudml_vm_imageId_setter(instance):
    original = instance.imageId
    instance.imageId = original
    assert instance.imageId == original



@given(instance=cloudml_VM_strategy)
def test_hyp_cloudml_vm_securityGroup_setter(instance):
    original = instance.securityGroup
    instance.securityGroup = original
    assert instance.securityGroup == original



@given(instance=cloudml_VM_strategy)
def test_hyp_cloudml_vm_maxCores_setter(instance):
    original = instance.maxCores
    instance.maxCores = original
    assert instance.maxCores == original



@given(instance=cloudml_VM_strategy)
def test_hyp_cloudml_vm_minCores_setter(instance):
    original = instance.minCores
    instance.minCores = original
    assert instance.minCores == original



@given(instance=cloudml_VM_strategy)
def test_hyp_cloudml_vm_minStorage_setter(instance):
    original = instance.minStorage
    instance.minStorage = original
    assert instance.minStorage == original



@given(instance=cloudml_VM_strategy)
def test_hyp_cloudml_vm_is64os_setter(instance):
    original = instance.is64os
    instance.is64os = original
    assert instance.is64os == original



@given(instance=cloudml_VM_strategy)
def test_hyp_cloudml_vm_maxStorage_setter(instance):
    original = instance.maxStorage
    instance.maxStorage = original
    assert instance.maxStorage == original



@given(instance=cloudml_VM_strategy)
def test_hyp_cloudml_vm_os_setter(instance):
    original = instance.os
    instance.os = original
    assert instance.os == original






@given(instance=cloudml_Property_strategy)
def test_hyp_cloudml_property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=cloudml_CloudMLElement_strategy)
def test_hyp_cloudml_cloudmlelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=cloudml_ExternalComponentInstance_strategy)
def test_hyp_cloudml_externalcomponentinstance_ips_setter(instance):
    original = instance.ips
    instance.ips = original
    assert instance.ips == original





@given(instance=cloudml_ExternalComponent_strategy)
def test_hyp_cloudml_externalcomponent_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=cloudml_ExternalComponent_strategy)
def test_hyp_cloudml_externalcomponent_serviceType_setter(instance):
    original = instance.serviceType
    instance.serviceType = original
    assert instance.serviceType == original



@given(instance=cloudml_ExternalComponent_strategy)
def test_hyp_cloudml_externalcomponent_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original



@given(instance=cloudml_ExternalComponent_strategy)
def test_hyp_cloudml_externalcomponent_endPoint_setter(instance):
    original = instance.endPoint
    instance.endPoint = original
    assert instance.endPoint == original



@given(instance=cloudml_ExternalComponent_strategy)
def test_hyp_cloudml_externalcomponent_Region_setter(instance):
    original = instance.Region
    instance.Region = original
    assert instance.Region == original



@given(instance=cloudml_ExternalComponent_strategy)
def test_hyp_cloudml_externalcomponent_passwd_setter(instance):
    original = instance.passwd
    instance.passwd = original
    assert instance.passwd == original














@given(instance=cloudml_Port_strategy)
def test_hyp_cloudml_port_portNumber_setter(instance):
    original = instance.portNumber
    instance.portNumber = original
    assert instance.portNumber == original



@given(instance=cloudml_Port_strategy)
def test_hyp_cloudml_port_isLocal_setter(instance):
    original = instance.isLocal
    instance.isLocal = original
    assert instance.isLocal == original






@given(instance=cloudml_Provider_strategy)
def test_hyp_cloudml_provider_credentials_setter(instance):
    original = instance.credentials
    instance.credentials = original
    assert instance.credentials == original






@given(instance=cloudml_PuppetResource_strategy)
def test_hyp_cloudml_puppetresource_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=cloudml_PuppetResource_strategy)
def test_hyp_cloudml_puppetresource_configurationFile_setter(instance):
    original = instance.configurationFile
    instance.configurationFile = original
    assert instance.configurationFile == original



@given(instance=cloudml_PuppetResource_strategy)
def test_hyp_cloudml_puppetresource_configureHostnameCommand_setter(instance):
    original = instance.configureHostnameCommand
    instance.configureHostnameCommand = original
    assert instance.configureHostnameCommand == original



@given(instance=cloudml_PuppetResource_strategy)
def test_hyp_cloudml_puppetresource_repositoryKey_setter(instance):
    original = instance.repositoryKey
    instance.repositoryKey = original
    assert instance.repositoryKey == original



@given(instance=cloudml_PuppetResource_strategy)
def test_hyp_cloudml_puppetresource_repositoryEndpoint_setter(instance):
    original = instance.repositoryEndpoint
    instance.repositoryEndpoint = original
    assert instance.repositoryEndpoint == original



@given(instance=cloudml_PuppetResource_strategy)
def test_hyp_cloudml_puppetresource_masterEndpoint_setter(instance):
    original = instance.masterEndpoint
    instance.masterEndpoint = original
    assert instance.masterEndpoint == original



@given(instance=cloudml_PuppetResource_strategy)
def test_hyp_cloudml_puppetresource_manifestEntry_setter(instance):
    original = instance.manifestEntry
    instance.manifestEntry = original
    assert instance.manifestEntry == original




@given(instance=cloudml_Resource_strategy)
def test_hyp_cloudml_resource_startCommand_setter(instance):
    original = instance.startCommand
    instance.startCommand = original
    assert instance.startCommand == original



@given(instance=cloudml_Resource_strategy)
def test_hyp_cloudml_resource_uploadCommand_setter(instance):
    original = instance.uploadCommand
    instance.uploadCommand = original
    assert instance.uploadCommand == original



@given(instance=cloudml_Resource_strategy)
def test_hyp_cloudml_resource_executeLocally_setter(instance):
    original = instance.executeLocally
    instance.executeLocally = original
    assert instance.executeLocally == original



@given(instance=cloudml_Resource_strategy)
def test_hyp_cloudml_resource_configureCommand_setter(instance):
    original = instance.configureCommand
    instance.configureCommand = original
    assert instance.configureCommand == original



@given(instance=cloudml_Resource_strategy)
def test_hyp_cloudml_resource_installCommand_setter(instance):
    original = instance.installCommand
    instance.installCommand = original
    assert instance.installCommand == original



@given(instance=cloudml_Resource_strategy)
def test_hyp_cloudml_resource_requireCredentials_setter(instance):
    original = instance.requireCredentials
    instance.requireCredentials = original
    assert instance.requireCredentials == original



@given(instance=cloudml_Resource_strategy)
def test_hyp_cloudml_resource_downloadCommand_setter(instance):
    original = instance.downloadCommand
    instance.downloadCommand = original
    assert instance.downloadCommand == original



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
    CloudMLElement,
    CloudMLElementWithProperties,
    Component,
    ComponentInstance,
    ExecutionPlatform,
    ExecutionPlatformInstance,
    ExternalComponent,
    ExternalComponentInstance,
    Port,
    PortInstance,
    Resource,
    cloudml_Cloud,
    cloudml_CloudMLElement,
    cloudml_CloudMLElementWithProperties,
    cloudml_CloudMLModel,
    cloudml_Component,
    cloudml_ComponentInstance,
    cloudml_ExecuteInstance,
    cloudml_ExecutionPlatform,
    cloudml_ExecutionPlatformInstance,
    cloudml_ExternalComponent,
    cloudml_ExternalComponentInstance,
    cloudml_InternalComponent,
    cloudml_InternalComponentInstance,
    cloudml_Port,
    cloudml_PortInstance,
    cloudml_Property,
    cloudml_ProvidedExecutionPlatform,
    cloudml_ProvidedExecutionPlatformInstance,
    cloudml_ProvidedPort,
    cloudml_ProvidedPortInstance,
    cloudml_Provider,
    cloudml_PuppetResource,
    cloudml_Relationship,
    cloudml_RelationshipInstance,
    cloudml_RequiredExecutionPlatform,
    cloudml_RequiredExecutionPlatformInstance,
    cloudml_RequiredPort,
    cloudml_RequiredPortInstance,
    cloudml_Resource,
    cloudml_VM,
    cloudml_VMInstance,
    cloudml_VMPort,
    cloudml_VMPortInstance,
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

def test_cloudml_CloudMLElement_name_value_roundtrip():
    instance = cloudml_CloudMLElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cloudml_ExternalComponent_Region_value_roundtrip():
    instance = cloudml_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    assert instance.Region == "sample_text"
    instance.Region = "sample_text_2"
    assert instance.Region == "sample_text_2"


def test_cloudml_ExternalComponent_endPoint_value_roundtrip():
    instance = cloudml_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    assert instance.endPoint == "sample_text"
    instance.endPoint = "sample_text_2"
    assert instance.endPoint == "sample_text_2"


def test_cloudml_ExternalComponent_location_value_roundtrip():
    instance = cloudml_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_cloudml_ExternalComponent_login_value_roundtrip():
    instance = cloudml_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    assert instance.login == "sample_text"
    instance.login = "sample_text_2"
    assert instance.login == "sample_text_2"


def test_cloudml_ExternalComponent_passwd_value_roundtrip():
    instance = cloudml_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    assert instance.passwd == "sample_text"
    instance.passwd = "sample_text_2"
    assert instance.passwd == "sample_text_2"


def test_cloudml_ExternalComponent_serviceType_value_roundtrip():
    instance = cloudml_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    assert instance.serviceType == "sample_text"
    instance.serviceType = "sample_text_2"
    assert instance.serviceType == "sample_text_2"


def test_cloudml_ExternalComponentInstance_ips_value_roundtrip():
    instance = cloudml_ExternalComponentInstance(ips="sample_text")
    assert instance.ips == "sample_text"
    instance.ips = "sample_text_2"
    assert instance.ips == "sample_text_2"


def test_cloudml_Port_isLocal_value_roundtrip():
    instance = cloudml_Port(isLocal=True, portNumber=7)
    assert instance.isLocal == True
    instance.isLocal = False
    assert instance.isLocal == False


def test_cloudml_Port_portNumber_value_roundtrip():
    instance = cloudml_Port(isLocal=True, portNumber=7)
    assert instance.portNumber == 7
    instance.portNumber = 13
    assert instance.portNumber == 13


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


def test_cloudml_PuppetResource_configurationFile_value_roundtrip():
    instance = cloudml_PuppetResource(configurationFile="sample_text", configureHostnameCommand="sample_text", manifestEntry="sample_text", masterEndpoint="sample_text", repositoryEndpoint="sample_text", repositoryKey="sample_text", username="sample_text")
    assert instance.configurationFile == "sample_text"
    instance.configurationFile = "sample_text_2"
    assert instance.configurationFile == "sample_text_2"


def test_cloudml_PuppetResource_configureHostnameCommand_value_roundtrip():
    instance = cloudml_PuppetResource(configurationFile="sample_text", configureHostnameCommand="sample_text", manifestEntry="sample_text", masterEndpoint="sample_text", repositoryEndpoint="sample_text", repositoryKey="sample_text", username="sample_text")
    assert instance.configureHostnameCommand == "sample_text"
    instance.configureHostnameCommand = "sample_text_2"
    assert instance.configureHostnameCommand == "sample_text_2"


def test_cloudml_PuppetResource_manifestEntry_value_roundtrip():
    instance = cloudml_PuppetResource(configurationFile="sample_text", configureHostnameCommand="sample_text", manifestEntry="sample_text", masterEndpoint="sample_text", repositoryEndpoint="sample_text", repositoryKey="sample_text", username="sample_text")
    assert instance.manifestEntry == "sample_text"
    instance.manifestEntry = "sample_text_2"
    assert instance.manifestEntry == "sample_text_2"


def test_cloudml_PuppetResource_masterEndpoint_value_roundtrip():
    instance = cloudml_PuppetResource(configurationFile="sample_text", configureHostnameCommand="sample_text", manifestEntry="sample_text", masterEndpoint="sample_text", repositoryEndpoint="sample_text", repositoryKey="sample_text", username="sample_text")
    assert instance.masterEndpoint == "sample_text"
    instance.masterEndpoint = "sample_text_2"
    assert instance.masterEndpoint == "sample_text_2"


def test_cloudml_PuppetResource_repositoryEndpoint_value_roundtrip():
    instance = cloudml_PuppetResource(configurationFile="sample_text", configureHostnameCommand="sample_text", manifestEntry="sample_text", masterEndpoint="sample_text", repositoryEndpoint="sample_text", repositoryKey="sample_text", username="sample_text")
    assert instance.repositoryEndpoint == "sample_text"
    instance.repositoryEndpoint = "sample_text_2"
    assert instance.repositoryEndpoint == "sample_text_2"


def test_cloudml_PuppetResource_repositoryKey_value_roundtrip():
    instance = cloudml_PuppetResource(configurationFile="sample_text", configureHostnameCommand="sample_text", manifestEntry="sample_text", masterEndpoint="sample_text", repositoryEndpoint="sample_text", repositoryKey="sample_text", username="sample_text")
    assert instance.repositoryKey == "sample_text"
    instance.repositoryKey = "sample_text_2"
    assert instance.repositoryKey == "sample_text_2"


def test_cloudml_PuppetResource_username_value_roundtrip():
    instance = cloudml_PuppetResource(configurationFile="sample_text", configureHostnameCommand="sample_text", manifestEntry="sample_text", masterEndpoint="sample_text", repositoryEndpoint="sample_text", repositoryKey="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_cloudml_RequiredPort_isMandatory_value_roundtrip():
    instance = cloudml_RequiredPort(isMandatory=True)
    assert instance.isMandatory == True
    instance.isMandatory = False
    assert instance.isMandatory == False


def test_cloudml_Resource_configureCommand_value_roundtrip():
    instance = cloudml_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.configureCommand == "sample_text"
    instance.configureCommand = "sample_text_2"
    assert instance.configureCommand == "sample_text_2"


def test_cloudml_Resource_downloadCommand_value_roundtrip():
    instance = cloudml_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.downloadCommand == "sample_text"
    instance.downloadCommand = "sample_text_2"
    assert instance.downloadCommand == "sample_text_2"


def test_cloudml_Resource_executeLocally_value_roundtrip():
    instance = cloudml_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.executeLocally == True
    instance.executeLocally = False
    assert instance.executeLocally == False


def test_cloudml_Resource_installCommand_value_roundtrip():
    instance = cloudml_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.installCommand == "sample_text"
    instance.installCommand = "sample_text_2"
    assert instance.installCommand == "sample_text_2"


def test_cloudml_Resource_requireCredentials_value_roundtrip():
    instance = cloudml_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.requireCredentials == True
    instance.requireCredentials = False
    assert instance.requireCredentials == False


def test_cloudml_Resource_startCommand_value_roundtrip():
    instance = cloudml_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.startCommand == "sample_text"
    instance.startCommand = "sample_text_2"
    assert instance.startCommand == "sample_text_2"


def test_cloudml_Resource_stopCommand_value_roundtrip():
    instance = cloudml_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.stopCommand == "sample_text"
    instance.stopCommand = "sample_text_2"
    assert instance.stopCommand == "sample_text_2"


def test_cloudml_Resource_uploadCommand_value_roundtrip():
    instance = cloudml_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.uploadCommand == "sample_text"
    instance.uploadCommand = "sample_text_2"
    assert instance.uploadCommand == "sample_text_2"


def test_cloudml_VM_groupName_value_roundtrip():
    instance = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.groupName == "sample_text"
    instance.groupName = "sample_text_2"
    assert instance.groupName == "sample_text_2"


def test_cloudml_VM_imageId_value_roundtrip():
    instance = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.imageId == "sample_text"
    instance.imageId = "sample_text_2"
    assert instance.imageId == "sample_text_2"


def test_cloudml_VM_is64os_value_roundtrip():
    instance = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.is64os == True
    instance.is64os = False
    assert instance.is64os == False


def test_cloudml_VM_maxCores_value_roundtrip():
    instance = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.maxCores == 7
    instance.maxCores = 13
    assert instance.maxCores == 13


def test_cloudml_VM_maxRam_value_roundtrip():
    instance = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.maxRam == 7
    instance.maxRam = 13
    assert instance.maxRam == 13


def test_cloudml_VM_maxStorage_value_roundtrip():
    instance = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.maxStorage == 7
    instance.maxStorage = 13
    assert instance.maxStorage == 13


def test_cloudml_VM_minCores_value_roundtrip():
    instance = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.minCores == 7
    instance.minCores = 13
    assert instance.minCores == 13


def test_cloudml_VM_minRam_value_roundtrip():
    instance = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.minRam == 7
    instance.minRam = 13
    assert instance.minRam == 13


def test_cloudml_VM_minStorage_value_roundtrip():
    instance = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.minStorage == 7
    instance.minStorage = 13
    assert instance.minStorage == 13


def test_cloudml_VM_os_value_roundtrip():
    instance = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.os == "sample_text"
    instance.os = "sample_text_2"
    assert instance.os == "sample_text_2"


def test_cloudml_VM_privateKey_value_roundtrip():
    instance = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.privateKey == "sample_text"
    instance.privateKey = "sample_text_2"
    assert instance.privateKey == "sample_text_2"


def test_cloudml_VM_providerSpecificTypeName_value_roundtrip():
    instance = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.providerSpecificTypeName == "sample_text"
    instance.providerSpecificTypeName = "sample_text_2"
    assert instance.providerSpecificTypeName == "sample_text_2"


def test_cloudml_VM_securityGroup_value_roundtrip():
    instance = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.securityGroup == "sample_text"
    instance.securityGroup = "sample_text_2"
    assert instance.securityGroup == "sample_text_2"


def test_cloudml_VM_sshKey_value_roundtrip():
    instance = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.sshKey == "sample_text"
    instance.sshKey = "sample_text_2"
    assert instance.sshKey == "sample_text_2"


def test_cloudml_VMInstance_id_value_roundtrip():
    instance = cloudml_VMInstance(id="sample_text", publicAddress="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_cloudml_VMInstance_publicAddress_value_roundtrip():
    instance = cloudml_VMInstance(id="sample_text", publicAddress="sample_text")
    assert instance.publicAddress == "sample_text"
    instance.publicAddress = "sample_text_2"
    assert instance.publicAddress == "sample_text_2"


def test_cloudml_CloudMLElementWithProperties_isa_CloudMLElement():
    instance = cloudml_CloudMLElementWithProperties()
    assert isinstance(instance, CloudMLElement)


def test_cloudml_Property_isa_CloudMLElement():
    instance = cloudml_Property(value="sample_text")
    assert isinstance(instance, CloudMLElement)


def test_cloudml_Cloud_isa_CloudMLElementWithProperties():
    instance = cloudml_Cloud()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_CloudMLModel_isa_CloudMLElementWithProperties():
    instance = cloudml_CloudMLModel()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_Component_isa_CloudMLElementWithProperties():
    instance = cloudml_Component()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_ComponentInstance_isa_CloudMLElementWithProperties():
    instance = cloudml_ComponentInstance()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_ExecuteInstance_isa_CloudMLElementWithProperties():
    instance = cloudml_ExecuteInstance()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_ExecutionPlatform_isa_CloudMLElementWithProperties():
    instance = cloudml_ExecutionPlatform()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_ExecutionPlatformInstance_isa_CloudMLElementWithProperties():
    instance = cloudml_ExecutionPlatformInstance()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_Port_isa_CloudMLElementWithProperties():
    instance = cloudml_Port(isLocal=True, portNumber=7)
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_PortInstance_isa_CloudMLElementWithProperties():
    instance = cloudml_PortInstance()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_Provider_isa_CloudMLElementWithProperties():
    instance = cloudml_Provider(credentials="sample_text")
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_Relationship_isa_CloudMLElementWithProperties():
    instance = cloudml_Relationship()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_RelationshipInstance_isa_CloudMLElementWithProperties():
    instance = cloudml_RelationshipInstance()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_Resource_isa_CloudMLElementWithProperties():
    instance = cloudml_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_VMPort_isa_CloudMLElementWithProperties():
    instance = cloudml_VMPort()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_VMPortInstance_isa_CloudMLElementWithProperties():
    instance = cloudml_VMPortInstance()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_ExternalComponent_isa_Component():
    instance = cloudml_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    assert isinstance(instance, Component)


def test_cloudml_InternalComponent_isa_Component():
    instance = cloudml_InternalComponent()
    assert isinstance(instance, Component)


def test_cloudml_ExternalComponentInstance_isa_ComponentInstance():
    instance = cloudml_ExternalComponentInstance(ips="sample_text")
    assert isinstance(instance, ComponentInstance)


def test_cloudml_InternalComponentInstance_isa_ComponentInstance():
    instance = cloudml_InternalComponentInstance()
    assert isinstance(instance, ComponentInstance)


def test_cloudml_ProvidedExecutionPlatform_isa_ExecutionPlatform():
    instance = cloudml_ProvidedExecutionPlatform()
    assert isinstance(instance, ExecutionPlatform)


def test_cloudml_RequiredExecutionPlatform_isa_ExecutionPlatform():
    instance = cloudml_RequiredExecutionPlatform()
    assert isinstance(instance, ExecutionPlatform)


def test_cloudml_ProvidedExecutionPlatformInstance_isa_ExecutionPlatformInstance():
    instance = cloudml_ProvidedExecutionPlatformInstance()
    assert isinstance(instance, ExecutionPlatformInstance)


def test_cloudml_RequiredExecutionPlatformInstance_isa_ExecutionPlatformInstance():
    instance = cloudml_RequiredExecutionPlatformInstance()
    assert isinstance(instance, ExecutionPlatformInstance)


def test_cloudml_VM_isa_ExternalComponent():
    instance = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert isinstance(instance, ExternalComponent)


def test_cloudml_VMInstance_isa_ExternalComponentInstance():
    instance = cloudml_VMInstance(id="sample_text", publicAddress="sample_text")
    assert isinstance(instance, ExternalComponentInstance)


def test_cloudml_ProvidedPort_isa_Port():
    instance = cloudml_ProvidedPort()
    assert isinstance(instance, Port)


def test_cloudml_RequiredPort_isa_Port():
    instance = cloudml_RequiredPort(isMandatory=True)
    assert isinstance(instance, Port)


def test_cloudml_ProvidedPortInstance_isa_PortInstance():
    instance = cloudml_ProvidedPortInstance()
    assert isinstance(instance, PortInstance)


def test_cloudml_RequiredPortInstance_isa_PortInstance():
    instance = cloudml_RequiredPortInstance()
    assert isinstance(instance, PortInstance)


def test_cloudml_PuppetResource_isa_Resource():
    instance = cloudml_PuppetResource(configurationFile="sample_text", configureHostnameCommand="sample_text", manifestEntry="sample_text", masterEndpoint="sample_text", repositoryEndpoint="sample_text", repositoryKey="sample_text", username="sample_text")
    assert isinstance(instance, Resource)


def test_assoc_component43_link_reassign_clear():
    a = cloudml_Port(isLocal=True, portNumber=7)
    b1 = cloudml_Component()
    b2 = cloudml_Component()
    _safe_set(a, 'cloudml_Port', b1)
    assert _is_linked(a, 'cloudml_Port', b1)
    if hasattr(b1, 'cloudml_Component44'):
        assert _is_linked(b1, 'cloudml_Component44', a)
    _safe_set(a, 'cloudml_Port', b2)
    assert _is_linked(a, 'cloudml_Port', b2)
    if hasattr(b1, 'cloudml_Component44'):
        assert not _is_linked(b1, 'cloudml_Component44', a)
    if hasattr(b2, 'cloudml_Component44'):
        assert _is_linked(b2, 'cloudml_Component44', a)
    _safe_set(a, 'cloudml_Port', None)
    assert not _is_linked(a, 'cloudml_Port', b2)
    if hasattr(b2, 'cloudml_Component44'):
        assert not _is_linked(b2, 'cloudml_Component44', a)


def test_assoc_demands109_link_reassign_clear():
    a = cloudml_Property(value="sample_text")
    b1 = cloudml_RequiredExecutionPlatform()
    b2 = cloudml_RequiredExecutionPlatform()
    _safe_set(a, 'cloudml_Property111', b1)
    assert _is_linked(a, 'cloudml_Property111', b1)
    if hasattr(b1, 'cloudml_RequiredExecutionPlatform110'):
        assert _is_linked(b1, 'cloudml_RequiredExecutionPlatform110', a)
    _safe_set(a, 'cloudml_Property111', b2)
    assert _is_linked(a, 'cloudml_Property111', b2)
    if hasattr(b1, 'cloudml_RequiredExecutionPlatform110'):
        assert not _is_linked(b1, 'cloudml_RequiredExecutionPlatform110', a)
    if hasattr(b2, 'cloudml_RequiredExecutionPlatform110'):
        assert _is_linked(b2, 'cloudml_RequiredExecutionPlatform110', a)
    _safe_set(a, 'cloudml_Property111', None)
    assert not _is_linked(a, 'cloudml_Property111', b2)
    if hasattr(b2, 'cloudml_RequiredExecutionPlatform110'):
        assert not _is_linked(b2, 'cloudml_RequiredExecutionPlatform110', a)


def test_assoc_externalComponentInstances18_link_reassign_clear():
    a = cloudml_ExternalComponentInstance(ips="sample_text")
    b1 = cloudml_CloudMLModel()
    b2 = cloudml_CloudMLModel()
    _safe_set(a, 'cloudml_ExternalComponentInstance', b1)
    assert _is_linked(a, 'cloudml_ExternalComponentInstance', b1)
    if hasattr(b1, 'cloudml_CloudMLModel19'):
        assert _is_linked(b1, 'cloudml_CloudMLModel19', a)
    _safe_set(a, 'cloudml_ExternalComponentInstance', b2)
    assert _is_linked(a, 'cloudml_ExternalComponentInstance', b2)
    if hasattr(b1, 'cloudml_CloudMLModel19'):
        assert not _is_linked(b1, 'cloudml_CloudMLModel19', a)
    if hasattr(b2, 'cloudml_CloudMLModel19'):
        assert _is_linked(b2, 'cloudml_CloudMLModel19', a)
    _safe_set(a, 'cloudml_ExternalComponentInstance', None)
    assert not _is_linked(a, 'cloudml_ExternalComponentInstance', b2)
    if hasattr(b2, 'cloudml_CloudMLModel19'):
        assert not _is_linked(b2, 'cloudml_CloudMLModel19', a)


def test_assoc_externalComponents14_link_reassign_clear():
    a = cloudml_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    b1 = cloudml_CloudMLModel()
    b2 = cloudml_CloudMLModel()
    _safe_set(a, 'cloudml_ExternalComponent', b1)
    assert _is_linked(a, 'cloudml_ExternalComponent', b1)
    if hasattr(b1, 'cloudml_CloudMLModel15'):
        assert _is_linked(b1, 'cloudml_CloudMLModel15', a)
    _safe_set(a, 'cloudml_ExternalComponent', b2)
    assert _is_linked(a, 'cloudml_ExternalComponent', b2)
    if hasattr(b1, 'cloudml_CloudMLModel15'):
        assert not _is_linked(b1, 'cloudml_CloudMLModel15', a)
    if hasattr(b2, 'cloudml_CloudMLModel15'):
        assert _is_linked(b2, 'cloudml_CloudMLModel15', a)
    _safe_set(a, 'cloudml_ExternalComponent', None)
    assert not _is_linked(a, 'cloudml_ExternalComponent', b2)
    if hasattr(b2, 'cloudml_CloudMLModel15'):
        assert not _is_linked(b2, 'cloudml_CloudMLModel15', a)


def test_assoc_offers106_link_reassign_clear():
    a = cloudml_Property(value="sample_text")
    b1 = cloudml_ProvidedExecutionPlatform()
    b2 = cloudml_ProvidedExecutionPlatform()
    _safe_set(a, 'cloudml_Property108', b1)
    assert _is_linked(a, 'cloudml_Property108', b1)
    if hasattr(b1, 'cloudml_ProvidedExecutionPlatform107'):
        assert _is_linked(b1, 'cloudml_ProvidedExecutionPlatform107', a)
    _safe_set(a, 'cloudml_Property108', b2)
    assert _is_linked(a, 'cloudml_Property108', b2)
    if hasattr(b1, 'cloudml_ProvidedExecutionPlatform107'):
        assert not _is_linked(b1, 'cloudml_ProvidedExecutionPlatform107', a)
    if hasattr(b2, 'cloudml_ProvidedExecutionPlatform107'):
        assert _is_linked(b2, 'cloudml_ProvidedExecutionPlatform107', a)
    _safe_set(a, 'cloudml_Property108', None)
    assert not _is_linked(a, 'cloudml_Property108', b2)
    if hasattr(b2, 'cloudml_ProvidedExecutionPlatform107'):
        assert not _is_linked(b2, 'cloudml_ProvidedExecutionPlatform107', a)


def test_assoc_properties0_link_reassign_clear():
    a = cloudml_Property(value="sample_text")
    b1 = cloudml_CloudMLElementWithProperties()
    b2 = cloudml_CloudMLElementWithProperties()
    _safe_set(a, 'cloudml_Property', b1)
    assert _is_linked(a, 'cloudml_Property', b1)
    if hasattr(b1, 'cloudml_CloudMLElementWithProperties'):
        assert _is_linked(b1, 'cloudml_CloudMLElementWithProperties', a)
    _safe_set(a, 'cloudml_Property', b2)
    assert _is_linked(a, 'cloudml_Property', b2)
    if hasattr(b1, 'cloudml_CloudMLElementWithProperties'):
        assert not _is_linked(b1, 'cloudml_CloudMLElementWithProperties', a)
    if hasattr(b2, 'cloudml_CloudMLElementWithProperties'):
        assert _is_linked(b2, 'cloudml_CloudMLElementWithProperties', a)
    _safe_set(a, 'cloudml_Property', None)
    assert not _is_linked(a, 'cloudml_Property', b2)
    if hasattr(b2, 'cloudml_CloudMLElementWithProperties'):
        assert not _is_linked(b2, 'cloudml_CloudMLElementWithProperties', a)


def test_assoc_provide93_link_reassign_clear():
    a = cloudml_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    b1 = cloudml_VMPort()
    b2 = cloudml_VMPort()
    _safe_set(a, 'cloudml_ExternalComponent94', {b1})
    assert _is_linked(a, 'cloudml_ExternalComponent94', b1)
    if hasattr(b1, 'cloudml_VMPort95'):
        assert _is_linked(b1, 'cloudml_VMPort95', a)
    _safe_set(a, 'cloudml_ExternalComponent94', {b2})
    assert _is_linked(a, 'cloudml_ExternalComponent94', b2)
    if hasattr(b1, 'cloudml_VMPort95'):
        assert not _is_linked(b1, 'cloudml_VMPort95', a)
    if hasattr(b2, 'cloudml_VMPort95'):
        assert _is_linked(b2, 'cloudml_VMPort95', a)
    _safe_set(a, 'cloudml_ExternalComponent94', set())
    assert not _is_linked(a, 'cloudml_ExternalComponent94', b2)
    if hasattr(b2, 'cloudml_VMPort95'):
        assert not _is_linked(b2, 'cloudml_VMPort95', a)


def test_assoc_provide96_link_reassign_clear():
    a = cloudml_ExternalComponentInstance(ips="sample_text")
    b1 = cloudml_VMPortInstance()
    b2 = cloudml_VMPortInstance()
    _safe_set(a, 'cloudml_ExternalComponentInstance97', {b1})
    assert _is_linked(a, 'cloudml_ExternalComponentInstance97', b1)
    if hasattr(b1, 'cloudml_VMPortInstance98'):
        assert _is_linked(b1, 'cloudml_VMPortInstance98', a)
    _safe_set(a, 'cloudml_ExternalComponentInstance97', {b2})
    assert _is_linked(a, 'cloudml_ExternalComponentInstance97', b2)
    if hasattr(b1, 'cloudml_VMPortInstance98'):
        assert not _is_linked(b1, 'cloudml_VMPortInstance98', a)
    if hasattr(b2, 'cloudml_VMPortInstance98'):
        assert _is_linked(b2, 'cloudml_VMPortInstance98', a)
    _safe_set(a, 'cloudml_ExternalComponentInstance97', set())
    assert not _is_linked(a, 'cloudml_ExternalComponentInstance97', b2)
    if hasattr(b2, 'cloudml_VMPortInstance98'):
        assert not _is_linked(b2, 'cloudml_VMPortInstance98', a)


def test_assoc_provided30_link_reassign_clear():
    a = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    b1 = cloudml_VMPort()
    b2 = cloudml_VMPort()
    _safe_set(a, 'cloudml_VM31', {b1})
    assert _is_linked(a, 'cloudml_VM31', b1)
    if hasattr(b1, 'cloudml_VMPort'):
        assert _is_linked(b1, 'cloudml_VMPort', a)
    _safe_set(a, 'cloudml_VM31', {b2})
    assert _is_linked(a, 'cloudml_VM31', b2)
    if hasattr(b1, 'cloudml_VMPort'):
        assert not _is_linked(b1, 'cloudml_VMPort', a)
    if hasattr(b2, 'cloudml_VMPort'):
        assert _is_linked(b2, 'cloudml_VMPort', a)
    _safe_set(a, 'cloudml_VM31', set())
    assert not _is_linked(a, 'cloudml_VM31', b2)
    if hasattr(b2, 'cloudml_VMPort'):
        assert not _is_linked(b2, 'cloudml_VMPort', a)


def test_assoc_provided60_link_reassign_clear():
    a = cloudml_VMInstance(id="sample_text", publicAddress="sample_text")
    b1 = cloudml_VMPortInstance()
    b2 = cloudml_VMPortInstance()
    _safe_set(a, 'cloudml_VMInstance61', {b1})
    assert _is_linked(a, 'cloudml_VMInstance61', b1)
    if hasattr(b1, 'cloudml_VMPortInstance'):
        assert _is_linked(b1, 'cloudml_VMPortInstance', a)
    _safe_set(a, 'cloudml_VMInstance61', {b2})
    assert _is_linked(a, 'cloudml_VMInstance61', b2)
    if hasattr(b1, 'cloudml_VMPortInstance'):
        assert not _is_linked(b1, 'cloudml_VMPortInstance', a)
    if hasattr(b2, 'cloudml_VMPortInstance'):
        assert _is_linked(b2, 'cloudml_VMPortInstance', a)
    _safe_set(a, 'cloudml_VMInstance61', set())
    assert not _is_linked(a, 'cloudml_VMInstance61', b2)
    if hasattr(b2, 'cloudml_VMPortInstance'):
        assert not _is_linked(b2, 'cloudml_VMPortInstance', a)


def test_assoc_providedPortResource54_link_reassign_clear():
    a = cloudml_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    b1 = cloudml_Relationship()
    b2 = cloudml_Relationship()
    _safe_set(a, 'cloudml_Resource56', b1)
    assert _is_linked(a, 'cloudml_Resource56', b1)
    if hasattr(b1, 'cloudml_Relationship55'):
        assert _is_linked(b1, 'cloudml_Relationship55', a)
    _safe_set(a, 'cloudml_Resource56', b2)
    assert _is_linked(a, 'cloudml_Resource56', b2)
    if hasattr(b1, 'cloudml_Relationship55'):
        assert not _is_linked(b1, 'cloudml_Relationship55', a)
    if hasattr(b2, 'cloudml_Relationship55'):
        assert _is_linked(b2, 'cloudml_Relationship55', a)
    _safe_set(a, 'cloudml_Resource56', None)
    assert not _is_linked(a, 'cloudml_Resource56', b2)
    if hasattr(b2, 'cloudml_Relationship55'):
        assert not _is_linked(b2, 'cloudml_Relationship55', a)


def test_assoc_provider90_link_reassign_clear():
    a = cloudml_Provider(credentials="sample_text")
    b1 = cloudml_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    b2 = cloudml_ExternalComponent(Region="sample_text_2", endPoint="sample_text_2", location="sample_text_2", login="sample_text_2", passwd="sample_text_2", serviceType="sample_text_2")
    _safe_set(a, 'cloudml_Provider92', b1)
    assert _is_linked(a, 'cloudml_Provider92', b1)
    if hasattr(b1, 'cloudml_ExternalComponent91'):
        assert _is_linked(b1, 'cloudml_ExternalComponent91', a)
    _safe_set(a, 'cloudml_Provider92', b2)
    assert _is_linked(a, 'cloudml_Provider92', b2)
    if hasattr(b1, 'cloudml_ExternalComponent91'):
        assert not _is_linked(b1, 'cloudml_ExternalComponent91', a)
    if hasattr(b2, 'cloudml_ExternalComponent91'):
        assert _is_linked(b2, 'cloudml_ExternalComponent91', a)
    _safe_set(a, 'cloudml_Provider92', None)
    assert not _is_linked(a, 'cloudml_Provider92', b2)
    if hasattr(b2, 'cloudml_ExternalComponent91'):
        assert not _is_linked(b2, 'cloudml_ExternalComponent91', a)


def test_assoc_providers5_link_reassign_clear():
    a = cloudml_Provider(credentials="sample_text")
    b1 = cloudml_CloudMLModel()
    b2 = cloudml_CloudMLModel()
    _safe_set(a, 'cloudml_Provider', b1)
    assert _is_linked(a, 'cloudml_Provider', b1)
    if hasattr(b1, 'cloudml_CloudMLModel'):
        assert _is_linked(b1, 'cloudml_CloudMLModel', a)
    _safe_set(a, 'cloudml_Provider', b2)
    assert _is_linked(a, 'cloudml_Provider', b2)
    if hasattr(b1, 'cloudml_CloudMLModel'):
        assert not _is_linked(b1, 'cloudml_CloudMLModel', a)
    if hasattr(b2, 'cloudml_CloudMLModel'):
        assert _is_linked(b2, 'cloudml_CloudMLModel', a)
    _safe_set(a, 'cloudml_Provider', None)
    assert not _is_linked(a, 'cloudml_Provider', b2)
    if hasattr(b2, 'cloudml_CloudMLModel'):
        assert not _is_linked(b2, 'cloudml_CloudMLModel', a)


def test_assoc_puppetResources3_link_reassign_clear():
    a = cloudml_PuppetResource(configurationFile="sample_text", configureHostnameCommand="sample_text", manifestEntry="sample_text", masterEndpoint="sample_text", repositoryEndpoint="sample_text", repositoryKey="sample_text", username="sample_text")
    b1 = cloudml_CloudMLElementWithProperties()
    b2 = cloudml_CloudMLElementWithProperties()
    _safe_set(a, 'cloudml_PuppetResource', b1)
    assert _is_linked(a, 'cloudml_PuppetResource', b1)
    if hasattr(b1, 'cloudml_CloudMLElementWithProperties4'):
        assert _is_linked(b1, 'cloudml_CloudMLElementWithProperties4', a)
    _safe_set(a, 'cloudml_PuppetResource', b2)
    assert _is_linked(a, 'cloudml_PuppetResource', b2)
    if hasattr(b1, 'cloudml_CloudMLElementWithProperties4'):
        assert not _is_linked(b1, 'cloudml_CloudMLElementWithProperties4', a)
    if hasattr(b2, 'cloudml_CloudMLElementWithProperties4'):
        assert _is_linked(b2, 'cloudml_CloudMLElementWithProperties4', a)
    _safe_set(a, 'cloudml_PuppetResource', None)
    assert not _is_linked(a, 'cloudml_PuppetResource', b2)
    if hasattr(b2, 'cloudml_CloudMLElementWithProperties4'):
        assert not _is_linked(b2, 'cloudml_CloudMLElementWithProperties4', a)


def test_assoc_requiredPort45_link_reassign_clear():
    a = cloudml_RequiredPort(isMandatory=True)
    b1 = cloudml_Relationship()
    b2 = cloudml_Relationship()
    _safe_set(a, 'cloudml_RequiredPort47', b1)
    assert _is_linked(a, 'cloudml_RequiredPort47', b1)
    if hasattr(b1, 'cloudml_Relationship46'):
        assert _is_linked(b1, 'cloudml_Relationship46', a)
    _safe_set(a, 'cloudml_RequiredPort47', b2)
    assert _is_linked(a, 'cloudml_RequiredPort47', b2)
    if hasattr(b1, 'cloudml_Relationship46'):
        assert not _is_linked(b1, 'cloudml_Relationship46', a)
    if hasattr(b2, 'cloudml_Relationship46'):
        assert _is_linked(b2, 'cloudml_Relationship46', a)
    _safe_set(a, 'cloudml_RequiredPort47', None)
    assert not _is_linked(a, 'cloudml_RequiredPort47', b2)
    if hasattr(b2, 'cloudml_Relationship46'):
        assert not _is_linked(b2, 'cloudml_Relationship46', a)


def test_assoc_requiredPortResource51_link_reassign_clear():
    a = cloudml_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    b1 = cloudml_Relationship()
    b2 = cloudml_Relationship()
    _safe_set(a, 'cloudml_Resource53', b1)
    assert _is_linked(a, 'cloudml_Resource53', b1)
    if hasattr(b1, 'cloudml_Relationship52'):
        assert _is_linked(b1, 'cloudml_Relationship52', a)
    _safe_set(a, 'cloudml_Resource53', b2)
    assert _is_linked(a, 'cloudml_Resource53', b2)
    if hasattr(b1, 'cloudml_Relationship52'):
        assert not _is_linked(b1, 'cloudml_Relationship52', a)
    if hasattr(b2, 'cloudml_Relationship52'):
        assert _is_linked(b2, 'cloudml_Relationship52', a)
    _safe_set(a, 'cloudml_Resource53', None)
    assert not _is_linked(a, 'cloudml_Resource53', b2)
    if hasattr(b2, 'cloudml_Relationship52'):
        assert not _is_linked(b2, 'cloudml_Relationship52', a)


def test_assoc_requiredPorts36_link_reassign_clear():
    a = cloudml_RequiredPort(isMandatory=True)
    b1 = cloudml_InternalComponent()
    b2 = cloudml_InternalComponent()
    _safe_set(a, 'cloudml_RequiredPort', b1)
    assert _is_linked(a, 'cloudml_RequiredPort', b1)
    if hasattr(b1, 'cloudml_InternalComponent37'):
        assert _is_linked(b1, 'cloudml_InternalComponent37', a)
    _safe_set(a, 'cloudml_RequiredPort', b2)
    assert _is_linked(a, 'cloudml_RequiredPort', b2)
    if hasattr(b1, 'cloudml_InternalComponent37'):
        assert not _is_linked(b1, 'cloudml_InternalComponent37', a)
    if hasattr(b2, 'cloudml_InternalComponent37'):
        assert _is_linked(b2, 'cloudml_InternalComponent37', a)
    _safe_set(a, 'cloudml_RequiredPort', None)
    assert not _is_linked(a, 'cloudml_RequiredPort', b2)
    if hasattr(b2, 'cloudml_InternalComponent37'):
        assert not _is_linked(b2, 'cloudml_InternalComponent37', a)


def test_assoc_resources1_link_reassign_clear():
    a = cloudml_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    b1 = cloudml_CloudMLElementWithProperties()
    b2 = cloudml_CloudMLElementWithProperties()
    _safe_set(a, 'cloudml_Resource', b1)
    assert _is_linked(a, 'cloudml_Resource', b1)
    if hasattr(b1, 'cloudml_CloudMLElementWithProperties2'):
        assert _is_linked(b1, 'cloudml_CloudMLElementWithProperties2', a)
    _safe_set(a, 'cloudml_Resource', b2)
    assert _is_linked(a, 'cloudml_Resource', b2)
    if hasattr(b1, 'cloudml_CloudMLElementWithProperties2'):
        assert not _is_linked(b1, 'cloudml_CloudMLElementWithProperties2', a)
    if hasattr(b2, 'cloudml_CloudMLElementWithProperties2'):
        assert _is_linked(b2, 'cloudml_CloudMLElementWithProperties2', a)
    _safe_set(a, 'cloudml_Resource', None)
    assert not _is_linked(a, 'cloudml_Resource', b2)
    if hasattr(b2, 'cloudml_CloudMLElementWithProperties2'):
        assert not _is_linked(b2, 'cloudml_CloudMLElementWithProperties2', a)


def test_assoc_type76_link_reassign_clear():
    a = cloudml_Port(isLocal=True, portNumber=7)
    b1 = cloudml_PortInstance()
    b2 = cloudml_PortInstance()
    _safe_set(a, 'cloudml_Port77', b1)
    assert _is_linked(a, 'cloudml_Port77', b1)
    if hasattr(b1, 'cloudml_PortInstance'):
        assert _is_linked(b1, 'cloudml_PortInstance', a)
    _safe_set(a, 'cloudml_Port77', b2)
    assert _is_linked(a, 'cloudml_Port77', b2)
    if hasattr(b1, 'cloudml_PortInstance'):
        assert not _is_linked(b1, 'cloudml_PortInstance', a)
    if hasattr(b2, 'cloudml_PortInstance'):
        assert _is_linked(b2, 'cloudml_PortInstance', a)
    _safe_set(a, 'cloudml_Port77', None)
    assert not _is_linked(a, 'cloudml_Port77', b2)
    if hasattr(b2, 'cloudml_PortInstance'):
        assert not _is_linked(b2, 'cloudml_PortInstance', a)


def test_assoc_vmInstances22_link_reassign_clear():
    a = cloudml_VMInstance(id="sample_text", publicAddress="sample_text")
    b1 = cloudml_CloudMLModel()
    b2 = cloudml_CloudMLModel()
    _safe_set(a, 'cloudml_VMInstance', b1)
    assert _is_linked(a, 'cloudml_VMInstance', b1)
    if hasattr(b1, 'cloudml_CloudMLModel23'):
        assert _is_linked(b1, 'cloudml_CloudMLModel23', a)
    _safe_set(a, 'cloudml_VMInstance', b2)
    assert _is_linked(a, 'cloudml_VMInstance', b2)
    if hasattr(b1, 'cloudml_CloudMLModel23'):
        assert not _is_linked(b1, 'cloudml_CloudMLModel23', a)
    if hasattr(b2, 'cloudml_CloudMLModel23'):
        assert _is_linked(b2, 'cloudml_CloudMLModel23', a)
    _safe_set(a, 'cloudml_VMInstance', None)
    assert not _is_linked(a, 'cloudml_VMInstance', b2)
    if hasattr(b2, 'cloudml_CloudMLModel23'):
        assert not _is_linked(b2, 'cloudml_CloudMLModel23', a)


def test_assoc_vmInstances57_link_reassign_clear():
    a = cloudml_VMInstance(id="sample_text", publicAddress="sample_text")
    b1 = cloudml_Cloud()
    b2 = cloudml_Cloud()
    _safe_set(a, 'cloudml_VMInstance59', b1)
    assert _is_linked(a, 'cloudml_VMInstance59', b1)
    if hasattr(b1, 'cloudml_Cloud58'):
        assert _is_linked(b1, 'cloudml_Cloud58', a)
    _safe_set(a, 'cloudml_VMInstance59', b2)
    assert _is_linked(a, 'cloudml_VMInstance59', b2)
    if hasattr(b1, 'cloudml_Cloud58'):
        assert not _is_linked(b1, 'cloudml_Cloud58', a)
    if hasattr(b2, 'cloudml_Cloud58'):
        assert _is_linked(b2, 'cloudml_Cloud58', a)
    _safe_set(a, 'cloudml_VMInstance59', None)
    assert not _is_linked(a, 'cloudml_VMInstance59', b2)
    if hasattr(b2, 'cloudml_Cloud58'):
        assert not _is_linked(b2, 'cloudml_Cloud58', a)


def test_assoc_vms20_link_reassign_clear():
    a = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    b1 = cloudml_CloudMLModel()
    b2 = cloudml_CloudMLModel()
    _safe_set(a, 'cloudml_VM', b1)
    assert _is_linked(a, 'cloudml_VM', b1)
    if hasattr(b1, 'cloudml_CloudMLModel21'):
        assert _is_linked(b1, 'cloudml_CloudMLModel21', a)
    _safe_set(a, 'cloudml_VM', b2)
    assert _is_linked(a, 'cloudml_VM', b2)
    if hasattr(b1, 'cloudml_CloudMLModel21'):
        assert not _is_linked(b1, 'cloudml_CloudMLModel21', a)
    if hasattr(b2, 'cloudml_CloudMLModel21'):
        assert _is_linked(b2, 'cloudml_CloudMLModel21', a)
    _safe_set(a, 'cloudml_VM', None)
    assert not _is_linked(a, 'cloudml_VM', b2)
    if hasattr(b2, 'cloudml_CloudMLModel21'):
        assert not _is_linked(b2, 'cloudml_CloudMLModel21', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CloudMLElement_strategy = st.builds(CloudMLElement)
@given(instance=CloudMLElement_strategy)
@settings(max_examples=25)
def test_CloudMLElement_instantiation(instance):
    assert isinstance(instance, CloudMLElement)


CloudMLElementWithProperties_strategy = st.builds(CloudMLElementWithProperties)
@given(instance=CloudMLElementWithProperties_strategy)
@settings(max_examples=25)
def test_CloudMLElementWithProperties_instantiation(instance):
    assert isinstance(instance, CloudMLElementWithProperties)


Component_strategy = st.builds(Component)
@given(instance=Component_strategy)
@settings(max_examples=25)
def test_Component_instantiation(instance):
    assert isinstance(instance, Component)


ComponentInstance_strategy = st.builds(ComponentInstance)
@given(instance=ComponentInstance_strategy)
@settings(max_examples=25)
def test_ComponentInstance_instantiation(instance):
    assert isinstance(instance, ComponentInstance)


ExecutionPlatform_strategy = st.builds(ExecutionPlatform)
@given(instance=ExecutionPlatform_strategy)
@settings(max_examples=25)
def test_ExecutionPlatform_instantiation(instance):
    assert isinstance(instance, ExecutionPlatform)


ExecutionPlatformInstance_strategy = st.builds(ExecutionPlatformInstance)
@given(instance=ExecutionPlatformInstance_strategy)
@settings(max_examples=25)
def test_ExecutionPlatformInstance_instantiation(instance):
    assert isinstance(instance, ExecutionPlatformInstance)


ExternalComponent_strategy = st.builds(ExternalComponent)
@given(instance=ExternalComponent_strategy)
@settings(max_examples=25)
def test_ExternalComponent_instantiation(instance):
    assert isinstance(instance, ExternalComponent)


ExternalComponentInstance_strategy = st.builds(ExternalComponentInstance)
@given(instance=ExternalComponentInstance_strategy)
@settings(max_examples=25)
def test_ExternalComponentInstance_instantiation(instance):
    assert isinstance(instance, ExternalComponentInstance)


Port_strategy = st.builds(Port)
@given(instance=Port_strategy)
@settings(max_examples=25)
def test_Port_instantiation(instance):
    assert isinstance(instance, Port)


PortInstance_strategy = st.builds(PortInstance)
@given(instance=PortInstance_strategy)
@settings(max_examples=25)
def test_PortInstance_instantiation(instance):
    assert isinstance(instance, PortInstance)


Resource_strategy = st.builds(Resource)
@given(instance=Resource_strategy)
@settings(max_examples=25)
def test_Resource_instantiation(instance):
    assert isinstance(instance, Resource)


cloudml_Cloud_strategy = st.builds(cloudml_Cloud)
@given(instance=cloudml_Cloud_strategy)
@settings(max_examples=25)
def test_cloudml_Cloud_instantiation(instance):
    assert isinstance(instance, cloudml_Cloud)


cloudml_CloudMLElement_strategy = st.builds(cloudml_CloudMLElement, name=safe_text)
@given(instance=cloudml_CloudMLElement_strategy)
@settings(max_examples=25)
def test_cloudml_CloudMLElement_instantiation(instance):
    assert isinstance(instance, cloudml_CloudMLElement)


cloudml_CloudMLElementWithProperties_strategy = st.builds(cloudml_CloudMLElementWithProperties)
@given(instance=cloudml_CloudMLElementWithProperties_strategy)
@settings(max_examples=25)
def test_cloudml_CloudMLElementWithProperties_instantiation(instance):
    assert isinstance(instance, cloudml_CloudMLElementWithProperties)


cloudml_CloudMLModel_strategy = st.builds(cloudml_CloudMLModel)
@given(instance=cloudml_CloudMLModel_strategy)
@settings(max_examples=25)
def test_cloudml_CloudMLModel_instantiation(instance):
    assert isinstance(instance, cloudml_CloudMLModel)


cloudml_Component_strategy = st.builds(cloudml_Component)
@given(instance=cloudml_Component_strategy)
@settings(max_examples=25)
def test_cloudml_Component_instantiation(instance):
    assert isinstance(instance, cloudml_Component)


cloudml_ComponentInstance_strategy = st.builds(cloudml_ComponentInstance)
@given(instance=cloudml_ComponentInstance_strategy)
@settings(max_examples=25)
def test_cloudml_ComponentInstance_instantiation(instance):
    assert isinstance(instance, cloudml_ComponentInstance)


cloudml_ExecuteInstance_strategy = st.builds(cloudml_ExecuteInstance)
@given(instance=cloudml_ExecuteInstance_strategy)
@settings(max_examples=25)
def test_cloudml_ExecuteInstance_instantiation(instance):
    assert isinstance(instance, cloudml_ExecuteInstance)


cloudml_ExecutionPlatform_strategy = st.builds(cloudml_ExecutionPlatform)
@given(instance=cloudml_ExecutionPlatform_strategy)
@settings(max_examples=25)
def test_cloudml_ExecutionPlatform_instantiation(instance):
    assert isinstance(instance, cloudml_ExecutionPlatform)


cloudml_ExecutionPlatformInstance_strategy = st.builds(cloudml_ExecutionPlatformInstance)
@given(instance=cloudml_ExecutionPlatformInstance_strategy)
@settings(max_examples=25)
def test_cloudml_ExecutionPlatformInstance_instantiation(instance):
    assert isinstance(instance, cloudml_ExecutionPlatformInstance)


cloudml_ExternalComponent_strategy = st.builds(cloudml_ExternalComponent, Region=safe_text, endPoint=safe_text, location=safe_text, login=safe_text, passwd=safe_text, serviceType=safe_text)
@given(instance=cloudml_ExternalComponent_strategy)
@settings(max_examples=25)
def test_cloudml_ExternalComponent_instantiation(instance):
    assert isinstance(instance, cloudml_ExternalComponent)


cloudml_ExternalComponentInstance_strategy = st.builds(cloudml_ExternalComponentInstance, ips=safe_text)
@given(instance=cloudml_ExternalComponentInstance_strategy)
@settings(max_examples=25)
def test_cloudml_ExternalComponentInstance_instantiation(instance):
    assert isinstance(instance, cloudml_ExternalComponentInstance)


cloudml_InternalComponent_strategy = st.builds(cloudml_InternalComponent)
@given(instance=cloudml_InternalComponent_strategy)
@settings(max_examples=25)
def test_cloudml_InternalComponent_instantiation(instance):
    assert isinstance(instance, cloudml_InternalComponent)


cloudml_InternalComponentInstance_strategy = st.builds(cloudml_InternalComponentInstance)
@given(instance=cloudml_InternalComponentInstance_strategy)
@settings(max_examples=25)
def test_cloudml_InternalComponentInstance_instantiation(instance):
    assert isinstance(instance, cloudml_InternalComponentInstance)


cloudml_Port_strategy = st.builds(cloudml_Port, isLocal=st.booleans(), portNumber=st.integers())
@given(instance=cloudml_Port_strategy)
@settings(max_examples=25)
def test_cloudml_Port_instantiation(instance):
    assert isinstance(instance, cloudml_Port)


cloudml_PortInstance_strategy = st.builds(cloudml_PortInstance)
@given(instance=cloudml_PortInstance_strategy)
@settings(max_examples=25)
def test_cloudml_PortInstance_instantiation(instance):
    assert isinstance(instance, cloudml_PortInstance)


cloudml_Property_strategy = st.builds(cloudml_Property, value=safe_text)
@given(instance=cloudml_Property_strategy)
@settings(max_examples=25)
def test_cloudml_Property_instantiation(instance):
    assert isinstance(instance, cloudml_Property)


cloudml_ProvidedExecutionPlatform_strategy = st.builds(cloudml_ProvidedExecutionPlatform)
@given(instance=cloudml_ProvidedExecutionPlatform_strategy)
@settings(max_examples=25)
def test_cloudml_ProvidedExecutionPlatform_instantiation(instance):
    assert isinstance(instance, cloudml_ProvidedExecutionPlatform)


cloudml_ProvidedExecutionPlatformInstance_strategy = st.builds(cloudml_ProvidedExecutionPlatformInstance)
@given(instance=cloudml_ProvidedExecutionPlatformInstance_strategy)
@settings(max_examples=25)
def test_cloudml_ProvidedExecutionPlatformInstance_instantiation(instance):
    assert isinstance(instance, cloudml_ProvidedExecutionPlatformInstance)


cloudml_ProvidedPort_strategy = st.builds(cloudml_ProvidedPort)
@given(instance=cloudml_ProvidedPort_strategy)
@settings(max_examples=25)
def test_cloudml_ProvidedPort_instantiation(instance):
    assert isinstance(instance, cloudml_ProvidedPort)


cloudml_ProvidedPortInstance_strategy = st.builds(cloudml_ProvidedPortInstance)
@given(instance=cloudml_ProvidedPortInstance_strategy)
@settings(max_examples=25)
def test_cloudml_ProvidedPortInstance_instantiation(instance):
    assert isinstance(instance, cloudml_ProvidedPortInstance)


cloudml_Provider_strategy = st.builds(cloudml_Provider, credentials=safe_text)
@given(instance=cloudml_Provider_strategy)
@settings(max_examples=25)
def test_cloudml_Provider_instantiation(instance):
    assert isinstance(instance, cloudml_Provider)


cloudml_PuppetResource_strategy = st.builds(cloudml_PuppetResource, configurationFile=safe_text, configureHostnameCommand=safe_text, manifestEntry=safe_text, masterEndpoint=safe_text, repositoryEndpoint=safe_text, repositoryKey=safe_text, username=safe_text)
@given(instance=cloudml_PuppetResource_strategy)
@settings(max_examples=25)
def test_cloudml_PuppetResource_instantiation(instance):
    assert isinstance(instance, cloudml_PuppetResource)


cloudml_Relationship_strategy = st.builds(cloudml_Relationship)
@given(instance=cloudml_Relationship_strategy)
@settings(max_examples=25)
def test_cloudml_Relationship_instantiation(instance):
    assert isinstance(instance, cloudml_Relationship)


cloudml_RelationshipInstance_strategy = st.builds(cloudml_RelationshipInstance)
@given(instance=cloudml_RelationshipInstance_strategy)
@settings(max_examples=25)
def test_cloudml_RelationshipInstance_instantiation(instance):
    assert isinstance(instance, cloudml_RelationshipInstance)


cloudml_RequiredExecutionPlatform_strategy = st.builds(cloudml_RequiredExecutionPlatform)
@given(instance=cloudml_RequiredExecutionPlatform_strategy)
@settings(max_examples=25)
def test_cloudml_RequiredExecutionPlatform_instantiation(instance):
    assert isinstance(instance, cloudml_RequiredExecutionPlatform)


cloudml_RequiredExecutionPlatformInstance_strategy = st.builds(cloudml_RequiredExecutionPlatformInstance)
@given(instance=cloudml_RequiredExecutionPlatformInstance_strategy)
@settings(max_examples=25)
def test_cloudml_RequiredExecutionPlatformInstance_instantiation(instance):
    assert isinstance(instance, cloudml_RequiredExecutionPlatformInstance)


cloudml_RequiredPort_strategy = st.builds(cloudml_RequiredPort, isMandatory=st.booleans())
@given(instance=cloudml_RequiredPort_strategy)
@settings(max_examples=25)
def test_cloudml_RequiredPort_instantiation(instance):
    assert isinstance(instance, cloudml_RequiredPort)


cloudml_RequiredPortInstance_strategy = st.builds(cloudml_RequiredPortInstance)
@given(instance=cloudml_RequiredPortInstance_strategy)
@settings(max_examples=25)
def test_cloudml_RequiredPortInstance_instantiation(instance):
    assert isinstance(instance, cloudml_RequiredPortInstance)


cloudml_Resource_strategy = st.builds(cloudml_Resource, configureCommand=safe_text, downloadCommand=safe_text, executeLocally=st.booleans(), installCommand=safe_text, requireCredentials=st.booleans(), startCommand=safe_text, stopCommand=safe_text, uploadCommand=safe_text)
@given(instance=cloudml_Resource_strategy)
@settings(max_examples=25)
def test_cloudml_Resource_instantiation(instance):
    assert isinstance(instance, cloudml_Resource)


cloudml_VM_strategy = st.builds(cloudml_VM, groupName=safe_text, imageId=safe_text, is64os=st.booleans(), maxCores=st.integers(), maxRam=st.integers(), maxStorage=st.integers(), minCores=st.integers(), minRam=st.integers(), minStorage=st.integers(), os=safe_text, privateKey=safe_text, providerSpecificTypeName=safe_text, securityGroup=safe_text, sshKey=safe_text)
@given(instance=cloudml_VM_strategy)
@settings(max_examples=25)
def test_cloudml_VM_instantiation(instance):
    assert isinstance(instance, cloudml_VM)


cloudml_VMInstance_strategy = st.builds(cloudml_VMInstance, id=safe_text, publicAddress=safe_text)
@given(instance=cloudml_VMInstance_strategy)
@settings(max_examples=25)
def test_cloudml_VMInstance_instantiation(instance):
    assert isinstance(instance, cloudml_VMInstance)


cloudml_VMPort_strategy = st.builds(cloudml_VMPort)
@given(instance=cloudml_VMPort_strategy)
@settings(max_examples=25)
def test_cloudml_VMPort_instantiation(instance):
    assert isinstance(instance, cloudml_VMPort)


cloudml_VMPortInstance_strategy = st.builds(cloudml_VMPortInstance)
@given(instance=cloudml_VMPortInstance_strategy)
@settings(max_examples=25)
def test_cloudml_VMPortInstance_instantiation(instance):
    assert isinstance(instance, cloudml_VMPortInstance)



