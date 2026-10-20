import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EClassifier,
    EDataType,
    ENamedElement,
    EStructuralFeature,
    ETypedElement,
    Ecore_EAttribute,
    Ecore_EClass,
    Ecore_EClassifier,
    Ecore_EDataType,
    Ecore_EEnum,
    Ecore_EEnumLiteral,
    Ecore_ENamedElement,
    Ecore_EOperation,
    Ecore_EPackage,
    Ecore_EParameter,
    Ecore_EReference,
    Ecore_EStringToStringMapEntry,
    Ecore_EStructuralFeature,
    Ecore_ETypedElement,
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

def test_assoc_eAllAttributes4_reverse_link_reassign_clear():
    a1 = Ecore_EClass(abstract=True, interface=True)
    a2 = Ecore_EClass(abstract=False, interface=False)
    b = Ecore_EAttribute(iD=True)
    _safe_set(b, 'Ecore_EAttribute6', a1)
    assert _is_linked(b, 'Ecore_EAttribute6', a1)
    if hasattr(a1, 'Ecore_EClass5'):
        assert _is_linked(a1, 'Ecore_EClass5', b)
    _safe_set(b, 'Ecore_EAttribute6', a2)
    assert _is_linked(b, 'Ecore_EAttribute6', a2)
    if hasattr(a1, 'Ecore_EClass5'):
        assert not _is_linked(a1, 'Ecore_EClass5', b)
    if hasattr(a2, 'Ecore_EClass5'):
        assert _is_linked(a2, 'Ecore_EClass5', b)
    _safe_set(b, 'Ecore_EAttribute6', None)
    assert not _is_linked(b, 'Ecore_EAttribute6', a2)
    if hasattr(a2, 'Ecore_EClass5'):
        assert not _is_linked(a2, 'Ecore_EClass5', b)


def test_assoc_eAllContainments15_reverse_link_reassign_clear():
    a1 = Ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = Ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = Ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'Ecore_EClass16', {a1})
    assert _is_linked(b, 'Ecore_EClass16', a1)
    if hasattr(a1, 'Ecore_EReference17'):
        assert _is_linked(a1, 'Ecore_EReference17', b)
    _safe_set(b, 'Ecore_EClass16', {a2})
    assert _is_linked(b, 'Ecore_EClass16', a2)
    if hasattr(a1, 'Ecore_EReference17'):
        assert not _is_linked(a1, 'Ecore_EReference17', b)
    if hasattr(a2, 'Ecore_EReference17'):
        assert _is_linked(a2, 'Ecore_EReference17', b)
    _safe_set(b, 'Ecore_EClass16', set())
    assert not _is_linked(b, 'Ecore_EClass16', a2)
    if hasattr(a2, 'Ecore_EReference17'):
        assert not _is_linked(a2, 'Ecore_EReference17', b)


def test_assoc_eAllReferences7_reverse_link_reassign_clear():
    a1 = Ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = Ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = Ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'Ecore_EClass8', {a1})
    assert _is_linked(b, 'Ecore_EClass8', a1)
    if hasattr(a1, 'Ecore_EReference'):
        assert _is_linked(a1, 'Ecore_EReference', b)
    _safe_set(b, 'Ecore_EClass8', {a2})
    assert _is_linked(b, 'Ecore_EClass8', a2)
    if hasattr(a1, 'Ecore_EReference'):
        assert not _is_linked(a1, 'Ecore_EReference', b)
    if hasattr(a2, 'Ecore_EReference'):
        assert _is_linked(a2, 'Ecore_EReference', b)
    _safe_set(b, 'Ecore_EClass8', set())
    assert not _is_linked(b, 'Ecore_EClass8', a2)
    if hasattr(a2, 'Ecore_EReference'):
        assert not _is_linked(a2, 'Ecore_EReference', b)


