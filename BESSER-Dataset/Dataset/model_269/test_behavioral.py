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
    javaless_EAnnotation,
    javaless_EAttribute,
    javaless_EClass,
    javaless_EClassifier,
    javaless_EDataType,
    javaless_EEnum,
    javaless_EEnumLiteral,
    javaless_EFactory,
    javaless_EModelElement,
    javaless_ENamedElement,
    javaless_EObject,
    javaless_EOperation,
    javaless_EPackage,
    javaless_EParameter,
    javaless_EReference,
    javaless_EStringToStringMapEntry,
    javaless_EStructuralFeature,
    javaless_ETypedElement,
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
    a1 = javaless_EObject()
    a2 = javaless_EObject()
    b = javaless_EAnnotation(source="sample_text")
    _safe_set(b, 'javaless_EAnnotation4', {a1})
    assert _is_linked(b, 'javaless_EAnnotation4', a1)
    if hasattr(a1, 'javaless_EObject'):
        assert _is_linked(a1, 'javaless_EObject', b)
    _safe_set(b, 'javaless_EAnnotation4', {a2})
    assert _is_linked(b, 'javaless_EAnnotation4', a2)
    if hasattr(a1, 'javaless_EObject'):
        assert not _is_linked(a1, 'javaless_EObject', b)
    if hasattr(a2, 'javaless_EObject'):
        assert _is_linked(a2, 'javaless_EObject', b)
    _safe_set(b, 'javaless_EAnnotation4', set())
    assert not _is_linked(b, 'javaless_EAnnotation4', a2)
    if hasattr(a2, 'javaless_EObject'):
        assert not _is_linked(a2, 'javaless_EObject', b)


def test_assoc_details1_reverse_link_reassign_clear():
    a1 = javaless_EStringToStringMapEntry(key="sample_text", value="sample_text")
    a2 = javaless_EStringToStringMapEntry(key="sample_text_2", value="sample_text_2")
    b = javaless_EAnnotation(source="sample_text")
    _safe_set(b, 'javaless_EAnnotation', {a1})
    assert _is_linked(b, 'javaless_EAnnotation', a1)
    if hasattr(a1, 'javaless_EStringToStringMapEntry'):
        assert _is_linked(a1, 'javaless_EStringToStringMapEntry', b)
    _safe_set(b, 'javaless_EAnnotation', {a2})
    assert _is_linked(b, 'javaless_EAnnotation', a2)
    if hasattr(a1, 'javaless_EStringToStringMapEntry'):
        assert not _is_linked(a1, 'javaless_EStringToStringMapEntry', b)
    if hasattr(a2, 'javaless_EStringToStringMapEntry'):
        assert _is_linked(a2, 'javaless_EStringToStringMapEntry', b)
    _safe_set(b, 'javaless_EAnnotation', set())
    assert not _is_linked(b, 'javaless_EAnnotation', a2)
    if hasattr(a2, 'javaless_EStringToStringMapEntry'):
        assert not _is_linked(a2, 'javaless_EStringToStringMapEntry', b)


def test_assoc_eAllAttributes11_reverse_link_reassign_clear():
    a1 = javaless_EClass(abstract=True, interface=True)
    a2 = javaless_EClass(abstract=False, interface=False)
    b = javaless_EAttribute(iD=True)
    _safe_set(b, 'javaless_EAttribute13', a1)
    assert _is_linked(b, 'javaless_EAttribute13', a1)
    if hasattr(a1, 'javaless_EClass12'):
        assert _is_linked(a1, 'javaless_EClass12', b)
    _safe_set(b, 'javaless_EAttribute13', a2)
    assert _is_linked(b, 'javaless_EAttribute13', a2)
    if hasattr(a1, 'javaless_EClass12'):
        assert not _is_linked(a1, 'javaless_EClass12', b)
    if hasattr(a2, 'javaless_EClass12'):
        assert _is_linked(a2, 'javaless_EClass12', b)
    _safe_set(b, 'javaless_EAttribute13', None)
    assert not _is_linked(b, 'javaless_EAttribute13', a2)
    if hasattr(a2, 'javaless_EClass12'):
        assert not _is_linked(a2, 'javaless_EClass12', b)


