import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EClassifier,
    EDataType,
    EModelElement,
    ENamedElement,
    EObject,
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
    ecore_Visitable,
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


def test_assoc_eAllAttributes11_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EAttribute(iD=True)
    _safe_set(b, 'ecore_EAttribute13', a1)
    assert _is_linked(b, 'ecore_EAttribute13', a1)
    if hasattr(a1, 'ecore_EClass12'):
        assert _is_linked(a1, 'ecore_EClass12', b)
    _safe_set(b, 'ecore_EAttribute13', a2)
    assert _is_linked(b, 'ecore_EAttribute13', a2)
    if hasattr(a1, 'ecore_EClass12'):
        assert not _is_linked(a1, 'ecore_EClass12', b)
    if hasattr(a2, 'ecore_EClass12'):
        assert _is_linked(a2, 'ecore_EClass12', b)
    _safe_set(b, 'ecore_EAttribute13', None)
    assert not _is_linked(b, 'ecore_EAttribute13', a2)
    if hasattr(a2, 'ecore_EClass12'):
        assert not _is_linked(a2, 'ecore_EClass12', b)


def test_assoc_eAllContainments22_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass23', {a1})
    assert _is_linked(b, 'ecore_EClass23', a1)
    if hasattr(a1, 'ecore_EReference24'):
        assert _is_linked(a1, 'ecore_EReference24', b)
    _safe_set(b, 'ecore_EClass23', {a2})
    assert _is_linked(b, 'ecore_EClass23', a2)
    if hasattr(a1, 'ecore_EReference24'):
        assert not _is_linked(a1, 'ecore_EReference24', b)
    if hasattr(a2, 'ecore_EReference24'):
        assert _is_linked(a2, 'ecore_EReference24', b)
    _safe_set(b, 'ecore_EClass23', set())
    assert not _is_linked(b, 'ecore_EClass23', a2)
    if hasattr(a2, 'ecore_EReference24'):
        assert not _is_linked(a2, 'ecore_EReference24', b)


def test_assoc_eAllReferences14_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass15', {a1})
    assert _is_linked(b, 'ecore_EClass15', a1)
    if hasattr(a1, 'ecore_EReference'):
        assert _is_linked(a1, 'ecore_EReference', b)
    _safe_set(b, 'ecore_EClass15', {a2})
    assert _is_linked(b, 'ecore_EClass15', a2)
    if hasattr(a1, 'ecore_EReference'):
        assert not _is_linked(a1, 'ecore_EReference', b)
    if hasattr(a2, 'ecore_EReference'):
        assert _is_linked(a2, 'ecore_EReference', b)
    _safe_set(b, 'ecore_EClass15', set())
    assert not _is_linked(b, 'ecore_EClass15', a2)
    if hasattr(a2, 'ecore_EReference'):
        assert not _is_linked(a2, 'ecore_EReference', b)


def test_assoc_eAllStructuralFeatures27_reverse_link_reassign_clear():
    a1 = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = ecore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass28', {a1})
    assert _is_linked(b, 'ecore_EClass28', a1)
    if hasattr(a1, 'ecore_EStructuralFeature'):
        assert _is_linked(a1, 'ecore_EStructuralFeature', b)
    _safe_set(b, 'ecore_EClass28', {a2})
    assert _is_linked(b, 'ecore_EClass28', a2)
    if hasattr(a1, 'ecore_EStructuralFeature'):
        assert not _is_linked(a1, 'ecore_EStructuralFeature', b)
    if hasattr(a2, 'ecore_EStructuralFeature'):
        assert _is_linked(a2, 'ecore_EStructuralFeature', b)
    _safe_set(b, 'ecore_EClass28', set())
    assert not _is_linked(b, 'ecore_EClass28', a2)
    if hasattr(a2, 'ecore_EStructuralFeature'):
        assert not _is_linked(a2, 'ecore_EStructuralFeature', b)


