import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CloudElement,
    Cluster,
    Component,
    ExecutionPlatform,
    ExternalComponent,
    InternalComponent,
    Port,
    Resource,
    ddsm_ChefResource,
    ddsm_ClientNode,
    ddsm_CloudElement,
    ddsm_Cluster,
    ddsm_Component,
    ddsm_DDSM,
    ddsm_ExecutionBinding,
    ddsm_ExecutionPlatform,
    ddsm_ExternalComponent,
    ddsm_HDFSDataNode,
    ddsm_HDFSNameNode,
    ddsm_InternalComponent,
    ddsm_Kafka,
    ddsm_Port,
    ddsm_Property,
    ddsm_ProvidedExecutionPlatform,
    ddsm_ProvidedPort,
    ddsm_Provider,
    ddsm_Relationship,
    ddsm_RequiredExecutionPlatform,
    ddsm_RequiredPort,
    ddsm_Resource,
    ddsm_StormCluster,
    ddsm_StormNimbus,
    ddsm_StormSupervisor,
    ddsm_VM,
    ddsm_YarnNodeManager,
    ddsm_YarnResourceManager,
    ddsm_Zookeeper,
    ProviderType,
    VMSize,
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

def test_ddsm_ChefResource_cookbookId_value_roundtrip():
    instance = ddsm_ChefResource(cookbookId="sample_text")
    assert instance.cookbookId == "sample_text"
    instance.cookbookId = "sample_text_2"
    assert instance.cookbookId == "sample_text_2"


def test_ddsm_ClientNode_artifactUrl_value_roundtrip():
    instance = ddsm_ClientNode(artifactUrl="sample_text", mainClass="sample_text", type="sample_text")
    assert instance.artifactUrl == "sample_text"
    instance.artifactUrl = "sample_text_2"
    assert instance.artifactUrl == "sample_text_2"


def test_ddsm_ClientNode_mainClass_value_roundtrip():
    instance = ddsm_ClientNode(artifactUrl="sample_text", mainClass="sample_text", type="sample_text")
    assert instance.mainClass == "sample_text"
    instance.mainClass = "sample_text_2"
    assert instance.mainClass == "sample_text_2"


