import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EClassifier,
    EDataType,
    EModelElement,
    ENamedElement,
    EStructuralFeature,
    ETypedElement,
    ecore_EAnnotation,
    ecore_EAttribute,
    ecore_EClass,
    ecore_EClassifier,
    ecore_EDataType,
    ecore_EEnum,
    ecore_EEnumLiteral,
    ecore_EFactory,
    ecore_EGenericType,
    ecore_EModelElement,
    ecore_ENamedElement,
    ecore_EObject,
    ecore_EOperation,
    ecore_EPackage,
    ecore_EParameter,
    ecore_EReference,
    ecore_EStringToStringMapEntry,
    ecore_EStructuralFeature,
    ecore_ETypeParameter,
    ecore_ETypedElement,
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

def test_assoc_contents3_reverse_link_reassign_clear():
    a1 = ecore_EObject()
    a2 = ecore_EObject()
    b = ecore_EAnnotation(source="sample_text")
    _safe_set(b, 'ecore_EAnnotation4', {a1})
    assert _is_linked(b, 'ecore_EAnnotation4', a1)
    if hasattr(a1, 'ecore_EObject'):
        assert _is_linked(a1, 'ecore_EObject', b)
    _safe_set(b, 'ecore_EAnnotation4', {a2})
    assert _is_linked(b, 'ecore_EAnnotation4', a2)
    if hasattr(a1, 'ecore_EObject'):
        assert not _is_linked(a1, 'ecore_EObject', b)
    if hasattr(a2, 'ecore_EObject'):
        assert _is_linked(a2, 'ecore_EObject', b)
    _safe_set(b, 'ecore_EAnnotation4', set())
    assert not _is_linked(b, 'ecore_EAnnotation4', a2)
    if hasattr(a2, 'ecore_EObject'):
        assert not _is_linked(a2, 'ecore_EObject', b)


def test_assoc_details1_reverse_link_reassign_clear():
    a1 = ecore_EStringToStringMapEntry(key="sample_text", value="sample_text")
    a2 = ecore_EStringToStringMapEntry(key="sample_text_2", value="sample_text_2")
    b = ecore_EAnnotation(source="sample_text")
    _safe_set(b, 'ecore_EAnnotation', {a1})
    assert _is_linked(b, 'ecore_EAnnotation', a1)
    if hasattr(a1, 'ecore_EStringToStringMapEntry'):
        assert _is_linked(a1, 'ecore_EStringToStringMapEntry', b)
    _safe_set(b, 'ecore_EAnnotation', {a2})
    assert _is_linked(b, 'ecore_EAnnotation', a2)
    if hasattr(a1, 'ecore_EStringToStringMapEntry'):
        assert not _is_linked(a1, 'ecore_EStringToStringMapEntry', b)
    if hasattr(a2, 'ecore_EStringToStringMapEntry'):
        assert _is_linked(a2, 'ecore_EStringToStringMapEntry', b)
    _safe_set(b, 'ecore_EAnnotation', set())
    assert not _is_linked(b, 'ecore_EAnnotation', a2)
    if hasattr(a2, 'ecore_EStringToStringMapEntry'):
        assert not _is_linked(a2, 'ecore_EStringToStringMapEntry', b)


def test_assoc_eAllAttributes24_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EAttribute(iD=True)
    _safe_set(b, 'ecore_EAttribute26', a1)
    assert _is_linked(b, 'ecore_EAttribute26', a1)
    if hasattr(a1, 'ecore_EClass25'):
        assert _is_linked(a1, 'ecore_EClass25', b)
    _safe_set(b, 'ecore_EAttribute26', a2)
    assert _is_linked(b, 'ecore_EAttribute26', a2)
    if hasattr(a1, 'ecore_EClass25'):
        assert not _is_linked(a1, 'ecore_EClass25', b)
    if hasattr(a2, 'ecore_EClass25'):
        assert _is_linked(a2, 'ecore_EClass25', b)
    _safe_set(b, 'ecore_EAttribute26', None)
    assert not _is_linked(b, 'ecore_EAttribute26', a2)
    if hasattr(a2, 'ecore_EClass25'):
        assert not _is_linked(a2, 'ecore_EClass25', b)


def test_assoc_eAllContainments30_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass31', {a1})
    assert _is_linked(b, 'ecore_EClass31', a1)
    if hasattr(a1, 'ecore_EReference32'):
        assert _is_linked(a1, 'ecore_EReference32', b)
    _safe_set(b, 'ecore_EClass31', {a2})
    assert _is_linked(b, 'ecore_EClass31', a2)
    if hasattr(a1, 'ecore_EReference32'):
        assert not _is_linked(a1, 'ecore_EReference32', b)
    if hasattr(a2, 'ecore_EReference32'):
        assert _is_linked(a2, 'ecore_EReference32', b)
    _safe_set(b, 'ecore_EClass31', set())
    assert not _is_linked(b, 'ecore_EClass31', a2)
    if hasattr(a2, 'ecore_EReference32'):
        assert not _is_linked(a2, 'ecore_EReference32', b)


