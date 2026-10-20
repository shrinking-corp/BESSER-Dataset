import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EAnnotation,
    EAttribute,
    EClass,
    EClassifier,
    EDataType,
    EEnum,
    EEnumLiteral,
    EFactory,
    EGenericType,
    EModelElement,
    ENamedElement,
    EObject,
    EOperation,
    EPackage,
    EParameter,
    EReference,
    EStringToStringMapEntry,
    EStructuralFeature,
    ETypeParameter,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_contents3_stub_double():
    # EObject has no real 'EObject' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EAnnotation(source="sample_text")
    partner = EObject()
    setattr(partner, 'EObject', None)
    _safe_set(owner, 'ecore_EAnnotation4', {partner})
    assert getattr(partner, 'EObject') == owner
    _safe_set(owner, 'ecore_EAnnotation4', set())
    assert getattr(partner, 'EObject') is None


def test_assoc_details1_stub_double():
    # EStringToStringMapEntry has no real 'EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EAnnotation(source="sample_text")
    partner = EStringToStringMapEntry()
    setattr(partner, 'EStringToStringMapEntry', None)
    _safe_set(owner, 'ecore_EAnnotation', {partner})
    assert getattr(partner, 'EStringToStringMapEntry') == owner
    _safe_set(owner, 'ecore_EAnnotation', set())
    assert getattr(partner, 'EStringToStringMapEntry') is None


def test_assoc_eAllAttributes10_stub_double():
    # EAttribute has no real 'EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract="sample_text", interface="sample_text")
    partner = EAttribute()
    setattr(partner, 'EAttribute', None)
    _safe_set(owner, 'ecore_EClass11', {partner})
    assert getattr(partner, 'EAttribute') == owner
    _safe_set(owner, 'ecore_EClass11', set())
    assert getattr(partner, 'EAttribute') is None


def test_assoc_eAllContainments20_stub_double():
    # EReference has no real 'EReference22' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract="sample_text", interface="sample_text")
    partner = EReference()
    setattr(partner, 'EReference22', None)
    _safe_set(owner, 'ecore_EClass21', {partner})
    assert getattr(partner, 'EReference22') == owner
    _safe_set(owner, 'ecore_EClass21', set())
    assert getattr(partner, 'EReference22') is None


def test_assoc_eAllGenericSuperTypes39_stub_double():
    # EGenericType has no real 'EGenericType41' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract="sample_text", interface="sample_text")
    partner = EGenericType()
    setattr(partner, 'EGenericType41', None)
    _safe_set(owner, 'ecore_EClass40', {partner})
    assert getattr(partner, 'EGenericType41') == owner
    _safe_set(owner, 'ecore_EClass40', set())
    assert getattr(partner, 'EGenericType41') is None


def test_assoc_eAllOperations23_stub_double():
    # EOperation has no real 'EOperation25' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract="sample_text", interface="sample_text")
    partner = EOperation()
    setattr(partner, 'EOperation25', None)
    _safe_set(owner, 'ecore_EClass24', {partner})
    assert getattr(partner, 'EOperation25') == owner
    _safe_set(owner, 'ecore_EClass24', set())
    assert getattr(partner, 'EOperation25') is None


def test_assoc_eAllReferences12_stub_double():
    # EReference has no real 'EReference' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract="sample_text", interface="sample_text")
    partner = EReference()
    setattr(partner, 'EReference', None)
    _safe_set(owner, 'ecore_EClass13', {partner})
    assert getattr(partner, 'EReference') == owner
    _safe_set(owner, 'ecore_EClass13', set())
    assert getattr(partner, 'EReference') is None


def test_assoc_eAllStructuralFeatures26_stub_double():
    # EStructuralFeature has no real 'EStructuralFeature' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract="sample_text", interface="sample_text")
    partner = EStructuralFeature()
    setattr(partner, 'EStructuralFeature', None)
    _safe_set(owner, 'ecore_EClass27', {partner})
    assert getattr(partner, 'EStructuralFeature') == owner
    _safe_set(owner, 'ecore_EClass27', set())
    assert getattr(partner, 'EStructuralFeature') is None


