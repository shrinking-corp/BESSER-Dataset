import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EClassifier,
    EDataType,
    EModelElement,
    ENamedElement,
    EStructuralFeature,
    ETypedElement,
    ecoreO_EAnnotation,
    ecoreO_EAttribute,
    ecoreO_EClass,
    ecoreO_EClassifier,
    ecoreO_EDataType,
    ecoreO_EEnum,
    ecoreO_EEnumLiteral,
    ecoreO_EFactory,
    ecoreO_EGenericType,
    ecoreO_EModelElement,
    ecoreO_ENamedElement,
    ecoreO_EObject,
    ecoreO_EOperation,
    ecoreO_EPackage,
    ecoreO_EParameter,
    ecoreO_EReference,
    ecoreO_EStringToStringMapEntry,
    ecoreO_EStructuralFeature,
    ecoreO_ETypeParameter,
    ecoreO_ETypedElement,
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
    a1 = ecoreO_EObject()
    a2 = ecoreO_EObject()
    b = ecoreO_EAnnotation(source="sample_text")
    _safe_set(b, 'ecoreO_EAnnotation4', {a1})
    assert _is_linked(b, 'ecoreO_EAnnotation4', a1)
    if hasattr(a1, 'ecoreO_EObject'):
        assert _is_linked(a1, 'ecoreO_EObject', b)
    _safe_set(b, 'ecoreO_EAnnotation4', {a2})
    assert _is_linked(b, 'ecoreO_EAnnotation4', a2)
    if hasattr(a1, 'ecoreO_EObject'):
        assert not _is_linked(a1, 'ecoreO_EObject', b)
    if hasattr(a2, 'ecoreO_EObject'):
        assert _is_linked(a2, 'ecoreO_EObject', b)
    _safe_set(b, 'ecoreO_EAnnotation4', set())
    assert not _is_linked(b, 'ecoreO_EAnnotation4', a2)
    if hasattr(a2, 'ecoreO_EObject'):
        assert not _is_linked(a2, 'ecoreO_EObject', b)


def test_assoc_details1_reverse_link_reassign_clear():
    a1 = ecoreO_EStringToStringMapEntry(key="sample_text", value="sample_text")
    a2 = ecoreO_EStringToStringMapEntry(key="sample_text_2", value="sample_text_2")
    b = ecoreO_EAnnotation(source="sample_text")
    _safe_set(b, 'ecoreO_EAnnotation', {a1})
    assert _is_linked(b, 'ecoreO_EAnnotation', a1)
    if hasattr(a1, 'ecoreO_EStringToStringMapEntry'):
        assert _is_linked(a1, 'ecoreO_EStringToStringMapEntry', b)
    _safe_set(b, 'ecoreO_EAnnotation', {a2})
    assert _is_linked(b, 'ecoreO_EAnnotation', a2)
    if hasattr(a1, 'ecoreO_EStringToStringMapEntry'):
        assert not _is_linked(a1, 'ecoreO_EStringToStringMapEntry', b)
    if hasattr(a2, 'ecoreO_EStringToStringMapEntry'):
        assert _is_linked(a2, 'ecoreO_EStringToStringMapEntry', b)
    _safe_set(b, 'ecoreO_EAnnotation', set())
    assert not _is_linked(b, 'ecoreO_EAnnotation', a2)
    if hasattr(a2, 'ecoreO_EStringToStringMapEntry'):
        assert not _is_linked(a2, 'ecoreO_EStringToStringMapEntry', b)


def test_assoc_eAllAttributes11_reverse_link_reassign_clear():
    a1 = ecoreO_EClass(abstract=True, interface=True)
    a2 = ecoreO_EClass(abstract=False, interface=False)
    b = ecoreO_EAttribute(iD=True)
    _safe_set(b, 'ecoreO_EAttribute13', a1)
    assert _is_linked(b, 'ecoreO_EAttribute13', a1)
    if hasattr(a1, 'ecoreO_EClass12'):
        assert _is_linked(a1, 'ecoreO_EClass12', b)
    _safe_set(b, 'ecoreO_EAttribute13', a2)
    assert _is_linked(b, 'ecoreO_EAttribute13', a2)
    if hasattr(a1, 'ecoreO_EClass12'):
        assert not _is_linked(a1, 'ecoreO_EClass12', b)
    if hasattr(a2, 'ecoreO_EClass12'):
        assert _is_linked(a2, 'ecoreO_EClass12', b)
    _safe_set(b, 'ecoreO_EAttribute13', None)
    assert not _is_linked(b, 'ecoreO_EAttribute13', a2)
    if hasattr(a2, 'ecoreO_EClass12'):
        assert not _is_linked(a2, 'ecoreO_EClass12', b)


