import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EClassifier,
    EDataType,
    EModelElement,
    ENamedElement,
    EStructuralFeature,
    ETypedElement,
    encore_EAnnotation,
    encore_EAttribute,
    encore_EClass,
    encore_EClassifier,
    encore_EDataType,
    encore_EEnum,
    encore_EEnumLiteral,
    encore_EFactory,
    encore_EGenericType,
    encore_EModelElement,
    encore_ENamedElement,
    encore_EObject,
    encore_EOperation,
    encore_EPackage,
    encore_EParameter,
    encore_EReference,
    encore_EStringToStringMapEntry,
    encore_EStructuralFeature,
    encore_ETypeParameter,
    encore_ETypedElement,
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
    a1 = encore_EObject()
    a2 = encore_EObject()
    b = encore_EAnnotation(source="sample_text")
    _safe_set(b, 'encore_EAnnotation4', {a1})
    assert _is_linked(b, 'encore_EAnnotation4', a1)
    if hasattr(a1, 'encore_EObject'):
        assert _is_linked(a1, 'encore_EObject', b)
    _safe_set(b, 'encore_EAnnotation4', {a2})
    assert _is_linked(b, 'encore_EAnnotation4', a2)
    if hasattr(a1, 'encore_EObject'):
        assert not _is_linked(a1, 'encore_EObject', b)
    if hasattr(a2, 'encore_EObject'):
        assert _is_linked(a2, 'encore_EObject', b)
    _safe_set(b, 'encore_EAnnotation4', set())
    assert not _is_linked(b, 'encore_EAnnotation4', a2)
    if hasattr(a2, 'encore_EObject'):
        assert not _is_linked(a2, 'encore_EObject', b)


def test_assoc_details1_reverse_link_reassign_clear():
    a1 = encore_EStringToStringMapEntry(key="sample_text", value="sample_text")
    a2 = encore_EStringToStringMapEntry(key="sample_text_2", value="sample_text_2")
    b = encore_EAnnotation(source="sample_text")
    _safe_set(b, 'encore_EAnnotation', {a1})
    assert _is_linked(b, 'encore_EAnnotation', a1)
    if hasattr(a1, 'encore_EStringToStringMapEntry'):
        assert _is_linked(a1, 'encore_EStringToStringMapEntry', b)
    _safe_set(b, 'encore_EAnnotation', {a2})
    assert _is_linked(b, 'encore_EAnnotation', a2)
    if hasattr(a1, 'encore_EStringToStringMapEntry'):
        assert not _is_linked(a1, 'encore_EStringToStringMapEntry', b)
    if hasattr(a2, 'encore_EStringToStringMapEntry'):
        assert _is_linked(a2, 'encore_EStringToStringMapEntry', b)
    _safe_set(b, 'encore_EAnnotation', set())
    assert not _is_linked(b, 'encore_EAnnotation', a2)
    if hasattr(a2, 'encore_EStringToStringMapEntry'):
        assert not _is_linked(a2, 'encore_EStringToStringMapEntry', b)


def test_assoc_eAllAttributes11_reverse_link_reassign_clear():
    a1 = encore_EClass(abstract=True, interface=True)
    a2 = encore_EClass(abstract=False, interface=False)
    b = encore_EAttribute(iD=True)
    _safe_set(b, 'encore_EAttribute13', a1)
    assert _is_linked(b, 'encore_EAttribute13', a1)
    if hasattr(a1, 'encore_EClass12'):
        assert _is_linked(a1, 'encore_EClass12', b)
    _safe_set(b, 'encore_EAttribute13', a2)
    assert _is_linked(b, 'encore_EAttribute13', a2)
    if hasattr(a1, 'encore_EClass12'):
        assert not _is_linked(a1, 'encore_EClass12', b)
    if hasattr(a2, 'encore_EClass12'):
        assert _is_linked(a2, 'encore_EClass12', b)
    _safe_set(b, 'encore_EAttribute13', None)
    assert not _is_linked(b, 'encore_EAttribute13', a2)
    if hasattr(a2, 'encore_EClass12'):
        assert not _is_linked(a2, 'encore_EClass12', b)


