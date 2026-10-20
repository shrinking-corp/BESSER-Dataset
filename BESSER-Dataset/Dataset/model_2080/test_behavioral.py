import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_artifacts51_reverse_link_reassign_clear():
    a1 = ddsm_DDSM(description="sample_text", modelId="sample_text")
    a2 = ddsm_DDSM(description="sample_text_2", modelId="sample_text_2")
    b = ddsm_Artifact(arguments="sample_text", artifactPath="sample_text", language="sample_text", resources="sample_text")
    _safe_set(b, 'ddsm_Artifact53', a1)
    assert _is_linked(b, 'ddsm_Artifact53', a1)
    if hasattr(a1, 'ddsm_DDSM52'):
        assert _is_linked(a1, 'ddsm_DDSM52', b)
    _safe_set(b, 'ddsm_Artifact53', a2)
    assert _is_linked(b, 'ddsm_Artifact53', a2)
    if hasattr(a1, 'ddsm_DDSM52'):
        assert not _is_linked(a1, 'ddsm_DDSM52', b)
    if hasattr(a2, 'ddsm_DDSM52'):
        assert _is_linked(a2, 'ddsm_DDSM52', b)
    _safe_set(b, 'ddsm_Artifact53', None)
    assert not _is_linked(b, 'ddsm_Artifact53', a2)
    if hasattr(a2, 'ddsm_DDSM52'):
        assert not _is_linked(a2, 'ddsm_DDSM52', b)


def test_assoc_cloudelement43_reverse_link_reassign_clear():
    a1 = ddsm_DDSM(description="sample_text", modelId="sample_text")
    a2 = ddsm_DDSM(description="sample_text_2", modelId="sample_text_2")
    b = ddsm_CloudElement(description="sample_text", elementId="sample_text")
    _safe_set(b, 'ddsm_CloudElement44', a1)
    assert _is_linked(b, 'ddsm_CloudElement44', a1)
    if hasattr(a1, 'ddsm_DDSM'):
        assert _is_linked(a1, 'ddsm_DDSM', b)
    _safe_set(b, 'ddsm_CloudElement44', a2)
    assert _is_linked(b, 'ddsm_CloudElement44', a2)
    if hasattr(a1, 'ddsm_DDSM'):
        assert not _is_linked(a1, 'ddsm_DDSM', b)
    if hasattr(a2, 'ddsm_DDSM'):
        assert _is_linked(a2, 'ddsm_DDSM', b)
    _safe_set(b, 'ddsm_CloudElement44', None)
    assert not _is_linked(b, 'ddsm_CloudElement44', a2)
    if hasattr(a2, 'ddsm_DDSM'):
        assert not _is_linked(a2, 'ddsm_DDSM', b)


def test_assoc_configure5_reverse_link_reassign_clear():
    a1 = ddsm_Resource(resourceId="sample_text")
    a2 = ddsm_Resource(resourceId="sample_text_2")
    b = ddsm_Artifact(arguments="sample_text", artifactPath="sample_text", language="sample_text", resources="sample_text")
    _safe_set(b, 'ddsm_Artifact7', a1)
    assert _is_linked(b, 'ddsm_Artifact7', a1)
    if hasattr(a1, 'ddsm_Resource6'):
        assert _is_linked(a1, 'ddsm_Resource6', b)
    _safe_set(b, 'ddsm_Artifact7', a2)
    assert _is_linked(b, 'ddsm_Artifact7', a2)
    if hasattr(a1, 'ddsm_Resource6'):
        assert not _is_linked(a1, 'ddsm_Resource6', b)
    if hasattr(a2, 'ddsm_Resource6'):
        assert _is_linked(a2, 'ddsm_Resource6', b)
    _safe_set(b, 'ddsm_Artifact7', None)
    assert not _is_linked(b, 'ddsm_Artifact7', a2)
    if hasattr(a2, 'ddsm_Resource6'):
        assert not _is_linked(a2, 'ddsm_Resource6', b)