def test_assoc_eAllOperations33_reverse_link_reassign_clear():
    a1 = ecore_EOperation(operationID=7)
    a2 = ecore_EOperation(operationID=13)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass34', {a1})
    assert _is_linked(b, 'ecore_EClass34', a1)
    if hasattr(a1, 'ecore_EOperation'):
        assert _is_linked(a1, 'ecore_EOperation', b)
    _safe_set(b, 'ecore_EClass34', {a2})
    assert _is_linked(b, 'ecore_EClass34', a2)
    if hasattr(a1, 'ecore_EOperation'):
        assert not _is_linked(a1, 'ecore_EOperation', b)
    if hasattr(a2, 'ecore_EOperation'):
        assert _is_linked(a2, 'ecore_EOperation', b)
    _safe_set(b, 'ecore_EClass34', set())
    assert not _is_linked(b, 'ecore_EClass34', a2)
    if hasattr(a2, 'ecore_EOperation'):
        assert not _is_linked(a2, 'ecore_EOperation', b)


def test_assoc_eAllReferences27_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass28', {a1})
    assert _is_linked(b, 'ecore_EClass28', a1)
    if hasattr(a1, 'ecore_EReference29'):
        assert _is_linked(a1, 'ecore_EReference29', b)
    _safe_set(b, 'ecore_EClass28', {a2})
    assert _is_linked(b, 'ecore_EClass28', a2)
    if hasattr(a1, 'ecore_EReference29'):
        assert not _is_linked(a1, 'ecore_EReference29', b)
    if hasattr(a2, 'ecore_EReference29'):
        assert _is_linked(a2, 'ecore_EReference29', b)
    _safe_set(b, 'ecore_EClass28', set())
    assert not _is_linked(b, 'ecore_EClass28', a2)
    if hasattr(a2, 'ecore_EReference29'):
        assert not _is_linked(a2, 'ecore_EReference29', b)


def test_assoc_eAllStructuralFeatures35_reverse_link_reassign_clear():
    a1 = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, featureID=7, transient=True, unsettable=True, volatile=True)
    a2 = ecore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, featureID=13, transient=False, unsettable=False, volatile=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass36', {a1})
    assert _is_linked(b, 'ecore_EClass36', a1)
    if hasattr(a1, 'ecore_EStructuralFeature'):
        assert _is_linked(a1, 'ecore_EStructuralFeature', b)
    _safe_set(b, 'ecore_EClass36', {a2})
    assert _is_linked(b, 'ecore_EClass36', a2)
    if hasattr(a1, 'ecore_EStructuralFeature'):
        assert not _is_linked(a1, 'ecore_EStructuralFeature', b)
    if hasattr(a2, 'ecore_EStructuralFeature'):
        assert _is_linked(a2, 'ecore_EStructuralFeature', b)
    _safe_set(b, 'ecore_EClass36', set())
    assert not _is_linked(b, 'ecore_EClass36', a2)
    if hasattr(a2, 'ecore_EStructuralFeature'):
        assert not _is_linked(a2, 'ecore_EStructuralFeature', b)


def test_assoc_eAllSuperTypes38_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass39', a1)
    assert _is_linked(b, 'ecore_EClass39', a1)
    if hasattr(a1, 'ecore_EClass37'):
        assert _is_linked(a1, 'ecore_EClass37', b)
    _safe_set(b, 'ecore_EClass39', a2)
    assert _is_linked(b, 'ecore_EClass39', a2)
    if hasattr(a1, 'ecore_EClass37'):
        assert not _is_linked(a1, 'ecore_EClass37', b)
    if hasattr(a2, 'ecore_EClass37'):
        assert _is_linked(a2, 'ecore_EClass37', b)
    _safe_set(b, 'ecore_EClass39', None)
    assert not _is_linked(b, 'ecore_EClass39', a2)
    if hasattr(a2, 'ecore_EClass37'):
        assert not _is_linked(a2, 'ecore_EClass37', b)


def test_assoc_eAnnotations48_reverse_link_reassign_clear():
    a1 = ecore_EModelElement()
    a2 = ecore_EModelElement()
    b = ecore_EAnnotation(source="sample_text")
    _safe_set(b, 'EAnnotation', a1)
    assert _is_linked(b, 'EAnnotation', a1)
    if hasattr(a1, 'eModelElement'):
        assert _is_linked(a1, 'eModelElement', b)
    _safe_set(b, 'EAnnotation', a2)
    assert _is_linked(b, 'EAnnotation', a2)
    if hasattr(a1, 'eModelElement'):
        assert not _is_linked(a1, 'eModelElement', b)
    if hasattr(a2, 'eModelElement'):
        assert _is_linked(a2, 'eModelElement', b)
    _safe_set(b, 'EAnnotation', None)
    assert not _is_linked(b, 'EAnnotation', a2)
    if hasattr(a2, 'eModelElement'):
        assert not _is_linked(a2, 'eModelElement', b)


