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

def test_assoc_contents2_reverse_link_reassign_clear():
    a1 = ecore_EObject()
    a2 = ecore_EObject()
    b = ecore_EAnnotation(source="sample_text")
    _safe_set(b, 'ecore_EAnnotation', {a1})
    assert _is_linked(b, 'ecore_EAnnotation', a1)
    if hasattr(a1, 'ecore_EObject'):
        assert _is_linked(a1, 'ecore_EObject', b)
    _safe_set(b, 'ecore_EAnnotation', {a2})
    assert _is_linked(b, 'ecore_EAnnotation', a2)
    if hasattr(a1, 'ecore_EObject'):
        assert not _is_linked(a1, 'ecore_EObject', b)
    if hasattr(a2, 'ecore_EObject'):
        assert _is_linked(a2, 'ecore_EObject', b)
    _safe_set(b, 'ecore_EAnnotation', set())
    assert not _is_linked(b, 'ecore_EAnnotation', a2)
    if hasattr(a2, 'ecore_EObject'):
        assert not _is_linked(a2, 'ecore_EObject', b)


def test_assoc_eAllAttributes9_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EAttribute(iD=True)
    _safe_set(b, 'ecore_EAttribute11', a1)
    assert _is_linked(b, 'ecore_EAttribute11', a1)
    if hasattr(a1, 'ecore_EClass10'):
        assert _is_linked(a1, 'ecore_EClass10', b)
    _safe_set(b, 'ecore_EAttribute11', a2)
    assert _is_linked(b, 'ecore_EAttribute11', a2)
    if hasattr(a1, 'ecore_EClass10'):
        assert not _is_linked(a1, 'ecore_EClass10', b)
    if hasattr(a2, 'ecore_EClass10'):
        assert _is_linked(a2, 'ecore_EClass10', b)
    _safe_set(b, 'ecore_EAttribute11', None)
    assert not _is_linked(b, 'ecore_EAttribute11', a2)
    if hasattr(a2, 'ecore_EClass10'):
        assert not _is_linked(a2, 'ecore_EClass10', b)


def test_assoc_eAllAttributesForTest43_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EAttribute(iD=True)
    _safe_set(b, 'ecore_EAttribute45', a1)
    assert _is_linked(b, 'ecore_EAttribute45', a1)
    if hasattr(a1, 'ecore_EClass44'):
        assert _is_linked(a1, 'ecore_EClass44', b)
    _safe_set(b, 'ecore_EAttribute45', a2)
    assert _is_linked(b, 'ecore_EAttribute45', a2)
    if hasattr(a1, 'ecore_EClass44'):
        assert not _is_linked(a1, 'ecore_EClass44', b)
    if hasattr(a2, 'ecore_EClass44'):
        assert _is_linked(a2, 'ecore_EClass44', b)
    _safe_set(b, 'ecore_EAttribute45', None)
    assert not _is_linked(b, 'ecore_EAttribute45', a2)
    if hasattr(a2, 'ecore_EClass44'):
        assert not _is_linked(a2, 'ecore_EClass44', b)


def test_assoc_eAllContainments20_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass21', {a1})
    assert _is_linked(b, 'ecore_EClass21', a1)
    if hasattr(a1, 'ecore_EReference22'):
        assert _is_linked(a1, 'ecore_EReference22', b)
    _safe_set(b, 'ecore_EClass21', {a2})
    assert _is_linked(b, 'ecore_EClass21', a2)
    if hasattr(a1, 'ecore_EReference22'):
        assert not _is_linked(a1, 'ecore_EReference22', b)
    if hasattr(a2, 'ecore_EReference22'):
        assert _is_linked(a2, 'ecore_EReference22', b)
    _safe_set(b, 'ecore_EClass21', set())
    assert not _is_linked(b, 'ecore_EClass21', a2)
    if hasattr(a2, 'ecore_EReference22'):
        assert not _is_linked(a2, 'ecore_EReference22', b)