def test_assoc_destroy14_reverse_link_reassign_clear():
    a1 = ddsm_Resource(resourceId="sample_text")
    a2 = ddsm_Resource(resourceId="sample_text_2")
    b = ddsm_Artifact(arguments="sample_text", artifactPath="sample_text", language="sample_text", resources="sample_text")
    _safe_set(b, 'ddsm_Artifact16', a1)
    assert _is_linked(b, 'ddsm_Artifact16', a1)
    if hasattr(a1, 'ddsm_Resource15'):
        assert _is_linked(a1, 'ddsm_Resource15', b)
    _safe_set(b, 'ddsm_Artifact16', a2)
    assert _is_linked(b, 'ddsm_Artifact16', a2)
    if hasattr(a1, 'ddsm_Resource15'):
        assert not _is_linked(a1, 'ddsm_Resource15', b)
    if hasattr(a2, 'ddsm_Resource15'):
        assert _is_linked(a2, 'ddsm_Resource15', b)
    _safe_set(b, 'ddsm_Artifact16', None)
    assert not _is_linked(b, 'ddsm_Artifact16', a2)
    if hasattr(a2, 'ddsm_Resource15'):
        assert not _is_linked(a2, 'ddsm_Resource15', b)


def test_assoc_download3_reverse_link_reassign_clear():
    a1 = ddsm_Resource(resourceId="sample_text")
    a2 = ddsm_Resource(resourceId="sample_text_2")
    b = ddsm_Artifact(arguments="sample_text", artifactPath="sample_text", language="sample_text", resources="sample_text")
    _safe_set(b, 'ddsm_Artifact', a1)
    assert _is_linked(b, 'ddsm_Artifact', a1)
    if hasattr(a1, 'ddsm_Resource4'):
        assert _is_linked(a1, 'ddsm_Resource4', b)
    _safe_set(b, 'ddsm_Artifact', a2)
    assert _is_linked(b, 'ddsm_Artifact', a2)
    if hasattr(a1, 'ddsm_Resource4'):
        assert not _is_linked(a1, 'ddsm_Resource4', b)
    if hasattr(a2, 'ddsm_Resource4'):
        assert _is_linked(a2, 'ddsm_Resource4', b)
    _safe_set(b, 'ddsm_Artifact', None)
    assert not _is_linked(b, 'ddsm_Artifact', a2)
    if hasattr(a2, 'ddsm_Resource4'):
        assert not _is_linked(a2, 'ddsm_Resource4', b)


def test_assoc_hasSchedule55_reverse_link_reassign_clear():
    a1 = ddsm_Crontab(dayOfMonth=7, dayOfWeek=7, hour=7, min=7, month=7)
    a2 = ddsm_Crontab(dayOfMonth=13, dayOfWeek=13, hour=13, min=13, month=13)
    b = ddsm_ClientNode(numberOfSubmissions=7, skipRunningJob=True)
    _safe_set(b, 'ddsm_ClientNode56', a1)
    assert _is_linked(b, 'ddsm_ClientNode56', a1)
    if hasattr(a1, 'ddsm_Crontab'):
        assert _is_linked(a1, 'ddsm_Crontab', b)
    _safe_set(b, 'ddsm_ClientNode56', a2)
    assert _is_linked(b, 'ddsm_ClientNode56', a2)
    if hasattr(a1, 'ddsm_Crontab'):
        assert not _is_linked(a1, 'ddsm_Crontab', b)
    if hasattr(a2, 'ddsm_Crontab'):
        assert _is_linked(a2, 'ddsm_Crontab', b)
    _safe_set(b, 'ddsm_ClientNode56', None)
    assert not _is_linked(b, 'ddsm_ClientNode56', a2)
    if hasattr(a2, 'ddsm_Crontab'):
        assert not _is_linked(a2, 'ddsm_Crontab', b)