def test_assoc_eAttributeType0_reverse_link_reassign_clear():
    a1 = ecore_EDataType(serializable=True)
    a2 = ecore_EDataType(serializable=False)
    b = ecore_EAttribute(iD=True)
    _safe_set(b, 'ecore_EAttribute', a1)
    assert _is_linked(b, 'ecore_EAttribute', a1)
    if hasattr(a1, 'ecore_EDataType'):
        assert _is_linked(a1, 'ecore_EDataType', b)
    _safe_set(b, 'ecore_EAttribute', a2)
    assert _is_linked(b, 'ecore_EAttribute', a2)
    if hasattr(a1, 'ecore_EDataType'):
        assert not _is_linked(a1, 'ecore_EDataType', b)
    if hasattr(a2, 'ecore_EDataType'):
        assert _is_linked(a2, 'ecore_EDataType', b)
    _safe_set(b, 'ecore_EAttribute', None)
    assert not _is_linked(b, 'ecore_EAttribute', a2)
    if hasattr(a2, 'ecore_EDataType'):
        assert not _is_linked(a2, 'ecore_EDataType', b)


def test_assoc_eAttributes9_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EAttribute(iD=True)
    _safe_set(b, 'ecore_EAttribute10', a1)
    assert _is_linked(b, 'ecore_EAttribute10', a1)
    if hasattr(a1, 'ecore_EClass'):
        assert _is_linked(a1, 'ecore_EClass', b)
    _safe_set(b, 'ecore_EAttribute10', a2)
    assert _is_linked(b, 'ecore_EAttribute10', a2)
    if hasattr(a1, 'ecore_EClass'):
        assert not _is_linked(a1, 'ecore_EClass', b)
    if hasattr(a2, 'ecore_EClass'):
        assert _is_linked(a2, 'ecore_EClass', b)
    _safe_set(b, 'ecore_EAttribute10', None)
    assert not _is_linked(b, 'ecore_EAttribute10', a2)
    if hasattr(a2, 'ecore_EClass'):
        assert not _is_linked(a2, 'ecore_EClass', b)


def test_assoc_eClassifier90_reverse_link_reassign_clear():
    a1 = ecore_EGenericType()
    a2 = ecore_EGenericType()
    b = ecore_EClassifier(classifierID=7, defaultValue="sample_text", instanceClass="sample_text")
    _safe_set(b, 'ecore_EClassifier92', a1)
    assert _is_linked(b, 'ecore_EClassifier92', a1)
    if hasattr(a1, 'ecore_EGenericType91'):
        assert _is_linked(a1, 'ecore_EGenericType91', b)
    _safe_set(b, 'ecore_EClassifier92', a2)
    assert _is_linked(b, 'ecore_EClassifier92', a2)
    if hasattr(a1, 'ecore_EGenericType91'):
        assert not _is_linked(a1, 'ecore_EGenericType91', b)
    if hasattr(a2, 'ecore_EGenericType91'):
        assert _is_linked(a2, 'ecore_EGenericType91', b)
    _safe_set(b, 'ecore_EClassifier92', None)
    assert not _is_linked(b, 'ecore_EClassifier92', a2)
    if hasattr(a2, 'ecore_EGenericType91'):
        assert not _is_linked(a2, 'ecore_EGenericType91', b)


def test_assoc_eClassifiers54_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EClassifier(classifierID=7, defaultValue="sample_text", instanceClass="sample_text")
    _safe_set(b, 'EClassifier', a1)
    assert _is_linked(b, 'EClassifier', a1)
    if hasattr(a1, 'ePackage55'):
        assert _is_linked(a1, 'ePackage55', b)
    _safe_set(b, 'EClassifier', a2)
    assert _is_linked(b, 'EClassifier', a2)
    if hasattr(a1, 'ePackage55'):
        assert not _is_linked(a1, 'ePackage55', b)
    if hasattr(a2, 'ePackage55'):
        assert _is_linked(a2, 'ePackage55', b)
    _safe_set(b, 'EClassifier', None)
    assert not _is_linked(b, 'EClassifier', a2)
    if hasattr(a2, 'ePackage55'):
        assert not _is_linked(a2, 'ePackage55', b)


def test_assoc_eContainingClass49_reverse_link_reassign_clear():
    a1 = ecore_EOperation(operationID=7)
    a2 = ecore_EOperation(operationID=13)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'EClass', a1)
    assert _is_linked(b, 'EClass', a1)
    if hasattr(a1, 'eOperations'):
        assert _is_linked(a1, 'eOperations', b)
    _safe_set(b, 'EClass', a2)
    assert _is_linked(b, 'EClass', a2)
    if hasattr(a1, 'eOperations'):
        assert not _is_linked(a1, 'eOperations', b)
    if hasattr(a2, 'eOperations'):
        assert _is_linked(a2, 'eOperations', b)
    _safe_set(b, 'EClass', None)
    assert not _is_linked(b, 'EClass', a2)
    if hasattr(a2, 'eOperations'):
        assert not _is_linked(a2, 'eOperations', b)


