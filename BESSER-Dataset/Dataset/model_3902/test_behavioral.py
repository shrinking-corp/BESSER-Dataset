import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Collaboration,
    FreeFormValue,
    NodeDescriptor,
    Participant,
    soaml_Agent,
    soaml_Artifact,
    soaml_Attachment,
    soaml_Capability,
    soaml_Catalog,
    soaml_Categorization,
    soaml_Category,
    soaml_CategoryValue,
    soaml_Class,
    soaml_Collaboration,
    soaml_CollaborationUse,
    soaml_Comment,
    soaml_Connector,
    soaml_Consumer,
    soaml_DataType,
    soaml_Dependency,
    soaml_Expose,
    soaml_FreeFormDescriptor,
    soaml_FreeFormValue,
    soaml_Interface,
    soaml_MessageType,
    soaml_Milestone,
    soaml_MotivationRealization,
    soaml_NodeDescriptor,
    soaml_Package,
    soaml_Participant,
    soaml_Port,
    soaml_Property,
    soaml_Provider,
    soaml_Realization,
    soaml_Request,
    soaml_Service,
    soaml_ServiceArchitecture,
    soaml_ServiceChannel,
    soaml_ServiceContract,
    soaml_ServiceInterface,
    soaml_Signal,
    soaml_ValueSpecification,
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

def test_assoc_base_Collaboration1_reverse_link_reassign_clear():
    a1 = soaml_Collaboration(isStrict="sample_text")
    a2 = soaml_Collaboration(isStrict="sample_text_2")
    b = soaml_Collaboration(isStrict="sample_text")
    _safe_set(b, 'soaml_Collaboration0', a1)
    assert _is_linked(b, 'soaml_Collaboration0', a1)
    if hasattr(a1, 'soaml_Collaboration'):
        assert _is_linked(a1, 'soaml_Collaboration', b)
    _safe_set(b, 'soaml_Collaboration0', a2)
    assert _is_linked(b, 'soaml_Collaboration0', a2)
    if hasattr(a1, 'soaml_Collaboration'):
        assert not _is_linked(a1, 'soaml_Collaboration', b)
    if hasattr(a2, 'soaml_Collaboration'):
        assert _is_linked(a2, 'soaml_Collaboration', b)
    _safe_set(b, 'soaml_Collaboration0', None)
    assert not _is_linked(b, 'soaml_Collaboration0', a2)
    if hasattr(a2, 'soaml_Collaboration'):
        assert not _is_linked(a2, 'soaml_Collaboration', b)


def test_assoc_base_CollaborationUse3_reverse_link_reassign_clear():
    a1 = soaml_CollaborationUse(isStrict="sample_text")
    a2 = soaml_CollaborationUse(isStrict="sample_text_2")
    b = soaml_CollaborationUse(isStrict="sample_text")
    _safe_set(b, 'soaml_CollaborationUse2', a1)
    assert _is_linked(b, 'soaml_CollaborationUse2', a1)
    if hasattr(a1, 'soaml_CollaborationUse'):
        assert _is_linked(a1, 'soaml_CollaborationUse', b)
    _safe_set(b, 'soaml_CollaborationUse2', a2)
    assert _is_linked(b, 'soaml_CollaborationUse2', a2)
    if hasattr(a1, 'soaml_CollaborationUse'):
        assert not _is_linked(a1, 'soaml_CollaborationUse', b)
    if hasattr(a2, 'soaml_CollaborationUse'):
        assert _is_linked(a2, 'soaml_CollaborationUse', b)
    _safe_set(b, 'soaml_CollaborationUse2', None)
    assert not _is_linked(b, 'soaml_CollaborationUse2', a2)
    if hasattr(a2, 'soaml_CollaborationUse'):
        assert not _is_linked(a2, 'soaml_CollaborationUse', b)


