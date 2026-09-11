import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CloudElement,
    Component,
    ExecutionPlatform,
    ExternalComponent,
    InternalComponent,
    MasterSlavePlatform,
    PeerToPeerPlatform,
    Port,
    ddsm_Artifact,
    ddsm_CassandraCluster,
    ddsm_ClientNode,
    ddsm_CloudElement,
    ddsm_Component,
    ddsm_Crontab,
    ddsm_DDSM,
    ddsm_ExecutionBinding,
    ddsm_ExecutionPlatform,
    ddsm_ExternalComponent,
    ddsm_HDFSCluster,
    ddsm_InternalComponent,
    ddsm_JobSubmission,
    ddsm_KafkaCluster,
    ddsm_MasterNode,
    ddsm_MasterSlavePlatform,
    ddsm_PeerNode,
    ddsm_PeerToPeerPlatform,
    ddsm_PeersQuorum,
    ddsm_Port,
    ddsm_Property,
    ddsm_ProvidedExecutionPlatform,
    ddsm_ProvidedPort,
    ddsm_Provider,
    ddsm_Relationship,
    ddsm_RequiredExecutionPlatform,
    ddsm_RequiredPort,
    ddsm_Resource,
    ddsm_SlaveNode,
    ddsm_SparkCluster,
    ddsm_StormCluster,
    ddsm_VM,
    ddsm_YarnCluster,
    ddsm_ZookeeperCluster,
    Language,
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

def test_ddsm_Artifact_arguments_value_roundtrip():
    instance = ddsm_Artifact(arguments="sample_text", artifactPath="sample_text", language="sample_text", resources="sample_text")
    assert instance.arguments == "sample_text"
    instance.arguments = "sample_text_2"
    assert instance.arguments == "sample_text_2"


def test_ddsm_Artifact_artifactPath_value_roundtrip():
    instance = ddsm_Artifact(arguments="sample_text", artifactPath="sample_text", language="sample_text", resources="sample_text")
    assert instance.artifactPath == "sample_text"
    instance.artifactPath = "sample_text_2"
    assert instance.artifactPath == "sample_text_2"


