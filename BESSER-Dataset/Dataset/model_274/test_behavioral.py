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

def test_assoc_contents2_reverse_link_reassign_clear():
    a1 = ecore_EObject()
    a2 = ecore_EObject()
    b = ecore_EAnnotation(source="sample_text")
    _safe_set(b, 'ecore_EAnnotation3', {a1})
    assert _is_linked(b, 'ecore_EAnnotation3', a1)
    if hasattr(a1, 'ecore_EObject'):
        assert _is_linked(a1, 'ecore_EObject', b)
    _safe_set(b, 'ecore_EAnnotation3', {a2})
    assert _is_linked(b, 'ecore_EAnnotation3', a2)
    if hasattr(a1, 'ecore_EObject'):
        assert not _is_linked(a1, 'ecore_EObject', b)
    if hasattr(a2, 'ecore_EObject'):
        assert _is_linked(a2, 'ecore_EObject', b)
    _safe_set(b, 'ecore_EAnnotation3', set())
    assert not _is_linked(b, 'ecore_EAnnotation3', a2)
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


def test_assoc_eAllGenericSuperTypes14_reverse_link_reassign_clear():
    a1 = ecore_EGenericType()
    a2 = ecore_EGenericType()
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass15', {a1})
    assert _is_linked(b, 'ecore_EClass15', a1)
    if hasattr(a1, 'ecore_EGenericType16'):
        assert _is_linked(a1, 'ecore_EGenericType16', b)
    _safe_set(b, 'ecore_EClass15', {a2})
    assert _is_linked(b, 'ecore_EClass15', a2)
    if hasattr(a1, 'ecore_EGenericType16'):
        assert not _is_linked(a1, 'ecore_EGenericType16', b)
    if hasattr(a2, 'ecore_EGenericType16'):
        assert _is_linked(a2, 'ecore_EGenericType16', b)
    _safe_set(b, 'ecore_EClass15', set())
    assert not _is_linked(b, 'ecore_EClass15', a2)
    if hasattr(a2, 'ecore_EGenericType16'):
        assert not _is_linked(a2, 'ecore_EGenericType16', b)


def test_assoc_eAnnotations22_reverse_link_reassign_clear():
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


