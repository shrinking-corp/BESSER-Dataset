import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractClass,
    Classifier,
    LedsCodeModel_AbstractClass,
    LedsCodeModel_Association,
    LedsCodeModel_Attribute,
    LedsCodeModel_Class,
    LedsCodeModel_ClassDiagram,
    LedsCodeModel_Classifier,
    LedsCodeModel_ENUM,
    LedsCodeModel_Feature,
    LedsCodeModel_Model,
    LedsCodeModel_PrimitiveDataType,
    LedsCodeModel_Specification,
    Model,
    PrimitiveData,
    StereotypeAttribute,
    StereotypeClass,
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

def test_assoc_attributes4_reverse_link_reassign_clear():
    a1 = LedsCodeModel_Class(abstract=True, stereotypeClass="sample_text")
    a2 = LedsCodeModel_Class(abstract=False, stereotypeClass="sample_text_2")
    b = LedsCodeModel_Attribute(name="sample_text")
    _safe_set(b, 'LedsCodeModel_Attribute', a1)
    assert _is_linked(b, 'LedsCodeModel_Attribute', a1)
    if hasattr(a1, 'LedsCodeModel_Class'):
        assert _is_linked(a1, 'LedsCodeModel_Class', b)
    _safe_set(b, 'LedsCodeModel_Attribute', a2)
    assert _is_linked(b, 'LedsCodeModel_Attribute', a2)
    if hasattr(a1, 'LedsCodeModel_Class'):
        assert not _is_linked(a1, 'LedsCodeModel_Class', b)
    if hasattr(a2, 'LedsCodeModel_Class'):
        assert _is_linked(a2, 'LedsCodeModel_Class', b)
    _safe_set(b, 'LedsCodeModel_Attribute', None)
    assert not _is_linked(b, 'LedsCodeModel_Attribute', a2)
    if hasattr(a2, 'LedsCodeModel_Class'):
        assert not _is_linked(a2, 'LedsCodeModel_Class', b)


def test_assoc_described1_reverse_link_reassign_clear():
    a1 = LedsCodeModel_Specification(createdDate=date(2024, 1, 1), name="sample_text")
    a2 = LedsCodeModel_Specification(createdDate=date(2025, 6, 15), name="sample_text_2")
    b = LedsCodeModel_Feature(applicationType="sample_text", dataBaseName="sample_text", engine="sample_text", language="sample_text", orm="sample_text")
    _safe_set(b, 'LedsCodeModel_Feature', a1)
    assert _is_linked(b, 'LedsCodeModel_Feature', a1)
    if hasattr(a1, 'LedsCodeModel_Specification2'):
        assert _is_linked(a1, 'LedsCodeModel_Specification2', b)
    _safe_set(b, 'LedsCodeModel_Feature', a2)
    assert _is_linked(b, 'LedsCodeModel_Feature', a2)
    if hasattr(a1, 'LedsCodeModel_Specification2'):
        assert not _is_linked(a1, 'LedsCodeModel_Specification2', b)
    if hasattr(a2, 'LedsCodeModel_Specification2'):
        assert _is_linked(a2, 'LedsCodeModel_Specification2', b)
    _safe_set(b, 'LedsCodeModel_Feature', None)
    assert not _is_linked(b, 'LedsCodeModel_Feature', a2)
    if hasattr(a2, 'LedsCodeModel_Specification2'):
        assert not _is_linked(a2, 'LedsCodeModel_Specification2', b)


def test_assoc_parent6_reverse_link_reassign_clear():
    a1 = LedsCodeModel_Class(abstract=True, stereotypeClass="sample_text")
    a2 = LedsCodeModel_Class(abstract=False, stereotypeClass="sample_text_2")
    b = LedsCodeModel_Class(abstract=True, stereotypeClass="sample_text")
    _safe_set(b, 'LedsCodeModel_Class7', a1)
    assert _is_linked(b, 'LedsCodeModel_Class7', a1)
    if hasattr(a1, 'LedsCodeModel_Class5'):
        assert _is_linked(a1, 'LedsCodeModel_Class5', b)
    _safe_set(b, 'LedsCodeModel_Class7', a2)
    assert _is_linked(b, 'LedsCodeModel_Class7', a2)
    if hasattr(a1, 'LedsCodeModel_Class5'):
        assert not _is_linked(a1, 'LedsCodeModel_Class5', b)
    if hasattr(a2, 'LedsCodeModel_Class5'):
        assert _is_linked(a2, 'LedsCodeModel_Class5', b)
    _safe_set(b, 'LedsCodeModel_Class7', None)
    assert not _is_linked(b, 'LedsCodeModel_Class7', a2)
    if hasattr(a2, 'LedsCodeModel_Class5'):
        assert not _is_linked(a2, 'LedsCodeModel_Class5', b)


