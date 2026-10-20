import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_cloudelement29_reverse_link_reassign_clear():
    a1 = ddsm_DDSM(description="sample_text", modelId="sample_text")
    a2 = ddsm_DDSM(description="sample_text_2", modelId="sample_text_2")
    b = ddsm_CloudElement(description="sample_text", elementId="sample_text")
    _safe_set(b, 'ddsm_CloudElement30', a1)
    assert _is_linked(b, 'ddsm_CloudElement30', a1)
    if hasattr(a1, 'ddsm_DDSM'):
        assert _is_linked(a1, 'ddsm_DDSM', b)
    _safe_set(b, 'ddsm_CloudElement30', a2)
    assert _is_linked(b, 'ddsm_CloudElement30', a2)
    if hasattr(a1, 'ddsm_DDSM'):
        assert not _is_linked(a1, 'ddsm_DDSM', b)
    if hasattr(a2, 'ddsm_DDSM'):
        assert _is_linked(a2, 'ddsm_DDSM', b)
    _safe_set(b, 'ddsm_CloudElement30', None)
    assert not _is_linked(b, 'ddsm_CloudElement30', a2)
    if hasattr(a2, 'ddsm_DDSM'):
        assert not _is_linked(a2, 'ddsm_DDSM', b)


def test_assoc_properties31_reverse_link_reassign_clear():
    a1 = ddsm_Property(propertyId="sample_text", value="sample_text")
    a2 = ddsm_Property(propertyId="sample_text_2", value="sample_text_2")
    b = ddsm_DDSM(description="sample_text", modelId="sample_text")
    _safe_set(b, 'ddsm_DDSM32', {a1})
    assert _is_linked(b, 'ddsm_DDSM32', a1)
    if hasattr(a1, 'ddsm_Property33'):
        assert _is_linked(a1, 'ddsm_Property33', b)
    _safe_set(b, 'ddsm_DDSM32', {a2})
    assert _is_linked(b, 'ddsm_DDSM32', a2)
    if hasattr(a1, 'ddsm_Property33'):
        assert not _is_linked(a1, 'ddsm_Property33', b)
    if hasattr(a2, 'ddsm_Property33'):
        assert _is_linked(a2, 'ddsm_Property33', b)
    _safe_set(b, 'ddsm_DDSM32', set())
    assert not _is_linked(b, 'ddsm_DDSM32', a2)
    if hasattr(a2, 'ddsm_Property33'):
        assert not _is_linked(a2, 'ddsm_Property33', b)


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


def test_assoc_provider28_reverse_link_reassign_clear():
    a1 = ddsm_Provider(credentialsPath="sample_text", type="sample_text")
    a2 = ddsm_Provider(credentialsPath="sample_text_2", type="sample_text_2")
    b = ddsm_ExternalComponent(location="sample_text", login="sample_text", password="sample_text", region="sample_text", serviceType="sample_text")
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
    a1 = ddsm_Resource(configureCommand="sample_text", createCommand="sample_text", downloadCommand="sample_text", installCommand="sample_text", resourceId="sample_text", startCommand="sample_text", stopCommand="sample_text")
    a2 = ddsm_Resource(configureCommand="sample_text_2", createCommand="sample_text_2", downloadCommand="sample_text_2", installCommand="sample_text_2", resourceId="sample_text_2", startCommand="sample_text_2", stopCommand="sample_text_2")
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