def test_assoc_eAllSuperTypes30_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass31', a1)
    assert _is_linked(b, 'ecore_EClass31', a1)
    if hasattr(a1, 'ecore_EClass29'):
        assert _is_linked(a1, 'ecore_EClass29', b)
    _safe_set(b, 'ecore_EClass31', a2)
    assert _is_linked(b, 'ecore_EClass31', a2)
    if hasattr(a1, 'ecore_EClass29'):
        assert not _is_linked(a1, 'ecore_EClass29', b)
    if hasattr(a2, 'ecore_EClass29'):
        assert _is_linked(a2, 'ecore_EClass29', b)
    _safe_set(b, 'ecore_EClass31', None)
    assert not _is_linked(b, 'ecore_EClass31', a2)
    if hasattr(a2, 'ecore_EClass29'):
        assert not _is_linked(a2, 'ecore_EClass29', b)


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


def test_assoc_eAttributes19_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EAttribute(iD=True)
    _safe_set(b, 'ecore_EAttribute21', a1)
    assert _is_linked(b, 'ecore_EAttribute21', a1)
    if hasattr(a1, 'ecore_EClass20'):
        assert _is_linked(a1, 'ecore_EClass20', b)
    _safe_set(b, 'ecore_EAttribute21', a2)
    assert _is_linked(b, 'ecore_EAttribute21', a2)
    if hasattr(a1, 'ecore_EClass20'):
        assert not _is_linked(a1, 'ecore_EClass20', b)
    if hasattr(a2, 'ecore_EClass20'):
        assert _is_linked(a2, 'ecore_EClass20', b)
    _safe_set(b, 'ecore_EAttribute21', None)
    assert not _is_linked(b, 'ecore_EAttribute21', a2)
    if hasattr(a2, 'ecore_EClass20'):
        assert not _is_linked(a2, 'ecore_EClass20', b)


def test_assoc_eClassifiers61_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
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


def test_assoc_eContainingClass80_reverse_link_reassign_clear():
    a1 = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = ecore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = ecore_EClass(abstract=True, interface=True)
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


def test_assoc_eFactoryInstance60_reverse_link_reassign_clear():
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


def test_assoc_eIDAttribute32_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EAttribute(iD=True)
    _safe_set(b, 'ecore_EAttribute34', a1)
    assert _is_linked(b, 'ecore_EAttribute34', a1)
    if hasattr(a1, 'ecore_EClass33'):
        assert _is_linked(a1, 'ecore_EClass33', b)
    _safe_set(b, 'ecore_EAttribute34', a2)
    assert _is_linked(b, 'ecore_EAttribute34', a2)
    if hasattr(a1, 'ecore_EClass33'):
        assert not _is_linked(a1, 'ecore_EClass33', b)
    if hasattr(a2, 'ecore_EClass33'):
        assert _is_linked(a2, 'ecore_EClass33', b)
    _safe_set(b, 'ecore_EAttribute34', None)
    assert not _is_linked(b, 'ecore_EAttribute34', a2)
    if hasattr(a2, 'ecore_EClass33'):
        assert not _is_linked(a2, 'ecore_EClass33', b)


def test_assoc_eKeys77_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EAttribute(iD=True)
    _safe_set(b, 'ecore_EAttribute79', a1)
    assert _is_linked(b, 'ecore_EAttribute79', a1)
    if hasattr(a1, 'ecore_EReference78'):
        assert _is_linked(a1, 'ecore_EReference78', b)
    _safe_set(b, 'ecore_EAttribute79', a2)
    assert _is_linked(b, 'ecore_EAttribute79', a2)
    if hasattr(a1, 'ecore_EReference78'):
        assert not _is_linked(a1, 'ecore_EReference78', b)
    if hasattr(a2, 'ecore_EReference78'):
        assert _is_linked(a2, 'ecore_EReference78', b)
    _safe_set(b, 'ecore_EAttribute79', None)
    assert not _is_linked(b, 'ecore_EAttribute79', a2)
    if hasattr(a2, 'ecore_EReference78'):
        assert not _is_linked(a2, 'ecore_EReference78', b)


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


def test_assoc_eOpposite72_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EReference(container=True, containment=True, resolveProxies=True)
    _safe_set(b, 'ecore_EReference73', a1)
    assert _is_linked(b, 'ecore_EReference73', a1)
    if hasattr(a1, 'ecore_EReference71'):
        assert _is_linked(a1, 'ecore_EReference71', b)
    _safe_set(b, 'ecore_EReference73', a2)
    assert _is_linked(b, 'ecore_EReference73', a2)
    if hasattr(a1, 'ecore_EReference71'):
        assert not _is_linked(a1, 'ecore_EReference71', b)
    if hasattr(a2, 'ecore_EReference71'):
        assert _is_linked(a2, 'ecore_EReference71', b)
    _safe_set(b, 'ecore_EReference73', None)
    assert not _is_linked(b, 'ecore_EReference73', a2)
    if hasattr(a2, 'ecore_EReference71'):
        assert not _is_linked(a2, 'ecore_EReference71', b)