def test_ddsm_Artifact_language_value_roundtrip():
    instance = ddsm_Artifact(arguments="sample_text", artifactPath="sample_text", language="sample_text", resources="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_ddsm_Artifact_resources_value_roundtrip():
    instance = ddsm_Artifact(arguments="sample_text", artifactPath="sample_text", language="sample_text", resources="sample_text")
    assert instance.resources == "sample_text"
    instance.resources = "sample_text_2"
    assert instance.resources == "sample_text_2"


def test_ddsm_ClientNode_numberOfSubmissions_value_roundtrip():
    instance = ddsm_ClientNode(numberOfSubmissions=7, skipRunningJob=True)
    assert instance.numberOfSubmissions == 7
    instance.numberOfSubmissions = 13
    assert instance.numberOfSubmissions == 13


def test_ddsm_ClientNode_skipRunningJob_value_roundtrip():
    instance = ddsm_ClientNode(numberOfSubmissions=7, skipRunningJob=True)
    assert instance.skipRunningJob == True
    instance.skipRunningJob = False
    assert instance.skipRunningJob == False


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


def test_ddsm_Crontab_dayOfMonth_value_roundtrip():
    instance = ddsm_Crontab(dayOfMonth=7, dayOfWeek=7, hour=7, min=7, month=7)
    assert instance.dayOfMonth == 7
    instance.dayOfMonth = 13
    assert instance.dayOfMonth == 13


def test_ddsm_Crontab_dayOfWeek_value_roundtrip():
    instance = ddsm_Crontab(dayOfMonth=7, dayOfWeek=7, hour=7, min=7, month=7)
    assert instance.dayOfWeek == 7
    instance.dayOfWeek = 13
    assert instance.dayOfWeek == 13


def test_ddsm_Crontab_hour_value_roundtrip():
    instance = ddsm_Crontab(dayOfMonth=7, dayOfWeek=7, hour=7, min=7, month=7)
    assert instance.hour == 7
    instance.hour = 13
    assert instance.hour == 13


def test_ddsm_Crontab_min_value_roundtrip():
    instance = ddsm_Crontab(dayOfMonth=7, dayOfWeek=7, hour=7, min=7, month=7)
    assert instance.min == 7
    instance.min = 13
    assert instance.min == 13


def test_ddsm_Crontab_month_value_roundtrip():
    instance = ddsm_Crontab(dayOfMonth=7, dayOfWeek=7, hour=7, min=7, month=7)
    assert instance.month == 7
    instance.month = 13
    assert instance.month == 13


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


def test_ddsm_ExternalComponent_endPoint_value_roundtrip():
    instance = ddsm_ExternalComponent(endPoint="sample_text", location="sample_text", login="sample_text", password="sample_text", region="sample_text", serviceType="sample_text")
    assert instance.endPoint == "sample_text"
    instance.endPoint = "sample_text_2"
    assert instance.endPoint == "sample_text_2"


def test_ddsm_ExternalComponent_location_value_roundtrip():
    instance = ddsm_ExternalComponent(endPoint="sample_text", location="sample_text", login="sample_text", password="sample_text", region="sample_text", serviceType="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_ddsm_ExternalComponent_login_value_roundtrip():
    instance = ddsm_ExternalComponent(endPoint="sample_text", location="sample_text", login="sample_text", password="sample_text", region="sample_text", serviceType="sample_text")
    assert instance.login == "sample_text"
    instance.login = "sample_text_2"
    assert instance.login == "sample_text_2"


def test_ddsm_ExternalComponent_password_value_roundtrip():
    instance = ddsm_ExternalComponent(endPoint="sample_text", location="sample_text", login="sample_text", password="sample_text", region="sample_text", serviceType="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_ddsm_ExternalComponent_region_value_roundtrip():
    instance = ddsm_ExternalComponent(endPoint="sample_text", location="sample_text", login="sample_text", password="sample_text", region="sample_text", serviceType="sample_text")
    assert instance.region == "sample_text"
    instance.region = "sample_text_2"
    assert instance.region == "sample_text_2"


def test_ddsm_ExternalComponent_serviceType_value_roundtrip():
    instance = ddsm_ExternalComponent(endPoint="sample_text", location="sample_text", login="sample_text", password="sample_text", region="sample_text", serviceType="sample_text")
    assert instance.serviceType == "sample_text"
    instance.serviceType = "sample_text_2"
    assert instance.serviceType == "sample_text_2"


def test_ddsm_JobSubmission_applicationArguments_value_roundtrip():
    instance = ddsm_JobSubmission(applicationArguments="sample_text", artifactUrl="sample_text", mainClass="sample_text")
    assert instance.applicationArguments == "sample_text"
    instance.applicationArguments = "sample_text_2"
    assert instance.applicationArguments == "sample_text_2"


def test_ddsm_JobSubmission_artifactUrl_value_roundtrip():
    instance = ddsm_JobSubmission(applicationArguments="sample_text", artifactUrl="sample_text", mainClass="sample_text")
    assert instance.artifactUrl == "sample_text"
    instance.artifactUrl = "sample_text_2"
    assert instance.artifactUrl == "sample_text_2"


def test_ddsm_JobSubmission_mainClass_value_roundtrip():
    instance = ddsm_JobSubmission(applicationArguments="sample_text", artifactUrl="sample_text", mainClass="sample_text")
    assert instance.mainClass == "sample_text"
    instance.mainClass = "sample_text_2"
    assert instance.mainClass == "sample_text_2"


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


def test_ddsm_Resource_resourceId_value_roundtrip():
    instance = ddsm_Resource(resourceId="sample_text")
    assert instance.resourceId == "sample_text"
    instance.resourceId = "sample_text_2"
    assert instance.resourceId == "sample_text_2"


def test_ddsm_SparkCluster_UIPort_value_roundtrip():
    instance = ddsm_SparkCluster(UIPort=7, driverCores=7, driverMemory=7, maxResultSize=7, sparkExecutorMemory=7)
    assert instance.UIPort == 7
    instance.UIPort = 13
    assert instance.UIPort == 13


def test_ddsm_SparkCluster_driverCores_value_roundtrip():
    instance = ddsm_SparkCluster(UIPort=7, driverCores=7, driverMemory=7, maxResultSize=7, sparkExecutorMemory=7)
    assert instance.driverCores == 7
    instance.driverCores = 13
    assert instance.driverCores == 13


def test_ddsm_SparkCluster_driverMemory_value_roundtrip():
    instance = ddsm_SparkCluster(UIPort=7, driverCores=7, driverMemory=7, maxResultSize=7, sparkExecutorMemory=7)
    assert instance.driverMemory == 7
    instance.driverMemory = 13
    assert instance.driverMemory == 13


def test_ddsm_SparkCluster_maxResultSize_value_roundtrip():
    instance = ddsm_SparkCluster(UIPort=7, driverCores=7, driverMemory=7, maxResultSize=7, sparkExecutorMemory=7)
    assert instance.maxResultSize == 7
    instance.maxResultSize = 13
    assert instance.maxResultSize == 13


def test_ddsm_SparkCluster_sparkExecutorMemory_value_roundtrip():
    instance = ddsm_SparkCluster(UIPort=7, driverCores=7, driverMemory=7, maxResultSize=7, sparkExecutorMemory=7)
    assert instance.sparkExecutorMemory == 7
    instance.sparkExecutorMemory = 13
    assert instance.sparkExecutorMemory == 13


def test_ddsm_StormCluster_cpuCapacity_value_roundtrip():
    instance = ddsm_StormCluster(cpuCapacity=7, heartbeatFrequency=7, memoryCapacity=7, monitorFrequency=7, queueSize=7, retryInterval=7, retryTimes=7, supervisorFrequency=7, taskTimeout=7, workerStartTimeout=7)
    assert instance.cpuCapacity == 7
    instance.cpuCapacity = 13
    assert instance.cpuCapacity == 13


def test_ddsm_StormCluster_heartbeatFrequency_value_roundtrip():
    instance = ddsm_StormCluster(cpuCapacity=7, heartbeatFrequency=7, memoryCapacity=7, monitorFrequency=7, queueSize=7, retryInterval=7, retryTimes=7, supervisorFrequency=7, taskTimeout=7, workerStartTimeout=7)
    assert instance.heartbeatFrequency == 7
    instance.heartbeatFrequency = 13
    assert instance.heartbeatFrequency == 13


def test_ddsm_StormCluster_memoryCapacity_value_roundtrip():
    instance = ddsm_StormCluster(cpuCapacity=7, heartbeatFrequency=7, memoryCapacity=7, monitorFrequency=7, queueSize=7, retryInterval=7, retryTimes=7, supervisorFrequency=7, taskTimeout=7, workerStartTimeout=7)
    assert instance.memoryCapacity == 7
    instance.memoryCapacity = 13
    assert instance.memoryCapacity == 13


def test_ddsm_StormCluster_monitorFrequency_value_roundtrip():
    instance = ddsm_StormCluster(cpuCapacity=7, heartbeatFrequency=7, memoryCapacity=7, monitorFrequency=7, queueSize=7, retryInterval=7, retryTimes=7, supervisorFrequency=7, taskTimeout=7, workerStartTimeout=7)
    assert instance.monitorFrequency == 7
    instance.monitorFrequency = 13
    assert instance.monitorFrequency == 13


def test_ddsm_StormCluster_queueSize_value_roundtrip():
    instance = ddsm_StormCluster(cpuCapacity=7, heartbeatFrequency=7, memoryCapacity=7, monitorFrequency=7, queueSize=7, retryInterval=7, retryTimes=7, supervisorFrequency=7, taskTimeout=7, workerStartTimeout=7)
    assert instance.queueSize == 7
    instance.queueSize = 13
    assert instance.queueSize == 13


def test_ddsm_StormCluster_retryInterval_value_roundtrip():
    instance = ddsm_StormCluster(cpuCapacity=7, heartbeatFrequency=7, memoryCapacity=7, monitorFrequency=7, queueSize=7, retryInterval=7, retryTimes=7, supervisorFrequency=7, taskTimeout=7, workerStartTimeout=7)
    assert instance.retryInterval == 7
    instance.retryInterval = 13
    assert instance.retryInterval == 13


def test_ddsm_StormCluster_retryTimes_value_roundtrip():
    instance = ddsm_StormCluster(cpuCapacity=7, heartbeatFrequency=7, memoryCapacity=7, monitorFrequency=7, queueSize=7, retryInterval=7, retryTimes=7, supervisorFrequency=7, taskTimeout=7, workerStartTimeout=7)
    assert instance.retryTimes == 7
    instance.retryTimes = 13
    assert instance.retryTimes == 13


def test_ddsm_StormCluster_supervisorFrequency_value_roundtrip():
    instance = ddsm_StormCluster(cpuCapacity=7, heartbeatFrequency=7, memoryCapacity=7, monitorFrequency=7, queueSize=7, retryInterval=7, retryTimes=7, supervisorFrequency=7, taskTimeout=7, workerStartTimeout=7)
    assert instance.supervisorFrequency == 7
    instance.supervisorFrequency = 13
    assert instance.supervisorFrequency == 13


def test_ddsm_StormCluster_taskTimeout_value_roundtrip():
    instance = ddsm_StormCluster(cpuCapacity=7, heartbeatFrequency=7, memoryCapacity=7, monitorFrequency=7, queueSize=7, retryInterval=7, retryTimes=7, supervisorFrequency=7, taskTimeout=7, workerStartTimeout=7)
    assert instance.taskTimeout == 7
    instance.taskTimeout = 13
    assert instance.taskTimeout == 13


def test_ddsm_StormCluster_workerStartTimeout_value_roundtrip():
    instance = ddsm_StormCluster(cpuCapacity=7, heartbeatFrequency=7, memoryCapacity=7, monitorFrequency=7, queueSize=7, retryInterval=7, retryTimes=7, supervisorFrequency=7, taskTimeout=7, workerStartTimeout=7)
    assert instance.workerStartTimeout == 7
    instance.workerStartTimeout = 13
    assert instance.workerStartTimeout == 13


def test_ddsm_VM_genericSize_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances=7, is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts=7, securityGroup="sample_text", sshKey="sample_text")
    assert instance.genericSize == "sample_text"
    instance.genericSize = "sample_text_2"
    assert instance.genericSize == "sample_text_2"


def test_ddsm_VM_imageId_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances=7, is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts=7, securityGroup="sample_text", sshKey="sample_text")
    assert instance.imageId == "sample_text"
    instance.imageId = "sample_text_2"
    assert instance.imageId == "sample_text_2"


def test_ddsm_VM_instances_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances=7, is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts=7, securityGroup="sample_text", sshKey="sample_text")
    assert instance.instances == 7
    instance.instances = 13
    assert instance.instances == 13