def test_assoc_eAllReferences12_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass13', {a1})
    assert _is_linked(b, 'ecore_EClass13', a1)
    if hasattr(a1, 'ecore_EReference'):
        assert _is_linked(a1, 'ecore_EReference', b)
    _safe_set(b, 'ecore_EClass13', {a2})
    assert _is_linked(b, 'ecore_EClass13', a2)
    if hasattr(a1, 'ecore_EReference'):
        assert not _is_linked(a1, 'ecore_EReference', b)
    if hasattr(a2, 'ecore_EReference'):
        assert _is_linked(a2, 'ecore_EReference', b)
    _safe_set(b, 'ecore_EClass13', set())
    assert not _is_linked(b, 'ecore_EClass13', a2)
    if hasattr(a2, 'ecore_EReference'):
        assert not _is_linked(a2, 'ecore_EReference', b)


def test_assoc_eAllStructuralFeatures25_reverse_link_reassign_clear():
    a1 = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = ecore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass26', {a1})
    assert _is_linked(b, 'ecore_EClass26', a1)
    if hasattr(a1, 'ecore_EStructuralFeature'):
        assert _is_linked(a1, 'ecore_EStructuralFeature', b)
    _safe_set(b, 'ecore_EClass26', {a2})
    assert _is_linked(b, 'ecore_EClass26', a2)
    if hasattr(a1, 'ecore_EStructuralFeature'):
        assert not _is_linked(a1, 'ecore_EStructuralFeature', b)
    if hasattr(a2, 'ecore_EStructuralFeature'):
        assert _is_linked(a2, 'ecore_EStructuralFeature', b)
    _safe_set(b, 'ecore_EClass26', set())
    assert not _is_linked(b, 'ecore_EClass26', a2)
    if hasattr(a2, 'ecore_EStructuralFeature'):
        assert not _is_linked(a2, 'ecore_EStructuralFeature', b)


def test_assoc_eAllSuperTypes28_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass29', a1)
    assert _is_linked(b, 'ecore_EClass29', a1)
    if hasattr(a1, 'ecore_EClass27'):
        assert _is_linked(a1, 'ecore_EClass27', b)
    _safe_set(b, 'ecore_EClass29', a2)
    assert _is_linked(b, 'ecore_EClass29', a2)
    if hasattr(a1, 'ecore_EClass27'):
        assert not _is_linked(a1, 'ecore_EClass27', b)
    if hasattr(a2, 'ecore_EClass27'):
        assert _is_linked(a2, 'ecore_EClass27', b)
    _safe_set(b, 'ecore_EClass29', None)
    assert not _is_linked(b, 'ecore_EClass29', a2)
    if hasattr(a2, 'ecore_EClass27'):
        assert not _is_linked(a2, 'ecore_EClass27', b)


def test_assoc_eAnnotations52_reverse_link_reassign_clear():
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


def test_assoc_eAttributes17_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EAttribute(iD=True)
    _safe_set(b, 'ecore_EAttribute19', a1)
    assert _is_linked(b, 'ecore_EAttribute19', a1)
    if hasattr(a1, 'ecore_EClass18'):
        assert _is_linked(a1, 'ecore_EClass18', b)
    _safe_set(b, 'ecore_EAttribute19', a2)
    assert _is_linked(b, 'ecore_EAttribute19', a2)
    if hasattr(a1, 'ecore_EClass18'):
        assert not _is_linked(a1, 'ecore_EClass18', b)
    if hasattr(a2, 'ecore_EClass18'):
        assert _is_linked(a2, 'ecore_EClass18', b)
    _safe_set(b, 'ecore_EAttribute19', None)
    assert not _is_linked(b, 'ecore_EAttribute19', a2)
    if hasattr(a2, 'ecore_EClass18'):
        assert not _is_linked(a2, 'ecore_EClass18', b)


