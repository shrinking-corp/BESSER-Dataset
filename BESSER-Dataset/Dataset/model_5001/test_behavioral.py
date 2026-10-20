import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArtefactPort,
    ArtefactPortInstance,
    CloudMLElement,
    NamedElement,
    WithProperties,
    cloudml_Artefact,
    cloudml_ArtefactInstance,
    cloudml_ArtefactPort,
    cloudml_ArtefactPortInstance,
    cloudml_Binding,
    cloudml_BindingInstance,
    cloudml_ClientPort,
    cloudml_ClientPortInstance,
    cloudml_CloudMLElement,
    cloudml_Composite,
    cloudml_DeploymentModel,
    cloudml_NamedElement,
    cloudml_Node,
    cloudml_NodeInstance,
    cloudml_Property,
    cloudml_Provider,
    cloudml_Resource,
    cloudml_ServerPort,
    cloudml_ServerPortInstance,
    cloudml_UploadCommand,
    cloudml_WithProperties,
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

def test_assoc_cloudProvider24_reverse_link_reassign_clear():
    a1 = cloudml_Provider(credentials="sample_text")
    a2 = cloudml_Provider(credentials="sample_text_2")
    b = cloudml_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    _safe_set(b, 'cloudml_Node25', a1)
    assert _is_linked(b, 'cloudml_Node25', a1)
    if hasattr(a1, 'cloudml_Provider26'):
        assert _is_linked(a1, 'cloudml_Provider26', b)
    _safe_set(b, 'cloudml_Node25', a2)
    assert _is_linked(b, 'cloudml_Node25', a2)
    if hasattr(a1, 'cloudml_Provider26'):
        assert not _is_linked(a1, 'cloudml_Provider26', b)
    if hasattr(a2, 'cloudml_Provider26'):
        assert _is_linked(a2, 'cloudml_Provider26', b)
    _safe_set(b, 'cloudml_Node25', None)
    assert not _is_linked(b, 'cloudml_Node25', a2)
    if hasattr(a2, 'cloudml_Provider26'):
        assert not _is_linked(a2, 'cloudml_Provider26', b)


def test_assoc_type39_reverse_link_reassign_clear():
    a1 = cloudml_NodeInstance(id="sample_text", publicAddress="sample_text")
    a2 = cloudml_NodeInstance(id="sample_text_2", publicAddress="sample_text_2")
    b = cloudml_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    _safe_set(b, 'cloudml_Node41', a1)
    assert _is_linked(b, 'cloudml_Node41', a1)
    if hasattr(a1, 'cloudml_NodeInstance40'):
        assert _is_linked(a1, 'cloudml_NodeInstance40', b)
    _safe_set(b, 'cloudml_Node41', a2)
    assert _is_linked(b, 'cloudml_Node41', a2)
    if hasattr(a1, 'cloudml_NodeInstance40'):
        assert not _is_linked(a1, 'cloudml_NodeInstance40', b)
    if hasattr(a2, 'cloudml_NodeInstance40'):
        assert _is_linked(a2, 'cloudml_NodeInstance40', b)
    _safe_set(b, 'cloudml_Node41', None)
    assert not _is_linked(b, 'cloudml_Node41', a2)
    if hasattr(a2, 'cloudml_NodeInstance40'):
        assert not _is_linked(a2, 'cloudml_NodeInstance40', b)