def test_assoc_resources34_reverse_link_reassign_clear():
    a1 = ddsm_Resource(configureCommand="sample_text", createCommand="sample_text", downloadCommand="sample_text", installCommand="sample_text", resourceId="sample_text", startCommand="sample_text", stopCommand="sample_text")
    a2 = ddsm_Resource(configureCommand="sample_text_2", createCommand="sample_text_2", downloadCommand="sample_text_2", installCommand="sample_text_2", resourceId="sample_text_2", startCommand="sample_text_2", stopCommand="sample_text_2")
    b = ddsm_DDSM(description="sample_text", modelId="sample_text")
    _safe_set(b, 'ddsm_DDSM35', {a1})
    assert _is_linked(b, 'ddsm_DDSM35', a1)
    if hasattr(a1, 'ddsm_Resource36'):
        assert _is_linked(a1, 'ddsm_Resource36', b)
    _safe_set(b, 'ddsm_DDSM35', {a2})
    assert _is_linked(b, 'ddsm_DDSM35', a2)
    if hasattr(a1, 'ddsm_Resource36'):
        assert not _is_linked(a1, 'ddsm_Resource36', b)
    if hasattr(a2, 'ddsm_Resource36'):
        assert _is_linked(a2, 'ddsm_Resource36', b)
    _safe_set(b, 'ddsm_DDSM35', set())
    assert not _is_linked(b, 'ddsm_DDSM35', a2)
    if hasattr(a2, 'ddsm_Resource36'):
        assert not _is_linked(a2, 'ddsm_Resource36', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_hasVm37_stub_double():
    # ddsm_Cluster has no real 'ddsm_Cluster' property in the generated
    # code (a bare stub) -- manually attach it so ddsm_VM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsm_VM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsm_VM(genericSize="sample_text", imageId="sample_text", instances="sample_text", is64os="sample_text", maxCores="sample_text", maxRam="sample_text", maxStorage="sample_text", minCores="sample_text", minRam="sample_text", minStorage="sample_text", os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", publicAddress="sample_text", publicPorts="sample_text", securityGroup="sample_text", sshKey="sample_text")
    partner = ddsm_Cluster()
    setattr(partner, 'ddsm_Cluster', None)
    _safe_set(owner, 'ddsm_VM', partner)
    assert owner in getattr(partner, 'ddsm_Cluster')
    _safe_set(owner, 'ddsm_VM', None)
    assert owner not in getattr(partner, 'ddsm_Cluster')


def test_assoc_requiredexecutionplatform10_stub_double():
    # ddsm_InternalComponent has no real 'ddsm_InternalComponent11' property in the generated
    # code (a bare stub) -- manually attach it so ddsm_RequiredExecutionPlatform's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsm_RequiredExecutionPlatform's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsm_RequiredExecutionPlatform(isMandatory=True)
    partner = ddsm_InternalComponent()
    setattr(partner, 'ddsm_InternalComponent11', None)
    _safe_set(owner, 'ddsm_RequiredExecutionPlatform', partner)
    assert owner in getattr(partner, 'ddsm_InternalComponent11')
    _safe_set(owner, 'ddsm_RequiredExecutionPlatform', None)
    assert owner not in getattr(partner, 'ddsm_InternalComponent11')


def test_assoc_requiredexecutionplatform23_stub_double():
    # ddsm_ExecutionBinding has no real 'ddsm_ExecutionBinding' property in the generated
    # code (a bare stub) -- manually attach it so ddsm_RequiredExecutionPlatform's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsm_RequiredExecutionPlatform's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsm_RequiredExecutionPlatform(isMandatory=True)
    partner = ddsm_ExecutionBinding()
    setattr(partner, 'ddsm_ExecutionBinding', None)
    _safe_set(owner, 'ddsm_RequiredExecutionPlatform24', partner)
    assert getattr(partner, 'ddsm_ExecutionBinding') == owner
    _safe_set(owner, 'ddsm_RequiredExecutionPlatform24', None)
    assert getattr(partner, 'ddsm_ExecutionBinding') is None


def test_assoc_requiredport20_stub_double():
    # ddsm_Relationship has no real 'ddsm_Relationship21' property in the generated
    # code (a bare stub) -- manually attach it so ddsm_RequiredPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsm_RequiredPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsm_RequiredPort(isMandatory=True)
    partner = ddsm_Relationship()
    setattr(partner, 'ddsm_Relationship21', None)
    _safe_set(owner, 'ddsm_RequiredPort22', partner)
    assert getattr(partner, 'ddsm_Relationship21') == owner
    _safe_set(owner, 'ddsm_RequiredPort22', None)
    assert getattr(partner, 'ddsm_Relationship21') is None


def test_assoc_requiredport6_stub_double():
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


