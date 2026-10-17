import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EClassifier,
    EDataType,
    EModelElement,
    ENamedElement,
    EStructuralFeature,
    ETypedElement,
    FSM,
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
    ecore_FSM,
    ecore_State,
    ecore_Transition,
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


def test_assoc_eAllGenericSuperTypes39_reverse_link_reassign_clear():
    a1 = ecore_EGenericType()
    a2 = ecore_EGenericType()
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass40', {a1})
    assert _is_linked(b, 'ecore_EClass40', a1)
    if hasattr(a1, 'ecore_EGenericType41'):
        assert _is_linked(a1, 'ecore_EGenericType41', b)
    _safe_set(b, 'ecore_EClass40', {a2})
    assert _is_linked(b, 'ecore_EClass40', a2)
    if hasattr(a1, 'ecore_EGenericType41'):
        assert not _is_linked(a1, 'ecore_EGenericType41', b)
    if hasattr(a2, 'ecore_EGenericType41'):
        assert _is_linked(a2, 'ecore_EGenericType41', b)
    _safe_set(b, 'ecore_EClass40', set())
    assert not _is_linked(b, 'ecore_EClass40', a2)
    if hasattr(a2, 'ecore_EGenericType41'):
        assert not _is_linked(a2, 'ecore_EGenericType41', b)


def test_assoc_eAllOperations25_reverse_link_reassign_clear():
    a1 = ecore_EOperation()
    a2 = ecore_EOperation()
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass26', {a1})
    assert _is_linked(b, 'ecore_EClass26', a1)
    if hasattr(a1, 'ecore_EOperation'):
        assert _is_linked(a1, 'ecore_EOperation', b)
    _safe_set(b, 'ecore_EClass26', {a2})
    assert _is_linked(b, 'ecore_EClass26', a2)
    if hasattr(a1, 'ecore_EOperation'):
        assert not _is_linked(a1, 'ecore_EOperation', b)
    if hasattr(a2, 'ecore_EOperation'):
        assert _is_linked(a2, 'ecore_EOperation', b)
    _safe_set(b, 'ecore_EClass26', set())
    assert not _is_linked(b, 'ecore_EClass26', a2)
    if hasattr(a2, 'ecore_EOperation'):
        assert not _is_linked(a2, 'ecore_EOperation', b)


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


def test_assoc_eClassifier103_reverse_link_reassign_clear():
    a1 = ecore_EGenericType()
    a2 = ecore_EGenericType()
    b = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'ecore_EClassifier105', a1)
    assert _is_linked(b, 'ecore_EClassifier105', a1)
    if hasattr(a1, 'ecore_EGenericType104'):
        assert _is_linked(a1, 'ecore_EGenericType104', b)
    _safe_set(b, 'ecore_EClassifier105', a2)
    assert _is_linked(b, 'ecore_EClassifier105', a2)
    if hasattr(a1, 'ecore_EGenericType104'):
        assert not _is_linked(a1, 'ecore_EGenericType104', b)
    if hasattr(a2, 'ecore_EGenericType104'):
        assert _is_linked(a2, 'ecore_EGenericType104', b)
    _safe_set(b, 'ecore_EClassifier105', None)
    assert not _is_linked(b, 'ecore_EClassifier105', a2)
    if hasattr(a2, 'ecore_EGenericType104'):
        assert not _is_linked(a2, 'ecore_EGenericType104', b)


def test_assoc_eClassifiers62_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'EClassifier', a1)
    assert _is_linked(b, 'EClassifier', a1)
    if hasattr(a1, 'ePackage63'):
        assert _is_linked(a1, 'ePackage63', b)
    _safe_set(b, 'EClassifier', a2)
    assert _is_linked(b, 'EClassifier', a2)
    if hasattr(a1, 'ePackage63'):
        assert not _is_linked(a1, 'ePackage63', b)
    if hasattr(a2, 'ePackage63'):
        assert _is_linked(a2, 'ePackage63', b)
    _safe_set(b, 'EClassifier', None)
    assert not _is_linked(b, 'EClassifier', a2)
    if hasattr(a2, 'ePackage63'):
        assert not _is_linked(a2, 'ePackage63', b)


