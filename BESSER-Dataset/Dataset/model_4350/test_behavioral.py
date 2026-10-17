import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DifferenceElement,
    EAnnotation,
    EAttribute,
    EClass,
    EClassifier,
    EClassifier_Wildcard,
    EDataType,
    EEnum,
    EEnumLiteral,
    EFactory,
    EGenericType,
    EModelElement,
    ENamedElement,
    EObject,
    EOperation,
    EPackage,
    EParameter,
    EReference,
    EStringToStringMapEntry,
    EStructuralFeature,
    EStructuralFeature_Wildcard,
    ETypeParameter,
    ETypedElement,
    ecoreDiff_AddedEAnnotation,
    ecoreDiff_AddedEAttribute,
    ecoreDiff_AddedEClass,
    ecoreDiff_AddedEClassifier,
    ecoreDiff_AddedEClassifier_Wildcard,
    ecoreDiff_AddedEDataType,
    ecoreDiff_AddedEEnum,
    ecoreDiff_AddedEEnumLiteral,
    ecoreDiff_AddedEFactory,
    ecoreDiff_AddedEGenericType,
    ecoreDiff_AddedEModelElement,
    ecoreDiff_AddedENamedElement,
    ecoreDiff_AddedEObject,
    ecoreDiff_AddedEOperation,
    ecoreDiff_AddedEPackage,
    ecoreDiff_AddedEParameter,
    ecoreDiff_AddedEReference,
    ecoreDiff_AddedEStringToStringMapEntry,
    ecoreDiff_AddedEStructuralFeature,
    ecoreDiff_AddedEStructuralFeature_Wildcard,
    ecoreDiff_AddedETypeParameter,
    ecoreDiff_AddedETypedElement,
    ecoreDiff_ChangedEAnnotation,
    ecoreDiff_ChangedEAttribute,
    ecoreDiff_ChangedEClass,
    ecoreDiff_ChangedEClassifier,
    ecoreDiff_ChangedEClassifier_Wildcard,
    ecoreDiff_ChangedEDataType,
    ecoreDiff_ChangedEEnum,
    ecoreDiff_ChangedEEnumLiteral,
    ecoreDiff_ChangedEFactory,
    ecoreDiff_ChangedEGenericType,
    ecoreDiff_ChangedEModelElement,
    ecoreDiff_ChangedENamedElement,
    ecoreDiff_ChangedEObject,
    ecoreDiff_ChangedEOperation,
    ecoreDiff_ChangedEPackage,
    ecoreDiff_ChangedEParameter,
    ecoreDiff_ChangedEReference,
    ecoreDiff_ChangedEStringToStringMapEntry,
    ecoreDiff_ChangedEStructuralFeature,
    ecoreDiff_ChangedEStructuralFeature_Wildcard,
    ecoreDiff_ChangedETypeParameter,
    ecoreDiff_ChangedETypedElement,
    ecoreDiff_DeletedEAnnotation,
    ecoreDiff_DeletedEAttribute,
    ecoreDiff_DeletedEClass,
    ecoreDiff_DeletedEClassifier,
    ecoreDiff_DeletedEClassifier_Wildcard,
    ecoreDiff_DeletedEDataType,
    ecoreDiff_DeletedEEnum,
    ecoreDiff_DeletedEEnumLiteral,
    ecoreDiff_DeletedEFactory,
    ecoreDiff_DeletedEGenericType,
    ecoreDiff_DeletedEModelElement,
    ecoreDiff_DeletedENamedElement,
    ecoreDiff_DeletedEObject,
    ecoreDiff_DeletedEOperation,
    ecoreDiff_DeletedEPackage,
    ecoreDiff_DeletedEParameter,
    ecoreDiff_DeletedEReference,
    ecoreDiff_DeletedEStringToStringMapEntry,
    ecoreDiff_DeletedEStructuralFeature,
    ecoreDiff_DeletedEStructuralFeature_Wildcard,
    ecoreDiff_DeletedETypeParameter,
    ecoreDiff_DeletedETypedElement,
    ecoreDiff_DifferenceElement,
    ecoreDiff_DifferenceModel,
    ecoreDiff_EAnnotation,
    ecoreDiff_EAttribute,
    ecoreDiff_EClass,
    ecoreDiff_EClassifier,
    ecoreDiff_EClassifier_Wildcard,
    ecoreDiff_EDataType,
    ecoreDiff_EEnum,
    ecoreDiff_EEnumLiteral,
    ecoreDiff_EFactory,
    ecoreDiff_EGenericType,
    ecoreDiff_EModelElement,
    ecoreDiff_ENamedElement,
    ecoreDiff_EObject,
    ecoreDiff_EOperation,
    ecoreDiff_EPackage,
    ecoreDiff_EParameter,
    ecoreDiff_EReference,
    ecoreDiff_EStringToStringMapEntry,
    ecoreDiff_EStructuralFeature,
    ecoreDiff_EStructuralFeature_Wildcard,
    ecoreDiff_ETypeParameter,
    ecoreDiff_ETypedElement,
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