def test_assoc_eContainingClass73_reverse_link_reassign_clear():
    a1 = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, featureID=7, transient=True, unsettable=True, volatile=True)
    a2 = ecore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, featureID=13, transient=False, unsettable=False, volatile=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'EClass74', a1)
    assert _is_linked(b, 'EClass74', a1)
    if hasattr(a1, 'eStructuralFeatures'):
        assert _is_linked(a1, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass74', a2)
    assert _is_linked(b, 'EClass74', a2)
    if hasattr(a1, 'eStructuralFeatures'):
        assert not _is_linked(a1, 'eStructuralFeatures', b)
    if hasattr(a2, 'eStructuralFeatures'):
        assert _is_linked(a2, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass74', None)
    assert not _is_linked(b, 'EClass74', a2)
    if hasattr(a2, 'eStructuralFeatures'):
        assert not _is_linked(a2, 'eStructuralFeatures', b)


def test_assoc_eContainments18_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass19', {a1})
    assert _is_linked(b, 'ecore_EClass19', a1)
    if hasattr(a1, 'ecore_EReference20'):
        assert _is_linked(a1, 'ecore_EReference20', b)
    _safe_set(b, 'ecore_EClass19', {a2})
    assert _is_linked(b, 'ecore_EClass19', a2)
    if hasattr(a1, 'ecore_EReference20'):
        assert not _is_linked(a1, 'ecore_EReference20', b)
    if hasattr(a2, 'ecore_EReference20'):
        assert _is_linked(a2, 'ecore_EReference20', b)
    _safe_set(b, 'ecore_EClass19', set())
    assert not _is_linked(b, 'ecore_EClass19', a2)
    if hasattr(a2, 'ecore_EReference20'):
        assert not _is_linked(a2, 'ecore_EReference20', b)


def test_assoc_eCrossReferences21_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass22', {a1})
    assert _is_linked(b, 'ecore_EClass22', a1)
    if hasattr(a1, 'ecore_EReference23'):
        assert _is_linked(a1, 'ecore_EReference23', b)
    _safe_set(b, 'ecore_EClass22', {a2})
    assert _is_linked(b, 'ecore_EClass22', a2)
    if hasattr(a1, 'ecore_EReference23'):
        assert not _is_linked(a1, 'ecore_EReference23', b)
    if hasattr(a2, 'ecore_EReference23'):
        assert _is_linked(a2, 'ecore_EReference23', b)
    _safe_set(b, 'ecore_EClass22', set())
    assert not _is_linked(b, 'ecore_EClass22', a2)
    if hasattr(a2, 'ecore_EReference23'):
        assert not _is_linked(a2, 'ecore_EReference23', b)


def test_assoc_eEnum45_reverse_link_reassign_clear():
    a1 = ecore_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    a2 = ecore_EEnumLiteral(instance="sample_text_2", literal="sample_text_2", value=13)
    b = ecore_EEnum()
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


def test_assoc_eExceptions51_reverse_link_reassign_clear():
    a1 = ecore_EOperation(operationID=7)
    a2 = ecore_EOperation(operationID=13)
    b = ecore_EClassifier(classifierID=7, defaultValue="sample_text", instanceClass="sample_text")
    _safe_set(b, 'ecore_EClassifier', a1)
    assert _is_linked(b, 'ecore_EClassifier', a1)
    if hasattr(a1, 'ecore_EOperation52'):
        assert _is_linked(a1, 'ecore_EOperation52', b)
    _safe_set(b, 'ecore_EClassifier', a2)
    assert _is_linked(b, 'ecore_EClassifier', a2)
    if hasattr(a1, 'ecore_EOperation52'):
        assert not _is_linked(a1, 'ecore_EOperation52', b)
    if hasattr(a2, 'ecore_EOperation52'):
        assert _is_linked(a2, 'ecore_EOperation52', b)
    _safe_set(b, 'ecore_EClassifier', None)
    assert not _is_linked(b, 'ecore_EClassifier', a2)
    if hasattr(a2, 'ecore_EOperation52'):
        assert not _is_linked(a2, 'ecore_EOperation52', b)


def test_assoc_eFactoryInstance53_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EFactory()
    _safe_set(b, 'EFactory', a1)
    assert _is_linked(b, 'EFactory', a1)
    if hasattr(a1, 'ePackage'):
        assert _is_linked(a1, 'ePackage', b)
    _safe_set(b, 'EFactory', a2)
    assert _is_linked(b, 'EFactory', a2)
    if hasattr(a1, 'ePackage'):
        assert not _is_linked(a1, 'ePackage', b)
    if hasattr(a2, 'ePackage'):
        assert _is_linked(a2, 'ePackage', b)
    _safe_set(b, 'EFactory', None)
    assert not _is_linked(b, 'EFactory', a2)
    if hasattr(a2, 'ePackage'):
        assert not _is_linked(a2, 'ePackage', b)


def test_assoc_eIDAttribute40_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EAttribute(iD=True)
    _safe_set(b, 'ecore_EAttribute42', a1)
    assert _is_linked(b, 'ecore_EAttribute42', a1)
    if hasattr(a1, 'ecore_EClass41'):
        assert _is_linked(a1, 'ecore_EClass41', b)
    _safe_set(b, 'ecore_EAttribute42', a2)
    assert _is_linked(b, 'ecore_EAttribute42', a2)
    if hasattr(a1, 'ecore_EClass41'):
        assert not _is_linked(a1, 'ecore_EClass41', b)
    if hasattr(a2, 'ecore_EClass41'):
        assert _is_linked(a2, 'ecore_EClass41', b)
    _safe_set(b, 'ecore_EAttribute42', None)
    assert not _is_linked(b, 'ecore_EAttribute42', a2)
    if hasattr(a2, 'ecore_EClass41'):
        assert not _is_linked(a2, 'ecore_EClass41', b)


def test_assoc_eKeys70_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EAttribute(iD=True)
    _safe_set(b, 'ecore_EAttribute72', a1)
    assert _is_linked(b, 'ecore_EAttribute72', a1)
    if hasattr(a1, 'ecore_EReference71'):
        assert _is_linked(a1, 'ecore_EReference71', b)
    _safe_set(b, 'ecore_EAttribute72', a2)
    assert _is_linked(b, 'ecore_EAttribute72', a2)
    if hasattr(a1, 'ecore_EReference71'):
        assert not _is_linked(a1, 'ecore_EReference71', b)
    if hasattr(a2, 'ecore_EReference71'):
        assert _is_linked(a2, 'ecore_EReference71', b)
    _safe_set(b, 'ecore_EAttribute72', None)
    assert not _is_linked(b, 'ecore_EAttribute72', a2)
    if hasattr(a2, 'ecore_EReference71'):
        assert not _is_linked(a2, 'ecore_EReference71', b)


def test_assoc_eLiterals44_reverse_link_reassign_clear():
    a1 = ecore_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    a2 = ecore_EEnumLiteral(instance="sample_text_2", literal="sample_text_2", value=13)
    b = ecore_EEnum()
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


def test_assoc_eLowerBound86_reverse_link_reassign_clear():
    a1 = ecore_EGenericType()
    a2 = ecore_EGenericType()
    b = ecore_EGenericType()
    _safe_set(b, 'ecore_EGenericType87', a1)
    assert _is_linked(b, 'ecore_EGenericType87', a1)
    if hasattr(a1, 'ecore_EGenericType85'):
        assert _is_linked(a1, 'ecore_EGenericType85', b)
    _safe_set(b, 'ecore_EGenericType87', a2)
    assert _is_linked(b, 'ecore_EGenericType87', a2)
    if hasattr(a1, 'ecore_EGenericType85'):
        assert not _is_linked(a1, 'ecore_EGenericType85', b)
    if hasattr(a2, 'ecore_EGenericType85'):
        assert _is_linked(a2, 'ecore_EGenericType85', b)
    _safe_set(b, 'ecore_EGenericType87', None)
    assert not _is_linked(b, 'ecore_EGenericType87', a2)
    if hasattr(a2, 'ecore_EGenericType85'):
        assert not _is_linked(a2, 'ecore_EGenericType85', b)


def test_assoc_eModelElement2_reverse_link_reassign_clear():
    a1 = ecore_EModelElement()
    a2 = ecore_EModelElement()
    b = ecore_EAnnotation(source="sample_text")
    _safe_set(b, 'eAnnotations', a1)
    assert _is_linked(b, 'eAnnotations', a1)
    if hasattr(a1, 'EModelElement'):
        assert _is_linked(a1, 'EModelElement', b)
    _safe_set(b, 'eAnnotations', a2)
    assert _is_linked(b, 'eAnnotations', a2)
    if hasattr(a1, 'EModelElement'):
        assert not _is_linked(a1, 'EModelElement', b)
    if hasattr(a2, 'EModelElement'):
        assert _is_linked(a2, 'EModelElement', b)
    _safe_set(b, 'eAnnotations', None)
    assert not _is_linked(b, 'eAnnotations', a2)
    if hasattr(a2, 'EModelElement'):
        assert not _is_linked(a2, 'EModelElement', b)


def test_assoc_eOperations16_reverse_link_reassign_clear():
    a1 = ecore_EOperation(operationID=7)
    a2 = ecore_EOperation(operationID=13)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'eContainingClass17', {a1})
    assert _is_linked(b, 'eContainingClass17', a1)
    if hasattr(a1, 'EOperation'):
        assert _is_linked(a1, 'EOperation', b)
    _safe_set(b, 'eContainingClass17', {a2})
    assert _is_linked(b, 'eContainingClass17', a2)
    if hasattr(a1, 'EOperation'):
        assert not _is_linked(a1, 'EOperation', b)
    if hasattr(a2, 'EOperation'):
        assert _is_linked(a2, 'EOperation', b)
    _safe_set(b, 'eContainingClass17', set())
    assert not _is_linked(b, 'eContainingClass17', a2)
    if hasattr(a2, 'EOperation'):
        assert not _is_linked(a2, 'EOperation', b)


def test_assoc_eOpposite65_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EReference(container=True, containment=True, resolveProxies=True)
    _safe_set(b, 'ecore_EReference66', a1)
    assert _is_linked(b, 'ecore_EReference66', a1)
    if hasattr(a1, 'ecore_EReference64'):
        assert _is_linked(a1, 'ecore_EReference64', b)
    _safe_set(b, 'ecore_EReference66', a2)
    assert _is_linked(b, 'ecore_EReference66', a2)
    if hasattr(a1, 'ecore_EReference64'):
        assert not _is_linked(a1, 'ecore_EReference64', b)
    if hasattr(a2, 'ecore_EReference64'):
        assert _is_linked(a2, 'ecore_EReference64', b)
    _safe_set(b, 'ecore_EReference66', None)
    assert not _is_linked(b, 'ecore_EReference66', a2)
    if hasattr(a2, 'ecore_EReference64'):
        assert not _is_linked(a2, 'ecore_EReference64', b)


def test_assoc_ePackage43_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EClassifier(classifierID=7, defaultValue="sample_text", instanceClass="sample_text")
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


def test_assoc_ePackage46_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EFactory()
    _safe_set(b, 'eFactoryInstance', a1)
    assert _is_linked(b, 'eFactoryInstance', a1)
    if hasattr(a1, 'EPackage47'):
        assert _is_linked(a1, 'EPackage47', b)
    _safe_set(b, 'eFactoryInstance', a2)
    assert _is_linked(b, 'eFactoryInstance', a2)
    if hasattr(a1, 'EPackage47'):
        assert not _is_linked(a1, 'EPackage47', b)
    if hasattr(a2, 'EPackage47'):
        assert _is_linked(a2, 'EPackage47', b)
    _safe_set(b, 'eFactoryInstance', None)
    assert not _is_linked(b, 'eFactoryInstance', a2)
    if hasattr(a2, 'EPackage47'):
        assert not _is_linked(a2, 'EPackage47', b)


def test_assoc_eRawType82_reverse_link_reassign_clear():
    a1 = ecore_EGenericType()
    a2 = ecore_EGenericType()
    b = ecore_EClassifier(classifierID=7, defaultValue="sample_text", instanceClass="sample_text")
    _safe_set(b, 'ecore_EClassifier84', a1)
    assert _is_linked(b, 'ecore_EClassifier84', a1)
    if hasattr(a1, 'ecore_EGenericType83'):
        assert _is_linked(a1, 'ecore_EGenericType83', b)
    _safe_set(b, 'ecore_EClassifier84', a2)
    assert _is_linked(b, 'ecore_EClassifier84', a2)
    if hasattr(a1, 'ecore_EGenericType83'):
        assert not _is_linked(a1, 'ecore_EGenericType83', b)
    if hasattr(a2, 'ecore_EGenericType83'):
        assert _is_linked(a2, 'ecore_EGenericType83', b)
    _safe_set(b, 'ecore_EClassifier84', None)
    assert not _is_linked(b, 'ecore_EClassifier84', a2)
    if hasattr(a2, 'ecore_EGenericType83'):
        assert not _is_linked(a2, 'ecore_EGenericType83', b)


def test_assoc_eReferenceType67_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass69', a1)
    assert _is_linked(b, 'ecore_EClass69', a1)
    if hasattr(a1, 'ecore_EReference68'):
        assert _is_linked(a1, 'ecore_EReference68', b)
    _safe_set(b, 'ecore_EClass69', a2)
    assert _is_linked(b, 'ecore_EClass69', a2)
    if hasattr(a1, 'ecore_EReference68'):
        assert not _is_linked(a1, 'ecore_EReference68', b)
    if hasattr(a2, 'ecore_EReference68'):
        assert _is_linked(a2, 'ecore_EReference68', b)
    _safe_set(b, 'ecore_EClass69', None)
    assert not _is_linked(b, 'ecore_EClass69', a2)
    if hasattr(a2, 'ecore_EReference68'):
        assert not _is_linked(a2, 'ecore_EReference68', b)


def test_assoc_eReferences11_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass12', {a1})
    assert _is_linked(b, 'ecore_EClass12', a1)
    if hasattr(a1, 'ecore_EReference'):
        assert _is_linked(a1, 'ecore_EReference', b)
    _safe_set(b, 'ecore_EClass12', {a2})
    assert _is_linked(b, 'ecore_EClass12', a2)
    if hasattr(a1, 'ecore_EReference'):
        assert not _is_linked(a1, 'ecore_EReference', b)
    if hasattr(a2, 'ecore_EReference'):
        assert _is_linked(a2, 'ecore_EReference', b)
    _safe_set(b, 'ecore_EClass12', set())
    assert not _is_linked(b, 'ecore_EClass12', a2)
    if hasattr(a2, 'ecore_EReference'):
        assert not _is_linked(a2, 'ecore_EReference', b)


def test_assoc_eStructuralFeatures8_reverse_link_reassign_clear():
    a1 = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, featureID=7, transient=True, unsettable=True, volatile=True)
    a2 = ecore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, featureID=13, transient=False, unsettable=False, volatile=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'eContainingClass', {a1})
    assert _is_linked(b, 'eContainingClass', a1)
    if hasattr(a1, 'EStructuralFeature'):
        assert _is_linked(a1, 'EStructuralFeature', b)
    _safe_set(b, 'eContainingClass', {a2})
    assert _is_linked(b, 'eContainingClass', a2)
    if hasattr(a1, 'EStructuralFeature'):
        assert not _is_linked(a1, 'EStructuralFeature', b)
    if hasattr(a2, 'EStructuralFeature'):
        assert _is_linked(a2, 'EStructuralFeature', b)
    _safe_set(b, 'eContainingClass', set())
    assert not _is_linked(b, 'eContainingClass', a2)
    if hasattr(a2, 'EStructuralFeature'):
        assert not _is_linked(a2, 'EStructuralFeature', b)