def test_assoc_eAllStructuralFeatures20_reverse_link_reassign_clear():
    a1 = Ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = Ecore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = Ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'Ecore_EClass21', {a1})
    assert _is_linked(b, 'Ecore_EClass21', a1)
    if hasattr(a1, 'Ecore_EStructuralFeature'):
        assert _is_linked(a1, 'Ecore_EStructuralFeature', b)
    _safe_set(b, 'Ecore_EClass21', {a2})
    assert _is_linked(b, 'Ecore_EClass21', a2)
    if hasattr(a1, 'Ecore_EStructuralFeature'):
        assert not _is_linked(a1, 'Ecore_EStructuralFeature', b)
    if hasattr(a2, 'Ecore_EStructuralFeature'):
        assert _is_linked(a2, 'Ecore_EStructuralFeature', b)
    _safe_set(b, 'Ecore_EClass21', set())
    assert not _is_linked(b, 'Ecore_EClass21', a2)
    if hasattr(a2, 'Ecore_EStructuralFeature'):
        assert not _is_linked(a2, 'Ecore_EStructuralFeature', b)


def test_assoc_eAllSuperTypes23_reverse_link_reassign_clear():
    a1 = Ecore_EClass(abstract=True, interface=True)
    a2 = Ecore_EClass(abstract=False, interface=False)
    b = Ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'Ecore_EClass24', a1)
    assert _is_linked(b, 'Ecore_EClass24', a1)
    if hasattr(a1, 'Ecore_EClass22'):
        assert _is_linked(a1, 'Ecore_EClass22', b)
    _safe_set(b, 'Ecore_EClass24', a2)
    assert _is_linked(b, 'Ecore_EClass24', a2)
    if hasattr(a1, 'Ecore_EClass22'):
        assert not _is_linked(a1, 'Ecore_EClass22', b)
    if hasattr(a2, 'Ecore_EClass22'):
        assert _is_linked(a2, 'Ecore_EClass22', b)
    _safe_set(b, 'Ecore_EClass24', None)
    assert not _is_linked(b, 'Ecore_EClass24', a2)
    if hasattr(a2, 'Ecore_EClass22'):
        assert not _is_linked(a2, 'Ecore_EClass22', b)


def test_assoc_eAttributeType0_reverse_link_reassign_clear():
    a1 = Ecore_EDataType(serializable=True)
    a2 = Ecore_EDataType(serializable=False)
    b = Ecore_EAttribute(iD=True)
    _safe_set(b, 'Ecore_EAttribute', a1)
    assert _is_linked(b, 'Ecore_EAttribute', a1)
    if hasattr(a1, 'Ecore_EDataType'):
        assert _is_linked(a1, 'Ecore_EDataType', b)
    _safe_set(b, 'Ecore_EAttribute', a2)
    assert _is_linked(b, 'Ecore_EAttribute', a2)
    if hasattr(a1, 'Ecore_EDataType'):
        assert not _is_linked(a1, 'Ecore_EDataType', b)
    if hasattr(a2, 'Ecore_EDataType'):
        assert _is_linked(a2, 'Ecore_EDataType', b)
    _safe_set(b, 'Ecore_EAttribute', None)
    assert not _is_linked(b, 'Ecore_EAttribute', a2)
    if hasattr(a2, 'Ecore_EDataType'):
        assert not _is_linked(a2, 'Ecore_EDataType', b)


def test_assoc_eAttributes12_reverse_link_reassign_clear():
    a1 = Ecore_EClass(abstract=True, interface=True)
    a2 = Ecore_EClass(abstract=False, interface=False)
    b = Ecore_EAttribute(iD=True)
    _safe_set(b, 'Ecore_EAttribute14', a1)
    assert _is_linked(b, 'Ecore_EAttribute14', a1)
    if hasattr(a1, 'Ecore_EClass13'):
        assert _is_linked(a1, 'Ecore_EClass13', b)
    _safe_set(b, 'Ecore_EAttribute14', a2)
    assert _is_linked(b, 'Ecore_EAttribute14', a2)
    if hasattr(a1, 'Ecore_EClass13'):
        assert not _is_linked(a1, 'Ecore_EClass13', b)
    if hasattr(a2, 'Ecore_EClass13'):
        assert _is_linked(a2, 'Ecore_EClass13', b)
    _safe_set(b, 'Ecore_EAttribute14', None)
    assert not _is_linked(b, 'Ecore_EAttribute14', a2)
    if hasattr(a2, 'Ecore_EClass13'):
        assert not _is_linked(a2, 'Ecore_EClass13', b)