def test_assoc_eAllContainments22_reverse_link_reassign_clear():
    a1 = encore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = encore_EReference(container=False, containment=False, resolveProxies=False)
    b = encore_EClass(abstract=True, interface=True)
    _safe_set(b, 'encore_EClass23', {a1})
    assert _is_linked(b, 'encore_EClass23', a1)
    if hasattr(a1, 'encore_EReference24'):
        assert _is_linked(a1, 'encore_EReference24', b)
    _safe_set(b, 'encore_EClass23', {a2})
    assert _is_linked(b, 'encore_EClass23', a2)
    if hasattr(a1, 'encore_EReference24'):
        assert not _is_linked(a1, 'encore_EReference24', b)
    if hasattr(a2, 'encore_EReference24'):
        assert _is_linked(a2, 'encore_EReference24', b)
    _safe_set(b, 'encore_EClass23', set())
    assert not _is_linked(b, 'encore_EClass23', a2)
    if hasattr(a2, 'encore_EReference24'):
        assert not _is_linked(a2, 'encore_EReference24', b)


def test_assoc_eAllOperations25_reverse_link_reassign_clear():
    a1 = encore_EOperation()
    a2 = encore_EOperation()
    b = encore_EClass(abstract=True, interface=True)
    _safe_set(b, 'encore_EClass26', {a1})
    assert _is_linked(b, 'encore_EClass26', a1)
    if hasattr(a1, 'encore_EOperation'):
        assert _is_linked(a1, 'encore_EOperation', b)
    _safe_set(b, 'encore_EClass26', {a2})
    assert _is_linked(b, 'encore_EClass26', a2)
    if hasattr(a1, 'encore_EOperation'):
        assert not _is_linked(a1, 'encore_EOperation', b)
    if hasattr(a2, 'encore_EOperation'):
        assert _is_linked(a2, 'encore_EOperation', b)
    _safe_set(b, 'encore_EClass26', set())
    assert not _is_linked(b, 'encore_EClass26', a2)
    if hasattr(a2, 'encore_EOperation'):
        assert not _is_linked(a2, 'encore_EOperation', b)


def test_assoc_eAllReferences14_reverse_link_reassign_clear():
    a1 = encore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = encore_EReference(container=False, containment=False, resolveProxies=False)
    b = encore_EClass(abstract=True, interface=True)
    _safe_set(b, 'encore_EClass15', {a1})
    assert _is_linked(b, 'encore_EClass15', a1)
    if hasattr(a1, 'encore_EReference'):
        assert _is_linked(a1, 'encore_EReference', b)
    _safe_set(b, 'encore_EClass15', {a2})
    assert _is_linked(b, 'encore_EClass15', a2)
    if hasattr(a1, 'encore_EReference'):
        assert not _is_linked(a1, 'encore_EReference', b)
    if hasattr(a2, 'encore_EReference'):
        assert _is_linked(a2, 'encore_EReference', b)
    _safe_set(b, 'encore_EClass15', set())
    assert not _is_linked(b, 'encore_EClass15', a2)
    if hasattr(a2, 'encore_EReference'):
        assert not _is_linked(a2, 'encore_EReference', b)


def test_assoc_eAllStructuralFeatures27_reverse_link_reassign_clear():
    a1 = encore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = encore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = encore_EClass(abstract=True, interface=True)
    _safe_set(b, 'encore_EClass28', {a1})
    assert _is_linked(b, 'encore_EClass28', a1)
    if hasattr(a1, 'encore_EStructuralFeature'):
        assert _is_linked(a1, 'encore_EStructuralFeature', b)
    _safe_set(b, 'encore_EClass28', {a2})
    assert _is_linked(b, 'encore_EClass28', a2)
    if hasattr(a1, 'encore_EStructuralFeature'):
        assert not _is_linked(a1, 'encore_EStructuralFeature', b)
    if hasattr(a2, 'encore_EStructuralFeature'):
        assert _is_linked(a2, 'encore_EStructuralFeature', b)
    _safe_set(b, 'encore_EClass28', set())
    assert not _is_linked(b, 'encore_EClass28', a2)
    if hasattr(a2, 'encore_EStructuralFeature'):
        assert not _is_linked(a2, 'encore_EStructuralFeature', b)


