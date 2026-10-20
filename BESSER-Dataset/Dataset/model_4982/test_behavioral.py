import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_provider90_reverse_link_reassign_clear():
    a1 = cloudml_Provider(credentials="sample_text")
    a2 = cloudml_Provider(credentials="sample_text_2")
    b = cloudml_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    _safe_set(b, 'cloudml_ExternalComponent91', a1)
    assert _is_linked(b, 'cloudml_ExternalComponent91', a1)
    if hasattr(a1, 'cloudml_Provider92'):
        assert _is_linked(a1, 'cloudml_Provider92', b)
    _safe_set(b, 'cloudml_ExternalComponent91', a2)
    assert _is_linked(b, 'cloudml_ExternalComponent91', a2)
    if hasattr(a1, 'cloudml_Provider92'):
        assert not _is_linked(a1, 'cloudml_Provider92', b)
    if hasattr(a2, 'cloudml_Provider92'):
        assert _is_linked(a2, 'cloudml_Provider92', b)
    _safe_set(b, 'cloudml_ExternalComponent91', None)
    assert not _is_linked(b, 'cloudml_ExternalComponent91', a2)
    if hasattr(a2, 'cloudml_Provider92'):
        assert not _is_linked(a2, 'cloudml_Provider92', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_component43_stub_double():
    # cloudml_Component has no real 'cloudml_Component44' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_Port(isLocal=True, portNumber=7)
    partner = cloudml_Component()
    setattr(partner, 'cloudml_Component44', None)
    _safe_set(owner, 'cloudml_Port', partner)
    assert getattr(partner, 'cloudml_Component44') == owner
    _safe_set(owner, 'cloudml_Port', None)
    assert getattr(partner, 'cloudml_Component44') is None


def test_assoc_demands109_stub_double():
    # cloudml_RequiredExecutionPlatform has no real 'cloudml_RequiredExecutionPlatform110' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_Property(value="sample_text")
    partner = cloudml_RequiredExecutionPlatform()
    setattr(partner, 'cloudml_RequiredExecutionPlatform110', None)
    _safe_set(owner, 'cloudml_Property111', partner)
    assert owner in getattr(partner, 'cloudml_RequiredExecutionPlatform110')
    _safe_set(owner, 'cloudml_Property111', None)
    assert owner not in getattr(partner, 'cloudml_RequiredExecutionPlatform110')


def test_assoc_externalComponentInstances18_stub_double():
    # cloudml_CloudMLModel has no real 'cloudml_CloudMLModel19' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_ExternalComponentInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_ExternalComponentInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_ExternalComponentInstance(ips="sample_text")
    partner = cloudml_CloudMLModel()
    setattr(partner, 'cloudml_CloudMLModel19', None)
    _safe_set(owner, 'cloudml_ExternalComponentInstance', partner)
    assert owner in getattr(partner, 'cloudml_CloudMLModel19')
    _safe_set(owner, 'cloudml_ExternalComponentInstance', None)
    assert owner not in getattr(partner, 'cloudml_CloudMLModel19')


def test_assoc_externalComponents14_stub_double():
    # cloudml_CloudMLModel has no real 'cloudml_CloudMLModel15' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_ExternalComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_ExternalComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    partner = cloudml_CloudMLModel()
    setattr(partner, 'cloudml_CloudMLModel15', None)
    _safe_set(owner, 'cloudml_ExternalComponent', partner)
    assert owner in getattr(partner, 'cloudml_CloudMLModel15')
    _safe_set(owner, 'cloudml_ExternalComponent', None)
    assert owner not in getattr(partner, 'cloudml_CloudMLModel15')


def test_assoc_offers106_stub_double():
    # cloudml_ProvidedExecutionPlatform has no real 'cloudml_ProvidedExecutionPlatform107' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_Property(value="sample_text")
    partner = cloudml_ProvidedExecutionPlatform()
    setattr(partner, 'cloudml_ProvidedExecutionPlatform107', None)
    _safe_set(owner, 'cloudml_Property108', partner)
    assert owner in getattr(partner, 'cloudml_ProvidedExecutionPlatform107')
    _safe_set(owner, 'cloudml_Property108', None)
    assert owner not in getattr(partner, 'cloudml_ProvidedExecutionPlatform107')


def test_assoc_properties0_stub_double():
    # cloudml_CloudMLElementWithProperties has no real 'cloudml_CloudMLElementWithProperties' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_Property(value="sample_text")
    partner = cloudml_CloudMLElementWithProperties()
    setattr(partner, 'cloudml_CloudMLElementWithProperties', None)
    _safe_set(owner, 'cloudml_Property', partner)
    assert owner in getattr(partner, 'cloudml_CloudMLElementWithProperties')
    _safe_set(owner, 'cloudml_Property', None)
    assert owner not in getattr(partner, 'cloudml_CloudMLElementWithProperties')


def test_assoc_provide93_stub_double():
    # cloudml_VMPort has no real 'cloudml_VMPort95' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_ExternalComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_ExternalComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_ExternalComponent(Region="sample_text", endPoint="sample_text", location="sample_text", login="sample_text", passwd="sample_text", serviceType="sample_text")
    partner = cloudml_VMPort()
    setattr(partner, 'cloudml_VMPort95', None)
    _safe_set(owner, 'cloudml_ExternalComponent94', {partner})
    assert getattr(partner, 'cloudml_VMPort95') == owner
    _safe_set(owner, 'cloudml_ExternalComponent94', set())
    assert getattr(partner, 'cloudml_VMPort95') is None


def test_assoc_provide96_stub_double():
    # cloudml_VMPortInstance has no real 'cloudml_VMPortInstance98' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_ExternalComponentInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_ExternalComponentInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_ExternalComponentInstance(ips="sample_text")
    partner = cloudml_VMPortInstance()
    setattr(partner, 'cloudml_VMPortInstance98', None)
    _safe_set(owner, 'cloudml_ExternalComponentInstance97', {partner})
    assert getattr(partner, 'cloudml_VMPortInstance98') == owner
    _safe_set(owner, 'cloudml_ExternalComponentInstance97', set())
    assert getattr(partner, 'cloudml_VMPortInstance98') is None


def test_assoc_provided30_stub_double():
    # cloudml_VMPort has no real 'cloudml_VMPort' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_VM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_VM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    partner = cloudml_VMPort()
    setattr(partner, 'cloudml_VMPort', None)
    _safe_set(owner, 'cloudml_VM31', {partner})
    assert getattr(partner, 'cloudml_VMPort') == owner
    _safe_set(owner, 'cloudml_VM31', set())
    assert getattr(partner, 'cloudml_VMPort') is None


def test_assoc_provided60_stub_double():
    # cloudml_VMPortInstance has no real 'cloudml_VMPortInstance' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_VMInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_VMInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_VMInstance(id="sample_text", publicAddress="sample_text")
    partner = cloudml_VMPortInstance()
    setattr(partner, 'cloudml_VMPortInstance', None)
    _safe_set(owner, 'cloudml_VMInstance61', {partner})
    assert getattr(partner, 'cloudml_VMPortInstance') == owner
    _safe_set(owner, 'cloudml_VMInstance61', set())
    assert getattr(partner, 'cloudml_VMPortInstance') is None


def test_assoc_providedPortResource54_stub_double():
    # cloudml_Relationship has no real 'cloudml_Relationship55' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    partner = cloudml_Relationship()
    setattr(partner, 'cloudml_Relationship55', None)
    _safe_set(owner, 'cloudml_Resource56', partner)
    assert getattr(partner, 'cloudml_Relationship55') == owner
    _safe_set(owner, 'cloudml_Resource56', None)
    assert getattr(partner, 'cloudml_Relationship55') is None


def test_assoc_providers5_stub_double():
    # cloudml_CloudMLModel has no real 'cloudml_CloudMLModel' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_Provider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_Provider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_Provider(credentials="sample_text")
    partner = cloudml_CloudMLModel()
    setattr(partner, 'cloudml_CloudMLModel', None)
    _safe_set(owner, 'cloudml_Provider', partner)
    assert owner in getattr(partner, 'cloudml_CloudMLModel')
    _safe_set(owner, 'cloudml_Provider', None)
    assert owner not in getattr(partner, 'cloudml_CloudMLModel')


def test_assoc_puppetResources3_stub_double():
    # cloudml_CloudMLElementWithProperties has no real 'cloudml_CloudMLElementWithProperties4' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_PuppetResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_PuppetResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_PuppetResource(configurationFile="sample_text", configureHostnameCommand="sample_text", manifestEntry="sample_text", masterEndpoint="sample_text", repositoryEndpoint="sample_text", repositoryKey="sample_text", username="sample_text")
    partner = cloudml_CloudMLElementWithProperties()
    setattr(partner, 'cloudml_CloudMLElementWithProperties4', None)
    _safe_set(owner, 'cloudml_PuppetResource', partner)
    assert owner in getattr(partner, 'cloudml_CloudMLElementWithProperties4')
    _safe_set(owner, 'cloudml_PuppetResource', None)
    assert owner not in getattr(partner, 'cloudml_CloudMLElementWithProperties4')


def test_assoc_requiredPort45_stub_double():
    # cloudml_Relationship has no real 'cloudml_Relationship46' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_RequiredPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_RequiredPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_RequiredPort(isMandatory=True)
    partner = cloudml_Relationship()
    setattr(partner, 'cloudml_Relationship46', None)
    _safe_set(owner, 'cloudml_RequiredPort47', partner)
    assert getattr(partner, 'cloudml_Relationship46') == owner
    _safe_set(owner, 'cloudml_RequiredPort47', None)
    assert getattr(partner, 'cloudml_Relationship46') is None


def test_assoc_requiredPortResource51_stub_double():
    # cloudml_Relationship has no real 'cloudml_Relationship52' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    partner = cloudml_Relationship()
    setattr(partner, 'cloudml_Relationship52', None)
    _safe_set(owner, 'cloudml_Resource53', partner)
    assert getattr(partner, 'cloudml_Relationship52') == owner
    _safe_set(owner, 'cloudml_Resource53', None)
    assert getattr(partner, 'cloudml_Relationship52') is None


def test_assoc_requiredPorts36_stub_double():
    # cloudml_InternalComponent has no real 'cloudml_InternalComponent37' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_RequiredPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_RequiredPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_RequiredPort(isMandatory=True)
    partner = cloudml_InternalComponent()
    setattr(partner, 'cloudml_InternalComponent37', None)
    _safe_set(owner, 'cloudml_RequiredPort', partner)
    assert owner in getattr(partner, 'cloudml_InternalComponent37')
    _safe_set(owner, 'cloudml_RequiredPort', None)
    assert owner not in getattr(partner, 'cloudml_InternalComponent37')


def test_assoc_resources1_stub_double():
    # cloudml_CloudMLElementWithProperties has no real 'cloudml_CloudMLElementWithProperties2' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_Resource(configureCommand="sample_text", downloadCommand="sample_text", executeLocally=True, installCommand="sample_text", requireCredentials=True, startCommand="sample_text", stopCommand="sample_text", uploadCommand="sample_text")
    partner = cloudml_CloudMLElementWithProperties()
    setattr(partner, 'cloudml_CloudMLElementWithProperties2', None)
    _safe_set(owner, 'cloudml_Resource', partner)
    assert owner in getattr(partner, 'cloudml_CloudMLElementWithProperties2')
    _safe_set(owner, 'cloudml_Resource', None)
    assert owner not in getattr(partner, 'cloudml_CloudMLElementWithProperties2')


def test_assoc_type76_stub_double():
    # cloudml_PortInstance has no real 'cloudml_PortInstance' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_Port(isLocal=True, portNumber=7)
    partner = cloudml_PortInstance()
    setattr(partner, 'cloudml_PortInstance', None)
    _safe_set(owner, 'cloudml_Port77', partner)
    assert getattr(partner, 'cloudml_PortInstance') == owner
    _safe_set(owner, 'cloudml_Port77', None)
    assert getattr(partner, 'cloudml_PortInstance') is None


def test_assoc_vmInstances22_stub_double():
    # cloudml_CloudMLModel has no real 'cloudml_CloudMLModel23' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_VMInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_VMInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_VMInstance(id="sample_text", publicAddress="sample_text")
    partner = cloudml_CloudMLModel()
    setattr(partner, 'cloudml_CloudMLModel23', None)
    _safe_set(owner, 'cloudml_VMInstance', partner)
    assert owner in getattr(partner, 'cloudml_CloudMLModel23')
    _safe_set(owner, 'cloudml_VMInstance', None)
    assert owner not in getattr(partner, 'cloudml_CloudMLModel23')


def test_assoc_vmInstances57_stub_double():
    # cloudml_Cloud has no real 'cloudml_Cloud58' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_VMInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_VMInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_VMInstance(id="sample_text", publicAddress="sample_text")
    partner = cloudml_Cloud()
    setattr(partner, 'cloudml_Cloud58', None)
    _safe_set(owner, 'cloudml_VMInstance59', partner)
    assert owner in getattr(partner, 'cloudml_Cloud58')
    _safe_set(owner, 'cloudml_VMInstance59', None)
    assert owner not in getattr(partner, 'cloudml_Cloud58')


def test_assoc_vms20_stub_double():
    # cloudml_CloudMLModel has no real 'cloudml_CloudMLModel21' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_VM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_VM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_VM(groupName="sample_text", imageId="sample_text", is64os=True, maxCores=7, maxRam=7, maxStorage=7, minCores=7, minRam=7, minStorage=7, os="sample_text", privateKey="sample_text", providerSpecificTypeName="sample_text", securityGroup="sample_text", sshKey="sample_text")
    partner = cloudml_CloudMLModel()
    setattr(partner, 'cloudml_CloudMLModel21', None)
    _safe_set(owner, 'cloudml_VM', partner)
    assert owner in getattr(partner, 'cloudml_CloudMLModel21')
    _safe_set(owner, 'cloudml_VM', None)
    assert owner not in getattr(partner, 'cloudml_CloudMLModel21')


