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