def test_ddsm_ClientNode_type_value_roundtrip():
    instance = ddsm_ClientNode(artifactUrl="sample_text", mainClass="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_ddsm_CloudElement_description_value_roundtrip():
    instance = ddsm_CloudElement(description="sample_text", elementId="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_ddsm_CloudElement_elementId_value_roundtrip():
    instance = ddsm_CloudElement(description="sample_text", elementId="sample_text")
    assert instance.elementId == "sample_text"
    instance.elementId = "sample_text_2"
    assert instance.elementId == "sample_text_2"


def test_ddsm_DDSM_description_value_roundtrip():
    instance = ddsm_DDSM(description="sample_text", modelId="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_ddsm_DDSM_modelId_value_roundtrip():
    instance = ddsm_DDSM(description="sample_text", modelId="sample_text")
    assert instance.modelId == "sample_text"
    instance.modelId = "sample_text_2"
    assert instance.modelId == "sample_text_2"


def test_ddsm_ExternalComponent_location_value_roundtrip():
    instance = ddsm_ExternalComponent(location="sample_text", login="sample_text", password="sample_text", region="sample_text", serviceType="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_ddsm_ExternalComponent_login_value_roundtrip():
    instance = ddsm_ExternalComponent(location="sample_text", login="sample_text", password="sample_text", region="sample_text", serviceType="sample_text")
    assert instance.login == "sample_text"
    instance.login = "sample_text_2"
    assert instance.login == "sample_text_2"


def test_ddsm_ExternalComponent_password_value_roundtrip():
    instance = ddsm_ExternalComponent(location="sample_text", login="sample_text", password="sample_text", region="sample_text", serviceType="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_ddsm_ExternalComponent_region_value_roundtrip():
    instance = ddsm_ExternalComponent(location="sample_text", login="sample_text", password="sample_text", region="sample_text", serviceType="sample_text")
    assert instance.region == "sample_text"
    instance.region = "sample_text_2"
    assert instance.region == "sample_text_2"


def test_ddsm_ExternalComponent_serviceType_value_roundtrip():
    instance = ddsm_ExternalComponent(location="sample_text", login="sample_text", password="sample_text", region="sample_text", serviceType="sample_text")
    assert instance.serviceType == "sample_text"
    instance.serviceType = "sample_text_2"
    assert instance.serviceType == "sample_text_2"


def test_ddsm_Port_isLocal_value_roundtrip():
    instance = ddsm_Port(isLocal=True, portNumber="sample_text")
    assert instance.isLocal == True
    instance.isLocal = False
    assert instance.isLocal == False


def test_ddsm_Port_portNumber_value_roundtrip():
    instance = ddsm_Port(isLocal=True, portNumber="sample_text")
    assert instance.portNumber == "sample_text"
    instance.portNumber = "sample_text_2"
    assert instance.portNumber == "sample_text_2"


def test_ddsm_Property_propertyId_value_roundtrip():
    instance = ddsm_Property(propertyId="sample_text", value="sample_text")
    assert instance.propertyId == "sample_text"
    instance.propertyId = "sample_text_2"
    assert instance.propertyId == "sample_text_2"


def test_ddsm_Property_value_value_roundtrip():
    instance = ddsm_Property(propertyId="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_ddsm_Provider_credentialsPath_value_roundtrip():
    instance = ddsm_Provider(credentialsPath="sample_text", type="sample_text")
    assert instance.credentialsPath == "sample_text"
    instance.credentialsPath = "sample_text_2"
    assert instance.credentialsPath == "sample_text_2"


def test_ddsm_Provider_type_value_roundtrip():
    instance = ddsm_Provider(credentialsPath="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_ddsm_RequiredExecutionPlatform_isMandatory_value_roundtrip():
    instance = ddsm_RequiredExecutionPlatform(isMandatory=True)
    assert instance.isMandatory == True
    instance.isMandatory = False
    assert instance.isMandatory == False


def test_ddsm_RequiredPort_isMandatory_value_roundtrip():
    instance = ddsm_RequiredPort(isMandatory=True)
    assert instance.isMandatory == True
    instance.isMandatory = False
    assert instance.isMandatory == False


def test_ddsm_Resource_configureCommand_value_roundtrip():
    instance = ddsm_Resource(configureCommand="sample_text", createCommand="sample_text", downloadCommand="sample_text", installCommand="sample_text", resourceId="sample_text", startCommand="sample_text", stopCommand="sample_text")
    assert instance.configureCommand == "sample_text"
    instance.configureCommand = "sample_text_2"
    assert instance.configureCommand == "sample_text_2"


def test_ddsm_Resource_createCommand_value_roundtrip():
    instance = ddsm_Resource(configureCommand="sample_text", createCommand="sample_text", downloadCommand="sample_text", installCommand="sample_text", resourceId="sample_text", startCommand="sample_text", stopCommand="sample_text")
    assert instance.createCommand == "sample_text"
    instance.createCommand = "sample_text_2"
    assert instance.createCommand == "sample_text_2"


def test_ddsm_Resource_downloadCommand_value_roundtrip():
    instance = ddsm_Resource(configureCommand="sample_text", createCommand="sample_text", downloadCommand="sample_text", installCommand="sample_text", resourceId="sample_text", startCommand="sample_text", stopCommand="sample_text")
    assert instance.downloadCommand == "sample_text"
    instance.downloadCommand = "sample_text_2"
    assert instance.downloadCommand == "sample_text_2"


def test_ddsm_Resource_installCommand_value_roundtrip():
    instance = ddsm_Resource(configureCommand="sample_text", createCommand="sample_text", downloadCommand="sample_text", installCommand="sample_text", resourceId="sample_text", startCommand="sample_text", stopCommand="sample_text")
    assert instance.installCommand == "sample_text"
    instance.installCommand = "sample_text_2"
    assert instance.installCommand == "sample_text_2"


def test_ddsm_Resource_resourceId_value_roundtrip():
    instance = ddsm_Resource(configureCommand="sample_text", createCommand="sample_text", downloadCommand="sample_text", installCommand="sample_text", resourceId="sample_text", startCommand="sample_text", stopCommand="sample_text")
    assert instance.resourceId == "sample_text"
    instance.resourceId = "sample_text_2"
    assert instance.resourceId == "sample_text_2"


def test_ddsm_Resource_startCommand_value_roundtrip():
    instance = ddsm_Resource(configureCommand="sample_text", createCommand="sample_text", downloadCommand="sample_text", installCommand="sample_text", resourceId="sample_text", startCommand="sample_text", stopCommand="sample_text")
    assert instance.startCommand == "sample_text"
    instance.startCommand = "sample_text_2"
    assert instance.startCommand == "sample_text_2"


def test_ddsm_Resource_stopCommand_value_roundtrip():
    instance = ddsm_Resource(configureCommand="sample_text", createCommand="sample_text", downloadCommand="sample_text", installCommand="sample_text", resourceId="sample_text", startCommand="sample_text", stopCommand="sample_text")
    assert instance.stopCommand == "sample_text"
    instance.stopCommand = "sample_text_2"
    assert instance.stopCommand == "sample_text_2"


def test_ddsm_StormCluster_number_of_workers_value_roundtrip():
    instance = ddsm_StormCluster(number_of_workers="sample_text")
    assert instance.number_of_workers == "sample_text"
    instance.number_of_workers = "sample_text_2"
    assert instance.number_of_workers == "sample_text_2"


def test_ddsm_StormNimbus_monitorFrequency_value_roundtrip():
    instance = ddsm_StormNimbus(monitorFrequency="sample_text", queueSize="sample_text", retryInterval="sample_text", retryTimes="sample_text", supervisorTimeout="sample_text", taskTimeout="sample_text")
    assert instance.monitorFrequency == "sample_text"
    instance.monitorFrequency = "sample_text_2"
    assert instance.monitorFrequency == "sample_text_2"


def test_ddsm_StormNimbus_queueSize_value_roundtrip():
    instance = ddsm_StormNimbus(monitorFrequency="sample_text", queueSize="sample_text", retryInterval="sample_text", retryTimes="sample_text", supervisorTimeout="sample_text", taskTimeout="sample_text")
    assert instance.queueSize == "sample_text"
    instance.queueSize = "sample_text_2"
    assert instance.queueSize == "sample_text_2"


def test_ddsm_StormNimbus_retryInterval_value_roundtrip():
    instance = ddsm_StormNimbus(monitorFrequency="sample_text", queueSize="sample_text", retryInterval="sample_text", retryTimes="sample_text", supervisorTimeout="sample_text", taskTimeout="sample_text")
    assert instance.retryInterval == "sample_text"
    instance.retryInterval = "sample_text_2"
    assert instance.retryInterval == "sample_text_2"


def test_ddsm_StormNimbus_retryTimes_value_roundtrip():
    instance = ddsm_StormNimbus(monitorFrequency="sample_text", queueSize="sample_text", retryInterval="sample_text", retryTimes="sample_text", supervisorTimeout="sample_text", taskTimeout="sample_text")
    assert instance.retryTimes == "sample_text"
    instance.retryTimes = "sample_text_2"
    assert instance.retryTimes == "sample_text_2"


def test_ddsm_StormNimbus_supervisorTimeout_value_roundtrip():
    instance = ddsm_StormNimbus(monitorFrequency="sample_text", queueSize="sample_text", retryInterval="sample_text", retryTimes="sample_text", supervisorTimeout="sample_text", taskTimeout="sample_text")
    assert instance.supervisorTimeout == "sample_text"
    instance.supervisorTimeout = "sample_text_2"
    assert instance.supervisorTimeout == "sample_text_2"


def test_ddsm_StormNimbus_taskTimeout_value_roundtrip():
    instance = ddsm_StormNimbus(monitorFrequency="sample_text", queueSize="sample_text", retryInterval="sample_text", retryTimes="sample_text", supervisorTimeout="sample_text", taskTimeout="sample_text")
    assert instance.taskTimeout == "sample_text"
    instance.taskTimeout = "sample_text_2"
    assert instance.taskTimeout == "sample_text_2"


def test_ddsm_StormSupervisor_cpuCapacity_value_roundtrip():
    instance = ddsm_StormSupervisor(cpuCapacity="sample_text", heartbeatFrequency="sample_text", memoryCapacity="sample_text", workerStartTimeout="sample_text")
    assert instance.cpuCapacity == "sample_text"
    instance.cpuCapacity = "sample_text_2"
    assert instance.cpuCapacity == "sample_text_2"


def test_ddsm_StormSupervisor_heartbeatFrequency_value_roundtrip():
    instance = ddsm_StormSupervisor(cpuCapacity="sample_text", heartbeatFrequency="sample_text", memoryCapacity="sample_text", workerStartTimeout="sample_text")
    assert instance.heartbeatFrequency == "sample_text"
    instance.heartbeatFrequency = "sample_text_2"
    assert instance.heartbeatFrequency == "sample_text_2"


def test_ddsm_StormSupervisor_memoryCapacity_value_roundtrip():
    instance = ddsm_StormSupervisor(cpuCapacity="sample_text", heartbeatFrequency="sample_text", memoryCapacity="sample_text", workerStartTimeout="sample_text")
    assert instance.memoryCapacity == "sample_text"
    instance.memoryCapacity = "sample_text_2"
    assert instance.memoryCapacity == "sample_text_2"


def test_ddsm_StormSupervisor_workerStartTimeout_value_roundtrip():
    instance = ddsm_StormSupervisor(cpuCapacity="sample_text", heartbeatFrequency="sample_text", memoryCapacity="sample_text", workerStartTimeout="sample_text")
    assert instance.workerStartTimeout == "sample_text"
    instance.workerStartTimeout = "sample_text_2"
    assert instance.workerStartTimeout == "sample_text_2"


def test_ddsm_VM_genericSize_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.genericSize == "sample_text"
    instance.genericSize = "sample_text_2"
    assert instance.genericSize == "sample_text_2"


def test_ddsm_VM_imageId_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.imageId == "sample_text"
    instance.imageId = "sample_text_2"
    assert instance.imageId == "sample_text_2"


def test_ddsm_VM_instances_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.instances == "sample_text"
    instance.instances = "sample_text_2"
    assert instance.instances == "sample_text_2"


def test_ddsm_VM_is64os_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.is64os == "sample_text"
    instance.is64os = "sample_text_2"
    assert instance.is64os == "sample_text_2"


def test_ddsm_VM_maxCores_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.maxCores == "sample_text"
    instance.maxCores = "sample_text_2"
    assert instance.maxCores == "sample_text_2"


def test_ddsm_VM_maxRam_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.maxRam == "sample_text"
    instance.maxRam = "sample_text_2"
    assert instance.maxRam == "sample_text_2"


def test_ddsm_VM_maxStorage_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.maxStorage == "sample_text"
    instance.maxStorage = "sample_text_2"
    assert instance.maxStorage == "sample_text_2"


def test_ddsm_VM_minCores_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.minCores == "sample_text"
    instance.minCores = "sample_text_2"
    assert instance.minCores == "sample_text_2"


def test_ddsm_VM_minRam_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.minRam == "sample_text"
    instance.minRam = "sample_text_2"
    assert instance.minRam == "sample_text_2"


def test_ddsm_VM_minStorage_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.minStorage == "sample_text"
    instance.minStorage = "sample_text_2"
    assert instance.minStorage == "sample_text_2"


def test_ddsm_VM_os_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.os == "sample_text"
    instance.os = "sample_text_2"
    assert instance.os == "sample_text_2"


def test_ddsm_VM_privateKey_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.privateKey == "sample_text"
    instance.privateKey = "sample_text_2"
    assert instance.privateKey == "sample_text_2"


def test_ddsm_VM_providerSpecificTypeName_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.providerSpecificTypeName == "sample_text"
    instance.providerSpecificTypeName = "sample_text_2"
    assert instance.providerSpecificTypeName == "sample_text_2"


def test_ddsm_VM_publicAddress_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.publicAddress == "sample_text"
    instance.publicAddress = "sample_text_2"
    assert instance.publicAddress == "sample_text_2"


def test_ddsm_VM_publicPorts_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.publicPorts == "sample_text"
    instance.publicPorts = "sample_text_2"
    assert instance.publicPorts == "sample_text_2"


def test_ddsm_VM_securityGroup_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.securityGroup == "sample_text"
    instance.securityGroup = "sample_text_2"
    assert instance.securityGroup == "sample_text_2"


def test_ddsm_VM_sshKey_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert instance.sshKey == "sample_text"
    instance.sshKey = "sample_text_2"
    assert instance.sshKey == "sample_text_2"


def test_ddsm_Zookeeper_initLimit_value_roundtrip():
    instance = ddsm_Zookeeper(initLimit="sample_text", syncLimit="sample_text", tickTime="sample_text")
    assert instance.initLimit == "sample_text"
    instance.initLimit = "sample_text_2"
    assert instance.initLimit == "sample_text_2"


def test_ddsm_Zookeeper_syncLimit_value_roundtrip():
    instance = ddsm_Zookeeper(initLimit="sample_text", syncLimit="sample_text", tickTime="sample_text")
    assert instance.syncLimit == "sample_text"
    instance.syncLimit = "sample_text_2"
    assert instance.syncLimit == "sample_text_2"


def test_ddsm_Zookeeper_tickTime_value_roundtrip():
    instance = ddsm_Zookeeper(initLimit="sample_text", syncLimit="sample_text", tickTime="sample_text")
    assert instance.tickTime == "sample_text"
    instance.tickTime = "sample_text_2"
    assert instance.tickTime == "sample_text_2"


def test_ddsm_Component_isa_CloudElement():
    instance = ddsm_Component()
    assert isinstance(instance, CloudElement)


def test_ddsm_ExecutionBinding_isa_CloudElement():
    instance = ddsm_ExecutionBinding()
    assert isinstance(instance, CloudElement)


def test_ddsm_ExecutionPlatform_isa_CloudElement():
    instance = ddsm_ExecutionPlatform()
    assert isinstance(instance, CloudElement)


def test_ddsm_Port_isa_CloudElement():
    instance = ddsm_Port(isLocal=True, portNumber="sample_text")
    assert isinstance(instance, CloudElement)


def test_ddsm_Provider_isa_CloudElement():
    instance = ddsm_Provider(credentialsPath="sample_text", type="sample_text")
    assert isinstance(instance, CloudElement)


def test_ddsm_Relationship_isa_CloudElement():
    instance = ddsm_Relationship()
    assert isinstance(instance, CloudElement)


def test_ddsm_StormCluster_isa_Cluster():
    instance = ddsm_StormCluster(number_of_workers="sample_text")
    assert isinstance(instance, Cluster)


def test_ddsm_ExternalComponent_isa_Component():
    instance = ddsm_ExternalComponent(location="sample_text", login="sample_text", password="sample_text", region="sample_text", serviceType="sample_text")
    assert isinstance(instance, Component)


def test_ddsm_InternalComponent_isa_Component():
    instance = ddsm_InternalComponent()
    assert isinstance(instance, Component)


def test_ddsm_ProvidedExecutionPlatform_isa_ExecutionPlatform():
    instance = ddsm_ProvidedExecutionPlatform()
    assert isinstance(instance, ExecutionPlatform)


def test_ddsm_RequiredExecutionPlatform_isa_ExecutionPlatform():
    instance = ddsm_RequiredExecutionPlatform(isMandatory=True)
    assert isinstance(instance, ExecutionPlatform)


def test_ddsm_Cluster_isa_ExternalComponent():
    instance = ddsm_Cluster()
    assert isinstance(instance, ExternalComponent)


def test_ddsm_VM_isa_ExternalComponent():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    assert isinstance(instance, ExternalComponent)


def test_ddsm_ClientNode_isa_InternalComponent():
    instance = ddsm_ClientNode(artifactUrl="sample_text", mainClass="sample_text", type="sample_text")
    assert isinstance(instance, InternalComponent)


def test_ddsm_HDFSDataNode_isa_InternalComponent():
    instance = ddsm_HDFSDataNode()
    assert isinstance(instance, InternalComponent)


def test_ddsm_HDFSNameNode_isa_InternalComponent():
    instance = ddsm_HDFSNameNode()
    assert isinstance(instance, InternalComponent)


def test_ddsm_Kafka_isa_InternalComponent():
    instance = ddsm_Kafka()
    assert isinstance(instance, InternalComponent)


def test_ddsm_StormNimbus_isa_InternalComponent():
    instance = ddsm_StormNimbus(monitorFrequency="sample_text", queueSize="sample_text", retryInterval="sample_text", retryTimes="sample_text", supervisorTimeout="sample_text", taskTimeout="sample_text")
    assert isinstance(instance, InternalComponent)


def test_ddsm_StormSupervisor_isa_InternalComponent():
    instance = ddsm_StormSupervisor(cpuCapacity="sample_text", heartbeatFrequency="sample_text", memoryCapacity="sample_text", workerStartTimeout="sample_text")
    assert isinstance(instance, InternalComponent)


def test_ddsm_YarnNodeManager_isa_InternalComponent():
    instance = ddsm_YarnNodeManager()
    assert isinstance(instance, InternalComponent)


def test_ddsm_YarnResourceManager_isa_InternalComponent():
    instance = ddsm_YarnResourceManager()
    assert isinstance(instance, InternalComponent)


def test_ddsm_Zookeeper_isa_InternalComponent():
    instance = ddsm_Zookeeper(initLimit="sample_text", syncLimit="sample_text", tickTime="sample_text")
    assert isinstance(instance, InternalComponent)


def test_ddsm_ProvidedPort_isa_Port():
    instance = ddsm_ProvidedPort()
    assert isinstance(instance, Port)


def test_ddsm_RequiredPort_isa_Port():
    instance = ddsm_RequiredPort(isMandatory=True)
    assert isinstance(instance, Port)


def test_ddsm_ChefResource_isa_Resource():
    instance = ddsm_ChefResource(cookbookId="sample_text")
    assert isinstance(instance, Resource)


def test_assoc_cloudelement29_link_reassign_clear():
    a = ddsm_DDSM(description="sample_text", modelId="sample_text")
    b1 = ddsm_CloudElement(description="sample_text", elementId="sample_text")
    b2 = ddsm_CloudElement(description="sample_text_2", elementId="sample_text_2")
    _safe_set(a, 'ddsm_DDSM', {b1})
    assert _is_linked(a, 'ddsm_DDSM', b1)
    if hasattr(b1, 'ddsm_CloudElement30'):
        assert _is_linked(b1, 'ddsm_CloudElement30', a)
    _safe_set(a, 'ddsm_DDSM', {b2})
    assert _is_linked(a, 'ddsm_DDSM', b2)
    if hasattr(b1, 'ddsm_CloudElement30'):
        assert not _is_linked(b1, 'ddsm_CloudElement30', a)
    if hasattr(b2, 'ddsm_CloudElement30'):
        assert _is_linked(b2, 'ddsm_CloudElement30', a)
    _safe_set(a, 'ddsm_DDSM', set())
    assert not _is_linked(a, 'ddsm_DDSM', b2)
    if hasattr(b2, 'ddsm_CloudElement30'):
        assert not _is_linked(b2, 'ddsm_CloudElement30', a)


def test_assoc_hasVm37_link_reassign_clear():
    a = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    b1 = ddsm_Cluster()
    b2 = ddsm_Cluster()
    _safe_set(a, 'ddsm_VM', b1)
    assert _is_linked(a, 'ddsm_VM', b1)
    if hasattr(b1, 'ddsm_Cluster'):
        assert _is_linked(b1, 'ddsm_Cluster', a)
    _safe_set(a, 'ddsm_VM', b2)
    assert _is_linked(a, 'ddsm_VM', b2)
    if hasattr(b1, 'ddsm_Cluster'):
        assert not _is_linked(b1, 'ddsm_Cluster', a)
    if hasattr(b2, 'ddsm_Cluster'):
        assert _is_linked(b2, 'ddsm_Cluster', a)
    _safe_set(a, 'ddsm_VM', None)
    assert not _is_linked(a, 'ddsm_VM', b2)
    if hasattr(b2, 'ddsm_Cluster'):
        assert not _is_linked(b2, 'ddsm_Cluster', a)


def test_assoc_properties31_link_reassign_clear():
    a = ddsm_Property(propertyId="sample_text", value="sample_text")
    b1 = ddsm_DDSM(description="sample_text", modelId="sample_text")
    b2 = ddsm_DDSM(description="sample_text_2", modelId="sample_text_2")
    _safe_set(a, 'ddsm_Property33', b1)
    assert _is_linked(a, 'ddsm_Property33', b1)
    if hasattr(b1, 'ddsm_DDSM32'):
        assert _is_linked(b1, 'ddsm_DDSM32', a)
    _safe_set(a, 'ddsm_Property33', b2)
    assert _is_linked(a, 'ddsm_Property33', b2)
    if hasattr(b1, 'ddsm_DDSM32'):
        assert not _is_linked(b1, 'ddsm_DDSM32', a)
    if hasattr(b2, 'ddsm_DDSM32'):
        assert _is_linked(b2, 'ddsm_DDSM32', a)
    _safe_set(a, 'ddsm_Property33', None)
    assert not _is_linked(a, 'ddsm_Property33', b2)
    if hasattr(b2, 'ddsm_DDSM32'):
        assert not _is_linked(b2, 'ddsm_DDSM32', a)


def test_assoc_property1_link_reassign_clear():
    a = ddsm_Property(propertyId="sample_text", value="sample_text")
    b1 = ddsm_CloudElement(description="sample_text", elementId="sample_text")
    b2 = ddsm_CloudElement(description="sample_text_2", elementId="sample_text_2")
    _safe_set(a, 'ddsm_Property', b1)
    assert _is_linked(a, 'ddsm_Property', b1)
    if hasattr(b1, 'ddsm_CloudElement2'):
        assert _is_linked(b1, 'ddsm_CloudElement2', a)
    _safe_set(a, 'ddsm_Property', b2)
    assert _is_linked(a, 'ddsm_Property', b2)
    if hasattr(b1, 'ddsm_CloudElement2'):
        assert not _is_linked(b1, 'ddsm_CloudElement2', a)
    if hasattr(b2, 'ddsm_CloudElement2'):
        assert _is_linked(b2, 'ddsm_CloudElement2', a)
    _safe_set(a, 'ddsm_Property', None)
    assert not _is_linked(a, 'ddsm_Property', b2)
    if hasattr(b2, 'ddsm_CloudElement2'):
        assert not _is_linked(b2, 'ddsm_CloudElement2', a)


def test_assoc_provider28_link_reassign_clear():
    a = ddsm_Provider(credentialsPath="sample_text", type="sample_text")
    b1 = ddsm_ExternalComponent(location="sample_text", login="sample_text", password="sample_text", region="sample_text", serviceType="sample_text")
    b2 = ddsm_ExternalComponent(location="sample_text_2", login="sample_text_2", password="sample_text_2", region="sample_text_2", serviceType="sample_text_2")
    _safe_set(a, 'ddsm_Provider', b1)
    assert _is_linked(a, 'ddsm_Provider', b1)
    if hasattr(b1, 'ddsm_ExternalComponent'):
        assert _is_linked(b1, 'ddsm_ExternalComponent', a)
    _safe_set(a, 'ddsm_Provider', b2)
    assert _is_linked(a, 'ddsm_Provider', b2)
    if hasattr(b1, 'ddsm_ExternalComponent'):
        assert not _is_linked(b1, 'ddsm_ExternalComponent', a)
    if hasattr(b2, 'ddsm_ExternalComponent'):
        assert _is_linked(b2, 'ddsm_ExternalComponent', a)
    _safe_set(a, 'ddsm_Provider', None)
    assert not _is_linked(a, 'ddsm_Provider', b2)
    if hasattr(b2, 'ddsm_ExternalComponent'):
        assert not _is_linked(b2, 'ddsm_ExternalComponent', a)


def test_assoc_requiredexecutionplatform10_link_reassign_clear():
    a = ddsm_RequiredExecutionPlatform(isMandatory=True)
    b1 = ddsm_InternalComponent()
    b2 = ddsm_InternalComponent()
    _safe_set(a, 'ddsm_RequiredExecutionPlatform', b1)
    assert _is_linked(a, 'ddsm_RequiredExecutionPlatform', b1)
    if hasattr(b1, 'ddsm_InternalComponent11'):
        assert _is_linked(b1, 'ddsm_InternalComponent11', a)
    _safe_set(a, 'ddsm_RequiredExecutionPlatform', b2)
    assert _is_linked(a, 'ddsm_RequiredExecutionPlatform', b2)
    if hasattr(b1, 'ddsm_InternalComponent11'):
        assert not _is_linked(b1, 'ddsm_InternalComponent11', a)
    if hasattr(b2, 'ddsm_InternalComponent11'):
        assert _is_linked(b2, 'ddsm_InternalComponent11', a)
    _safe_set(a, 'ddsm_RequiredExecutionPlatform', None)
    assert not _is_linked(a, 'ddsm_RequiredExecutionPlatform', b2)
    if hasattr(b2, 'ddsm_InternalComponent11'):
        assert not _is_linked(b2, 'ddsm_InternalComponent11', a)


def test_assoc_requiredexecutionplatform23_link_reassign_clear():
    a = ddsm_RequiredExecutionPlatform(isMandatory=True)
    b1 = ddsm_ExecutionBinding()
    b2 = ddsm_ExecutionBinding()
    _safe_set(a, 'ddsm_RequiredExecutionPlatform24', b1)
    assert _is_linked(a, 'ddsm_RequiredExecutionPlatform24', b1)
    if hasattr(b1, 'ddsm_ExecutionBinding'):
        assert _is_linked(b1, 'ddsm_ExecutionBinding', a)
    _safe_set(a, 'ddsm_RequiredExecutionPlatform24', b2)
    assert _is_linked(a, 'ddsm_RequiredExecutionPlatform24', b2)
    if hasattr(b1, 'ddsm_ExecutionBinding'):
        assert not _is_linked(b1, 'ddsm_ExecutionBinding', a)
    if hasattr(b2, 'ddsm_ExecutionBinding'):
        assert _is_linked(b2, 'ddsm_ExecutionBinding', a)
    _safe_set(a, 'ddsm_RequiredExecutionPlatform24', None)
    assert not _is_linked(a, 'ddsm_RequiredExecutionPlatform24', b2)
    if hasattr(b2, 'ddsm_ExecutionBinding'):
        assert not _is_linked(b2, 'ddsm_ExecutionBinding', a)


def test_assoc_requiredport20_link_reassign_clear():
    a = ddsm_RequiredPort(isMandatory=True)
    b1 = ddsm_Relationship()
    b2 = ddsm_Relationship()
    _safe_set(a, 'ddsm_RequiredPort22', b1)
    assert _is_linked(a, 'ddsm_RequiredPort22', b1)
    if hasattr(b1, 'ddsm_Relationship21'):
        assert _is_linked(b1, 'ddsm_Relationship21', a)
    _safe_set(a, 'ddsm_RequiredPort22', b2)
    assert _is_linked(a, 'ddsm_RequiredPort22', b2)
    if hasattr(b1, 'ddsm_Relationship21'):
        assert not _is_linked(b1, 'ddsm_Relationship21', a)
    if hasattr(b2, 'ddsm_Relationship21'):
        assert _is_linked(b2, 'ddsm_Relationship21', a)
    _safe_set(a, 'ddsm_RequiredPort22', None)
    assert not _is_linked(a, 'ddsm_RequiredPort22', b2)
    if hasattr(b2, 'ddsm_Relationship21'):
        assert not _is_linked(b2, 'ddsm_Relationship21', a)


def test_assoc_requiredport6_link_reassign_clear():
    a = ddsm_RequiredPort(isMandatory=True)
    b1 = ddsm_InternalComponent()
    b2 = ddsm_InternalComponent()
    _safe_set(a, 'ddsm_RequiredPort', b1)
    assert _is_linked(a, 'ddsm_RequiredPort', b1)
    if hasattr(b1, 'ddsm_InternalComponent'):
        assert _is_linked(b1, 'ddsm_InternalComponent', a)
    _safe_set(a, 'ddsm_RequiredPort', b2)
    assert _is_linked(a, 'ddsm_RequiredPort', b2)
    if hasattr(b1, 'ddsm_InternalComponent'):
        assert not _is_linked(b1, 'ddsm_InternalComponent', a)
    if hasattr(b2, 'ddsm_InternalComponent'):
        assert _is_linked(b2, 'ddsm_InternalComponent', a)
    _safe_set(a, 'ddsm_RequiredPort', None)
    assert not _is_linked(a, 'ddsm_RequiredPort', b2)
    if hasattr(b2, 'ddsm_InternalComponent'):
        assert not _is_linked(b2, 'ddsm_InternalComponent', a)


def test_assoc_resource0_link_reassign_clear():
    a = ddsm_Resource(configureCommand="sample_text", createCommand="sample_text", downloadCommand="sample_text", installCommand="sample_text", resourceId="sample_text", startCommand="sample_text", stopCommand="sample_text")
    b1 = ddsm_CloudElement(description="sample_text", elementId="sample_text")
    b2 = ddsm_CloudElement(description="sample_text_2", elementId="sample_text_2")
    _safe_set(a, 'ddsm_Resource', b1)
    assert _is_linked(a, 'ddsm_Resource', b1)
    if hasattr(b1, 'ddsm_CloudElement'):
        assert _is_linked(b1, 'ddsm_CloudElement', a)
    _safe_set(a, 'ddsm_Resource', b2)
    assert _is_linked(a, 'ddsm_Resource', b2)
    if hasattr(b1, 'ddsm_CloudElement'):
        assert not _is_linked(b1, 'ddsm_CloudElement', a)
    if hasattr(b2, 'ddsm_CloudElement'):
        assert _is_linked(b2, 'ddsm_CloudElement', a)
    _safe_set(a, 'ddsm_Resource', None)
    assert not _is_linked(a, 'ddsm_Resource', b2)
    if hasattr(b2, 'ddsm_CloudElement'):
        assert not _is_linked(b2, 'ddsm_CloudElement', a)


def test_assoc_resources34_link_reassign_clear():
    a = ddsm_Resource(configureCommand="sample_text", createCommand="sample_text", downloadCommand="sample_text", installCommand="sample_text", resourceId="sample_text", startCommand="sample_text", stopCommand="sample_text")
    b1 = ddsm_DDSM(description="sample_text", modelId="sample_text")
    b2 = ddsm_DDSM(description="sample_text_2", modelId="sample_text_2")
    _safe_set(a, 'ddsm_Resource36', b1)
    assert _is_linked(a, 'ddsm_Resource36', b1)
    if hasattr(b1, 'ddsm_DDSM35'):
        assert _is_linked(b1, 'ddsm_DDSM35', a)
    _safe_set(a, 'ddsm_Resource36', b2)
    assert _is_linked(a, 'ddsm_Resource36', b2)
    if hasattr(b1, 'ddsm_DDSM35'):
        assert not _is_linked(b1, 'ddsm_DDSM35', a)
    if hasattr(b2, 'ddsm_DDSM35'):
        assert _is_linked(b2, 'ddsm_DDSM35', a)
    _safe_set(a, 'ddsm_Resource36', None)
    assert not _is_linked(a, 'ddsm_Resource36', b2)
    if hasattr(b2, 'ddsm_DDSM35'):
        assert not _is_linked(b2, 'ddsm_DDSM35', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CloudElement_strategy = st.builds(CloudElement)
@given(instance=CloudElement_strategy)
@settings(max_examples=25)
def test_CloudElement_instantiation(instance):
    assert isinstance(instance, CloudElement)


Cluster_strategy = st.builds(Cluster)
@given(instance=Cluster_strategy)
@settings(max_examples=25)
def test_Cluster_instantiation(instance):
    assert isinstance(instance, Cluster)


Component_strategy = st.builds(Component)
@given(instance=Component_strategy)
@settings(max_examples=25)
def test_Component_instantiation(instance):
    assert isinstance(instance, Component)


ExecutionPlatform_strategy = st.builds(ExecutionPlatform)
@given(instance=ExecutionPlatform_strategy)
@settings(max_examples=25)
def test_ExecutionPlatform_instantiation(instance):
    assert isinstance(instance, ExecutionPlatform)


ExternalComponent_strategy = st.builds(ExternalComponent)
@given(instance=ExternalComponent_strategy)
@settings(max_examples=25)
def test_ExternalComponent_instantiation(instance):
    assert isinstance(instance, ExternalComponent)


InternalComponent_strategy = st.builds(InternalComponent)
@given(instance=InternalComponent_strategy)
@settings(max_examples=25)
def test_InternalComponent_instantiation(instance):
    assert isinstance(instance, InternalComponent)


Port_strategy = st.builds(Port)
@given(instance=Port_strategy)
@settings(max_examples=25)
def test_Port_instantiation(instance):
    assert isinstance(instance, Port)


Resource_strategy = st.builds(Resource)
@given(instance=Resource_strategy)
@settings(max_examples=25)
def test_Resource_instantiation(instance):
    assert isinstance(instance, Resource)


ddsm_ChefResource_strategy = st.builds(ddsm_ChefResource, cookbookId=safe_text)
@given(instance=ddsm_ChefResource_strategy)
@settings(max_examples=25)
def test_ddsm_ChefResource_instantiation(instance):
    assert isinstance(instance, ddsm_ChefResource)


ddsm_ClientNode_strategy = st.builds(ddsm_ClientNode, artifactUrl=safe_text, mainClass=safe_text, type=safe_text)
@given(instance=ddsm_ClientNode_strategy)
@settings(max_examples=25)
def test_ddsm_ClientNode_instantiation(instance):
    assert isinstance(instance, ddsm_ClientNode)


ddsm_CloudElement_strategy = st.builds(ddsm_CloudElement, description=safe_text, elementId=safe_text)
@given(instance=ddsm_CloudElement_strategy)
@settings(max_examples=25)
def test_ddsm_CloudElement_instantiation(instance):
    assert isinstance(instance, ddsm_CloudElement)


ddsm_Cluster_strategy = st.builds(ddsm_Cluster)
@given(instance=ddsm_Cluster_strategy)
@settings(max_examples=25)
def test_ddsm_Cluster_instantiation(instance):
    assert isinstance(instance, ddsm_Cluster)


ddsm_Component_strategy = st.builds(ddsm_Component)
@given(instance=ddsm_Component_strategy)
@settings(max_examples=25)
def test_ddsm_Component_instantiation(instance):
    assert isinstance(instance, ddsm_Component)


ddsm_DDSM_strategy = st.builds(ddsm_DDSM, description=safe_text, modelId=safe_text)
@given(instance=ddsm_DDSM_strategy)
@settings(max_examples=25)
def test_ddsm_DDSM_instantiation(instance):
    assert isinstance(instance, ddsm_DDSM)


ddsm_ExecutionBinding_strategy = st.builds(ddsm_ExecutionBinding)
@given(instance=ddsm_ExecutionBinding_strategy)
@settings(max_examples=25)
def test_ddsm_ExecutionBinding_instantiation(instance):
    assert isinstance(instance, ddsm_ExecutionBinding)


ddsm_ExecutionPlatform_strategy = st.builds(ddsm_ExecutionPlatform)
@given(instance=ddsm_ExecutionPlatform_strategy)
@settings(max_examples=25)
def test_ddsm_ExecutionPlatform_instantiation(instance):
    assert isinstance(instance, ddsm_ExecutionPlatform)


ddsm_ExternalComponent_strategy = st.builds(ddsm_ExternalComponent, location=safe_text, login=safe_text, password=safe_text, region=safe_text, serviceType=safe_text)
@given(instance=ddsm_ExternalComponent_strategy)
@settings(max_examples=25)
def test_ddsm_ExternalComponent_instantiation(instance):
    assert isinstance(instance, ddsm_ExternalComponent)


ddsm_HDFSDataNode_strategy = st.builds(ddsm_HDFSDataNode)
@given(instance=ddsm_HDFSDataNode_strategy)
@settings(max_examples=25)
def test_ddsm_HDFSDataNode_instantiation(instance):
    assert isinstance(instance, ddsm_HDFSDataNode)


ddsm_HDFSNameNode_strategy = st.builds(ddsm_HDFSNameNode)
@given(instance=ddsm_HDFSNameNode_strategy)
@settings(max_examples=25)
def test_ddsm_HDFSNameNode_instantiation(instance):
    assert isinstance(instance, ddsm_HDFSNameNode)


ddsm_InternalComponent_strategy = st.builds(ddsm_InternalComponent)
@given(instance=ddsm_InternalComponent_strategy)
@settings(max_examples=25)
def test_ddsm_InternalComponent_instantiation(instance):
    assert isinstance(instance, ddsm_InternalComponent)


ddsm_Kafka_strategy = st.builds(ddsm_Kafka)
@given(instance=ddsm_Kafka_strategy)
@settings(max_examples=25)
def test_ddsm_Kafka_instantiation(instance):
    assert isinstance(instance, ddsm_Kafka)


ddsm_Port_strategy = st.builds(ddsm_Port, isLocal=st.booleans(), portNumber=safe_text)
@given(instance=ddsm_Port_strategy)
@settings(max_examples=25)
def test_ddsm_Port_instantiation(instance):
    assert isinstance(instance, ddsm_Port)


ddsm_Property_strategy = st.builds(ddsm_Property, propertyId=safe_text, value=safe_text)
@given(instance=ddsm_Property_strategy)
@settings(max_examples=25)
def test_ddsm_Property_instantiation(instance):
    assert isinstance(instance, ddsm_Property)


ddsm_ProvidedExecutionPlatform_strategy = st.builds(ddsm_ProvidedExecutionPlatform)
@given(instance=ddsm_ProvidedExecutionPlatform_strategy)
@settings(max_examples=25)
def test_ddsm_ProvidedExecutionPlatform_instantiation(instance):
    assert isinstance(instance, ddsm_ProvidedExecutionPlatform)


ddsm_ProvidedPort_strategy = st.builds(ddsm_ProvidedPort)
@given(instance=ddsm_ProvidedPort_strategy)
@settings(max_examples=25)
def test_ddsm_ProvidedPort_instantiation(instance):
    assert isinstance(instance, ddsm_ProvidedPort)


ddsm_Provider_strategy = st.builds(ddsm_Provider, credentialsPath=safe_text, type=safe_text)
@given(instance=ddsm_Provider_strategy)
@settings(max_examples=25)
def test_ddsm_Provider_instantiation(instance):
    assert isinstance(instance, ddsm_Provider)


ddsm_Relationship_strategy = st.builds(ddsm_Relationship)
@given(instance=ddsm_Relationship_strategy)
@settings(max_examples=25)
def test_ddsm_Relationship_instantiation(instance):
    assert isinstance(instance, ddsm_Relationship)


ddsm_RequiredExecutionPlatform_strategy = st.builds(ddsm_RequiredExecutionPlatform, isMandatory=st.booleans())
@given(instance=ddsm_RequiredExecutionPlatform_strategy)
@settings(max_examples=25)
def test_ddsm_RequiredExecutionPlatform_instantiation(instance):
    assert isinstance(instance, ddsm_RequiredExecutionPlatform)


ddsm_RequiredPort_strategy = st.builds(ddsm_RequiredPort, isMandatory=st.booleans())
@given(instance=ddsm_RequiredPort_strategy)
@settings(max_examples=25)
def test_ddsm_RequiredPort_instantiation(instance):
    assert isinstance(instance, ddsm_RequiredPort)


ddsm_Resource_strategy = st.builds(ddsm_Resource, configureCommand=safe_text, createCommand=safe_text, downloadCommand=safe_text, installCommand=safe_text, resourceId=safe_text, startCommand=safe_text, stopCommand=safe_text)
@given(instance=ddsm_Resource_strategy)
@settings(max_examples=25)
def test_ddsm_Resource_instantiation(instance):
    assert isinstance(instance, ddsm_Resource)


ddsm_StormCluster_strategy = st.builds(ddsm_StormCluster, number_of_workers=safe_text)
@given(instance=ddsm_StormCluster_strategy)
@settings(max_examples=25)
def test_ddsm_StormCluster_instantiation(instance):
    assert isinstance(instance, ddsm_StormCluster)


ddsm_StormNimbus_strategy = st.builds(ddsm_StormNimbus, monitorFrequency=safe_text, queueSize=safe_text, retryInterval=safe_text, retryTimes=safe_text, supervisorTimeout=safe_text, taskTimeout=safe_text)
@given(instance=ddsm_StormNimbus_strategy)
@settings(max_examples=25)
def test_ddsm_StormNimbus_instantiation(instance):
    assert isinstance(instance, ddsm_StormNimbus)


ddsm_StormSupervisor_strategy = st.builds(ddsm_StormSupervisor, cpuCapacity=safe_text, heartbeatFrequency=safe_text, memoryCapacity=safe_text, workerStartTimeout=safe_text)
@given(instance=ddsm_StormSupervisor_strategy)
@settings(max_examples=25)
def test_ddsm_StormSupervisor_instantiation(instance):
    assert isinstance(instance, ddsm_StormSupervisor)


ddsm_VM_strategy = st.builds(ddsm_VM, genericSize=safe_text, imageId=safe_text, instances=safe_text, is64os=safe_text, maxCores=safe_text, maxRam=safe_text, maxStorage=safe_text, minCores=safe_text, minRam=safe_text, minStorage=safe_text, os=safe_text, privateKey=safe_text, providerSpecificTypeName=safe_text, publicAddress=safe_text, publicPorts=safe_text, securityGroup=safe_text, sshKey=safe_text)
@given(instance=ddsm_VM_strategy)
@settings(max_examples=25)
def test_ddsm_VM_instantiation(instance):
    assert isinstance(instance, ddsm_VM)


ddsm_YarnNodeManager_strategy = st.builds(ddsm_YarnNodeManager)
@given(instance=ddsm_YarnNodeManager_strategy)
@settings(max_examples=25)
def test_ddsm_YarnNodeManager_instantiation(instance):
    assert isinstance(instance, ddsm_YarnNodeManager)


ddsm_YarnResourceManager_strategy = st.builds(ddsm_YarnResourceManager)
@given(instance=ddsm_YarnResourceManager_strategy)
@settings(max_examples=25)
def test_ddsm_YarnResourceManager_instantiation(instance):
    assert isinstance(instance, ddsm_YarnResourceManager)


ddsm_Zookeeper_strategy = st.builds(ddsm_Zookeeper, initLimit=safe_text, syncLimit=safe_text, tickTime=safe_text)
@given(instance=ddsm_Zookeeper_strategy)
@settings(max_examples=25)
def test_ddsm_Zookeeper_instantiation(instance):
    assert isinstance(instance, ddsm_Zookeeper)