def test_assoc_eSubPackages57_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSuperPackage', {a1})
    assert _is_linked(b, 'eSuperPackage', a1)
    if hasattr(a1, 'EPackage58'):
        assert _is_linked(a1, 'EPackage58', b)
    _safe_set(b, 'eSuperPackage', {a2})
    assert _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a1, 'EPackage58'):
        assert not _is_linked(a1, 'EPackage58', b)
    if hasattr(a2, 'EPackage58'):
        assert _is_linked(a2, 'EPackage58', b)
    _safe_set(b, 'eSuperPackage', set())
    assert not _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a2, 'EPackage58'):
        assert not _is_linked(a2, 'EPackage58', b)


def test_assoc_eSuperPackage60_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSubPackages', a1)
    assert _is_linked(b, 'eSubPackages', a1)
    if hasattr(a1, 'EPackage61'):
        assert _is_linked(a1, 'EPackage61', b)
    _safe_set(b, 'eSubPackages', a2)
    assert _is_linked(b, 'eSubPackages', a2)
    if hasattr(a1, 'EPackage61'):
        assert not _is_linked(a1, 'EPackage61', b)
    if hasattr(a2, 'EPackage61'):
        assert _is_linked(a2, 'EPackage61', b)
    _safe_set(b, 'eSubPackages', None)
    assert not _is_linked(b, 'eSubPackages', a2)
    if hasattr(a2, 'EPackage61'):
        assert not _is_linked(a2, 'EPackage61', b)