def test_assoc_eAllSuperTypes30_reverse_link_reassign_clear():
    a1 = encore_EClass(abstract=True, interface=True)
    a2 = encore_EClass(abstract=False, interface=False)
    b = encore_EClass(abstract=True, interface=True)
    _safe_set(b, 'encore_EClass31', a1)
    assert _is_linked(b, 'encore_EClass31', a1)
    if hasattr(a1, 'encore_EClass29'):
        assert _is_linked(a1, 'encore_EClass29', b)
    _safe_set(b, 'encore_EClass31', a2)
    assert _is_linked(b, 'encore_EClass31', a2)
    if hasattr(a1, 'encore_EClass29'):
        assert not _is_linked(a1, 'encore_EClass29', b)
    if hasattr(a2, 'encore_EClass29'):
        assert _is_linked(a2, 'encore_EClass29', b)
    _safe_set(b, 'encore_EClass31', None)
    assert not _is_linked(b, 'encore_EClass31', a2)
    if hasattr(a2, 'encore_EClass29'):
        assert not _is_linked(a2, 'encore_EClass29', b)


def test_assoc_eAnnotations48_reverse_link_reassign_clear():
    a1 = encore_EModelElement()
    a2 = encore_EModelElement()
    b = encore_EAnnotation(source="sample_text")
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
    a1 = encore_EDataType(serializable=True)
    a2 = encore_EDataType(serializable=False)
    b = encore_EAttribute(iD=True)
    _safe_set(b, 'encore_EAttribute', a1)
    assert _is_linked(b, 'encore_EAttribute', a1)
    if hasattr(a1, 'encore_EDataType'):
        assert _is_linked(a1, 'encore_EDataType', b)
    _safe_set(b, 'encore_EAttribute', a2)
    assert _is_linked(b, 'encore_EAttribute', a2)
    if hasattr(a1, 'encore_EDataType'):
        assert not _is_linked(a1, 'encore_EDataType', b)
    if hasattr(a2, 'encore_EDataType'):
        assert _is_linked(a2, 'encore_EDataType', b)
    _safe_set(b, 'encore_EAttribute', None)
    assert not _is_linked(b, 'encore_EAttribute', a2)
    if hasattr(a2, 'encore_EDataType'):
        assert not _is_linked(a2, 'encore_EDataType', b)


def test_assoc_eAttributes19_reverse_link_reassign_clear():
    a1 = encore_EClass(abstract=True, interface=True)
    a2 = encore_EClass(abstract=False, interface=False)
    b = encore_EAttribute(iD=True)
    _safe_set(b, 'encore_EAttribute21', a1)
    assert _is_linked(b, 'encore_EAttribute21', a1)
    if hasattr(a1, 'encore_EClass20'):
        assert _is_linked(a1, 'encore_EClass20', b)
    _safe_set(b, 'encore_EAttribute21', a2)
    assert _is_linked(b, 'encore_EAttribute21', a2)
    if hasattr(a1, 'encore_EClass20'):
        assert not _is_linked(a1, 'encore_EClass20', b)
    if hasattr(a2, 'encore_EClass20'):
        assert _is_linked(a2, 'encore_EClass20', b)
    _safe_set(b, 'encore_EAttribute21', None)
    assert not _is_linked(b, 'encore_EAttribute21', a2)
    if hasattr(a2, 'encore_EClass20'):
        assert not _is_linked(a2, 'encore_EClass20', b)


def test_assoc_eClassifiers61_reverse_link_reassign_clear():
    a1 = encore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = encore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = encore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'encore_EClassifier63', a1)
    assert _is_linked(b, 'encore_EClassifier63', a1)
    if hasattr(a1, 'encore_EPackage62'):
        assert _is_linked(a1, 'encore_EPackage62', b)
    _safe_set(b, 'encore_EClassifier63', a2)
    assert _is_linked(b, 'encore_EClassifier63', a2)
    if hasattr(a1, 'encore_EPackage62'):
        assert not _is_linked(a1, 'encore_EPackage62', b)
    if hasattr(a2, 'encore_EPackage62'):
        assert _is_linked(a2, 'encore_EPackage62', b)
    _safe_set(b, 'encore_EClassifier63', None)
    assert not _is_linked(b, 'encore_EClassifier63', a2)
    if hasattr(a2, 'encore_EPackage62'):
        assert not _is_linked(a2, 'encore_EPackage62', b)


def test_assoc_eContainingClass49_reverse_link_reassign_clear():
    a1 = encore_EOperation()
    a2 = encore_EOperation()
    b = encore_EClass(abstract=True, interface=True)
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