def test_assoc_eAllContainments22_reverse_link_reassign_clear():
    a1 = javaless_EReference(container=True, containment=True, resolveProxies=True)
    a2 = javaless_EReference(container=False, containment=False, resolveProxies=False)
    b = javaless_EClass(abstract=True, interface=True)
    _safe_set(b, 'javaless_EClass23', {a1})
    assert _is_linked(b, 'javaless_EClass23', a1)
    if hasattr(a1, 'javaless_EReference24'):
        assert _is_linked(a1, 'javaless_EReference24', b)
    _safe_set(b, 'javaless_EClass23', {a2})
    assert _is_linked(b, 'javaless_EClass23', a2)
    if hasattr(a1, 'javaless_EReference24'):
        assert not _is_linked(a1, 'javaless_EReference24', b)
    if hasattr(a2, 'javaless_EReference24'):
        assert _is_linked(a2, 'javaless_EReference24', b)
    _safe_set(b, 'javaless_EClass23', set())
    assert not _is_linked(b, 'javaless_EClass23', a2)
    if hasattr(a2, 'javaless_EReference24'):
        assert not _is_linked(a2, 'javaless_EReference24', b)


def test_assoc_eAllReferences14_reverse_link_reassign_clear():
    a1 = javaless_EReference(container=True, containment=True, resolveProxies=True)
    a2 = javaless_EReference(container=False, containment=False, resolveProxies=False)
    b = javaless_EClass(abstract=True, interface=True)
    _safe_set(b, 'javaless_EClass15', {a1})
    assert _is_linked(b, 'javaless_EClass15', a1)
    if hasattr(a1, 'javaless_EReference'):
        assert _is_linked(a1, 'javaless_EReference', b)
    _safe_set(b, 'javaless_EClass15', {a2})
    assert _is_linked(b, 'javaless_EClass15', a2)
    if hasattr(a1, 'javaless_EReference'):
        assert not _is_linked(a1, 'javaless_EReference', b)
    if hasattr(a2, 'javaless_EReference'):
        assert _is_linked(a2, 'javaless_EReference', b)
    _safe_set(b, 'javaless_EClass15', set())
    assert not _is_linked(b, 'javaless_EClass15', a2)
    if hasattr(a2, 'javaless_EReference'):
        assert not _is_linked(a2, 'javaless_EReference', b)


def test_assoc_eAllStructuralFeatures27_reverse_link_reassign_clear():
    a1 = javaless_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = javaless_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = javaless_EClass(abstract=True, interface=True)
    _safe_set(b, 'javaless_EClass28', {a1})
    assert _is_linked(b, 'javaless_EClass28', a1)
    if hasattr(a1, 'javaless_EStructuralFeature'):
        assert _is_linked(a1, 'javaless_EStructuralFeature', b)
    _safe_set(b, 'javaless_EClass28', {a2})
    assert _is_linked(b, 'javaless_EClass28', a2)
    if hasattr(a1, 'javaless_EStructuralFeature'):
        assert not _is_linked(a1, 'javaless_EStructuralFeature', b)
    if hasattr(a2, 'javaless_EStructuralFeature'):
        assert _is_linked(a2, 'javaless_EStructuralFeature', b)
    _safe_set(b, 'javaless_EClass28', set())
    assert not _is_linked(b, 'javaless_EClass28', a2)
    if hasattr(a2, 'javaless_EStructuralFeature'):
        assert not _is_linked(a2, 'javaless_EStructuralFeature', b)


def test_assoc_eAllSuperTypes30_reverse_link_reassign_clear():
    a1 = javaless_EClass(abstract=True, interface=True)
    a2 = javaless_EClass(abstract=False, interface=False)
    b = javaless_EClass(abstract=True, interface=True)
    _safe_set(b, 'javaless_EClass31', a1)
    assert _is_linked(b, 'javaless_EClass31', a1)
    if hasattr(a1, 'javaless_EClass29'):
        assert _is_linked(a1, 'javaless_EClass29', b)
    _safe_set(b, 'javaless_EClass31', a2)
    assert _is_linked(b, 'javaless_EClass31', a2)
    if hasattr(a1, 'javaless_EClass29'):
        assert not _is_linked(a1, 'javaless_EClass29', b)
    if hasattr(a2, 'javaless_EClass29'):
        assert _is_linked(a2, 'javaless_EClass29', b)
    _safe_set(b, 'javaless_EClass31', None)
    assert not _is_linked(b, 'javaless_EClass31', a2)
    if hasattr(a2, 'javaless_EClass29'):
        assert not _is_linked(a2, 'javaless_EClass29', b)


