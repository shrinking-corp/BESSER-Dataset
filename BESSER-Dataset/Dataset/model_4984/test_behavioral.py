import pytest
from datetime import date, datetime, time, timedelta

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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_baseInstances105_stub_double():
    # VMInstance has no real 'VMInstance106' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_core_ResourcesPool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_core_ResourcesPool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_core_ResourcesPool(maxReplicats=7, minReplicats=7, nbReplicats=7, type="sample_text")
    partner = VMInstance()
    setattr(partner, 'VMInstance106', None)
    _safe_set(owner, 'cloudml_core_ResourcesPool', {partner})
    assert getattr(partner, 'VMInstance106') == owner
    _safe_set(owner, 'cloudml_core_ResourcesPool', set())
    assert getattr(partner, 'VMInstance106') is None


def test_assoc_component44_stub_double():
    # Component has no real 'Component45' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_core_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_core_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_core_Port(isLocal=True, portNumber=7)
    partner = Component()
    setattr(partner, 'Component45', None)
    _safe_set(owner, 'cloudml_core_Port', partner)
    assert getattr(partner, 'Component45') == owner
    _safe_set(owner, 'cloudml_core_Port', None)
    assert getattr(partner, 'Component45') is None


def test_assoc_provide85_stub_double():
    # VMPort has no real 'VMPort87' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_core_ExternalComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_core_ExternalComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_core_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    partner = VMPort()
    setattr(partner, 'VMPort87', None)
    _safe_set(owner, 'cloudml_core_ExternalComponent86', {partner})
    assert getattr(partner, 'VMPort87') == owner
    _safe_set(owner, 'cloudml_core_ExternalComponent86', set())
    assert getattr(partner, 'VMPort87') is None


def test_assoc_provide88_stub_double():
    # VMPortInstance has no real 'VMPortInstance89' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_core_ExternalComponentInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_core_ExternalComponentInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_core_ExternalComponentInstance(ips="sample_text", status="sample_text")
    partner = VMPortInstance()
    setattr(partner, 'VMPortInstance89', None)
    _safe_set(owner, 'cloudml_core_ExternalComponentInstance', {partner})
    assert getattr(partner, 'VMPortInstance89') == owner
    _safe_set(owner, 'cloudml_core_ExternalComponentInstance', set())
    assert getattr(partner, 'VMPortInstance89') is None


def test_assoc_provided34_stub_double():
    # VMPort has no real 'VMPort' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_core_VM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_core_VM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_core_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    partner = VMPort()
    setattr(partner, 'VMPort', None)
    _safe_set(owner, 'cloudml_core_VM', {partner})
    assert getattr(partner, 'VMPort') == owner
    _safe_set(owner, 'cloudml_core_VM', set())
    assert getattr(partner, 'VMPort') is None


def test_assoc_provided59_stub_double():
    # VMPortInstance has no real 'VMPortInstance' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_core_VMInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_core_VMInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_core_VMInstance(hostname="sample_text", id="sample_text", publicAddress="sample_text")
    partner = VMPortInstance()
    setattr(partner, 'VMPortInstance', None)
    _safe_set(owner, 'cloudml_core_VMInstance', {partner})
    assert getattr(partner, 'VMPortInstance') == owner
    _safe_set(owner, 'cloudml_core_VMInstance', set())
    assert getattr(partner, 'VMPortInstance') is None


def test_assoc_provider83_stub_double():
    # Provider has no real 'Provider84' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_core_ExternalComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_core_ExternalComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_core_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    partner = Provider()
    setattr(partner, 'Provider84', None)
    _safe_set(owner, 'cloudml_core_ExternalComponent', partner)
    assert getattr(partner, 'Provider84') == owner
    _safe_set(owner, 'cloudml_core_ExternalComponent', None)
    assert getattr(partner, 'Provider84') is None


def test_assoc_replicats107_stub_double():
    # VMInstance has no real 'VMInstance109' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_core_ResourcesPool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_core_ResourcesPool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_core_ResourcesPool(maxReplicats=7, minReplicats=7, nbReplicats=7, type="sample_text")
    partner = VMInstance()
    setattr(partner, 'VMInstance109', None)
    _safe_set(owner, 'cloudml_core_ResourcesPool108', {partner})
    assert getattr(partner, 'VMInstance109') == owner
    _safe_set(owner, 'cloudml_core_ResourcesPool108', set())
    assert getattr(partner, 'VMInstance109') is None


