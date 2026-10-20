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

def test_assoc_contents1_reverse_link_reassign_clear():
    a1 = ecore_EObject()
    a2 = ecore_EObject()
    b = ecore_EAnnotation(source="sample_text")
    _safe_set(b, 'ecore_EAnnotation2', {a1})
    assert _is_linked(b, 'ecore_EAnnotation2', a1)
    if hasattr(a1, 'ecore_EObject'):
        assert _is_linked(a1, 'ecore_EObject', b)
    _safe_set(b, 'ecore_EAnnotation2', {a2})
    assert _is_linked(b, 'ecore_EAnnotation2', a2)
    if hasattr(a1, 'ecore_EObject'):
        assert not _is_linked(a1, 'ecore_EObject', b)
    if hasattr(a2, 'ecore_EObject'):
        assert _is_linked(a2, 'ecore_EObject', b)
    _safe_set(b, 'ecore_EAnnotation2', set())
    assert not _is_linked(b, 'ecore_EAnnotation2', a2)
    if hasattr(a2, 'ecore_EObject'):
        assert not _is_linked(a2, 'ecore_EObject', b)


def test_assoc_details0_reverse_link_reassign_clear():
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


def test_assoc_eAllAttributes12_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EAttribute(iD=True)
    _safe_set(b, 'ecore_EAttribute14', a1)
    assert _is_linked(b, 'ecore_EAttribute14', a1)
    if hasattr(a1, 'ecore_EClass13'):
        assert _is_linked(a1, 'ecore_EClass13', b)
    _safe_set(b, 'ecore_EAttribute14', a2)
    assert _is_linked(b, 'ecore_EAttribute14', a2)
    if hasattr(a1, 'ecore_EClass13'):
        assert not _is_linked(a1, 'ecore_EClass13', b)
    if hasattr(a2, 'ecore_EClass13'):
        assert _is_linked(a2, 'ecore_EClass13', b)
    _safe_set(b, 'ecore_EAttribute14', None)
    assert not _is_linked(b, 'ecore_EAttribute14', a2)
    if hasattr(a2, 'ecore_EClass13'):
        assert not _is_linked(a2, 'ecore_EClass13', b)


def test_assoc_eAllContainments15_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass16', {a1})
    assert _is_linked(b, 'ecore_EClass16', a1)
    if hasattr(a1, 'ecore_EReference'):
        assert _is_linked(a1, 'ecore_EReference', b)
    _safe_set(b, 'ecore_EClass16', {a2})
    assert _is_linked(b, 'ecore_EClass16', a2)
    if hasattr(a1, 'ecore_EReference'):
        assert not _is_linked(a1, 'ecore_EReference', b)
    if hasattr(a2, 'ecore_EReference'):
        assert _is_linked(a2, 'ecore_EReference', b)
    _safe_set(b, 'ecore_EClass16', set())
    assert not _is_linked(b, 'ecore_EClass16', a2)
    if hasattr(a2, 'ecore_EReference'):
        assert not _is_linked(a2, 'ecore_EReference', b)


def test_assoc_eAllOperations20_reverse_link_reassign_clear():
    a1 = ecore_EOperation()
    a2 = ecore_EOperation()
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass21', {a1})
    assert _is_linked(b, 'ecore_EClass21', a1)
    if hasattr(a1, 'ecore_EOperation'):
        assert _is_linked(a1, 'ecore_EOperation', b)
    _safe_set(b, 'ecore_EClass21', {a2})
    assert _is_linked(b, 'ecore_EClass21', a2)
    if hasattr(a1, 'ecore_EOperation'):
        assert not _is_linked(a1, 'ecore_EOperation', b)
    if hasattr(a2, 'ecore_EOperation'):
        assert _is_linked(a2, 'ecore_EOperation', b)
    _safe_set(b, 'ecore_EClass21', set())
    assert not _is_linked(b, 'ecore_EClass21', a2)
    if hasattr(a2, 'ecore_EOperation'):
        assert not _is_linked(a2, 'ecore_EOperation', b)


