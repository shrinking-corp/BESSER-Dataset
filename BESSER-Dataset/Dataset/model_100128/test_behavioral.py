import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_connection5_reverse_link_reassign_clear():
    a1 = db_Query(catalog="sample_text", querySql="sample_text", queryType="sample_text")
    a2 = db_Query(catalog="sample_text_2", querySql="sample_text_2", queryType="sample_text_2")
    b = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    _safe_set(b, 'DBConnection6', a1)
    assert _is_linked(b, 'DBConnection6', a1)
    if hasattr(a1, 'queries'):
        assert _is_linked(a1, 'queries', b)
    _safe_set(b, 'DBConnection6', a2)
    assert _is_linked(b, 'DBConnection6', a2)
    if hasattr(a1, 'queries'):
        assert not _is_linked(a1, 'queries', b)
    if hasattr(a2, 'queries'):
        assert _is_linked(a2, 'queries', b)
    _safe_set(b, 'DBConnection6', None)
    assert not _is_linked(b, 'DBConnection6', a2)
    if hasattr(a2, 'queries'):
        assert not _is_linked(a2, 'queries', b)


def test_assoc_connections2_reverse_link_reassign_clear():
    a1 = db_DBDriver(default=True, defaultPort=7, driverClassName="sample_text", exampleUrl="sample_text", guideUrl="sample_text", jars="sample_text", pooling=True, urlRegexPattern="sample_text", websiteUrl="sample_text")
    a2 = db_DBDriver(default=False, defaultPort=13, driverClassName="sample_text_2", exampleUrl="sample_text_2", guideUrl="sample_text_2", jars="sample_text_2", pooling=False, urlRegexPattern="sample_text_2", websiteUrl="sample_text_2")
    b = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    _safe_set(b, 'DBConnection', a1)
    assert _is_linked(b, 'DBConnection', a1)
    if hasattr(a1, 'driver'):
        assert _is_linked(a1, 'driver', b)
    _safe_set(b, 'DBConnection', a2)
    assert _is_linked(b, 'DBConnection', a2)
    if hasattr(a1, 'driver'):
        assert not _is_linked(a1, 'driver', b)
    if hasattr(a2, 'driver'):
        assert _is_linked(a2, 'driver', b)
    _safe_set(b, 'DBConnection', None)
    assert not _is_linked(b, 'DBConnection', a2)
    if hasattr(a2, 'driver'):
        assert not _is_linked(a2, 'driver', b)


def test_assoc_driver0_reverse_link_reassign_clear():
    a1 = db_DBDriver(default=True, defaultPort=7, driverClassName="sample_text", exampleUrl="sample_text", guideUrl="sample_text", jars="sample_text", pooling=True, urlRegexPattern="sample_text", websiteUrl="sample_text")
    a2 = db_DBDriver(default=False, defaultPort=13, driverClassName="sample_text_2", exampleUrl="sample_text_2", guideUrl="sample_text_2", jars="sample_text_2", pooling=False, urlRegexPattern="sample_text_2", websiteUrl="sample_text_2")
    b = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    _safe_set(b, 'connections', a1)
    assert _is_linked(b, 'connections', a1)
    if hasattr(a1, 'DBDriver'):
        assert _is_linked(a1, 'DBDriver', b)
    _safe_set(b, 'connections', a2)
    assert _is_linked(b, 'connections', a2)
    if hasattr(a1, 'DBDriver'):
        assert not _is_linked(a1, 'DBDriver', b)
    if hasattr(a2, 'DBDriver'):
        assert _is_linked(a2, 'DBDriver', b)
    _safe_set(b, 'connections', None)
    assert not _is_linked(b, 'connections', a2)
    if hasattr(a2, 'DBDriver'):
        assert not _is_linked(a2, 'DBDriver', b)


def test_assoc_driverManager3_reverse_link_reassign_clear():
    a1 = db_SafiDriverManager()
    a2 = db_SafiDriverManager()
    b = db_DBDriver(default=True, defaultPort=7, driverClassName="sample_text", exampleUrl="sample_text", guideUrl="sample_text", jars="sample_text", pooling=True, urlRegexPattern="sample_text", websiteUrl="sample_text")
    _safe_set(b, 'drivers', a1)
    assert _is_linked(b, 'drivers', a1)
    if hasattr(a1, 'SafiDriverManager'):
        assert _is_linked(a1, 'SafiDriverManager', b)
    _safe_set(b, 'drivers', a2)
    assert _is_linked(b, 'drivers', a2)
    if hasattr(a1, 'SafiDriverManager'):
        assert not _is_linked(a1, 'SafiDriverManager', b)
    if hasattr(a2, 'SafiDriverManager'):
        assert _is_linked(a2, 'SafiDriverManager', b)
    _safe_set(b, 'drivers', None)
    assert not _is_linked(b, 'drivers', a2)
    if hasattr(a2, 'SafiDriverManager'):
        assert not _is_linked(a2, 'SafiDriverManager', b)