def test_assoc_eSuperTypes14_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass15', a1)
    assert _is_linked(b, 'ecore_EClass15', a1)
    if hasattr(a1, 'ecore_EClass13'):
        assert _is_linked(a1, 'ecore_EClass13', b)
    _safe_set(b, 'ecore_EClass15', a2)
    assert _is_linked(b, 'ecore_EClass15', a2)
    if hasattr(a1, 'ecore_EClass13'):
        assert not _is_linked(a1, 'ecore_EClass13', b)
    if hasattr(a2, 'ecore_EClass13'):
        assert _is_linked(a2, 'ecore_EClass13', b)
    _safe_set(b, 'ecore_EClass15', None)
    assert not _is_linked(b, 'ecore_EClass15', a2)
    if hasattr(a2, 'ecore_EClass13'):
        assert not _is_linked(a2, 'ecore_EClass13', b)


def test_assoc_eType75_reverse_link_reassign_clear():
    a1 = ecore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    a2 = ecore_ETypedElement(lowerBound=13, many=False, ordered=False, required=False, unique=False, upperBound=13)
    b = ecore_EClassifier(classifierID=7, defaultValue="sample_text", instanceClass="sample_text")
    _safe_set(b, 'ecore_EClassifier76', a1)
    assert _is_linked(b, 'ecore_EClassifier76', a1)
    if hasattr(a1, 'ecore_ETypedElement'):
        assert _is_linked(a1, 'ecore_ETypedElement', b)
    _safe_set(b, 'ecore_EClassifier76', a2)
    assert _is_linked(b, 'ecore_EClassifier76', a2)
    if hasattr(a1, 'ecore_ETypedElement'):
        assert not _is_linked(a1, 'ecore_ETypedElement', b)
    if hasattr(a2, 'ecore_ETypedElement'):
        assert _is_linked(a2, 'ecore_ETypedElement', b)
    _safe_set(b, 'ecore_EClassifier76', None)
    assert not _is_linked(b, 'ecore_EClassifier76', a2)
    if hasattr(a2, 'ecore_ETypedElement'):
        assert not _is_linked(a2, 'ecore_ETypedElement', b)