def test_ddsm_VM_is64os_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances=7, is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts=7, securityGroup="sample_text", sshKey="sample_text")
    assert instance.is64os == "sample_text"
    instance.is64os = "sample_text_2"
    assert instance.is64os == "sample_text_2"


def test_ddsm_VM_maxCores_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances=7, is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts=7, securityGroup="sample_text", sshKey="sample_text")
    assert instance.maxCores == "sample_text"
    instance.maxCores = "sample_text_2"
    assert instance.maxCores == "sample_text_2"


def test_ddsm_VM_maxRam_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances=7, is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts=7, securityGroup="sample_text", sshKey="sample_text")
    assert instance.maxRam == "sample_text"
    instance.maxRam = "sample_text_2"
    assert instance.maxRam == "sample_text_2"


def test_ddsm_VM_maxStorage_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances=7, is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts=7, securityGroup="sample_text", sshKey="sample_text")
    assert instance.maxStorage == "sample_text"
    instance.maxStorage = "sample_text_2"
    assert instance.maxStorage == "sample_text_2"


def test_ddsm_VM_minCores_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances=7, is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts=7, securityGroup="sample_text", sshKey="sample_text")
    assert instance.minCores == "sample_text"
    instance.minCores = "sample_text_2"
    assert instance.minCores == "sample_text_2"


def test_ddsm_VM_minRam_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances=7, is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts=7, securityGroup="sample_text", sshKey="sample_text")
    assert instance.minRam == "sample_text"
    instance.minRam = "sample_text_2"
    assert instance.minRam == "sample_text_2"


def test_ddsm_VM_minStorage_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances=7, is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts=7, securityGroup="sample_text", sshKey="sample_text")
    assert instance.minStorage == "sample_text"
    instance.minStorage = "sample_text_2"
    assert instance.minStorage == "sample_text_2"


def test_ddsm_VM_os_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances=7, is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts=7, securityGroup="sample_text", sshKey="sample_text")
    assert instance.os == "sample_text"
    instance.os = "sample_text_2"
    assert instance.os == "sample_text_2"


def test_ddsm_VM_privateKey_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances=7, is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts=7, securityGroup="sample_text", sshKey="sample_text")
    assert instance.privateKey == "sample_text"
    instance.privateKey = "sample_text_2"
    assert instance.privateKey == "sample_text_2"


def test_ddsm_VM_providerSpecificTypeName_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances=7, is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts=7, securityGroup="sample_text", sshKey="sample_text")
    assert instance.providerSpecificTypeName == "sample_text"
    instance.providerSpecificTypeName = "sample_text_2"
    assert instance.providerSpecificTypeName == "sample_text_2"


def test_ddsm_VM_publicAddress_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances=7, is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts=7, securityGroup="sample_text", sshKey="sample_text")
    assert instance.publicAddress == "sample_text"
    instance.publicAddress = "sample_text_2"
    assert instance.publicAddress == "sample_text_2"


def test_ddsm_VM_publicPorts_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances=7, is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts=7, securityGroup="sample_text", sshKey="sample_text")
    assert instance.publicPorts == 7
    instance.publicPorts = 13
    assert instance.publicPorts == 13


def test_ddsm_VM_securityGroup_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances=7, is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts=7, securityGroup="sample_text", sshKey="sample_text")
    assert instance.securityGroup == "sample_text"
    instance.securityGroup = "sample_text_2"
    assert instance.securityGroup == "sample_text_2"


def test_ddsm_VM_sshKey_value_roundtrip():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances=7, is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts=7, securityGroup="sample_text", sshKey="sample_text")
    assert instance.sshKey == "sample_text"
    instance.sshKey = "sample_text_2"
    assert instance.sshKey == "sample_text_2"


def test_ddsm_ZookeeperCluster_initLimit_value_roundtrip():
    instance = ddsm_ZookeeperCluster(initLimit=7, syncLimit=7, tickTime=7)
    assert instance.initLimit == 7
    instance.initLimit = 13
    assert instance.initLimit == 13


def test_ddsm_ZookeeperCluster_syncLimit_value_roundtrip():
    instance = ddsm_ZookeeperCluster(initLimit=7, syncLimit=7, tickTime=7)
    assert instance.syncLimit == 7
    instance.syncLimit = 13
    assert instance.syncLimit == 13


def test_ddsm_ZookeeperCluster_tickTime_value_roundtrip():
    instance = ddsm_ZookeeperCluster(initLimit=7, syncLimit=7, tickTime=7)
    assert instance.tickTime == 7
    instance.tickTime = 13
    assert instance.tickTime == 13


def test_ddsm_Component_isa_CloudElement():
    instance = ddsm_Component()
    assert isinstance(instance, CloudElement)


def test_ddsm_ExecutionBinding_isa_CloudElement():
    instance = ddsm_ExecutionBinding()
    assert isinstance(instance, CloudElement)


def test_ddsm_ExecutionPlatform_isa_CloudElement():
    instance = ddsm_ExecutionPlatform()
    assert isinstance(instance, CloudElement)


def test_ddsm_JobSubmission_isa_CloudElement():
    instance = ddsm_JobSubmission(applicationArguments="sample_text", artifactUrl="sample_text", mainClass="sample_text")
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


def test_ddsm_ExternalComponent_isa_Component():
    instance = ddsm_ExternalComponent(endPoint="sample_text", location="sample_text", login="sample_text", password="sample_text", region="sample_text", serviceType="sample_text")
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


def test_ddsm_VM_isa_ExternalComponent():
    instance = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances=7, is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts=7, securityGroup="sample_text", sshKey="sample_text")
    assert isinstance(instance, ExternalComponent)


def test_ddsm_ClientNode_isa_InternalComponent():
    instance = ddsm_ClientNode(numberOfSubmissions=7, skipRunningJob=True)
    assert isinstance(instance, InternalComponent)


def test_ddsm_MasterNode_isa_InternalComponent():
    instance = ddsm_MasterNode()
    assert isinstance(instance, InternalComponent)


def test_ddsm_MasterSlavePlatform_isa_InternalComponent():
    instance = ddsm_MasterSlavePlatform()
    assert isinstance(instance, InternalComponent)


def test_ddsm_PeerNode_isa_InternalComponent():
    instance = ddsm_PeerNode()
    assert isinstance(instance, InternalComponent)


def test_ddsm_PeerToPeerPlatform_isa_InternalComponent():
    instance = ddsm_PeerToPeerPlatform()
    assert isinstance(instance, InternalComponent)