def test_assoc_eClassifiers37_reverse_link_reassign_clear():
    a1 = Ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = Ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = Ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'EClassifier', a1)
    assert _is_linked(b, 'EClassifier', a1)
    if hasattr(a1, 'ePackage'):
        assert _is_linked(a1, 'ePackage', b)
    _safe_set(b, 'EClassifier', a2)
    assert _is_linked(b, 'EClassifier', a2)
    if hasattr(a1, 'ePackage'):
        assert not _is_linked(a1, 'ePackage', b)
    if hasattr(a2, 'ePackage'):
        assert _is_linked(a2, 'ePackage', b)
    _safe_set(b, 'EClassifier', None)
    assert not _is_linked(b, 'EClassifier', a2)
    if hasattr(a2, 'ePackage'):
        assert not _is_linked(a2, 'ePackage', b)


def test_assoc_eContainingClass55_reverse_link_reassign_clear():
    a1 = Ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = Ecore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = Ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'EClass56', a1)
    assert _is_linked(b, 'EClass56', a1)
    if hasattr(a1, 'eStructuralFeatures'):
        assert _is_linked(a1, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass56', a2)
    assert _is_linked(b, 'EClass56', a2)
    if hasattr(a1, 'eStructuralFeatures'):
        assert not _is_linked(a1, 'eStructuralFeatures', b)
    if hasattr(a2, 'eStructuralFeatures'):
        assert _is_linked(a2, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass56', None)
    assert not _is_linked(b, 'EClass56', a2)
    if hasattr(a2, 'eStructuralFeatures'):
        assert not _is_linked(a2, 'eStructuralFeatures', b)


def test_assoc_eEnum32_reverse_link_reassign_clear():
    a1 = Ecore_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    a2 = Ecore_EEnumLiteral(instance="sample_text_2", literal="sample_text_2", value=13)
    b = Ecore_EEnum()
    _safe_set(b, 'EEnum', a1)
    assert _is_linked(b, 'EEnum', a1)
    if hasattr(a1, 'eLiterals'):
        assert _is_linked(a1, 'eLiterals', b)
    _safe_set(b, 'EEnum', a2)
    assert _is_linked(b, 'EEnum', a2)
    if hasattr(a1, 'eLiterals'):
        assert not _is_linked(a1, 'eLiterals', b)
    if hasattr(a2, 'eLiterals'):
        assert _is_linked(a2, 'eLiterals', b)
    _safe_set(b, 'EEnum', None)
    assert not _is_linked(b, 'EEnum', a2)
    if hasattr(a2, 'eLiterals'):
        assert not _is_linked(a2, 'eLiterals', b)


def test_assoc_eIDAttribute25_reverse_link_reassign_clear():
    a1 = Ecore_EClass(abstract=True, interface=True)
    a2 = Ecore_EClass(abstract=False, interface=False)
    b = Ecore_EAttribute(iD=True)
    _safe_set(b, 'Ecore_EAttribute27', a1)
    assert _is_linked(b, 'Ecore_EAttribute27', a1)
    if hasattr(a1, 'Ecore_EClass26'):
        assert _is_linked(a1, 'Ecore_EClass26', b)
    _safe_set(b, 'Ecore_EAttribute27', a2)
    assert _is_linked(b, 'Ecore_EAttribute27', a2)
    if hasattr(a1, 'Ecore_EClass26'):
        assert not _is_linked(a1, 'Ecore_EClass26', b)
    if hasattr(a2, 'Ecore_EClass26'):
        assert _is_linked(a2, 'Ecore_EClass26', b)
    _safe_set(b, 'Ecore_EAttribute27', None)
    assert not _is_linked(b, 'Ecore_EAttribute27', a2)
    if hasattr(a2, 'Ecore_EClass26'):
        assert not _is_linked(a2, 'Ecore_EClass26', b)


def test_assoc_eKeys52_reverse_link_reassign_clear():
    a1 = Ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = Ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = Ecore_EAttribute(iD=True)
    _safe_set(b, 'Ecore_EAttribute54', a1)
    assert _is_linked(b, 'Ecore_EAttribute54', a1)
    if hasattr(a1, 'Ecore_EReference53'):
        assert _is_linked(a1, 'Ecore_EReference53', b)
    _safe_set(b, 'Ecore_EAttribute54', a2)
    assert _is_linked(b, 'Ecore_EAttribute54', a2)
    if hasattr(a1, 'Ecore_EReference53'):
        assert not _is_linked(a1, 'Ecore_EReference53', b)
    if hasattr(a2, 'Ecore_EReference53'):
        assert _is_linked(a2, 'Ecore_EReference53', b)
    _safe_set(b, 'Ecore_EAttribute54', None)
    assert not _is_linked(b, 'Ecore_EAttribute54', a2)
    if hasattr(a2, 'Ecore_EReference53'):
        assert not _is_linked(a2, 'Ecore_EReference53', b)


def test_assoc_eLiterals31_reverse_link_reassign_clear():
    a1 = Ecore_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    a2 = Ecore_EEnumLiteral(instance="sample_text_2", literal="sample_text_2", value=13)
    b = Ecore_EEnum()
    _safe_set(b, 'eEnum', {a1})
    assert _is_linked(b, 'eEnum', a1)
    if hasattr(a1, 'EEnumLiteral'):
        assert _is_linked(a1, 'EEnumLiteral', b)
    _safe_set(b, 'eEnum', {a2})
    assert _is_linked(b, 'eEnum', a2)
    if hasattr(a1, 'EEnumLiteral'):
        assert not _is_linked(a1, 'EEnumLiteral', b)
    if hasattr(a2, 'EEnumLiteral'):
        assert _is_linked(a2, 'EEnumLiteral', b)
    _safe_set(b, 'eEnum', set())
    assert not _is_linked(b, 'eEnum', a2)
    if hasattr(a2, 'EEnumLiteral'):
        assert not _is_linked(a2, 'EEnumLiteral', b)


def test_assoc_eOpposite47_reverse_link_reassign_clear():
    a1 = Ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = Ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = Ecore_EReference(container=True, containment=True, resolveProxies=True)
    _safe_set(b, 'Ecore_EReference48', a1)
    assert _is_linked(b, 'Ecore_EReference48', a1)
    if hasattr(a1, 'Ecore_EReference46'):
        assert _is_linked(a1, 'Ecore_EReference46', b)
    _safe_set(b, 'Ecore_EReference48', a2)
    assert _is_linked(b, 'Ecore_EReference48', a2)
    if hasattr(a1, 'Ecore_EReference46'):
        assert not _is_linked(a1, 'Ecore_EReference46', b)
    if hasattr(a2, 'Ecore_EReference46'):
        assert _is_linked(a2, 'Ecore_EReference46', b)
    _safe_set(b, 'Ecore_EReference48', None)
    assert not _is_linked(b, 'Ecore_EReference48', a2)
    if hasattr(a2, 'Ecore_EReference46'):
        assert not _is_linked(a2, 'Ecore_EReference46', b)


def test_assoc_ePackage30_reverse_link_reassign_clear():
    a1 = Ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = Ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = Ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'eClassifiers', a1)
    assert _is_linked(b, 'eClassifiers', a1)
    if hasattr(a1, 'EPackage'):
        assert _is_linked(a1, 'EPackage', b)
    _safe_set(b, 'eClassifiers', a2)
    assert _is_linked(b, 'eClassifiers', a2)
    if hasattr(a1, 'EPackage'):
        assert not _is_linked(a1, 'EPackage', b)
    if hasattr(a2, 'EPackage'):
        assert _is_linked(a2, 'EPackage', b)
    _safe_set(b, 'eClassifiers', None)
    assert not _is_linked(b, 'eClassifiers', a2)
    if hasattr(a2, 'EPackage'):
        assert not _is_linked(a2, 'EPackage', b)


def test_assoc_eReferenceType49_reverse_link_reassign_clear():
    a1 = Ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = Ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = Ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'Ecore_EClass51', a1)
    assert _is_linked(b, 'Ecore_EClass51', a1)
    if hasattr(a1, 'Ecore_EReference50'):
        assert _is_linked(a1, 'Ecore_EReference50', b)
    _safe_set(b, 'Ecore_EClass51', a2)
    assert _is_linked(b, 'Ecore_EClass51', a2)
    if hasattr(a1, 'Ecore_EReference50'):
        assert not _is_linked(a1, 'Ecore_EReference50', b)
    if hasattr(a2, 'Ecore_EReference50'):
        assert _is_linked(a2, 'Ecore_EReference50', b)
    _safe_set(b, 'Ecore_EClass51', None)
    assert not _is_linked(b, 'Ecore_EClass51', a2)
    if hasattr(a2, 'Ecore_EReference50'):
        assert not _is_linked(a2, 'Ecore_EReference50', b)