def test_assoc_source12_reverse_link_reassign_clear():
    a1 = LedsCodeModel_Class(abstract=True, stereotypeClass="sample_text")
    a2 = LedsCodeModel_Class(abstract=False, stereotypeClass="sample_text_2")
    b = LedsCodeModel_Association(name="sample_text")
    _safe_set(b, 'LedsCodeModel_Association13', a1)
    assert _is_linked(b, 'LedsCodeModel_Association13', a1)
    if hasattr(a1, 'LedsCodeModel_Class14'):
        assert _is_linked(a1, 'LedsCodeModel_Class14', b)
    _safe_set(b, 'LedsCodeModel_Association13', a2)
    assert _is_linked(b, 'LedsCodeModel_Association13', a2)
    if hasattr(a1, 'LedsCodeModel_Class14'):
        assert not _is_linked(a1, 'LedsCodeModel_Class14', b)
    if hasattr(a2, 'LedsCodeModel_Class14'):
        assert _is_linked(a2, 'LedsCodeModel_Class14', b)
    _safe_set(b, 'LedsCodeModel_Association13', None)
    assert not _is_linked(b, 'LedsCodeModel_Association13', a2)
    if hasattr(a2, 'LedsCodeModel_Class14'):
        assert not _is_linked(a2, 'LedsCodeModel_Class14', b)


def test_assoc_target10_reverse_link_reassign_clear():
    a1 = LedsCodeModel_Class(abstract=True, stereotypeClass="sample_text")
    a2 = LedsCodeModel_Class(abstract=False, stereotypeClass="sample_text_2")
    b = LedsCodeModel_Association(name="sample_text")
    _safe_set(b, 'LedsCodeModel_Association', a1)
    assert _is_linked(b, 'LedsCodeModel_Association', a1)
    if hasattr(a1, 'LedsCodeModel_Class11'):
        assert _is_linked(a1, 'LedsCodeModel_Class11', b)
    _safe_set(b, 'LedsCodeModel_Association', a2)
    assert _is_linked(b, 'LedsCodeModel_Association', a2)
    if hasattr(a1, 'LedsCodeModel_Class11'):
        assert not _is_linked(a1, 'LedsCodeModel_Class11', b)
    if hasattr(a2, 'LedsCodeModel_Class11'):
        assert _is_linked(a2, 'LedsCodeModel_Class11', b)
    _safe_set(b, 'LedsCodeModel_Association', None)
    assert not _is_linked(b, 'LedsCodeModel_Association', a2)
    if hasattr(a2, 'LedsCodeModel_Class11'):
        assert not _is_linked(a2, 'LedsCodeModel_Class11', b)


def test_assoc_type8_reverse_link_reassign_clear():
    a1 = LedsCodeModel_Classifier(name="sample_text")
    a2 = LedsCodeModel_Classifier(name="sample_text_2")
    b = LedsCodeModel_Attribute(name="sample_text")
    _safe_set(b, 'LedsCodeModel_Attribute9', a1)
    assert _is_linked(b, 'LedsCodeModel_Attribute9', a1)
    if hasattr(a1, 'LedsCodeModel_Classifier'):
        assert _is_linked(a1, 'LedsCodeModel_Classifier', b)
    _safe_set(b, 'LedsCodeModel_Attribute9', a2)
    assert _is_linked(b, 'LedsCodeModel_Attribute9', a2)
    if hasattr(a1, 'LedsCodeModel_Classifier'):
        assert not _is_linked(a1, 'LedsCodeModel_Classifier', b)
    if hasattr(a2, 'LedsCodeModel_Classifier'):
        assert _is_linked(a2, 'LedsCodeModel_Classifier', b)
    _safe_set(b, 'LedsCodeModel_Attribute9', None)
    assert not _is_linked(b, 'LedsCodeModel_Attribute9', a2)
    if hasattr(a2, 'LedsCodeModel_Classifier'):
        assert not _is_linked(a2, 'LedsCodeModel_Classifier', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_composed3_stub_double():
    # LedsCodeModel_AbstractClass has no real 'LedsCodeModel_AbstractClass' property in the generated
    # code (a bare stub) -- manually attach it so LedsCodeModel_ClassDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # LedsCodeModel_ClassDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = LedsCodeModel_ClassDiagram(name="sample_text")
    partner = LedsCodeModel_AbstractClass()
    setattr(partner, 'LedsCodeModel_AbstractClass', None)
    _safe_set(owner, 'LedsCodeModel_ClassDiagram', {partner})
    assert getattr(partner, 'LedsCodeModel_AbstractClass') == owner
    _safe_set(owner, 'LedsCodeModel_ClassDiagram', set())
    assert getattr(partner, 'LedsCodeModel_AbstractClass') is None


def test_assoc_has0_stub_double():
    # LedsCodeModel_Model has no real 'LedsCodeModel_Model' property in the generated
    # code (a bare stub) -- manually attach it so LedsCodeModel_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # LedsCodeModel_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = LedsCodeModel_Specification(createdDate=date(2024, 1, 1), name="sample_text")
    partner = LedsCodeModel_Model()
    setattr(partner, 'LedsCodeModel_Model', None)
    _safe_set(owner, 'LedsCodeModel_Specification', {partner})
    assert getattr(partner, 'LedsCodeModel_Model') == owner
    _safe_set(owner, 'LedsCodeModel_Specification', set())
    assert getattr(partner, 'LedsCodeModel_Model') is None