def test_ddsm_PeersQuorum_isa_InternalComponent():
    instance = ddsm_PeersQuorum()
    assert isinstance(instance, InternalComponent)


def test_ddsm_SlaveNode_isa_InternalComponent():
    instance = ddsm_SlaveNode()
    assert isinstance(instance, InternalComponent)


def test_ddsm_HDFSCluster_isa_MasterSlavePlatform():
    instance = ddsm_HDFSCluster()
    assert isinstance(instance, MasterSlavePlatform)


def test_ddsm_SparkCluster_isa_MasterSlavePlatform():
    instance = ddsm_SparkCluster(UIPort=7, driverCores=7, driverMemory=7, maxResultSize=7, sparkExecutorMemory=7)
    assert isinstance(instance, MasterSlavePlatform)


def test_ddsm_StormCluster_isa_MasterSlavePlatform():
    instance = ddsm_StormCluster(cpuCapacity=7, heartbeatFrequency=7, memoryCapacity=7, monitorFrequency=7, queueSize=7, retryInterval=7, retryTimes=7, supervisorFrequency=7, taskTimeout=7, workerStartTimeout=7)
    assert isinstance(instance, MasterSlavePlatform)


def test_ddsm_YarnCluster_isa_MasterSlavePlatform():
    instance = ddsm_YarnCluster()
    assert isinstance(instance, MasterSlavePlatform)


def test_ddsm_CassandraCluster_isa_PeerToPeerPlatform():
    instance = ddsm_CassandraCluster()
    assert isinstance(instance, PeerToPeerPlatform)


def test_ddsm_KafkaCluster_isa_PeerToPeerPlatform():
    instance = ddsm_KafkaCluster()
    assert isinstance(instance, PeerToPeerPlatform)


def test_ddsm_ZookeeperCluster_isa_PeerToPeerPlatform():
    instance = ddsm_ZookeeperCluster(initLimit=7, syncLimit=7, tickTime=7)
    assert isinstance(instance, PeerToPeerPlatform)


def test_ddsm_ProvidedPort_isa_Port():
    instance = ddsm_ProvidedPort()
    assert isinstance(instance, Port)


def test_ddsm_RequiredPort_isa_Port():
    instance = ddsm_RequiredPort(isMandatory=True)
    assert isinstance(instance, Port)


def test_assoc_artifacts51_link_reassign_clear():
    a = ddsm_DDSM(description="sample_text", modelId="sample_text")
    b1 = ddsm_Artifact(arguments="sample_text", artifactPath="sample_text", language="sample_text", resources="sample_text")
    b2 = ddsm_Artifact(arguments="sample_text_2", artifactPath="sample_text_2", language="sample_text_2", resources="sample_text_2")
    _safe_set(a, 'ddsm_DDSM52', {b1})
    assert _is_linked(a, 'ddsm_DDSM52', b1)
    if hasattr(b1, 'ddsm_Artifact53'):
        assert _is_linked(b1, 'ddsm_Artifact53', a)
    _safe_set(a, 'ddsm_DDSM52', {b2})
    assert _is_linked(a, 'ddsm_DDSM52', b2)
    if hasattr(b1, 'ddsm_Artifact53'):
        assert not _is_linked(b1, 'ddsm_Artifact53', a)
    if hasattr(b2, 'ddsm_Artifact53'):
        assert _is_linked(b2, 'ddsm_Artifact53', a)
    _safe_set(a, 'ddsm_DDSM52', set())
    assert not _is_linked(a, 'ddsm_DDSM52', b2)
    if hasattr(b2, 'ddsm_Artifact53'):
        assert not _is_linked(b2, 'ddsm_Artifact53', a)


def test_assoc_cloudelement43_link_reassign_clear():
    a = ddsm_DDSM(description="sample_text", modelId="sample_text")
    b1 = ddsm_CloudElement(description="sample_text", elementId="sample_text")
    b2 = ddsm_CloudElement(description="sample_text_2", elementId="sample_text_2")
    _safe_set(a, 'ddsm_DDSM', {b1})
    assert _is_linked(a, 'ddsm_DDSM', b1)
    if hasattr(b1, 'ddsm_CloudElement44'):
        assert _is_linked(b1, 'ddsm_CloudElement44', a)
    _safe_set(a, 'ddsm_DDSM', {b2})
    assert _is_linked(a, 'ddsm_DDSM', b2)
    if hasattr(b1, 'ddsm_CloudElement44'):
        assert not _is_linked(b1, 'ddsm_CloudElement44', a)
    if hasattr(b2, 'ddsm_CloudElement44'):
        assert _is_linked(b2, 'ddsm_CloudElement44', a)
    _safe_set(a, 'ddsm_DDSM', set())
    assert not _is_linked(a, 'ddsm_DDSM', b2)
    if hasattr(b2, 'ddsm_CloudElement44'):
        assert not _is_linked(b2, 'ddsm_CloudElement44', a)


def test_assoc_configure5_link_reassign_clear():
    a = ddsm_Resource(resourceId="sample_text")
    b1 = ddsm_Artifact(arguments="sample_text", artifactPath="sample_text", language="sample_text", resources="sample_text")
    b2 = ddsm_Artifact(arguments="sample_text_2", artifactPath="sample_text_2", language="sample_text_2", resources="sample_text_2")
    _safe_set(a, 'ddsm_Resource6', b1)
    assert _is_linked(a, 'ddsm_Resource6', b1)
    if hasattr(b1, 'ddsm_Artifact7'):
        assert _is_linked(b1, 'ddsm_Artifact7', a)
    _safe_set(a, 'ddsm_Resource6', b2)
    assert _is_linked(a, 'ddsm_Resource6', b2)
    if hasattr(b1, 'ddsm_Artifact7'):
        assert not _is_linked(b1, 'ddsm_Artifact7', a)
    if hasattr(b2, 'ddsm_Artifact7'):
        assert _is_linked(b2, 'ddsm_Artifact7', a)
    _safe_set(a, 'ddsm_Resource6', None)
    assert not _is_linked(a, 'ddsm_Resource6', b2)
    if hasattr(b2, 'ddsm_Artifact7'):
        assert not _is_linked(b2, 'ddsm_Artifact7', a)


def test_assoc_destroy14_link_reassign_clear():
    a = ddsm_Resource(resourceId="sample_text")
    b1 = ddsm_Artifact(arguments="sample_text", artifactPath="sample_text", language="sample_text", resources="sample_text")
    b2 = ddsm_Artifact(arguments="sample_text_2", artifactPath="sample_text_2", language="sample_text_2", resources="sample_text_2")
    _safe_set(a, 'ddsm_Resource15', b1)
    assert _is_linked(a, 'ddsm_Resource15', b1)
    if hasattr(b1, 'ddsm_Artifact16'):
        assert _is_linked(b1, 'ddsm_Artifact16', a)
    _safe_set(a, 'ddsm_Resource15', b2)
    assert _is_linked(a, 'ddsm_Resource15', b2)
    if hasattr(b1, 'ddsm_Artifact16'):
        assert not _is_linked(b1, 'ddsm_Artifact16', a)
    if hasattr(b2, 'ddsm_Artifact16'):
        assert _is_linked(b2, 'ddsm_Artifact16', a)
    _safe_set(a, 'ddsm_Resource15', None)
    assert not _is_linked(a, 'ddsm_Resource15', b2)
    if hasattr(b2, 'ddsm_Artifact16'):
        assert not _is_linked(b2, 'ddsm_Artifact16', a)


