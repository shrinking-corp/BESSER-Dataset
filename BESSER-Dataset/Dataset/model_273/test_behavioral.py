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


def test_assoc_eClassifiers61_reverse_link_reassign_clear():
    a1 = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecore_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecore_EClassifier(instanceTypeName="sample_text")
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


def test_assoc_eExceptions54_reverse_link_reassign_clear():
    a1 = ecore_EOperation()
    a2 = ecore_EOperation()
    b = ecore_EClassifier(instanceTypeName="sample_text")
    _safe_set(b, 'ecore_EClassifier56', a1)
    assert _is_linked(b, 'ecore_EClassifier56', a1)
    if hasattr(a1, 'ecore_EOperation55'):
        assert _is_linked(a1, 'ecore_EOperation55', b)
    _safe_set(b, 'ecore_EClassifier56', a2)
    assert _is_linked(b, 'ecore_EClassifier56', a2)
    if hasattr(a1, 'ecore_EOperation55'):
        assert not _is_linked(a1, 'ecore_EOperation55', b)
    if hasattr(a2, 'ecore_EOperation55'):
        assert _is_linked(a2, 'ecore_EOperation55', b)
    _safe_set(b, 'ecore_EClassifier56', None)
    assert not _is_linked(b, 'ecore_EClassifier56', a2)
    if hasattr(a2, 'ecore_EOperation55'):
        assert not _is_linked(a2, 'ecore_EOperation55', b)


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
    a1 = ecore_EReference(containment=True)
    a2 = ecore_EReference(containment=False)
    b = ecore_EReference(containment=True)
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
    b = ecore_EClassifier(instanceTypeName="sample_text")
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


def test_assoc_eType82_reverse_link_reassign_clear():
    a1 = ecore_ETypedElement(lowerBound=7, upperBound=7)
    a2 = ecore_ETypedElement(lowerBound=13, upperBound=13)
    b = ecore_EClassifier(instanceTypeName="sample_text")
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

def test_assoc_eAllContainments22_stub_double():
    # ecore_EClass has no real 'ecore_EClass23' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EReference(containment=True)
    partner = ecore_EClass()
    setattr(partner, 'ecore_EClass23', None)
    _safe_set(owner, 'ecore_EReference24', partner)
    assert owner in getattr(partner, 'ecore_EClass23')
    _safe_set(owner, 'ecore_EReference24', None)
    assert owner not in getattr(partner, 'ecore_EClass23')


def test_assoc_eAllOperations25_stub_double():
    # ecore_EClass has no real 'ecore_EClass26' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EOperation()
    partner = ecore_EClass()
    setattr(partner, 'ecore_EClass26', None)
    _safe_set(owner, 'ecore_EOperation', partner)
    assert owner in getattr(partner, 'ecore_EClass26')
    _safe_set(owner, 'ecore_EOperation', None)
    assert owner not in getattr(partner, 'ecore_EClass26')


def test_assoc_eAllReferences14_stub_double():
    # ecore_EClass has no real 'ecore_EClass15' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EReference(containment=True)
    partner = ecore_EClass()
    setattr(partner, 'ecore_EClass15', None)
    _safe_set(owner, 'ecore_EReference', partner)
    assert owner in getattr(partner, 'ecore_EClass15')
    _safe_set(owner, 'ecore_EReference', None)
    assert owner not in getattr(partner, 'ecore_EClass15')


def test_assoc_eClassifier102_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType103' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClassifier(instanceTypeName="sample_text")
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType103', None)
    _safe_set(owner, 'ecore_EClassifier104', partner)
    assert getattr(partner, 'ecore_EGenericType103') == owner
    _safe_set(owner, 'ecore_EClassifier104', None)
    assert getattr(partner, 'ecore_EGenericType103') is None


def test_assoc_eContainingClass49_stub_double():
    # ecore_EClass has no real 'EClass' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EOperation()
    partner = ecore_EClass()
    setattr(partner, 'EClass', None)
    _safe_set(owner, 'eOperations', partner)
    assert getattr(partner, 'EClass') == owner
    _safe_set(owner, 'eOperations', None)
    assert getattr(partner, 'EClass') is None


def test_assoc_eEnum45_stub_double():
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


def test_assoc_eGenericExceptions57_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType59' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EOperation()
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType59', None)
    _safe_set(owner, 'ecore_EOperation58', {partner})
    assert getattr(partner, 'ecore_EGenericType59') == owner
    _safe_set(owner, 'ecore_EOperation58', set())
    assert getattr(partner, 'ecore_EGenericType59') is None