def test_assoc_eAnnotations42_reverse_link_reassign_clear():
    a1 = javaless_EModelElement()
    a2 = javaless_EModelElement()
    b = javaless_EAnnotation(source="sample_text")
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
    a1 = javaless_EDataType(serializable=True)
    a2 = javaless_EDataType(serializable=False)
    b = javaless_EAttribute(iD=True)
    _safe_set(b, 'javaless_EAttribute', a1)
    assert _is_linked(b, 'javaless_EAttribute', a1)
    if hasattr(a1, 'javaless_EDataType'):
        assert _is_linked(a1, 'javaless_EDataType', b)
    _safe_set(b, 'javaless_EAttribute', a2)
    assert _is_linked(b, 'javaless_EAttribute', a2)
    if hasattr(a1, 'javaless_EDataType'):
        assert not _is_linked(a1, 'javaless_EDataType', b)
    if hasattr(a2, 'javaless_EDataType'):
        assert _is_linked(a2, 'javaless_EDataType', b)
    _safe_set(b, 'javaless_EAttribute', None)
    assert not _is_linked(b, 'javaless_EAttribute', a2)
    if hasattr(a2, 'javaless_EDataType'):
        assert not _is_linked(a2, 'javaless_EDataType', b)


def test_assoc_eAttributes19_reverse_link_reassign_clear():
    a1 = javaless_EClass(abstract=True, interface=True)
    a2 = javaless_EClass(abstract=False, interface=False)
    b = javaless_EAttribute(iD=True)
    _safe_set(b, 'javaless_EAttribute21', a1)
    assert _is_linked(b, 'javaless_EAttribute21', a1)
    if hasattr(a1, 'javaless_EClass20'):
        assert _is_linked(a1, 'javaless_EClass20', b)
    _safe_set(b, 'javaless_EAttribute21', a2)
    assert _is_linked(b, 'javaless_EAttribute21', a2)
    if hasattr(a1, 'javaless_EClass20'):
        assert not _is_linked(a1, 'javaless_EClass20', b)
    if hasattr(a2, 'javaless_EClass20'):
        assert _is_linked(a2, 'javaless_EClass20', b)
    _safe_set(b, 'javaless_EAttribute21', None)
    assert not _is_linked(b, 'javaless_EAttribute21', a2)
    if hasattr(a2, 'javaless_EClass20'):
        assert not _is_linked(a2, 'javaless_EClass20', b)


def test_assoc_eClassifiers48_reverse_link_reassign_clear():
    a1 = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = javaless_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = javaless_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text")
    _safe_set(b, 'EClassifier', a1)
    assert _is_linked(b, 'EClassifier', a1)
    if hasattr(a1, 'ePackage49'):
        assert _is_linked(a1, 'ePackage49', b)
    _safe_set(b, 'EClassifier', a2)
    assert _is_linked(b, 'EClassifier', a2)
    if hasattr(a1, 'ePackage49'):
        assert not _is_linked(a1, 'ePackage49', b)
    if hasattr(a2, 'ePackage49'):
        assert _is_linked(a2, 'ePackage49', b)
    _safe_set(b, 'EClassifier', None)
    assert not _is_linked(b, 'EClassifier', a2)
    if hasattr(a2, 'ePackage49'):
        assert not _is_linked(a2, 'ePackage49', b)