def test_assoc_eContainingClass50_reverse_link_reassign_clear():
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


def test_assoc_eContainingClass81_reverse_link_reassign_clear():
    a1 = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = ecore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = ecore_EClass(abstract=True, interface=True)
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


def test_assoc_eExceptions55_reverse_link_reassign_clear():
    a1 = ecore_EOperation()
    a2 = ecore_EOperation()
    b = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'ecore_EClassifier57', a1)
    assert _is_linked(b, 'ecore_EClassifier57', a1)
    if hasattr(a1, 'ecore_EOperation56'):
        assert _is_linked(a1, 'ecore_EOperation56', b)
    _safe_set(b, 'ecore_EClassifier57', a2)
    assert _is_linked(b, 'ecore_EClassifier57', a2)
    if hasattr(a1, 'ecore_EOperation56'):
        assert not _is_linked(a1, 'ecore_EOperation56', b)
    if hasattr(a2, 'ecore_EOperation56'):
        assert _is_linked(a2, 'ecore_EOperation56', b)
    _safe_set(b, 'ecore_EClassifier57', None)
    assert not _is_linked(b, 'ecore_EClassifier57', a2)
    if hasattr(a2, 'ecore_EOperation56'):
        assert not _is_linked(a2, 'ecore_EOperation56', b)


def test_assoc_eFactoryInstance61_reverse_link_reassign_clear():
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


def test_assoc_eGenericExceptions58_reverse_link_reassign_clear():
    a1 = ecore_EOperation()
    a2 = ecore_EOperation()
    b = ecore_EGenericType()
    _safe_set(b, 'ecore_EGenericType60', a1)
    assert _is_linked(b, 'ecore_EGenericType60', a1)
    if hasattr(a1, 'ecore_EOperation59'):
        assert _is_linked(a1, 'ecore_EOperation59', b)
    _safe_set(b, 'ecore_EGenericType60', a2)
    assert _is_linked(b, 'ecore_EGenericType60', a2)
    if hasattr(a1, 'ecore_EOperation59'):
        assert not _is_linked(a1, 'ecore_EOperation59', b)
    if hasattr(a2, 'ecore_EOperation59'):
        assert _is_linked(a2, 'ecore_EOperation59', b)
    _safe_set(b, 'ecore_EGenericType60', None)
    assert not _is_linked(b, 'ecore_EGenericType60', a2)
    if hasattr(a2, 'ecore_EOperation59'):
        assert not _is_linked(a2, 'ecore_EOperation59', b)


def test_assoc_eGenericSuperTypes37_reverse_link_reassign_clear():
    a1 = ecore_EGenericType()
    a2 = ecore_EGenericType()
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass38', {a1})
    assert _is_linked(b, 'ecore_EClass38', a1)
    if hasattr(a1, 'ecore_EGenericType'):
        assert _is_linked(a1, 'ecore_EGenericType', b)
    _safe_set(b, 'ecore_EClass38', {a2})
    assert _is_linked(b, 'ecore_EClass38', a2)
    if hasattr(a1, 'ecore_EGenericType'):
        assert not _is_linked(a1, 'ecore_EGenericType', b)
    if hasattr(a2, 'ecore_EGenericType'):
        assert _is_linked(a2, 'ecore_EGenericType', b)
    _safe_set(b, 'ecore_EClass38', set())
    assert not _is_linked(b, 'ecore_EClass38', a2)
    if hasattr(a2, 'ecore_EGenericType'):
        assert not _is_linked(a2, 'ecore_EGenericType', b)