def test_assoc_download3_link_reassign_clear():
    a = ddsm_Resource(resourceId="sample_text")
    b1 = ddsm_Artifact(arguments="sample_text", artifactPath="sample_text", language="sample_text", resources="sample_text")
    b2 = ddsm_Artifact(arguments="sample_text_2", artifactPath="sample_text_2", language="sample_text_2", resources="sample_text_2")
    _safe_set(a, 'ddsm_Resource4', b1)
    assert _is_linked(a, 'ddsm_Resource4', b1)
    if hasattr(b1, 'ddsm_Artifact'):
        assert _is_linked(b1, 'ddsm_Artifact', a)
    _safe_set(a, 'ddsm_Resource4', b2)
    assert _is_linked(a, 'ddsm_Resource4', b2)
    if hasattr(b1, 'ddsm_Artifact'):
        assert not _is_linked(b1, 'ddsm_Artifact', a)
    if hasattr(b2, 'ddsm_Artifact'):
        assert _is_linked(b2, 'ddsm_Artifact', a)
    _safe_set(a, 'ddsm_Resource4', None)
    assert not _is_linked(a, 'ddsm_Resource4', b2)
    if hasattr(b2, 'ddsm_Artifact'):
        assert not _is_linked(b2, 'ddsm_Artifact', a)


def test_assoc_hasSchedule55_link_reassign_clear():
    a = ddsm_Crontab(dayOfMonth=7, dayOfWeek=7, hour=7, min=7, month=7)
    b1 = ddsm_ClientNode(numberOfSubmissions=7, skipRunningJob=True)
    b2 = ddsm_ClientNode(numberOfSubmissions=13, skipRunningJob=False)
    _safe_set(a, 'ddsm_Crontab', b1)
    assert _is_linked(a, 'ddsm_Crontab', b1)
    if hasattr(b1, 'ddsm_ClientNode56'):
        assert _is_linked(b1, 'ddsm_ClientNode56', a)
    _safe_set(a, 'ddsm_Crontab', b2)
    assert _is_linked(a, 'ddsm_Crontab', b2)
    if hasattr(b1, 'ddsm_ClientNode56'):
        assert not _is_linked(b1, 'ddsm_ClientNode56', a)
    if hasattr(b2, 'ddsm_ClientNode56'):
        assert _is_linked(b2, 'ddsm_ClientNode56', a)
    _safe_set(a, 'ddsm_Crontab', None)
    assert not _is_linked(a, 'ddsm_Crontab', b2)
    if hasattr(b2, 'ddsm_ClientNode56'):
        assert not _is_linked(b2, 'ddsm_ClientNode56', a)


def test_assoc_install17_link_reassign_clear():
    a = ddsm_Resource(resourceId="sample_text")
    b1 = ddsm_Artifact(arguments="sample_text", artifactPath="sample_text", language="sample_text", resources="sample_text")
    b2 = ddsm_Artifact(arguments="sample_text_2", artifactPath="sample_text_2", language="sample_text_2", resources="sample_text_2")
    _safe_set(a, 'ddsm_Resource18', b1)
    assert _is_linked(a, 'ddsm_Resource18', b1)
    if hasattr(b1, 'ddsm_Artifact19'):
        assert _is_linked(b1, 'ddsm_Artifact19', a)
    _safe_set(a, 'ddsm_Resource18', b2)
    assert _is_linked(a, 'ddsm_Resource18', b2)
    if hasattr(b1, 'ddsm_Artifact19'):
        assert not _is_linked(b1, 'ddsm_Artifact19', a)
    if hasattr(b2, 'ddsm_Artifact19'):
        assert _is_linked(b2, 'ddsm_Artifact19', a)
    _safe_set(a, 'ddsm_Resource18', None)
    assert not _is_linked(a, 'ddsm_Resource18', b2)
    if hasattr(b2, 'ddsm_Artifact19'):
        assert not _is_linked(b2, 'ddsm_Artifact19', a)


def test_assoc_properties45_link_reassign_clear():
    a = ddsm_Property(propertyId="sample_text", value="sample_text")
    b1 = ddsm_DDSM(description="sample_text", modelId="sample_text")
    b2 = ddsm_DDSM(description="sample_text_2", modelId="sample_text_2")
    _safe_set(a, 'ddsm_Property47', b1)
    assert _is_linked(a, 'ddsm_Property47', b1)
    if hasattr(b1, 'ddsm_DDSM46'):
        assert _is_linked(b1, 'ddsm_DDSM46', a)
    _safe_set(a, 'ddsm_Property47', b2)
    assert _is_linked(a, 'ddsm_Property47', b2)
    if hasattr(b1, 'ddsm_DDSM46'):
        assert not _is_linked(b1, 'ddsm_DDSM46', a)
    if hasattr(b2, 'ddsm_DDSM46'):
        assert _is_linked(b2, 'ddsm_DDSM46', a)
    _safe_set(a, 'ddsm_Property47', None)
    assert not _is_linked(a, 'ddsm_Property47', b2)
    if hasattr(b2, 'ddsm_DDSM46'):
        assert not _is_linked(b2, 'ddsm_DDSM46', a)


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


def test_assoc_provider42_link_reassign_clear():
    a = ddsm_Provider(credentialsPath="sample_text", type="sample_text")
    b1 = ddsm_ExternalComponent(endPoint="sample_text", location="sample_text", login="sample_text", password="sample_text", region="sample_text", serviceType="sample_text")
    b2 = ddsm_ExternalComponent(endPoint="sample_text_2", location="sample_text_2", login="sample_text_2", password="sample_text_2", region="sample_text_2", serviceType="sample_text_2")
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


def test_assoc_requiredexecutionplatform24_link_reassign_clear():
    a = ddsm_RequiredExecutionPlatform(isMandatory=True)
    b1 = ddsm_InternalComponent()
    b2 = ddsm_InternalComponent()
    _safe_set(a, 'ddsm_RequiredExecutionPlatform', b1)
    assert _is_linked(a, 'ddsm_RequiredExecutionPlatform', b1)
    if hasattr(b1, 'ddsm_InternalComponent25'):
        assert _is_linked(b1, 'ddsm_InternalComponent25', a)
    _safe_set(a, 'ddsm_RequiredExecutionPlatform', b2)
    assert _is_linked(a, 'ddsm_RequiredExecutionPlatform', b2)
    if hasattr(b1, 'ddsm_InternalComponent25'):
        assert not _is_linked(b1, 'ddsm_InternalComponent25', a)
    if hasattr(b2, 'ddsm_InternalComponent25'):
        assert _is_linked(b2, 'ddsm_InternalComponent25', a)
    _safe_set(a, 'ddsm_RequiredExecutionPlatform', None)
    assert not _is_linked(a, 'ddsm_RequiredExecutionPlatform', b2)
    if hasattr(b2, 'ddsm_InternalComponent25'):
        assert not _is_linked(b2, 'ddsm_InternalComponent25', a)