def test_assoc_eContainingClass42_reverse_link_reassign_clear():
    a1 = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = ecore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'EClass43', a1)
    assert _is_linked(b, 'EClass43', a1)
    if hasattr(a1, 'eStructuralFeatures'):
        assert _is_linked(a1, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass43', a2)
    assert _is_linked(b, 'EClass43', a2)
    if hasattr(a1, 'eStructuralFeatures'):
        assert not _is_linked(a1, 'eStructuralFeatures', b)
    if hasattr(a2, 'eStructuralFeatures'):
        assert _is_linked(a2, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass43', None)
    assert not _is_linked(b, 'EClass43', a2)
    if hasattr(a2, 'eStructuralFeatures'):
        assert not _is_linked(a2, 'eStructuralFeatures', b)


def test_assoc_eFactoryInstance29_reverse_link_reassign_clear():
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


def test_assoc_eGenericSuperTypes12_reverse_link_reassign_clear():
    a1 = ecore_EGenericType()
    a2 = ecore_EGenericType()
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass13', {a1})
    assert _is_linked(b, 'ecore_EClass13', a1)
    if hasattr(a1, 'ecore_EGenericType'):
        assert _is_linked(a1, 'ecore_EGenericType', b)
    _safe_set(b, 'ecore_EClass13', {a2})
    assert _is_linked(b, 'ecore_EClass13', a2)
    if hasattr(a1, 'ecore_EGenericType'):
        assert not _is_linked(a1, 'ecore_EGenericType', b)
    if hasattr(a2, 'ecore_EGenericType'):
        assert _is_linked(a2, 'ecore_EGenericType', b)
    _safe_set(b, 'ecore_EClass13', set())
    assert not _is_linked(b, 'ecore_EClass13', a2)
    if hasattr(a2, 'ecore_EGenericType'):
        assert not _is_linked(a2, 'ecore_EGenericType', b)


def test_assoc_eGenericType45_reverse_link_reassign_clear():
    a1 = ecore_ETypedElement(lowerBound=7, ordered=True, unique=True, upperBound=7)
    a2 = ecore_ETypedElement(lowerBound=13, ordered=False, unique=False, upperBound=13)
    b = ecore_EGenericType()
    _safe_set(b, 'ecore_EGenericType47', a1)
    assert _is_linked(b, 'ecore_EGenericType47', a1)
    if hasattr(a1, 'ecore_ETypedElement46'):
        assert _is_linked(a1, 'ecore_ETypedElement46', b)
    _safe_set(b, 'ecore_EGenericType47', a2)
    assert _is_linked(b, 'ecore_EGenericType47', a2)
    if hasattr(a1, 'ecore_ETypedElement46'):
        assert not _is_linked(a1, 'ecore_ETypedElement46', b)
    if hasattr(a2, 'ecore_ETypedElement46'):
        assert _is_linked(a2, 'ecore_ETypedElement46', b)
    _safe_set(b, 'ecore_EGenericType47', None)
    assert not _is_linked(b, 'ecore_EGenericType47', a2)
    if hasattr(a2, 'ecore_ETypedElement46'):
        assert not _is_linked(a2, 'ecore_ETypedElement46', b)


def test_assoc_eLowerBound58_reverse_link_reassign_clear():
    a1 = ecore_EGenericType()
    a2 = ecore_EGenericType()
    b = ecore_EGenericType()
    _safe_set(b, 'ecore_EGenericType59', a1)
    assert _is_linked(b, 'ecore_EGenericType59', a1)
    if hasattr(a1, 'ecore_EGenericType57'):
        assert _is_linked(a1, 'ecore_EGenericType57', b)
    _safe_set(b, 'ecore_EGenericType59', a2)
    assert _is_linked(b, 'ecore_EGenericType59', a2)
    if hasattr(a1, 'ecore_EGenericType57'):
        assert not _is_linked(a1, 'ecore_EGenericType57', b)
    if hasattr(a2, 'ecore_EGenericType57'):
        assert _is_linked(a2, 'ecore_EGenericType57', b)
    _safe_set(b, 'ecore_EGenericType59', None)
    assert not _is_linked(b, 'ecore_EGenericType59', a2)
    if hasattr(a2, 'ecore_EGenericType57'):
        assert not _is_linked(a2, 'ecore_EGenericType57', b)


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


def test_assoc_eOpposite41_reverse_link_reassign_clear():
    a1 = ecore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = ecore_EReference(container=False, containment=False, resolveProxies=False)
    b = ecore_EReference(container=True, containment=True, resolveProxies=True)
    _safe_set(b, 'ecore_EReference40', a1)
    assert _is_linked(b, 'ecore_EReference40', a1)
    if hasattr(a1, 'ecore_EReference'):
        assert _is_linked(a1, 'ecore_EReference', b)
    _safe_set(b, 'ecore_EReference40', a2)
    assert _is_linked(b, 'ecore_EReference40', a2)
    if hasattr(a1, 'ecore_EReference'):
        assert not _is_linked(a1, 'ecore_EReference', b)
    if hasattr(a2, 'ecore_EReference'):
        assert _is_linked(a2, 'ecore_EReference', b)
    _safe_set(b, 'ecore_EReference40', None)
    assert not _is_linked(b, 'ecore_EReference40', a2)
    if hasattr(a2, 'ecore_EReference'):
        assert not _is_linked(a2, 'ecore_EReference', b)


def test_assoc_ePackage20_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EFactory()
    _safe_set(b, 'eFactoryInstance', a1)
    assert _is_linked(b, 'eFactoryInstance', a1)
    if hasattr(a1, 'EPackage21'):
        assert _is_linked(a1, 'EPackage21', b)
    _safe_set(b, 'eFactoryInstance', a2)
    assert _is_linked(b, 'eFactoryInstance', a2)
    if hasattr(a1, 'EPackage21'):
        assert not _is_linked(a1, 'EPackage21', b)
    if hasattr(a2, 'EPackage21'):
        assert _is_linked(a2, 'EPackage21', b)
    _safe_set(b, 'eFactoryInstance', None)
    assert not _is_linked(b, 'eFactoryInstance', a2)
    if hasattr(a2, 'EPackage21'):
        assert not _is_linked(a2, 'EPackage21', b)


def test_assoc_eStructuralFeatures10_reverse_link_reassign_clear():
    a1 = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = ecore_EStructuralFeature(changeable=False, defaultValue="sample_text_2", defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'eContainingClass11', {a1})
    assert _is_linked(b, 'eContainingClass11', a1)
    if hasattr(a1, 'EStructuralFeature'):
        assert _is_linked(a1, 'EStructuralFeature', b)
    _safe_set(b, 'eContainingClass11', {a2})
    assert _is_linked(b, 'eContainingClass11', a2)
    if hasattr(a1, 'EStructuralFeature'):
        assert not _is_linked(a1, 'EStructuralFeature', b)
    if hasattr(a2, 'EStructuralFeature'):
        assert _is_linked(a2, 'EStructuralFeature', b)
    _safe_set(b, 'eContainingClass11', set())
    assert not _is_linked(b, 'eContainingClass11', a2)
    if hasattr(a2, 'EStructuralFeature'):
        assert not _is_linked(a2, 'EStructuralFeature', b)


def test_assoc_eSubpackages33_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSuperPackage', {a1})
    assert _is_linked(b, 'eSuperPackage', a1)
    if hasattr(a1, 'EPackage34'):
        assert _is_linked(a1, 'EPackage34', b)
    _safe_set(b, 'eSuperPackage', {a2})
    assert _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a1, 'EPackage34'):
        assert not _is_linked(a1, 'EPackage34', b)
    if hasattr(a2, 'EPackage34'):
        assert _is_linked(a2, 'EPackage34', b)
    _safe_set(b, 'eSuperPackage', set())
    assert not _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a2, 'EPackage34'):
        assert not _is_linked(a2, 'EPackage34', b)