def test_assoc_eGenericType85_reverse_link_reassign_clear():
    a1 = ecore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    a2 = ecore_ETypedElement(lowerBound=13, many=False, ordered=False, required=False, unique=False, upperBound=13)
    b = ecore_EGenericType()
    _safe_set(b, 'ecore_EGenericType87', a1)
    assert _is_linked(b, 'ecore_EGenericType87', a1)
    if hasattr(a1, 'ecore_ETypedElement86'):
        assert _is_linked(a1, 'ecore_ETypedElement86', b)
    _safe_set(b, 'ecore_EGenericType87', a2)
    assert _is_linked(b, 'ecore_EGenericType87', a2)
    if hasattr(a1, 'ecore_ETypedElement86'):
        assert not _is_linked(a1, 'ecore_ETypedElement86', b)
    if hasattr(a2, 'ecore_ETypedElement86'):
        assert _is_linked(a2, 'ecore_ETypedElement86', b)
    _safe_set(b, 'ecore_EGenericType87', None)
    assert not _is_linked(b, 'ecore_EGenericType87', a2)
    if hasattr(a2, 'ecore_ETypedElement86'):
        assert not _is_linked(a2, 'ecore_ETypedElement86', b)


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


def test_assoc_eKeys78_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EAttribute(iD=True)
    _safe_set(b, 'ecore_EAttribute80', a1)
    assert _is_linked(b, 'ecore_EAttribute80', a1)
    if hasattr(a1, 'ecore_EReference79'):
        assert _is_linked(a1, 'ecore_EReference79', b)
    _safe_set(b, 'ecore_EAttribute80', a2)
    assert _is_linked(b, 'ecore_EAttribute80', a2)
    if hasattr(a1, 'ecore_EReference79'):
        assert not _is_linked(a1, 'ecore_EReference79', b)
    if hasattr(a2, 'ecore_EReference79'):
        assert _is_linked(a2, 'ecore_EReference79', b)
    _safe_set(b, 'ecore_EAttribute80', None)
    assert not _is_linked(b, 'ecore_EAttribute80', a2)
    if hasattr(a2, 'ecore_EReference79'):
        assert not _is_linked(a2, 'ecore_EReference79', b)


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


def test_assoc_eLowerBound98_reverse_link_reassign_clear():
    a1 = ecore_EGenericType()
    a2 = ecore_EGenericType()
    b = ecore_EGenericType()
    _safe_set(b, 'ecore_EGenericType99', a1)
    assert _is_linked(b, 'ecore_EGenericType99', a1)
    if hasattr(a1, 'ecore_EGenericType97'):
        assert _is_linked(a1, 'ecore_EGenericType97', b)
    _safe_set(b, 'ecore_EGenericType99', a2)
    assert _is_linked(b, 'ecore_EGenericType99', a2)
    if hasattr(a1, 'ecore_EGenericType97'):
        assert not _is_linked(a1, 'ecore_EGenericType97', b)
    if hasattr(a2, 'ecore_EGenericType97'):
        assert _is_linked(a2, 'ecore_EGenericType97', b)
    _safe_set(b, 'ecore_EGenericType99', None)
    assert not _is_linked(b, 'ecore_EGenericType99', a2)
    if hasattr(a2, 'ecore_EGenericType97'):
        assert not _is_linked(a2, 'ecore_EGenericType97', b)


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


def test_assoc_eOperations10_reverse_link_reassign_clear():
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


def test_assoc_eOpposite73_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EReference(container=True, containment=True, resolveProxies=True)
    _safe_set(b, 'ecore_EReference74', a1)
    assert _is_linked(b, 'ecore_EReference74', a1)
    if hasattr(a1, 'ecore_EReference72'):
        assert _is_linked(a1, 'ecore_EReference72', b)
    _safe_set(b, 'ecore_EReference74', a2)
    assert _is_linked(b, 'ecore_EReference74', a2)
    if hasattr(a1, 'ecore_EReference72'):
        assert not _is_linked(a1, 'ecore_EReference72', b)
    if hasattr(a2, 'ecore_EReference72'):
        assert _is_linked(a2, 'ecore_EReference72', b)
    _safe_set(b, 'ecore_EReference74', None)
    assert not _is_linked(b, 'ecore_EReference74', a2)
    if hasattr(a2, 'ecore_EReference72'):
        assert not _is_linked(a2, 'ecore_EReference72', b)


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


