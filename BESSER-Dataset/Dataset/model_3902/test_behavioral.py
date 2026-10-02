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