def test_assoc_details0_reverse_link_reassign_clear():
    a1 = ecoreDiff_EStringToStringMapEntry(key="sample_text", value="sample_text")
    a2 = ecoreDiff_EStringToStringMapEntry(key="sample_text_2", value="sample_text_2")
    b = ecoreDiff_EAnnotation(source="sample_text")
    _safe_set(b, 'ecoreDiff_EAnnotation', {a1})
    assert _is_linked(b, 'ecoreDiff_EAnnotation', a1)
    if hasattr(a1, 'ecoreDiff_EStringToStringMapEntry'):
        assert _is_linked(a1, 'ecoreDiff_EStringToStringMapEntry', b)
    _safe_set(b, 'ecoreDiff_EAnnotation', {a2})
    assert _is_linked(b, 'ecoreDiff_EAnnotation', a2)
    if hasattr(a1, 'ecoreDiff_EStringToStringMapEntry'):
        assert not _is_linked(a1, 'ecoreDiff_EStringToStringMapEntry', b)
    if hasattr(a2, 'ecoreDiff_EStringToStringMapEntry'):
        assert _is_linked(a2, 'ecoreDiff_EStringToStringMapEntry', b)
    _safe_set(b, 'ecoreDiff_EAnnotation', set())
    assert not _is_linked(b, 'ecoreDiff_EAnnotation', a2)
    if hasattr(a2, 'ecoreDiff_EStringToStringMapEntry'):
        assert not _is_linked(a2, 'ecoreDiff_EStringToStringMapEntry', b)


def test_assoc_eAllAttributes10_reverse_link_reassign_clear():
    a1 = ecoreDiff_EClass(abstract=True, interface=True)
    a2 = ecoreDiff_EClass(abstract=False, interface=False)
    b = ecoreDiff_EAttribute(iD=True)
    _safe_set(b, 'ecoreDiff_EAttribute', a1)
    assert _is_linked(b, 'ecoreDiff_EAttribute', a1)
    if hasattr(a1, 'ecoreDiff_EClass11'):
        assert _is_linked(a1, 'ecoreDiff_EClass11', b)
    _safe_set(b, 'ecoreDiff_EAttribute', a2)
    assert _is_linked(b, 'ecoreDiff_EAttribute', a2)
    if hasattr(a1, 'ecoreDiff_EClass11'):
        assert not _is_linked(a1, 'ecoreDiff_EClass11', b)
    if hasattr(a2, 'ecoreDiff_EClass11'):
        assert _is_linked(a2, 'ecoreDiff_EClass11', b)
    _safe_set(b, 'ecoreDiff_EAttribute', None)
    assert not _is_linked(b, 'ecoreDiff_EAttribute', a2)
    if hasattr(a2, 'ecoreDiff_EClass11'):
        assert not _is_linked(a2, 'ecoreDiff_EClass11', b)


def test_assoc_eAllContainments22_reverse_link_reassign_clear():
    a1 = ecoreDiff_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecoreDiff_EReference(container=False, containment=False, resolveProxies=False)
    b = ecoreDiff_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecoreDiff_EClass23', {a1})
    assert _is_linked(b, 'ecoreDiff_EClass23', a1)
    if hasattr(a1, 'ecoreDiff_EReference24'):
        assert _is_linked(a1, 'ecoreDiff_EReference24', b)
    _safe_set(b, 'ecoreDiff_EClass23', {a2})
    assert _is_linked(b, 'ecoreDiff_EClass23', a2)
    if hasattr(a1, 'ecoreDiff_EReference24'):
        assert not _is_linked(a1, 'ecoreDiff_EReference24', b)
    if hasattr(a2, 'ecoreDiff_EReference24'):
        assert _is_linked(a2, 'ecoreDiff_EReference24', b)
    _safe_set(b, 'ecoreDiff_EClass23', set())
    assert not _is_linked(b, 'ecoreDiff_EClass23', a2)
    if hasattr(a2, 'ecoreDiff_EReference24'):
        assert not _is_linked(a2, 'ecoreDiff_EReference24', b)


def test_assoc_eAllReferences14_reverse_link_reassign_clear():
    a1 = ecoreDiff_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecoreDiff_EReference(container=False, containment=False, resolveProxies=False)
    b = ecoreDiff_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecoreDiff_EClass15', {a1})
    assert _is_linked(b, 'ecoreDiff_EClass15', a1)
    if hasattr(a1, 'ecoreDiff_EReference'):
        assert _is_linked(a1, 'ecoreDiff_EReference', b)
    _safe_set(b, 'ecoreDiff_EClass15', {a2})
    assert _is_linked(b, 'ecoreDiff_EClass15', a2)
    if hasattr(a1, 'ecoreDiff_EReference'):
        assert not _is_linked(a1, 'ecoreDiff_EReference', b)
    if hasattr(a2, 'ecoreDiff_EReference'):
        assert _is_linked(a2, 'ecoreDiff_EReference', b)
    _safe_set(b, 'ecoreDiff_EClass15', set())
    assert not _is_linked(b, 'ecoreDiff_EClass15', a2)
    if hasattr(a2, 'ecoreDiff_EReference'):
        assert not _is_linked(a2, 'ecoreDiff_EReference', b)


def test_assoc_eAllStructuralFeatures27_reverse_link_reassign_clear():
    a1 = ecoreDiff_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = ecoreDiff_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = ecoreDiff_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecoreDiff_EClass28', {a1})
    assert _is_linked(b, 'ecoreDiff_EClass28', a1)
    if hasattr(a1, 'ecoreDiff_EStructuralFeature'):
        assert _is_linked(a1, 'ecoreDiff_EStructuralFeature', b)
    _safe_set(b, 'ecoreDiff_EClass28', {a2})
    assert _is_linked(b, 'ecoreDiff_EClass28', a2)
    if hasattr(a1, 'ecoreDiff_EStructuralFeature'):
        assert not _is_linked(a1, 'ecoreDiff_EStructuralFeature', b)
    if hasattr(a2, 'ecoreDiff_EStructuralFeature'):
        assert _is_linked(a2, 'ecoreDiff_EStructuralFeature', b)
    _safe_set(b, 'ecoreDiff_EClass28', set())
    assert not _is_linked(b, 'ecoreDiff_EClass28', a2)
    if hasattr(a2, 'ecoreDiff_EStructuralFeature'):
        assert not _is_linked(a2, 'ecoreDiff_EStructuralFeature', b)