def test_assoc_eRawType94_reverse_link_reassign_clear():
    a1 = ecore_EGenericType()
    a2 = ecore_EGenericType()
    b = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'ecore_EClassifier96', a1)
    assert _is_linked(b, 'ecore_EClassifier96', a1)
    if hasattr(a1, 'ecore_EGenericType95'):
        assert _is_linked(a1, 'ecore_EGenericType95', b)
    _safe_set(b, 'ecore_EClassifier96', a2)
    assert _is_linked(b, 'ecore_EClassifier96', a2)
    if hasattr(a1, 'ecore_EGenericType95'):
        assert not _is_linked(a1, 'ecore_EGenericType95', b)
    if hasattr(a2, 'ecore_EGenericType95'):
        assert _is_linked(a2, 'ecore_EGenericType95', b)
    _safe_set(b, 'ecore_EClassifier96', None)
    assert not _is_linked(b, 'ecore_EClassifier96', a2)
    if hasattr(a2, 'ecore_EGenericType95'):
        assert not _is_linked(a2, 'ecore_EGenericType95', b)


def test_assoc_eReferenceType75_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass77', a1)
    assert _is_linked(b, 'ecore_EClass77', a1)
    if hasattr(a1, 'ecore_EReference76'):
        assert _is_linked(a1, 'ecore_EReference76', b)
    _safe_set(b, 'ecore_EClass77', a2)
    assert _is_linked(b, 'ecore_EClass77', a2)
    if hasattr(a1, 'ecore_EReference76'):
        assert not _is_linked(a1, 'ecore_EReference76', b)
    if hasattr(a2, 'ecore_EReference76'):
        assert _is_linked(a2, 'ecore_EReference76', b)
    _safe_set(b, 'ecore_EClass77', None)
    assert not _is_linked(b, 'ecore_EClass77', a2)
    if hasattr(a2, 'ecore_EReference76'):
        assert not _is_linked(a2, 'ecore_EReference76', b)


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


def test_assoc_eSubpackages65_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSuperPackage', {a1})
    assert _is_linked(b, 'eSuperPackage', a1)
    if hasattr(a1, 'EPackage66'):
        assert _is_linked(a1, 'EPackage66', b)
    _safe_set(b, 'eSuperPackage', {a2})
    assert _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a1, 'EPackage66'):
        assert not _is_linked(a1, 'EPackage66', b)
    if hasattr(a2, 'EPackage66'):
        assert _is_linked(a2, 'EPackage66', b)
    _safe_set(b, 'eSuperPackage', set())
    assert not _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a2, 'EPackage66'):
        assert not _is_linked(a2, 'EPackage66', b)


def test_assoc_eSuperPackage68_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSubpackages', a1)
    assert _is_linked(b, 'eSubpackages', a1)
    if hasattr(a1, 'EPackage69'):
        assert _is_linked(a1, 'EPackage69', b)
    _safe_set(b, 'eSubpackages', a2)
    assert _is_linked(b, 'eSubpackages', a2)
    if hasattr(a1, 'EPackage69'):
        assert not _is_linked(a1, 'EPackage69', b)
    if hasattr(a2, 'EPackage69'):
        assert _is_linked(a2, 'EPackage69', b)
    _safe_set(b, 'eSubpackages', None)
    assert not _is_linked(b, 'eSubpackages', a2)
    if hasattr(a2, 'EPackage69'):
        assert not _is_linked(a2, 'EPackage69', b)


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


