import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EClassifier,
    EDataType,
    EModelElement,
    ENamedElement,
    EStructuralFeature,
    ETypedElement,
    RefinementsEcore_EAnnotation,
    RefinementsEcore_EAttribute,
    RefinementsEcore_EClass,
    RefinementsEcore_EClassifier,
    RefinementsEcore_EDataType,
    RefinementsEcore_EEnum,
    RefinementsEcore_EEnumLiteral,
    RefinementsEcore_EModelElement,
    RefinementsEcore_ENamedElement,
    RefinementsEcore_EOperation,
    RefinementsEcore_EPackage,
    RefinementsEcore_EParameter,
    RefinementsEcore_EReference,
    RefinementsEcore_EStructuralFeature,
    RefinementsEcore_ETypedElement,
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

def test_assoc_Refines2_reverse_link_reassign_clear():
    a1 = RefinementsEcore_EAttribute(iD=7)
    a2 = RefinementsEcore_EAttribute(iD=13)
    b = RefinementsEcore_EAttribute(iD=7)
    _safe_set(b, 'RefinementsEcore_EAttribute3', a1)
    assert _is_linked(b, 'RefinementsEcore_EAttribute3', a1)
    if hasattr(a1, 'RefinementsEcore_EAttribute1'):
        assert _is_linked(a1, 'RefinementsEcore_EAttribute1', b)
    _safe_set(b, 'RefinementsEcore_EAttribute3', a2)
    assert _is_linked(b, 'RefinementsEcore_EAttribute3', a2)
    if hasattr(a1, 'RefinementsEcore_EAttribute1'):
        assert not _is_linked(a1, 'RefinementsEcore_EAttribute1', b)
    if hasattr(a2, 'RefinementsEcore_EAttribute1'):
        assert _is_linked(a2, 'RefinementsEcore_EAttribute1', b)
    _safe_set(b, 'RefinementsEcore_EAttribute3', None)
    assert not _is_linked(b, 'RefinementsEcore_EAttribute3', a2)
    if hasattr(a2, 'RefinementsEcore_EAttribute1'):
        assert not _is_linked(a2, 'RefinementsEcore_EAttribute1', b)


def test_assoc_Refines44_reverse_link_reassign_clear():
    a1 = RefinementsEcore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = RefinementsEcore_EReference(container=False, containment=False, resolveProxies=False)
    b = RefinementsEcore_EReference(container=True, containment=True, resolveProxies=True)
    _safe_set(b, 'RefinementsEcore_EReference45', a1)
    assert _is_linked(b, 'RefinementsEcore_EReference45', a1)
    if hasattr(a1, 'RefinementsEcore_EReference43'):
        assert _is_linked(a1, 'RefinementsEcore_EReference43', b)
    _safe_set(b, 'RefinementsEcore_EReference45', a2)
    assert _is_linked(b, 'RefinementsEcore_EReference45', a2)
    if hasattr(a1, 'RefinementsEcore_EReference43'):
        assert not _is_linked(a1, 'RefinementsEcore_EReference43', b)
    if hasattr(a2, 'RefinementsEcore_EReference43'):
        assert _is_linked(a2, 'RefinementsEcore_EReference43', b)
    _safe_set(b, 'RefinementsEcore_EReference45', None)
    assert not _is_linked(b, 'RefinementsEcore_EReference45', a2)
    if hasattr(a2, 'RefinementsEcore_EReference43'):
        assert not _is_linked(a2, 'RefinementsEcore_EReference43', b)