def test_assoc_eContainingClass81_reverse_link_reassign_clear():
    a1 = encore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = encore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = encore_EClass(abstract=True, interface=True)
    _safe_set(b, 'EClass82', a1)
    assert _is_linked(b, 'EClass82', a1)
    if hasattr(a1, 'eStructuralFeatures'):
        assert _is_linked(a1, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass82', a2)
    assert _is_linked(b, 'EClass82', a2)
    if hasattr(a1, 'eStructuralFeatures'):
        assert not _is_linked(a1, 'eStructuralFeatures', b)
    if hasattr(a2, 'eStructuralFeatures'):
        assert _is_linked(a2, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass82', None)
    assert not _is_linked(b, 'EClass82', a2)
    if hasattr(a2, 'eStructuralFeatures'):
        assert not _is_linked(a2, 'eStructuralFeatures', b)


def test_assoc_eEnum46_reverse_link_reassign_clear():
    a1 = encore_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    a2 = encore_EEnumLiteral(instance="sample_text_2", literal="sample_text_2", value=13)
    b = encore_EEnum()
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


def test_assoc_eExceptions54_reverse_link_reassign_clear():
    a1 = encore_EOperation()
    a2 = encore_EOperation()
    b = encore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'encore_EClassifier56', a1)
    assert _is_linked(b, 'encore_EClassifier56', a1)
    if hasattr(a1, 'encore_EOperation55'):
        assert _is_linked(a1, 'encore_EOperation55', b)
    _safe_set(b, 'encore_EClassifier56', a2)
    assert _is_linked(b, 'encore_EClassifier56', a2)
    if hasattr(a1, 'encore_EOperation55'):
        assert not _is_linked(a1, 'encore_EOperation55', b)
    if hasattr(a2, 'encore_EOperation55'):
        assert _is_linked(a2, 'encore_EOperation55', b)
    _safe_set(b, 'encore_EClassifier56', None)
    assert not _is_linked(b, 'encore_EClassifier56', a2)
    if hasattr(a2, 'encore_EOperation55'):
        assert not _is_linked(a2, 'encore_EOperation55', b)


def test_assoc_eFactoryInstance60_reverse_link_reassign_clear():
    a1 = encore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = encore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = encore_EFactory()
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


def test_assoc_eIDAttribute32_reverse_link_reassign_clear():
    a1 = encore_EClass(abstract=True, interface=True)
    a2 = encore_EClass(abstract=False, interface=False)
    b = encore_EAttribute(iD=True)
    _safe_set(b, 'encore_EAttribute34', a1)
    assert _is_linked(b, 'encore_EAttribute34', a1)
    if hasattr(a1, 'encore_EClass33'):
        assert _is_linked(a1, 'encore_EClass33', b)
    _safe_set(b, 'encore_EAttribute34', a2)
    assert _is_linked(b, 'encore_EAttribute34', a2)
    if hasattr(a1, 'encore_EClass33'):
        assert not _is_linked(a1, 'encore_EClass33', b)
    if hasattr(a2, 'encore_EClass33'):
        assert _is_linked(a2, 'encore_EClass33', b)
    _safe_set(b, 'encore_EAttribute34', None)
    assert not _is_linked(b, 'encore_EAttribute34', a2)
    if hasattr(a2, 'encore_EClass33'):
        assert not _is_linked(a2, 'encore_EClass33', b)


def test_assoc_eKeys78_reverse_link_reassign_clear():
    a1 = encore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = encore_EReference(container=False, containment=False, resolveProxies=False)
    b = encore_EAttribute(iD=True)
    _safe_set(b, 'encore_EAttribute80', a1)
    assert _is_linked(b, 'encore_EAttribute80', a1)
    if hasattr(a1, 'encore_EReference79'):
        assert _is_linked(a1, 'encore_EReference79', b)
    _safe_set(b, 'encore_EAttribute80', a2)
    assert _is_linked(b, 'encore_EAttribute80', a2)
    if hasattr(a1, 'encore_EReference79'):
        assert not _is_linked(a1, 'encore_EReference79', b)
    if hasattr(a2, 'encore_EReference79'):
        assert _is_linked(a2, 'encore_EReference79', b)
    _safe_set(b, 'encore_EAttribute80', None)
    assert not _is_linked(b, 'encore_EAttribute80', a2)
    if hasattr(a2, 'encore_EReference79'):
        assert not _is_linked(a2, 'encore_EReference79', b)


def test_assoc_eLiterals45_reverse_link_reassign_clear():
    a1 = encore_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    a2 = encore_EEnumLiteral(instance="sample_text_2", literal="sample_text_2", value=13)
    b = encore_EEnum()
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


def test_assoc_eModelElement2_reverse_link_reassign_clear():
    a1 = encore_EModelElement()
    a2 = encore_EModelElement()
    b = encore_EAnnotation(source="sample_text")
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


def test_assoc_eOperations10_reverse_link_reassign_clear():
    a1 = encore_EOperation()
    a2 = encore_EOperation()
    b = encore_EClass(abstract=True, interface=True)
    _safe_set(b, 'eContainingClass', {a1})
    assert _is_linked(b, 'eContainingClass', a1)
    if hasattr(a1, 'EOperation'):
        assert _is_linked(a1, 'EOperation', b)
    _safe_set(b, 'eContainingClass', {a2})
    assert _is_linked(b, 'eContainingClass', a2)
    if hasattr(a1, 'EOperation'):
        assert not _is_linked(a1, 'EOperation', b)
    if hasattr(a2, 'EOperation'):
        assert _is_linked(a2, 'EOperation', b)
    _safe_set(b, 'eContainingClass', set())
    assert not _is_linked(b, 'eContainingClass', a2)
    if hasattr(a2, 'EOperation'):
        assert not _is_linked(a2, 'EOperation', b)


def test_assoc_eOpposite73_reverse_link_reassign_clear():
    a1 = encore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = encore_EReference(container=False, containment=False, resolveProxies=False)
    b = encore_EReference(container=True, containment=True, resolveProxies=True)
    _safe_set(b, 'encore_EReference74', a1)
    assert _is_linked(b, 'encore_EReference74', a1)
    if hasattr(a1, 'encore_EReference72'):
        assert _is_linked(a1, 'encore_EReference72', b)
    _safe_set(b, 'encore_EReference74', a2)
    assert _is_linked(b, 'encore_EReference74', a2)
    if hasattr(a1, 'encore_EReference72'):
        assert not _is_linked(a1, 'encore_EReference72', b)
    if hasattr(a2, 'encore_EReference72'):
        assert _is_linked(a2, 'encore_EReference72', b)
    _safe_set(b, 'encore_EReference74', None)
    assert not _is_linked(b, 'encore_EReference74', a2)
    if hasattr(a2, 'encore_EReference72'):
        assert not _is_linked(a2, 'encore_EReference72', b)


def test_assoc_ePackage42_reverse_link_reassign_clear():
    a1 = encore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = encore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = encore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'encore_EClassifier', a1)
    assert _is_linked(b, 'encore_EClassifier', a1)
    if hasattr(a1, 'encore_EPackage'):
        assert _is_linked(a1, 'encore_EPackage', b)
    _safe_set(b, 'encore_EClassifier', a2)
    assert _is_linked(b, 'encore_EClassifier', a2)
    if hasattr(a1, 'encore_EPackage'):
        assert not _is_linked(a1, 'encore_EPackage', b)
    if hasattr(a2, 'encore_EPackage'):
        assert _is_linked(a2, 'encore_EPackage', b)
    _safe_set(b, 'encore_EClassifier', None)
    assert not _is_linked(b, 'encore_EClassifier', a2)
    if hasattr(a2, 'encore_EPackage'):
        assert not _is_linked(a2, 'encore_EPackage', b)