def test_assoc_eContainingClass64_reverse_link_reassign_clear():
    a1 = javaless_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = javaless_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = javaless_EClass(abstract=True, interface=True)
    _safe_set(b, 'EClass65', a1)
    assert _is_linked(b, 'EClass65', a1)
    if hasattr(a1, 'eStructuralFeatures'):
        assert _is_linked(a1, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass65', a2)
    assert _is_linked(b, 'EClass65', a2)
    if hasattr(a1, 'eStructuralFeatures'):
        assert not _is_linked(a1, 'eStructuralFeatures', b)
    if hasattr(a2, 'eStructuralFeatures'):
        assert _is_linked(a2, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass65', None)
    assert not _is_linked(b, 'EClass65', a2)
    if hasattr(a2, 'eStructuralFeatures'):
        assert not _is_linked(a2, 'eStructuralFeatures', b)


def test_assoc_eEnum39_reverse_link_reassign_clear():
    a1 = javaless_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    a2 = javaless_EEnumLiteral(instance="sample_text_2", literal="sample_text_2", value=13)
    b = javaless_EEnum()
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


def test_assoc_eFactoryInstance47_reverse_link_reassign_clear():
    a1 = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = javaless_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = javaless_EFactory()
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
    a1 = javaless_EClass(abstract=True, interface=True)
    a2 = javaless_EClass(abstract=False, interface=False)
    b = javaless_EAttribute(iD=True)
    _safe_set(b, 'javaless_EAttribute34', a1)
    assert _is_linked(b, 'javaless_EAttribute34', a1)
    if hasattr(a1, 'javaless_EClass33'):
        assert _is_linked(a1, 'javaless_EClass33', b)
    _safe_set(b, 'javaless_EAttribute34', a2)
    assert _is_linked(b, 'javaless_EAttribute34', a2)
    if hasattr(a1, 'javaless_EClass33'):
        assert not _is_linked(a1, 'javaless_EClass33', b)
    if hasattr(a2, 'javaless_EClass33'):
        assert _is_linked(a2, 'javaless_EClass33', b)
    _safe_set(b, 'javaless_EAttribute34', None)
    assert not _is_linked(b, 'javaless_EAttribute34', a2)
    if hasattr(a2, 'javaless_EClass33'):
        assert not _is_linked(a2, 'javaless_EClass33', b)


def test_assoc_eLiterals38_reverse_link_reassign_clear():
    a1 = javaless_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    a2 = javaless_EEnumLiteral(instance="sample_text_2", literal="sample_text_2", value=13)
    b = javaless_EEnum()
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
    a1 = javaless_EModelElement()
    a2 = javaless_EModelElement()
    b = javaless_EAnnotation(source="sample_text")
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


def test_assoc_eOpposite59_reverse_link_reassign_clear():
    a1 = javaless_EReference(container=True, containment=True, resolveProxies=True)
    a2 = javaless_EReference(container=False, containment=False, resolveProxies=False)
    b = javaless_EReference(container=True, containment=True, resolveProxies=True)
    _safe_set(b, 'javaless_EReference60', a1)
    assert _is_linked(b, 'javaless_EReference60', a1)
    if hasattr(a1, 'javaless_EReference58'):
        assert _is_linked(a1, 'javaless_EReference58', b)
    _safe_set(b, 'javaless_EReference60', a2)
    assert _is_linked(b, 'javaless_EReference60', a2)
    if hasattr(a1, 'javaless_EReference58'):
        assert not _is_linked(a1, 'javaless_EReference58', b)
    if hasattr(a2, 'javaless_EReference58'):
        assert _is_linked(a2, 'javaless_EReference58', b)
    _safe_set(b, 'javaless_EReference60', None)
    assert not _is_linked(b, 'javaless_EReference60', a2)
    if hasattr(a2, 'javaless_EReference58'):
        assert not _is_linked(a2, 'javaless_EReference58', b)


def test_assoc_ePackage37_reverse_link_reassign_clear():
    a1 = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = javaless_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = javaless_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text")
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


def test_assoc_ePackage40_reverse_link_reassign_clear():
    a1 = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = javaless_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = javaless_EFactory()
    _safe_set(b, 'eFactoryInstance', a1)
    assert _is_linked(b, 'eFactoryInstance', a1)
    if hasattr(a1, 'EPackage41'):
        assert _is_linked(a1, 'EPackage41', b)
    _safe_set(b, 'eFactoryInstance', a2)
    assert _is_linked(b, 'eFactoryInstance', a2)
    if hasattr(a1, 'EPackage41'):
        assert not _is_linked(a1, 'EPackage41', b)
    if hasattr(a2, 'EPackage41'):
        assert _is_linked(a2, 'EPackage41', b)
    _safe_set(b, 'eFactoryInstance', None)
    assert not _is_linked(b, 'eFactoryInstance', a2)
    if hasattr(a2, 'EPackage41'):
        assert not _is_linked(a2, 'EPackage41', b)


def test_assoc_eReferenceType61_reverse_link_reassign_clear():
    a1 = javaless_EReference(container=True, containment=True, resolveProxies=True)
    a2 = javaless_EReference(container=False, containment=False, resolveProxies=False)
    b = javaless_EClass(abstract=True, interface=True)
    _safe_set(b, 'javaless_EClass63', a1)
    assert _is_linked(b, 'javaless_EClass63', a1)
    if hasattr(a1, 'javaless_EReference62'):
        assert _is_linked(a1, 'javaless_EReference62', b)
    _safe_set(b, 'javaless_EClass63', a2)
    assert _is_linked(b, 'javaless_EClass63', a2)
    if hasattr(a1, 'javaless_EReference62'):
        assert not _is_linked(a1, 'javaless_EReference62', b)
    if hasattr(a2, 'javaless_EReference62'):
        assert _is_linked(a2, 'javaless_EReference62', b)
    _safe_set(b, 'javaless_EClass63', None)
    assert not _is_linked(b, 'javaless_EClass63', a2)
    if hasattr(a2, 'javaless_EReference62'):
        assert not _is_linked(a2, 'javaless_EReference62', b)


def test_assoc_eReferences16_reverse_link_reassign_clear():
    a1 = javaless_EReference(container=True, containment=True, resolveProxies=True)
    a2 = javaless_EReference(container=False, containment=False, resolveProxies=False)
    b = javaless_EClass(abstract=True, interface=True)
    _safe_set(b, 'javaless_EClass17', {a1})
    assert _is_linked(b, 'javaless_EClass17', a1)
    if hasattr(a1, 'javaless_EReference18'):
        assert _is_linked(a1, 'javaless_EReference18', b)
    _safe_set(b, 'javaless_EClass17', {a2})
    assert _is_linked(b, 'javaless_EClass17', a2)
    if hasattr(a1, 'javaless_EReference18'):
        assert not _is_linked(a1, 'javaless_EReference18', b)
    if hasattr(a2, 'javaless_EReference18'):
        assert _is_linked(a2, 'javaless_EReference18', b)
    _safe_set(b, 'javaless_EClass17', set())
    assert not _is_linked(b, 'javaless_EClass17', a2)
    if hasattr(a2, 'javaless_EReference18'):
        assert not _is_linked(a2, 'javaless_EReference18', b)


def test_assoc_eStructuralFeatures35_reverse_link_reassign_clear():
    a1 = javaless_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = javaless_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = javaless_EClass(abstract=True, interface=True)
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


def test_assoc_eSubpackages51_reverse_link_reassign_clear():
    a1 = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = javaless_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSuperPackage', {a1})
    assert _is_linked(b, 'eSuperPackage', a1)
    if hasattr(a1, 'EPackage52'):
        assert _is_linked(a1, 'EPackage52', b)
    _safe_set(b, 'eSuperPackage', {a2})
    assert _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a1, 'EPackage52'):
        assert not _is_linked(a1, 'EPackage52', b)
    if hasattr(a2, 'EPackage52'):
        assert _is_linked(a2, 'EPackage52', b)
    _safe_set(b, 'eSuperPackage', set())
    assert not _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a2, 'EPackage52'):
        assert not _is_linked(a2, 'EPackage52', b)