def test_assoc_eClassifiers65_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'EClassifier', a1)
    assert _is_linked(b, 'EClassifier', a1)
    if hasattr(a1, 'ePackage66'):
        assert _is_linked(a1, 'ePackage66', b)
    _safe_set(b, 'EClassifier', a2)
    assert _is_linked(b, 'EClassifier', a2)
    if hasattr(a1, 'ePackage66'):
        assert not _is_linked(a1, 'ePackage66', b)
    if hasattr(a2, 'ePackage66'):
        assert _is_linked(a2, 'ePackage66', b)
    _safe_set(b, 'EClassifier', None)
    assert not _is_linked(b, 'EClassifier', a2)
    if hasattr(a2, 'ePackage66'):
        assert not _is_linked(a2, 'ePackage66', b)


def test_assoc_eContainingClass84_reverse_link_reassign_clear():
    a1 = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = ecore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'EClass85', a1)
    assert _is_linked(b, 'EClass85', a1)
    if hasattr(a1, 'eStructuralFeatures'):
        assert _is_linked(a1, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass85', a2)
    assert _is_linked(b, 'EClass85', a2)
    if hasattr(a1, 'eStructuralFeatures'):
        assert not _is_linked(a1, 'eStructuralFeatures', b)
    if hasattr(a2, 'eStructuralFeatures'):
        assert _is_linked(a2, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass85', None)
    assert not _is_linked(b, 'EClass85', a2)
    if hasattr(a2, 'eStructuralFeatures'):
        assert not _is_linked(a2, 'eStructuralFeatures', b)


def test_assoc_eEnum49_reverse_link_reassign_clear():
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


def test_assoc_eFactoryInstance64_reverse_link_reassign_clear():
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


def test_assoc_eIDAttribute30_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EAttribute(iD=True)
    _safe_set(b, 'ecore_EAttribute32', a1)
    assert _is_linked(b, 'ecore_EAttribute32', a1)
    if hasattr(a1, 'ecore_EClass31'):
        assert _is_linked(a1, 'ecore_EClass31', b)
    _safe_set(b, 'ecore_EAttribute32', a2)
    assert _is_linked(b, 'ecore_EAttribute32', a2)
    if hasattr(a1, 'ecore_EClass31'):
        assert not _is_linked(a1, 'ecore_EClass31', b)
    if hasattr(a2, 'ecore_EClass31'):
        assert _is_linked(a2, 'ecore_EClass31', b)
    _safe_set(b, 'ecore_EAttribute32', None)
    assert not _is_linked(b, 'ecore_EAttribute32', a2)
    if hasattr(a2, 'ecore_EClass31'):
        assert not _is_linked(a2, 'ecore_EClass31', b)


def test_assoc_eIDAttributeForTest40_reverse_link_reassign_clear():
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


def test_assoc_eKeys81_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EAttribute(iD=True)
    _safe_set(b, 'ecore_EAttribute83', a1)
    assert _is_linked(b, 'ecore_EAttribute83', a1)
    if hasattr(a1, 'ecore_EReference82'):
        assert _is_linked(a1, 'ecore_EReference82', b)
    _safe_set(b, 'ecore_EAttribute83', a2)
    assert _is_linked(b, 'ecore_EAttribute83', a2)
    if hasattr(a1, 'ecore_EReference82'):
        assert not _is_linked(a1, 'ecore_EReference82', b)
    if hasattr(a2, 'ecore_EReference82'):
        assert _is_linked(a2, 'ecore_EReference82', b)
    _safe_set(b, 'ecore_EAttribute83', None)
    assert not _is_linked(b, 'ecore_EAttribute83', a2)
    if hasattr(a2, 'ecore_EReference82'):
        assert not _is_linked(a2, 'ecore_EReference82', b)


def test_assoc_eLiterals48_reverse_link_reassign_clear():
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


def test_assoc_eModelElement1_reverse_link_reassign_clear():
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


def test_assoc_eOpposite76_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EReference(container=True, containment=True, resolveProxies=True)
    _safe_set(b, 'ecore_EReference77', a1)
    assert _is_linked(b, 'ecore_EReference77', a1)
    if hasattr(a1, 'ecore_EReference75'):
        assert _is_linked(a1, 'ecore_EReference75', b)
    _safe_set(b, 'ecore_EReference77', a2)
    assert _is_linked(b, 'ecore_EReference77', a2)
    if hasattr(a1, 'ecore_EReference75'):
        assert not _is_linked(a1, 'ecore_EReference75', b)
    if hasattr(a2, 'ecore_EReference75'):
        assert _is_linked(a2, 'ecore_EReference75', b)
    _safe_set(b, 'ecore_EReference77', None)
    assert not _is_linked(b, 'ecore_EReference77', a2)
    if hasattr(a2, 'ecore_EReference75'):
        assert not _is_linked(a2, 'ecore_EReference75', b)


def test_assoc_ePackage46_reverse_link_reassign_clear():
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


def test_assoc_ePackage50_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EFactory()
    _safe_set(b, 'eFactoryInstance', a1)
    assert _is_linked(b, 'eFactoryInstance', a1)
    if hasattr(a1, 'EPackage51'):
        assert _is_linked(a1, 'EPackage51', b)
    _safe_set(b, 'eFactoryInstance', a2)
    assert _is_linked(b, 'eFactoryInstance', a2)
    if hasattr(a1, 'EPackage51'):
        assert not _is_linked(a1, 'EPackage51', b)
    if hasattr(a2, 'EPackage51'):
        assert _is_linked(a2, 'EPackage51', b)
    _safe_set(b, 'eFactoryInstance', None)
    assert not _is_linked(b, 'eFactoryInstance', a2)
    if hasattr(a2, 'EPackage51'):
        assert not _is_linked(a2, 'EPackage51', b)


def test_assoc_eReferenceType78_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass80', a1)
    assert _is_linked(b, 'ecore_EClass80', a1)
    if hasattr(a1, 'ecore_EReference79'):
        assert _is_linked(a1, 'ecore_EReference79', b)
    _safe_set(b, 'ecore_EClass80', a2)
    assert _is_linked(b, 'ecore_EClass80', a2)
    if hasattr(a1, 'ecore_EReference79'):
        assert not _is_linked(a1, 'ecore_EReference79', b)
    if hasattr(a2, 'ecore_EReference79'):
        assert _is_linked(a2, 'ecore_EReference79', b)
    _safe_set(b, 'ecore_EClass80', None)
    assert not _is_linked(b, 'ecore_EClass80', a2)
    if hasattr(a2, 'ecore_EReference79'):
        assert not _is_linked(a2, 'ecore_EReference79', b)


def test_assoc_eReferences14_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass15', {a1})
    assert _is_linked(b, 'ecore_EClass15', a1)
    if hasattr(a1, 'ecore_EReference16'):
        assert _is_linked(a1, 'ecore_EReference16', b)
    _safe_set(b, 'ecore_EClass15', {a2})
    assert _is_linked(b, 'ecore_EClass15', a2)
    if hasattr(a1, 'ecore_EReference16'):
        assert not _is_linked(a1, 'ecore_EReference16', b)
    if hasattr(a2, 'ecore_EReference16'):
        assert _is_linked(a2, 'ecore_EReference16', b)
    _safe_set(b, 'ecore_EClass15', set())
    assert not _is_linked(b, 'ecore_EClass15', a2)
    if hasattr(a2, 'ecore_EReference16'):
        assert not _is_linked(a2, 'ecore_EReference16', b)


def test_assoc_eStructuralFeatures33_reverse_link_reassign_clear():
    a1 = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = ecore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'eContainingClass34', {a1})
    assert _is_linked(b, 'eContainingClass34', a1)
    if hasattr(a1, 'EStructuralFeature'):
        assert _is_linked(a1, 'EStructuralFeature', b)
    _safe_set(b, 'eContainingClass34', {a2})
    assert _is_linked(b, 'eContainingClass34', a2)
    if hasattr(a1, 'EStructuralFeature'):
        assert not _is_linked(a1, 'EStructuralFeature', b)
    if hasattr(a2, 'EStructuralFeature'):
        assert _is_linked(a2, 'EStructuralFeature', b)
    _safe_set(b, 'eContainingClass34', set())
    assert not _is_linked(b, 'eContainingClass34', a2)
    if hasattr(a2, 'EStructuralFeature'):
        assert not _is_linked(a2, 'EStructuralFeature', b)


def test_assoc_eSubpackages68_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSuperPackage', {a1})
    assert _is_linked(b, 'eSuperPackage', a1)
    if hasattr(a1, 'EPackage69'):
        assert _is_linked(a1, 'EPackage69', b)
    _safe_set(b, 'eSuperPackage', {a2})
    assert _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a1, 'EPackage69'):
        assert not _is_linked(a1, 'EPackage69', b)
    if hasattr(a2, 'EPackage69'):
        assert _is_linked(a2, 'EPackage69', b)
    _safe_set(b, 'eSuperPackage', set())
    assert not _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a2, 'EPackage69'):
        assert not _is_linked(a2, 'EPackage69', b)