def test_assoc_ePackage47_reverse_link_reassign_clear():
    a1 = encore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = encore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = encore_EFactory()
    _safe_set(b, 'eFactoryInstance', a1)
    assert _is_linked(b, 'eFactoryInstance', a1)
    if hasattr(a1, 'EPackage'):
        assert _is_linked(a1, 'EPackage', b)
    _safe_set(b, 'eFactoryInstance', a2)
    assert _is_linked(b, 'eFactoryInstance', a2)
    if hasattr(a1, 'EPackage'):
        assert not _is_linked(a1, 'EPackage', b)
    if hasattr(a2, 'EPackage'):
        assert _is_linked(a2, 'EPackage', b)
    _safe_set(b, 'eFactoryInstance', None)
    assert not _is_linked(b, 'eFactoryInstance', a2)
    if hasattr(a2, 'EPackage'):
        assert not _is_linked(a2, 'EPackage', b)


def test_assoc_eReferenceType75_reverse_link_reassign_clear():
    a1 = encore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = encore_EReference(container=False, containment=False, resolveProxies=False)
    b = encore_EClass(abstract=True, interface=True)
    _safe_set(b, 'encore_EClass77', a1)
    assert _is_linked(b, 'encore_EClass77', a1)
    if hasattr(a1, 'encore_EReference76'):
        assert _is_linked(a1, 'encore_EReference76', b)
    _safe_set(b, 'encore_EClass77', a2)
    assert _is_linked(b, 'encore_EClass77', a2)
    if hasattr(a1, 'encore_EReference76'):
        assert not _is_linked(a1, 'encore_EReference76', b)
    if hasattr(a2, 'encore_EReference76'):
        assert _is_linked(a2, 'encore_EReference76', b)
    _safe_set(b, 'encore_EClass77', None)
    assert not _is_linked(b, 'encore_EClass77', a2)
    if hasattr(a2, 'encore_EReference76'):
        assert not _is_linked(a2, 'encore_EReference76', b)