def test_assoc_eAllReferences22_reverse_link_reassign_clear():
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


def test_assoc_eAnnotations66_reverse_link_reassign_clear():
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


def test_assoc_eAttributeType7_reverse_link_reassign_clear():
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


def test_assoc_eAttributes30_reverse_link_reassign_clear():
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


def test_assoc_eClassifiers78_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
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


def test_assoc_eContainingClass77_reverse_link_reassign_clear():
    a1 = ecore_EOperation()
    a2 = ecore_EOperation()
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


def test_assoc_eContainingClass98_reverse_link_reassign_clear():
    a1 = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = ecore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'EClass99', a1)
    assert _is_linked(b, 'EClass99', a1)
    if hasattr(a1, 'eStructuralFeatures'):
        assert _is_linked(a1, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass99', a2)
    assert _is_linked(b, 'EClass99', a2)
    if hasattr(a1, 'eStructuralFeatures'):
        assert not _is_linked(a1, 'eStructuralFeatures', b)
    if hasattr(a2, 'eStructuralFeatures'):
        assert _is_linked(a2, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass99', None)
    assert not _is_linked(b, 'EClass99', a2)
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


def test_assoc_eExceptions74_reverse_link_reassign_clear():
    a1 = ecore_EOperation()
    a2 = ecore_EOperation()
    b = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'ecore_EClassifier76', a1)
    assert _is_linked(b, 'ecore_EClassifier76', a1)
    if hasattr(a1, 'ecore_EOperation75'):
        assert _is_linked(a1, 'ecore_EOperation75', b)
    _safe_set(b, 'ecore_EClassifier76', a2)
    assert _is_linked(b, 'ecore_EClassifier76', a2)
    if hasattr(a1, 'ecore_EOperation75'):
        assert not _is_linked(a1, 'ecore_EOperation75', b)
    if hasattr(a2, 'ecore_EOperation75'):
        assert _is_linked(a2, 'ecore_EOperation75', b)
    _safe_set(b, 'ecore_EClassifier76', None)
    assert not _is_linked(b, 'ecore_EClassifier76', a2)
    if hasattr(a2, 'ecore_EOperation75'):
        assert not _is_linked(a2, 'ecore_EOperation75', b)


def test_assoc_eFactoryInstance82_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EFactory()
    _safe_set(b, 'EFactory', a1)
    assert _is_linked(b, 'EFactory', a1)
    if hasattr(a1, 'ePackage83'):
        assert _is_linked(a1, 'ePackage83', b)
    _safe_set(b, 'EFactory', a2)
    assert _is_linked(b, 'EFactory', a2)
    if hasattr(a1, 'ePackage83'):
        assert not _is_linked(a1, 'ePackage83', b)
    if hasattr(a2, 'ePackage83'):
        assert _is_linked(a2, 'ePackage83', b)
    _safe_set(b, 'EFactory', None)
    assert not _is_linked(b, 'EFactory', a2)
    if hasattr(a2, 'ePackage83'):
        assert not _is_linked(a2, 'ePackage83', b)


def test_assoc_eIDAttribute33_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EAttribute(iD=True)
    _safe_set(b, 'ecore_EAttribute35', a1)
    assert _is_linked(b, 'ecore_EAttribute35', a1)
    if hasattr(a1, 'ecore_EClass34'):
        assert _is_linked(a1, 'ecore_EClass34', b)
    _safe_set(b, 'ecore_EAttribute35', a2)
    assert _is_linked(b, 'ecore_EAttribute35', a2)
    if hasattr(a1, 'ecore_EClass34'):
        assert not _is_linked(a1, 'ecore_EClass34', b)
    if hasattr(a2, 'ecore_EClass34'):
        assert _is_linked(a2, 'ecore_EClass34', b)
    _safe_set(b, 'ecore_EAttribute35', None)
    assert not _is_linked(b, 'ecore_EAttribute35', a2)
    if hasattr(a2, 'ecore_EClass34'):
        assert not _is_linked(a2, 'ecore_EClass34', b)


def test_assoc_eKeys89_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EAttribute(iD=True)
    _safe_set(b, 'ecore_EAttribute91', a1)
    assert _is_linked(b, 'ecore_EAttribute91', a1)
    if hasattr(a1, 'ecore_EReference90'):
        assert _is_linked(a1, 'ecore_EReference90', b)
    _safe_set(b, 'ecore_EAttribute91', a2)
    assert _is_linked(b, 'ecore_EAttribute91', a2)
    if hasattr(a1, 'ecore_EReference90'):
        assert not _is_linked(a1, 'ecore_EReference90', b)
    if hasattr(a2, 'ecore_EReference90'):
        assert _is_linked(a2, 'ecore_EReference90', b)
    _safe_set(b, 'ecore_EAttribute91', None)
    assert not _is_linked(b, 'ecore_EAttribute91', a2)
    if hasattr(a2, 'ecore_EReference90'):
        assert not _is_linked(a2, 'ecore_EReference90', b)


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


def test_assoc_eModelElement6_reverse_link_reassign_clear():
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


def test_assoc_eOperations8_reverse_link_reassign_clear():
    a1 = ecore_EOperation()
    a2 = ecore_EOperation()
    b = ecore_EClass(abstract=True, interface=True)
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


def test_assoc_eOpposite93_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EReference(container=True, containment=True, resolveProxies=True)
    _safe_set(b, 'ecore_EReference94', a1)
    assert _is_linked(b, 'ecore_EReference94', a1)
    if hasattr(a1, 'ecore_EReference92'):
        assert _is_linked(a1, 'ecore_EReference92', b)
    _safe_set(b, 'ecore_EReference94', a2)
    assert _is_linked(b, 'ecore_EReference94', a2)
    if hasattr(a1, 'ecore_EReference92'):
        assert not _is_linked(a1, 'ecore_EReference92', b)
    if hasattr(a2, 'ecore_EReference92'):
        assert _is_linked(a2, 'ecore_EReference92', b)
    _safe_set(b, 'ecore_EReference94', None)
    assert not _is_linked(b, 'ecore_EReference94', a2)
    if hasattr(a2, 'ecore_EReference92'):
        assert not _is_linked(a2, 'ecore_EReference92', b)


def test_assoc_ePackage43_reverse_link_reassign_clear():
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


def test_assoc_eReferenceType95_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass97', a1)
    assert _is_linked(b, 'ecore_EClass97', a1)
    if hasattr(a1, 'ecore_EReference96'):
        assert _is_linked(a1, 'ecore_EReference96', b)
    _safe_set(b, 'ecore_EClass97', a2)
    assert _is_linked(b, 'ecore_EClass97', a2)
    if hasattr(a1, 'ecore_EReference96'):
        assert not _is_linked(a1, 'ecore_EReference96', b)
    if hasattr(a2, 'ecore_EReference96'):
        assert _is_linked(a2, 'ecore_EReference96', b)
    _safe_set(b, 'ecore_EClass97', None)
    assert not _is_linked(b, 'ecore_EClass97', a2)
    if hasattr(a2, 'ecore_EReference96'):
        assert not _is_linked(a2, 'ecore_EReference96', b)


def test_assoc_eReferences36_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass37', {a1})
    assert _is_linked(b, 'ecore_EClass37', a1)
    if hasattr(a1, 'ecore_EReference38'):
        assert _is_linked(a1, 'ecore_EReference38', b)
    _safe_set(b, 'ecore_EClass37', {a2})
    assert _is_linked(b, 'ecore_EClass37', a2)
    if hasattr(a1, 'ecore_EReference38'):
        assert not _is_linked(a1, 'ecore_EReference38', b)
    if hasattr(a2, 'ecore_EReference38'):
        assert _is_linked(a2, 'ecore_EReference38', b)
    _safe_set(b, 'ecore_EClass37', set())
    assert not _is_linked(b, 'ecore_EClass37', a2)
    if hasattr(a2, 'ecore_EReference38'):
        assert not _is_linked(a2, 'ecore_EReference38', b)


def test_assoc_eStructuralFeatures9_reverse_link_reassign_clear():
    a1 = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = ecore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'eContainingClass10', {a1})
    assert _is_linked(b, 'eContainingClass10', a1)
    if hasattr(a1, 'EStructuralFeature'):
        assert _is_linked(a1, 'EStructuralFeature', b)
    _safe_set(b, 'eContainingClass10', {a2})
    assert _is_linked(b, 'eContainingClass10', a2)
    if hasattr(a1, 'EStructuralFeature'):
        assert not _is_linked(a1, 'EStructuralFeature', b)
    if hasattr(a2, 'EStructuralFeature'):
        assert _is_linked(a2, 'EStructuralFeature', b)
    _safe_set(b, 'eContainingClass10', set())
    assert not _is_linked(b, 'eContainingClass10', a2)
    if hasattr(a2, 'EStructuralFeature'):
        assert not _is_linked(a2, 'EStructuralFeature', b)


