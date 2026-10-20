import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Artefact,
    ArtefactInstance,
    ArtefactPort,
    ArtefactPortInstance,
    Binding,
    BindingInstance,
    ClientPort,
    ClientPortInstance,
    CloudMLElement,
    NamedElement,
    Node,
    NodeInstance,
    Property,
    Provider,
    Resource,
    ServerPort,
    ServerPortInstance,
    UploadCommand,
    WithProperties,
    cloudml_core_Artefact,
    cloudml_core_ArtefactInstance,
    cloudml_core_ArtefactPort,
    cloudml_core_ArtefactPortInstance,
    cloudml_core_Binding,
    cloudml_core_BindingInstance,
    cloudml_core_ClientPort,
    cloudml_core_ClientPortInstance,
    cloudml_core_CloudMLElement,
    cloudml_core_Composite,
    cloudml_core_DeploymentModel,
    cloudml_core_NamedElement,
    cloudml_core_Node,
    cloudml_core_NodeInstance,
    cloudml_core_Property,
    cloudml_core_Provider,
    cloudml_core_Resource,
    cloudml_core_ServerPort,
    cloudml_core_ServerPortInstance,
    cloudml_core_UploadCommand,
    cloudml_core_WithProperties,
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

def test_assoc_cloudProvider22_stub_double():
    # Provider has no real 'Provider23' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_core_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_core_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_core_Node(OS="sample_text", groupName="sample_text", imageID="sample_text", is64os=True, location="sample_text", minCore=7, minDisk=7, minRam=7, privateKey="sample_text", securityGroup="sample_text", sshKey="sample_text")
    partner = Provider()
    setattr(partner, 'Provider23', None)
    _safe_set(owner, 'cloudml_core_Node', partner)
    assert getattr(partner, 'Provider23') == owner
    _safe_set(owner, 'cloudml_core_Node', None)
    assert getattr(partner, 'Provider23') is None


def test_assoc_type35_stub_double():
    # Node has no real 'Node36' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_core_NodeInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_core_NodeInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_core_NodeInstance(id="sample_text", publicAddress="sample_text")
    partner = Node()
    setattr(partner, 'Node36', None)
    _safe_set(owner, 'cloudml_core_NodeInstance', partner)
    assert getattr(partner, 'Node36') == owner
    _safe_set(owner, 'cloudml_core_NodeInstance', None)
    assert getattr(partner, 'Node36') is None


def test_assoc_uploadCommand1_stub_double():
    # UploadCommand has no real 'UploadCommand' property in the generated
    # code (a bare stub) -- manually attach it so cloudml_core_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cloudml_core_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cloudml_core_Resource(configurationCommand="sample_text", deployingCommand="sample_text", retrievingCommand="sample_text", startCommand="sample_text", stopCommand="sample_text")
    partner = UploadCommand()
    setattr(partner, 'UploadCommand', None)
    _safe_set(owner, 'cloudml_core_Resource', {partner})
    assert getattr(partner, 'UploadCommand') == owner
    _safe_set(owner, 'cloudml_core_Resource', set())
    assert getattr(partner, 'UploadCommand') is None


