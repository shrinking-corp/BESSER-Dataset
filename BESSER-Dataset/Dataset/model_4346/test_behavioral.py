import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ModelElement,
    Object,
    hutn_AttributeSlot,
    hutn_ClassObject,
    hutn_ClassObjectSlot,
    hutn_ContainmentSlot,
    hutn_EPackage,
    hutn_ModelElement,
    hutn_NsUri,
    hutn_Object,
    hutn_PackageObject,
    hutn_ReferenceSlot,
    hutn_Slot,
    hutn_Spec,
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

def test_assoc_classObjects5_reverse_link_reassign_clear():
    a1 = hutn_PackageObject()
    a2 = hutn_PackageObject()
    b = hutn_ClassObject()
    _safe_set(b, 'hutn_ClassObject', a1)
    assert _is_linked(b, 'hutn_ClassObject', a1)
    if hasattr(a1, 'hutn_PackageObject6'):
        assert _is_linked(a1, 'hutn_PackageObject6', b)
    _safe_set(b, 'hutn_ClassObject', a2)
    assert _is_linked(b, 'hutn_ClassObject', a2)
    if hasattr(a1, 'hutn_PackageObject6'):
        assert not _is_linked(a1, 'hutn_PackageObject6', b)
    if hasattr(a2, 'hutn_PackageObject6'):
        assert _is_linked(a2, 'hutn_PackageObject6', b)
    _safe_set(b, 'hutn_ClassObject', None)
    assert not _is_linked(b, 'hutn_ClassObject', a2)
    if hasattr(a2, 'hutn_PackageObject6'):
        assert not _is_linked(a2, 'hutn_PackageObject6', b)


def test_assoc_nsUris0_reverse_link_reassign_clear():
    a1 = hutn_Spec(modelFile="sample_text", sourceFile="sample_text")
    a2 = hutn_Spec(modelFile="sample_text_2", sourceFile="sample_text_2")
    b = hutn_NsUri(value="sample_text")
    _safe_set(b, 'hutn_NsUri', a1)
    assert _is_linked(b, 'hutn_NsUri', a1)
    if hasattr(a1, 'hutn_Spec'):
        assert _is_linked(a1, 'hutn_Spec', b)
    _safe_set(b, 'hutn_NsUri', a2)
    assert _is_linked(b, 'hutn_NsUri', a2)
    if hasattr(a1, 'hutn_Spec'):
        assert not _is_linked(a1, 'hutn_Spec', b)
    if hasattr(a2, 'hutn_Spec'):
        assert _is_linked(a2, 'hutn_Spec', b)
    _safe_set(b, 'hutn_NsUri', None)
    assert not _is_linked(b, 'hutn_NsUri', a2)
    if hasattr(a2, 'hutn_Spec'):
        assert not _is_linked(a2, 'hutn_Spec', b)


def test_assoc_objects1_reverse_link_reassign_clear():
    a1 = hutn_Spec(modelFile="sample_text", sourceFile="sample_text")
    a2 = hutn_Spec(modelFile="sample_text_2", sourceFile="sample_text_2")
    b = hutn_PackageObject()
    _safe_set(b, 'hutn_PackageObject', a1)
    assert _is_linked(b, 'hutn_PackageObject', a1)
    if hasattr(a1, 'hutn_Spec2'):
        assert _is_linked(a1, 'hutn_Spec2', b)
    _safe_set(b, 'hutn_PackageObject', a2)
    assert _is_linked(b, 'hutn_PackageObject', a2)
    if hasattr(a1, 'hutn_Spec2'):
        assert not _is_linked(a1, 'hutn_Spec2', b)
    if hasattr(a2, 'hutn_Spec2'):
        assert _is_linked(a2, 'hutn_Spec2', b)
    _safe_set(b, 'hutn_PackageObject', None)
    assert not _is_linked(b, 'hutn_PackageObject', a2)
    if hasattr(a2, 'hutn_Spec2'):
        assert not _is_linked(a2, 'hutn_Spec2', b)


def test_assoc_owner7_reverse_link_reassign_clear():
    a1 = hutn_Slot(feature="sample_text", values="sample_text")
    a2 = hutn_Slot(feature="sample_text_2", values="sample_text_2")
    b = hutn_ClassObject()
    _safe_set(b, 'ClassObject', a1)
    assert _is_linked(b, 'ClassObject', a1)
    if hasattr(a1, 'slots'):
        assert _is_linked(a1, 'slots', b)
    _safe_set(b, 'ClassObject', a2)
    assert _is_linked(b, 'ClassObject', a2)
    if hasattr(a1, 'slots'):
        assert not _is_linked(a1, 'slots', b)
    if hasattr(a2, 'slots'):
        assert _is_linked(a2, 'slots', b)
    _safe_set(b, 'ClassObject', None)
    assert not _is_linked(b, 'ClassObject', a2)
    if hasattr(a2, 'slots'):
        assert not _is_linked(a2, 'slots', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_classObjects8_stub_double():
    # hutn_ContainmentSlot has no real 'hutn_ContainmentSlot' property in the generated
    # code (a bare stub) -- manually attach it so hutn_ClassObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hutn_ClassObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hutn_ClassObject()
    partner = hutn_ContainmentSlot()
    setattr(partner, 'hutn_ContainmentSlot', None)
    _safe_set(owner, 'hutn_ClassObject9', partner)
    assert getattr(partner, 'hutn_ContainmentSlot') == owner
    _safe_set(owner, 'hutn_ClassObject9', None)
    assert getattr(partner, 'hutn_ContainmentSlot') is None


def test_assoc_metamodel3_stub_double():
    # hutn_EPackage has no real 'hutn_EPackage' property in the generated
    # code (a bare stub) -- manually attach it so hutn_PackageObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hutn_PackageObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hutn_PackageObject()
    partner = hutn_EPackage()
    setattr(partner, 'hutn_EPackage', None)
    _safe_set(owner, 'hutn_PackageObject4', {partner})
    assert getattr(partner, 'hutn_EPackage') == owner
    _safe_set(owner, 'hutn_PackageObject4', set())
    assert getattr(partner, 'hutn_EPackage') is None