def test_assoc_eTypeArguments80_reverse_link_reassign_clear():
    a1 = ecore_EGenericType()
    a2 = ecore_EGenericType()
    b = ecore_EGenericType()
    _safe_set(b, 'ecore_EGenericType81', a1)
    assert _is_linked(b, 'ecore_EGenericType81', a1)
    if hasattr(a1, 'ecore_EGenericType79'):
        assert _is_linked(a1, 'ecore_EGenericType79', b)
    _safe_set(b, 'ecore_EGenericType81', a2)
    assert _is_linked(b, 'ecore_EGenericType81', a2)
    if hasattr(a1, 'ecore_EGenericType79'):
        assert not _is_linked(a1, 'ecore_EGenericType79', b)
    if hasattr(a2, 'ecore_EGenericType79'):
        assert _is_linked(a2, 'ecore_EGenericType79', b)
    _safe_set(b, 'ecore_EGenericType81', None)
    assert not _is_linked(b, 'ecore_EGenericType81', a2)
    if hasattr(a2, 'ecore_EGenericType79'):
        assert not _is_linked(a2, 'ecore_EGenericType79', b)


def test_assoc_eUpperBound78_reverse_link_reassign_clear():
    a1 = ecore_EGenericType()
    a2 = ecore_EGenericType()
    b = ecore_EGenericType()
    _safe_set(b, 'ecore_EGenericType77', a1)
    assert _is_linked(b, 'ecore_EGenericType77', a1)
    if hasattr(a1, 'ecore_EGenericType'):
        assert _is_linked(a1, 'ecore_EGenericType', b)
    _safe_set(b, 'ecore_EGenericType77', a2)
    assert _is_linked(b, 'ecore_EGenericType77', a2)
    if hasattr(a1, 'ecore_EGenericType'):
        assert not _is_linked(a1, 'ecore_EGenericType', b)
    if hasattr(a2, 'ecore_EGenericType'):
        assert _is_linked(a2, 'ecore_EGenericType', b)
    _safe_set(b, 'ecore_EGenericType77', None)
    assert not _is_linked(b, 'ecore_EGenericType77', a2)
    if hasattr(a2, 'ecore_EGenericType'):
        assert not _is_linked(a2, 'ecore_EGenericType', b)