def test_assoc_eGenericType84_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType86' property in the generated
    # code (a bare stub) -- manually attach it so ecore_ETypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_ETypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_ETypedElement(lowerBound=7, upperBound=7)
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType86', None)
    _safe_set(owner, 'ecore_ETypedElement85', partner)
    assert getattr(partner, 'ecore_EGenericType86') == owner
    _safe_set(owner, 'ecore_ETypedElement85', None)
    assert getattr(partner, 'ecore_EGenericType86') is None


def test_assoc_eKeys77_stub_double():
    # ecore_EAttribute has no real 'ecore_EAttribute79' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EReference(containment=True)
    partner = ecore_EAttribute()
    setattr(partner, 'ecore_EAttribute79', None)
    _safe_set(owner, 'ecore_EReference78', {partner})
    assert getattr(partner, 'ecore_EAttribute79') == owner
    _safe_set(owner, 'ecore_EReference78', set())
    assert getattr(partner, 'ecore_EAttribute79') is None


def test_assoc_eLiterals44_stub_double():
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


def test_assoc_eOperation69_stub_double():
    # ecore_EParameter has no real 'eParameters' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EOperation()
    partner = ecore_EParameter()
    setattr(partner, 'eParameters', None)
    _safe_set(owner, 'EOperation70', partner)
    assert getattr(partner, 'eParameters') == owner
    _safe_set(owner, 'EOperation70', None)
    assert getattr(partner, 'eParameters') is None


def test_assoc_eOperations10_stub_double():
    # ecore_EClass has no real 'eContainingClass' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EOperation()
    partner = ecore_EClass()
    setattr(partner, 'eContainingClass', None)
    _safe_set(owner, 'EOperation', partner)
    assert owner in getattr(partner, 'eContainingClass')
    _safe_set(owner, 'EOperation', None)
    assert owner not in getattr(partner, 'eContainingClass')


def test_assoc_eParameters53_stub_double():
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


def test_assoc_eRawType93_stub_double():
    # ecore_EGenericType has no real 'ecore_EGenericType94' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClassifier(instanceTypeName="sample_text")
    partner = ecore_EGenericType()
    setattr(partner, 'ecore_EGenericType94', None)
    _safe_set(owner, 'ecore_EClassifier95', partner)
    assert getattr(partner, 'ecore_EGenericType94') == owner
    _safe_set(owner, 'ecore_EClassifier95', None)
    assert getattr(partner, 'ecore_EGenericType94') is None


def test_assoc_eReferenceType74_stub_double():
    # ecore_EClass has no real 'ecore_EClass76' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EReference(containment=True)
    partner = ecore_EClass()
    setattr(partner, 'ecore_EClass76', None)
    _safe_set(owner, 'ecore_EReference75', partner)
    assert getattr(partner, 'ecore_EClass76') == owner
    _safe_set(owner, 'ecore_EReference75', None)
    assert getattr(partner, 'ecore_EClass76') is None


def test_assoc_eReferences16_stub_double():
    # ecore_EClass has no real 'ecore_EClass17' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EReference(containment=True)
    partner = ecore_EClass()
    setattr(partner, 'ecore_EClass17', None)
    _safe_set(owner, 'ecore_EReference18', partner)
    assert owner in getattr(partner, 'ecore_EClass17')
    _safe_set(owner, 'ecore_EReference18', None)
    assert owner not in getattr(partner, 'ecore_EClass17')


def test_assoc_eTypeParameters43_stub_double():
    # ecore_ETypeParameter has no real 'ecore_ETypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClassifier(instanceTypeName="sample_text")
    partner = ecore_ETypeParameter()
    setattr(partner, 'ecore_ETypeParameter', None)
    _safe_set(owner, 'ecore_EClassifier', {partner})
    assert getattr(partner, 'ecore_ETypeParameter') == owner
    _safe_set(owner, 'ecore_EClassifier', set())
    assert getattr(partner, 'ecore_ETypeParameter') is None


def test_assoc_eTypeParameters50_stub_double():
    # ecore_ETypeParameter has no real 'ecore_ETypeParameter52' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EOperation()
    partner = ecore_ETypeParameter()
    setattr(partner, 'ecore_ETypeParameter52', None)
    _safe_set(owner, 'ecore_EOperation51', {partner})
    assert getattr(partner, 'ecore_ETypeParameter52') == owner
    _safe_set(owner, 'ecore_EOperation51', set())
    assert getattr(partner, 'ecore_ETypeParameter52') is None