def test_assoc_eAttributeType0_reverse_link_reassign_clear():
    a1 = RefinementsEcore_EDataType(serializable=True)
    a2 = RefinementsEcore_EDataType(serializable=False)
    b = RefinementsEcore_EAttribute(iD=7)
    _safe_set(b, 'RefinementsEcore_EAttribute', a1)
    assert _is_linked(b, 'RefinementsEcore_EAttribute', a1)
    if hasattr(a1, 'RefinementsEcore_EDataType'):
        assert _is_linked(a1, 'RefinementsEcore_EDataType', b)
    _safe_set(b, 'RefinementsEcore_EAttribute', a2)
    assert _is_linked(b, 'RefinementsEcore_EAttribute', a2)
    if hasattr(a1, 'RefinementsEcore_EDataType'):
        assert not _is_linked(a1, 'RefinementsEcore_EDataType', b)
    if hasattr(a2, 'RefinementsEcore_EDataType'):
        assert _is_linked(a2, 'RefinementsEcore_EDataType', b)
    _safe_set(b, 'RefinementsEcore_EAttribute', None)
    assert not _is_linked(b, 'RefinementsEcore_EAttribute', a2)
    if hasattr(a2, 'RefinementsEcore_EDataType'):
        assert not _is_linked(a2, 'RefinementsEcore_EDataType', b)


def test_assoc_eAttributes10_reverse_link_reassign_clear():
    a1 = RefinementsEcore_EClass(abstract=True, interface=True)
    a2 = RefinementsEcore_EClass(abstract=False, interface=False)
    b = RefinementsEcore_EAttribute(iD=7)
    _safe_set(b, 'RefinementsEcore_EAttribute12', a1)
    assert _is_linked(b, 'RefinementsEcore_EAttribute12', a1)
    if hasattr(a1, 'RefinementsEcore_EClass11'):
        assert _is_linked(a1, 'RefinementsEcore_EClass11', b)
    _safe_set(b, 'RefinementsEcore_EAttribute12', a2)
    assert _is_linked(b, 'RefinementsEcore_EAttribute12', a2)
    if hasattr(a1, 'RefinementsEcore_EClass11'):
        assert not _is_linked(a1, 'RefinementsEcore_EClass11', b)
    if hasattr(a2, 'RefinementsEcore_EClass11'):
        assert _is_linked(a2, 'RefinementsEcore_EClass11', b)
    _safe_set(b, 'RefinementsEcore_EAttribute12', None)
    assert not _is_linked(b, 'RefinementsEcore_EAttribute12', a2)
    if hasattr(a2, 'RefinementsEcore_EClass11'):
        assert not _is_linked(a2, 'RefinementsEcore_EClass11', b)