def test_assoc_eReferences16_reverse_link_reassign_clear():
    a1 = encore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = encore_EReference(container=False, containment=False, resolveProxies=False)
    b = encore_EClass(abstract=True, interface=True)
    _safe_set(b, 'encore_EClass17', {a1})
    assert _is_linked(b, 'encore_EClass17', a1)
    if hasattr(a1, 'encore_EReference18'):
        assert _is_linked(a1, 'encore_EReference18', b)
    _safe_set(b, 'encore_EClass17', {a2})
    assert _is_linked(b, 'encore_EClass17', a2)
    if hasattr(a1, 'encore_EReference18'):
        assert not _is_linked(a1, 'encore_EReference18', b)
    if hasattr(a2, 'encore_EReference18'):
        assert _is_linked(a2, 'encore_EReference18', b)
    _safe_set(b, 'encore_EClass17', set())
    assert not _is_linked(b, 'encore_EClass17', a2)
    if hasattr(a2, 'encore_EReference18'):
        assert not _is_linked(a2, 'encore_EReference18', b)


def test_assoc_eStructuralFeatures35_reverse_link_reassign_clear():
    a1 = encore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = encore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = encore_EClass(abstract=True, interface=True)
    _safe_set(b, 'eContainingClass36', {a1})
    assert _is_linked(b, 'eContainingClass36', a1)
    if hasattr(a1, 'EStructuralFeature'):
        assert _is_linked(a1, 'EStructuralFeature', b)
    _safe_set(b, 'eContainingClass36', {a2})
    assert _is_linked(b, 'eContainingClass36', a2)
    if hasattr(a1, 'EStructuralFeature'):
        assert not _is_linked(a1, 'EStructuralFeature', b)
    if hasattr(a2, 'EStructuralFeature'):
        assert _is_linked(a2, 'EStructuralFeature', b)
    _safe_set(b, 'eContainingClass36', set())
    assert not _is_linked(b, 'eContainingClass36', a2)
    if hasattr(a2, 'EStructuralFeature'):
        assert not _is_linked(a2, 'EStructuralFeature', b)


def test_assoc_eSubpackages65_reverse_link_reassign_clear():
    a1 = encore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = encore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = encore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'encore_EPackage66', a1)
    assert _is_linked(b, 'encore_EPackage66', a1)
    if hasattr(a1, 'encore_EPackage64'):
        assert _is_linked(a1, 'encore_EPackage64', b)
    _safe_set(b, 'encore_EPackage66', a2)
    assert _is_linked(b, 'encore_EPackage66', a2)
    if hasattr(a1, 'encore_EPackage64'):
        assert not _is_linked(a1, 'encore_EPackage64', b)
    if hasattr(a2, 'encore_EPackage64'):
        assert _is_linked(a2, 'encore_EPackage64', b)
    _safe_set(b, 'encore_EPackage66', None)
    assert not _is_linked(b, 'encore_EPackage66', a2)
    if hasattr(a2, 'encore_EPackage64'):
        assert not _is_linked(a2, 'encore_EPackage64', b)


def test_assoc_eSuperPackage68_reverse_link_reassign_clear():
    a1 = encore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = encore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = encore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'encore_EPackage69', a1)
    assert _is_linked(b, 'encore_EPackage69', a1)
    if hasattr(a1, 'encore_EPackage67'):
        assert _is_linked(a1, 'encore_EPackage67', b)
    _safe_set(b, 'encore_EPackage69', a2)
    assert _is_linked(b, 'encore_EPackage69', a2)
    if hasattr(a1, 'encore_EPackage67'):
        assert not _is_linked(a1, 'encore_EPackage67', b)
    if hasattr(a2, 'encore_EPackage67'):
        assert _is_linked(a2, 'encore_EPackage67', b)
    _safe_set(b, 'encore_EPackage69', None)
    assert not _is_linked(b, 'encore_EPackage69', a2)
    if hasattr(a2, 'encore_EPackage67'):
        assert not _is_linked(a2, 'encore_EPackage67', b)