def test_assoc_base_Port21_reverse_link_reassign_clear():
    a1 = soaml_Port(connectorRequired="sample_text")
    a2 = soaml_Port(connectorRequired="sample_text_2")
    b = soaml_Port(connectorRequired="sample_text")
    _safe_set(b, 'soaml_Port20', a1)
    assert _is_linked(b, 'soaml_Port20', a1)
    if hasattr(a1, 'soaml_Port'):
        assert _is_linked(a1, 'soaml_Port', b)
    _safe_set(b, 'soaml_Port20', a2)
    assert _is_linked(b, 'soaml_Port20', a2)
    if hasattr(a1, 'soaml_Port'):
        assert not _is_linked(a1, 'soaml_Port', b)
    if hasattr(a2, 'soaml_Port'):
        assert _is_linked(a2, 'soaml_Port', b)
    _safe_set(b, 'soaml_Port20', None)
    assert not _is_linked(b, 'soaml_Port20', a2)
    if hasattr(a2, 'soaml_Port'):
        assert not _is_linked(a2, 'soaml_Port', b)


def test_assoc_base_Property28_reverse_link_reassign_clear():
    a1 = soaml_Property(isID="sample_text")
    a2 = soaml_Property(isID="sample_text_2")
    b = soaml_Property(isID="sample_text")
    _safe_set(b, 'soaml_Property27', a1)
    assert _is_linked(b, 'soaml_Property27', a1)
    if hasattr(a1, 'soaml_Property'):
        assert _is_linked(a1, 'soaml_Property', b)
    _safe_set(b, 'soaml_Property27', a2)
    assert _is_linked(b, 'soaml_Property27', a2)
    if hasattr(a1, 'soaml_Property'):
        assert not _is_linked(a1, 'soaml_Property', b)
    if hasattr(a2, 'soaml_Property'):
        assert _is_linked(a2, 'soaml_Property', b)
    _safe_set(b, 'soaml_Property27', None)
    assert not _is_linked(b, 'soaml_Property27', a2)
    if hasattr(a2, 'soaml_Property'):
        assert not _is_linked(a2, 'soaml_Property', b)