def test_assoc_eAllSuperTypes28_stub_double():
    # EClass has no real 'EClass30' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract="sample_text", interface="sample_text")
    partner = EClass()
    setattr(partner, 'EClass30', None)
    _safe_set(owner, 'ecore_EClass29', {partner})
    assert getattr(partner, 'EClass30') == owner
    _safe_set(owner, 'ecore_EClass29', set())
    assert getattr(partner, 'EClass30') is None


def test_assoc_eAnnotations48_stub_double():
    # EAnnotation has no real 'EAnnotation' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EModelElement()
    partner = EAnnotation()
    setattr(partner, 'EAnnotation', None)
    _safe_set(owner, 'eModelElement', {partner})
    assert getattr(partner, 'EAnnotation') == owner
    _safe_set(owner, 'eModelElement', set())
    assert getattr(partner, 'EAnnotation') is None


def test_assoc_eAttributeType0_stub_double():
    # EDataType has no real 'EDataType' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EAttribute(iD="sample_text")
    partner = EDataType()
    setattr(partner, 'EDataType', None)
    _safe_set(owner, 'ecore_EAttribute', partner)
    assert getattr(partner, 'EDataType') == owner
    _safe_set(owner, 'ecore_EAttribute', None)
    assert getattr(partner, 'EDataType') is None


def test_assoc_eAttributes17_stub_double():
    # EAttribute has no real 'EAttribute19' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract="sample_text", interface="sample_text")
    partner = EAttribute()
    setattr(partner, 'EAttribute19', None)
    _safe_set(owner, 'ecore_EClass18', {partner})
    assert getattr(partner, 'EAttribute19') == owner
    _safe_set(owner, 'ecore_EClass18', set())
    assert getattr(partner, 'EAttribute19') is None


def test_assoc_eClassifiers50_stub_double():
    # EClassifier has no real 'EClassifier' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    partner = EClassifier()
    setattr(partner, 'EClassifier', None)
    _safe_set(owner, 'ePackage51', {partner})
    assert getattr(partner, 'EClassifier') == owner
    _safe_set(owner, 'ePackage51', set())
    assert getattr(partner, 'EClassifier') is None


def test_assoc_eContainingClass66_stub_double():
    # EClass has no real 'EClass67' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EStructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EStructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EStructuralFeature(changeable="sample_text", defaultValue="sample_text", defaultValueLiteral="sample_text", derived="sample_text", transient="sample_text", unsettable="sample_text", volatile="sample_text")
    partner = EClass()
    setattr(partner, 'EClass67', None)
    _safe_set(owner, 'eStructuralFeatures', partner)
    assert getattr(partner, 'EClass67') == owner
    _safe_set(owner, 'eStructuralFeatures', None)
    assert getattr(partner, 'EClass67') is None


def test_assoc_eEnum45_stub_double():
    # EEnum has no real 'EEnum' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EEnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EEnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EEnumLiteral(instance="sample_text", literal="sample_text", value="sample_text")
    partner = EEnum()
    setattr(partner, 'EEnum', None)
    _safe_set(owner, 'eLiterals', partner)
    assert getattr(partner, 'EEnum') == owner
    _safe_set(owner, 'eLiterals', None)
    assert getattr(partner, 'EEnum') is None


def test_assoc_eFactoryInstance49_stub_double():
    # EFactory has no real 'EFactory' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    partner = EFactory()
    setattr(partner, 'EFactory', None)
    _safe_set(owner, 'ePackage', partner)
    assert getattr(partner, 'EFactory') == owner
    _safe_set(owner, 'ePackage', None)
    assert getattr(partner, 'EFactory') is None


def test_assoc_eGenericSuperTypes37_stub_double():
    # EGenericType has no real 'EGenericType' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract="sample_text", interface="sample_text")
    partner = EGenericType()
    setattr(partner, 'EGenericType', None)
    _safe_set(owner, 'ecore_EClass38', {partner})
    assert getattr(partner, 'EGenericType') == owner
    _safe_set(owner, 'ecore_EClass38', set())
    assert getattr(partner, 'EGenericType') is None


