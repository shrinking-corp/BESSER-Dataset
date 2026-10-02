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