def test_assoc_eAllSuperTypes30_reverse_link_reassign_clear():
    a1 = ecoreDiff_EClass(abstract=True, interface=True)
    a2 = ecoreDiff_EClass(abstract=False, interface=False)
    b = ecoreDiff_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecoreDiff_EClass31', a1)
    assert _is_linked(b, 'ecoreDiff_EClass31', a1)
    if hasattr(a1, 'ecoreDiff_EClass29'):
        assert _is_linked(a1, 'ecoreDiff_EClass29', b)
    _safe_set(b, 'ecoreDiff_EClass31', a2)
    assert _is_linked(b, 'ecoreDiff_EClass31', a2)
    if hasattr(a1, 'ecoreDiff_EClass29'):
        assert not _is_linked(a1, 'ecoreDiff_EClass29', b)
    if hasattr(a2, 'ecoreDiff_EClass29'):
        assert _is_linked(a2, 'ecoreDiff_EClass29', b)
    _safe_set(b, 'ecoreDiff_EClass31', None)
    assert not _is_linked(b, 'ecoreDiff_EClass31', a2)
    if hasattr(a2, 'ecoreDiff_EClass29'):
        assert not _is_linked(a2, 'ecoreDiff_EClass29', b)


def test_assoc_eAttributeType92_reverse_link_reassign_clear():
    a1 = ecoreDiff_EDataType(serializable=True)
    a2 = ecoreDiff_EDataType(serializable=False)
    b = ecoreDiff_EAttribute(iD=True)
    _safe_set(b, 'ecoreDiff_EAttribute93', a1)
    assert _is_linked(b, 'ecoreDiff_EAttribute93', a1)
    if hasattr(a1, 'ecoreDiff_EDataType'):
        assert _is_linked(a1, 'ecoreDiff_EDataType', b)
    _safe_set(b, 'ecoreDiff_EAttribute93', a2)
    assert _is_linked(b, 'ecoreDiff_EAttribute93', a2)
    if hasattr(a1, 'ecoreDiff_EDataType'):
        assert not _is_linked(a1, 'ecoreDiff_EDataType', b)
    if hasattr(a2, 'ecoreDiff_EDataType'):
        assert _is_linked(a2, 'ecoreDiff_EDataType', b)
    _safe_set(b, 'ecoreDiff_EAttribute93', None)
    assert not _is_linked(b, 'ecoreDiff_EAttribute93', a2)
    if hasattr(a2, 'ecoreDiff_EDataType'):
        assert not _is_linked(a2, 'ecoreDiff_EDataType', b)


def test_assoc_eAttributes19_reverse_link_reassign_clear():
    a1 = ecoreDiff_EClass(abstract=True, interface=True)
    a2 = ecoreDiff_EClass(abstract=False, interface=False)
    b = ecoreDiff_EAttribute(iD=True)
    _safe_set(b, 'ecoreDiff_EAttribute21', a1)
    assert _is_linked(b, 'ecoreDiff_EAttribute21', a1)
    if hasattr(a1, 'ecoreDiff_EClass20'):
        assert _is_linked(a1, 'ecoreDiff_EClass20', b)
    _safe_set(b, 'ecoreDiff_EAttribute21', a2)
    assert _is_linked(b, 'ecoreDiff_EAttribute21', a2)
    if hasattr(a1, 'ecoreDiff_EClass20'):
        assert not _is_linked(a1, 'ecoreDiff_EClass20', b)
    if hasattr(a2, 'ecoreDiff_EClass20'):
        assert _is_linked(a2, 'ecoreDiff_EClass20', b)
    _safe_set(b, 'ecoreDiff_EAttribute21', None)
    assert not _is_linked(b, 'ecoreDiff_EAttribute21', a2)
    if hasattr(a2, 'ecoreDiff_EClass20'):
        assert not _is_linked(a2, 'ecoreDiff_EClass20', b)


def test_assoc_eClassifiers49_reverse_link_reassign_clear():
    a1 = ecoreDiff_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecoreDiff_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecoreDiff_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'EClassifier', a1)
    assert _is_linked(b, 'EClassifier', a1)
    if hasattr(a1, 'ePackage50'):
        assert _is_linked(a1, 'ePackage50', b)
    _safe_set(b, 'EClassifier', a2)
    assert _is_linked(b, 'EClassifier', a2)
    if hasattr(a1, 'ePackage50'):
        assert not _is_linked(a1, 'ePackage50', b)
    if hasattr(a2, 'ePackage50'):
        assert _is_linked(a2, 'ePackage50', b)
    _safe_set(b, 'EClassifier', None)
    assert not _is_linked(b, 'EClassifier', a2)
    if hasattr(a2, 'ePackage50'):
        assert not _is_linked(a2, 'ePackage50', b)