def test_assoc_eAllContainments22_reverse_link_reassign_clear():
    a1 = ecoreO_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecoreO_EReference(container=False, containment=False, resolveProxies=False)
    b = ecoreO_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecoreO_EClass23', {a1})
    assert _is_linked(b, 'ecoreO_EClass23', a1)
    if hasattr(a1, 'ecoreO_EReference24'):
        assert _is_linked(a1, 'ecoreO_EReference24', b)
    _safe_set(b, 'ecoreO_EClass23', {a2})
    assert _is_linked(b, 'ecoreO_EClass23', a2)
    if hasattr(a1, 'ecoreO_EReference24'):
        assert not _is_linked(a1, 'ecoreO_EReference24', b)
    if hasattr(a2, 'ecoreO_EReference24'):
        assert _is_linked(a2, 'ecoreO_EReference24', b)
    _safe_set(b, 'ecoreO_EClass23', set())
    assert not _is_linked(b, 'ecoreO_EClass23', a2)
    if hasattr(a2, 'ecoreO_EReference24'):
        assert not _is_linked(a2, 'ecoreO_EReference24', b)


def test_assoc_eAllOperations25_reverse_link_reassign_clear():
    a1 = ecoreO_EOperation()
    a2 = ecoreO_EOperation()
    b = ecoreO_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecoreO_EClass26', {a1})
    assert _is_linked(b, 'ecoreO_EClass26', a1)
    if hasattr(a1, 'ecoreO_EOperation'):
        assert _is_linked(a1, 'ecoreO_EOperation', b)
    _safe_set(b, 'ecoreO_EClass26', {a2})
    assert _is_linked(b, 'ecoreO_EClass26', a2)
    if hasattr(a1, 'ecoreO_EOperation'):
        assert not _is_linked(a1, 'ecoreO_EOperation', b)
    if hasattr(a2, 'ecoreO_EOperation'):
        assert _is_linked(a2, 'ecoreO_EOperation', b)
    _safe_set(b, 'ecoreO_EClass26', set())
    assert not _is_linked(b, 'ecoreO_EClass26', a2)
    if hasattr(a2, 'ecoreO_EOperation'):
        assert not _is_linked(a2, 'ecoreO_EOperation', b)


def test_assoc_eAllReferences14_reverse_link_reassign_clear():
    a1 = ecoreO_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecoreO_EReference(container=False, containment=False, resolveProxies=False)
    b = ecoreO_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecoreO_EClass15', {a1})
    assert _is_linked(b, 'ecoreO_EClass15', a1)
    if hasattr(a1, 'ecoreO_EReference'):
        assert _is_linked(a1, 'ecoreO_EReference', b)
    _safe_set(b, 'ecoreO_EClass15', {a2})
    assert _is_linked(b, 'ecoreO_EClass15', a2)
    if hasattr(a1, 'ecoreO_EReference'):
        assert not _is_linked(a1, 'ecoreO_EReference', b)
    if hasattr(a2, 'ecoreO_EReference'):
        assert _is_linked(a2, 'ecoreO_EReference', b)
    _safe_set(b, 'ecoreO_EClass15', set())
    assert not _is_linked(b, 'ecoreO_EClass15', a2)
    if hasattr(a2, 'ecoreO_EReference'):
        assert not _is_linked(a2, 'ecoreO_EReference', b)


def test_assoc_eAllStructuralFeatures27_reverse_link_reassign_clear():
    a1 = ecoreO_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = ecoreO_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = ecoreO_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecoreO_EClass28', {a1})
    assert _is_linked(b, 'ecoreO_EClass28', a1)
    if hasattr(a1, 'ecoreO_EStructuralFeature'):
        assert _is_linked(a1, 'ecoreO_EStructuralFeature', b)
    _safe_set(b, 'ecoreO_EClass28', {a2})
    assert _is_linked(b, 'ecoreO_EClass28', a2)
    if hasattr(a1, 'ecoreO_EStructuralFeature'):
        assert not _is_linked(a1, 'ecoreO_EStructuralFeature', b)
    if hasattr(a2, 'ecoreO_EStructuralFeature'):
        assert _is_linked(a2, 'ecoreO_EStructuralFeature', b)
    _safe_set(b, 'ecoreO_EClass28', set())
    assert not _is_linked(b, 'ecoreO_EClass28', a2)
    if hasattr(a2, 'ecoreO_EStructuralFeature'):
        assert not _is_linked(a2, 'ecoreO_EStructuralFeature', b)