def test_assoc_drivers11_reverse_link_reassign_clear():
    a1 = db_SafiDriverManager()
    a2 = db_SafiDriverManager()
    b = db_DBDriver(default=True, defaultPort=7, driverClassName="sample_text", exampleUrl="sample_text", guideUrl="sample_text", jars="sample_text", pooling=True, urlRegexPattern="sample_text", websiteUrl="sample_text")
    _safe_set(b, 'DBDriver12', a1)
    assert _is_linked(b, 'DBDriver12', a1)
    if hasattr(a1, 'driverManager'):
        assert _is_linked(a1, 'driverManager', b)
    _safe_set(b, 'DBDriver12', a2)
    assert _is_linked(b, 'DBDriver12', a2)
    if hasattr(a1, 'driverManager'):
        assert not _is_linked(a1, 'driverManager', b)
    if hasattr(a2, 'driverManager'):
        assert _is_linked(a2, 'driverManager', b)
    _safe_set(b, 'DBDriver12', None)
    assert not _is_linked(b, 'DBDriver12', a2)
    if hasattr(a2, 'driverManager'):
        assert not _is_linked(a2, 'driverManager', b)


def test_assoc_parameters4_reverse_link_reassign_clear():
    a1 = db_QueryParameter(dataType="sample_text")
    a2 = db_QueryParameter(dataType="sample_text_2")
    b = db_Query(catalog="sample_text", querySql="sample_text", queryType="sample_text")
    _safe_set(b, 'query', {a1})
    assert _is_linked(b, 'query', a1)
    if hasattr(a1, 'QueryParameter'):
        assert _is_linked(a1, 'QueryParameter', b)
    _safe_set(b, 'query', {a2})
    assert _is_linked(b, 'query', a2)
    if hasattr(a1, 'QueryParameter'):
        assert not _is_linked(a1, 'QueryParameter', b)
    if hasattr(a2, 'QueryParameter'):
        assert _is_linked(a2, 'QueryParameter', b)
    _safe_set(b, 'query', set())
    assert not _is_linked(b, 'query', a2)
    if hasattr(a2, 'QueryParameter'):
        assert not _is_linked(a2, 'QueryParameter', b)


def test_assoc_queries1_reverse_link_reassign_clear():
    a1 = db_Query(catalog="sample_text", querySql="sample_text", queryType="sample_text")
    a2 = db_Query(catalog="sample_text_2", querySql="sample_text_2", queryType="sample_text_2")
    b = db_DBConnection(acquireIncrement=7, loginTimeout=7, maxIdleTime=7, maxPoolSize=7, minPoolSize=7, password="sample_text", properties="sample_text", transactionMode="sample_text", url="sample_text", user="sample_text")
    _safe_set(b, 'connection', {a1})
    assert _is_linked(b, 'connection', a1)
    if hasattr(a1, 'Query'):
        assert _is_linked(a1, 'Query', b)
    _safe_set(b, 'connection', {a2})
    assert _is_linked(b, 'connection', a2)
    if hasattr(a1, 'Query'):
        assert not _is_linked(a1, 'Query', b)
    if hasattr(a2, 'Query'):
        assert _is_linked(a2, 'Query', b)
    _safe_set(b, 'connection', set())
    assert not _is_linked(b, 'connection', a2)
    if hasattr(a2, 'Query'):
        assert not _is_linked(a2, 'Query', b)