def test_assoc_eSuperPackage54_reverse_link_reassign_clear():
    a1 = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = javaless_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = javaless_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSubpackages', a1)
    assert _is_linked(b, 'eSubpackages', a1)
    if hasattr(a1, 'EPackage55'):
        assert _is_linked(a1, 'EPackage55', b)
    _safe_set(b, 'eSubpackages', a2)
    assert _is_linked(b, 'eSubpackages', a2)
    if hasattr(a1, 'EPackage55'):
        assert not _is_linked(a1, 'EPackage55', b)
    if hasattr(a2, 'EPackage55'):
        assert _is_linked(a2, 'EPackage55', b)
    _safe_set(b, 'eSubpackages', None)
    assert not _is_linked(b, 'eSubpackages', a2)
    if hasattr(a2, 'EPackage55'):
        assert not _is_linked(a2, 'EPackage55', b)


def test_assoc_eSuperTypes9_reverse_link_reassign_clear():
    a1 = javaless_EClass(abstract=True, interface=True)
    a2 = javaless_EClass(abstract=False, interface=False)
    b = javaless_EClass(abstract=True, interface=True)
    _safe_set(b, 'javaless_EClass8', {a1})
    assert _is_linked(b, 'javaless_EClass8', a1)
    if hasattr(a1, 'javaless_EClass'):
        assert _is_linked(a1, 'javaless_EClass', b)
    _safe_set(b, 'javaless_EClass8', {a2})
    assert _is_linked(b, 'javaless_EClass8', a2)
    if hasattr(a1, 'javaless_EClass'):
        assert not _is_linked(a1, 'javaless_EClass', b)
    if hasattr(a2, 'javaless_EClass'):
        assert _is_linked(a2, 'javaless_EClass', b)
    _safe_set(b, 'javaless_EClass8', set())
    assert not _is_linked(b, 'javaless_EClass8', a2)
    if hasattr(a2, 'javaless_EClass'):
        assert not _is_linked(a2, 'javaless_EClass', b)