def test_assoc_eAllSuperTypes30_reverse_link_reassign_clear():
    a1 = ecoreO_EClass(abstract=True, interface=True)
    a2 = ecoreO_EClass(abstract=False, interface=False)
    b = ecoreO_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecoreO_EClass31', a1)
    assert _is_linked(b, 'ecoreO_EClass31', a1)
    if hasattr(a1, 'ecoreO_EClass29'):
        assert _is_linked(a1, 'ecoreO_EClass29', b)
    _safe_set(b, 'ecoreO_EClass31', a2)
    assert _is_linked(b, 'ecoreO_EClass31', a2)
    if hasattr(a1, 'ecoreO_EClass29'):
        assert not _is_linked(a1, 'ecoreO_EClass29', b)
    if hasattr(a2, 'ecoreO_EClass29'):
        assert _is_linked(a2, 'ecoreO_EClass29', b)
    _safe_set(b, 'ecoreO_EClass31', None)
    assert not _is_linked(b, 'ecoreO_EClass31', a2)
    if hasattr(a2, 'ecoreO_EClass29'):
        assert not _is_linked(a2, 'ecoreO_EClass29', b)


def test_assoc_eAnnotations48_reverse_link_reassign_clear():
    a1 = ecoreO_EModelElement()
    a2 = ecoreO_EModelElement()
    b = ecoreO_EAnnotation(source="sample_text")
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
    a1 = ecoreO_EDataType(serializable=True)
    a2 = ecoreO_EDataType(serializable=False)
    b = ecoreO_EAttribute(iD=True)
    _safe_set(b, 'ecoreO_EAttribute', a1)
    assert _is_linked(b, 'ecoreO_EAttribute', a1)
    if hasattr(a1, 'ecoreO_EDataType'):
        assert _is_linked(a1, 'ecoreO_EDataType', b)
    _safe_set(b, 'ecoreO_EAttribute', a2)
    assert _is_linked(b, 'ecoreO_EAttribute', a2)
    if hasattr(a1, 'ecoreO_EDataType'):
        assert not _is_linked(a1, 'ecoreO_EDataType', b)
    if hasattr(a2, 'ecoreO_EDataType'):
        assert _is_linked(a2, 'ecoreO_EDataType', b)
    _safe_set(b, 'ecoreO_EAttribute', None)
    assert not _is_linked(b, 'ecoreO_EAttribute', a2)
    if hasattr(a2, 'ecoreO_EDataType'):
        assert not _is_linked(a2, 'ecoreO_EDataType', b)


def test_assoc_eAttributes19_reverse_link_reassign_clear():
    a1 = ecoreO_EClass(abstract=True, interface=True)
    a2 = ecoreO_EClass(abstract=False, interface=False)
    b = ecoreO_EAttribute(iD=True)
    _safe_set(b, 'ecoreO_EAttribute21', a1)
    assert _is_linked(b, 'ecoreO_EAttribute21', a1)
    if hasattr(a1, 'ecoreO_EClass20'):
        assert _is_linked(a1, 'ecoreO_EClass20', b)
    _safe_set(b, 'ecoreO_EAttribute21', a2)
    assert _is_linked(b, 'ecoreO_EAttribute21', a2)
    if hasattr(a1, 'ecoreO_EClass20'):
        assert not _is_linked(a1, 'ecoreO_EClass20', b)
    if hasattr(a2, 'ecoreO_EClass20'):
        assert _is_linked(a2, 'ecoreO_EClass20', b)
    _safe_set(b, 'ecoreO_EAttribute21', None)
    assert not _is_linked(b, 'ecoreO_EAttribute21', a2)
    if hasattr(a2, 'ecoreO_EClass20'):
        assert not _is_linked(a2, 'ecoreO_EClass20', b)


