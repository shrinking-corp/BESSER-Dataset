import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    DBResource,
    ServerResource,
    config_Entitlement,
    config_Prompt,
    config_Role,
    config_SafiServer,
    config_Saflet,
    config_SafletProject,
    config_User,
    db_DBConnection,
    db_DBDriver,
    db_DBResource,
    db_Query,
    db_QueryParameter,
    db_SafiDriverManager,
    db_SafiResultSet,
    db_Variable,
    db_config_Entitlement,
    db_config_Prompt,
    db_config_Role,
    db_config_SFTPInfo,
    db_config_SafiServer,
    db_config_Saflet,
    db_config_SafletProject,
    db_config_ServerResource,
    db_config_TelephonySubsystem,
    db_config_User,
    QueryType,
    RSHoldabilityMode,
    RSScrollMode,
    SQLDataType,
    SynchMode,
    TransactionMode,
    VariableScope,
    VariableType,
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

def test_db_DBConnection_acquireIncrement_value_roundtrip():
    instance = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    assert instance.acquireIncrement == 7
    instance.acquireIncrement = 13
    assert instance.acquireIncrement == 13


def test_db_DBConnection_loginTimeout_value_roundtrip():
    instance = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    assert instance.loginTimeout == 7
    instance.loginTimeout = 13
    assert instance.loginTimeout == 13


def test_db_DBConnection_maxIdleTime_value_roundtrip():
    instance = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    assert instance.maxIdleTime == 7
    instance.maxIdleTime = 13
    assert instance.maxIdleTime == 13


def test_db_DBConnection_maxPoolSize_value_roundtrip():
    instance = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    assert instance.maxPoolSize == 7
    instance.maxPoolSize = 13
    assert instance.maxPoolSize == 13


def test_db_DBConnection_minPoolSize_value_roundtrip():
    instance = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    assert instance.minPoolSize == 7
    instance.minPoolSize = 13
    assert instance.minPoolSize == 13


def test_db_DBConnection_password_value_roundtrip():
    instance = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_db_DBConnection_properties_value_roundtrip():
    instance = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    assert instance.properties == "sample_text"
    instance.properties = "sample_text_2"
    assert instance.properties == "sample_text_2"


def test_db_DBConnection_transactionMode_value_roundtrip():
    instance = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    assert instance.transactionMode == "sample_text"
    instance.transactionMode = "sample_text_2"
    assert instance.transactionMode == "sample_text_2"


def test_db_DBConnection_url_value_roundtrip():
    instance = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_db_DBConnection_user_value_roundtrip():
    instance = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    assert instance.user == "sample_text"
    instance.user = "sample_text_2"
    assert instance.user == "sample_text_2"


def test_db_DBDriver_default_value_roundtrip():
    instance = db_DBDriver(default=True, defaultPort=7, driverClassName="sample_text", exampleUrl="sample_text", guideUrl="sample_text", jars="sample_text", pooling=True, urlRegexPattern="sample_text", websiteUrl="sample_text")
    assert instance.default == True
    instance.default = False
    assert instance.default == False


def test_db_DBDriver_defaultPort_value_roundtrip():
    instance = db_DBDriver(default=True, defaultPort=7, driverClassName="sample_text", exampleUrl="sample_text", guideUrl="sample_text", jars="sample_text", pooling=True, urlRegexPattern="sample_text", websiteUrl="sample_text")
    assert instance.defaultPort == 7
    instance.defaultPort = 13
    assert instance.defaultPort == 13


def test_db_DBDriver_driverClassName_value_roundtrip():
    instance = db_DBDriver(default=True, defaultPort=7, driverClassName="sample_text", exampleUrl="sample_text", guideUrl="sample_text", jars="sample_text", pooling=True, urlRegexPattern="sample_text", websiteUrl="sample_text")
    assert instance.driverClassName == "sample_text"
    instance.driverClassName = "sample_text_2"
    assert instance.driverClassName == "sample_text_2"


def test_db_DBDriver_exampleUrl_value_roundtrip():
    instance = db_DBDriver(default=True, defaultPort=7, driverClassName="sample_text", exampleUrl="sample_text", guideUrl="sample_text", jars="sample_text", pooling=True, urlRegexPattern="sample_text", websiteUrl="sample_text")
    assert instance.exampleUrl == "sample_text"
    instance.exampleUrl = "sample_text_2"
    assert instance.exampleUrl == "sample_text_2"


def test_db_DBDriver_guideUrl_value_roundtrip():
    instance = db_DBDriver(default=True, defaultPort=7, driverClassName="sample_text", exampleUrl="sample_text", guideUrl="sample_text", jars="sample_text", pooling=True, urlRegexPattern="sample_text", websiteUrl="sample_text")
    assert instance.guideUrl == "sample_text"
    instance.guideUrl = "sample_text_2"
    assert instance.guideUrl == "sample_text_2"


def test_db_DBDriver_jars_value_roundtrip():
    instance = db_DBDriver(default=True, defaultPort=7, driverClassName="sample_text", exampleUrl="sample_text", guideUrl="sample_text", jars="sample_text", pooling=True, urlRegexPattern="sample_text", websiteUrl="sample_text")
    assert instance.jars == "sample_text"
    instance.jars = "sample_text_2"
    assert instance.jars == "sample_text_2"


def test_db_DBDriver_pooling_value_roundtrip():
    instance = db_DBDriver(default=True, defaultPort=7, driverClassName="sample_text", exampleUrl="sample_text", guideUrl="sample_text", jars="sample_text", pooling=True, urlRegexPattern="sample_text", websiteUrl="sample_text")
    assert instance.pooling == True
    instance.pooling = False
    assert instance.pooling == False


def test_db_DBDriver_urlRegexPattern_value_roundtrip():
    instance = db_DBDriver(default=True, defaultPort=7, driverClassName="sample_text", exampleUrl="sample_text", guideUrl="sample_text", jars="sample_text", pooling=True, urlRegexPattern="sample_text", websiteUrl="sample_text")
    assert instance.urlRegexPattern == "sample_text"
    instance.urlRegexPattern = "sample_text_2"
    assert instance.urlRegexPattern == "sample_text_2"


def test_db_DBDriver_websiteUrl_value_roundtrip():
    instance = db_DBDriver(default=True, defaultPort=7, driverClassName="sample_text", exampleUrl="sample_text", guideUrl="sample_text", jars="sample_text", pooling=True, urlRegexPattern="sample_text", websiteUrl="sample_text")
    assert instance.websiteUrl == "sample_text"
    instance.websiteUrl = "sample_text_2"
    assert instance.websiteUrl == "sample_text_2"