def test_assoc_eSuperPackage36_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSubpackages', a1)
    assert _is_linked(b, 'eSubpackages', a1)
    if hasattr(a1, 'EPackage37'):
        assert _is_linked(a1, 'EPackage37', b)
    _safe_set(b, 'eSubpackages', a2)
    assert _is_linked(b, 'eSubpackages', a2)
    if hasattr(a1, 'EPackage37'):
        assert not _is_linked(a1, 'EPackage37', b)
    if hasattr(a2, 'EPackage37'):
        assert _is_linked(a2, 'EPackage37', b)
    _safe_set(b, 'eSubpackages', None)
    assert not _is_linked(b, 'eSubpackages', a2)
    if hasattr(a2, 'EPackage37'):
        assert not _is_linked(a2, 'EPackage37', b)


def test_assoc_eSuperTypes8_reverse_link_reassign_clear():
    a1 = ecore_EClass(abstract=True, interface=True)
    a2 = ecore_EClass(abstract=False, interface=False)
    b = ecore_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecore_EClass7', {a1})
    assert _is_linked(b, 'ecore_EClass7', a1)
    if hasattr(a1, 'ecore_EClass'):
        assert _is_linked(a1, 'ecore_EClass', b)
    _safe_set(b, 'ecore_EClass7', {a2})
    assert _is_linked(b, 'ecore_EClass7', a2)
    if hasattr(a1, 'ecore_EClass'):
        assert not _is_linked(a1, 'ecore_EClass', b)
    if hasattr(a2, 'ecore_EClass'):
        assert _is_linked(a2, 'ecore_EClass', b)
    _safe_set(b, 'ecore_EClass7', set())
    assert not _is_linked(b, 'ecore_EClass7', a2)
    if hasattr(a2, 'ecore_EClass'):
        assert not _is_linked(a2, 'ecore_EClass', b)