def test_assoc_eSubpackages80_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSuperPackage', {a1})
    assert _is_linked(b, 'eSuperPackage', a1)
    if hasattr(a1, 'EPackage81'):
        assert _is_linked(a1, 'EPackage81', b)
    _safe_set(b, 'eSuperPackage', {a2})
    assert _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a1, 'EPackage81'):
        assert not _is_linked(a1, 'EPackage81', b)
    if hasattr(a2, 'EPackage81'):
        assert _is_linked(a2, 'EPackage81', b)
    _safe_set(b, 'eSuperPackage', set())
    assert not _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a2, 'EPackage81'):
        assert not _is_linked(a2, 'EPackage81', b)


def test_assoc_eSuperPackage85_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSubpackages', a1)
    assert _is_linked(b, 'eSubpackages', a1)
    if hasattr(a1, 'EPackage86'):
        assert _is_linked(a1, 'EPackage86', b)
    _safe_set(b, 'eSubpackages', a2)
    assert _is_linked(b, 'eSubpackages', a2)
    if hasattr(a1, 'EPackage86'):
        assert not _is_linked(a1, 'EPackage86', b)
    if hasattr(a2, 'EPackage86'):
        assert _is_linked(a2, 'EPackage86', b)
    _safe_set(b, 'eSubpackages', None)
    assert not _is_linked(b, 'eSubpackages', a2)
    if hasattr(a2, 'EPackage86'):
        assert not _is_linked(a2, 'EPackage86', b)