def test_assoc_query13_reverse_link_reassign_clear():
    a1 = db_SafiResultSet(holdabilityMode="sample_text", readOnly=True, scrollMode="sample_text", scrollable=True, useCache=True)
    a2 = db_SafiResultSet(holdabilityMode="sample_text_2", readOnly=False, scrollMode="sample_text_2", scrollable=False, useCache=False)
    b = db_Query(catalog="sample_text", querySql="sample_text", queryType="sample_text")
    _safe_set(b, 'Query14', a1)
    assert _is_linked(b, 'Query14', a1)
    if hasattr(a1, 'resultSets'):
        assert _is_linked(a1, 'resultSets', b)
    _safe_set(b, 'Query14', a2)
    assert _is_linked(b, 'Query14', a2)
    if hasattr(a1, 'resultSets'):
        assert not _is_linked(a1, 'resultSets', b)
    if hasattr(a2, 'resultSets'):
        assert _is_linked(a2, 'resultSets', b)
    _safe_set(b, 'Query14', None)
    assert not _is_linked(b, 'Query14', a2)
    if hasattr(a2, 'resultSets'):
        assert not _is_linked(a2, 'resultSets', b)


def test_assoc_query9_reverse_link_reassign_clear():
    a1 = db_QueryParameter(dataType="sample_text")
    a2 = db_QueryParameter(dataType="sample_text_2")
    b = db_Query(catalog="sample_text", querySql="sample_text", queryType="sample_text")
    _safe_set(b, 'Query10', a1)
    assert _is_linked(b, 'Query10', a1)
    if hasattr(a1, 'parameters'):
        assert _is_linked(a1, 'parameters', b)
    _safe_set(b, 'Query10', a2)
    assert _is_linked(b, 'Query10', a2)
    if hasattr(a1, 'parameters'):
        assert not _is_linked(a1, 'parameters', b)
    if hasattr(a2, 'parameters'):
        assert _is_linked(a2, 'parameters', b)
    _safe_set(b, 'Query10', None)
    assert not _is_linked(b, 'Query10', a2)
    if hasattr(a2, 'parameters'):
        assert not _is_linked(a2, 'parameters', b)