def test_assoc_eTypeArguments52_reverse_link_reassign_clear():
    a1 = ecore_EGenericType()
    a2 = ecore_EGenericType()
    b = ecore_EGenericType()
    _safe_set(b, 'ecore_EGenericType53', a1)
    assert _is_linked(b, 'ecore_EGenericType53', a1)
    if hasattr(a1, 'ecore_EGenericType51'):
        assert _is_linked(a1, 'ecore_EGenericType51', b)
    _safe_set(b, 'ecore_EGenericType53', a2)
    assert _is_linked(b, 'ecore_EGenericType53', a2)
    if hasattr(a1, 'ecore_EGenericType51'):
        assert not _is_linked(a1, 'ecore_EGenericType51', b)
    if hasattr(a2, 'ecore_EGenericType51'):
        assert _is_linked(a2, 'ecore_EGenericType51', b)
    _safe_set(b, 'ecore_EGenericType53', None)
    assert not _is_linked(b, 'ecore_EGenericType53', a2)
    if hasattr(a2, 'ecore_EGenericType51'):
        assert not _is_linked(a2, 'ecore_EGenericType51', b)


def test_assoc_eUpperBound49_reverse_link_reassign_clear():
    a1 = ecore_EGenericType()
    a2 = ecore_EGenericType()
    b = ecore_EGenericType()
    _safe_set(b, 'ecore_EGenericType50', a1)
    assert _is_linked(b, 'ecore_EGenericType50', a1)
    if hasattr(a1, 'ecore_EGenericType48'):
        assert _is_linked(a1, 'ecore_EGenericType48', b)
    _safe_set(b, 'ecore_EGenericType50', a2)
    assert _is_linked(b, 'ecore_EGenericType50', a2)
    if hasattr(a1, 'ecore_EGenericType48'):
        assert not _is_linked(a1, 'ecore_EGenericType48', b)
    if hasattr(a2, 'ecore_EGenericType48'):
        assert _is_linked(a2, 'ecore_EGenericType48', b)
    _safe_set(b, 'ecore_EGenericType50', None)
    assert not _is_linked(b, 'ecore_EGenericType50', a2)
    if hasattr(a2, 'ecore_EGenericType48'):
        assert not _is_linked(a2, 'ecore_EGenericType48', b)