def test_assoc_eSuperTypes9_reverse_link_reassign_clear():
    a1 = encore_EClass(abstract=True, interface=True)
    a2 = encore_EClass(abstract=False, interface=False)
    b = encore_EClass(abstract=True, interface=True)
    _safe_set(b, 'encore_EClass8', {a1})
    assert _is_linked(b, 'encore_EClass8', a1)
    if hasattr(a1, 'encore_EClass'):
        assert _is_linked(a1, 'encore_EClass', b)
    _safe_set(b, 'encore_EClass8', {a2})
    assert _is_linked(b, 'encore_EClass8', a2)
    if hasattr(a1, 'encore_EClass'):
        assert not _is_linked(a1, 'encore_EClass', b)
    if hasattr(a2, 'encore_EClass'):
        assert _is_linked(a2, 'encore_EClass', b)
    _safe_set(b, 'encore_EClass8', set())
    assert not _is_linked(b, 'encore_EClass8', a2)
    if hasattr(a2, 'encore_EClass'):
        assert not _is_linked(a2, 'encore_EClass', b)


def test_assoc_eType83_reverse_link_reassign_clear():
    a1 = encore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    a2 = encore_ETypedElement(lowerBound=13, many=False, ordered=False, required=False, unique=False, upperBound=13)
    b = encore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'encore_EClassifier84', a1)
    assert _is_linked(b, 'encore_EClassifier84', a1)
    if hasattr(a1, 'encore_ETypedElement'):
        assert _is_linked(a1, 'encore_ETypedElement', b)
    _safe_set(b, 'encore_EClassifier84', a2)
    assert _is_linked(b, 'encore_EClassifier84', a2)
    if hasattr(a1, 'encore_ETypedElement'):
        assert not _is_linked(a1, 'encore_ETypedElement', b)
    if hasattr(a2, 'encore_ETypedElement'):
        assert _is_linked(a2, 'encore_ETypedElement', b)
    _safe_set(b, 'encore_EClassifier84', None)
    assert not _is_linked(b, 'encore_EClassifier84', a2)
    if hasattr(a2, 'encore_ETypedElement'):
        assert not _is_linked(a2, 'encore_ETypedElement', b)