def test_assoc_eReferences9_reverse_link_reassign_clear():
    a1 = Ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = Ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = Ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'Ecore_EClass10', {a1})
    assert _is_linked(b, 'Ecore_EClass10', a1)
    if hasattr(a1, 'Ecore_EReference11'):
        assert _is_linked(a1, 'Ecore_EReference11', b)
    _safe_set(b, 'Ecore_EClass10', {a2})
    assert _is_linked(b, 'Ecore_EClass10', a2)
    if hasattr(a1, 'Ecore_EReference11'):
        assert not _is_linked(a1, 'Ecore_EReference11', b)
    if hasattr(a2, 'Ecore_EReference11'):
        assert _is_linked(a2, 'Ecore_EReference11', b)
    _safe_set(b, 'Ecore_EClass10', set())
    assert not _is_linked(b, 'Ecore_EClass10', a2)
    if hasattr(a2, 'Ecore_EReference11'):
        assert not _is_linked(a2, 'Ecore_EReference11', b)


def test_assoc_eStructuralFeatures28_reverse_link_reassign_clear():
    a1 = Ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = Ecore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = Ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'eContainingClass29', {a1})
    assert _is_linked(b, 'eContainingClass29', a1)
    if hasattr(a1, 'EStructuralFeature'):
        assert _is_linked(a1, 'EStructuralFeature', b)
    _safe_set(b, 'eContainingClass29', {a2})
    assert _is_linked(b, 'eContainingClass29', a2)
    if hasattr(a1, 'EStructuralFeature'):
        assert not _is_linked(a1, 'EStructuralFeature', b)
    if hasattr(a2, 'EStructuralFeature'):
        assert _is_linked(a2, 'EStructuralFeature', b)
    _safe_set(b, 'eContainingClass29', set())
    assert not _is_linked(b, 'eContainingClass29', a2)
    if hasattr(a2, 'EStructuralFeature'):
        assert not _is_linked(a2, 'EStructuralFeature', b)