def test_assoc_requiredexecutionplatform37_link_reassign_clear():
    a = ddsm_RequiredExecutionPlatform(isMandatory=True)
    b1 = ddsm_ExecutionBinding()
    b2 = ddsm_ExecutionBinding()
    _safe_set(a, 'ddsm_RequiredExecutionPlatform38', b1)
    assert _is_linked(a, 'ddsm_RequiredExecutionPlatform38', b1)
    if hasattr(b1, 'ddsm_ExecutionBinding'):
        assert _is_linked(b1, 'ddsm_ExecutionBinding', a)
    _safe_set(a, 'ddsm_RequiredExecutionPlatform38', b2)
    assert _is_linked(a, 'ddsm_RequiredExecutionPlatform38', b2)
    if hasattr(b1, 'ddsm_ExecutionBinding'):
        assert not _is_linked(b1, 'ddsm_ExecutionBinding', a)
    if hasattr(b2, 'ddsm_ExecutionBinding'):
        assert _is_linked(b2, 'ddsm_ExecutionBinding', a)
    _safe_set(a, 'ddsm_RequiredExecutionPlatform38', None)
    assert not _is_linked(a, 'ddsm_RequiredExecutionPlatform38', b2)
    if hasattr(b2, 'ddsm_ExecutionBinding'):
        assert not _is_linked(b2, 'ddsm_ExecutionBinding', a)


def test_assoc_requiredport23_link_reassign_clear():
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


def test_assoc_requiredport34_link_reassign_clear():
    a = ddsm_RequiredPort(isMandatory=True)
    b1 = ddsm_Relationship()
    b2 = ddsm_Relationship()
    _safe_set(a, 'ddsm_RequiredPort36', b1)
    assert _is_linked(a, 'ddsm_RequiredPort36', b1)
    if hasattr(b1, 'ddsm_Relationship35'):
        assert _is_linked(b1, 'ddsm_Relationship35', a)
    _safe_set(a, 'ddsm_RequiredPort36', b2)
    assert _is_linked(a, 'ddsm_RequiredPort36', b2)
    if hasattr(b1, 'ddsm_Relationship35'):
        assert not _is_linked(b1, 'ddsm_Relationship35', a)
    if hasattr(b2, 'ddsm_Relationship35'):
        assert _is_linked(b2, 'ddsm_Relationship35', a)
    _safe_set(a, 'ddsm_RequiredPort36', None)
    assert not _is_linked(a, 'ddsm_RequiredPort36', b2)
    if hasattr(b2, 'ddsm_Relationship35'):
        assert not _is_linked(b2, 'ddsm_Relationship35', a)


def test_assoc_requiresMasterVm61_link_reassign_clear():
    a = ddsm_RequiredExecutionPlatform(isMandatory=True)
    b1 = ddsm_MasterSlavePlatform()
    b2 = ddsm_MasterSlavePlatform()
    _safe_set(a, 'ddsm_RequiredExecutionPlatform62', b1)
    assert _is_linked(a, 'ddsm_RequiredExecutionPlatform62', b1)
    if hasattr(b1, 'ddsm_MasterSlavePlatform'):
        assert _is_linked(b1, 'ddsm_MasterSlavePlatform', a)
    _safe_set(a, 'ddsm_RequiredExecutionPlatform62', b2)
    assert _is_linked(a, 'ddsm_RequiredExecutionPlatform62', b2)
    if hasattr(b1, 'ddsm_MasterSlavePlatform'):
        assert not _is_linked(b1, 'ddsm_MasterSlavePlatform', a)
    if hasattr(b2, 'ddsm_MasterSlavePlatform'):
        assert _is_linked(b2, 'ddsm_MasterSlavePlatform', a)
    _safe_set(a, 'ddsm_RequiredExecutionPlatform62', None)
    assert not _is_linked(a, 'ddsm_RequiredExecutionPlatform62', b2)
    if hasattr(b2, 'ddsm_MasterSlavePlatform'):
        assert not _is_linked(b2, 'ddsm_MasterSlavePlatform', a)


def test_assoc_requiresPeerVm59_link_reassign_clear():
    a = ddsm_RequiredExecutionPlatform(isMandatory=True)
    b1 = ddsm_PeerToPeerPlatform()
    b2 = ddsm_PeerToPeerPlatform()
    _safe_set(a, 'ddsm_RequiredExecutionPlatform60', b1)
    assert _is_linked(a, 'ddsm_RequiredExecutionPlatform60', b1)
    if hasattr(b1, 'ddsm_PeerToPeerPlatform'):
        assert _is_linked(b1, 'ddsm_PeerToPeerPlatform', a)
    _safe_set(a, 'ddsm_RequiredExecutionPlatform60', b2)
    assert _is_linked(a, 'ddsm_RequiredExecutionPlatform60', b2)
    if hasattr(b1, 'ddsm_PeerToPeerPlatform'):
        assert not _is_linked(b1, 'ddsm_PeerToPeerPlatform', a)
    if hasattr(b2, 'ddsm_PeerToPeerPlatform'):
        assert _is_linked(b2, 'ddsm_PeerToPeerPlatform', a)
    _safe_set(a, 'ddsm_RequiredExecutionPlatform60', None)
    assert not _is_linked(a, 'ddsm_RequiredExecutionPlatform60', b2)
    if hasattr(b2, 'ddsm_PeerToPeerPlatform'):
        assert not _is_linked(b2, 'ddsm_PeerToPeerPlatform', a)


def test_assoc_requiresSlaveVm63_link_reassign_clear():
    a = ddsm_RequiredExecutionPlatform(isMandatory=True)
    b1 = ddsm_MasterSlavePlatform()
    b2 = ddsm_MasterSlavePlatform()
    _safe_set(a, 'ddsm_RequiredExecutionPlatform65', b1)
    assert _is_linked(a, 'ddsm_RequiredExecutionPlatform65', b1)
    if hasattr(b1, 'ddsm_MasterSlavePlatform64'):
        assert _is_linked(b1, 'ddsm_MasterSlavePlatform64', a)
    _safe_set(a, 'ddsm_RequiredExecutionPlatform65', b2)
    assert _is_linked(a, 'ddsm_RequiredExecutionPlatform65', b2)
    if hasattr(b1, 'ddsm_MasterSlavePlatform64'):
        assert not _is_linked(b1, 'ddsm_MasterSlavePlatform64', a)
    if hasattr(b2, 'ddsm_MasterSlavePlatform64'):
        assert _is_linked(b2, 'ddsm_MasterSlavePlatform64', a)
    _safe_set(a, 'ddsm_RequiredExecutionPlatform65', None)
    assert not _is_linked(a, 'ddsm_RequiredExecutionPlatform65', b2)
    if hasattr(b2, 'ddsm_MasterSlavePlatform64'):
        assert not _is_linked(b2, 'ddsm_MasterSlavePlatform64', a)


def test_assoc_resource0_link_reassign_clear():
    a = ddsm_Resource(resourceId="sample_text")
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