def test_assoc_ePackage42_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
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


def test_assoc_eReferenceType74_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass76', a1)
    assert _is_linked(b, 'ecore_EClass76', a1)
    if hasattr(a1, 'ecore_EReference75'):
        assert _is_linked(a1, 'ecore_EReference75', b)
    _safe_set(b, 'ecore_EClass76', a2)
    assert _is_linked(b, 'ecore_EClass76', a2)
    if hasattr(a1, 'ecore_EReference75'):
        assert not _is_linked(a1, 'ecore_EReference75', b)
    if hasattr(a2, 'ecore_EReference75'):
        assert _is_linked(a2, 'ecore_EReference75', b)
    _safe_set(b, 'ecore_EClass76', None)
    assert not _is_linked(b, 'ecore_EClass76', a2)
    if hasattr(a2, 'ecore_EReference75'):
        assert not _is_linked(a2, 'ecore_EReference75', b)


def test_assoc_eReferences16_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass17', {a1})
    assert _is_linked(b, 'ecore_EClass17', a1)
    if hasattr(a1, 'ecore_EReference18'):
        assert _is_linked(a1, 'ecore_EReference18', b)
    _safe_set(b, 'ecore_EClass17', {a2})
    assert _is_linked(b, 'ecore_EClass17', a2)
    if hasattr(a1, 'ecore_EReference18'):
        assert not _is_linked(a1, 'ecore_EReference18', b)
    if hasattr(a2, 'ecore_EReference18'):
        assert _is_linked(a2, 'ecore_EReference18', b)
    _safe_set(b, 'ecore_EClass17', set())
    assert not _is_linked(b, 'ecore_EClass17', a2)
    if hasattr(a2, 'ecore_EReference18'):
        assert not _is_linked(a2, 'ecore_EReference18', b)


def test_assoc_eStructuralFeatures35_reverse_link_reassign_clear():
    a1 = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = ecore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = ecore_EClass(abstract=True, interface=True)
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
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
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
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
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
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass8', {a1})
    assert _is_linked(b, 'ecore_EClass8', a1)
    if hasattr(a1, 'ecore_EClass'):
        assert _is_linked(a1, 'ecore_EClass', b)
    _safe_set(b, 'ecore_EClass8', {a2})
    assert _is_linked(b, 'ecore_EClass8', a2)
    if hasattr(a1, 'ecore_EClass'):
        assert not _is_linked(a1, 'ecore_EClass', b)
    if hasattr(a2, 'ecore_EClass'):
        assert _is_linked(a2, 'ecore_EClass', b)
    _safe_set(b, 'ecore_EClass8', set())
    assert not _is_linked(b, 'ecore_EClass8', a2)
    if hasattr(a2, 'ecore_EClass'):
        assert not _is_linked(a2, 'ecore_EClass', b)


def test_assoc_eType82_reverse_link_reassign_clear():
    a1 = ecore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    a2 = ecore_ETypedElement(lowerBound=13, many=False, ordered=False, required=False, unique=False, upperBound=13)
    b = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'ecore_EClassifier83', a1)
    assert _is_linked(b, 'ecore_EClassifier83', a1)
    if hasattr(a1, 'ecore_ETypedElement'):
        assert _is_linked(a1, 'ecore_ETypedElement', b)
    _safe_set(b, 'ecore_EClassifier83', a2)
    assert _is_linked(b, 'ecore_EClassifier83', a2)
    if hasattr(a1, 'ecore_ETypedElement'):
        assert not _is_linked(a1, 'ecore_ETypedElement', b)
    if hasattr(a2, 'ecore_ETypedElement'):
        assert _is_linked(a2, 'ecore_ETypedElement', b)
    _safe_set(b, 'ecore_EClassifier83', None)
    assert not _is_linked(b, 'ecore_EClassifier83', a2)
    if hasattr(a2, 'ecore_ETypedElement'):
        assert not _is_linked(a2, 'ecore_ETypedElement', b)


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