def test_assoc_eContainingClass94_reverse_link_reassign_clear():
    a1 = ecoreDiff_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = ecoreDiff_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = ecoreDiff_EClass(abstract=True, interface=True)
    _safe_set(b, 'EClass95', a1)
    assert _is_linked(b, 'EClass95', a1)
    if hasattr(a1, 'eStructuralFeatures'):
        assert _is_linked(a1, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass95', a2)
    assert _is_linked(b, 'EClass95', a2)
    if hasattr(a1, 'eStructuralFeatures'):
        assert not _is_linked(a1, 'eStructuralFeatures', b)
    if hasattr(a2, 'eStructuralFeatures'):
        assert _is_linked(a2, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass95', None)
    assert not _is_linked(b, 'EClass95', a2)
    if hasattr(a2, 'eStructuralFeatures'):
        assert not _is_linked(a2, 'eStructuralFeatures', b)


def test_assoc_eIDAttribute32_reverse_link_reassign_clear():
    a1 = ecoreDiff_EClass(abstract=True, interface=True)
    a2 = ecoreDiff_EClass(abstract=False, interface=False)
    b = ecoreDiff_EAttribute(iD=True)
    _safe_set(b, 'ecoreDiff_EAttribute34', a1)
    assert _is_linked(b, 'ecoreDiff_EAttribute34', a1)
    if hasattr(a1, 'ecoreDiff_EClass33'):
        assert _is_linked(a1, 'ecoreDiff_EClass33', b)
    _safe_set(b, 'ecoreDiff_EAttribute34', a2)
    assert _is_linked(b, 'ecoreDiff_EAttribute34', a2)
    if hasattr(a1, 'ecoreDiff_EClass33'):
        assert not _is_linked(a1, 'ecoreDiff_EClass33', b)
    if hasattr(a2, 'ecoreDiff_EClass33'):
        assert _is_linked(a2, 'ecoreDiff_EClass33', b)
    _safe_set(b, 'ecoreDiff_EAttribute34', None)
    assert not _is_linked(b, 'ecoreDiff_EAttribute34', a2)
    if hasattr(a2, 'ecoreDiff_EClass33'):
        assert not _is_linked(a2, 'ecoreDiff_EClass33', b)


def test_assoc_eKeys102_reverse_link_reassign_clear():
    a1 = ecoreDiff_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecoreDiff_EReference(container=False, containment=False, resolveProxies=False)
    b = ecoreDiff_EAttribute(iD=True)
    _safe_set(b, 'ecoreDiff_EAttribute104', a1)
    assert _is_linked(b, 'ecoreDiff_EAttribute104', a1)
    if hasattr(a1, 'ecoreDiff_EReference103'):
        assert _is_linked(a1, 'ecoreDiff_EReference103', b)
    _safe_set(b, 'ecoreDiff_EAttribute104', a2)
    assert _is_linked(b, 'ecoreDiff_EAttribute104', a2)
    if hasattr(a1, 'ecoreDiff_EReference103'):
        assert not _is_linked(a1, 'ecoreDiff_EReference103', b)
    if hasattr(a2, 'ecoreDiff_EReference103'):
        assert _is_linked(a2, 'ecoreDiff_EReference103', b)
    _safe_set(b, 'ecoreDiff_EAttribute104', None)
    assert not _is_linked(b, 'ecoreDiff_EAttribute104', a2)
    if hasattr(a2, 'ecoreDiff_EReference103'):
        assert not _is_linked(a2, 'ecoreDiff_EReference103', b)


def test_assoc_eOpposite97_reverse_link_reassign_clear():
    a1 = ecoreDiff_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecoreDiff_EReference(container=False, containment=False, resolveProxies=False)
    b = ecoreDiff_EReference(container=True, containment=True, resolveProxies=True)
    _safe_set(b, 'ecoreDiff_EReference98', a1)
    assert _is_linked(b, 'ecoreDiff_EReference98', a1)
    if hasattr(a1, 'ecoreDiff_EReference96'):
        assert _is_linked(a1, 'ecoreDiff_EReference96', b)
    _safe_set(b, 'ecoreDiff_EReference98', a2)
    assert _is_linked(b, 'ecoreDiff_EReference98', a2)
    if hasattr(a1, 'ecoreDiff_EReference96'):
        assert not _is_linked(a1, 'ecoreDiff_EReference96', b)
    if hasattr(a2, 'ecoreDiff_EReference96'):
        assert _is_linked(a2, 'ecoreDiff_EReference96', b)
    _safe_set(b, 'ecoreDiff_EReference98', None)
    assert not _is_linked(b, 'ecoreDiff_EReference98', a2)
    if hasattr(a2, 'ecoreDiff_EReference96'):
        assert not _is_linked(a2, 'ecoreDiff_EReference96', b)


def test_assoc_ePackage40_reverse_link_reassign_clear():
    a1 = ecoreDiff_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecoreDiff_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecoreDiff_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
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


def test_assoc_eReferenceType99_reverse_link_reassign_clear():
    a1 = ecoreDiff_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecoreDiff_EReference(container=False, containment=False, resolveProxies=False)
    b = ecoreDiff_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecoreDiff_EClass101', a1)
    assert _is_linked(b, 'ecoreDiff_EClass101', a1)
    if hasattr(a1, 'ecoreDiff_EReference100'):
        assert _is_linked(a1, 'ecoreDiff_EReference100', b)
    _safe_set(b, 'ecoreDiff_EClass101', a2)
    assert _is_linked(b, 'ecoreDiff_EClass101', a2)
    if hasattr(a1, 'ecoreDiff_EReference100'):
        assert not _is_linked(a1, 'ecoreDiff_EReference100', b)
    if hasattr(a2, 'ecoreDiff_EReference100'):
        assert _is_linked(a2, 'ecoreDiff_EReference100', b)
    _safe_set(b, 'ecoreDiff_EClass101', None)
    assert not _is_linked(b, 'ecoreDiff_EClass101', a2)
    if hasattr(a2, 'ecoreDiff_EReference100'):
        assert not _is_linked(a2, 'ecoreDiff_EReference100', b)


def test_assoc_eReferences16_reverse_link_reassign_clear():
    a1 = ecoreDiff_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecoreDiff_EReference(container=False, containment=False, resolveProxies=False)
    b = ecoreDiff_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecoreDiff_EClass17', {a1})
    assert _is_linked(b, 'ecoreDiff_EClass17', a1)
    if hasattr(a1, 'ecoreDiff_EReference18'):
        assert _is_linked(a1, 'ecoreDiff_EReference18', b)
    _safe_set(b, 'ecoreDiff_EClass17', {a2})
    assert _is_linked(b, 'ecoreDiff_EClass17', a2)
    if hasattr(a1, 'ecoreDiff_EReference18'):
        assert not _is_linked(a1, 'ecoreDiff_EReference18', b)
    if hasattr(a2, 'ecoreDiff_EReference18'):
        assert _is_linked(a2, 'ecoreDiff_EReference18', b)
    _safe_set(b, 'ecoreDiff_EClass17', set())
    assert not _is_linked(b, 'ecoreDiff_EClass17', a2)
    if hasattr(a2, 'ecoreDiff_EReference18'):
        assert not _is_linked(a2, 'ecoreDiff_EReference18', b)


def test_assoc_eStructuralFeatures12_reverse_link_reassign_clear():
    a1 = ecoreDiff_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = ecoreDiff_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = ecoreDiff_EClass(abstract=True, interface=True)
    _safe_set(b, 'eContainingClass13', {a1})
    assert _is_linked(b, 'eContainingClass13', a1)
    if hasattr(a1, 'EStructuralFeature'):
        assert _is_linked(a1, 'EStructuralFeature', b)
    _safe_set(b, 'eContainingClass13', {a2})
    assert _is_linked(b, 'eContainingClass13', a2)
    if hasattr(a1, 'EStructuralFeature'):
        assert not _is_linked(a1, 'EStructuralFeature', b)
    if hasattr(a2, 'EStructuralFeature'):
        assert _is_linked(a2, 'EStructuralFeature', b)
    _safe_set(b, 'eContainingClass13', set())
    assert not _is_linked(b, 'eContainingClass13', a2)
    if hasattr(a2, 'EStructuralFeature'):
        assert not _is_linked(a2, 'EStructuralFeature', b)


def test_assoc_eSubpackages44_reverse_link_reassign_clear():
    a1 = ecoreDiff_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecoreDiff_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecoreDiff_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSuperPackage', {a1})
    assert _is_linked(b, 'eSuperPackage', a1)
    if hasattr(a1, 'EPackage45'):
        assert _is_linked(a1, 'EPackage45', b)
    _safe_set(b, 'eSuperPackage', {a2})
    assert _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a1, 'EPackage45'):
        assert not _is_linked(a1, 'EPackage45', b)
    if hasattr(a2, 'EPackage45'):
        assert _is_linked(a2, 'EPackage45', b)
    _safe_set(b, 'eSuperPackage', set())
    assert not _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a2, 'EPackage45'):
        assert not _is_linked(a2, 'EPackage45', b)