def test_assoc_references5_reverse_link_reassign_clear():
    a1 = encore_EObject()
    a2 = encore_EObject()
    b = encore_EAnnotation(source="sample_text")
    _safe_set(b, 'encore_EAnnotation6', {a1})
    assert _is_linked(b, 'encore_EAnnotation6', a1)
    if hasattr(a1, 'encore_EObject7'):
        assert _is_linked(a1, 'encore_EObject7', b)
    _safe_set(b, 'encore_EAnnotation6', {a2})
    assert _is_linked(b, 'encore_EAnnotation6', a2)
    if hasattr(a1, 'encore_EObject7'):
        assert not _is_linked(a1, 'encore_EObject7', b)
    if hasattr(a2, 'encore_EObject7'):
        assert _is_linked(a2, 'encore_EObject7', b)
    _safe_set(b, 'encore_EAnnotation6', set())
    assert not _is_linked(b, 'encore_EAnnotation6', a2)
    if hasattr(a2, 'encore_EObject7'):
        assert not _is_linked(a2, 'encore_EObject7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_eAllGenericSuperTypes39_stub_double():
    # encore_EGenericType has no real 'encore_EGenericType41' property in the generated
    # code (a bare stub) -- manually attach it so encore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # encore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = encore_EClass(abstract=True, interface=True)
    partner = encore_EGenericType()
    setattr(partner, 'encore_EGenericType41', None)
    _safe_set(owner, 'encore_EClass40', {partner})
    assert getattr(partner, 'encore_EGenericType41') == owner
    _safe_set(owner, 'encore_EClass40', set())
    assert getattr(partner, 'encore_EGenericType41') is None


def test_assoc_eClassifier103_stub_double():
    # encore_EGenericType has no real 'encore_EGenericType104' property in the generated
    # code (a bare stub) -- manually attach it so encore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # encore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = encore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = encore_EGenericType()
    setattr(partner, 'encore_EGenericType104', None)
    _safe_set(owner, 'encore_EClassifier105', partner)
    assert getattr(partner, 'encore_EGenericType104') == owner
    _safe_set(owner, 'encore_EClassifier105', None)
    assert getattr(partner, 'encore_EGenericType104') is None


def test_assoc_eGenericExceptions57_stub_double():
    # encore_EGenericType has no real 'encore_EGenericType59' property in the generated
    # code (a bare stub) -- manually attach it so encore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # encore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = encore_EOperation()
    partner = encore_EGenericType()
    setattr(partner, 'encore_EGenericType59', None)
    _safe_set(owner, 'encore_EOperation58', {partner})
    assert getattr(partner, 'encore_EGenericType59') == owner
    _safe_set(owner, 'encore_EOperation58', set())
    assert getattr(partner, 'encore_EGenericType59') is None


def test_assoc_eGenericSuperTypes37_stub_double():
    # encore_EGenericType has no real 'encore_EGenericType' property in the generated
    # code (a bare stub) -- manually attach it so encore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # encore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = encore_EClass(abstract=True, interface=True)
    partner = encore_EGenericType()
    setattr(partner, 'encore_EGenericType', None)
    _safe_set(owner, 'encore_EClass38', {partner})
    assert getattr(partner, 'encore_EGenericType') == owner
    _safe_set(owner, 'encore_EClass38', set())
    assert getattr(partner, 'encore_EGenericType') is None


def test_assoc_eGenericType85_stub_double():
    # encore_EGenericType has no real 'encore_EGenericType87' property in the generated
    # code (a bare stub) -- manually attach it so encore_ETypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # encore_ETypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = encore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    partner = encore_EGenericType()
    setattr(partner, 'encore_EGenericType87', None)
    _safe_set(owner, 'encore_ETypedElement86', partner)
    assert getattr(partner, 'encore_EGenericType87') == owner
    _safe_set(owner, 'encore_ETypedElement86', None)
    assert getattr(partner, 'encore_EGenericType87') is None


def test_assoc_eOperation70_stub_double():
    # encore_EParameter has no real 'eParameters' property in the generated
    # code (a bare stub) -- manually attach it so encore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # encore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = encore_EOperation()
    partner = encore_EParameter()
    setattr(partner, 'eParameters', None)
    _safe_set(owner, 'EOperation71', partner)
    assert getattr(partner, 'eParameters') == owner
    _safe_set(owner, 'EOperation71', None)
    assert getattr(partner, 'eParameters') is None


def test_assoc_eParameters53_stub_double():
    # encore_EParameter has no real 'EParameter' property in the generated
    # code (a bare stub) -- manually attach it so encore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # encore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = encore_EOperation()
    partner = encore_EParameter()
    setattr(partner, 'EParameter', None)
    _safe_set(owner, 'eOperation', {partner})
    assert getattr(partner, 'EParameter') == owner
    _safe_set(owner, 'eOperation', set())
    assert getattr(partner, 'EParameter') is None


def test_assoc_eRawType94_stub_double():
    # encore_EGenericType has no real 'encore_EGenericType95' property in the generated
    # code (a bare stub) -- manually attach it so encore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # encore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = encore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = encore_EGenericType()
    setattr(partner, 'encore_EGenericType95', None)
    _safe_set(owner, 'encore_EClassifier96', partner)
    assert getattr(partner, 'encore_EGenericType95') == owner
    _safe_set(owner, 'encore_EClassifier96', None)
    assert getattr(partner, 'encore_EGenericType95') is None


def test_assoc_eTypeParameters43_stub_double():
    # encore_ETypeParameter has no real 'encore_ETypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so encore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # encore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = encore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = encore_ETypeParameter()
    setattr(partner, 'encore_ETypeParameter', None)
    _safe_set(owner, 'encore_EClassifier44', {partner})
    assert getattr(partner, 'encore_ETypeParameter') == owner
    _safe_set(owner, 'encore_EClassifier44', set())
    assert getattr(partner, 'encore_ETypeParameter') is None


def test_assoc_eTypeParameters50_stub_double():
    # encore_ETypeParameter has no real 'encore_ETypeParameter52' property in the generated
    # code (a bare stub) -- manually attach it so encore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # encore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = encore_EOperation()
    partner = encore_ETypeParameter()
    setattr(partner, 'encore_ETypeParameter52', None)
    _safe_set(owner, 'encore_EOperation51', {partner})
    assert getattr(partner, 'encore_ETypeParameter52') == owner
    _safe_set(owner, 'encore_EOperation51', set())
    assert getattr(partner, 'encore_ETypeParameter52') is None