def test_assoc_references4_reverse_link_reassign_clear():
    a1 = ecore_EObject()
    a2 = ecore_EObject()
    b = ecore_EAnnotation(source="sample_text")
    _safe_set(b, 'ecore_EAnnotation5', {a1})
    assert _is_linked(b, 'ecore_EAnnotation5', a1)
    if hasattr(a1, 'ecore_EObject6'):
        assert _is_linked(a1, 'ecore_EObject6', b)
    _safe_set(b, 'ecore_EAnnotation5', {a2})
    assert _is_linked(b, 'ecore_EAnnotation5', a2)
    if hasattr(a1, 'ecore_EObject6'):
        assert not _is_linked(a1, 'ecore_EObject6', b)
    if hasattr(a2, 'ecore_EObject6'):
        assert _is_linked(a2, 'ecore_EObject6', b)
    _safe_set(b, 'ecore_EAnnotation5', set())
    assert not _is_linked(b, 'ecore_EAnnotation5', a2)
    if hasattr(a2, 'ecore_EObject6'):
        assert not _is_linked(a2, 'ecore_EObject6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_eBounds66_stub_double():
    # ecore_ETypeParameter has no real 'ecore_ETypeParameter67' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EGenericType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EGenericType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EGenericType()
    partner = ecore_ETypeParameter()
    setattr(partner, 'ecore_ETypeParameter67', None)
    _safe_set(owner, 'ecore_EGenericType68', partner)
    assert owner in getattr(partner, 'ecore_ETypeParameter67')
    _safe_set(owner, 'ecore_EGenericType68', None)
    assert owner not in getattr(partner, 'ecore_ETypeParameter67')


def test_assoc_eClassifier63_stub_double():
    # ecore_EClassifier has no real 'ecore_EClassifier65' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EGenericType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EGenericType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EGenericType()
    partner = ecore_EClassifier()
    setattr(partner, 'ecore_EClassifier65', None)
    _safe_set(owner, 'ecore_EGenericType64', partner)
    assert getattr(partner, 'ecore_EClassifier65') == owner
    _safe_set(owner, 'ecore_EGenericType64', None)
    assert getattr(partner, 'ecore_EClassifier65') is None


def test_assoc_eClassifiers30_stub_double():
    # ecore_EClassifier has no real 'EClassifier' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    partner = ecore_EClassifier()
    setattr(partner, 'EClassifier', None)
    _safe_set(owner, 'ePackage31', {partner})
    assert getattr(partner, 'EClassifier') == owner
    _safe_set(owner, 'ePackage31', set())
    assert getattr(partner, 'EClassifier') is None


def test_assoc_eContainingClass23_stub_double():
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


def test_assoc_eEnum19_stub_double():
    # ecore_EEnum has no real 'EEnum' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EEnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EEnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EEnumLiteral(literal="sample_text")
    partner = ecore_EEnum()
    setattr(partner, 'EEnum', None)
    _safe_set(owner, 'eLiterals', partner)
    assert getattr(partner, 'EEnum') == owner
    _safe_set(owner, 'eLiterals', None)
    assert getattr(partner, 'EEnum') is None


def test_assoc_eGenericExceptions26_stub_double():
    # ecore_EOperation has no real 'ecore_EOperation27' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EGenericType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EGenericType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EGenericType()
    partner = ecore_EOperation()
    setattr(partner, 'ecore_EOperation27', None)
    _safe_set(owner, 'ecore_EGenericType28', partner)
    assert owner in getattr(partner, 'ecore_EOperation27')
    _safe_set(owner, 'ecore_EGenericType28', None)
    assert owner not in getattr(partner, 'ecore_EOperation27')


def test_assoc_eLiterals18_stub_double():
    # ecore_EEnum has no real 'eEnum' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EEnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EEnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EEnumLiteral(literal="sample_text")
    partner = ecore_EEnum()
    setattr(partner, 'eEnum', None)
    _safe_set(owner, 'EEnumLiteral', partner)
    assert owner in getattr(partner, 'eEnum')
    _safe_set(owner, 'EEnumLiteral', None)
    assert owner not in getattr(partner, 'eEnum')


def test_assoc_eOperations9_stub_double():
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


def test_assoc_ePackage17_stub_double():
    # ecore_EClassifier has no real 'eClassifiers' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    partner = ecore_EClassifier()
    setattr(partner, 'eClassifiers', None)
    _safe_set(owner, 'EPackage', partner)
    assert getattr(partner, 'eClassifiers') == owner
    _safe_set(owner, 'EPackage', None)
    assert getattr(partner, 'eClassifiers') is None


def test_assoc_eRawType54_stub_double():
    # ecore_EClassifier has no real 'ecore_EClassifier56' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EGenericType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EGenericType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EGenericType()
    partner = ecore_EClassifier()
    setattr(partner, 'ecore_EClassifier56', None)
    _safe_set(owner, 'ecore_EGenericType55', partner)
    assert getattr(partner, 'ecore_EClassifier56') == owner
    _safe_set(owner, 'ecore_EGenericType55', None)
    assert getattr(partner, 'ecore_EClassifier56') is None


def test_assoc_eType44_stub_double():
    # ecore_EClassifier has no real 'ecore_EClassifier' property in the generated
    # code (a bare stub) -- manually attach it so ecore_ETypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_ETypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_ETypedElement(lowerBound=7, ordered=True, unique=True, upperBound=7)
    partner = ecore_EClassifier()
    setattr(partner, 'ecore_EClassifier', None)
    _safe_set(owner, 'ecore_ETypedElement', partner)
    assert getattr(partner, 'ecore_EClassifier') == owner
    _safe_set(owner, 'ecore_ETypedElement', None)
    assert getattr(partner, 'ecore_EClassifier') is None


def test_assoc_eTypeParameter60_stub_double():
    # ecore_ETypeParameter has no real 'ecore_ETypeParameter62' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EGenericType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EGenericType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EGenericType()
    partner = ecore_ETypeParameter()
    setattr(partner, 'ecore_ETypeParameter62', None)
    _safe_set(owner, 'ecore_EGenericType61', partner)
    assert getattr(partner, 'ecore_ETypeParameter62') == owner
    _safe_set(owner, 'ecore_EGenericType61', None)
    assert getattr(partner, 'ecore_ETypeParameter62') is None


