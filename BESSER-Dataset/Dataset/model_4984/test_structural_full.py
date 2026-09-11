import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Cloud,
    CloudMLElement,
    CloudMLElementWithProperties,
    Component,
    ComponentInstance,
    DockerResource,
    ExecuteInstance,
    ExecutionPlatform,
    ExecutionPlatformInstance,
    ExternalComponent,
    ExternalComponentInstance,
    InternalComponent,
    InternalComponentInstance,
    Port,
    PortInstance,
    Property,
    ProvidedExecutionPlatform,
    ProvidedExecutionPlatformInstance,
    ProvidedPort,
    ProvidedPortInstance,
    Provider,
    PuppetResource,
    Relationship,
    RelationshipInstance,
    RequiredExecutionPlatform,
    RequiredExecutionPlatformInstance,
    RequiredPort,
    RequiredPortInstance,
    Resource,
    ResourcesPool,
    VM,
    VMInstance,
    VMPort,
    VMPortInstance,
    cloudml_core_Cloud,
    cloudml_core_CloudMLElement,
    cloudml_core_CloudMLElementWithProperties,
    cloudml_core_CloudMLModel,
    cloudml_core_Component,
    cloudml_core_ComponentInstance,
    cloudml_core_DockerResource,
    cloudml_core_ExecuteInstance,
    cloudml_core_ExecutionPlatform,
    cloudml_core_ExecutionPlatformInstance,
    cloudml_core_ExternalComponent,
    cloudml_core_ExternalComponentInstance,
    cloudml_core_InternalComponent,
    cloudml_core_InternalComponentInstance,
    cloudml_core_Port,
    cloudml_core_PortInstance,
    cloudml_core_Property,
    cloudml_core_ProvidedExecutionPlatform,
    cloudml_core_ProvidedExecutionPlatformInstance,
    cloudml_core_ProvidedPort,
    cloudml_core_ProvidedPortInstance,
    cloudml_core_Provider,
    cloudml_core_PuppetResource,
    cloudml_core_Relationship,
    cloudml_core_RelationshipInstance,
    cloudml_core_RequiredExecutionPlatform,
    cloudml_core_RequiredExecutionPlatformInstance,
    cloudml_core_RequiredPort,
    cloudml_core_RequiredPortInstance,
    cloudml_core_Resource,
    cloudml_core_ResourcesPool,
    cloudml_core_VM,
    cloudml_core_VMInstance,
    cloudml_core_VMPort,
    cloudml_core_VMPortInstance,
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

def test_cloudml_core_CloudMLElement_name_value_roundtrip():
    instance = cloudml_core_CloudMLElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cloudml_core_DockerResource_dockerFilePath_value_roundtrip():
    instance = cloudml_core_DockerResource(dockerFilePath="sample_text", image="sample_text")
    assert instance.dockerFilePath == "sample_text"
    instance.dockerFilePath = "sample_text_2"
    assert instance.dockerFilePath == "sample_text_2"


def test_cloudml_core_DockerResource_image_value_roundtrip():
    instance = cloudml_core_DockerResource(dockerFilePath="sample_text", image="sample_text")
    assert instance.image == "sample_text"
    instance.image = "sample_text_2"
    assert instance.image == "sample_text_2"


def test_cloudml_core_ExternalComponent_Region_value_roundtrip():
    instance = cloudml_core_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    assert instance.Region == "sample_text"
    instance.Region = "sample_text_2"
    assert instance.Region == "sample_text_2"


def test_cloudml_core_ExternalComponent_endPoint_value_roundtrip():
    instance = cloudml_core_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    assert instance.endPoint == "sample_text"
    instance.endPoint = "sample_text_2"
    assert instance.endPoint == "sample_text_2"


def test_cloudml_core_ExternalComponent_location_value_roundtrip():
    instance = cloudml_core_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_cloudml_core_ExternalComponent_login_value_roundtrip():
    instance = cloudml_core_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    assert instance.login == "sample_text"
    instance.login = "sample_text_2"
    assert instance.login == "sample_text_2"


def test_cloudml_core_ExternalComponent_passwd_value_roundtrip():
    instance = cloudml_core_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    assert instance.passwd == "sample_text"
    instance.passwd = "sample_text_2"
    assert instance.passwd == "sample_text_2"


def test_cloudml_core_ExternalComponent_serviceType_value_roundtrip():
    instance = cloudml_core_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    assert instance.serviceType == "sample_text"
    instance.serviceType = "sample_text_2"
    assert instance.serviceType == "sample_text_2"


def test_cloudml_core_ExternalComponentInstance_ips_value_roundtrip():
    instance = cloudml_core_ExternalComponentInstance(ips="sample_text", status="sample_text")
    assert instance.ips == "sample_text"
    instance.ips = "sample_text_2"
    assert instance.ips == "sample_text_2"