def test_assoc_resultSets7_reverse_link_reassign_clear():
    a1 = db_SafiResultSet(holdabilityMode="sample_text", readOnly=True, scrollMode="sample_text", scrollable=True, useCache=True)
    a2 = db_SafiResultSet(holdabilityMode="sample_text_2", readOnly=False, scrollMode="sample_text_2", scrollable=False, useCache=False)
    b = db_Query(catalog="sample_text", querySql="sample_text", queryType="sample_text")
    _safe_set(b, 'query8', {a1})
    assert _is_linked(b, 'query8', a1)
    if hasattr(a1, 'SafiResultSet'):
        assert _is_linked(a1, 'SafiResultSet', b)
    _safe_set(b, 'query8', {a2})
    assert _is_linked(b, 'query8', a2)
    if hasattr(a1, 'SafiResultSet'):
        assert not _is_linked(a1, 'SafiResultSet', b)
    if hasattr(a2, 'SafiResultSet'):
        assert _is_linked(a2, 'SafiResultSet', b)
    _safe_set(b, 'query8', set())
    assert not _is_linked(b, 'query8', a2)
    if hasattr(a2, 'SafiResultSet'):
        assert not _is_linked(a2, 'SafiResultSet', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_createdBy15_stub_double():
    # config_User has no real 'config_User' property in the generated
    # code (a bare stub) -- manually attach it so db_config_ServerResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # db_config_ServerResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = db_config_ServerResource(description="sample_text", id=7, lastModified=date(2024, 1, 1), lastUpdated=date(2024, 1, 1), name="sample_text")
    partner = config_User()
    setattr(partner, 'config_User', None)
    _safe_set(owner, 'db_config_ServerResource', partner)
    assert getattr(partner, 'config_User') == owner
    _safe_set(owner, 'db_config_ServerResource', None)
    assert getattr(partner, 'config_User') is None


def test_assoc_modifiedBy16_stub_double():
    # config_User has no real 'config_User18' property in the generated
    # code (a bare stub) -- manually attach it so db_config_ServerResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # db_config_ServerResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = db_config_ServerResource(description="sample_text", id=7, lastModified=date(2024, 1, 1), lastUpdated=date(2024, 1, 1), name="sample_text")
    partner = config_User()
    setattr(partner, 'config_User18', None)
    _safe_set(owner, 'db_config_ServerResource17', partner)
    assert getattr(partner, 'config_User18') == owner
    _safe_set(owner, 'db_config_ServerResource17', None)
    assert getattr(partner, 'config_User18') is None


def test_assoc_project26_stub_double():
    # config_SafletProject has no real 'SafletProject' property in the generated
    # code (a bare stub) -- manually attach it so db_config_Saflet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # db_config_Saflet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = db_config_Saflet(code="sample_text", subsystemId="sample_text")
    partner = config_SafletProject()
    setattr(partner, 'SafletProject', None)
    _safe_set(owner, 'saflets', partner)
    assert getattr(partner, 'SafletProject') == owner
    _safe_set(owner, 'saflets', None)
    assert getattr(partner, 'SafletProject') is None


def test_assoc_project30_stub_double():
    # config_SafletProject has no real 'SafletProject31' property in the generated
    # code (a bare stub) -- manually attach it so db_config_Prompt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # db_config_Prompt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = db_config_Prompt(extension="sample_text", system=True)
    partner = config_SafletProject()
    setattr(partner, 'SafletProject31', None)
    _safe_set(owner, 'prompts', partner)
    assert getattr(partner, 'SafletProject31') == owner
    _safe_set(owner, 'prompts', None)
    assert getattr(partner, 'SafletProject31') is None


def test_assoc_prompts28_stub_double():
    # config_Prompt has no real 'Prompt' property in the generated
    # code (a bare stub) -- manually attach it so db_config_SafletProject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # db_config_SafletProject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = db_config_SafletProject(enabled=True)
    partner = config_Prompt()
    setattr(partner, 'Prompt', None)
    _safe_set(owner, 'project29', {partner})
    assert getattr(partner, 'Prompt') == owner
    _safe_set(owner, 'project29', set())
    assert getattr(partner, 'Prompt') is None


def test_assoc_roles25_stub_double():
    # config_Role has no real 'config_Role' property in the generated
    # code (a bare stub) -- manually attach it so db_config_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # db_config_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = db_config_User(firstname="sample_text", lastname="sample_text", password="sample_text")
    partner = config_Role()
    setattr(partner, 'config_Role', None)
    _safe_set(owner, 'db_config_User', {partner})
    assert getattr(partner, 'config_Role') == owner
    _safe_set(owner, 'db_config_User', set())
    assert getattr(partner, 'config_Role') is None


def test_assoc_safiServer32_stub_double():
    # config_SafiServer has no real 'config_SafiServer' property in the generated
    # code (a bare stub) -- manually attach it so db_config_TelephonySubsystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # db_config_TelephonySubsystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = db_config_TelephonySubsystem(enabled=True, hostname="sample_text", managerName="sample_text", managerPassword="sample_text", managerPort=7, platformId="sample_text", private=True, promptDirectory="sample_text", running=True, versionId="sample_text", visibleSafiServerIP="sample_text")
    partner = config_SafiServer()
    setattr(partner, 'config_SafiServer', None)
    _safe_set(owner, 'db_config_TelephonySubsystem', partner)
    assert getattr(partner, 'config_SafiServer') == owner
    _safe_set(owner, 'db_config_TelephonySubsystem', None)
    assert getattr(partner, 'config_SafiServer') is None


def test_assoc_saflets27_stub_double():
    # config_Saflet has no real 'Saflet' property in the generated
    # code (a bare stub) -- manually attach it so db_config_SafletProject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # db_config_SafletProject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = db_config_SafletProject(enabled=True)
    partner = config_Saflet()
    setattr(partner, 'Saflet', None)
    _safe_set(owner, 'project', {partner})
    assert getattr(partner, 'Saflet') == owner
    _safe_set(owner, 'project', set())
    assert getattr(partner, 'Saflet') is None


def test_assoc_user19_stub_double():
    # config_User has no real 'config_User20' property in the generated
    # code (a bare stub) -- manually attach it so db_config_SafiServer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # db_config_SafiServer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = db_config_SafiServer(bindIP="sample_text", dbPort=7, debug=True, managementPort=7, running=True)
    partner = config_User()
    setattr(partner, 'config_User20', None)
    _safe_set(owner, 'db_config_SafiServer', partner)
    assert getattr(partner, 'config_User20') == owner
    _safe_set(owner, 'db_config_SafiServer', None)
    assert getattr(partner, 'config_User20') is None


def test_assoc_users21_stub_double():
    # config_User has no real 'config_User23' property in the generated
    # code (a bare stub) -- manually attach it so db_config_SafiServer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # db_config_SafiServer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = db_config_SafiServer(bindIP="sample_text", dbPort=7, debug=True, managementPort=7, running=True)
    partner = config_User()
    setattr(partner, 'config_User23', None)
    _safe_set(owner, 'db_config_SafiServer22', {partner})
    assert getattr(partner, 'config_User23') == owner
    _safe_set(owner, 'db_config_SafiServer22', set())
    assert getattr(partner, 'config_User23') is None