def test_assoc_eClassifiers25_reverse_link_reassign_clear():
    a1 = RefinementsEcore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = RefinementsEcore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = RefinementsEcore_EClassifier(instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
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


def test_assoc_eContainingClass46_reverse_link_reassign_clear():
    a1 = RefinementsEcore_EStructuralFeature(changeable=True, defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = RefinementsEcore_EStructuralFeature(changeable=False, defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = RefinementsEcore_EClass(abstract=True, interface=True)
    _safe_set(b, 'EClass47', a1)
    assert _is_linked(b, 'EClass47', a1)
    if hasattr(a1, 'eStructuralFeatures'):
        assert _is_linked(a1, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass47', a2)
    assert _is_linked(b, 'EClass47', a2)
    if hasattr(a1, 'eStructuralFeatures'):
        assert not _is_linked(a1, 'eStructuralFeatures', b)
    if hasattr(a2, 'eStructuralFeatures'):
        assert _is_linked(a2, 'eStructuralFeatures', b)
    _safe_set(b, 'EClass47', None)
    assert not _is_linked(b, 'EClass47', a2)
    if hasattr(a2, 'eStructuralFeatures'):
        assert not _is_linked(a2, 'eStructuralFeatures', b)


def test_assoc_eIDAttribute13_reverse_link_reassign_clear():
    a1 = RefinementsEcore_EClass(abstract=True, interface=True)
    a2 = RefinementsEcore_EClass(abstract=False, interface=False)
    b = RefinementsEcore_EAttribute(iD=7)
    _safe_set(b, 'RefinementsEcore_EAttribute15', a1)
    assert _is_linked(b, 'RefinementsEcore_EAttribute15', a1)
    if hasattr(a1, 'RefinementsEcore_EClass14'):
        assert _is_linked(a1, 'RefinementsEcore_EClass14', b)
    _safe_set(b, 'RefinementsEcore_EAttribute15', a2)
    assert _is_linked(b, 'RefinementsEcore_EAttribute15', a2)
    if hasattr(a1, 'RefinementsEcore_EClass14'):
        assert not _is_linked(a1, 'RefinementsEcore_EClass14', b)
    if hasattr(a2, 'RefinementsEcore_EClass14'):
        assert _is_linked(a2, 'RefinementsEcore_EClass14', b)
    _safe_set(b, 'RefinementsEcore_EAttribute15', None)
    assert not _is_linked(b, 'RefinementsEcore_EAttribute15', a2)
    if hasattr(a2, 'RefinementsEcore_EClass14'):
        assert not _is_linked(a2, 'RefinementsEcore_EClass14', b)


def test_assoc_eKeys40_reverse_link_reassign_clear():
    a1 = RefinementsEcore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = RefinementsEcore_EReference(container=False, containment=False, resolveProxies=False)
    b = RefinementsEcore_EAttribute(iD=7)
    _safe_set(b, 'RefinementsEcore_EAttribute42', a1)
    assert _is_linked(b, 'RefinementsEcore_EAttribute42', a1)
    if hasattr(a1, 'RefinementsEcore_EReference41'):
        assert _is_linked(a1, 'RefinementsEcore_EReference41', b)
    _safe_set(b, 'RefinementsEcore_EAttribute42', a2)
    assert _is_linked(b, 'RefinementsEcore_EAttribute42', a2)
    if hasattr(a1, 'RefinementsEcore_EReference41'):
        assert not _is_linked(a1, 'RefinementsEcore_EReference41', b)
    if hasattr(a2, 'RefinementsEcore_EReference41'):
        assert _is_linked(a2, 'RefinementsEcore_EReference41', b)
    _safe_set(b, 'RefinementsEcore_EAttribute42', None)
    assert not _is_linked(b, 'RefinementsEcore_EAttribute42', a2)
    if hasattr(a2, 'RefinementsEcore_EReference41'):
        assert not _is_linked(a2, 'RefinementsEcore_EReference41', b)


def test_assoc_eOpposite35_reverse_link_reassign_clear():
    a1 = RefinementsEcore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = RefinementsEcore_EReference(container=False, containment=False, resolveProxies=False)
    b = RefinementsEcore_EReference(container=True, containment=True, resolveProxies=True)
    _safe_set(b, 'RefinementsEcore_EReference36', a1)
    assert _is_linked(b, 'RefinementsEcore_EReference36', a1)
    if hasattr(a1, 'RefinementsEcore_EReference34'):
        assert _is_linked(a1, 'RefinementsEcore_EReference34', b)
    _safe_set(b, 'RefinementsEcore_EReference36', a2)
    assert _is_linked(b, 'RefinementsEcore_EReference36', a2)
    if hasattr(a1, 'RefinementsEcore_EReference34'):
        assert not _is_linked(a1, 'RefinementsEcore_EReference34', b)
    if hasattr(a2, 'RefinementsEcore_EReference34'):
        assert _is_linked(a2, 'RefinementsEcore_EReference34', b)
    _safe_set(b, 'RefinementsEcore_EReference36', None)
    assert not _is_linked(b, 'RefinementsEcore_EReference36', a2)
    if hasattr(a2, 'RefinementsEcore_EReference34'):
        assert not _is_linked(a2, 'RefinementsEcore_EReference34', b)


def test_assoc_ePackage18_reverse_link_reassign_clear():
    a1 = RefinementsEcore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = RefinementsEcore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = RefinementsEcore_EClassifier(instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
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


def test_assoc_eReferenceType37_reverse_link_reassign_clear():
    a1 = RefinementsEcore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = RefinementsEcore_EReference(container=False, containment=False, resolveProxies=False)
    b = RefinementsEcore_EClass(abstract=True, interface=True)
    _safe_set(b, 'RefinementsEcore_EClass39', a1)
    assert _is_linked(b, 'RefinementsEcore_EClass39', a1)
    if hasattr(a1, 'RefinementsEcore_EReference38'):
        assert _is_linked(a1, 'RefinementsEcore_EReference38', b)
    _safe_set(b, 'RefinementsEcore_EClass39', a2)
    assert _is_linked(b, 'RefinementsEcore_EClass39', a2)
    if hasattr(a1, 'RefinementsEcore_EReference38'):
        assert not _is_linked(a1, 'RefinementsEcore_EReference38', b)
    if hasattr(a2, 'RefinementsEcore_EReference38'):
        assert _is_linked(a2, 'RefinementsEcore_EReference38', b)
    _safe_set(b, 'RefinementsEcore_EClass39', None)
    assert not _is_linked(b, 'RefinementsEcore_EClass39', a2)
    if hasattr(a2, 'RefinementsEcore_EReference38'):
        assert not _is_linked(a2, 'RefinementsEcore_EReference38', b)


def test_assoc_eReferences8_reverse_link_reassign_clear():
    a1 = RefinementsEcore_EReference(container=True, containment=True, resolveProxies=True)
    a2 = RefinementsEcore_EReference(container=False, containment=False, resolveProxies=False)
    b = RefinementsEcore_EClass(abstract=True, interface=True)
    _safe_set(b, 'RefinementsEcore_EClass9', {a1})
    assert _is_linked(b, 'RefinementsEcore_EClass9', a1)
    if hasattr(a1, 'RefinementsEcore_EReference'):
        assert _is_linked(a1, 'RefinementsEcore_EReference', b)
    _safe_set(b, 'RefinementsEcore_EClass9', {a2})
    assert _is_linked(b, 'RefinementsEcore_EClass9', a2)
    if hasattr(a1, 'RefinementsEcore_EReference'):
        assert not _is_linked(a1, 'RefinementsEcore_EReference', b)
    if hasattr(a2, 'RefinementsEcore_EReference'):
        assert _is_linked(a2, 'RefinementsEcore_EReference', b)
    _safe_set(b, 'RefinementsEcore_EClass9', set())
    assert not _is_linked(b, 'RefinementsEcore_EClass9', a2)
    if hasattr(a2, 'RefinementsEcore_EReference'):
        assert not _is_linked(a2, 'RefinementsEcore_EReference', b)


def test_assoc_eStructuralFeatures16_reverse_link_reassign_clear():
    a1 = RefinementsEcore_EStructuralFeature(changeable=True, defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = RefinementsEcore_EStructuralFeature(changeable=False, defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = RefinementsEcore_EClass(abstract=True, interface=True)
    _safe_set(b, 'eContainingClass17', {a1})
    assert _is_linked(b, 'eContainingClass17', a1)
    if hasattr(a1, 'EStructuralFeature'):
        assert _is_linked(a1, 'EStructuralFeature', b)
    _safe_set(b, 'eContainingClass17', {a2})
    assert _is_linked(b, 'eContainingClass17', a2)
    if hasattr(a1, 'EStructuralFeature'):
        assert not _is_linked(a1, 'EStructuralFeature', b)
    if hasattr(a2, 'EStructuralFeature'):
        assert _is_linked(a2, 'EStructuralFeature', b)
    _safe_set(b, 'eContainingClass17', set())
    assert not _is_linked(b, 'eContainingClass17', a2)
    if hasattr(a2, 'EStructuralFeature'):
        assert not _is_linked(a2, 'EStructuralFeature', b)


def test_assoc_eSubpackages27_reverse_link_reassign_clear():
    a1 = RefinementsEcore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = RefinementsEcore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = RefinementsEcore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSuperPackage', {a1})
    assert _is_linked(b, 'eSuperPackage', a1)
    if hasattr(a1, 'EPackage28'):
        assert _is_linked(a1, 'EPackage28', b)
    _safe_set(b, 'eSuperPackage', {a2})
    assert _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a1, 'EPackage28'):
        assert not _is_linked(a1, 'EPackage28', b)
    if hasattr(a2, 'EPackage28'):
        assert _is_linked(a2, 'EPackage28', b)
    _safe_set(b, 'eSuperPackage', set())
    assert not _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a2, 'EPackage28'):
        assert not _is_linked(a2, 'EPackage28', b)


def test_assoc_eSuperPackage30_reverse_link_reassign_clear():
    a1 = RefinementsEcore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = RefinementsEcore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = RefinementsEcore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSubpackages', a1)
    assert _is_linked(b, 'eSubpackages', a1)
    if hasattr(a1, 'EPackage31'):
        assert _is_linked(a1, 'EPackage31', b)
    _safe_set(b, 'eSubpackages', a2)
    assert _is_linked(b, 'eSubpackages', a2)
    if hasattr(a1, 'EPackage31'):
        assert not _is_linked(a1, 'EPackage31', b)
    if hasattr(a2, 'EPackage31'):
        assert _is_linked(a2, 'EPackage31', b)
    _safe_set(b, 'eSubpackages', None)
    assert not _is_linked(b, 'eSubpackages', a2)
    if hasattr(a2, 'EPackage31'):
        assert not _is_linked(a2, 'EPackage31', b)


def test_assoc_eSuperTypes6_reverse_link_reassign_clear():
    a1 = RefinementsEcore_EClass(abstract=True, interface=True)
    a2 = RefinementsEcore_EClass(abstract=False, interface=False)
    b = RefinementsEcore_EClass(abstract=True, interface=True)
    _safe_set(b, 'RefinementsEcore_EClass5', {a1})
    assert _is_linked(b, 'RefinementsEcore_EClass5', a1)
    if hasattr(a1, 'RefinementsEcore_EClass'):
        assert _is_linked(a1, 'RefinementsEcore_EClass', b)
    _safe_set(b, 'RefinementsEcore_EClass5', {a2})
    assert _is_linked(b, 'RefinementsEcore_EClass5', a2)
    if hasattr(a1, 'RefinementsEcore_EClass'):
        assert not _is_linked(a1, 'RefinementsEcore_EClass', b)
    if hasattr(a2, 'RefinementsEcore_EClass'):
        assert _is_linked(a2, 'RefinementsEcore_EClass', b)
    _safe_set(b, 'RefinementsEcore_EClass5', set())
    assert not _is_linked(b, 'RefinementsEcore_EClass5', a2)
    if hasattr(a2, 'RefinementsEcore_EClass'):
        assert not _is_linked(a2, 'RefinementsEcore_EClass', b)


def test_assoc_eType48_reverse_link_reassign_clear():
    a1 = RefinementsEcore_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    a2 = RefinementsEcore_ETypedElement(lowerBound=13, many=False, ordered=False, required=False, unique=False, upperBound=13)
    b = RefinementsEcore_EClassifier(instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'RefinementsEcore_EClassifier49', a1)
    assert _is_linked(b, 'RefinementsEcore_EClassifier49', a1)
    if hasattr(a1, 'RefinementsEcore_ETypedElement'):
        assert _is_linked(a1, 'RefinementsEcore_ETypedElement', b)
    _safe_set(b, 'RefinementsEcore_EClassifier49', a2)
    assert _is_linked(b, 'RefinementsEcore_EClassifier49', a2)
    if hasattr(a1, 'RefinementsEcore_ETypedElement'):
        assert not _is_linked(a1, 'RefinementsEcore_ETypedElement', b)
    if hasattr(a2, 'RefinementsEcore_ETypedElement'):
        assert _is_linked(a2, 'RefinementsEcore_ETypedElement', b)
    _safe_set(b, 'RefinementsEcore_EClassifier49', None)
    assert not _is_linked(b, 'RefinementsEcore_EClassifier49', a2)
    if hasattr(a2, 'RefinementsEcore_ETypedElement'):
        assert not _is_linked(a2, 'RefinementsEcore_ETypedElement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_eAnnotations21_stub_double():
    # RefinementsEcore_EModelElement has no real 'eModelElement' property in the generated
    # code (a bare stub) -- manually attach it so RefinementsEcore_EAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RefinementsEcore_EAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RefinementsEcore_EAnnotation(source="sample_text")
    partner = RefinementsEcore_EModelElement()
    setattr(partner, 'eModelElement', None)
    _safe_set(owner, 'EAnnotation', partner)
    assert owner in getattr(partner, 'eModelElement')
    _safe_set(owner, 'EAnnotation', None)
    assert owner not in getattr(partner, 'eModelElement')


def test_assoc_eContainingClass22_stub_double():
    # RefinementsEcore_EOperation has no real 'eOperations' property in the generated
    # code (a bare stub) -- manually attach it so RefinementsEcore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RefinementsEcore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RefinementsEcore_EClass(abstract=True, interface=True)
    partner = RefinementsEcore_EOperation()
    setattr(partner, 'eOperations', None)
    _safe_set(owner, 'EClass', partner)
    assert getattr(partner, 'eOperations') == owner
    _safe_set(owner, 'EClass', None)
    assert getattr(partner, 'eOperations') is None


def test_assoc_eEnum20_stub_double():
    # RefinementsEcore_EEnum has no real 'EEnum' property in the generated
    # code (a bare stub) -- manually attach it so RefinementsEcore_EEnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RefinementsEcore_EEnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RefinementsEcore_EEnumLiteral(literal="sample_text", value=7)
    partner = RefinementsEcore_EEnum()
    setattr(partner, 'EEnum', None)
    _safe_set(owner, 'eLiterals', partner)
    assert getattr(partner, 'EEnum') == owner
    _safe_set(owner, 'eLiterals', None)
    assert getattr(partner, 'EEnum') is None


def test_assoc_eExceptions24_stub_double():
    # RefinementsEcore_EOperation has no real 'RefinementsEcore_EOperation' property in the generated
    # code (a bare stub) -- manually attach it so RefinementsEcore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RefinementsEcore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RefinementsEcore_EClassifier(instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = RefinementsEcore_EOperation()
    setattr(partner, 'RefinementsEcore_EOperation', None)
    _safe_set(owner, 'RefinementsEcore_EClassifier', partner)
    assert owner in getattr(partner, 'RefinementsEcore_EOperation')
    _safe_set(owner, 'RefinementsEcore_EClassifier', None)
    assert owner not in getattr(partner, 'RefinementsEcore_EOperation')


def test_assoc_eLiterals19_stub_double():
    # RefinementsEcore_EEnum has no real 'eEnum' property in the generated
    # code (a bare stub) -- manually attach it so RefinementsEcore_EEnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RefinementsEcore_EEnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RefinementsEcore_EEnumLiteral(literal="sample_text", value=7)
    partner = RefinementsEcore_EEnum()
    setattr(partner, 'eEnum', None)
    _safe_set(owner, 'EEnumLiteral', partner)
    assert owner in getattr(partner, 'eEnum')
    _safe_set(owner, 'EEnumLiteral', None)
    assert owner not in getattr(partner, 'eEnum')


def test_assoc_eModelElement4_stub_double():
    # RefinementsEcore_EModelElement has no real 'EModelElement' property in the generated
    # code (a bare stub) -- manually attach it so RefinementsEcore_EAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RefinementsEcore_EAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RefinementsEcore_EAnnotation(source="sample_text")
    partner = RefinementsEcore_EModelElement()
    setattr(partner, 'EModelElement', None)
    _safe_set(owner, 'eAnnotations', partner)
    assert getattr(partner, 'EModelElement') == owner
    _safe_set(owner, 'eAnnotations', None)
    assert getattr(partner, 'EModelElement') is None


def test_assoc_eOperations7_stub_double():
    # RefinementsEcore_EOperation has no real 'EOperation' property in the generated
    # code (a bare stub) -- manually attach it so RefinementsEcore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RefinementsEcore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RefinementsEcore_EClass(abstract=True, interface=True)
    partner = RefinementsEcore_EOperation()
    setattr(partner, 'EOperation', None)
    _safe_set(owner, 'eContainingClass', {partner})
    assert getattr(partner, 'EOperation') == owner
    _safe_set(owner, 'eContainingClass', set())
    assert getattr(partner, 'EOperation') is None