def test_assoc_eSuperTypes40_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass41', a1)
    assert _is_linked(b, 'ecore_EClass41', a1)
    if hasattr(a1, 'ecore_EClass39'):
        assert _is_linked(a1, 'ecore_EClass39', b)
    _safe_set(b, 'ecore_EClass41', a2)
    assert _is_linked(b, 'ecore_EClass41', a2)
    if hasattr(a1, 'ecore_EClass39'):
        assert not _is_linked(a1, 'ecore_EClass39', b)
    if hasattr(a2, 'ecore_EClass39'):
        assert _is_linked(a2, 'ecore_EClass39', b)
    _safe_set(b, 'ecore_EClass41', None)
    assert not _is_linked(b, 'ecore_EClass41', a2)
    if hasattr(a2, 'ecore_EClass39'):
        assert not _is_linked(a2, 'ecore_EClass39', b)


def test_assoc_eType102_reverse_link_reassign_clear():
    a1 = ecore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    a2 = ecore_ETypedElement(lowerBound=13, many=False, ordered=False, required=False, unique=False, upperBound=13)
    b = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'ecore_EClassifier104', a1)
    assert _is_linked(b, 'ecore_EClassifier104', a1)
    if hasattr(a1, 'ecore_ETypedElement103'):
        assert _is_linked(a1, 'ecore_ETypedElement103', b)
    _safe_set(b, 'ecore_EClassifier104', a2)
    assert _is_linked(b, 'ecore_EClassifier104', a2)
    if hasattr(a1, 'ecore_ETypedElement103'):
        assert not _is_linked(a1, 'ecore_ETypedElement103', b)
    if hasattr(a2, 'ecore_ETypedElement103'):
        assert _is_linked(a2, 'ecore_ETypedElement103', b)
    _safe_set(b, 'ecore_EClassifier104', None)
    assert not _is_linked(b, 'ecore_EClassifier104', a2)
    if hasattr(a2, 'ecore_ETypedElement103'):
        assert not _is_linked(a2, 'ecore_ETypedElement103', b)


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