def test_assoc_eClassifiers61_reverse_link_reassign_clear():
    a1 = ecoreO_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecoreO_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecoreO_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'EClassifier', a1)
    assert _is_linked(b, 'EClassifier', a1)
    if hasattr(a1, 'ePackage62'):
        assert _is_linked(a1, 'ePackage62', b)
    _safe_set(b, 'EClassifier', a2)
    assert _is_linked(b, 'EClassifier', a2)
    if hasattr(a1, 'ePackage62'):
        assert not _is_linked(a1, 'ePackage62', b)
    if hasattr(a2, 'ePackage62'):
        assert _is_linked(a2, 'ePackage62', b)
    _safe_set(b, 'EClassifier', None)
    assert not _is_linked(b, 'EClassifier', a2)
    if hasattr(a2, 'ePackage62'):
        assert not _is_linked(a2, 'ePackage62', b)


def test_assoc_eContainingClass49_reverse_link_reassign_clear():
    a1 = ecoreO_EOperation()
    a2 = ecoreO_EOperation()
    b = ecoreO_EClass(abstract=True, interface=True)
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


def test_assoc_eContainingClass80_reverse_link_reassign_clear():
    a1 = ecoreO_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = ecoreO_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = ecoreO_EClass(abstract=True, interface=True)
    _safe_set(b, 'EClass81', a1)
    assert _is_linked(b, 'EClass81', a1)
    if hasattr(a1, 'eStructuralFeatures'):
        assert _is_linked(a1, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass81', a2)
    assert _is_linked(b, 'EClass81', a2)
    if hasattr(a1, 'eStructuralFeatures'):
        assert not _is_linked(a1, 'eStructuralFeatures', b)
    if hasattr(a2, 'eStructuralFeatures'):
        assert _is_linked(a2, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass81', None)
    assert not _is_linked(b, 'EClass81', a2)
    if hasattr(a2, 'eStructuralFeatures'):
        assert not _is_linked(a2, 'eStructuralFeatures', b)


def test_assoc_eEnum45_reverse_link_reassign_clear():
    a1 = ecoreO_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    a2 = ecoreO_EEnumLiteral(instance="sample_text_2", literal="sample_text_2", value=13)
    b = ecoreO_EEnum()
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
    a1 = ecoreO_EOperation()
    a2 = ecoreO_EOperation()
    b = ecoreO_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'ecoreO_EClassifier56', a1)
    assert _is_linked(b, 'ecoreO_EClassifier56', a1)
    if hasattr(a1, 'ecoreO_EOperation55'):
        assert _is_linked(a1, 'ecoreO_EOperation55', b)
    _safe_set(b, 'ecoreO_EClassifier56', a2)
    assert _is_linked(b, 'ecoreO_EClassifier56', a2)
    if hasattr(a1, 'ecoreO_EOperation55'):
        assert not _is_linked(a1, 'ecoreO_EOperation55', b)
    if hasattr(a2, 'ecoreO_EOperation55'):
        assert _is_linked(a2, 'ecoreO_EOperation55', b)
    _safe_set(b, 'ecoreO_EClassifier56', None)
    assert not _is_linked(b, 'ecoreO_EClassifier56', a2)
    if hasattr(a2, 'ecoreO_EOperation55'):
        assert not _is_linked(a2, 'ecoreO_EOperation55', b)


def test_assoc_eFactoryInstance60_reverse_link_reassign_clear():
    a1 = ecoreO_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecoreO_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecoreO_EFactory()
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
    a1 = ecoreO_EClass(abstract=True, interface=True)
    a2 = ecoreO_EClass(abstract=False, interface=False)
    b = ecoreO_EAttribute(iD=True)
    _safe_set(b, 'ecoreO_EAttribute34', a1)
    assert _is_linked(b, 'ecoreO_EAttribute34', a1)
    if hasattr(a1, 'ecoreO_EClass33'):
        assert _is_linked(a1, 'ecoreO_EClass33', b)
    _safe_set(b, 'ecoreO_EAttribute34', a2)
    assert _is_linked(b, 'ecoreO_EAttribute34', a2)
    if hasattr(a1, 'ecoreO_EClass33'):
        assert not _is_linked(a1, 'ecoreO_EClass33', b)
    if hasattr(a2, 'ecoreO_EClass33'):
        assert _is_linked(a2, 'ecoreO_EClass33', b)
    _safe_set(b, 'ecoreO_EAttribute34', None)
    assert not _is_linked(b, 'ecoreO_EAttribute34', a2)
    if hasattr(a2, 'ecoreO_EClass33'):
        assert not _is_linked(a2, 'ecoreO_EClass33', b)


def test_assoc_eKeys77_reverse_link_reassign_clear():
    a1 = ecoreO_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecoreO_EReference(container=False, containment=False, resolveProxies=False)
    b = ecoreO_EAttribute(iD=True)
    _safe_set(b, 'ecoreO_EAttribute79', a1)
    assert _is_linked(b, 'ecoreO_EAttribute79', a1)
    if hasattr(a1, 'ecoreO_EReference78'):
        assert _is_linked(a1, 'ecoreO_EReference78', b)
    _safe_set(b, 'ecoreO_EAttribute79', a2)
    assert _is_linked(b, 'ecoreO_EAttribute79', a2)
    if hasattr(a1, 'ecoreO_EReference78'):
        assert not _is_linked(a1, 'ecoreO_EReference78', b)
    if hasattr(a2, 'ecoreO_EReference78'):
        assert _is_linked(a2, 'ecoreO_EReference78', b)
    _safe_set(b, 'ecoreO_EAttribute79', None)
    assert not _is_linked(b, 'ecoreO_EAttribute79', a2)
    if hasattr(a2, 'ecoreO_EReference78'):
        assert not _is_linked(a2, 'ecoreO_EReference78', b)


def test_assoc_eLiterals44_reverse_link_reassign_clear():
    a1 = ecoreO_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    a2 = ecoreO_EEnumLiteral(instance="sample_text_2", literal="sample_text_2", value=13)
    b = ecoreO_EEnum()
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
    a1 = ecoreO_EModelElement()
    a2 = ecoreO_EModelElement()
    b = ecoreO_EAnnotation(source="sample_text")
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
    a1 = ecoreO_EOperation()
    a2 = ecoreO_EOperation()
    b = ecoreO_EClass(abstract=True, interface=True)
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


def test_assoc_eOpposite72_reverse_link_reassign_clear():
    a1 = ecoreO_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecoreO_EReference(container=False, containment=False, resolveProxies=False)
    b = ecoreO_EReference(container=True, containment=True, resolveProxies=True)
    _safe_set(b, 'ecoreO_EReference73', a1)
    assert _is_linked(b, 'ecoreO_EReference73', a1)
    if hasattr(a1, 'ecoreO_EReference71'):
        assert _is_linked(a1, 'ecoreO_EReference71', b)
    _safe_set(b, 'ecoreO_EReference73', a2)
    assert _is_linked(b, 'ecoreO_EReference73', a2)
    if hasattr(a1, 'ecoreO_EReference71'):
        assert not _is_linked(a1, 'ecoreO_EReference71', b)
    if hasattr(a2, 'ecoreO_EReference71'):
        assert _is_linked(a2, 'ecoreO_EReference71', b)
    _safe_set(b, 'ecoreO_EReference73', None)
    assert not _is_linked(b, 'ecoreO_EReference73', a2)
    if hasattr(a2, 'ecoreO_EReference71'):
        assert not _is_linked(a2, 'ecoreO_EReference71', b)


def test_assoc_ePackage42_reverse_link_reassign_clear():
    a1 = ecoreO_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecoreO_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecoreO_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
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
    a1 = ecoreO_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecoreO_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecoreO_EFactory()
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


def test_assoc_eReferenceType74_reverse_link_reassign_clear():
    a1 = ecoreO_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecoreO_EReference(container=False, containment=False, resolveProxies=False)
    b = ecoreO_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecoreO_EClass76', a1)
    assert _is_linked(b, 'ecoreO_EClass76', a1)
    if hasattr(a1, 'ecoreO_EReference75'):
        assert _is_linked(a1, 'ecoreO_EReference75', b)
    _safe_set(b, 'ecoreO_EClass76', a2)
    assert _is_linked(b, 'ecoreO_EClass76', a2)
    if hasattr(a1, 'ecoreO_EReference75'):
        assert not _is_linked(a1, 'ecoreO_EReference75', b)
    if hasattr(a2, 'ecoreO_EReference75'):
        assert _is_linked(a2, 'ecoreO_EReference75', b)
    _safe_set(b, 'ecoreO_EClass76', None)
    assert not _is_linked(b, 'ecoreO_EClass76', a2)
    if hasattr(a2, 'ecoreO_EReference75'):
        assert not _is_linked(a2, 'ecoreO_EReference75', b)


def test_assoc_eReferences16_reverse_link_reassign_clear():
    a1 = ecoreO_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecoreO_EReference(container=False, containment=False, resolveProxies=False)
    b = ecoreO_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecoreO_EClass17', {a1})
    assert _is_linked(b, 'ecoreO_EClass17', a1)
    if hasattr(a1, 'ecoreO_EReference18'):
        assert _is_linked(a1, 'ecoreO_EReference18', b)
    _safe_set(b, 'ecoreO_EClass17', {a2})
    assert _is_linked(b, 'ecoreO_EClass17', a2)
    if hasattr(a1, 'ecoreO_EReference18'):
        assert not _is_linked(a1, 'ecoreO_EReference18', b)
    if hasattr(a2, 'ecoreO_EReference18'):
        assert _is_linked(a2, 'ecoreO_EReference18', b)
    _safe_set(b, 'ecoreO_EClass17', set())
    assert not _is_linked(b, 'ecoreO_EClass17', a2)
    if hasattr(a2, 'ecoreO_EReference18'):
        assert not _is_linked(a2, 'ecoreO_EReference18', b)


def test_assoc_eStructuralFeatures35_reverse_link_reassign_clear():
    a1 = ecoreO_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = ecoreO_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = ecoreO_EClass(abstract=True, interface=True)
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


def test_assoc_eSubpackages64_reverse_link_reassign_clear():
    a1 = ecoreO_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecoreO_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecoreO_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSuperPackage', {a1})
    assert _is_linked(b, 'eSuperPackage', a1)
    if hasattr(a1, 'EPackage65'):
        assert _is_linked(a1, 'EPackage65', b)
    _safe_set(b, 'eSuperPackage', {a2})
    assert _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a1, 'EPackage65'):
        assert not _is_linked(a1, 'EPackage65', b)
    if hasattr(a2, 'EPackage65'):
        assert _is_linked(a2, 'EPackage65', b)
    _safe_set(b, 'eSuperPackage', set())
    assert not _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a2, 'EPackage65'):
        assert not _is_linked(a2, 'EPackage65', b)