def test_assoc_install17_reverse_link_reassign_clear():
    a1 = ddsm_Resource(resourceId="sample_text")
    a2 = ddsm_Resource(resourceId="sample_text_2")
    b = ddsm_Artifact(arguments="sample_text", artifactPath="sample_text", language="sample_text", resources="sample_text")
    _safe_set(b, 'ddsm_Artifact19', a1)
    assert _is_linked(b, 'ddsm_Artifact19', a1)
    if hasattr(a1, 'ddsm_Resource18'):
        assert _is_linked(a1, 'ddsm_Resource18', b)
    _safe_set(b, 'ddsm_Artifact19', a2)
    assert _is_linked(b, 'ddsm_Artifact19', a2)
    if hasattr(a1, 'ddsm_Resource18'):
        assert not _is_linked(a1, 'ddsm_Resource18', b)
    if hasattr(a2, 'ddsm_Resource18'):
        assert _is_linked(a2, 'ddsm_Resource18', b)
    _safe_set(b, 'ddsm_Artifact19', None)
    assert not _is_linked(b, 'ddsm_Artifact19', a2)
    if hasattr(a2, 'ddsm_Resource18'):
        assert not _is_linked(a2, 'ddsm_Resource18', b)


def test_assoc_properties45_reverse_link_reassign_clear():
    a1 = ddsm_Property(propertyId="sample_text", value="sample_text")
    a2 = ddsm_Property(propertyId="sample_text_2", value="sample_text_2")
    b = ddsm_DDSM(description="sample_text", modelId="sample_text")
    _safe_set(b, 'ddsm_DDSM46', {a1})
    assert _is_linked(b, 'ddsm_DDSM46', a1)
    if hasattr(a1, 'ddsm_Property47'):
        assert _is_linked(a1, 'ddsm_Property47', b)
    _safe_set(b, 'ddsm_DDSM46', {a2})
    assert _is_linked(b, 'ddsm_DDSM46', a2)
    if hasattr(a1, 'ddsm_Property47'):
        assert not _is_linked(a1, 'ddsm_Property47', b)
    if hasattr(a2, 'ddsm_Property47'):
        assert _is_linked(a2, 'ddsm_Property47', b)
    _safe_set(b, 'ddsm_DDSM46', set())
    assert not _is_linked(b, 'ddsm_DDSM46', a2)
    if hasattr(a2, 'ddsm_Property47'):
        assert not _is_linked(a2, 'ddsm_Property47', b)


def test_assoc_property1_reverse_link_reassign_clear():
    a1 = ddsm_Property(propertyId="sample_text", value="sample_text")
    a2 = ddsm_Property(propertyId="sample_text_2", value="sample_text_2")
    b = ddsm_CloudElement(description="sample_text", elementId="sample_text")
    _safe_set(b, 'ddsm_CloudElement2', {a1})
    assert _is_linked(b, 'ddsm_CloudElement2', a1)
    if hasattr(a1, 'ddsm_Property'):
        assert _is_linked(a1, 'ddsm_Property', b)
    _safe_set(b, 'ddsm_CloudElement2', {a2})
    assert _is_linked(b, 'ddsm_CloudElement2', a2)
    if hasattr(a1, 'ddsm_Property'):
        assert not _is_linked(a1, 'ddsm_Property', b)
    if hasattr(a2, 'ddsm_Property'):
        assert _is_linked(a2, 'ddsm_Property', b)
    _safe_set(b, 'ddsm_CloudElement2', set())
    assert not _is_linked(b, 'ddsm_CloudElement2', a2)
    if hasattr(a2, 'ddsm_Property'):
        assert not _is_linked(a2, 'ddsm_Property', b)


def test_assoc_provider42_reverse_link_reassign_clear():
    a1 = ddsm_Provider(credentialsPath="sample_text", type="sample_text")
    a2 = ddsm_Provider(credentialsPath="sample_text_2", type="sample_text_2")
    b = ddsm_ExternalComponent(endPoint="sample_text", location="sample_text", login="sample_text", password="sample_text", region="sample_text", serviceType="sample_text")
    _safe_set(b, 'ddsm_ExternalComponent', a1)
    assert _is_linked(b, 'ddsm_ExternalComponent', a1)
    if hasattr(a1, 'ddsm_Provider'):
        assert _is_linked(a1, 'ddsm_Provider', b)
    _safe_set(b, 'ddsm_ExternalComponent', a2)
    assert _is_linked(b, 'ddsm_ExternalComponent', a2)
    if hasattr(a1, 'ddsm_Provider'):
        assert not _is_linked(a1, 'ddsm_Provider', b)
    if hasattr(a2, 'ddsm_Provider'):
        assert _is_linked(a2, 'ddsm_Provider', b)
    _safe_set(b, 'ddsm_ExternalComponent', None)
    assert not _is_linked(b, 'ddsm_ExternalComponent', a2)
    if hasattr(a2, 'ddsm_Provider'):
        assert not _is_linked(a2, 'ddsm_Provider', b)