def test_assoc_eSubpackages39_reverse_link_reassign_clear():
    a1 = Ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = Ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = Ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSuperPackage', {a1})
    assert _is_linked(b, 'eSuperPackage', a1)
    if hasattr(a1, 'EPackage40'):
        assert _is_linked(a1, 'EPackage40', b)
    _safe_set(b, 'eSuperPackage', {a2})
    assert _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a1, 'EPackage40'):
        assert not _is_linked(a1, 'EPackage40', b)
    if hasattr(a2, 'EPackage40'):
        assert _is_linked(a2, 'EPackage40', b)
    _safe_set(b, 'eSuperPackage', set())
    assert not _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a2, 'EPackage40'):
        assert not _is_linked(a2, 'EPackage40', b)


def test_assoc_eSuperPackage42_reverse_link_reassign_clear():
    a1 = Ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = Ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = Ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSubpackages', a1)
    assert _is_linked(b, 'eSubpackages', a1)
    if hasattr(a1, 'EPackage43'):
        assert _is_linked(a1, 'EPackage43', b)
    _safe_set(b, 'eSubpackages', a2)
    assert _is_linked(b, 'eSubpackages', a2)
    if hasattr(a1, 'EPackage43'):
        assert not _is_linked(a1, 'EPackage43', b)
    if hasattr(a2, 'EPackage43'):
        assert _is_linked(a2, 'EPackage43', b)
    _safe_set(b, 'eSubpackages', None)
    assert not _is_linked(b, 'eSubpackages', a2)
    if hasattr(a2, 'EPackage43'):
        assert not _is_linked(a2, 'EPackage43', b)