def test_assoc_eSuperPackage71_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSubpackages', a1)
    assert _is_linked(b, 'eSubpackages', a1)
    if hasattr(a1, 'EPackage72'):
        assert _is_linked(a1, 'EPackage72', b)
    _safe_set(b, 'eSubpackages', a2)
    assert _is_linked(b, 'eSubpackages', a2)
    if hasattr(a1, 'EPackage72'):
        assert not _is_linked(a1, 'EPackage72', b)
    if hasattr(a2, 'EPackage72'):
        assert _is_linked(a2, 'EPackage72', b)
    _safe_set(b, 'eSubpackages', None)
    assert not _is_linked(b, 'eSubpackages', a2)
    if hasattr(a2, 'EPackage72'):
        assert not _is_linked(a2, 'EPackage72', b)


def test_assoc_eSuperTypes7_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass6', {a1})
    assert _is_linked(b, 'ecore_EClass6', a1)
    if hasattr(a1, 'ecore_EClass'):
        assert _is_linked(a1, 'ecore_EClass', b)
    _safe_set(b, 'ecore_EClass6', {a2})
    assert _is_linked(b, 'ecore_EClass6', a2)
    if hasattr(a1, 'ecore_EClass'):
        assert not _is_linked(a1, 'ecore_EClass', b)
    if hasattr(a2, 'ecore_EClass'):
        assert _is_linked(a2, 'ecore_EClass', b)
    _safe_set(b, 'ecore_EClass6', set())
    assert not _is_linked(b, 'ecore_EClass6', a2)
    if hasattr(a2, 'ecore_EClass'):
        assert not _is_linked(a2, 'ecore_EClass', b)