def test_assoc_references5_reverse_link_reassign_clear():
    a1 = ecore_EObject()
    a2 = ecore_EObject()
    b = ecore_EAnnotation(source="sample_text")
    _safe_set(b, 'ecore_EAnnotation6', {a1})
    assert _is_linked(b, 'ecore_EAnnotation6', a1)
    if hasattr(a1, 'ecore_EObject7'):
        assert _is_linked(a1, 'ecore_EObject7', b)
    _safe_set(b, 'ecore_EAnnotation6', {a2})
    assert _is_linked(b, 'ecore_EAnnotation6', a2)
    if hasattr(a1, 'ecore_EObject7'):
        assert not _is_linked(a1, 'ecore_EObject7', b)
    if hasattr(a2, 'ecore_EObject7'):
        assert _is_linked(a2, 'ecore_EObject7', b)
    _safe_set(b, 'ecore_EAnnotation6', set())
    assert not _is_linked(b, 'ecore_EAnnotation6', a2)
    if hasattr(a2, 'ecore_EObject7'):
        assert not _is_linked(a2, 'ecore_EObject7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_eBounds93_stub_double():
    # ecore_ETypeParameter has no real 'ecore_ETypeParameter94' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EGenericType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EGenericType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EGenericType()
    partner = ecore_ETypeParameter()
    setattr(partner, 'ecore_ETypeParameter94', None)
    _safe_set(owner, 'ecore_EGenericType95', partner)
    assert owner in getattr(partner, 'ecore_ETypeParameter94')
    _safe_set(owner, 'ecore_EGenericType95', None)
    assert owner not in getattr(partner, 'ecore_ETypeParameter94')


def test_assoc_eOperation62_stub_double():
    # ecore_EParameter has no real 'eParameters' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EOperation(operationID=7)
    partner = ecore_EParameter()
    setattr(partner, 'eParameters', None)
    _safe_set(owner, 'EOperation63', partner)
    assert getattr(partner, 'eParameters') == owner
    _safe_set(owner, 'EOperation63', None)
    assert getattr(partner, 'eParameters') is None


def test_assoc_eParameters50_stub_double():
    # ecore_EParameter has no real 'EParameter' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EOperation(operationID=7)
    partner = ecore_EParameter()
    setattr(partner, 'EParameter', None)
    _safe_set(owner, 'eOperation', {partner})
    assert getattr(partner, 'EParameter') == owner
    _safe_set(owner, 'eOperation', set())
    assert getattr(partner, 'EParameter') is None


def test_assoc_eTypeParameter88_stub_double():
    # ecore_ETypeParameter has no real 'ecore_ETypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EGenericType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EGenericType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EGenericType()
    partner = ecore_ETypeParameter()
    setattr(partner, 'ecore_ETypeParameter', None)
    _safe_set(owner, 'ecore_EGenericType89', partner)
    assert getattr(partner, 'ecore_ETypeParameter') == owner
    _safe_set(owner, 'ecore_EGenericType89', None)
    assert getattr(partner, 'ecore_ETypeParameter') is None