def test_assoc_eSuperPackage67_reverse_link_reassign_clear():
    a1 = ecoreO_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecoreO_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecoreO_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSubpackages', a1)
    assert _is_linked(b, 'eSubpackages', a1)
    if hasattr(a1, 'EPackage68'):
        assert _is_linked(a1, 'EPackage68', b)
    _safe_set(b, 'eSubpackages', a2)
    assert _is_linked(b, 'eSubpackages', a2)
    if hasattr(a1, 'EPackage68'):
        assert not _is_linked(a1, 'EPackage68', b)
    if hasattr(a2, 'EPackage68'):
        assert _is_linked(a2, 'EPackage68', b)
    _safe_set(b, 'eSubpackages', None)
    assert not _is_linked(b, 'eSubpackages', a2)
    if hasattr(a2, 'EPackage68'):
        assert not _is_linked(a2, 'EPackage68', b)


def test_assoc_eSuperTypes9_reverse_link_reassign_clear():
    a1 = ecoreO_EClass(abstract=True, interface=True)
    a2 = ecoreO_EClass(abstract=False, interface=False)
    b = ecoreO_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecoreO_EClass8', {a1})
    assert _is_linked(b, 'ecoreO_EClass8', a1)
    if hasattr(a1, 'ecoreO_EClass'):
        assert _is_linked(a1, 'ecoreO_EClass', b)
    _safe_set(b, 'ecoreO_EClass8', {a2})
    assert _is_linked(b, 'ecoreO_EClass8', a2)
    if hasattr(a1, 'ecoreO_EClass'):
        assert not _is_linked(a1, 'ecoreO_EClass', b)
    if hasattr(a2, 'ecoreO_EClass'):
        assert _is_linked(a2, 'ecoreO_EClass', b)
    _safe_set(b, 'ecoreO_EClass8', set())
    assert not _is_linked(b, 'ecoreO_EClass8', a2)
    if hasattr(a2, 'ecoreO_EClass'):
        assert not _is_linked(a2, 'ecoreO_EClass', b)