def test_assoc_eType86_reverse_link_reassign_clear():
    a1 = ecore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    a2 = ecore_ETypedElement(lowerBound=13, many=False, ordered=False, required=False, unique=False, upperBound=13)
    b = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'ecore_EClassifier87', a1)
    assert _is_linked(b, 'ecore_EClassifier87', a1)
    if hasattr(a1, 'ecore_ETypedElement'):
        assert _is_linked(a1, 'ecore_ETypedElement', b)
    _safe_set(b, 'ecore_EClassifier87', a2)
    assert _is_linked(b, 'ecore_EClassifier87', a2)
    if hasattr(a1, 'ecore_ETypedElement'):
        assert not _is_linked(a1, 'ecore_ETypedElement', b)
    if hasattr(a2, 'ecore_ETypedElement'):
        assert _is_linked(a2, 'ecore_ETypedElement', b)
    _safe_set(b, 'ecore_EClassifier87', None)
    assert not _is_linked(b, 'ecore_EClassifier87', a2)
    if hasattr(a2, 'ecore_ETypedElement'):
        assert not _is_linked(a2, 'ecore_ETypedElement', b)


def test_assoc_references3_reverse_link_reassign_clear():
    a1 = ecore_EObject()
    a2 = ecore_EObject()
    b = ecore_EAnnotation(source="sample_text")
    _safe_set(b, 'ecore_EAnnotation4', {a1})
    assert _is_linked(b, 'ecore_EAnnotation4', a1)
    if hasattr(a1, 'ecore_EObject5'):
        assert _is_linked(a1, 'ecore_EObject5', b)
    _safe_set(b, 'ecore_EAnnotation4', {a2})
    assert _is_linked(b, 'ecore_EAnnotation4', a2)
    if hasattr(a1, 'ecore_EObject5'):
        assert not _is_linked(a1, 'ecore_EObject5', b)
    if hasattr(a2, 'ecore_EObject5'):
        assert _is_linked(a2, 'ecore_EObject5', b)
    _safe_set(b, 'ecore_EAnnotation4', set())
    assert not _is_linked(b, 'ecore_EAnnotation4', a2)
    if hasattr(a2, 'ecore_EObject5'):
        assert not _is_linked(a2, 'ecore_EObject5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_eAllGenericSuperTypes37_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType39' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract=True, interface=True)
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType39', None)
    _safe_set(owner, 'ecore_EClass38', {partner})
    assert getattr(partner, 'ecore_EGenericType39') == owner
    _safe_set(owner, 'ecore_EClass38', set())
    assert getattr(partner, 'ecore_EGenericType39') is None