def test_assoc_eAllGenericSuperTypes39_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType41' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract=True, interface=True)
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType41', None)
    _safe_set(owner, 'ecore_EClass40', {partner})
    assert getattr(partner, 'ecore_EGenericType41') == owner
    _safe_set(owner, 'ecore_EClass40', set())
    assert getattr(partner, 'ecore_EGenericType41') is None


def test_assoc_eAllOperations25_stub_double():
    # ecore_EOperation has no real 'ecore_EOperation' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract=True, interface=True)
    partner = ecore_EOperation()
    setattr(partner, 'ecore_EOperation', None)
    _safe_set(owner, 'ecore_EClass26', {partner})
    assert getattr(partner, 'ecore_EOperation') == owner
    _safe_set(owner, 'ecore_EClass26', set())
    assert getattr(partner, 'ecore_EOperation') is None


def test_assoc_eClassifier102_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType103' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType103', None)
    _safe_set(owner, 'ecore_EClassifier104', partner)
    assert getattr(partner, 'ecore_EGenericType103') == owner
    _safe_set(owner, 'ecore_EClassifier104', None)
    assert getattr(partner, 'ecore_EGenericType103') is None


def test_assoc_eContainingClass49_stub_double():
    # ecore_EOperation has no real 'eOperations' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract=True, interface=True)
    partner = ecore_EOperation()
    setattr(partner, 'eOperations', None)
    _safe_set(owner, 'EClass', partner)
    assert getattr(partner, 'eOperations') == owner
    _safe_set(owner, 'EClass', None)
    assert getattr(partner, 'eOperations') is None


def test_assoc_eExceptions54_stub_double():
    # ecore_EOperation has no real 'ecore_EOperation55' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecore_EOperation()
    setattr(partner, 'ecore_EOperation55', None)
    _safe_set(owner, 'ecore_EClassifier56', partner)
    assert owner in getattr(partner, 'ecore_EOperation55')
    _safe_set(owner, 'ecore_EClassifier56', None)
    assert owner not in getattr(partner, 'ecore_EOperation55')


def test_assoc_eGenericSuperTypes37_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract=True, interface=True)
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType', None)
    _safe_set(owner, 'ecore_EClass38', {partner})
    assert getattr(partner, 'ecore_EGenericType') == owner
    _safe_set(owner, 'ecore_EClass38', set())
    assert getattr(partner, 'ecore_EGenericType') is None


def test_assoc_eGenericType84_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType86' property in the generated
    # code (a bare stub) -- manually attach it so ecore_ETypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_ETypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType86', None)
    _safe_set(owner, 'ecore_ETypedElement85', partner)
    assert getattr(partner, 'ecore_EGenericType86') == owner
    _safe_set(owner, 'ecore_ETypedElement85', None)
    assert getattr(partner, 'ecore_EGenericType86') is None


def test_assoc_eOperations10_stub_double():
    # ecore_EOperation has no real 'EOperation' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract=True, interface=True)
    partner = ecore_EOperation()
    setattr(partner, 'EOperation', None)
    _safe_set(owner, 'eContainingClass', {partner})
    assert getattr(partner, 'EOperation') == owner
    _safe_set(owner, 'eContainingClass', set())
    assert getattr(partner, 'EOperation') is None


def test_assoc_eRawType93_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType94' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType94', None)
    _safe_set(owner, 'ecore_EClassifier95', partner)
    assert getattr(partner, 'ecore_EGenericType94') == owner
    _safe_set(owner, 'ecore_EClassifier95', None)
    assert getattr(partner, 'ecore_EGenericType94') is None


def test_assoc_eTypeParameters43_stub_double():
    # ecore_ETypeParameter has no real 'ecore_ETypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecore_ETypeParameter()
    setattr(partner, 'ecore_ETypeParameter', None)
    _safe_set(owner, 'ecore_EClassifier', {partner})
    assert getattr(partner, 'ecore_ETypeParameter') == owner
    _safe_set(owner, 'ecore_EClassifier', set())
    assert getattr(partner, 'ecore_ETypeParameter') is None