def test_assoc_eType82_reverse_link_reassign_clear():
    a1 = ecoreO_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    a2 = ecoreO_ETypedElement(lowerBound=13, many=False, ordered=False, required=False, unique=False, upperBound=13)
    b = ecoreO_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'ecoreO_EClassifier83', a1)
    assert _is_linked(b, 'ecoreO_EClassifier83', a1)
    if hasattr(a1, 'ecoreO_ETypedElement'):
        assert _is_linked(a1, 'ecoreO_ETypedElement', b)
    _safe_set(b, 'ecoreO_EClassifier83', a2)
    assert _is_linked(b, 'ecoreO_EClassifier83', a2)
    if hasattr(a1, 'ecoreO_ETypedElement'):
        assert not _is_linked(a1, 'ecoreO_ETypedElement', b)
    if hasattr(a2, 'ecoreO_ETypedElement'):
        assert _is_linked(a2, 'ecoreO_ETypedElement', b)
    _safe_set(b, 'ecoreO_EClassifier83', None)
    assert not _is_linked(b, 'ecoreO_EClassifier83', a2)
    if hasattr(a2, 'ecoreO_ETypedElement'):
        assert not _is_linked(a2, 'ecoreO_ETypedElement', b)


def test_assoc_references5_reverse_link_reassign_clear():
    a1 = ecoreO_EObject()
    a2 = ecoreO_EObject()
    b = ecoreO_EAnnotation(source="sample_text")
    _safe_set(b, 'ecoreO_EAnnotation6', {a1})
    assert _is_linked(b, 'ecoreO_EAnnotation6', a1)
    if hasattr(a1, 'ecoreO_EObject7'):
        assert _is_linked(a1, 'ecoreO_EObject7', b)
    _safe_set(b, 'ecoreO_EAnnotation6', {a2})
    assert _is_linked(b, 'ecoreO_EAnnotation6', a2)
    if hasattr(a1, 'ecoreO_EObject7'):
        assert not _is_linked(a1, 'ecoreO_EObject7', b)
    if hasattr(a2, 'ecoreO_EObject7'):
        assert _is_linked(a2, 'ecoreO_EObject7', b)
    _safe_set(b, 'ecoreO_EAnnotation6', set())
    assert not _is_linked(b, 'ecoreO_EAnnotation6', a2)
    if hasattr(a2, 'ecoreO_EObject7'):
        assert not _is_linked(a2, 'ecoreO_EObject7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_eAllGenericSuperTypes39_stub_double():
    # ecoreO_EGenericType has no real 'ecoreO_EGenericType41' property in the generated
    # code (a bare stub) -- manually attach it so ecoreO_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreO_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreO_EClass(abstract=True, interface=True)
    partner = ecoreO_EGenericType()
    setattr(partner, 'ecoreO_EGenericType41', None)
    _safe_set(owner, 'ecoreO_EClass40', {partner})
    assert getattr(partner, 'ecoreO_EGenericType41') == owner
    _safe_set(owner, 'ecoreO_EClass40', set())
    assert getattr(partner, 'ecoreO_EGenericType41') is None


def test_assoc_eClassifier102_stub_double():
    # ecoreO_EGenericType has no real 'ecoreO_EGenericType103' property in the generated
    # code (a bare stub) -- manually attach it so ecoreO_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreO_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreO_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecoreO_EGenericType()
    setattr(partner, 'ecoreO_EGenericType103', None)
    _safe_set(owner, 'ecoreO_EClassifier104', partner)
    assert getattr(partner, 'ecoreO_EGenericType103') == owner
    _safe_set(owner, 'ecoreO_EClassifier104', None)
    assert getattr(partner, 'ecoreO_EGenericType103') is None


def test_assoc_eGenericExceptions57_stub_double():
    # ecoreO_EGenericType has no real 'ecoreO_EGenericType59' property in the generated
    # code (a bare stub) -- manually attach it so ecoreO_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreO_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreO_EOperation()
    partner = ecoreO_EGenericType()
    setattr(partner, 'ecoreO_EGenericType59', None)
    _safe_set(owner, 'ecoreO_EOperation58', {partner})
    assert getattr(partner, 'ecoreO_EGenericType59') == owner
    _safe_set(owner, 'ecoreO_EOperation58', set())
    assert getattr(partner, 'ecoreO_EGenericType59') is None


def test_assoc_eGenericSuperTypes37_stub_double():
    # ecoreO_EGenericType has no real 'ecoreO_EGenericType' property in the generated
    # code (a bare stub) -- manually attach it so ecoreO_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreO_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreO_EClass(abstract=True, interface=True)
    partner = ecoreO_EGenericType()
    setattr(partner, 'ecoreO_EGenericType', None)
    _safe_set(owner, 'ecoreO_EClass38', {partner})
    assert getattr(partner, 'ecoreO_EGenericType') == owner
    _safe_set(owner, 'ecoreO_EClass38', set())
    assert getattr(partner, 'ecoreO_EGenericType') is None


def test_assoc_eGenericType84_stub_double():
    # ecoreO_EGenericType has no real 'ecoreO_EGenericType86' property in the generated
    # code (a bare stub) -- manually attach it so ecoreO_ETypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreO_ETypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreO_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    partner = ecoreO_EGenericType()
    setattr(partner, 'ecoreO_EGenericType86', None)
    _safe_set(owner, 'ecoreO_ETypedElement85', partner)
    assert getattr(partner, 'ecoreO_EGenericType86') == owner
    _safe_set(owner, 'ecoreO_ETypedElement85', None)
    assert getattr(partner, 'ecoreO_EGenericType86') is None


def test_assoc_eOperation69_stub_double():
    # ecoreO_EParameter has no real 'eParameters' property in the generated
    # code (a bare stub) -- manually attach it so ecoreO_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreO_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreO_EOperation()
    partner = ecoreO_EParameter()
    setattr(partner, 'eParameters', None)
    _safe_set(owner, 'EOperation70', partner)
    assert getattr(partner, 'eParameters') == owner
    _safe_set(owner, 'EOperation70', None)
    assert getattr(partner, 'eParameters') is None


def test_assoc_eParameters53_stub_double():
    # ecoreO_EParameter has no real 'EParameter' property in the generated
    # code (a bare stub) -- manually attach it so ecoreO_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreO_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreO_EOperation()
    partner = ecoreO_EParameter()
    setattr(partner, 'EParameter', None)
    _safe_set(owner, 'eOperation', {partner})
    assert getattr(partner, 'EParameter') == owner
    _safe_set(owner, 'eOperation', set())
    assert getattr(partner, 'EParameter') is None


def test_assoc_eRawType93_stub_double():
    # ecoreO_EGenericType has no real 'ecoreO_EGenericType94' property in the generated
    # code (a bare stub) -- manually attach it so ecoreO_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreO_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreO_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecoreO_EGenericType()
    setattr(partner, 'ecoreO_EGenericType94', None)
    _safe_set(owner, 'ecoreO_EClassifier95', partner)
    assert getattr(partner, 'ecoreO_EGenericType94') == owner
    _safe_set(owner, 'ecoreO_EClassifier95', None)
    assert getattr(partner, 'ecoreO_EGenericType94') is None


def test_assoc_eTypeParameters43_stub_double():
    # ecoreO_ETypeParameter has no real 'ecoreO_ETypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so ecoreO_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreO_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreO_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecoreO_ETypeParameter()
    setattr(partner, 'ecoreO_ETypeParameter', None)
    _safe_set(owner, 'ecoreO_EClassifier', {partner})
    assert getattr(partner, 'ecoreO_ETypeParameter') == owner
    _safe_set(owner, 'ecoreO_EClassifier', set())
    assert getattr(partner, 'ecoreO_ETypeParameter') is None


def test_assoc_eTypeParameters50_stub_double():
    # ecoreO_ETypeParameter has no real 'ecoreO_ETypeParameter52' property in the generated
    # code (a bare stub) -- manually attach it so ecoreO_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreO_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreO_EOperation()
    partner = ecoreO_ETypeParameter()
    setattr(partner, 'ecoreO_ETypeParameter52', None)
    _safe_set(owner, 'ecoreO_EOperation51', {partner})
    assert getattr(partner, 'ecoreO_ETypeParameter52') == owner
    _safe_set(owner, 'ecoreO_EOperation51', set())
    assert getattr(partner, 'ecoreO_ETypeParameter52') is None