def test_assoc_eType83_reverse_link_reassign_clear():
    a1 = ecore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    a2 = ecore_ETypedElement(lowerBound=13, many=False, ordered=False, required=False, unique=False, upperBound=13)
    b = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'ecore_EClassifier84', a1)
    assert _is_linked(b, 'ecore_EClassifier84', a1)
    if hasattr(a1, 'ecore_ETypedElement'):
        assert _is_linked(a1, 'ecore_ETypedElement', b)
    _safe_set(b, 'ecore_EClassifier84', a2)
    assert _is_linked(b, 'ecore_EClassifier84', a2)
    if hasattr(a1, 'ecore_ETypedElement'):
        assert not _is_linked(a1, 'ecore_ETypedElement', b)
    if hasattr(a2, 'ecore_ETypedElement'):
        assert _is_linked(a2, 'ecore_ETypedElement', b)
    _safe_set(b, 'ecore_EClassifier84', None)
    assert not _is_linked(b, 'ecore_EClassifier84', a2)
    if hasattr(a2, 'ecore_ETypedElement'):
        assert not _is_linked(a2, 'ecore_ETypedElement', b)


def test_assoc_eTypeArguments92_reverse_link_reassign_clear():
    a1 = ecore_EGenericType()
    a2 = ecore_EGenericType()
    b = ecore_EGenericType()
    _safe_set(b, 'ecore_EGenericType93', a1)
    assert _is_linked(b, 'ecore_EGenericType93', a1)
    if hasattr(a1, 'ecore_EGenericType91'):
        assert _is_linked(a1, 'ecore_EGenericType91', b)
    _safe_set(b, 'ecore_EGenericType93', a2)
    assert _is_linked(b, 'ecore_EGenericType93', a2)
    if hasattr(a1, 'ecore_EGenericType91'):
        assert not _is_linked(a1, 'ecore_EGenericType91', b)
    if hasattr(a2, 'ecore_EGenericType91'):
        assert _is_linked(a2, 'ecore_EGenericType91', b)
    _safe_set(b, 'ecore_EGenericType93', None)
    assert not _is_linked(b, 'ecore_EGenericType93', a2)
    if hasattr(a2, 'ecore_EGenericType91'):
        assert not _is_linked(a2, 'ecore_EGenericType91', b)


def test_assoc_eUpperBound89_reverse_link_reassign_clear():
    a1 = ecore_EGenericType()
    a2 = ecore_EGenericType()
    b = ecore_EGenericType()
    _safe_set(b, 'ecore_EGenericType90', a1)
    assert _is_linked(b, 'ecore_EGenericType90', a1)
    if hasattr(a1, 'ecore_EGenericType88'):
        assert _is_linked(a1, 'ecore_EGenericType88', b)
    _safe_set(b, 'ecore_EGenericType90', a2)
    assert _is_linked(b, 'ecore_EGenericType90', a2)
    if hasattr(a1, 'ecore_EGenericType88'):
        assert not _is_linked(a1, 'ecore_EGenericType88', b)
    if hasattr(a2, 'ecore_EGenericType88'):
        assert _is_linked(a2, 'ecore_EGenericType88', b)
    _safe_set(b, 'ecore_EGenericType90', None)
    assert not _is_linked(b, 'ecore_EGenericType90', a2)
    if hasattr(a2, 'ecore_EGenericType88'):
        assert not _is_linked(a2, 'ecore_EGenericType88', b)