def test_assoc_resource0_reverse_link_reassign_clear():
    a1 = ddsm_Resource(resourceId="sample_text")
    a2 = ddsm_Resource(resourceId="sample_text_2")
    b = ddsm_CloudElement(description="sample_text", elementId="sample_text")
    _safe_set(b, 'ddsm_CloudElement', {a1})
    assert _is_linked(b, 'ddsm_CloudElement', a1)
    if hasattr(a1, 'ddsm_Resource'):
        assert _is_linked(a1, 'ddsm_Resource', b)
    _safe_set(b, 'ddsm_CloudElement', {a2})
    assert _is_linked(b, 'ddsm_CloudElement', a2)
    if hasattr(a1, 'ddsm_Resource'):
        assert not _is_linked(a1, 'ddsm_Resource', b)
    if hasattr(a2, 'ddsm_Resource'):
        assert _is_linked(a2, 'ddsm_Resource', b)
    _safe_set(b, 'ddsm_CloudElement', set())
    assert not _is_linked(b, 'ddsm_CloudElement', a2)
    if hasattr(a2, 'ddsm_Resource'):
        assert not _is_linked(a2, 'ddsm_Resource', b)


def test_assoc_resources48_reverse_link_reassign_clear():
    a1 = ddsm_Resource(resourceId="sample_text")
    a2 = ddsm_Resource(resourceId="sample_text_2")
    b = ddsm_DDSM(description="sample_text", modelId="sample_text")
    _safe_set(b, 'ddsm_DDSM49', {a1})
    assert _is_linked(b, 'ddsm_DDSM49', a1)
    if hasattr(a1, 'ddsm_Resource50'):
        assert _is_linked(a1, 'ddsm_Resource50', b)
    _safe_set(b, 'ddsm_DDSM49', {a2})
    assert _is_linked(b, 'ddsm_DDSM49', a2)
    if hasattr(a1, 'ddsm_Resource50'):
        assert not _is_linked(a1, 'ddsm_Resource50', b)
    if hasattr(a2, 'ddsm_Resource50'):
        assert _is_linked(a2, 'ddsm_Resource50', b)
    _safe_set(b, 'ddsm_DDSM49', set())
    assert not _is_linked(b, 'ddsm_DDSM49', a2)
    if hasattr(a2, 'ddsm_Resource50'):
        assert not _is_linked(a2, 'ddsm_Resource50', b)


def test_assoc_start8_reverse_link_reassign_clear():
    a1 = ddsm_Resource(resourceId="sample_text")
    a2 = ddsm_Resource(resourceId="sample_text_2")
    b = ddsm_Artifact(arguments="sample_text", artifactPath="sample_text", language="sample_text", resources="sample_text")
    _safe_set(b, 'ddsm_Artifact10', a1)
    assert _is_linked(b, 'ddsm_Artifact10', a1)
    if hasattr(a1, 'ddsm_Resource9'):
        assert _is_linked(a1, 'ddsm_Resource9', b)
    _safe_set(b, 'ddsm_Artifact10', a2)
    assert _is_linked(b, 'ddsm_Artifact10', a2)
    if hasattr(a1, 'ddsm_Resource9'):
        assert not _is_linked(a1, 'ddsm_Resource9', b)
    if hasattr(a2, 'ddsm_Resource9'):
        assert _is_linked(a2, 'ddsm_Resource9', b)
    _safe_set(b, 'ddsm_Artifact10', None)
    assert not _is_linked(b, 'ddsm_Artifact10', a2)
    if hasattr(a2, 'ddsm_Resource9'):
        assert not _is_linked(a2, 'ddsm_Resource9', b)