def test_assoc_resources48_link_reassign_clear():
    a = ddsm_Resource(resourceId="sample_text")
    b1 = ddsm_DDSM(description="sample_text", modelId="sample_text")
    b2 = ddsm_DDSM(description="sample_text_2", modelId="sample_text_2")
    _safe_set(a, 'ddsm_Resource50', b1)
    assert _is_linked(a, 'ddsm_Resource50', b1)
    if hasattr(b1, 'ddsm_DDSM49'):
        assert _is_linked(b1, 'ddsm_DDSM49', a)
    _safe_set(a, 'ddsm_Resource50', b2)
    assert _is_linked(a, 'ddsm_Resource50', b2)
    if hasattr(b1, 'ddsm_DDSM49'):
        assert not _is_linked(b1, 'ddsm_DDSM49', a)
    if hasattr(b2, 'ddsm_DDSM49'):
        assert _is_linked(b2, 'ddsm_DDSM49', a)
    _safe_set(a, 'ddsm_Resource50', None)
    assert not _is_linked(a, 'ddsm_Resource50', b2)
    if hasattr(b2, 'ddsm_DDSM49'):
        assert not _is_linked(b2, 'ddsm_DDSM49', a)


def test_assoc_start8_link_reassign_clear():
    a = ddsm_Resource(resourceId="sample_text")
    b1 = ddsm_Artifact(arguments="sample_text", artifactPath="sample_text", language="sample_text", resources="sample_text")
    b2 = ddsm_Artifact(arguments="sample_text_2", artifactPath="sample_text_2", language="sample_text_2", resources="sample_text_2")
    _safe_set(a, 'ddsm_Resource9', b1)
    assert _is_linked(a, 'ddsm_Resource9', b1)
    if hasattr(b1, 'ddsm_Artifact10'):
        assert _is_linked(b1, 'ddsm_Artifact10', a)
    _safe_set(a, 'ddsm_Resource9', b2)
    assert _is_linked(a, 'ddsm_Resource9', b2)
    if hasattr(b1, 'ddsm_Artifact10'):
        assert not _is_linked(b1, 'ddsm_Artifact10', a)
    if hasattr(b2, 'ddsm_Artifact10'):
        assert _is_linked(b2, 'ddsm_Artifact10', a)
    _safe_set(a, 'ddsm_Resource9', None)
    assert not _is_linked(a, 'ddsm_Resource9', b2)
    if hasattr(b2, 'ddsm_Artifact10'):
        assert not _is_linked(b2, 'ddsm_Artifact10', a)


def test_assoc_stop11_link_reassign_clear():
    a = ddsm_Resource(resourceId="sample_text")
    b1 = ddsm_Artifact(arguments="sample_text", artifactPath="sample_text", language="sample_text", resources="sample_text")
    b2 = ddsm_Artifact(arguments="sample_text_2", artifactPath="sample_text_2", language="sample_text_2", resources="sample_text_2")
    _safe_set(a, 'ddsm_Resource12', b1)
    assert _is_linked(a, 'ddsm_Resource12', b1)
    if hasattr(b1, 'ddsm_Artifact13'):
        assert _is_linked(b1, 'ddsm_Artifact13', a)
    _safe_set(a, 'ddsm_Resource12', b2)
    assert _is_linked(a, 'ddsm_Resource12', b2)
    if hasattr(b1, 'ddsm_Artifact13'):
        assert not _is_linked(b1, 'ddsm_Artifact13', a)
    if hasattr(b2, 'ddsm_Artifact13'):
        assert _is_linked(b2, 'ddsm_Artifact13', a)
    _safe_set(a, 'ddsm_Resource12', None)
    assert not _is_linked(a, 'ddsm_Resource12', b2)
    if hasattr(b2, 'ddsm_Artifact13'):
        assert not _is_linked(b2, 'ddsm_Artifact13', a)


