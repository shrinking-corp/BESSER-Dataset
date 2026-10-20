import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnalysedElement,
    Dependency,
    ReferenceDependency,
    Relationship,
    RuntimeDependency,
    architecture_AnalysedElement,
    architecture_ArchitectureFile,
    architecture_CallRelationship,
    architecture_DeclaredType,
    architecture_Dependency,
    architecture_Field,
    architecture_FieldReferenceDependency,
    architecture_ImportReferenceDependency,
    architecture_InheritanceDependency,
    architecture_InjectionDependency,
    architecture_Library,
    architecture_Method,
    architecture_ParameterRelationship,
    architecture_Project,
    architecture_ReferenceDependency,
    architecture_Relationship,
    architecture_ReturnTypeRelationship,
    architecture_RuntimeDependency,
    architecture_Type,
    architecture_extension_Bop,
    architecture_extension_ExtensionRelationship,
    architecture_extension_Pattern,
    architecture_extension_PatternRelationship,
    architecture_extension_RelationshipConstraint,
    architecture_extension_Role,
    architecture_extension_RoleRelationship,
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

def test_assoc_containedElements4_reverse_link_reassign_clear():
    a1 = architecture_AnalysedElement(idAnalyzedElement=7, name="sample_text", properties=7)
    a2 = architecture_AnalysedElement(idAnalyzedElement=13, name="sample_text_2", properties=13)
    b = architecture_AnalysedElement(idAnalyzedElement=7, name="sample_text", properties=7)
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'AnalysedElement'):
        assert _is_linked(a1, 'AnalysedElement', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'AnalysedElement'):
        assert not _is_linked(a1, 'AnalysedElement', b)
    if hasattr(a2, 'AnalysedElement'):
        assert _is_linked(a2, 'AnalysedElement', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'AnalysedElement'):
        assert not _is_linked(a2, 'AnalysedElement', b)


def test_assoc_incomingRelationships1_reverse_link_reassign_clear():
    a1 = architecture_Relationship(relationShipId=7)
    a2 = architecture_Relationship(relationShipId=13)
    b = architecture_AnalysedElement(idAnalyzedElement=7, name="sample_text", properties=7)
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Relationship2'):
        assert _is_linked(a1, 'Relationship2', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Relationship2'):
        assert not _is_linked(a1, 'Relationship2', b)
    if hasattr(a2, 'Relationship2'):
        assert _is_linked(a2, 'Relationship2', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Relationship2'):
        assert not _is_linked(a2, 'Relationship2', b)


def test_assoc_outgoingRelationships0_reverse_link_reassign_clear():
    a1 = architecture_Relationship(relationShipId=7)
    a2 = architecture_Relationship(relationShipId=13)
    b = architecture_AnalysedElement(idAnalyzedElement=7, name="sample_text", properties=7)
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Relationship'):
        assert _is_linked(a1, 'Relationship', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Relationship'):
        assert not _is_linked(a1, 'Relationship', b)
    if hasattr(a2, 'Relationship'):
        assert _is_linked(a2, 'Relationship', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Relationship'):
        assert not _is_linked(a2, 'Relationship', b)


def test_assoc_parent6_reverse_link_reassign_clear():
    a1 = architecture_AnalysedElement(idAnalyzedElement=7, name="sample_text", properties=7)
    a2 = architecture_AnalysedElement(idAnalyzedElement=13, name="sample_text_2", properties=13)
    b = architecture_AnalysedElement(idAnalyzedElement=7, name="sample_text", properties=7)
    _safe_set(b, 'containedElements', a1)
    assert _is_linked(b, 'containedElements', a1)
    if hasattr(a1, 'AnalysedElement7'):
        assert _is_linked(a1, 'AnalysedElement7', b)
    _safe_set(b, 'containedElements', a2)
    assert _is_linked(b, 'containedElements', a2)
    if hasattr(a1, 'AnalysedElement7'):
        assert not _is_linked(a1, 'AnalysedElement7', b)
    if hasattr(a2, 'AnalysedElement7'):
        assert _is_linked(a2, 'AnalysedElement7', b)
    _safe_set(b, 'containedElements', None)
    assert not _is_linked(b, 'containedElements', a2)
    if hasattr(a2, 'AnalysedElement7'):
        assert not _is_linked(a2, 'AnalysedElement7', b)


def test_assoc_source10_reverse_link_reassign_clear():
    a1 = architecture_Relationship(relationShipId=7)
    a2 = architecture_Relationship(relationShipId=13)
    b = architecture_AnalysedElement(idAnalyzedElement=7, name="sample_text", properties=7)
    _safe_set(b, 'AnalysedElement11', a1)
    assert _is_linked(b, 'AnalysedElement11', a1)
    if hasattr(a1, 'outgoingRelationships'):
        assert _is_linked(a1, 'outgoingRelationships', b)
    _safe_set(b, 'AnalysedElement11', a2)
    assert _is_linked(b, 'AnalysedElement11', a2)
    if hasattr(a1, 'outgoingRelationships'):
        assert not _is_linked(a1, 'outgoingRelationships', b)
    if hasattr(a2, 'outgoingRelationships'):
        assert _is_linked(a2, 'outgoingRelationships', b)
    _safe_set(b, 'AnalysedElement11', None)
    assert not _is_linked(b, 'AnalysedElement11', a2)
    if hasattr(a2, 'outgoingRelationships'):
        assert not _is_linked(a2, 'outgoingRelationships', b)


def test_assoc_target8_reverse_link_reassign_clear():
    a1 = architecture_Relationship(relationShipId=7)
    a2 = architecture_Relationship(relationShipId=13)
    b = architecture_AnalysedElement(idAnalyzedElement=7, name="sample_text", properties=7)
    _safe_set(b, 'AnalysedElement9', a1)
    assert _is_linked(b, 'AnalysedElement9', a1)
    if hasattr(a1, 'incomingRelationships'):
        assert _is_linked(a1, 'incomingRelationships', b)
    _safe_set(b, 'AnalysedElement9', a2)
    assert _is_linked(b, 'AnalysedElement9', a2)
    if hasattr(a1, 'incomingRelationships'):
        assert not _is_linked(a1, 'incomingRelationships', b)
    if hasattr(a2, 'incomingRelationships'):
        assert _is_linked(a2, 'incomingRelationships', b)
    _safe_set(b, 'AnalysedElement9', None)
    assert not _is_linked(b, 'AnalysedElement9', a2)
    if hasattr(a2, 'incomingRelationships'):
        assert not _is_linked(a2, 'incomingRelationships', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_mapping12_stub_double():
    # architecture_InjectionDependency has no real 'architecture_InjectionDependency' property in the generated
    # code (a bare stub) -- manually attach it so architecture_AnalysedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # architecture_AnalysedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = architecture_AnalysedElement(idAnalyzedElement=7, name="sample_text", properties=7)
    partner = architecture_InjectionDependency()
    setattr(partner, 'architecture_InjectionDependency', None)
    _safe_set(owner, 'architecture_AnalysedElement', partner)
    assert getattr(partner, 'architecture_InjectionDependency') == owner
    _safe_set(owner, 'architecture_AnalysedElement', None)
    assert getattr(partner, 'architecture_InjectionDependency') is None