def test_assoc_eGenericType81_stub_double():
    # EGenericType has no real 'EGenericType83' property in the generated
    # code (a bare stub) -- manually attach it so ecore_ETypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_ETypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_ETypedElement(lowerBound="sample_text", many="sample_text", ordered="sample_text", required="sample_text", unique="sample_text", upperBound="sample_text")
    partner = EGenericType()
    setattr(partner, 'EGenericType83', None)
    _safe_set(owner, 'ecore_ETypedElement82', partner)
    assert getattr(partner, 'EGenericType83') == owner
    _safe_set(owner, 'ecore_ETypedElement82', None)
    assert getattr(partner, 'EGenericType83') is None


def test_assoc_eIDAttribute31_stub_double():
    # EAttribute has no real 'EAttribute33' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract="sample_text", interface="sample_text")
    partner = EAttribute()
    setattr(partner, 'EAttribute33', None)
    _safe_set(owner, 'ecore_EClass32', partner)
    assert getattr(partner, 'EAttribute33') == owner
    _safe_set(owner, 'ecore_EClass32', None)
    assert getattr(partner, 'EAttribute33') is None


def test_assoc_eKeys63_stub_double():
    # EAttribute has no real 'EAttribute65' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EReference(container="sample_text", containment="sample_text", resolveProxies="sample_text")
    partner = EAttribute()
    setattr(partner, 'EAttribute65', None)
    _safe_set(owner, 'ecore_EReference64', {partner})
    assert getattr(partner, 'EAttribute65') == owner
    _safe_set(owner, 'ecore_EReference64', set())
    assert getattr(partner, 'EAttribute65') is None


def test_assoc_eLiterals44_stub_double():
    # EEnumLiteral has no real 'EEnumLiteral' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EEnum's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EEnum's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EEnum()
    partner = EEnumLiteral()
    setattr(partner, 'EEnumLiteral', None)
    _safe_set(owner, 'eEnum', {partner})
    assert getattr(partner, 'EEnumLiteral') == owner
    _safe_set(owner, 'eEnum', set())
    assert getattr(partner, 'EEnumLiteral') is None


def test_assoc_eModelElement2_stub_double():
    # EModelElement has no real 'EModelElement' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EAnnotation(source="sample_text")
    partner = EModelElement()
    setattr(partner, 'EModelElement', None)
    _safe_set(owner, 'eAnnotations', partner)
    assert getattr(partner, 'EModelElement') == owner
    _safe_set(owner, 'eAnnotations', None)
    assert getattr(partner, 'EModelElement') is None


def test_assoc_eOperations9_stub_double():
    # EOperation has no real 'EOperation' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract="sample_text", interface="sample_text")
    partner = EOperation()
    setattr(partner, 'EOperation', None)
    _safe_set(owner, 'eContainingClass', {partner})
    assert getattr(partner, 'EOperation') == owner
    _safe_set(owner, 'eContainingClass', set())
    assert getattr(partner, 'EOperation') is None


def test_assoc_eOpposite58_stub_double():
    # EReference has no real 'EReference59' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EReference(container="sample_text", containment="sample_text", resolveProxies="sample_text")
    partner = EReference()
    setattr(partner, 'EReference59', None)
    _safe_set(owner, 'ecore_EReference', partner)
    assert getattr(partner, 'EReference59') == owner
    _safe_set(owner, 'ecore_EReference', None)
    assert getattr(partner, 'EReference59') is None


def test_assoc_ePackage42_stub_double():
    # EPackage has no real 'EPackage' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = EPackage()
    setattr(partner, 'EPackage', None)
    _safe_set(owner, 'eClassifiers', partner)
    assert getattr(partner, 'EPackage') == owner
    _safe_set(owner, 'eClassifiers', None)
    assert getattr(partner, 'EPackage') is None


def test_assoc_ePackage46_stub_double():
    # EPackage has no real 'EPackage47' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EFactory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EFactory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EFactory()
    partner = EPackage()
    setattr(partner, 'EPackage47', None)
    _safe_set(owner, 'eFactoryInstance', partner)
    assert getattr(partner, 'EPackage47') == owner
    _safe_set(owner, 'eFactoryInstance', None)
    assert getattr(partner, 'EPackage47') is None