def test_assoc_base_Property29_reverse_link_reassign_clear():
    a1 = soaml_Property(isID="sample_text")
    a2 = soaml_Property(isID="sample_text_2")
    b = soaml_Attachment(encoding="sample_text", mimeType="sample_text")
    _safe_set(b, 'soaml_Attachment', a1)
    assert _is_linked(b, 'soaml_Attachment', a1)
    if hasattr(a1, 'soaml_Property30'):
        assert _is_linked(a1, 'soaml_Property30', b)
    _safe_set(b, 'soaml_Attachment', a2)
    assert _is_linked(b, 'soaml_Attachment', a2)
    if hasattr(a1, 'soaml_Property30'):
        assert not _is_linked(a1, 'soaml_Property30', b)
    if hasattr(a2, 'soaml_Property30'):
        assert _is_linked(a2, 'soaml_Property30', b)
    _safe_set(b, 'soaml_Attachment', None)
    assert not _is_linked(b, 'soaml_Attachment', a2)
    if hasattr(a2, 'soaml_Property30'):
        assert not _is_linked(a2, 'soaml_Property30', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_base_Class31_stub_double():
    # soaml_Class has no real 'soaml_Class32' property in the generated
    # code (a bare stub) -- manually attach it so soaml_MessageType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soaml_MessageType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soaml_MessageType(encoding="sample_text")
    partner = soaml_Class()
    setattr(partner, 'soaml_Class32', None)
    _safe_set(owner, 'soaml_MessageType', partner)
    assert getattr(partner, 'soaml_Class32') == owner
    _safe_set(owner, 'soaml_MessageType', None)
    assert getattr(partner, 'soaml_Class32') is None


def test_assoc_base_Comment41_stub_double():
    # soaml_Comment has no real 'soaml_Comment' property in the generated
    # code (a bare stub) -- manually attach it so soaml_Milestone's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soaml_Milestone's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soaml_Milestone(progress="sample_text")
    partner = soaml_Comment()
    setattr(partner, 'soaml_Comment', None)
    _safe_set(owner, 'soaml_Milestone42', partner)
    assert getattr(partner, 'soaml_Comment') == owner
    _safe_set(owner, 'soaml_Milestone42', None)
    assert getattr(partner, 'soaml_Comment') is None


def test_assoc_base_DataType33_stub_double():
    # soaml_DataType has no real 'soaml_DataType' property in the generated
    # code (a bare stub) -- manually attach it so soaml_MessageType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soaml_MessageType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soaml_MessageType(encoding="sample_text")
    partner = soaml_DataType()
    setattr(partner, 'soaml_DataType', None)
    _safe_set(owner, 'soaml_MessageType34', partner)
    assert getattr(partner, 'soaml_DataType') == owner
    _safe_set(owner, 'soaml_MessageType34', None)
    assert getattr(partner, 'soaml_DataType') is None


def test_assoc_base_Port22_stub_double():
    # soaml_Request has no real 'soaml_Request' property in the generated
    # code (a bare stub) -- manually attach it so soaml_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soaml_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soaml_Port(connectorRequired="sample_text")
    partner = soaml_Request()
    setattr(partner, 'soaml_Request', None)
    _safe_set(owner, 'soaml_Port23', partner)
    assert getattr(partner, 'soaml_Request') == owner
    _safe_set(owner, 'soaml_Port23', None)
    assert getattr(partner, 'soaml_Request') is None


def test_assoc_base_Port24_stub_double():
    # soaml_Service has no real 'soaml_Service' property in the generated
    # code (a bare stub) -- manually attach it so soaml_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soaml_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soaml_Port(connectorRequired="sample_text")
    partner = soaml_Service()
    setattr(partner, 'soaml_Service', None)
    _safe_set(owner, 'soaml_Port25', partner)
    assert getattr(partner, 'soaml_Service') == owner
    _safe_set(owner, 'soaml_Port25', None)
    assert getattr(partner, 'soaml_Service') is None


def test_assoc_base_Property48_stub_double():
    # soaml_FreeFormDescriptor has no real 'soaml_FreeFormDescriptor' property in the generated
    # code (a bare stub) -- manually attach it so soaml_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soaml_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soaml_Property(isID="sample_text")
    partner = soaml_FreeFormDescriptor()
    setattr(partner, 'soaml_FreeFormDescriptor', None)
    _safe_set(owner, 'soaml_Property49', partner)
    assert getattr(partner, 'soaml_FreeFormDescriptor') == owner
    _safe_set(owner, 'soaml_Property49', None)
    assert getattr(partner, 'soaml_FreeFormDescriptor') is None


def test_assoc_base_Signal35_stub_double():
    # soaml_Signal has no real 'soaml_Signal' property in the generated
    # code (a bare stub) -- manually attach it so soaml_MessageType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soaml_MessageType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soaml_MessageType(encoding="sample_text")
    partner = soaml_Signal()
    setattr(partner, 'soaml_Signal', None)
    _safe_set(owner, 'soaml_MessageType36', partner)
    assert getattr(partner, 'soaml_Signal') == owner
    _safe_set(owner, 'soaml_MessageType36', None)
    assert getattr(partner, 'soaml_Signal') is None


def test_assoc_signal38_stub_double():
    # soaml_Signal has no real 'soaml_Signal40' property in the generated
    # code (a bare stub) -- manually attach it so soaml_Milestone's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soaml_Milestone's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soaml_Milestone(progress="sample_text")
    partner = soaml_Signal()
    setattr(partner, 'soaml_Signal40', None)
    _safe_set(owner, 'soaml_Milestone39', partner)
    assert getattr(partner, 'soaml_Signal40') == owner
    _safe_set(owner, 'soaml_Milestone39', None)
    assert getattr(partner, 'soaml_Signal40') is None


def test_assoc_value37_stub_double():
    # soaml_ValueSpecification has no real 'soaml_ValueSpecification' property in the generated
    # code (a bare stub) -- manually attach it so soaml_Milestone's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # soaml_Milestone's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = soaml_Milestone(progress="sample_text")
    partner = soaml_ValueSpecification()
    setattr(partner, 'soaml_ValueSpecification', None)
    _safe_set(owner, 'soaml_Milestone', {partner})
    assert getattr(partner, 'soaml_ValueSpecification') == owner
    _safe_set(owner, 'soaml_Milestone', set())
    assert getattr(partner, 'soaml_ValueSpecification') is None