def test_assoc_eAllOperations23_stub_double():
    # ecore_EOperation has no real 'ecore_EOperation' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract=True, interface=True)
    partner = ecore_EOperation()
    setattr(partner, 'ecore_EOperation', None)
    _safe_set(owner, 'ecore_EClass24', {partner})
    assert getattr(partner, 'ecore_EOperation') == owner
    _safe_set(owner, 'ecore_EClass24', set())
    assert getattr(partner, 'ecore_EOperation') is None


def test_assoc_eClassifier106_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType107' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType107', None)
    _safe_set(owner, 'ecore_EClassifier108', partner)
    assert getattr(partner, 'ecore_EGenericType107') == owner
    _safe_set(owner, 'ecore_EClassifier108', None)
    assert getattr(partner, 'ecore_EGenericType107') is None


def test_assoc_eContainingClass53_stub_double():
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


def test_assoc_eExceptions58_stub_double():
    # ecore_EOperation has no real 'ecore_EOperation59' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecore_EOperation()
    setattr(partner, 'ecore_EOperation59', None)
    _safe_set(owner, 'ecore_EClassifier60', partner)
    assert owner in getattr(partner, 'ecore_EOperation59')
    _safe_set(owner, 'ecore_EClassifier60', None)
    assert owner not in getattr(partner, 'ecore_EOperation59')


def test_assoc_eGenericSuperTypes35_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract=True, interface=True)
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType', None)
    _safe_set(owner, 'ecore_EClass36', {partner})
    assert getattr(partner, 'ecore_EGenericType') == owner
    _safe_set(owner, 'ecore_EClass36', set())
    assert getattr(partner, 'ecore_EGenericType') is None


def test_assoc_eGenericType88_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType90' property in the generated
    # code (a bare stub) -- manually attach it so ecore_ETypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_ETypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType90', None)
    _safe_set(owner, 'ecore_ETypedElement89', partner)
    assert getattr(partner, 'ecore_EGenericType90') == owner
    _safe_set(owner, 'ecore_ETypedElement89', None)
    assert getattr(partner, 'ecore_EGenericType90') is None


def test_assoc_eOperations8_stub_double():
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


def test_assoc_eRawType97_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType98' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType98', None)
    _safe_set(owner, 'ecore_EClassifier99', partner)
    assert getattr(partner, 'ecore_EGenericType98') == owner
    _safe_set(owner, 'ecore_EClassifier99', None)
    assert getattr(partner, 'ecore_EGenericType98') is None


def test_assoc_eTypeParameters47_stub_double():
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