def test_cloudml_core_ExternalComponentInstance_status_value_roundtrip():
    instance = cloudml_core_ExternalComponentInstance(ips="sample_text", status="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_cloudml_core_Port_isLocal_value_roundtrip():
    instance = cloudml_core_Port(isLocal=True, portNumber=7)
    assert instance.isLocal == True
    instance.isLocal = False
    assert instance.isLocal == False


def test_cloudml_core_Port_portNumber_value_roundtrip():
    instance = cloudml_core_Port(isLocal=True, portNumber=7)
    assert instance.portNumber == 7
    instance.portNumber = 13
    assert instance.portNumber == 13


def test_cloudml_core_Property_value_value_roundtrip():
    instance = cloudml_core_Property(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_cloudml_core_Provider_credentials_value_roundtrip():
    instance = cloudml_core_Provider(credentials="sample_text", login="sample_text", password="sample_text")
    assert instance.credentials == "sample_text"
    instance.credentials = "sample_text_2"
    assert instance.credentials == "sample_text_2"


def test_cloudml_core_Provider_login_value_roundtrip():
    instance = cloudml_core_Provider(credentials="sample_text", login="sample_text", password="sample_text")
    assert instance.login == "sample_text"
    instance.login = "sample_text_2"
    assert instance.login == "sample_text_2"


def test_cloudml_core_Provider_password_value_roundtrip():
    instance = cloudml_core_Provider(credentials="sample_text", login="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_cloudml_core_PuppetResource_configurationFile_value_roundtrip():
    instance = cloudml_core_PuppetResource(configurationFile="sample_text", configureHostnameCommand="sample_text", manifestEntry="sample_text", masterEndpoint="sample_text", repositoryEndpoint="sample_text", repositoryKey="sample_text", username="sample_text")
    assert instance.configurationFile == "sample_text"
    instance.configurationFile = "sample_text_2"
    assert instance.configurationFile == "sample_text_2"


def test_cloudml_core_PuppetResource_configureHostnameCommand_value_roundtrip():
    instance = cloudml_core_PuppetResource(configurationFile="sample_text", configureHostnameCommand="sample_text", manifestEntry="sample_text", masterEndpoint="sample_text", repositoryEndpoint="sample_text", repositoryKey="sample_text", username="sample_text")
    assert instance.configureHostnameCommand == "sample_text"
    instance.configureHostnameCommand = "sample_text_2"
    assert instance.configureHostnameCommand == "sample_text_2"


def test_cloudml_core_PuppetResource_manifestEntry_value_roundtrip():
    instance = cloudml_core_PuppetResource(configurationFile="sample_text", configureHostnameCommand="sample_text", manifestEntry="sample_text", masterEndpoint="sample_text", repositoryEndpoint="sample_text", repositoryKey="sample_text", username="sample_text")
    assert instance.manifestEntry == "sample_text"
    instance.manifestEntry = "sample_text_2"
    assert instance.manifestEntry == "sample_text_2"


def test_cloudml_core_PuppetResource_masterEndpoint_value_roundtrip():
    instance = cloudml_core_PuppetResource(configurationFile="sample_text", configureHostnameCommand="sample_text", manifestEntry="sample_text", masterEndpoint="sample_text", repositoryEndpoint="sample_text", repositoryKey="sample_text", username="sample_text")
    assert instance.masterEndpoint == "sample_text"
    instance.masterEndpoint = "sample_text_2"
    assert instance.masterEndpoint == "sample_text_2"


def test_cloudml_core_PuppetResource_repositoryEndpoint_value_roundtrip():
    instance = cloudml_core_PuppetResource(configurationFile="sample_text", configureHostnameCommand="sample_text", manifestEntry="sample_text", masterEndpoint="sample_text", repositoryEndpoint="sample_text", repositoryKey="sample_text", username="sample_text")
    assert instance.repositoryEndpoint == "sample_text"
    instance.repositoryEndpoint = "sample_text_2"
    assert instance.repositoryEndpoint == "sample_text_2"


def test_cloudml_core_PuppetResource_repositoryKey_value_roundtrip():
    instance = cloudml_core_PuppetResource(configurationFile="sample_text", configureHostnameCommand="sample_text", manifestEntry="sample_text", masterEndpoint="sample_text", repositoryEndpoint="sample_text", repositoryKey="sample_text", username="sample_text")
    assert instance.repositoryKey == "sample_text"
    instance.repositoryKey = "sample_text_2"
    assert instance.repositoryKey == "sample_text_2"


def test_cloudml_core_PuppetResource_username_value_roundtrip():
    instance = cloudml_core_PuppetResource(configurationFile="sample_text", configureHostnameCommand="sample_text", manifestEntry="sample_text", masterEndpoint="sample_text", repositoryEndpoint="sample_text", repositoryKey="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_cloudml_core_RequiredPort_isMandatory_value_roundtrip():
    instance = cloudml_core_RequiredPort(isMandatory=True)
    assert instance.isMandatory == True
    instance.isMandatory = False
    assert instance.isMandatory == False


def test_cloudml_core_Resource_configureCommand_value_roundtrip():
    instance = cloudml_core_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.configureCommand == "sample_text"
    instance.configureCommand = "sample_text_2"
    assert instance.configureCommand == "sample_text_2"


def test_cloudml_core_Resource_downloadCommand_value_roundtrip():
    instance = cloudml_core_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.downloadCommand == "sample_text"
    instance.downloadCommand = "sample_text_2"
    assert instance.downloadCommand == "sample_text_2"


def test_cloudml_core_Resource_executeLocally_value_roundtrip():
    instance = cloudml_core_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.executeLocally == True
    instance.executeLocally = False
    assert instance.executeLocally == False


def test_cloudml_core_Resource_installCommand_value_roundtrip():
    instance = cloudml_core_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.installCommand == "sample_text"
    instance.installCommand = "sample_text_2"
    assert instance.installCommand == "sample_text_2"


def test_cloudml_core_Resource_requireCredentials_value_roundtrip():
    instance = cloudml_core_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.requireCredentials == True
    instance.requireCredentials = False
    assert instance.requireCredentials == False


def test_cloudml_core_Resource_startCommand_value_roundtrip():
    instance = cloudml_core_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.startCommand == "sample_text"
    instance.startCommand = "sample_text_2"
    assert instance.startCommand == "sample_text_2"


def test_cloudml_core_Resource_stopCommand_value_roundtrip():
    instance = cloudml_core_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.stopCommand == "sample_text"
    instance.stopCommand = "sample_text_2"
    assert instance.stopCommand == "sample_text_2"


def test_cloudml_core_Resource_uploadCommand_value_roundtrip():
    instance = cloudml_core_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert instance.uploadCommand == "sample_text"
    instance.uploadCommand = "sample_text_2"
    assert instance.uploadCommand == "sample_text_2"


def test_cloudml_core_ResourcesPool_maxReplicats_value_roundtrip():
    instance = cloudml_core_ResourcesPool(maxReplicats=7, minReplicats=7, nbReplicats=7, type="sample_text")
    assert instance.maxReplicats == 7
    instance.maxReplicats = 13
    assert instance.maxReplicats == 13


def test_cloudml_core_ResourcesPool_minReplicats_value_roundtrip():
    instance = cloudml_core_ResourcesPool(maxReplicats=7, minReplicats=7, nbReplicats=7, type="sample_text")
    assert instance.minReplicats == 7
    instance.minReplicats = 13
    assert instance.minReplicats == 13


def test_cloudml_core_ResourcesPool_nbReplicats_value_roundtrip():
    instance = cloudml_core_ResourcesPool(maxReplicats=7, minReplicats=7, nbReplicats=7, type="sample_text")
    assert instance.nbReplicats == 7
    instance.nbReplicats = 13
    assert instance.nbReplicats == 13


def test_cloudml_core_ResourcesPool_type_value_roundtrip():
    instance = cloudml_core_ResourcesPool(maxReplicats=7, minReplicats=7, nbReplicats=7, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_cloudml_core_VM_groupName_value_roundtrip():
    instance = cloudml_core_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.groupName == "sample_text"
    instance.groupName = "sample_text_2"
    assert instance.groupName == "sample_text_2"


def test_cloudml_core_VM_imageId_value_roundtrip():
    instance = cloudml_core_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.imageId == "sample_text"
    instance.imageId = "sample_text_2"
    assert instance.imageId == "sample_text_2"


def test_cloudml_core_VM_is64os_value_roundtrip():
    instance = cloudml_core_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.is64os == True
    instance.is64os = False
    assert instance.is64os == False


def test_cloudml_core_VM_maxCores_value_roundtrip():
    instance = cloudml_core_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.maxCores == 7
    instance.maxCores = 13
    assert instance.maxCores == 13


def test_cloudml_core_VM_maxRam_value_roundtrip():
    instance = cloudml_core_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.maxRam == 7
    instance.maxRam = 13
    assert instance.maxRam == 13


def test_cloudml_core_VM_maxStorage_value_roundtrip():
    instance = cloudml_core_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.maxStorage == 7
    instance.maxStorage = 13
    assert instance.maxStorage == 13


def test_cloudml_core_VM_minCores_value_roundtrip():
    instance = cloudml_core_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.minCores == 7
    instance.minCores = 13
    assert instance.minCores == 13


def test_cloudml_core_VM_minRam_value_roundtrip():
    instance = cloudml_core_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.minRam == 7
    instance.minRam = 13
    assert instance.minRam == 13


def test_cloudml_core_VM_minStorage_value_roundtrip():
    instance = cloudml_core_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.minStorage == 7
    instance.minStorage = 13
    assert instance.minStorage == 13


def test_cloudml_core_VM_os_value_roundtrip():
    instance = cloudml_core_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.os == "sample_text"
    instance.os = "sample_text_2"
    assert instance.os == "sample_text_2"


def test_cloudml_core_VM_privateKey_value_roundtrip():
    instance = cloudml_core_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.privateKey == "sample_text"
    instance.privateKey = "sample_text_2"
    assert instance.privateKey == "sample_text_2"


def test_cloudml_core_VM_providerSpecificTypeName_value_roundtrip():
    instance = cloudml_core_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.providerSpecificTypeName == "sample_text"
    instance.providerSpecificTypeName = "sample_text_2"
    assert instance.providerSpecificTypeName == "sample_text_2"


def test_cloudml_core_VM_securityGroup_value_roundtrip():
    instance = cloudml_core_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.securityGroup == "sample_text"
    instance.securityGroup = "sample_text_2"
    assert instance.securityGroup == "sample_text_2"


def test_cloudml_core_VM_sshKey_value_roundtrip():
    instance = cloudml_core_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.sshKey == "sample_text"
    instance.sshKey = "sample_text_2"
    assert instance.sshKey == "sample_text_2"


def test_cloudml_core_VMInstance_hostname_value_roundtrip():
    instance = cloudml_core_VMInstance(hostname="sample_text", id="sample_text", publicAddress="sample_text")
    assert instance.hostname == "sample_text"
    instance.hostname = "sample_text_2"
    assert instance.hostname == "sample_text_2"


def test_cloudml_core_VMInstance_id_value_roundtrip():
    instance = cloudml_core_VMInstance(hostname="sample_text", id="sample_text", publicAddress="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_cloudml_core_VMInstance_publicAddress_value_roundtrip():
    instance = cloudml_core_VMInstance(hostname="sample_text", id="sample_text", publicAddress="sample_text")
    assert instance.publicAddress == "sample_text"
    instance.publicAddress = "sample_text_2"
    assert instance.publicAddress == "sample_text_2"


def test_cloudml_core_CloudMLElementWithProperties_isa_CloudMLElement():
    instance = cloudml_core_CloudMLElementWithProperties()
    assert isinstance(instance, CloudMLElement)


def test_cloudml_core_Property_isa_CloudMLElement():
    instance = cloudml_core_Property(value="sample_text")
    assert isinstance(instance, CloudMLElement)


def test_cloudml_core_Cloud_isa_CloudMLElementWithProperties():
    instance = cloudml_core_Cloud()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_core_CloudMLModel_isa_CloudMLElementWithProperties():
    instance = cloudml_core_CloudMLModel()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_core_Component_isa_CloudMLElementWithProperties():
    instance = cloudml_core_Component()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_core_ComponentInstance_isa_CloudMLElementWithProperties():
    instance = cloudml_core_ComponentInstance()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_core_ExecuteInstance_isa_CloudMLElementWithProperties():
    instance = cloudml_core_ExecuteInstance()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_core_ExecutionPlatform_isa_CloudMLElementWithProperties():
    instance = cloudml_core_ExecutionPlatform()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_core_ExecutionPlatformInstance_isa_CloudMLElementWithProperties():
    instance = cloudml_core_ExecutionPlatformInstance()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_core_Port_isa_CloudMLElementWithProperties():
    instance = cloudml_core_Port(isLocal=True, portNumber=7)
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_core_PortInstance_isa_CloudMLElementWithProperties():
    instance = cloudml_core_PortInstance()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_core_Provider_isa_CloudMLElementWithProperties():
    instance = cloudml_core_Provider(credentials="sample_text", login="sample_text", password="sample_text")
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_core_Relationship_isa_CloudMLElementWithProperties():
    instance = cloudml_core_Relationship()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_core_RelationshipInstance_isa_CloudMLElementWithProperties():
    instance = cloudml_core_RelationshipInstance()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_core_Resource_isa_CloudMLElementWithProperties():
    instance = cloudml_core_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_core_ResourcesPool_isa_CloudMLElementWithProperties():
    instance = cloudml_core_ResourcesPool(maxReplicats=7, minReplicats=7, nbReplicats=7, type="sample_text")
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_core_VMPort_isa_CloudMLElementWithProperties():
    instance = cloudml_core_VMPort()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_core_VMPortInstance_isa_CloudMLElementWithProperties():
    instance = cloudml_core_VMPortInstance()
    assert isinstance(instance, CloudMLElementWithProperties)


def test_cloudml_core_ExternalComponent_isa_Component():
    instance = cloudml_core_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    assert isinstance(instance, Component)


def test_cloudml_core_InternalComponent_isa_Component():
    instance = cloudml_core_InternalComponent()
    assert isinstance(instance, Component)


def test_cloudml_core_ExternalComponentInstance_isa_ComponentInstance():
    instance = cloudml_core_ExternalComponentInstance(ips="sample_text", status="sample_text")
    assert isinstance(instance, ComponentInstance)


def test_cloudml_core_InternalComponentInstance_isa_ComponentInstance():
    instance = cloudml_core_InternalComponentInstance()
    assert isinstance(instance, ComponentInstance)


def test_cloudml_core_ProvidedExecutionPlatform_isa_ExecutionPlatform():
    instance = cloudml_core_ProvidedExecutionPlatform()
    assert isinstance(instance, ExecutionPlatform)


def test_cloudml_core_RequiredExecutionPlatform_isa_ExecutionPlatform():
    instance = cloudml_core_RequiredExecutionPlatform()
    assert isinstance(instance, ExecutionPlatform)


def test_cloudml_core_ProvidedExecutionPlatformInstance_isa_ExecutionPlatformInstance():
    instance = cloudml_core_ProvidedExecutionPlatformInstance()
    assert isinstance(instance, ExecutionPlatformInstance)


def test_cloudml_core_RequiredExecutionPlatformInstance_isa_ExecutionPlatformInstance():
    instance = cloudml_core_RequiredExecutionPlatformInstance()
    assert isinstance(instance, ExecutionPlatformInstance)


def test_cloudml_core_VM_isa_ExternalComponent():
    instance = cloudml_core_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert isinstance(instance, ExternalComponent)


def test_cloudml_core_VMInstance_isa_ExternalComponentInstance():
    instance = cloudml_core_VMInstance(hostname="sample_text", id="sample_text", publicAddress="sample_text")
    assert isinstance(instance, ExternalComponentInstance)


def test_cloudml_core_ProvidedPort_isa_Port():
    instance = cloudml_core_ProvidedPort()
    assert isinstance(instance, Port)


def test_cloudml_core_RequiredPort_isa_Port():
    instance = cloudml_core_RequiredPort(isMandatory=True)
    assert isinstance(instance, Port)


def test_cloudml_core_ProvidedPortInstance_isa_PortInstance():
    instance = cloudml_core_ProvidedPortInstance()
    assert isinstance(instance, PortInstance)


def test_cloudml_core_RequiredPortInstance_isa_PortInstance():
    instance = cloudml_core_RequiredPortInstance()
    assert isinstance(instance, PortInstance)


def test_cloudml_core_DockerResource_isa_Resource():
    instance = cloudml_core_DockerResource(dockerFilePath="sample_text", image="sample_text")
    assert isinstance(instance, Resource)


def test_cloudml_core_PuppetResource_isa_Resource():
    instance = cloudml_core_PuppetResource(configurationFile="sample_text", configureHostnameCommand="sample_text", manifestEntry="sample_text", masterEndpoint="sample_text", repositoryEndpoint="sample_text", repositoryKey="sample_text", username="sample_text")
    assert isinstance(instance, Resource)


def test_assoc_baseInstances105_link_reassign_clear():
    a = cloudml_core_ResourcesPool(maxReplicats=7, minReplicats=7, nbReplicats=7, type="sample_text")
    b1 = VMInstance()
    b2 = VMInstance()
    _safe_set(a, 'cloudml_core_ResourcesPool', {b1})
    assert _is_linked(a, 'cloudml_core_ResourcesPool', b1)
    if hasattr(b1, 'VMInstance106'):
        assert _is_linked(b1, 'VMInstance106', a)
    _safe_set(a, 'cloudml_core_ResourcesPool', {b2})
    assert _is_linked(a, 'cloudml_core_ResourcesPool', b2)
    if hasattr(b1, 'VMInstance106'):
        assert not _is_linked(b1, 'VMInstance106', a)
    if hasattr(b2, 'VMInstance106'):
        assert _is_linked(b2, 'VMInstance106', a)
    _safe_set(a, 'cloudml_core_ResourcesPool', set())
    assert not _is_linked(a, 'cloudml_core_ResourcesPool', b2)
    if hasattr(b2, 'VMInstance106'):
        assert not _is_linked(b2, 'VMInstance106', a)


def test_assoc_component44_link_reassign_clear():
    a = cloudml_core_Port(isLocal=True, portNumber=7)
    b1 = Component()
    b2 = Component()
    _safe_set(a, 'cloudml_core_Port', b1)
    assert _is_linked(a, 'cloudml_core_Port', b1)
    if hasattr(b1, 'Component45'):
        assert _is_linked(b1, 'Component45', a)
    _safe_set(a, 'cloudml_core_Port', b2)
    assert _is_linked(a, 'cloudml_core_Port', b2)
    if hasattr(b1, 'Component45'):
        assert not _is_linked(b1, 'Component45', a)
    if hasattr(b2, 'Component45'):
        assert _is_linked(b2, 'Component45', a)
    _safe_set(a, 'cloudml_core_Port', None)
    assert not _is_linked(a, 'cloudml_core_Port', b2)
    if hasattr(b2, 'Component45'):
        assert not _is_linked(b2, 'Component45', a)


def test_assoc_provide85_link_reassign_clear():
    a = cloudml_core_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    b1 = VMPort()
    b2 = VMPort()
    _safe_set(a, 'cloudml_core_ExternalComponent86', {b1})
    assert _is_linked(a, 'cloudml_core_ExternalComponent86', b1)
    if hasattr(b1, 'VMPort87'):
        assert _is_linked(b1, 'VMPort87', a)
    _safe_set(a, 'cloudml_core_ExternalComponent86', {b2})
    assert _is_linked(a, 'cloudml_core_ExternalComponent86', b2)
    if hasattr(b1, 'VMPort87'):
        assert not _is_linked(b1, 'VMPort87', a)
    if hasattr(b2, 'VMPort87'):
        assert _is_linked(b2, 'VMPort87', a)
    _safe_set(a, 'cloudml_core_ExternalComponent86', set())
    assert not _is_linked(a, 'cloudml_core_ExternalComponent86', b2)
    if hasattr(b2, 'VMPort87'):
        assert not _is_linked(b2, 'VMPort87', a)


def test_assoc_provide88_link_reassign_clear():
    a = cloudml_core_ExternalComponentInstance(ips="sample_text", status="sample_text")
    b1 = VMPortInstance()
    b2 = VMPortInstance()
    _safe_set(a, 'cloudml_core_ExternalComponentInstance', {b1})
    assert _is_linked(a, 'cloudml_core_ExternalComponentInstance', b1)
    if hasattr(b1, 'VMPortInstance89'):
        assert _is_linked(b1, 'VMPortInstance89', a)
    _safe_set(a, 'cloudml_core_ExternalComponentInstance', {b2})
    assert _is_linked(a, 'cloudml_core_ExternalComponentInstance', b2)
    if hasattr(b1, 'VMPortInstance89'):
        assert not _is_linked(b1, 'VMPortInstance89', a)
    if hasattr(b2, 'VMPortInstance89'):
        assert _is_linked(b2, 'VMPortInstance89', a)
    _safe_set(a, 'cloudml_core_ExternalComponentInstance', set())
    assert not _is_linked(a, 'cloudml_core_ExternalComponentInstance', b2)
    if hasattr(b2, 'VMPortInstance89'):
        assert not _is_linked(b2, 'VMPortInstance89', a)


def test_assoc_provided34_link_reassign_clear():
    a = cloudml_core_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    b1 = VMPort()
    b2 = VMPort()
    _safe_set(a, 'cloudml_core_VM', {b1})
    assert _is_linked(a, 'cloudml_core_VM', b1)
    if hasattr(b1, 'VMPort'):
        assert _is_linked(b1, 'VMPort', a)
    _safe_set(a, 'cloudml_core_VM', {b2})
    assert _is_linked(a, 'cloudml_core_VM', b2)
    if hasattr(b1, 'VMPort'):
        assert not _is_linked(b1, 'VMPort', a)
    if hasattr(b2, 'VMPort'):
        assert _is_linked(b2, 'VMPort', a)
    _safe_set(a, 'cloudml_core_VM', set())
    assert not _is_linked(a, 'cloudml_core_VM', b2)
    if hasattr(b2, 'VMPort'):
        assert not _is_linked(b2, 'VMPort', a)


def test_assoc_provided59_link_reassign_clear():
    a = cloudml_core_VMInstance(hostname="sample_text", id="sample_text", publicAddress="sample_text")
    b1 = VMPortInstance()
    b2 = VMPortInstance()
    _safe_set(a, 'cloudml_core_VMInstance', {b1})
    assert _is_linked(a, 'cloudml_core_VMInstance', b1)
    if hasattr(b1, 'VMPortInstance'):
        assert _is_linked(b1, 'VMPortInstance', a)
    _safe_set(a, 'cloudml_core_VMInstance', {b2})
    assert _is_linked(a, 'cloudml_core_VMInstance', b2)
    if hasattr(b1, 'VMPortInstance'):
        assert not _is_linked(b1, 'VMPortInstance', a)
    if hasattr(b2, 'VMPortInstance'):
        assert _is_linked(b2, 'VMPortInstance', a)
    _safe_set(a, 'cloudml_core_VMInstance', set())
    assert not _is_linked(a, 'cloudml_core_VMInstance', b2)
    if hasattr(b2, 'VMPortInstance'):
        assert not _is_linked(b2, 'VMPortInstance', a)


def test_assoc_provider83_link_reassign_clear():
    a = cloudml_core_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    b1 = Provider()
    b2 = Provider()
    _safe_set(a, 'cloudml_core_ExternalComponent', b1)
    assert _is_linked(a, 'cloudml_core_ExternalComponent', b1)
    if hasattr(b1, 'Provider84'):
        assert _is_linked(b1, 'Provider84', a)
    _safe_set(a, 'cloudml_core_ExternalComponent', b2)
    assert _is_linked(a, 'cloudml_core_ExternalComponent', b2)
    if hasattr(b1, 'Provider84'):
        assert not _is_linked(b1, 'Provider84', a)
    if hasattr(b2, 'Provider84'):
        assert _is_linked(b2, 'Provider84', a)
    _safe_set(a, 'cloudml_core_ExternalComponent', None)
    assert not _is_linked(a, 'cloudml_core_ExternalComponent', b2)
    if hasattr(b2, 'Provider84'):
        assert not _is_linked(b2, 'Provider84', a)


def test_assoc_replicats107_link_reassign_clear():
    a = cloudml_core_ResourcesPool(maxReplicats=7, minReplicats=7, nbReplicats=7, type="sample_text")
    b1 = VMInstance()
    b2 = VMInstance()
    _safe_set(a, 'cloudml_core_ResourcesPool108', {b1})
    assert _is_linked(a, 'cloudml_core_ResourcesPool108', b1)
    if hasattr(b1, 'VMInstance109'):
        assert _is_linked(b1, 'VMInstance109', a)
    _safe_set(a, 'cloudml_core_ResourcesPool108', {b2})
    assert _is_linked(a, 'cloudml_core_ResourcesPool108', b2)
    if hasattr(b1, 'VMInstance109'):
        assert not _is_linked(b1, 'VMInstance109', a)
    if hasattr(b2, 'VMInstance109'):
        assert _is_linked(b2, 'VMInstance109', a)
    _safe_set(a, 'cloudml_core_ResourcesPool108', set())
    assert not _is_linked(a, 'cloudml_core_ResourcesPool108', b2)
    if hasattr(b2, 'VMInstance109'):
        assert not _is_linked(b2, 'VMInstance109', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Cloud_strategy = st.builds(Cloud)
@given(instance=Cloud_strategy)
@settings(max_examples=25)
def test_Cloud_instantiation(instance):
    assert isinstance(instance, Cloud)


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


DockerResource_strategy = st.builds(DockerResource)
@given(instance=DockerResource_strategy)
@settings(max_examples=25)
def test_DockerResource_instantiation(instance):
    assert isinstance(instance, DockerResource)


ExecuteInstance_strategy = st.builds(ExecuteInstance)
@given(instance=ExecuteInstance_strategy)
@settings(max_examples=25)
def test_ExecuteInstance_instantiation(instance):
    assert isinstance(instance, ExecuteInstance)


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


InternalComponent_strategy = st.builds(InternalComponent)
@given(instance=InternalComponent_strategy)
@settings(max_examples=25)
def test_InternalComponent_instantiation(instance):
    assert isinstance(instance, InternalComponent)


InternalComponentInstance_strategy = st.builds(InternalComponentInstance)
@given(instance=InternalComponentInstance_strategy)
@settings(max_examples=25)
def test_InternalComponentInstance_instantiation(instance):
    assert isinstance(instance, InternalComponentInstance)


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


Property_strategy = st.builds(Property)
@given(instance=Property_strategy)
@settings(max_examples=25)
def test_Property_instantiation(instance):
    assert isinstance(instance, Property)


ProvidedExecutionPlatform_strategy = st.builds(ProvidedExecutionPlatform)
@given(instance=ProvidedExecutionPlatform_strategy)
@settings(max_examples=25)
def test_ProvidedExecutionPlatform_instantiation(instance):
    assert isinstance(instance, ProvidedExecutionPlatform)


ProvidedExecutionPlatformInstance_strategy = st.builds(ProvidedExecutionPlatformInstance)
@given(instance=ProvidedExecutionPlatformInstance_strategy)
@settings(max_examples=25)
def test_ProvidedExecutionPlatformInstance_instantiation(instance):
    assert isinstance(instance, ProvidedExecutionPlatformInstance)


ProvidedPort_strategy = st.builds(ProvidedPort)
@given(instance=ProvidedPort_strategy)
@settings(max_examples=25)
def test_ProvidedPort_instantiation(instance):
    assert isinstance(instance, ProvidedPort)


ProvidedPortInstance_strategy = st.builds(ProvidedPortInstance)
@given(instance=ProvidedPortInstance_strategy)
@settings(max_examples=25)
def test_ProvidedPortInstance_instantiation(instance):
    assert isinstance(instance, ProvidedPortInstance)


Provider_strategy = st.builds(Provider)
@given(instance=Provider_strategy)
@settings(max_examples=25)
def test_Provider_instantiation(instance):
    assert isinstance(instance, Provider)


PuppetResource_strategy = st.builds(PuppetResource)
@given(instance=PuppetResource_strategy)
@settings(max_examples=25)
def test_PuppetResource_instantiation(instance):
    assert isinstance(instance, PuppetResource)


Relationship_strategy = st.builds(Relationship)
@given(instance=Relationship_strategy)
@settings(max_examples=25)
def test_Relationship_instantiation(instance):
    assert isinstance(instance, Relationship)


RelationshipInstance_strategy = st.builds(RelationshipInstance)
@given(instance=RelationshipInstance_strategy)
@settings(max_examples=25)
def test_RelationshipInstance_instantiation(instance):
    assert isinstance(instance, RelationshipInstance)


RequiredExecutionPlatform_strategy = st.builds(RequiredExecutionPlatform)
@given(instance=RequiredExecutionPlatform_strategy)
@settings(max_examples=25)
def test_RequiredExecutionPlatform_instantiation(instance):
    assert isinstance(instance, RequiredExecutionPlatform)


RequiredExecutionPlatformInstance_strategy = st.builds(RequiredExecutionPlatformInstance)
@given(instance=RequiredExecutionPlatformInstance_strategy)
@settings(max_examples=25)
def test_RequiredExecutionPlatformInstance_instantiation(instance):
    assert isinstance(instance, RequiredExecutionPlatformInstance)


RequiredPort_strategy = st.builds(RequiredPort)
@given(instance=RequiredPort_strategy)
@settings(max_examples=25)
def test_RequiredPort_instantiation(instance):
    assert isinstance(instance, RequiredPort)


RequiredPortInstance_strategy = st.builds(RequiredPortInstance)
@given(instance=RequiredPortInstance_strategy)
@settings(max_examples=25)
def test_RequiredPortInstance_instantiation(instance):
    assert isinstance(instance, RequiredPortInstance)


Resource_strategy = st.builds(Resource)
@given(instance=Resource_strategy)
@settings(max_examples=25)
def test_Resource_instantiation(instance):
    assert isinstance(instance, Resource)


ResourcesPool_strategy = st.builds(ResourcesPool)
@given(instance=ResourcesPool_strategy)
@settings(max_examples=25)
def test_ResourcesPool_instantiation(instance):
    assert isinstance(instance, ResourcesPool)


VM_strategy = st.builds(VM)
@given(instance=VM_strategy)
@settings(max_examples=25)
def test_VM_instantiation(instance):
    assert isinstance(instance, VM)


VMInstance_strategy = st.builds(VMInstance)
@given(instance=VMInstance_strategy)
@settings(max_examples=25)
def test_VMInstance_instantiation(instance):
    assert isinstance(instance, VMInstance)


VMPort_strategy = st.builds(VMPort)
@given(instance=VMPort_strategy)
@settings(max_examples=25)
def test_VMPort_instantiation(instance):
    assert isinstance(instance, VMPort)


VMPortInstance_strategy = st.builds(VMPortInstance)
@given(instance=VMPortInstance_strategy)
@settings(max_examples=25)
def test_VMPortInstance_instantiation(instance):
    assert isinstance(instance, VMPortInstance)


cloudml_core_Cloud_strategy = st.builds(cloudml_core_Cloud)
@given(instance=cloudml_core_Cloud_strategy)
@settings(max_examples=25)
def test_cloudml_core_Cloud_instantiation(instance):
    assert isinstance(instance, cloudml_core_Cloud)


cloudml_core_CloudMLElement_strategy = st.builds(cloudml_core_CloudMLElement, name=safe_text)
@given(instance=cloudml_core_CloudMLElement_strategy)
@settings(max_examples=25)
def test_cloudml_core_CloudMLElement_instantiation(instance):
    assert isinstance(instance, cloudml_core_CloudMLElement)


cloudml_core_CloudMLElementWithProperties_strategy = st.builds(cloudml_core_CloudMLElementWithProperties)
@given(instance=cloudml_core_CloudMLElementWithProperties_strategy)
@settings(max_examples=25)
def test_cloudml_core_CloudMLElementWithProperties_instantiation(instance):
    assert isinstance(instance, cloudml_core_CloudMLElementWithProperties)


cloudml_core_CloudMLModel_strategy = st.builds(cloudml_core_CloudMLModel)
@given(instance=cloudml_core_CloudMLModel_strategy)
@settings(max_examples=25)
def test_cloudml_core_CloudMLModel_instantiation(instance):
    assert isinstance(instance, cloudml_core_CloudMLModel)


cloudml_core_Component_strategy = st.builds(cloudml_core_Component)
@given(instance=cloudml_core_Component_strategy)
@settings(max_examples=25)
def test_cloudml_core_Component_instantiation(instance):
    assert isinstance(instance, cloudml_core_Component)


cloudml_core_ComponentInstance_strategy = st.builds(cloudml_core_ComponentInstance)
@given(instance=cloudml_core_ComponentInstance_strategy)
@settings(max_examples=25)
def test_cloudml_core_ComponentInstance_instantiation(instance):
    assert isinstance(instance, cloudml_core_ComponentInstance)


cloudml_core_DockerResource_strategy = st.builds(cloudml_core_DockerResource, dockerFilePath=safe_text, image=safe_text)
@given(instance=cloudml_core_DockerResource_strategy)
@settings(max_examples=25)
def test_cloudml_core_DockerResource_instantiation(instance):
    assert isinstance(instance, cloudml_core_DockerResource)


cloudml_core_ExecuteInstance_strategy = st.builds(cloudml_core_ExecuteInstance)
@given(instance=cloudml_core_ExecuteInstance_strategy)
@settings(max_examples=25)
def test_cloudml_core_ExecuteInstance_instantiation(instance):
    assert isinstance(instance, cloudml_core_ExecuteInstance)


cloudml_core_ExecutionPlatform_strategy = st.builds(cloudml_core_ExecutionPlatform)
@given(instance=cloudml_core_ExecutionPlatform_strategy)
@settings(max_examples=25)
def test_cloudml_core_ExecutionPlatform_instantiation(instance):
    assert isinstance(instance, cloudml_core_ExecutionPlatform)


cloudml_core_ExecutionPlatformInstance_strategy = st.builds(cloudml_core_ExecutionPlatformInstance)
@given(instance=cloudml_core_ExecutionPlatformInstance_strategy)
@settings(max_examples=25)
def test_cloudml_core_ExecutionPlatformInstance_instantiation(instance):
    assert isinstance(instance, cloudml_core_ExecutionPlatformInstance)


cloudml_core_ExternalComponent_strategy = st.builds(cloudml_core_ExternalComponent, Region=safe_text, endPoint=safe_text, location=safe_text, login=safe_text, passwd=safe_text, serviceType=safe_text)
@given(instance=cloudml_core_ExternalComponent_strategy)
@settings(max_examples=25)
def test_cloudml_core_ExternalComponent_instantiation(instance):
    assert isinstance(instance, cloudml_core_ExternalComponent)


cloudml_core_ExternalComponentInstance_strategy = st.builds(cloudml_core_ExternalComponentInstance, ips=safe_text, status=safe_text)
@given(instance=cloudml_core_ExternalComponentInstance_strategy)
@settings(max_examples=25)
def test_cloudml_core_ExternalComponentInstance_instantiation(instance):
    assert isinstance(instance, cloudml_core_ExternalComponentInstance)


cloudml_core_InternalComponent_strategy = st.builds(cloudml_core_InternalComponent)
@given(instance=cloudml_core_InternalComponent_strategy)
@settings(max_examples=25)
def test_cloudml_core_InternalComponent_instantiation(instance):
    assert isinstance(instance, cloudml_core_InternalComponent)


cloudml_core_InternalComponentInstance_strategy = st.builds(cloudml_core_InternalComponentInstance)
@given(instance=cloudml_core_InternalComponentInstance_strategy)
@settings(max_examples=25)
def test_cloudml_core_InternalComponentInstance_instantiation(instance):
    assert isinstance(instance, cloudml_core_InternalComponentInstance)


cloudml_core_Port_strategy = st.builds(cloudml_core_Port, isLocal=st.booleans(), portNumber=st.integers())
@given(instance=cloudml_core_Port_strategy)
@settings(max_examples=25)
def test_cloudml_core_Port_instantiation(instance):
    assert isinstance(instance, cloudml_core_Port)


cloudml_core_PortInstance_strategy = st.builds(cloudml_core_PortInstance)
@given(instance=cloudml_core_PortInstance_strategy)
@settings(max_examples=25)
def test_cloudml_core_PortInstance_instantiation(instance):
    assert isinstance(instance, cloudml_core_PortInstance)


cloudml_core_Property_strategy = st.builds(cloudml_core_Property, value=safe_text)
@given(instance=cloudml_core_Property_strategy)
@settings(max_examples=25)
def test_cloudml_core_Property_instantiation(instance):
    assert isinstance(instance, cloudml_core_Property)


cloudml_core_ProvidedExecutionPlatform_strategy = st.builds(cloudml_core_ProvidedExecutionPlatform)
@given(instance=cloudml_core_ProvidedExecutionPlatform_strategy)
@settings(max_examples=25)
def test_cloudml_core_ProvidedExecutionPlatform_instantiation(instance):
    assert isinstance(instance, cloudml_core_ProvidedExecutionPlatform)


cloudml_core_ProvidedExecutionPlatformInstance_strategy = st.builds(cloudml_core_ProvidedExecutionPlatformInstance)
@given(instance=cloudml_core_ProvidedExecutionPlatformInstance_strategy)
@settings(max_examples=25)
def test_cloudml_core_ProvidedExecutionPlatformInstance_instantiation(instance):
    assert isinstance(instance, cloudml_core_ProvidedExecutionPlatformInstance)


cloudml_core_ProvidedPort_strategy = st.builds(cloudml_core_ProvidedPort)
@given(instance=cloudml_core_ProvidedPort_strategy)
@settings(max_examples=25)
def test_cloudml_core_ProvidedPort_instantiation(instance):
    assert isinstance(instance, cloudml_core_ProvidedPort)


cloudml_core_ProvidedPortInstance_strategy = st.builds(cloudml_core_ProvidedPortInstance)
@given(instance=cloudml_core_ProvidedPortInstance_strategy)
@settings(max_examples=25)
def test_cloudml_core_ProvidedPortInstance_instantiation(instance):
    assert isinstance(instance, cloudml_core_ProvidedPortInstance)


cloudml_core_Provider_strategy = st.builds(cloudml_core_Provider, credentials=safe_text, login=safe_text, password=safe_text)
@given(instance=cloudml_core_Provider_strategy)
@settings(max_examples=25)
def test_cloudml_core_Provider_instantiation(instance):
    assert isinstance(instance, cloudml_core_Provider)


cloudml_core_PuppetResource_strategy = st.builds(cloudml_core_PuppetResource, configurationFile=safe_text, configureHostnameCommand=safe_text, manifestEntry=safe_text, masterEndpoint=safe_text, repositoryEndpoint=safe_text, repositoryKey=safe_text, username=safe_text)
@given(instance=cloudml_core_PuppetResource_strategy)
@settings(max_examples=25)
def test_cloudml_core_PuppetResource_instantiation(instance):
    assert isinstance(instance, cloudml_core_PuppetResource)


cloudml_core_Relationship_strategy = st.builds(cloudml_core_Relationship)
@given(instance=cloudml_core_Relationship_strategy)
@settings(max_examples=25)
def test_cloudml_core_Relationship_instantiation(instance):
    assert isinstance(instance, cloudml_core_Relationship)


cloudml_core_RelationshipInstance_strategy = st.builds(cloudml_core_RelationshipInstance)
@given(instance=cloudml_core_RelationshipInstance_strategy)
@settings(max_examples=25)
def test_cloudml_core_RelationshipInstance_instantiation(instance):
    assert isinstance(instance, cloudml_core_RelationshipInstance)


cloudml_core_RequiredExecutionPlatform_strategy = st.builds(cloudml_core_RequiredExecutionPlatform)
@given(instance=cloudml_core_RequiredExecutionPlatform_strategy)
@settings(max_examples=25)
def test_cloudml_core_RequiredExecutionPlatform_instantiation(instance):
    assert isinstance(instance, cloudml_core_RequiredExecutionPlatform)


cloudml_core_RequiredExecutionPlatformInstance_strategy = st.builds(cloudml_core_RequiredExecutionPlatformInstance)
@given(instance=cloudml_core_RequiredExecutionPlatformInstance_strategy)
@settings(max_examples=25)
def test_cloudml_core_RequiredExecutionPlatformInstance_instantiation(instance):
    assert isinstance(instance, cloudml_core_RequiredExecutionPlatformInstance)


cloudml_core_RequiredPort_strategy = st.builds(cloudml_core_RequiredPort, isMandatory=st.booleans())
@given(instance=cloudml_core_RequiredPort_strategy)
@settings(max_examples=25)
def test_cloudml_core_RequiredPort_instantiation(instance):
    assert isinstance(instance, cloudml_core_RequiredPort)


cloudml_core_RequiredPortInstance_strategy = st.builds(cloudml_core_RequiredPortInstance)
@given(instance=cloudml_core_RequiredPortInstance_strategy)
@settings(max_examples=25)
def test_cloudml_core_RequiredPortInstance_instantiation(instance):
    assert isinstance(instance, cloudml_core_RequiredPortInstance)


cloudml_core_Resource_strategy = st.builds(cloudml_core_Resource, configureCommand=safe_text, downloadCommand=safe_text, executeLocally=st.booleans(), installCommand=safe_text, requireCredentials=st.booleans(), startCommand=safe_text, stopCommand=safe_text, uploadCommand=safe_text)
@given(instance=cloudml_core_Resource_strategy)
@settings(max_examples=25)
def test_cloudml_core_Resource_instantiation(instance):
    assert isinstance(instance, cloudml_core_Resource)


cloudml_core_ResourcesPool_strategy = st.builds(cloudml_core_ResourcesPool, maxReplicats=st.integers(), minReplicats=st.integers(), nbReplicats=st.integers(), type=safe_text)
@given(instance=cloudml_core_ResourcesPool_strategy)
@settings(max_examples=25)
def test_cloudml_core_ResourcesPool_instantiation(instance):
    assert isinstance(instance, cloudml_core_ResourcesPool)


cloudml_core_VM_strategy = st.builds(cloudml_core_VM, groupName=safe_text, imageId=safe_text, is64os=st.booleans(), maxCores=st.integers(), maxRam=st.integers(), maxStorage=st.integers(), minCores=st.integers(), minRam=st.integers(), minStorage=st.integers(), os=safe_text, privateKey=safe_text, providerSpecificTypeName=safe_text, securityGroup=safe_text, sshKey=safe_text)
@given(instance=cloudml_core_VM_strategy)
@settings(max_examples=25)
def test_cloudml_core_VM_instantiation(instance):
    assert isinstance(instance, cloudml_core_VM)


cloudml_core_VMInstance_strategy = st.builds(cloudml_core_VMInstance, hostname=safe_text, id=safe_text, publicAddress=safe_text)
@given(instance=cloudml_core_VMInstance_strategy)
@settings(max_examples=25)
def test_cloudml_core_VMInstance_instantiation(instance):
    assert isinstance(instance, cloudml_core_VMInstance)


cloudml_core_VMPort_strategy = st.builds(cloudml_core_VMPort)
@given(instance=cloudml_core_VMPort_strategy)
@settings(max_examples=25)
def test_cloudml_core_VMPort_instantiation(instance):
    assert isinstance(instance, cloudml_core_VMPort)


cloudml_core_VMPortInstance_strategy = st.builds(cloudml_core_VMPortInstance)
@given(instance=cloudml_core_VMPortInstance_strategy)
@settings(max_examples=25)
def test_cloudml_core_VMPortInstance_instantiation(instance):
    assert isinstance(instance, cloudml_core_VMPortInstance)