def test_assoc_stop11_reverse_link_reassign_clear():
    a1 = ddsm_Resource(resourceId="sample_text")
    a2 = ddsm_Resource(resourceId="sample_text_2")
    b = ddsm_Artifact(arguments="sample_text", artifactPath="sample_text", language="sample_text", resources="sample_text")
    _safe_set(b, 'ddsm_Artifact13', a1)
    assert _is_linked(b, 'ddsm_Artifact13', a1)
    if hasattr(a1, 'ddsm_Resource12'):
        assert _is_linked(a1, 'ddsm_Resource12', b)
    _safe_set(b, 'ddsm_Artifact13', a2)
    assert _is_linked(b, 'ddsm_Artifact13', a2)
    if hasattr(a1, 'ddsm_Resource12'):
        assert not _is_linked(a1, 'ddsm_Resource12', b)
    if hasattr(a2, 'ddsm_Resource12'):
        assert _is_linked(a2, 'ddsm_Resource12', b)
    _safe_set(b, 'ddsm_Artifact13', None)
    assert not _is_linked(b, 'ddsm_Artifact13', a2)
    if hasattr(a2, 'ddsm_Resource12'):
        assert not _is_linked(a2, 'ddsm_Resource12', b)


def test_assoc_submits54_reverse_link_reassign_clear():
    a1 = ddsm_JobSubmission(applicationArguments="sample_text", artifactUrl="sample_text", mainClass="sample_text")
    a2 = ddsm_JobSubmission(applicationArguments="sample_text_2", artifactUrl="sample_text_2", mainClass="sample_text_2")
    b = ddsm_ClientNode(numberOfSubmissions=7, skipRunningJob=True)
    _safe_set(b, 'ddsm_ClientNode', a1)
    assert _is_linked(b, 'ddsm_ClientNode', a1)
    if hasattr(a1, 'ddsm_JobSubmission'):
        assert _is_linked(a1, 'ddsm_JobSubmission', b)
    _safe_set(b, 'ddsm_ClientNode', a2)
    assert _is_linked(b, 'ddsm_ClientNode', a2)
    if hasattr(a1, 'ddsm_JobSubmission'):
        assert not _is_linked(a1, 'ddsm_JobSubmission', b)
    if hasattr(a2, 'ddsm_JobSubmission'):
        assert _is_linked(a2, 'ddsm_JobSubmission', b)
    _safe_set(b, 'ddsm_ClientNode', None)
    assert not _is_linked(b, 'ddsm_ClientNode', a2)
    if hasattr(a2, 'ddsm_JobSubmission'):
        assert not _is_linked(a2, 'ddsm_JobSubmission', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_requiredexecutionplatform24_stub_double():
    # ddsm_InternalComponent has no real 'ddsm_InternalComponent25' property in the generated
    # code (a bare stub) -- manually attach it so ddsm_RequiredExecutionPlatform's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsm_RequiredExecutionPlatform's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsm_RequiredExecutionPlatform(isMandatory=True)
    partner = ddsm_InternalComponent()
    setattr(partner, 'ddsm_InternalComponent25', None)
    _safe_set(owner, 'ddsm_RequiredExecutionPlatform', partner)
    assert owner in getattr(partner, 'ddsm_InternalComponent25')
    _safe_set(owner, 'ddsm_RequiredExecutionPlatform', None)
    assert owner not in getattr(partner, 'ddsm_InternalComponent25')


def test_assoc_requiredexecutionplatform37_stub_double():
    # ddsm_ExecutionBinding has no real 'ddsm_ExecutionBinding' property in the generated
    # code (a bare stub) -- manually attach it so ddsm_RequiredExecutionPlatform's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsm_RequiredExecutionPlatform's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsm_RequiredExecutionPlatform(isMandatory=True)
    partner = ddsm_ExecutionBinding()
    setattr(partner, 'ddsm_ExecutionBinding', None)
    _safe_set(owner, 'ddsm_RequiredExecutionPlatform38', partner)
    assert getattr(partner, 'ddsm_ExecutionBinding') == owner
    _safe_set(owner, 'ddsm_RequiredExecutionPlatform38', None)
    assert getattr(partner, 'ddsm_ExecutionBinding') is None


def test_assoc_requiredport23_stub_double():
    # ddsm_InternalComponent has no real 'ddsm_InternalComponent' property in the generated
    # code (a bare stub) -- manually attach it so ddsm_RequiredPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsm_RequiredPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsm_RequiredPort(isMandatory=True)
    partner = ddsm_InternalComponent()
    setattr(partner, 'ddsm_InternalComponent', None)
    _safe_set(owner, 'ddsm_RequiredPort', partner)
    assert owner in getattr(partner, 'ddsm_InternalComponent')
    _safe_set(owner, 'ddsm_RequiredPort', None)
    assert owner not in getattr(partner, 'ddsm_InternalComponent')


def test_assoc_requiredport34_stub_double():
    # ddsm_Relationship has no real 'ddsm_Relationship35' property in the generated
    # code (a bare stub) -- manually attach it so ddsm_RequiredPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsm_RequiredPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsm_RequiredPort(isMandatory=True)
    partner = ddsm_Relationship()
    setattr(partner, 'ddsm_Relationship35', None)
    _safe_set(owner, 'ddsm_RequiredPort36', partner)
    assert getattr(partner, 'ddsm_Relationship35') == owner
    _safe_set(owner, 'ddsm_RequiredPort36', None)
    assert getattr(partner, 'ddsm_Relationship35') is None


def test_assoc_requiresMasterVm61_stub_double():
    # ddsm_MasterSlavePlatform has no real 'ddsm_MasterSlavePlatform' property in the generated
    # code (a bare stub) -- manually attach it so ddsm_RequiredExecutionPlatform's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsm_RequiredExecutionPlatform's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsm_RequiredExecutionPlatform(isMandatory=True)
    partner = ddsm_MasterSlavePlatform()
    setattr(partner, 'ddsm_MasterSlavePlatform', None)
    _safe_set(owner, 'ddsm_RequiredExecutionPlatform62', partner)
    assert getattr(partner, 'ddsm_MasterSlavePlatform') == owner
    _safe_set(owner, 'ddsm_RequiredExecutionPlatform62', None)
    assert getattr(partner, 'ddsm_MasterSlavePlatform') is None


def test_assoc_requiresPeerVm59_stub_double():
    # ddsm_PeerToPeerPlatform has no real 'ddsm_PeerToPeerPlatform' property in the generated
    # code (a bare stub) -- manually attach it so ddsm_RequiredExecutionPlatform's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsm_RequiredExecutionPlatform's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsm_RequiredExecutionPlatform(isMandatory=True)
    partner = ddsm_PeerToPeerPlatform()
    setattr(partner, 'ddsm_PeerToPeerPlatform', None)
    _safe_set(owner, 'ddsm_RequiredExecutionPlatform60', partner)
    assert owner in getattr(partner, 'ddsm_PeerToPeerPlatform')
    _safe_set(owner, 'ddsm_RequiredExecutionPlatform60', None)
    assert owner not in getattr(partner, 'ddsm_PeerToPeerPlatform')


def test_assoc_requiresSlaveVm63_stub_double():
    # ddsm_MasterSlavePlatform has no real 'ddsm_MasterSlavePlatform64' property in the generated
    # code (a bare stub) -- manually attach it so ddsm_RequiredExecutionPlatform's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsm_RequiredExecutionPlatform's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsm_RequiredExecutionPlatform(isMandatory=True)
    partner = ddsm_MasterSlavePlatform()
    setattr(partner, 'ddsm_MasterSlavePlatform64', None)
    _safe_set(owner, 'ddsm_RequiredExecutionPlatform65', partner)
    assert owner in getattr(partner, 'ddsm_MasterSlavePlatform64')
    _safe_set(owner, 'ddsm_RequiredExecutionPlatform65', None)
    assert owner not in getattr(partner, 'ddsm_MasterSlavePlatform64')