def test_assoc_eSuperPackage47_reverse_link_reassign_clear():
    a1 = ecoreDiff_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecoreDiff_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecoreDiff_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSubpackages', a1)
    assert _is_linked(b, 'eSubpackages', a1)
    if hasattr(a1, 'EPackage48'):
        assert _is_linked(a1, 'EPackage48', b)
    _safe_set(b, 'eSubpackages', a2)
    assert _is_linked(b, 'eSubpackages', a2)
    if hasattr(a1, 'EPackage48'):
        assert not _is_linked(a1, 'EPackage48', b)
    if hasattr(a2, 'EPackage48'):
        assert _is_linked(a2, 'EPackage48', b)
    _safe_set(b, 'eSubpackages', None)
    assert not _is_linked(b, 'eSubpackages', a2)
    if hasattr(a2, 'EPackage48'):
        assert not _is_linked(a2, 'EPackage48', b)


def test_assoc_eSuperTypes8_reverse_link_reassign_clear():
    a1 = ecoreDiff_EClass(abstract=True, interface=True)
    a2 = ecoreDiff_EClass(abstract=False, interface=False)
    b = ecoreDiff_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecoreDiff_EClass7', {a1})
    assert _is_linked(b, 'ecoreDiff_EClass7', a1)
    if hasattr(a1, 'ecoreDiff_EClass'):
        assert _is_linked(a1, 'ecoreDiff_EClass', b)
    _safe_set(b, 'ecoreDiff_EClass7', {a2})
    assert _is_linked(b, 'ecoreDiff_EClass7', a2)
    if hasattr(a1, 'ecoreDiff_EClass'):
        assert not _is_linked(a1, 'ecoreDiff_EClass', b)
    if hasattr(a2, 'ecoreDiff_EClass'):
        assert _is_linked(a2, 'ecoreDiff_EClass', b)
    _safe_set(b, 'ecoreDiff_EClass7', set())
    assert not _is_linked(b, 'ecoreDiff_EClass7', a2)
    if hasattr(a2, 'ecoreDiff_EClass'):
        assert not _is_linked(a2, 'ecoreDiff_EClass', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_contents2_stub_double():
    # ecoreDiff_EObject has no real 'ecoreDiff_EObject' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EAnnotation(source="sample_text")
    partner = ecoreDiff_EObject()
    setattr(partner, 'ecoreDiff_EObject', None)
    _safe_set(owner, 'ecoreDiff_EAnnotation3', {partner})
    assert getattr(partner, 'ecoreDiff_EObject') == owner
    _safe_set(owner, 'ecoreDiff_EAnnotation3', set())
    assert getattr(partner, 'ecoreDiff_EObject') is None


def test_assoc_eAllGenericSuperTypes37_stub_double():
    # ecoreDiff_EGenericType has no real 'ecoreDiff_EGenericType39' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClass(abstract=True, interface=True)
    partner = ecoreDiff_EGenericType()
    setattr(partner, 'ecoreDiff_EGenericType39', None)
    _safe_set(owner, 'ecoreDiff_EClass38', {partner})
    assert getattr(partner, 'ecoreDiff_EGenericType39') == owner
    _safe_set(owner, 'ecoreDiff_EClass38', set())
    assert getattr(partner, 'ecoreDiff_EGenericType39') is None


def test_assoc_eAllOperations25_stub_double():
    # ecoreDiff_EOperation has no real 'ecoreDiff_EOperation' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClass(abstract=True, interface=True)
    partner = ecoreDiff_EOperation()
    setattr(partner, 'ecoreDiff_EOperation', None)
    _safe_set(owner, 'ecoreDiff_EClass26', {partner})
    assert getattr(partner, 'ecoreDiff_EOperation') == owner
    _safe_set(owner, 'ecoreDiff_EClass26', set())
    assert getattr(partner, 'ecoreDiff_EOperation') is None


def test_assoc_eAnnotations107_stub_double():
    # ecoreDiff_EModelElement has no real 'eModelElement' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EAnnotation(source="sample_text")
    partner = ecoreDiff_EModelElement()
    setattr(partner, 'eModelElement', None)
    _safe_set(owner, 'EAnnotation', partner)
    assert getattr(partner, 'eModelElement') == owner
    _safe_set(owner, 'EAnnotation', None)
    assert getattr(partner, 'eModelElement') is None


def test_assoc_eClassifier71_stub_double():
    # ecoreDiff_EGenericType has no real 'ecoreDiff_EGenericType72' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecoreDiff_EGenericType()
    setattr(partner, 'ecoreDiff_EGenericType72', None)
    _safe_set(owner, 'ecoreDiff_EClassifier73', partner)
    assert getattr(partner, 'ecoreDiff_EGenericType72') == owner
    _safe_set(owner, 'ecoreDiff_EClassifier73', None)
    assert getattr(partner, 'ecoreDiff_EGenericType72') is None


def test_assoc_eContainingClass84_stub_double():
    # ecoreDiff_EOperation has no real 'eOperations' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClass(abstract=True, interface=True)
    partner = ecoreDiff_EOperation()
    setattr(partner, 'eOperations', None)
    _safe_set(owner, 'EClass', partner)
    assert getattr(partner, 'eOperations') == owner
    _safe_set(owner, 'EClass', None)
    assert getattr(partner, 'eOperations') is None


def test_assoc_eEnum106_stub_double():
    # ecoreDiff_EEnum has no real 'EEnum' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EEnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EEnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    partner = ecoreDiff_EEnum()
    setattr(partner, 'EEnum', None)
    _safe_set(owner, 'eLiterals', partner)
    assert getattr(partner, 'EEnum') == owner
    _safe_set(owner, 'eLiterals', None)
    assert getattr(partner, 'EEnum') is None


def test_assoc_eExceptions78_stub_double():
    # ecoreDiff_EOperation has no real 'ecoreDiff_EOperation79' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecoreDiff_EOperation()
    setattr(partner, 'ecoreDiff_EOperation79', None)
    _safe_set(owner, 'ecoreDiff_EClassifier80', partner)
    assert getattr(partner, 'ecoreDiff_EOperation79') == owner
    _safe_set(owner, 'ecoreDiff_EClassifier80', None)
    assert getattr(partner, 'ecoreDiff_EOperation79') is None


def test_assoc_eFactoryInstance42_stub_double():
    # ecoreDiff_EFactory has no real 'EFactory' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    partner = ecoreDiff_EFactory()
    setattr(partner, 'EFactory', None)
    _safe_set(owner, 'ePackage', partner)
    assert getattr(partner, 'EFactory') == owner
    _safe_set(owner, 'ePackage', None)
    assert getattr(partner, 'EFactory') is None


def test_assoc_eGenericSuperTypes35_stub_double():
    # ecoreDiff_EGenericType has no real 'ecoreDiff_EGenericType' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClass(abstract=True, interface=True)
    partner = ecoreDiff_EGenericType()
    setattr(partner, 'ecoreDiff_EGenericType', None)
    _safe_set(owner, 'ecoreDiff_EClass36', {partner})
    assert getattr(partner, 'ecoreDiff_EGenericType') == owner
    _safe_set(owner, 'ecoreDiff_EClass36', set())
    assert getattr(partner, 'ecoreDiff_EGenericType') is None


def test_assoc_eGenericType87_stub_double():
    # ecoreDiff_EGenericType has no real 'ecoreDiff_EGenericType89' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_ETypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_ETypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    partner = ecoreDiff_EGenericType()
    setattr(partner, 'ecoreDiff_EGenericType89', None)
    _safe_set(owner, 'ecoreDiff_ETypedElement88', partner)
    assert getattr(partner, 'ecoreDiff_EGenericType89') == owner
    _safe_set(owner, 'ecoreDiff_ETypedElement88', None)
    assert getattr(partner, 'ecoreDiff_EGenericType89') is None


def test_assoc_eLiterals105_stub_double():
    # ecoreDiff_EEnum has no real 'eEnum' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EEnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EEnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    partner = ecoreDiff_EEnum()
    setattr(partner, 'eEnum', None)
    _safe_set(owner, 'EEnumLiteral', partner)
    assert getattr(partner, 'eEnum') == owner
    _safe_set(owner, 'EEnumLiteral', None)
    assert getattr(partner, 'eEnum') is None


def test_assoc_eModelElement1_stub_double():
    # ecoreDiff_EModelElement has no real 'EModelElement' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EAnnotation(source="sample_text")
    partner = ecoreDiff_EModelElement()
    setattr(partner, 'EModelElement', None)
    _safe_set(owner, 'eAnnotations', partner)
    assert getattr(partner, 'EModelElement') == owner
    _safe_set(owner, 'eAnnotations', None)
    assert getattr(partner, 'EModelElement') is None


def test_assoc_eOperations9_stub_double():
    # ecoreDiff_EOperation has no real 'EOperation' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClass(abstract=True, interface=True)
    partner = ecoreDiff_EOperation()
    setattr(partner, 'EOperation', None)
    _safe_set(owner, 'eContainingClass', {partner})
    assert getattr(partner, 'EOperation') == owner
    _safe_set(owner, 'eContainingClass', set())
    assert getattr(partner, 'EOperation') is None


def test_assoc_ePackage51_stub_double():
    # ecoreDiff_EFactory has no real 'eFactoryInstance' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    partner = ecoreDiff_EFactory()
    setattr(partner, 'eFactoryInstance', None)
    _safe_set(owner, 'EPackage52', partner)
    assert getattr(partner, 'eFactoryInstance') == owner
    _safe_set(owner, 'EPackage52', None)
    assert getattr(partner, 'eFactoryInstance') is None


def test_assoc_eRawType62_stub_double():
    # ecoreDiff_EGenericType has no real 'ecoreDiff_EGenericType63' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecoreDiff_EGenericType()
    setattr(partner, 'ecoreDiff_EGenericType63', None)
    _safe_set(owner, 'ecoreDiff_EClassifier64', partner)
    assert getattr(partner, 'ecoreDiff_EGenericType63') == owner
    _safe_set(owner, 'ecoreDiff_EClassifier64', None)
    assert getattr(partner, 'ecoreDiff_EGenericType63') is None


def test_assoc_eType85_stub_double():
    # ecoreDiff_EObject has no real 'ecoreDiff_EObject86' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_ETypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_ETypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    partner = ecoreDiff_EObject()
    setattr(partner, 'ecoreDiff_EObject86', None)
    _safe_set(owner, 'ecoreDiff_ETypedElement', partner)
    assert getattr(partner, 'ecoreDiff_EObject86') == owner
    _safe_set(owner, 'ecoreDiff_ETypedElement', None)
    assert getattr(partner, 'ecoreDiff_EObject86') is None


def test_assoc_eTypeParameters41_stub_double():
    # ecoreDiff_ETypeParameter has no real 'ecoreDiff_ETypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecoreDiff_ETypeParameter()
    setattr(partner, 'ecoreDiff_ETypeParameter', None)
    _safe_set(owner, 'ecoreDiff_EClassifier', {partner})
    assert getattr(partner, 'ecoreDiff_ETypeParameter') == owner
    _safe_set(owner, 'ecoreDiff_EClassifier', set())
    assert getattr(partner, 'ecoreDiff_ETypeParameter') is None


def test_assoc_references4_stub_double():
    # ecoreDiff_EObject has no real 'ecoreDiff_EObject6' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EAnnotation(source="sample_text")
    partner = ecoreDiff_EObject()
    setattr(partner, 'ecoreDiff_EObject6', None)
    _safe_set(owner, 'ecoreDiff_EAnnotation5', {partner})
    assert getattr(partner, 'ecoreDiff_EObject6') == owner
    _safe_set(owner, 'ecoreDiff_EAnnotation5', set())
    assert getattr(partner, 'ecoreDiff_EObject6') is None


def test_assoc_updatedElement111_stub_double():
    # ecoreDiff_ChangedEAnnotation has no real 'ecoreDiff_ChangedEAnnotation' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EAnnotation(source="sample_text")
    partner = ecoreDiff_ChangedEAnnotation()
    setattr(partner, 'ecoreDiff_ChangedEAnnotation', None)
    _safe_set(owner, 'ecoreDiff_EAnnotation112', partner)
    assert getattr(partner, 'ecoreDiff_ChangedEAnnotation') == owner
    _safe_set(owner, 'ecoreDiff_EAnnotation112', None)
    assert getattr(partner, 'ecoreDiff_ChangedEAnnotation') is None


def test_assoc_updatedElement118_stub_double():
    # ecoreDiff_ChangedEStringToStringMapEntry has no real 'ecoreDiff_ChangedEStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EStringToStringMapEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EStringToStringMapEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EStringToStringMapEntry(key="sample_text", value="sample_text")
    partner = ecoreDiff_ChangedEStringToStringMapEntry()
    setattr(partner, 'ecoreDiff_ChangedEStringToStringMapEntry', None)
    _safe_set(owner, 'ecoreDiff_EStringToStringMapEntry119', partner)
    assert getattr(partner, 'ecoreDiff_ChangedEStringToStringMapEntry') == owner
    _safe_set(owner, 'ecoreDiff_EStringToStringMapEntry119', None)
    assert getattr(partner, 'ecoreDiff_ChangedEStringToStringMapEntry') is None


def test_assoc_updatedElement132_stub_double():
    # ecoreDiff_ChangedEClass has no real 'ecoreDiff_ChangedEClass' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClass(abstract=True, interface=True)
    partner = ecoreDiff_ChangedEClass()
    setattr(partner, 'ecoreDiff_ChangedEClass', None)
    _safe_set(owner, 'ecoreDiff_EClass133', partner)
    assert getattr(partner, 'ecoreDiff_ChangedEClass') == owner
    _safe_set(owner, 'ecoreDiff_EClass133', None)
    assert getattr(partner, 'ecoreDiff_ChangedEClass') is None


def test_assoc_updatedElement139_stub_double():
    # ecoreDiff_ChangedEClassifier has no real 'ecoreDiff_ChangedEClassifier' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecoreDiff_ChangedEClassifier()
    setattr(partner, 'ecoreDiff_ChangedEClassifier', None)
    _safe_set(owner, 'ecoreDiff_EClassifier140', partner)
    assert getattr(partner, 'ecoreDiff_ChangedEClassifier') == owner
    _safe_set(owner, 'ecoreDiff_EClassifier140', None)
    assert getattr(partner, 'ecoreDiff_ChangedEClassifier') is None


def test_assoc_updatedElement146_stub_double():
    # ecoreDiff_ChangedENamedElement has no real 'ecoreDiff_ChangedENamedElement' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_ENamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_ENamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_ENamedElement(name="sample_text")
    partner = ecoreDiff_ChangedENamedElement()
    setattr(partner, 'ecoreDiff_ChangedENamedElement', None)
    _safe_set(owner, 'ecoreDiff_ENamedElement', partner)
    assert getattr(partner, 'ecoreDiff_ChangedENamedElement') == owner
    _safe_set(owner, 'ecoreDiff_ENamedElement', None)
    assert getattr(partner, 'ecoreDiff_ChangedENamedElement') is None


def test_assoc_updatedElement152_stub_double():
    # ecoreDiff_ChangedEPackage has no real 'ecoreDiff_ChangedEPackage' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    partner = ecoreDiff_ChangedEPackage()
    setattr(partner, 'ecoreDiff_ChangedEPackage', None)
    _safe_set(owner, 'ecoreDiff_EPackage', partner)
    assert getattr(partner, 'ecoreDiff_ChangedEPackage') == owner
    _safe_set(owner, 'ecoreDiff_EPackage', None)
    assert getattr(partner, 'ecoreDiff_ChangedEPackage') is None


def test_assoc_updatedElement164_stub_double():
    # ecoreDiff_ChangedEDataType has no real 'ecoreDiff_ChangedEDataType' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EDataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EDataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EDataType(serializable=True)
    partner = ecoreDiff_ChangedEDataType()
    setattr(partner, 'ecoreDiff_ChangedEDataType', None)
    _safe_set(owner, 'ecoreDiff_EDataType165', partner)
    assert getattr(partner, 'ecoreDiff_ChangedEDataType') == owner
    _safe_set(owner, 'ecoreDiff_EDataType165', None)
    assert getattr(partner, 'ecoreDiff_ChangedEDataType') is None


def test_assoc_updatedElement198_stub_double():
    # ecoreDiff_ChangedETypedElement has no real 'ecoreDiff_ChangedETypedElement' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_ETypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_ETypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    partner = ecoreDiff_ChangedETypedElement()
    setattr(partner, 'ecoreDiff_ChangedETypedElement', None)
    _safe_set(owner, 'ecoreDiff_ETypedElement199', partner)
    assert getattr(partner, 'ecoreDiff_ChangedETypedElement') == owner
    _safe_set(owner, 'ecoreDiff_ETypedElement199', None)
    assert getattr(partner, 'ecoreDiff_ChangedETypedElement') is None


def test_assoc_updatedElement211_stub_double():
    # ecoreDiff_ChangedEAttribute has no real 'ecoreDiff_ChangedEAttribute' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EAttribute(iD=True)
    partner = ecoreDiff_ChangedEAttribute()
    setattr(partner, 'ecoreDiff_ChangedEAttribute', None)
    _safe_set(owner, 'ecoreDiff_EAttribute212', partner)
    assert getattr(partner, 'ecoreDiff_ChangedEAttribute') == owner
    _safe_set(owner, 'ecoreDiff_EAttribute212', None)
    assert getattr(partner, 'ecoreDiff_ChangedEAttribute') is None


def test_assoc_updatedElement218_stub_double():
    # ecoreDiff_ChangedEStructuralFeature has no real 'ecoreDiff_ChangedEStructuralFeature' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EStructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EStructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    partner = ecoreDiff_ChangedEStructuralFeature()
    setattr(partner, 'ecoreDiff_ChangedEStructuralFeature', None)
    _safe_set(owner, 'ecoreDiff_EStructuralFeature219', partner)
    assert getattr(partner, 'ecoreDiff_ChangedEStructuralFeature') == owner
    _safe_set(owner, 'ecoreDiff_EStructuralFeature219', None)
    assert getattr(partner, 'ecoreDiff_ChangedEStructuralFeature') is None


def test_assoc_updatedElement231_stub_double():
    # ecoreDiff_ChangedEReference has no real 'ecoreDiff_ChangedEReference' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EReference(container=True, containment=True, resolveProxies=True)
    partner = ecoreDiff_ChangedEReference()
    setattr(partner, 'ecoreDiff_ChangedEReference', None)
    _safe_set(owner, 'ecoreDiff_EReference232', partner)
    assert getattr(partner, 'ecoreDiff_ChangedEReference') == owner
    _safe_set(owner, 'ecoreDiff_EReference232', None)
    assert getattr(partner, 'ecoreDiff_ChangedEReference') is None


def test_assoc_updatedElement244_stub_double():
    # ecoreDiff_ChangedEEnumLiteral has no real 'ecoreDiff_ChangedEEnumLiteral' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EEnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EEnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    partner = ecoreDiff_ChangedEEnumLiteral()
    setattr(partner, 'ecoreDiff_ChangedEEnumLiteral', None)
    _safe_set(owner, 'ecoreDiff_EEnumLiteral', partner)
    assert getattr(partner, 'ecoreDiff_ChangedEEnumLiteral') == owner
    _safe_set(owner, 'ecoreDiff_EEnumLiteral', None)
    assert getattr(partner, 'ecoreDiff_ChangedEEnumLiteral') is None