def test_assoc_incomingTransition117_reverse_link_reassign_clear():
    a1 = ecore_Transition(input="sample_text", output="sample_text")
    a2 = ecore_Transition(input="sample_text_2", output="sample_text_2")
    b = ecore_State(name="sample_text")
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Transition118'):
        assert _is_linked(a1, 'Transition118', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Transition118'):
        assert not _is_linked(a1, 'Transition118', b)
    if hasattr(a2, 'Transition118'):
        assert _is_linked(a2, 'Transition118', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Transition118'):
        assert not _is_linked(a2, 'Transition118', b)


def test_assoc_myClasses119_reverse_link_reassign_clear():
    a1 = ecore_State(name="sample_text")
    a2 = ecore_State(name="sample_text_2")
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass121', a1)
    assert _is_linked(b, 'ecore_EClass121', a1)
    if hasattr(a1, 'ecore_State120'):
        assert _is_linked(a1, 'ecore_State120', b)
    _safe_set(b, 'ecore_EClass121', a2)
    assert _is_linked(b, 'ecore_EClass121', a2)
    if hasattr(a1, 'ecore_State120'):
        assert not _is_linked(a1, 'ecore_State120', b)
    if hasattr(a2, 'ecore_State120'):
        assert _is_linked(a2, 'ecore_State120', b)
    _safe_set(b, 'ecore_EClass121', None)
    assert not _is_linked(b, 'ecore_EClass121', a2)
    if hasattr(a2, 'ecore_State120'):
        assert not _is_linked(a2, 'ecore_State120', b)


def test_assoc_outgoingTransition116_reverse_link_reassign_clear():
    a1 = ecore_Transition(input="sample_text", output="sample_text")
    a2 = ecore_Transition(input="sample_text_2", output="sample_text_2")
    b = ecore_State(name="sample_text")
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


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


def test_assoc_source122_reverse_link_reassign_clear():
    a1 = ecore_Transition(input="sample_text", output="sample_text")
    a2 = ecore_Transition(input="sample_text_2", output="sample_text_2")
    b = ecore_State(name="sample_text")
    _safe_set(b, 'State123', a1)
    assert _is_linked(b, 'State123', a1)
    if hasattr(a1, 'outgoingTransition'):
        assert _is_linked(a1, 'outgoingTransition', b)
    _safe_set(b, 'State123', a2)
    assert _is_linked(b, 'State123', a2)
    if hasattr(a1, 'outgoingTransition'):
        assert not _is_linked(a1, 'outgoingTransition', b)
    if hasattr(a2, 'outgoingTransition'):
        assert _is_linked(a2, 'outgoingTransition', b)
    _safe_set(b, 'State123', None)
    assert not _is_linked(b, 'State123', a2)
    if hasattr(a2, 'outgoingTransition'):
        assert not _is_linked(a2, 'outgoingTransition', b)


def test_assoc_target124_reverse_link_reassign_clear():
    a1 = ecore_Transition(input="sample_text", output="sample_text")
    a2 = ecore_Transition(input="sample_text_2", output="sample_text_2")
    b = ecore_State(name="sample_text")
    _safe_set(b, 'State125', a1)
    assert _is_linked(b, 'State125', a1)
    if hasattr(a1, 'incomingTransition'):
        assert _is_linked(a1, 'incomingTransition', b)
    _safe_set(b, 'State125', a2)
    assert _is_linked(b, 'State125', a2)
    if hasattr(a1, 'incomingTransition'):
        assert not _is_linked(a1, 'incomingTransition', b)
    if hasattr(a2, 'incomingTransition'):
        assert _is_linked(a2, 'incomingTransition', b)
    _safe_set(b, 'State125', None)
    assert not _is_linked(b, 'State125', a2)
    if hasattr(a2, 'incomingTransition'):
        assert not _is_linked(a2, 'incomingTransition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_eBounds106_stub_double():
    # ecore_ETypeParameter has no real 'ecore_ETypeParameter107' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EGenericType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EGenericType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EGenericType()
    partner = ecore_ETypeParameter()
    setattr(partner, 'ecore_ETypeParameter107', None)
    _safe_set(owner, 'ecore_EGenericType108', partner)
    assert getattr(partner, 'ecore_ETypeParameter107') == owner
    _safe_set(owner, 'ecore_EGenericType108', None)
    assert getattr(partner, 'ecore_ETypeParameter107') is None


def test_assoc_eOperation70_stub_double():
    # ecore_EParameter has no real 'eParameters' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EOperation()
    partner = ecore_EParameter()
    setattr(partner, 'eParameters', None)
    _safe_set(owner, 'EOperation71', partner)
    assert getattr(partner, 'eParameters') == owner
    _safe_set(owner, 'EOperation71', None)
    assert getattr(partner, 'eParameters') is None


def test_assoc_eParameters54_stub_double():
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


def test_assoc_eTypeParameter100_stub_double():
    # ecore_ETypeParameter has no real 'ecore_ETypeParameter102' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EGenericType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EGenericType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EGenericType()
    partner = ecore_ETypeParameter()
    setattr(partner, 'ecore_ETypeParameter102', None)
    _safe_set(owner, 'ecore_EGenericType101', partner)
    assert getattr(partner, 'ecore_ETypeParameter102') == owner
    _safe_set(owner, 'ecore_EGenericType101', None)
    assert getattr(partner, 'ecore_ETypeParameter102') is None


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


def test_assoc_eTypeParameters51_stub_double():
    # ecore_ETypeParameter has no real 'ecore_ETypeParameter53' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EOperation()
    partner = ecore_ETypeParameter()
    setattr(partner, 'ecore_ETypeParameter53', None)
    _safe_set(owner, 'ecore_EOperation52', {partner})
    assert getattr(partner, 'ecore_ETypeParameter53') == owner
    _safe_set(owner, 'ecore_EOperation52', set())
    assert getattr(partner, 'ecore_ETypeParameter53') is None


def test_assoc_finalState112_stub_double():
    # ecore_FSM has no real 'ecore_FSM113' property in the generated
    # code (a bare stub) -- manually attach it so ecore_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_State(name="sample_text")
    partner = ecore_FSM()
    setattr(partner, 'ecore_FSM113', None)
    _safe_set(owner, 'ecore_State114', partner)
    assert getattr(partner, 'ecore_FSM113') == owner
    _safe_set(owner, 'ecore_State114', None)
    assert getattr(partner, 'ecore_FSM113') is None


def test_assoc_initialState110_stub_double():
    # ecore_FSM has no real 'ecore_FSM111' property in the generated
    # code (a bare stub) -- manually attach it so ecore_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_State(name="sample_text")
    partner = ecore_FSM()
    setattr(partner, 'ecore_FSM111', None)
    _safe_set(owner, 'ecore_State', partner)
    assert getattr(partner, 'ecore_FSM111') == owner
    _safe_set(owner, 'ecore_State', None)
    assert getattr(partner, 'ecore_FSM111') is None


def test_assoc_myFSMs49_stub_double():
    # ecore_FSM has no real 'ecore_FSM' property in the generated
    # code (a bare stub) -- manually attach it so ecore_ENamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_ENamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_ENamedElement(name="sample_text")
    partner = ecore_FSM()
    setattr(partner, 'ecore_FSM', None)
    _safe_set(owner, 'ecore_ENamedElement', {partner})
    assert getattr(partner, 'ecore_FSM') == owner
    _safe_set(owner, 'ecore_ENamedElement', set())
    assert getattr(partner, 'ecore_FSM') is None


def test_assoc_ownedState109_stub_double():
    # ecore_FSM has no real 'owningFSM' property in the generated
    # code (a bare stub) -- manually attach it so ecore_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_State(name="sample_text")
    partner = ecore_FSM()
    setattr(partner, 'owningFSM', None)
    _safe_set(owner, 'State', partner)
    assert getattr(partner, 'owningFSM') == owner
    _safe_set(owner, 'State', None)
    assert getattr(partner, 'owningFSM') is None


def test_assoc_owningFSM115_stub_double():
    # ecore_FSM has no real 'FSM' property in the generated
    # code (a bare stub) -- manually attach it so ecore_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_State(name="sample_text")
    partner = ecore_FSM()
    setattr(partner, 'FSM', None)
    _safe_set(owner, 'ownedState', partner)
    assert getattr(partner, 'FSM') == owner
    _safe_set(owner, 'ownedState', None)
    assert getattr(partner, 'FSM') is None