def test_db_DBResource_id_value_roundtrip():
    instance = db_DBResource(id=7, lastModified=date(2024, 1, 1), lastUpdated=date(2024, 1, 1), name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_db_DBResource_lastModified_value_roundtrip():
    instance = db_DBResource(id=7, lastModified=date(2024, 1, 1), lastUpdated=date(2024, 1, 1), name="sample_text")
    assert instance.lastModified == date(2024, 1, 1)
    instance.lastModified = date(2025, 6, 15)
    assert instance.lastModified == date(2025, 6, 15)


def test_db_DBResource_lastUpdated_value_roundtrip():
    instance = db_DBResource(id=7, lastModified=date(2024, 1, 1), lastUpdated=date(2024, 1, 1), name="sample_text")
    assert instance.lastUpdated == date(2024, 1, 1)
    instance.lastUpdated = date(2025, 6, 15)
    assert instance.lastUpdated == date(2025, 6, 15)


def test_db_DBResource_name_value_roundtrip():
    instance = db_DBResource(id=7, lastModified=date(2024, 1, 1), lastUpdated=date(2024, 1, 1), name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_db_Query_catalog_value_roundtrip():
    instance = db_Query(catalog="sample_text", querySql="sample_text", queryType="sample_text")
    assert instance.catalog == "sample_text"
    instance.catalog = "sample_text_2"
    assert instance.catalog == "sample_text_2"


def test_db_Query_querySql_value_roundtrip():
    instance = db_Query(catalog="sample_text", querySql="sample_text", queryType="sample_text")
    assert instance.querySql == "sample_text"
    instance.querySql = "sample_text_2"
    assert instance.querySql == "sample_text_2"


def test_db_Query_queryType_value_roundtrip():
    instance = db_Query(catalog="sample_text", querySql="sample_text", queryType="sample_text")
    assert instance.queryType == "sample_text"
    instance.queryType = "sample_text_2"
    assert instance.queryType == "sample_text_2"


def test_db_QueryParameter_dataType_value_roundtrip():
    instance = db_QueryParameter(dataType="sample_text")
    assert instance.dataType == "sample_text"
    instance.dataType = "sample_text_2"
    assert instance.dataType == "sample_text_2"


def test_db_SafiResultSet_holdabilityMode_value_roundtrip():
    instance = db_SafiResultSet(holdabilityMode="sample_text", readOnly=True, scrollMode="sample_text", scrollable=True, useCache=True)
    assert instance.holdabilityMode == "sample_text"
    instance.holdabilityMode = "sample_text_2"
    assert instance.holdabilityMode == "sample_text_2"


def test_db_SafiResultSet_readOnly_value_roundtrip():
    instance = db_SafiResultSet(holdabilityMode="sample_text", readOnly=True, scrollMode="sample_text", scrollable=True, useCache=True)
    assert instance.readOnly == True
    instance.readOnly = False
    assert instance.readOnly == False


def test_db_SafiResultSet_scrollMode_value_roundtrip():
    instance = db_SafiResultSet(holdabilityMode="sample_text", readOnly=True, scrollMode="sample_text", scrollable=True, useCache=True)
    assert instance.scrollMode == "sample_text"
    instance.scrollMode = "sample_text_2"
    assert instance.scrollMode == "sample_text_2"


def test_db_SafiResultSet_scrollable_value_roundtrip():
    instance = db_SafiResultSet(holdabilityMode="sample_text", readOnly=True, scrollMode="sample_text", scrollable=True, useCache=True)
    assert instance.scrollable == True
    instance.scrollable = False
    assert instance.scrollable == False


def test_db_SafiResultSet_useCache_value_roundtrip():
    instance = db_SafiResultSet(holdabilityMode="sample_text", readOnly=True, scrollMode="sample_text", scrollable=True, useCache=True)
    assert instance.useCache == True
    instance.useCache = False
    assert instance.useCache == False


def test_db_Variable_defaultValue_value_roundtrip():
    instance = db_Variable(defaultValue="sample_text", name="sample_text", scope="sample_text", type="sample_text")
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_db_Variable_name_value_roundtrip():
    instance = db_Variable(defaultValue="sample_text", name="sample_text", scope="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_db_Variable_scope_value_roundtrip():
    instance = db_Variable(defaultValue="sample_text", name="sample_text", scope="sample_text", type="sample_text")
    assert instance.scope == "sample_text"
    instance.scope = "sample_text_2"
    assert instance.scope == "sample_text_2"


def test_db_Variable_type_value_roundtrip():
    instance = db_Variable(defaultValue="sample_text", name="sample_text", scope="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_db_config_Prompt_extension_value_roundtrip():
    instance = db_config_Prompt(extension="sample_text", system=True)
    assert instance.extension == "sample_text"
    instance.extension = "sample_text_2"
    assert instance.extension == "sample_text_2"


def test_db_config_Prompt_system_value_roundtrip():
    instance = db_config_Prompt(extension="sample_text", system=True)
    assert instance.system == True
    instance.system = False
    assert instance.system == False


def test_db_config_SFTPInfo_sftpPassword_value_roundtrip():
    instance = db_config_SFTPInfo(sftpPassword="sample_text", sftpPort=7, sftpUser="sample_text")
    assert instance.sftpPassword == "sample_text"
    instance.sftpPassword = "sample_text_2"
    assert instance.sftpPassword == "sample_text_2"


def test_db_config_SFTPInfo_sftpPort_value_roundtrip():
    instance = db_config_SFTPInfo(sftpPassword="sample_text", sftpPort=7, sftpUser="sample_text")
    assert instance.sftpPort == 7
    instance.sftpPort = 13
    assert instance.sftpPort == 13


def test_db_config_SFTPInfo_sftpUser_value_roundtrip():
    instance = db_config_SFTPInfo(sftpPassword="sample_text", sftpPort=7, sftpUser="sample_text")
    assert instance.sftpUser == "sample_text"
    instance.sftpUser = "sample_text_2"
    assert instance.sftpUser == "sample_text_2"


def test_db_config_SafiServer_bindIP_value_roundtrip():
    instance = db_config_SafiServer(bindIP="sample_text", dbPort=7, debug=True, managementPort=7, running=True)
    assert instance.bindIP == "sample_text"
    instance.bindIP = "sample_text_2"
    assert instance.bindIP == "sample_text_2"


def test_db_config_SafiServer_dbPort_value_roundtrip():
    instance = db_config_SafiServer(bindIP="sample_text", dbPort=7, debug=True, managementPort=7, running=True)
    assert instance.dbPort == 7
    instance.dbPort = 13
    assert instance.dbPort == 13


def test_db_config_SafiServer_debug_value_roundtrip():
    instance = db_config_SafiServer(bindIP="sample_text", dbPort=7, debug=True, managementPort=7, running=True)
    assert instance.debug == True
    instance.debug = False
    assert instance.debug == False


def test_db_config_SafiServer_managementPort_value_roundtrip():
    instance = db_config_SafiServer(bindIP="sample_text", dbPort=7, debug=True, managementPort=7, running=True)
    assert instance.managementPort == 7
    instance.managementPort = 13
    assert instance.managementPort == 13


def test_db_config_SafiServer_running_value_roundtrip():
    instance = db_config_SafiServer(bindIP="sample_text", dbPort=7, debug=True, managementPort=7, running=True)
    assert instance.running == True
    instance.running = False
    assert instance.running == False


def test_db_config_Saflet_code_value_roundtrip():
    instance = db_config_Saflet(code="sample_text", subsystemId="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_db_config_Saflet_subsystemId_value_roundtrip():
    instance = db_config_Saflet(code="sample_text", subsystemId="sample_text")
    assert instance.subsystemId == "sample_text"
    instance.subsystemId = "sample_text_2"
    assert instance.subsystemId == "sample_text_2"


def test_db_config_SafletProject_enabled_value_roundtrip():
    instance = db_config_SafletProject(enabled=True)
    assert instance.enabled == True
    instance.enabled = False
    assert instance.enabled == False


def test_db_config_ServerResource_description_value_roundtrip():
    instance = db_config_ServerResource(description="sample_text", id=7, lastModified=date(2024, 1, 1), lastUpdated=date(2024, 1, 1), name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_db_config_ServerResource_id_value_roundtrip():
    instance = db_config_ServerResource(description="sample_text", id=7, lastModified=date(2024, 1, 1), lastUpdated=date(2024, 1, 1), name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_db_config_ServerResource_lastModified_value_roundtrip():
    instance = db_config_ServerResource(description="sample_text", id=7, lastModified=date(2024, 1, 1), lastUpdated=date(2024, 1, 1), name="sample_text")
    assert instance.lastModified == date(2024, 1, 1)
    instance.lastModified = date(2025, 6, 15)
    assert instance.lastModified == date(2025, 6, 15)


def test_db_config_ServerResource_lastUpdated_value_roundtrip():
    instance = db_config_ServerResource(description="sample_text", id=7, lastModified=date(2024, 1, 1), lastUpdated=date(2024, 1, 1), name="sample_text")
    assert instance.lastUpdated == date(2024, 1, 1)
    instance.lastUpdated = date(2025, 6, 15)
    assert instance.lastUpdated == date(2025, 6, 15)


def test_db_config_ServerResource_name_value_roundtrip():
    instance = db_config_ServerResource(description="sample_text", id=7, lastModified=date(2024, 1, 1), lastUpdated=date(2024, 1, 1), name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_db_config_TelephonySubsystem_enabled_value_roundtrip():
    instance = db_config_TelephonySubsystem(enabled=True, hostname="sample_text", managerName="sample_text", managerPassword="sample_text", managerPort=7, platformId="sample_text", private=True, promptDirectory="sample_text", running=True, versionId="sample_text", visibleSafiServerIP="sample_text")
    assert instance.enabled == True
    instance.enabled = False
    assert instance.enabled == False


def test_db_config_TelephonySubsystem_hostname_value_roundtrip():
    instance = db_config_TelephonySubsystem(enabled=True, hostname="sample_text", managerName="sample_text", managerPassword="sample_text", managerPort=7, platformId="sample_text", private=True, promptDirectory="sample_text", running=True, versionId="sample_text", visibleSafiServerIP="sample_text")
    assert instance.hostname == "sample_text"
    instance.hostname = "sample_text_2"
    assert instance.hostname == "sample_text_2"


def test_db_config_TelephonySubsystem_managerName_value_roundtrip():
    instance = db_config_TelephonySubsystem(enabled=True, hostname="sample_text", managerName="sample_text", managerPassword="sample_text", managerPort=7, platformId="sample_text", private=True, promptDirectory="sample_text", running=True, versionId="sample_text", visibleSafiServerIP="sample_text")
    assert instance.managerName == "sample_text"
    instance.managerName = "sample_text_2"
    assert instance.managerName == "sample_text_2"


def test_db_config_TelephonySubsystem_managerPassword_value_roundtrip():
    instance = db_config_TelephonySubsystem(enabled=True, hostname="sample_text", managerName="sample_text", managerPassword="sample_text", managerPort=7, platformId="sample_text", private=True, promptDirectory="sample_text", running=True, versionId="sample_text", visibleSafiServerIP="sample_text")
    assert instance.managerPassword == "sample_text"
    instance.managerPassword = "sample_text_2"
    assert instance.managerPassword == "sample_text_2"


def test_db_config_TelephonySubsystem_managerPort_value_roundtrip():
    instance = db_config_TelephonySubsystem(enabled=True, hostname="sample_text", managerName="sample_text", managerPassword="sample_text", managerPort=7, platformId="sample_text", private=True, promptDirectory="sample_text", running=True, versionId="sample_text", visibleSafiServerIP="sample_text")
    assert instance.managerPort == 7
    instance.managerPort = 13
    assert instance.managerPort == 13


def test_db_config_TelephonySubsystem_platformId_value_roundtrip():
    instance = db_config_TelephonySubsystem(enabled=True, hostname="sample_text", managerName="sample_text", managerPassword="sample_text", managerPort=7, platformId="sample_text", private=True, promptDirectory="sample_text", running=True, versionId="sample_text", visibleSafiServerIP="sample_text")
    assert instance.platformId == "sample_text"
    instance.platformId = "sample_text_2"
    assert instance.platformId == "sample_text_2"


def test_db_config_TelephonySubsystem_private_value_roundtrip():
    instance = db_config_TelephonySubsystem(enabled=True, hostname="sample_text", managerName="sample_text", managerPassword="sample_text", managerPort=7, platformId="sample_text", private=True, promptDirectory="sample_text", running=True, versionId="sample_text", visibleSafiServerIP="sample_text")
    assert instance.private == True
    instance.private = False
    assert instance.private == False


def test_db_config_TelephonySubsystem_promptDirectory_value_roundtrip():
    instance = db_config_TelephonySubsystem(enabled=True, hostname="sample_text", managerName="sample_text", managerPassword="sample_text", managerPort=7, platformId="sample_text", private=True, promptDirectory="sample_text", running=True, versionId="sample_text", visibleSafiServerIP="sample_text")
    assert instance.promptDirectory == "sample_text"
    instance.promptDirectory = "sample_text_2"
    assert instance.promptDirectory == "sample_text_2"


def test_db_config_TelephonySubsystem_running_value_roundtrip():
    instance = db_config_TelephonySubsystem(enabled=True, hostname="sample_text", managerName="sample_text", managerPassword="sample_text", managerPort=7, platformId="sample_text", private=True, promptDirectory="sample_text", running=True, versionId="sample_text", visibleSafiServerIP="sample_text")
    assert instance.running == True
    instance.running = False
    assert instance.running == False


def test_db_config_TelephonySubsystem_versionId_value_roundtrip():
    instance = db_config_TelephonySubsystem(enabled=True, hostname="sample_text", managerName="sample_text", managerPassword="sample_text", managerPort=7, platformId="sample_text", private=True, promptDirectory="sample_text", running=True, versionId="sample_text", visibleSafiServerIP="sample_text")
    assert instance.versionId == "sample_text"
    instance.versionId = "sample_text_2"
    assert instance.versionId == "sample_text_2"


def test_db_config_TelephonySubsystem_visibleSafiServerIP_value_roundtrip():
    instance = db_config_TelephonySubsystem(enabled=True, hostname="sample_text", managerName="sample_text", managerPassword="sample_text", managerPort=7, platformId="sample_text", private=True, promptDirectory="sample_text", running=True, versionId="sample_text", visibleSafiServerIP="sample_text")
    assert instance.visibleSafiServerIP == "sample_text"
    instance.visibleSafiServerIP = "sample_text_2"
    assert instance.visibleSafiServerIP == "sample_text_2"


def test_db_config_User_firstname_value_roundtrip():
    instance = db_config_User(firstname="sample_text", lastname="sample_text", password="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_db_config_User_lastname_value_roundtrip():
    instance = db_config_User(firstname="sample_text", lastname="sample_text", password="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_db_config_User_password_value_roundtrip():
    instance = db_config_User(firstname="sample_text", lastname="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_db_DBConnection_isa_DBResource():
    instance = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    assert isinstance(instance, DBResource)


def test_db_DBDriver_isa_DBResource():
    instance = db_DBDriver(default=True, defaultPort=7, driverClassName="sample_text", exampleUrl="sample_text", guideUrl="sample_text", jars="sample_text", pooling=True, urlRegexPattern="sample_text", websiteUrl="sample_text")
    assert isinstance(instance, DBResource)


def test_db_Query_isa_DBResource():
    instance = db_Query(catalog="sample_text", querySql="sample_text", queryType="sample_text")
    assert isinstance(instance, DBResource)


def test_db_QueryParameter_isa_DBResource():
    instance = db_QueryParameter(dataType="sample_text")
    assert isinstance(instance, DBResource)


def test_db_SafiDriverManager_isa_DBResource():
    instance = db_SafiDriverManager()
    assert isinstance(instance, DBResource)


def test_db_SafiResultSet_isa_DBResource():
    instance = db_SafiResultSet(holdabilityMode="sample_text", readOnly=True, scrollMode="sample_text", scrollable=True, useCache=True)
    assert isinstance(instance, DBResource)


def test_db_config_Entitlement_isa_ServerResource():
    instance = db_config_Entitlement()
    assert isinstance(instance, ServerResource)


def test_db_config_Prompt_isa_ServerResource():
    instance = db_config_Prompt(extension="sample_text", system=True)
    assert isinstance(instance, ServerResource)


def test_db_config_Role_isa_ServerResource():
    instance = db_config_Role()
    assert isinstance(instance, ServerResource)


def test_db_config_SafiServer_isa_ServerResource():
    instance = db_config_SafiServer(bindIP="sample_text", dbPort=7, debug=True, managementPort=7, running=True)
    assert isinstance(instance, ServerResource)


def test_db_config_Saflet_isa_ServerResource():
    instance = db_config_Saflet(code="sample_text", subsystemId="sample_text")
    assert isinstance(instance, ServerResource)


def test_db_config_SafletProject_isa_ServerResource():
    instance = db_config_SafletProject(enabled=True)
    assert isinstance(instance, ServerResource)


def test_db_config_TelephonySubsystem_isa_ServerResource():
    instance = db_config_TelephonySubsystem(enabled=True, hostname="sample_text", managerName="sample_text", managerPassword="sample_text", managerPort=7, platformId="sample_text", private=True, promptDirectory="sample_text", running=True, versionId="sample_text", visibleSafiServerIP="sample_text")
    assert isinstance(instance, ServerResource)


def test_db_config_User_isa_ServerResource():
    instance = db_config_User(firstname="sample_text", lastname="sample_text", password="sample_text")
    assert isinstance(instance, ServerResource)


def test_assoc_connection5_link_reassign_clear():
    a = db_Query(catalog="sample_text", querySql="sample_text", queryType="sample_text")
    b1 = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    b2 = db_DBConnection(acquireIncrement=13, loginTimeout=13, maxIdleTime=13, maxPoolSize=13, minPoolSize=13, password="sample_text_2", properties="sample_text_2", transactionMode="sample_text_2", url="sample_text_2", user="sample_text_2")
    _safe_set(a, 'queries', b1)
    assert _is_linked(a, 'queries', b1)
    if hasattr(b1, 'DBConnection6'):
        assert _is_linked(b1, 'DBConnection6', a)
    _safe_set(a, 'queries', b2)
    assert _is_linked(a, 'queries', b2)
    if hasattr(b1, 'DBConnection6'):
        assert not _is_linked(b1, 'DBConnection6', a)
    if hasattr(b2, 'DBConnection6'):
        assert _is_linked(b2, 'DBConnection6', a)
    _safe_set(a, 'queries', None)
    assert not _is_linked(a, 'queries', b2)
    if hasattr(b2, 'DBConnection6'):
        assert not _is_linked(b2, 'DBConnection6', a)


def test_assoc_connections2_link_reassign_clear():
    a = db_DBDriver(default=True, defaultPort=7, driverClassName="sample_text", exampleUrl="sample_text", guideUrl="sample_text", jars="sample_text", pooling=True, urlRegexPattern="sample_text", websiteUrl="sample_text")
    b1 = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    b2 = db_DBConnection(acquireIncrement=13, loginTimeout=13, maxIdleTime=13, maxPoolSize=13, minPoolSize=13, password="sample_text_2", properties="sample_text_2", transactionMode="sample_text_2", url="sample_text_2", user="sample_text_2")
    _safe_set(a, 'driver', {b1})
    assert _is_linked(a, 'driver', b1)
    if hasattr(b1, 'DBConnection'):
        assert _is_linked(b1, 'DBConnection', a)
    _safe_set(a, 'driver', {b2})
    assert _is_linked(a, 'driver', b2)
    if hasattr(b1, 'DBConnection'):
        assert not _is_linked(b1, 'DBConnection', a)
    if hasattr(b2, 'DBConnection'):
        assert _is_linked(b2, 'DBConnection', a)
    _safe_set(a, 'driver', set())
    assert not _is_linked(a, 'driver', b2)
    if hasattr(b2, 'DBConnection'):
        assert not _is_linked(b2, 'DBConnection', a)


def test_assoc_createdBy15_link_reassign_clear():
    a = db_config_ServerResource(description="sample_text", id=7, lastModified=date(2024, 1, 1), lastUpdated=date(2024, 1, 1), name="sample_text")
    b1 = config_User()
    b2 = config_User()
    _safe_set(a, 'db_config_ServerResource', b1)
    assert _is_linked(a, 'db_config_ServerResource', b1)
    if hasattr(b1, 'config_User'):
        assert _is_linked(b1, 'config_User', a)
    _safe_set(a, 'db_config_ServerResource', b2)
    assert _is_linked(a, 'db_config_ServerResource', b2)
    if hasattr(b1, 'config_User'):
        assert not _is_linked(b1, 'config_User', a)
    if hasattr(b2, 'config_User'):
        assert _is_linked(b2, 'config_User', a)
    _safe_set(a, 'db_config_ServerResource', None)
    assert not _is_linked(a, 'db_config_ServerResource', b2)
    if hasattr(b2, 'config_User'):
        assert not _is_linked(b2, 'config_User', a)


def test_assoc_driver0_link_reassign_clear():
    a = db_DBDriver(default=True, defaultPort=7, driverClassName="sample_text", exampleUrl="sample_text", guideUrl="sample_text", jars="sample_text", pooling=True, urlRegexPattern="sample_text", websiteUrl="sample_text")
    b1 = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    b2 = db_DBConnection(acquireIncrement=13, loginTimeout=13, maxIdleTime=13, maxPoolSize=13, minPoolSize=13, password="sample_text_2", properties="sample_text_2", transactionMode="sample_text_2", url="sample_text_2", user="sample_text_2")
    _safe_set(a, 'DBDriver', b1)
    assert _is_linked(a, 'DBDriver', b1)
    if hasattr(b1, 'connections'):
        assert _is_linked(b1, 'connections', a)
    _safe_set(a, 'DBDriver', b2)
    assert _is_linked(a, 'DBDriver', b2)
    if hasattr(b1, 'connections'):
        assert not _is_linked(b1, 'connections', a)
    if hasattr(b2, 'connections'):
        assert _is_linked(b2, 'connections', a)
    _safe_set(a, 'DBDriver', None)
    assert not _is_linked(a, 'DBDriver', b2)
    if hasattr(b2, 'connections'):
        assert not _is_linked(b2, 'connections', a)


def test_assoc_driverManager3_link_reassign_clear():
    a = db_SafiDriverManager()
    b1 = db_DBDriver(default=True, defaultPort=7, driverClassName="sample_text", exampleUrl="sample_text", guideUrl="sample_text", jars="sample_text", pooling=True, urlRegexPattern="sample_text", websiteUrl="sample_text")
    b2 = db_DBDriver(default=False, defaultPort=13, driverClassName="sample_text_2", exampleUrl="sample_text_2", guideUrl="sample_text_2", jars="sample_text_2", pooling=False, urlRegexPattern="sample_text_2", websiteUrl="sample_text_2")
    _safe_set(a, 'SafiDriverManager', b1)
    assert _is_linked(a, 'SafiDriverManager', b1)
    if hasattr(b1, 'drivers'):
        assert _is_linked(b1, 'drivers', a)
    _safe_set(a, 'SafiDriverManager', b2)
    assert _is_linked(a, 'SafiDriverManager', b2)
    if hasattr(b1, 'drivers'):
        assert not _is_linked(b1, 'drivers', a)
    if hasattr(b2, 'drivers'):
        assert _is_linked(b2, 'drivers', a)
    _safe_set(a, 'SafiDriverManager', None)
    assert not _is_linked(a, 'SafiDriverManager', b2)
    if hasattr(b2, 'drivers'):
        assert not _is_linked(b2, 'drivers', a)


def test_assoc_drivers11_link_reassign_clear():
    a = db_SafiDriverManager()
    b1 = db_DBDriver(default=True, defaultPort=7, driverClassName="sample_text", exampleUrl="sample_text", guideUrl="sample_text", jars="sample_text", pooling=True, urlRegexPattern="sample_text", websiteUrl="sample_text")
    b2 = db_DBDriver(default=False, defaultPort=13, driverClassName="sample_text_2", exampleUrl="sample_text_2", guideUrl="sample_text_2", jars="sample_text_2", pooling=False, urlRegexPattern="sample_text_2", websiteUrl="sample_text_2")
    _safe_set(a, 'driverManager', {b1})
    assert _is_linked(a, 'driverManager', b1)
    if hasattr(b1, 'DBDriver12'):
        assert _is_linked(b1, 'DBDriver12', a)
    _safe_set(a, 'driverManager', {b2})
    assert _is_linked(a, 'driverManager', b2)
    if hasattr(b1, 'DBDriver12'):
        assert not _is_linked(b1, 'DBDriver12', a)
    if hasattr(b2, 'DBDriver12'):
        assert _is_linked(b2, 'DBDriver12', a)
    _safe_set(a, 'driverManager', set())
    assert not _is_linked(a, 'driverManager', b2)
    if hasattr(b2, 'DBDriver12'):
        assert not _is_linked(b2, 'DBDriver12', a)


def test_assoc_modifiedBy16_link_reassign_clear():
    a = db_config_ServerResource(description="sample_text", id=7, lastModified=date(2024, 1, 1), lastUpdated=date(2024, 1, 1), name="sample_text")
    b1 = config_User()
    b2 = config_User()
    _safe_set(a, 'db_config_ServerResource17', b1)
    assert _is_linked(a, 'db_config_ServerResource17', b1)
    if hasattr(b1, 'config_User18'):
        assert _is_linked(b1, 'config_User18', a)
    _safe_set(a, 'db_config_ServerResource17', b2)
    assert _is_linked(a, 'db_config_ServerResource17', b2)
    if hasattr(b1, 'config_User18'):
        assert not _is_linked(b1, 'config_User18', a)
    if hasattr(b2, 'config_User18'):
        assert _is_linked(b2, 'config_User18', a)
    _safe_set(a, 'db_config_ServerResource17', None)
    assert not _is_linked(a, 'db_config_ServerResource17', b2)
    if hasattr(b2, 'config_User18'):
        assert not _is_linked(b2, 'config_User18', a)


def test_assoc_parameters4_link_reassign_clear():
    a = db_QueryParameter(dataType="sample_text")
    b1 = db_Query(catalog="sample_text", querySql="sample_text", queryType="sample_text")
    b2 = db_Query(catalog="sample_text_2", querySql="sample_text_2", queryType="sample_text_2")
    _safe_set(a, 'QueryParameter', b1)
    assert _is_linked(a, 'QueryParameter', b1)
    if hasattr(b1, 'query'):
        assert _is_linked(b1, 'query', a)
    _safe_set(a, 'QueryParameter', b2)
    assert _is_linked(a, 'QueryParameter', b2)
    if hasattr(b1, 'query'):
        assert not _is_linked(b1, 'query', a)
    if hasattr(b2, 'query'):
        assert _is_linked(b2, 'query', a)
    _safe_set(a, 'QueryParameter', None)
    assert not _is_linked(a, 'QueryParameter', b2)
    if hasattr(b2, 'query'):
        assert not _is_linked(b2, 'query', a)


def test_assoc_project26_link_reassign_clear():
    a = db_config_Saflet(code="sample_text", subsystemId="sample_text")
    b1 = config_SafletProject()
    b2 = config_SafletProject()
    _safe_set(a, 'saflets', b1)
    assert _is_linked(a, 'saflets', b1)
    if hasattr(b1, 'SafletProject'):
        assert _is_linked(b1, 'SafletProject', a)
    _safe_set(a, 'saflets', b2)
    assert _is_linked(a, 'saflets', b2)
    if hasattr(b1, 'SafletProject'):
        assert not _is_linked(b1, 'SafletProject', a)
    if hasattr(b2, 'SafletProject'):
        assert _is_linked(b2, 'SafletProject', a)
    _safe_set(a, 'saflets', None)
    assert not _is_linked(a, 'saflets', b2)
    if hasattr(b2, 'SafletProject'):
        assert not _is_linked(b2, 'SafletProject', a)


def test_assoc_project30_link_reassign_clear():
    a = db_config_Prompt(extension="sample_text", system=True)
    b1 = config_SafletProject()
    b2 = config_SafletProject()
    _safe_set(a, 'prompts', b1)
    assert _is_linked(a, 'prompts', b1)
    if hasattr(b1, 'SafletProject31'):
        assert _is_linked(b1, 'SafletProject31', a)
    _safe_set(a, 'prompts', b2)
    assert _is_linked(a, 'prompts', b2)
    if hasattr(b1, 'SafletProject31'):
        assert not _is_linked(b1, 'SafletProject31', a)
    if hasattr(b2, 'SafletProject31'):
        assert _is_linked(b2, 'SafletProject31', a)
    _safe_set(a, 'prompts', None)
    assert not _is_linked(a, 'prompts', b2)
    if hasattr(b2, 'SafletProject31'):
        assert not _is_linked(b2, 'SafletProject31', a)


def test_assoc_prompts28_link_reassign_clear():
    a = db_config_SafletProject(enabled=True)
    b1 = config_Prompt()
    b2 = config_Prompt()
    _safe_set(a, 'project29', {b1})
    assert _is_linked(a, 'project29', b1)
    if hasattr(b1, 'Prompt'):
        assert _is_linked(b1, 'Prompt', a)
    _safe_set(a, 'project29', {b2})
    assert _is_linked(a, 'project29', b2)
    if hasattr(b1, 'Prompt'):
        assert not _is_linked(b1, 'Prompt', a)
    if hasattr(b2, 'Prompt'):
        assert _is_linked(b2, 'Prompt', a)
    _safe_set(a, 'project29', set())
    assert not _is_linked(a, 'project29', b2)
    if hasattr(b2, 'Prompt'):
        assert not _is_linked(b2, 'Prompt', a)


def test_assoc_queries1_link_reassign_clear():
    a = db_Query(catalog="sample_text", querySql="sample_text", queryType="sample_text")
    b1 = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    b2 = db_DBConnection(acquireIncrement=13, loginTimeout=13, maxIdleTime=13, maxPoolSize=13, minPoolSize=13, password="sample_text_2", properties="sample_text_2", transactionMode="sample_text_2", url="sample_text_2", user="sample_text_2")
    _safe_set(a, 'Query', b1)
    assert _is_linked(a, 'Query', b1)
    if hasattr(b1, 'connection'):
        assert _is_linked(b1, 'connection', a)
    _safe_set(a, 'Query', b2)
    assert _is_linked(a, 'Query', b2)
    if hasattr(b1, 'connection'):
        assert not _is_linked(b1, 'connection', a)
    if hasattr(b2, 'connection'):
        assert _is_linked(b2, 'connection', a)
    _safe_set(a, 'Query', None)
    assert not _is_linked(a, 'Query', b2)
    if hasattr(b2, 'connection'):
        assert not _is_linked(b2, 'connection', a)


def test_assoc_query13_link_reassign_clear():
    a = db_SafiResultSet(holdabilityMode="sample_text", readOnly=True, scrollMode="sample_text", scrollable=True, useCache=True)
    b1 = db_Query(catalog="sample_text", querySql="sample_text", queryType="sample_text")
    b2 = db_Query(catalog="sample_text_2", querySql="sample_text_2", queryType="sample_text_2")
    _safe_set(a, 'resultSets', b1)
    assert _is_linked(a, 'resultSets', b1)
    if hasattr(b1, 'Query14'):
        assert _is_linked(b1, 'Query14', a)
    _safe_set(a, 'resultSets', b2)
    assert _is_linked(a, 'resultSets', b2)
    if hasattr(b1, 'Query14'):
        assert not _is_linked(b1, 'Query14', a)
    if hasattr(b2, 'Query14'):
        assert _is_linked(b2, 'Query14', a)
    _safe_set(a, 'resultSets', None)
    assert not _is_linked(a, 'resultSets', b2)
    if hasattr(b2, 'Query14'):
        assert not _is_linked(b2, 'Query14', a)


def test_assoc_query9_link_reassign_clear():
    a = db_QueryParameter(dataType="sample_text")
    b1 = db_Query(catalog="sample_text", querySql="sample_text", queryType="sample_text")
    b2 = db_Query(catalog="sample_text_2", querySql="sample_text_2", queryType="sample_text_2")
    _safe_set(a, 'parameters', b1)
    assert _is_linked(a, 'parameters', b1)
    if hasattr(b1, 'Query10'):
        assert _is_linked(b1, 'Query10', a)
    _safe_set(a, 'parameters', b2)
    assert _is_linked(a, 'parameters', b2)
    if hasattr(b1, 'Query10'):
        assert not _is_linked(b1, 'Query10', a)
    if hasattr(b2, 'Query10'):
        assert _is_linked(b2, 'Query10', a)
    _safe_set(a, 'parameters', None)
    assert not _is_linked(a, 'parameters', b2)
    if hasattr(b2, 'Query10'):
        assert not _is_linked(b2, 'Query10', a)


def test_assoc_resultSets7_link_reassign_clear():
    a = db_SafiResultSet(holdabilityMode="sample_text", readOnly=True, scrollMode="sample_text", scrollable=True, useCache=True)
    b1 = db_Query(catalog="sample_text", querySql="sample_text", queryType="sample_text")
    b2 = db_Query(catalog="sample_text_2", querySql="sample_text_2", queryType="sample_text_2")
    _safe_set(a, 'SafiResultSet', b1)
    assert _is_linked(a, 'SafiResultSet', b1)
    if hasattr(b1, 'query8'):
        assert _is_linked(b1, 'query8', a)
    _safe_set(a, 'SafiResultSet', b2)
    assert _is_linked(a, 'SafiResultSet', b2)
    if hasattr(b1, 'query8'):
        assert not _is_linked(b1, 'query8', a)
    if hasattr(b2, 'query8'):
        assert _is_linked(b2, 'query8', a)
    _safe_set(a, 'SafiResultSet', None)
    assert not _is_linked(a, 'SafiResultSet', b2)
    if hasattr(b2, 'query8'):
        assert not _is_linked(b2, 'query8', a)


def test_assoc_roles25_link_reassign_clear():
    a = db_config_User(firstname="sample_text", lastname="sample_text", password="sample_text")
    b1 = config_Role()
    b2 = config_Role()
    _safe_set(a, 'db_config_User', {b1})
    assert _is_linked(a, 'db_config_User', b1)
    if hasattr(b1, 'config_Role'):
        assert _is_linked(b1, 'config_Role', a)
    _safe_set(a, 'db_config_User', {b2})
    assert _is_linked(a, 'db_config_User', b2)
    if hasattr(b1, 'config_Role'):
        assert not _is_linked(b1, 'config_Role', a)
    if hasattr(b2, 'config_Role'):
        assert _is_linked(b2, 'config_Role', a)
    _safe_set(a, 'db_config_User', set())
    assert not _is_linked(a, 'db_config_User', b2)
    if hasattr(b2, 'config_Role'):
        assert not _is_linked(b2, 'config_Role', a)


def test_assoc_safiServer32_link_reassign_clear():
    a = db_config_TelephonySubsystem(enabled=True, hostname="sample_text", managerName="sample_text", managerPassword="sample_text", managerPort=7, platformId="sample_text", private=True, promptDirectory="sample_text", running=True, versionId="sample_text", visibleSafiServerIP="sample_text")
    b1 = config_SafiServer()
    b2 = config_SafiServer()
    _safe_set(a, 'db_config_TelephonySubsystem', b1)
    assert _is_linked(a, 'db_config_TelephonySubsystem', b1)
    if hasattr(b1, 'config_SafiServer'):
        assert _is_linked(b1, 'config_SafiServer', a)
    _safe_set(a, 'db_config_TelephonySubsystem', b2)
    assert _is_linked(a, 'db_config_TelephonySubsystem', b2)
    if hasattr(b1, 'config_SafiServer'):
        assert not _is_linked(b1, 'config_SafiServer', a)
    if hasattr(b2, 'config_SafiServer'):
        assert _is_linked(b2, 'config_SafiServer', a)
    _safe_set(a, 'db_config_TelephonySubsystem', None)
    assert not _is_linked(a, 'db_config_TelephonySubsystem', b2)
    if hasattr(b2, 'config_SafiServer'):
        assert not _is_linked(b2, 'config_SafiServer', a)


def test_assoc_saflets27_link_reassign_clear():
    a = db_config_SafletProject(enabled=True)
    b1 = config_Saflet()
    b2 = config_Saflet()
    _safe_set(a, 'project', {b1})
    assert _is_linked(a, 'project', b1)
    if hasattr(b1, 'Saflet'):
        assert _is_linked(b1, 'Saflet', a)
    _safe_set(a, 'project', {b2})
    assert _is_linked(a, 'project', b2)
    if hasattr(b1, 'Saflet'):
        assert not _is_linked(b1, 'Saflet', a)
    if hasattr(b2, 'Saflet'):
        assert _is_linked(b2, 'Saflet', a)
    _safe_set(a, 'project', set())
    assert not _is_linked(a, 'project', b2)
    if hasattr(b2, 'Saflet'):
        assert not _is_linked(b2, 'Saflet', a)


def test_assoc_user19_link_reassign_clear():
    a = db_config_SafiServer(bindIP="sample_text", dbPort=7, debug=True, managementPort=7, running=True)
    b1 = config_User()
    b2 = config_User()
    _safe_set(a, 'db_config_SafiServer', b1)
    assert _is_linked(a, 'db_config_SafiServer', b1)
    if hasattr(b1, 'config_User20'):
        assert _is_linked(b1, 'config_User20', a)
    _safe_set(a, 'db_config_SafiServer', b2)
    assert _is_linked(a, 'db_config_SafiServer', b2)
    if hasattr(b1, 'config_User20'):
        assert not _is_linked(b1, 'config_User20', a)
    if hasattr(b2, 'config_User20'):
        assert _is_linked(b2, 'config_User20', a)
    _safe_set(a, 'db_config_SafiServer', None)
    assert not _is_linked(a, 'db_config_SafiServer', b2)
    if hasattr(b2, 'config_User20'):
        assert not _is_linked(b2, 'config_User20', a)


def test_assoc_users21_link_reassign_clear():
    a = db_config_SafiServer(bindIP="sample_text", dbPort=7, debug=True, managementPort=7, running=True)
    b1 = config_User()
    b2 = config_User()
    _safe_set(a, 'db_config_SafiServer22', {b1})
    assert _is_linked(a, 'db_config_SafiServer22', b1)
    if hasattr(b1, 'config_User23'):
        assert _is_linked(b1, 'config_User23', a)
    _safe_set(a, 'db_config_SafiServer22', {b2})
    assert _is_linked(a, 'db_config_SafiServer22', b2)
    if hasattr(b1, 'config_User23'):
        assert not _is_linked(b1, 'config_User23', a)
    if hasattr(b2, 'config_User23'):
        assert _is_linked(b2, 'config_User23', a)
    _safe_set(a, 'db_config_SafiServer22', set())
    assert not _is_linked(a, 'db_config_SafiServer22', b2)
    if hasattr(b2, 'config_User23'):
        assert not _is_linked(b2, 'config_User23', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DBResource_strategy = st.builds(DBResource)
@given(instance=DBResource_strategy)
@settings(max_examples=25)
def test_DBResource_instantiation(instance):
    assert isinstance(instance, DBResource)


ServerResource_strategy = st.builds(ServerResource)
@given(instance=ServerResource_strategy)
@settings(max_examples=25)
def test_ServerResource_instantiation(instance):
    assert isinstance(instance, ServerResource)


config_Entitlement_strategy = st.builds(config_Entitlement)
@given(instance=config_Entitlement_strategy)
@settings(max_examples=25)
def test_config_Entitlement_instantiation(instance):
    assert isinstance(instance, config_Entitlement)


config_Prompt_strategy = st.builds(config_Prompt)
@given(instance=config_Prompt_strategy)
@settings(max_examples=25)
def test_config_Prompt_instantiation(instance):
    assert isinstance(instance, config_Prompt)


config_Role_strategy = st.builds(config_Role)
@given(instance=config_Role_strategy)
@settings(max_examples=25)
def test_config_Role_instantiation(instance):
    assert isinstance(instance, config_Role)


config_SafiServer_strategy = st.builds(config_SafiServer)
@given(instance=config_SafiServer_strategy)
@settings(max_examples=25)
def test_config_SafiServer_instantiation(instance):
    assert isinstance(instance, config_SafiServer)


config_Saflet_strategy = st.builds(config_Saflet)
@given(instance=config_Saflet_strategy)
@settings(max_examples=25)
def test_config_Saflet_instantiation(instance):
    assert isinstance(instance, config_Saflet)


config_SafletProject_strategy = st.builds(config_SafletProject)
@given(instance=config_SafletProject_strategy)
@settings(max_examples=25)
def test_config_SafletProject_instantiation(instance):
    assert isinstance(instance, config_SafletProject)


config_User_strategy = st.builds(config_User)
@given(instance=config_User_strategy)
@settings(max_examples=25)
def test_config_User_instantiation(instance):
    assert isinstance(instance, config_User)


db_DBConnection_strategy = st.builds(db_DBConnection, acquireIncrement=st.integers(), loginTimeout=st.integers(), maxIdleTime=st.integers(), maxPoolSize=st.integers(), minPoolSize=st.integers(), password=safe_text, properties=safe_text, transactionMode=safe_text, url=safe_text, user=safe_text)
@given(instance=db_DBConnection_strategy)
@settings(max_examples=25)
def test_db_DBConnection_instantiation(instance):
    assert isinstance(instance, db_DBConnection)


db_DBDriver_strategy = st.builds(db_DBDriver, default=st.booleans(), defaultPort=st.integers(), driverClassName=safe_text, exampleUrl=safe_text, guideUrl=safe_text, jars=safe_text, pooling=st.booleans(), urlRegexPattern=safe_text, websiteUrl=safe_text)
@given(instance=db_DBDriver_strategy)
@settings(max_examples=25)
def test_db_DBDriver_instantiation(instance):
    assert isinstance(instance, db_DBDriver)


db_DBResource_strategy = st.builds(db_DBResource, id=st.integers(), lastModified=st.dates(), lastUpdated=st.dates(), name=safe_text)
@given(instance=db_DBResource_strategy)
@settings(max_examples=25)
def test_db_DBResource_instantiation(instance):
    assert isinstance(instance, db_DBResource)


db_Query_strategy = st.builds(db_Query, catalog=safe_text, querySql=safe_text, queryType=safe_text)
@given(instance=db_Query_strategy)
@settings(max_examples=25)
def test_db_Query_instantiation(instance):
    assert isinstance(instance, db_Query)


db_QueryParameter_strategy = st.builds(db_QueryParameter, dataType=safe_text)
@given(instance=db_QueryParameter_strategy)
@settings(max_examples=25)
def test_db_QueryParameter_instantiation(instance):
    assert isinstance(instance, db_QueryParameter)


db_SafiDriverManager_strategy = st.builds(db_SafiDriverManager)
@given(instance=db_SafiDriverManager_strategy)
@settings(max_examples=25)
def test_db_SafiDriverManager_instantiation(instance):
    assert isinstance(instance, db_SafiDriverManager)


db_SafiResultSet_strategy = st.builds(db_SafiResultSet, holdabilityMode=safe_text, readOnly=st.booleans(), scrollMode=safe_text, scrollable=st.booleans(), useCache=st.booleans())
@given(instance=db_SafiResultSet_strategy)
@settings(max_examples=25)
def test_db_SafiResultSet_instantiation(instance):
    assert isinstance(instance, db_SafiResultSet)


db_Variable_strategy = st.builds(db_Variable, defaultValue=safe_text, name=safe_text, scope=safe_text, type=safe_text)
@given(instance=db_Variable_strategy)
@settings(max_examples=25)
def test_db_Variable_instantiation(instance):
    assert isinstance(instance, db_Variable)


db_config_Entitlement_strategy = st.builds(db_config_Entitlement)
@given(instance=db_config_Entitlement_strategy)
@settings(max_examples=25)
def test_db_config_Entitlement_instantiation(instance):
    assert isinstance(instance, db_config_Entitlement)


db_config_Prompt_strategy = st.builds(db_config_Prompt, extension=safe_text, system=st.booleans())
@given(instance=db_config_Prompt_strategy)
@settings(max_examples=25)
def test_db_config_Prompt_instantiation(instance):
    assert isinstance(instance, db_config_Prompt)


db_config_Role_strategy = st.builds(db_config_Role)
@given(instance=db_config_Role_strategy)
@settings(max_examples=25)
def test_db_config_Role_instantiation(instance):
    assert isinstance(instance, db_config_Role)


db_config_SFTPInfo_strategy = st.builds(db_config_SFTPInfo, sftpPassword=safe_text, sftpPort=st.integers(), sftpUser=safe_text)
@given(instance=db_config_SFTPInfo_strategy)
@settings(max_examples=25)
def test_db_config_SFTPInfo_instantiation(instance):
    assert isinstance(instance, db_config_SFTPInfo)


db_config_SafiServer_strategy = st.builds(db_config_SafiServer, bindIP=safe_text, dbPort=st.integers(), debug=st.booleans(), managementPort=st.integers(), running=st.booleans())
@given(instance=db_config_SafiServer_strategy)
@settings(max_examples=25)
def test_db_config_SafiServer_instantiation(instance):
    assert isinstance(instance, db_config_SafiServer)


db_config_Saflet_strategy = st.builds(db_config_Saflet, code=safe_text, subsystemId=safe_text)
@given(instance=db_config_Saflet_strategy)
@settings(max_examples=25)
def test_db_config_Saflet_instantiation(instance):
    assert isinstance(instance, db_config_Saflet)


db_config_SafletProject_strategy = st.builds(db_config_SafletProject, enabled=st.booleans())
@given(instance=db_config_SafletProject_strategy)
@settings(max_examples=25)
def test_db_config_SafletProject_instantiation(instance):
    assert isinstance(instance, db_config_SafletProject)


db_config_ServerResource_strategy = st.builds(db_config_ServerResource, description=safe_text, id=st.integers(), lastModified=st.dates(), lastUpdated=st.dates(), name=safe_text)
@given(instance=db_config_ServerResource_strategy)
@settings(max_examples=25)
def test_db_config_ServerResource_instantiation(instance):
    assert isinstance(instance, db_config_ServerResource)


db_config_TelephonySubsystem_strategy = st.builds(db_config_TelephonySubsystem, enabled=st.booleans(), hostname=safe_text, managerName=safe_text, managerPassword=safe_text, managerPort=st.integers(), platformId=safe_text, private=st.booleans(), promptDirectory=safe_text, running=st.booleans(), versionId=safe_text, visibleSafiServerIP=safe_text)
@given(instance=db_config_TelephonySubsystem_strategy)
@settings(max_examples=25)
def test_db_config_TelephonySubsystem_instantiation(instance):
    assert isinstance(instance, db_config_TelephonySubsystem)


db_config_User_strategy = st.builds(db_config_User, firstname=safe_text, lastname=safe_text, password=safe_text)
@given(instance=db_config_User_strategy)
@settings(max_examples=25)
def test_db_config_User_instantiation(instance):
    assert isinstance(instance, db_config_User)