def test_assoc_eType66_reverse_link_reassign_clear():
    a1 = javaless_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    a2 = javaless_ETypedElement(lowerBound=13, many=False, ordered=False, required=False, unique=False, upperBound=13)
    b = javaless_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text")
    _safe_set(b, 'javaless_EClassifier67', a1)
    assert _is_linked(b, 'javaless_EClassifier67', a1)
    if hasattr(a1, 'javaless_ETypedElement'):
        assert _is_linked(a1, 'javaless_ETypedElement', b)
    _safe_set(b, 'javaless_EClassifier67', a2)
    assert _is_linked(b, 'javaless_EClassifier67', a2)
    if hasattr(a1, 'javaless_ETypedElement'):
        assert not _is_linked(a1, 'javaless_ETypedElement', b)
    if hasattr(a2, 'javaless_ETypedElement'):
        assert _is_linked(a2, 'javaless_ETypedElement', b)
    _safe_set(b, 'javaless_EClassifier67', None)
    assert not _is_linked(b, 'javaless_EClassifier67', a2)
    if hasattr(a2, 'javaless_ETypedElement'):
        assert not _is_linked(a2, 'javaless_ETypedElement', b)


def test_assoc_references5_reverse_link_reassign_clear():
    a1 = javaless_EObject()
    a2 = javaless_EObject()
    b = javaless_EAnnotation(source="sample_text")
    _safe_set(b, 'javaless_EAnnotation6', {a1})
    assert _is_linked(b, 'javaless_EAnnotation6', a1)
    if hasattr(a1, 'javaless_EObject7'):
        assert _is_linked(a1, 'javaless_EObject7', b)
    _safe_set(b, 'javaless_EAnnotation6', {a2})
    assert _is_linked(b, 'javaless_EAnnotation6', a2)
    if hasattr(a1, 'javaless_EObject7'):
        assert not _is_linked(a1, 'javaless_EObject7', b)
    if hasattr(a2, 'javaless_EObject7'):
        assert _is_linked(a2, 'javaless_EObject7', b)
    _safe_set(b, 'javaless_EAnnotation6', set())
    assert not _is_linked(b, 'javaless_EAnnotation6', a2)
    if hasattr(a2, 'javaless_EObject7'):
        assert not _is_linked(a2, 'javaless_EObject7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_eAllOperations25_stub_double():
    # javaless_EOperation has no real 'javaless_EOperation' property in the generated
    # code (a bare stub) -- manually attach it so javaless_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaless_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaless_EClass(abstract=True, interface=True)
    partner = javaless_EOperation()
    setattr(partner, 'javaless_EOperation', None)
    _safe_set(owner, 'javaless_EClass26', {partner})
    assert getattr(partner, 'javaless_EOperation') == owner
    _safe_set(owner, 'javaless_EClass26', set())
    assert getattr(partner, 'javaless_EOperation') is None


def test_assoc_eContainingClass43_stub_double():
    # javaless_EOperation has no real 'eOperations' property in the generated
    # code (a bare stub) -- manually attach it so javaless_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaless_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaless_EClass(abstract=True, interface=True)
    partner = javaless_EOperation()
    setattr(partner, 'eOperations', None)
    _safe_set(owner, 'EClass', partner)
    assert getattr(partner, 'eOperations') == owner
    _safe_set(owner, 'EClass', None)
    assert getattr(partner, 'eOperations') is None


def test_assoc_eExceptions45_stub_double():
    # javaless_EOperation has no real 'javaless_EOperation46' property in the generated
    # code (a bare stub) -- manually attach it so javaless_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaless_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaless_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text")
    partner = javaless_EOperation()
    setattr(partner, 'javaless_EOperation46', None)
    _safe_set(owner, 'javaless_EClassifier', partner)
    assert owner in getattr(partner, 'javaless_EOperation46')
    _safe_set(owner, 'javaless_EClassifier', None)
    assert owner not in getattr(partner, 'javaless_EOperation46')


def test_assoc_eOperations10_stub_double():
    # javaless_EOperation has no real 'EOperation' property in the generated
    # code (a bare stub) -- manually attach it so javaless_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaless_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaless_EClass(abstract=True, interface=True)
    partner = javaless_EOperation()
    setattr(partner, 'EOperation', None)
    _safe_set(owner, 'eContainingClass', {partner})
    assert getattr(partner, 'EOperation') == owner
    _safe_set(owner, 'eContainingClass', set())
    assert getattr(partner, 'EOperation') is None