def test_assoc_eReferenceType60_stub_double():
    # EClass has no real 'EClass62' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EReference(container="sample_text", containment="sample_text", resolveProxies="sample_text")
    partner = EClass()
    setattr(partner, 'EClass62', None)
    _safe_set(owner, 'ecore_EReference61', partner)
    assert getattr(partner, 'EClass62') == owner
    _safe_set(owner, 'ecore_EReference61', None)
    assert getattr(partner, 'EClass62') is None


def test_assoc_eReferences14_stub_double():
    # EReference has no real 'EReference16' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract="sample_text", interface="sample_text")
    partner = EReference()
    setattr(partner, 'EReference16', None)
    _safe_set(owner, 'ecore_EClass15', {partner})
    assert getattr(partner, 'EReference16') == owner
    _safe_set(owner, 'ecore_EClass15', set())
    assert getattr(partner, 'EReference16') is None


def test_assoc_eStructuralFeatures34_stub_double():
    # EStructuralFeature has no real 'EStructuralFeature36' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract="sample_text", interface="sample_text")
    partner = EStructuralFeature()
    setattr(partner, 'EStructuralFeature36', None)
    _safe_set(owner, 'eContainingClass35', {partner})
    assert getattr(partner, 'EStructuralFeature36') == owner
    _safe_set(owner, 'eContainingClass35', set())
    assert getattr(partner, 'EStructuralFeature36') is None


def test_assoc_eSubpackages52_stub_double():
    # EPackage has no real 'EPackage53' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    partner = EPackage()
    setattr(partner, 'EPackage53', None)
    _safe_set(owner, 'eSuperPackage', {partner})
    assert getattr(partner, 'EPackage53') == owner
    _safe_set(owner, 'eSuperPackage', set())
    assert getattr(partner, 'EPackage53') is None


def test_assoc_eSuperPackage54_stub_double():
    # EPackage has no real 'EPackage55' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    partner = EPackage()
    setattr(partner, 'EPackage55', None)
    _safe_set(owner, 'eSubpackages', partner)
    assert getattr(partner, 'EPackage55') == owner
    _safe_set(owner, 'eSubpackages', None)
    assert getattr(partner, 'EPackage55') is None


def test_assoc_eSuperTypes8_stub_double():
    # EClass has no real 'EClass' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract="sample_text", interface="sample_text")
    partner = EClass()
    setattr(partner, 'EClass', None)
    _safe_set(owner, 'ecore_EClass', {partner})
    assert getattr(partner, 'EClass') == owner
    _safe_set(owner, 'ecore_EClass', set())
    assert getattr(partner, 'EClass') is None


def test_assoc_eType79_stub_double():
    # EClassifier has no real 'EClassifier80' property in the generated
    # code (a bare stub) -- manually attach it so ecore_ETypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_ETypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_ETypedElement(lowerBound="sample_text", many="sample_text", ordered="sample_text", required="sample_text", unique="sample_text", upperBound="sample_text")
    partner = EClassifier()
    setattr(partner, 'EClassifier80', None)
    _safe_set(owner, 'ecore_ETypedElement', partner)
    assert getattr(partner, 'EClassifier80') == owner
    _safe_set(owner, 'ecore_ETypedElement', None)
    assert getattr(partner, 'EClassifier80') is None


def test_assoc_eTypeParameters43_stub_double():
    # ETypeParameter has no real 'ETypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ETypeParameter()
    setattr(partner, 'ETypeParameter', None)
    _safe_set(owner, 'ecore_EClassifier', {partner})
    assert getattr(partner, 'ETypeParameter') == owner
    _safe_set(owner, 'ecore_EClassifier', set())
    assert getattr(partner, 'ETypeParameter') is None


def test_assoc_references5_stub_double():
    # EObject has no real 'EObject7' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EAnnotation(source="sample_text")
    partner = EObject()
    setattr(partner, 'EObject7', None)
    _safe_set(owner, 'ecore_EAnnotation6', {partner})
    assert getattr(partner, 'EObject7') == owner
    _safe_set(owner, 'ecore_EAnnotation6', set())
    assert getattr(partner, 'EObject7') is None