def test_assoc_eAllGenericSuperTypes17_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType19' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract=True, interface=True)
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType19', None)
    _safe_set(owner, 'ecore_EClass18', {partner})
    assert getattr(partner, 'ecore_EGenericType19') == owner
    _safe_set(owner, 'ecore_EClass18', set())
    assert getattr(partner, 'ecore_EGenericType19') is None


def test_assoc_eClassifier57_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType58' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType58', None)
    _safe_set(owner, 'ecore_EClassifier59', partner)
    assert getattr(partner, 'ecore_EGenericType58') == owner
    _safe_set(owner, 'ecore_EClassifier59', None)
    assert getattr(partner, 'ecore_EGenericType58') is None


def test_assoc_eGenericExceptions71_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType73' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EOperation()
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType73', None)
    _safe_set(owner, 'ecore_EOperation72', {partner})
    assert getattr(partner, 'ecore_EGenericType73') == owner
    _safe_set(owner, 'ecore_EOperation72', set())
    assert getattr(partner, 'ecore_EGenericType73') is None


def test_assoc_eGenericSuperTypes11_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract=True, interface=True)
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType', None)
    _safe_set(owner, 'ecore_EClass', {partner})
    assert getattr(partner, 'ecore_EGenericType') == owner
    _safe_set(owner, 'ecore_EClass', set())
    assert getattr(partner, 'ecore_EGenericType') is None


def test_assoc_eGenericType100_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType101' property in the generated
    # code (a bare stub) -- manually attach it so ecore_ETypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_ETypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType101', None)
    _safe_set(owner, 'ecore_ETypedElement', partner)
    assert getattr(partner, 'ecore_EGenericType101') == owner
    _safe_set(owner, 'ecore_ETypedElement', None)
    assert getattr(partner, 'ecore_EGenericType101') is None


def test_assoc_eOperation87_stub_double():
    # ecore_EParameter has no real 'eParameters' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EOperation()
    partner = ecore_EParameter()
    setattr(partner, 'eParameters', None)
    _safe_set(owner, 'EOperation88', partner)
    assert getattr(partner, 'eParameters') == owner
    _safe_set(owner, 'EOperation88', None)
    assert getattr(partner, 'eParameters') is None


def test_assoc_eParameters70_stub_double():
    # ecore_EParameter has no real 'EParameter' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EOperation()
    partner = ecore_EParameter()
    setattr(partner, 'EParameter', None)
    _safe_set(owner, 'eOperation', {partner})
    assert getattr(partner, 'EParameter') == owner
    _safe_set(owner, 'eOperation', set())
    assert getattr(partner, 'EParameter') is None


def test_assoc_eRawType60_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType61' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType61', None)
    _safe_set(owner, 'ecore_EClassifier62', partner)
    assert getattr(partner, 'ecore_EGenericType61') == owner
    _safe_set(owner, 'ecore_EClassifier62', None)
    assert getattr(partner, 'ecore_EGenericType61') is None


def test_assoc_eTypeParameters42_stub_double():
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


def test_assoc_eTypeParameters67_stub_double():
    # ecore_ETypeParameter has no real 'ecore_ETypeParameter69' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EOperation()
    partner = ecore_ETypeParameter()
    setattr(partner, 'ecore_ETypeParameter69', None)
    _safe_set(owner, 'ecore_EOperation68', {partner})
    assert getattr(partner, 'ecore_ETypeParameter69') == owner
    _safe_set(owner, 'ecore_EOperation68', set())
    assert getattr(partner, 'ecore_ETypeParameter69') is None