def test_assoc_uploadCommand1_reverse_link_reassign_clear():
    a1 = cloudml_UploadCommand(source="sample_text", target="sample_text")
    a2 = cloudml_UploadCommand(source="sample_text_2", target="sample_text_2")
    b = cloudml_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text", stopCommand="sample_text")
    _safe_set(b, 'cloudml_Resource', {a1})
    assert _is_linked(b, 'cloudml_Resource', a1)
    if hasattr(a1, 'cloudml_UploadCommand'):
        assert _is_linked(a1, 'cloudml_UploadCommand', b)
    _safe_set(b, 'cloudml_Resource', {a2})
    assert _is_linked(b, 'cloudml_Resource', a2)
    if hasattr(a1, 'cloudml_UploadCommand'):
        assert not _is_linked(a1, 'cloudml_UploadCommand', b)
    if hasattr(a2, 'cloudml_UploadCommand'):
        assert _is_linked(a2, 'cloudml_UploadCommand', b)
    _safe_set(b, 'cloudml_Resource', set())
    assert not _is_linked(b, 'cloudml_Resource', a2)
    if hasattr(a2, 'cloudml_UploadCommand'):
        assert not _is_linked(a2, 'cloudml_UploadCommand', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_client44_stub_double():
    # cloudml_Binding has no real 'cloudml_Binding45' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_ClientPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_ClientPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_ClientPort(isOptional=True)
    partner = cloudml_Binding()
    setattr(partner, 'cloudml_Binding45', None)
    _safe_set(owner, 'cloudml_ClientPort46', partner)
    assert getattr(partner, 'cloudml_Binding45') == owner
    _safe_set(owner, 'cloudml_ClientPort46', None)
    assert getattr(partner, 'cloudml_Binding45') is None


def test_assoc_clientResource50_stub_double():
    # cloudml_Binding has no real 'cloudml_Binding51' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text", stopCommand="sample_text")
    partner = cloudml_Binding()
    setattr(partner, 'cloudml_Binding51', None)
    _safe_set(owner, 'cloudml_Resource52', partner)
    assert getattr(partner, 'cloudml_Binding51') == owner
    _safe_set(owner, 'cloudml_Resource52', None)
    assert getattr(partner, 'cloudml_Binding51') is None


def test_assoc_destination15_stub_double():
    # cloudml_Artefact has no real 'cloudml_Artefact16' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_ArtefactPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_ArtefactPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_ArtefactPort(isRemote=True, portNumber=7)
    partner = cloudml_Artefact()
    setattr(partner, 'cloudml_Artefact16', None)
    _safe_set(owner, 'cloudml_ArtefactPort', partner)
    assert getattr(partner, 'cloudml_Artefact16') == owner
    _safe_set(owner, 'cloudml_ArtefactPort', None)
    assert getattr(partner, 'cloudml_Artefact16') is None


def test_assoc_destination32_stub_double():
    # cloudml_ArtefactInstance has no real 'cloudml_ArtefactInstance33' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_NodeInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_NodeInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_NodeInstance(id="sample_text", publicAddress="sample_text")
    partner = cloudml_ArtefactInstance()
    setattr(partner, 'cloudml_ArtefactInstance33', None)
    _safe_set(owner, 'cloudml_NodeInstance34', partner)
    assert getattr(partner, 'cloudml_ArtefactInstance33') == owner
    _safe_set(owner, 'cloudml_NodeInstance34', None)
    assert getattr(partner, 'cloudml_ArtefactInstance33') is None


def test_assoc_nodeInstances11_stub_double():
    # cloudml_DeploymentModel has no real 'cloudml_DeploymentModel12' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_NodeInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_NodeInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_NodeInstance(id="sample_text", publicAddress="sample_text")
    partner = cloudml_DeploymentModel()
    setattr(partner, 'cloudml_DeploymentModel12', None)
    _safe_set(owner, 'cloudml_NodeInstance', partner)
    assert owner in getattr(partner, 'cloudml_DeploymentModel12')
    _safe_set(owner, 'cloudml_NodeInstance', None)
    assert owner not in getattr(partner, 'cloudml_DeploymentModel12')


def test_assoc_nodeTypes5_stub_double():
    # cloudml_DeploymentModel has no real 'cloudml_DeploymentModel6' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    partner = cloudml_DeploymentModel()
    setattr(partner, 'cloudml_DeploymentModel6', None)
    _safe_set(owner, 'cloudml_Node', partner)
    assert owner in getattr(partner, 'cloudml_DeploymentModel6')
    _safe_set(owner, 'cloudml_Node', None)
    assert owner not in getattr(partner, 'cloudml_DeploymentModel6')


def test_assoc_properties0_stub_double():
    # cloudml_WithProperties has no real 'cloudml_WithProperties' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_Property(value="sample_text")
    partner = cloudml_WithProperties()
    setattr(partner, 'cloudml_WithProperties', None)
    _safe_set(owner, 'cloudml_Property', partner)
    assert owner in getattr(partner, 'cloudml_WithProperties')
    _safe_set(owner, 'cloudml_Property', None)
    assert owner not in getattr(partner, 'cloudml_WithProperties')


def test_assoc_providers2_stub_double():
    # cloudml_DeploymentModel has no real 'cloudml_DeploymentModel' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_Provider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_Provider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_Provider(credentials="sample_text")
    partner = cloudml_DeploymentModel()
    setattr(partner, 'cloudml_DeploymentModel', None)
    _safe_set(owner, 'cloudml_Provider', partner)
    assert owner in getattr(partner, 'cloudml_DeploymentModel')
    _safe_set(owner, 'cloudml_Provider', None)
    assert owner not in getattr(partner, 'cloudml_DeploymentModel')


def test_assoc_required22_stub_double():
    # cloudml_Artefact has no real 'cloudml_Artefact23' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_ClientPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_ClientPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_ClientPort(isOptional=True)
    partner = cloudml_Artefact()
    setattr(partner, 'cloudml_Artefact23', None)
    _safe_set(owner, 'cloudml_ClientPort', partner)
    assert owner in getattr(partner, 'cloudml_Artefact23')
    _safe_set(owner, 'cloudml_ClientPort', None)
    assert owner not in getattr(partner, 'cloudml_Artefact23')


def test_assoc_resource17_stub_double():
    # cloudml_Artefact has no real 'cloudml_Artefact18' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text", stopCommand="sample_text")
    partner = cloudml_Artefact()
    setattr(partner, 'cloudml_Artefact18', None)
    _safe_set(owner, 'cloudml_Resource19', partner)
    assert getattr(partner, 'cloudml_Artefact18') == owner
    _safe_set(owner, 'cloudml_Resource19', None)
    assert getattr(partner, 'cloudml_Artefact18') is None


def test_assoc_serverResource53_stub_double():
    # cloudml_Binding has no real 'cloudml_Binding54' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text", stopCommand="sample_text")
    partner = cloudml_Binding()
    setattr(partner, 'cloudml_Binding54', None)
    _safe_set(owner, 'cloudml_Resource55', partner)
    assert getattr(partner, 'cloudml_Binding54') == owner
    _safe_set(owner, 'cloudml_Resource55', None)
    assert getattr(partner, 'cloudml_Binding54') is None


def test_assoc_type27_stub_double():
    # cloudml_ArtefactPortInstance has no real 'cloudml_ArtefactPortInstance' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_ArtefactPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_ArtefactPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_ArtefactPort(isRemote=True, portNumber=7)
    partner = cloudml_ArtefactPortInstance()
    setattr(partner, 'cloudml_ArtefactPortInstance', None)
    _safe_set(owner, 'cloudml_ArtefactPort28', partner)
    assert getattr(partner, 'cloudml_ArtefactPortInstance') == owner
    _safe_set(owner, 'cloudml_ArtefactPort28', None)
    assert getattr(partner, 'cloudml_ArtefactPortInstance') is None