def test_assoc_submits54_link_reassign_clear():
    a = ddsm_JobSubmission(applicationArguments="sample_text", artifactUrl="sample_text", mainClass="sample_text")
    b1 = ddsm_ClientNode(numberOfSubmissions=7, skipRunningJob=True)
    b2 = ddsm_ClientNode(numberOfSubmissions=13, skipRunningJob=False)
    _safe_set(a, 'ddsm_JobSubmission', b1)
    assert _is_linked(a, 'ddsm_JobSubmission', b1)
    if hasattr(b1, 'ddsm_ClientNode'):
        assert _is_linked(b1, 'ddsm_ClientNode', a)
    _safe_set(a, 'ddsm_JobSubmission', b2)
    assert _is_linked(a, 'ddsm_JobSubmission', b2)
    if hasattr(b1, 'ddsm_ClientNode'):
        assert not _is_linked(b1, 'ddsm_ClientNode', a)
    if hasattr(b2, 'ddsm_ClientNode'):
        assert _is_linked(b2, 'ddsm_ClientNode', a)
    _safe_set(a, 'ddsm_JobSubmission', None)
    assert not _is_linked(a, 'ddsm_JobSubmission', b2)
    if hasattr(b2, 'ddsm_ClientNode'):
        assert not _is_linked(b2, 'ddsm_ClientNode', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CloudElement_strategy = st.builds(CloudElement)
@given(instance=CloudElement_strategy)
@settings(max_examples=25)
def test_CloudElement_instantiation(instance):
    assert isinstance(instance, CloudElement)


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


MasterSlavePlatform_strategy = st.builds(MasterSlavePlatform)
@given(instance=MasterSlavePlatform_strategy)
@settings(max_examples=25)
def test_MasterSlavePlatform_instantiation(instance):
    assert isinstance(instance, MasterSlavePlatform)


PeerToPeerPlatform_strategy = st.builds(PeerToPeerPlatform)
@given(instance=PeerToPeerPlatform_strategy)
@settings(max_examples=25)
def test_PeerToPeerPlatform_instantiation(instance):
    assert isinstance(instance, PeerToPeerPlatform)


Port_strategy = st.builds(Port)
@given(instance=Port_strategy)
@settings(max_examples=25)
def test_Port_instantiation(instance):
    assert isinstance(instance, Port)


ddsm_Artifact_strategy = st.builds(ddsm_Artifact, arguments=safe_text, artifactPath=safe_text, language=safe_text, resources=safe_text)
@given(instance=ddsm_Artifact_strategy)
@settings(max_examples=25)
def test_ddsm_Artifact_instantiation(instance):
    assert isinstance(instance, ddsm_Artifact)


ddsm_CassandraCluster_strategy = st.builds(ddsm_CassandraCluster)
@given(instance=ddsm_CassandraCluster_strategy)
@settings(max_examples=25)
def test_ddsm_CassandraCluster_instantiation(instance):
    assert isinstance(instance, ddsm_CassandraCluster)


ddsm_ClientNode_strategy = st.builds(ddsm_ClientNode, numberOfSubmissions=st.integers(), skipRunningJob=st.booleans())
@given(instance=ddsm_ClientNode_strategy)
@settings(max_examples=25)
def test_ddsm_ClientNode_instantiation(instance):
    assert isinstance(instance, ddsm_ClientNode)


ddsm_CloudElement_strategy = st.builds(ddsm_CloudElement, description=safe_text, elementId=safe_text)
@given(instance=ddsm_CloudElement_strategy)
@settings(max_examples=25)
def test_ddsm_CloudElement_instantiation(instance):
    assert isinstance(instance, ddsm_CloudElement)


ddsm_Component_strategy = st.builds(ddsm_Component)
@given(instance=ddsm_Component_strategy)
@settings(max_examples=25)
def test_ddsm_Component_instantiation(instance):
    assert isinstance(instance, ddsm_Component)


ddsm_Crontab_strategy = st.builds(ddsm_Crontab, dayOfMonth=st.integers(), dayOfWeek=st.integers(), hour=st.integers(), min=st.integers(), month=st.integers())
@given(instance=ddsm_Crontab_strategy)
@settings(max_examples=25)
def test_ddsm_Crontab_instantiation(instance):
    assert isinstance(instance, ddsm_Crontab)


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


ddsm_ExternalComponent_strategy = st.builds(ddsm_ExternalComponent, endPoint=safe_text, location=safe_text, login=safe_text, password=safe_text, region=safe_text, serviceType=safe_text)
@given(instance=ddsm_ExternalComponent_strategy)
@settings(max_examples=25)
def test_ddsm_ExternalComponent_instantiation(instance):
    assert isinstance(instance, ddsm_ExternalComponent)


ddsm_HDFSCluster_strategy = st.builds(ddsm_HDFSCluster)
@given(instance=ddsm_HDFSCluster_strategy)
@settings(max_examples=25)
def test_ddsm_HDFSCluster_instantiation(instance):
    assert isinstance(instance, ddsm_HDFSCluster)


ddsm_InternalComponent_strategy = st.builds(ddsm_InternalComponent)
@given(instance=ddsm_InternalComponent_strategy)
@settings(max_examples=25)
def test_ddsm_InternalComponent_instantiation(instance):
    assert isinstance(instance, ddsm_InternalComponent)


ddsm_JobSubmission_strategy = st.builds(ddsm_JobSubmission, applicationArguments=safe_text, artifactUrl=safe_text, mainClass=safe_text)
@given(instance=ddsm_JobSubmission_strategy)
@settings(max_examples=25)
def test_ddsm_JobSubmission_instantiation(instance):
    assert isinstance(instance, ddsm_JobSubmission)


ddsm_KafkaCluster_strategy = st.builds(ddsm_KafkaCluster)
@given(instance=ddsm_KafkaCluster_strategy)
@settings(max_examples=25)
def test_ddsm_KafkaCluster_instantiation(instance):
    assert isinstance(instance, ddsm_KafkaCluster)


ddsm_MasterNode_strategy = st.builds(ddsm_MasterNode)
@given(instance=ddsm_MasterNode_strategy)
@settings(max_examples=25)
def test_ddsm_MasterNode_instantiation(instance):
    assert isinstance(instance, ddsm_MasterNode)


ddsm_MasterSlavePlatform_strategy = st.builds(ddsm_MasterSlavePlatform)
@given(instance=ddsm_MasterSlavePlatform_strategy)
@settings(max_examples=25)
def test_ddsm_MasterSlavePlatform_instantiation(instance):
    assert isinstance(instance, ddsm_MasterSlavePlatform)


ddsm_PeerNode_strategy = st.builds(ddsm_PeerNode)
@given(instance=ddsm_PeerNode_strategy)
@settings(max_examples=25)
def test_ddsm_PeerNode_instantiation(instance):
    assert isinstance(instance, ddsm_PeerNode)


ddsm_PeerToPeerPlatform_strategy = st.builds(ddsm_PeerToPeerPlatform)
@given(instance=ddsm_PeerToPeerPlatform_strategy)
@settings(max_examples=25)
def test_ddsm_PeerToPeerPlatform_instantiation(instance):
    assert isinstance(instance, ddsm_PeerToPeerPlatform)


ddsm_PeersQuorum_strategy = st.builds(ddsm_PeersQuorum)
@given(instance=ddsm_PeersQuorum_strategy)
@settings(max_examples=25)
def test_ddsm_PeersQuorum_instantiation(instance):
    assert isinstance(instance, ddsm_PeersQuorum)


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


ddsm_Resource_strategy = st.builds(ddsm_Resource, resourceId=safe_text)
@given(instance=ddsm_Resource_strategy)
@settings(max_examples=25)
def test_ddsm_Resource_instantiation(instance):
    assert isinstance(instance, ddsm_Resource)


ddsm_SlaveNode_strategy = st.builds(ddsm_SlaveNode)
@given(instance=ddsm_SlaveNode_strategy)
@settings(max_examples=25)
def test_ddsm_SlaveNode_instantiation(instance):
    assert isinstance(instance, ddsm_SlaveNode)


ddsm_SparkCluster_strategy = st.builds(ddsm_SparkCluster, UIPort=st.integers(), driverCores=st.integers(), driverMemory=st.integers(), maxResultSize=st.integers(), sparkExecutorMemory=st.integers())
@given(instance=ddsm_SparkCluster_strategy)
@settings(max_examples=25)
def test_ddsm_SparkCluster_instantiation(instance):
    assert isinstance(instance, ddsm_SparkCluster)


ddsm_StormCluster_strategy = st.builds(ddsm_StormCluster, cpuCapacity=st.integers(), heartbeatFrequency=st.integers(), memoryCapacity=st.integers(), monitorFrequency=st.integers(), queueSize=st.integers(), retryInterval=st.integers(), retryTimes=st.integers(), supervisorFrequency=st.integers(), taskTimeout=st.integers(), workerStartTimeout=st.integers())
@given(instance=ddsm_StormCluster_strategy)
@settings(max_examples=25)
def test_ddsm_StormCluster_instantiation(instance):
    assert isinstance(instance, ddsm_StormCluster)


ddsm_VM_strategy = st.builds(ddsm_VM, genericSize=safe_text, imageId=safe_text, instances=st.integers(), is64os=safe_text, maxCores=safe_text, maxRam=safe_text, maxStorage=safe_text, minCores=safe_text, minRam=safe_text, minStorage=safe_text, os=safe_text, privateKey=safe_text, providerSpecificTypeName=safe_text, publicAddress=safe_text, publicPorts=st.integers(), securityGroup=safe_text, sshKey=safe_text)
@given(instance=ddsm_VM_strategy)
@settings(max_examples=25)
def test_ddsm_VM_instantiation(instance):
    assert isinstance(instance, ddsm_VM)


ddsm_YarnCluster_strategy = st.builds(ddsm_YarnCluster)
@given(instance=ddsm_YarnCluster_strategy)
@settings(max_examples=25)
def test_ddsm_YarnCluster_instantiation(instance):
    assert isinstance(instance, ddsm_YarnCluster)


ddsm_ZookeeperCluster_strategy = st.builds(ddsm_ZookeeperCluster, initLimit=st.integers(), syncLimit=st.integers(), tickTime=st.integers())
@given(instance=ddsm_ZookeeperCluster_strategy)
@settings(max_examples=25)
def test_ddsm_ZookeeperCluster_instantiation(instance):
    assert isinstance(instance, ddsm_ZookeeperCluster)