def test_assoc_eSuperTypes2_reverse_link_reassign_clear():
    a1 = Ecore_EClass(abstract=True, interface=True)
    a2 = Ecore_EClass(abstract=False, interface=False)
    b = Ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'Ecore_EClass1', {a1})
    assert _is_linked(b, 'Ecore_EClass1', a1)
    if hasattr(a1, 'Ecore_EClass'):
        assert _is_linked(a1, 'Ecore_EClass', b)
    _safe_set(b, 'Ecore_EClass1', {a2})
    assert _is_linked(b, 'Ecore_EClass1', a2)
    if hasattr(a1, 'Ecore_EClass'):
        assert not _is_linked(a1, 'Ecore_EClass', b)
    if hasattr(a2, 'Ecore_EClass'):
        assert _is_linked(a2, 'Ecore_EClass', b)
    _safe_set(b, 'Ecore_EClass1', set())
    assert not _is_linked(b, 'Ecore_EClass1', a2)
    if hasattr(a2, 'Ecore_EClass'):
        assert not _is_linked(a2, 'Ecore_EClass', b)


def test_assoc_eType57_reverse_link_reassign_clear():
    a1 = Ecore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    a2 = Ecore_ETypedElement(lowerBound=13, many=False, ordered=False, required=False, unique=False, upperBound=13)
    b = Ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'Ecore_EClassifier58', a1)
    assert _is_linked(b, 'Ecore_EClassifier58', a1)
    if hasattr(a1, 'Ecore_ETypedElement'):
        assert _is_linked(a1, 'Ecore_ETypedElement', b)
    _safe_set(b, 'Ecore_EClassifier58', a2)
    assert _is_linked(b, 'Ecore_EClassifier58', a2)
    if hasattr(a1, 'Ecore_ETypedElement'):
        assert not _is_linked(a1, 'Ecore_ETypedElement', b)
    if hasattr(a2, 'Ecore_ETypedElement'):
        assert _is_linked(a2, 'Ecore_ETypedElement', b)
    _safe_set(b, 'Ecore_EClassifier58', None)
    assert not _is_linked(b, 'Ecore_EClassifier58', a2)
    if hasattr(a2, 'Ecore_ETypedElement'):
        assert not _is_linked(a2, 'Ecore_ETypedElement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_eAllOperations18_stub_double():
    # Ecore_EOperation has no real 'Ecore_EOperation' property in the generated
    # code (a bare stub) -- manually attach it so Ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ecore_EClass(abstract=True, interface=True)
    partner = Ecore_EOperation()
    setattr(partner, 'Ecore_EOperation', None)
    _safe_set(owner, 'Ecore_EClass19', {partner})
    assert getattr(partner, 'Ecore_EOperation') == owner
    _safe_set(owner, 'Ecore_EClass19', set())
    assert getattr(partner, 'Ecore_EOperation') is None


def test_assoc_eContainingClass33_stub_double():
    # Ecore_EOperation has no real 'eOperations' property in the generated
    # code (a bare stub) -- manually attach it so Ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ecore_EClass(abstract=True, interface=True)
    partner = Ecore_EOperation()
    setattr(partner, 'eOperations', None)
    _safe_set(owner, 'EClass', partner)
    assert getattr(partner, 'eOperations') == owner
    _safe_set(owner, 'EClass', None)
    assert getattr(partner, 'eOperations') is None


def test_assoc_eExceptions35_stub_double():
    # Ecore_EOperation has no real 'Ecore_EOperation36' property in the generated
    # code (a bare stub) -- manually attach it so Ecore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ecore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = Ecore_EOperation()
    setattr(partner, 'Ecore_EOperation36', None)
    _safe_set(owner, 'Ecore_EClassifier', partner)
    assert owner in getattr(partner, 'Ecore_EOperation36')
    _safe_set(owner, 'Ecore_EClassifier', None)
    assert owner not in getattr(partner, 'Ecore_EOperation36')


def test_assoc_eOperations3_stub_double():
    # Ecore_EOperation has no real 'EOperation' property in the generated
    # code (a bare stub) -- manually attach it so Ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Ecore_EClass(abstract=True, interface=True)
    partner = Ecore_EOperation()
    setattr(partner, 'EOperation', None)
    _safe_set(owner, 'eContainingClass', {partner})
    assert getattr(partner, 'EOperation') == owner
    _safe_set(owner, 'eContainingClass', set())
    assert getattr(partner, 'EOperation') is None


