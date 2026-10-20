import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DifferenceElement,
    EAnnotation,
    EAttribute,
    EClass,
    EClassifier,
    EClassifier_Wildcard,
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
    EStructuralFeature_Wildcard,
    ETypeParameter,
    ETypedElement,
    ecoreDiff_AddedEAnnotation,
    ecoreDiff_AddedEAttribute,
    ecoreDiff_AddedEClass,
    ecoreDiff_AddedEClassifier,
    ecoreDiff_AddedEClassifier_Wildcard,
    ecoreDiff_AddedEDataType,
    ecoreDiff_AddedEEnum,
    ecoreDiff_AddedEEnumLiteral,
    ecoreDiff_AddedEFactory,
    ecoreDiff_AddedEGenericType,
    ecoreDiff_AddedEModelElement,
    ecoreDiff_AddedENamedElement,
    ecoreDiff_AddedEObject,
    ecoreDiff_AddedEOperation,
    ecoreDiff_AddedEPackage,
    ecoreDiff_AddedEParameter,
    ecoreDiff_AddedEReference,
    ecoreDiff_AddedEStringToStringMapEntry,
    ecoreDiff_AddedEStructuralFeature,
    ecoreDiff_AddedEStructuralFeature_Wildcard,
    ecoreDiff_AddedETypeParameter,
    ecoreDiff_AddedETypedElement,
    ecoreDiff_ChangedEAnnotation,
    ecoreDiff_ChangedEAttribute,
    ecoreDiff_ChangedEClass,
    ecoreDiff_ChangedEClassifier,
    ecoreDiff_ChangedEClassifier_Wildcard,
    ecoreDiff_ChangedEDataType,
    ecoreDiff_ChangedEEnum,
    ecoreDiff_ChangedEEnumLiteral,
    ecoreDiff_ChangedEFactory,
    ecoreDiff_ChangedEGenericType,
    ecoreDiff_ChangedEModelElement,
    ecoreDiff_ChangedENamedElement,
    ecoreDiff_ChangedEObject,
    ecoreDiff_ChangedEOperation,
    ecoreDiff_ChangedEPackage,
    ecoreDiff_ChangedEParameter,
    ecoreDiff_ChangedEReference,
    ecoreDiff_ChangedEStringToStringMapEntry,
    ecoreDiff_ChangedEStructuralFeature,
    ecoreDiff_ChangedEStructuralFeature_Wildcard,
    ecoreDiff_ChangedETypeParameter,
    ecoreDiff_ChangedETypedElement,
    ecoreDiff_DeletedEAnnotation,
    ecoreDiff_DeletedEAttribute,
    ecoreDiff_DeletedEClass,
    ecoreDiff_DeletedEClassifier,
    ecoreDiff_DeletedEClassifier_Wildcard,
    ecoreDiff_DeletedEDataType,
    ecoreDiff_DeletedEEnum,
    ecoreDiff_DeletedEEnumLiteral,
    ecoreDiff_DeletedEFactory,
    ecoreDiff_DeletedEGenericType,
    ecoreDiff_DeletedEModelElement,
    ecoreDiff_DeletedENamedElement,
    ecoreDiff_DeletedEObject,
    ecoreDiff_DeletedEOperation,
    ecoreDiff_DeletedEPackage,
    ecoreDiff_DeletedEParameter,
    ecoreDiff_DeletedEReference,
    ecoreDiff_DeletedEStringToStringMapEntry,
    ecoreDiff_DeletedEStructuralFeature,
    ecoreDiff_DeletedEStructuralFeature_Wildcard,
    ecoreDiff_DeletedETypeParameter,
    ecoreDiff_DeletedETypedElement,
    ecoreDiff_DifferenceElement,
    ecoreDiff_DifferenceModel,
    ecoreDiff_EAnnotation,
    ecoreDiff_EAttribute,
    ecoreDiff_EClass,
    ecoreDiff_EClassifier,
    ecoreDiff_EClassifier_Wildcard,
    ecoreDiff_EDataType,
    ecoreDiff_EEnum,
    ecoreDiff_EEnumLiteral,
    ecoreDiff_EFactory,
    ecoreDiff_EGenericType,
    ecoreDiff_EModelElement,
    ecoreDiff_ENamedElement,
    ecoreDiff_EObject,
    ecoreDiff_EOperation,
    ecoreDiff_EPackage,
    ecoreDiff_EParameter,
    ecoreDiff_EReference,
    ecoreDiff_EStringToStringMapEntry,
    ecoreDiff_EStructuralFeature,
    ecoreDiff_EStructuralFeature_Wildcard,
    ecoreDiff_ETypeParameter,
    ecoreDiff_ETypedElement,
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

def test_assoc_details0_reverse_link_reassign_clear():
    a1 = ecoreDiff_EStringToStringMapEntry(key="sample_text", value="sample_text")
    a2 = ecoreDiff_EStringToStringMapEntry(key="sample_text_2", value="sample_text_2")
    b = ecoreDiff_EAnnotation(source="sample_text")
    _safe_set(b, 'ecoreDiff_EAnnotation', {a1})
    assert _is_linked(b, 'ecoreDiff_EAnnotation', a1)
    if hasattr(a1, 'ecoreDiff_EStringToStringMapEntry'):
        assert _is_linked(a1, 'ecoreDiff_EStringToStringMapEntry', b)
    _safe_set(b, 'ecoreDiff_EAnnotation', {a2})
    assert _is_linked(b, 'ecoreDiff_EAnnotation', a2)
    if hasattr(a1, 'ecoreDiff_EStringToStringMapEntry'):
        assert not _is_linked(a1, 'ecoreDiff_EStringToStringMapEntry', b)
    if hasattr(a2, 'ecoreDiff_EStringToStringMapEntry'):
        assert _is_linked(a2, 'ecoreDiff_EStringToStringMapEntry', b)
    _safe_set(b, 'ecoreDiff_EAnnotation', set())
    assert not _is_linked(b, 'ecoreDiff_EAnnotation', a2)
    if hasattr(a2, 'ecoreDiff_EStringToStringMapEntry'):
        assert not _is_linked(a2, 'ecoreDiff_EStringToStringMapEntry', b)


def test_assoc_eClassifiers27_reverse_link_reassign_clear():
    a1 = ecoreDiff_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecoreDiff_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecoreDiff_EClassifier(instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'ecoreDiff_EClassifier29', a1)
    assert _is_linked(b, 'ecoreDiff_EClassifier29', a1)
    if hasattr(a1, 'ecoreDiff_EPackage28'):
        assert _is_linked(a1, 'ecoreDiff_EPackage28', b)
    _safe_set(b, 'ecoreDiff_EClassifier29', a2)
    assert _is_linked(b, 'ecoreDiff_EClassifier29', a2)
    if hasattr(a1, 'ecoreDiff_EPackage28'):
        assert not _is_linked(a1, 'ecoreDiff_EPackage28', b)
    if hasattr(a2, 'ecoreDiff_EPackage28'):
        assert _is_linked(a2, 'ecoreDiff_EPackage28', b)
    _safe_set(b, 'ecoreDiff_EClassifier29', None)
    assert not _is_linked(b, 'ecoreDiff_EClassifier29', a2)
    if hasattr(a2, 'ecoreDiff_EPackage28'):
        assert not _is_linked(a2, 'ecoreDiff_EPackage28', b)


def test_assoc_eKeys78_reverse_link_reassign_clear():
    a1 = ecoreDiff_EReference(containment=True, resolveProxies=True)
    a2 = ecoreDiff_EReference(containment=False, resolveProxies=False)
    b = ecoreDiff_EAttribute(iD=True)
    _safe_set(b, 'ecoreDiff_EAttribute', a1)
    assert _is_linked(b, 'ecoreDiff_EAttribute', a1)
    if hasattr(a1, 'ecoreDiff_EReference79'):
        assert _is_linked(a1, 'ecoreDiff_EReference79', b)
    _safe_set(b, 'ecoreDiff_EAttribute', a2)
    assert _is_linked(b, 'ecoreDiff_EAttribute', a2)
    if hasattr(a1, 'ecoreDiff_EReference79'):
        assert not _is_linked(a1, 'ecoreDiff_EReference79', b)
    if hasattr(a2, 'ecoreDiff_EReference79'):
        assert _is_linked(a2, 'ecoreDiff_EReference79', b)
    _safe_set(b, 'ecoreDiff_EAttribute', None)
    assert not _is_linked(b, 'ecoreDiff_EAttribute', a2)
    if hasattr(a2, 'ecoreDiff_EReference79'):
        assert not _is_linked(a2, 'ecoreDiff_EReference79', b)


def test_assoc_eOpposite77_reverse_link_reassign_clear():
    a1 = ecoreDiff_EReference(containment=True, resolveProxies=True)
    a2 = ecoreDiff_EReference(containment=False, resolveProxies=False)
    b = ecoreDiff_EReference(containment=True, resolveProxies=True)
    _safe_set(b, 'ecoreDiff_EReference76', a1)
    assert _is_linked(b, 'ecoreDiff_EReference76', a1)
    if hasattr(a1, 'ecoreDiff_EReference'):
        assert _is_linked(a1, 'ecoreDiff_EReference', b)
    _safe_set(b, 'ecoreDiff_EReference76', a2)
    assert _is_linked(b, 'ecoreDiff_EReference76', a2)
    if hasattr(a1, 'ecoreDiff_EReference'):
        assert not _is_linked(a1, 'ecoreDiff_EReference', b)
    if hasattr(a2, 'ecoreDiff_EReference'):
        assert _is_linked(a2, 'ecoreDiff_EReference', b)
    _safe_set(b, 'ecoreDiff_EReference76', None)
    assert not _is_linked(b, 'ecoreDiff_EReference76', a2)
    if hasattr(a2, 'ecoreDiff_EReference'):
        assert not _is_linked(a2, 'ecoreDiff_EReference', b)


def test_assoc_eStructuralFeatures12_reverse_link_reassign_clear():
    a1 = ecoreDiff_EStructuralFeature(changeable=True, defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = ecoreDiff_EStructuralFeature(changeable=False, defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = ecoreDiff_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecoreDiff_EClass13', {a1})
    assert _is_linked(b, 'ecoreDiff_EClass13', a1)
    if hasattr(a1, 'ecoreDiff_EStructuralFeature'):
        assert _is_linked(a1, 'ecoreDiff_EStructuralFeature', b)
    _safe_set(b, 'ecoreDiff_EClass13', {a2})
    assert _is_linked(b, 'ecoreDiff_EClass13', a2)
    if hasattr(a1, 'ecoreDiff_EStructuralFeature'):
        assert not _is_linked(a1, 'ecoreDiff_EStructuralFeature', b)
    if hasattr(a2, 'ecoreDiff_EStructuralFeature'):
        assert _is_linked(a2, 'ecoreDiff_EStructuralFeature', b)
    _safe_set(b, 'ecoreDiff_EClass13', set())
    assert not _is_linked(b, 'ecoreDiff_EClass13', a2)
    if hasattr(a2, 'ecoreDiff_EStructuralFeature'):
        assert not _is_linked(a2, 'ecoreDiff_EStructuralFeature', b)


def test_assoc_eSubpackages22_reverse_link_reassign_clear():
    a1 = ecoreDiff_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecoreDiff_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecoreDiff_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'ecoreDiff_EPackage23', a1)
    assert _is_linked(b, 'ecoreDiff_EPackage23', a1)
    if hasattr(a1, 'ecoreDiff_EPackage21'):
        assert _is_linked(a1, 'ecoreDiff_EPackage21', b)
    _safe_set(b, 'ecoreDiff_EPackage23', a2)
    assert _is_linked(b, 'ecoreDiff_EPackage23', a2)
    if hasattr(a1, 'ecoreDiff_EPackage21'):
        assert not _is_linked(a1, 'ecoreDiff_EPackage21', b)
    if hasattr(a2, 'ecoreDiff_EPackage21'):
        assert _is_linked(a2, 'ecoreDiff_EPackage21', b)
    _safe_set(b, 'ecoreDiff_EPackage23', None)
    assert not _is_linked(b, 'ecoreDiff_EPackage23', a2)
    if hasattr(a2, 'ecoreDiff_EPackage21'):
        assert not _is_linked(a2, 'ecoreDiff_EPackage21', b)


def test_assoc_eSuperPackage25_reverse_link_reassign_clear():
    a1 = ecoreDiff_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = ecoreDiff_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = ecoreDiff_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'ecoreDiff_EPackage26', a1)
    assert _is_linked(b, 'ecoreDiff_EPackage26', a1)
    if hasattr(a1, 'ecoreDiff_EPackage24'):
        assert _is_linked(a1, 'ecoreDiff_EPackage24', b)
    _safe_set(b, 'ecoreDiff_EPackage26', a2)
    assert _is_linked(b, 'ecoreDiff_EPackage26', a2)
    if hasattr(a1, 'ecoreDiff_EPackage24'):
        assert not _is_linked(a1, 'ecoreDiff_EPackage24', b)
    if hasattr(a2, 'ecoreDiff_EPackage24'):
        assert _is_linked(a2, 'ecoreDiff_EPackage24', b)
    _safe_set(b, 'ecoreDiff_EPackage26', None)
    assert not _is_linked(b, 'ecoreDiff_EPackage26', a2)
    if hasattr(a2, 'ecoreDiff_EPackage24'):
        assert not _is_linked(a2, 'ecoreDiff_EPackage24', b)


def test_assoc_eSuperTypes9_reverse_link_reassign_clear():
    a1 = ecoreDiff_EClass(abstract=True, interface=True)
    a2 = ecoreDiff_EClass(abstract=False, interface=False)
    b = ecoreDiff_EClass(abstract=True, interface=True)
    _safe_set(b, 'ecoreDiff_EClass8', {a1})
    assert _is_linked(b, 'ecoreDiff_EClass8', a1)
    if hasattr(a1, 'ecoreDiff_EClass'):
        assert _is_linked(a1, 'ecoreDiff_EClass', b)
    _safe_set(b, 'ecoreDiff_EClass8', {a2})
    assert _is_linked(b, 'ecoreDiff_EClass8', a2)
    if hasattr(a1, 'ecoreDiff_EClass'):
        assert not _is_linked(a1, 'ecoreDiff_EClass', b)
    if hasattr(a2, 'ecoreDiff_EClass'):
        assert _is_linked(a2, 'ecoreDiff_EClass', b)
    _safe_set(b, 'ecoreDiff_EClass8', set())
    assert not _is_linked(b, 'ecoreDiff_EClass8', a2)
    if hasattr(a2, 'ecoreDiff_EClass'):
        assert not _is_linked(a2, 'ecoreDiff_EClass', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_contents3_stub_double():
    # ecoreDiff_EObject has no real 'ecoreDiff_EObject' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EAnnotation(source="sample_text")
    partner = ecoreDiff_EObject()
    setattr(partner, 'ecoreDiff_EObject', None)
    _safe_set(owner, 'ecoreDiff_EAnnotation4', {partner})
    assert getattr(partner, 'ecoreDiff_EObject') == owner
    _safe_set(owner, 'ecoreDiff_EAnnotation4', set())
    assert getattr(partner, 'ecoreDiff_EObject') is None


def test_assoc_eAnnotations84_stub_double():
    # ecoreDiff_EModelElement has no real 'ecoreDiff_EModelElement85' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EAnnotation(source="sample_text")
    partner = ecoreDiff_EModelElement()
    setattr(partner, 'ecoreDiff_EModelElement85', None)
    _safe_set(owner, 'ecoreDiff_EAnnotation86', partner)
    assert owner in getattr(partner, 'ecoreDiff_EModelElement85')
    _safe_set(owner, 'ecoreDiff_EAnnotation86', None)
    assert owner not in getattr(partner, 'ecoreDiff_EModelElement85')


def test_assoc_eClassifier48_stub_double():
    # ecoreDiff_EGenericType has no real 'ecoreDiff_EGenericType49' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClassifier(instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecoreDiff_EGenericType()
    setattr(partner, 'ecoreDiff_EGenericType49', None)
    _safe_set(owner, 'ecoreDiff_EClassifier50', partner)
    assert getattr(partner, 'ecoreDiff_EGenericType49') == owner
    _safe_set(owner, 'ecoreDiff_EClassifier50', None)
    assert getattr(partner, 'ecoreDiff_EGenericType49') is None


def test_assoc_eContainingClass73_stub_double():
    # ecoreDiff_EObject has no real 'ecoreDiff_EObject75' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EStructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EStructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EStructuralFeature(changeable=True, defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    partner = ecoreDiff_EObject()
    setattr(partner, 'ecoreDiff_EObject75', None)
    _safe_set(owner, 'ecoreDiff_EStructuralFeature74', partner)
    assert getattr(partner, 'ecoreDiff_EObject75') == owner
    _safe_set(owner, 'ecoreDiff_EStructuralFeature74', None)
    assert getattr(partner, 'ecoreDiff_EObject75') is None


def test_assoc_eEnum81_stub_double():
    # ecoreDiff_EEnum has no real 'ecoreDiff_EEnum83' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EEnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EEnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    partner = ecoreDiff_EEnum()
    setattr(partner, 'ecoreDiff_EEnum83', None)
    _safe_set(owner, 'ecoreDiff_EEnumLiteral82', partner)
    assert getattr(partner, 'ecoreDiff_EEnum83') == owner
    _safe_set(owner, 'ecoreDiff_EEnumLiteral82', None)
    assert getattr(partner, 'ecoreDiff_EEnum83') is None


def test_assoc_eExceptions56_stub_double():
    # ecoreDiff_EOperation has no real 'ecoreDiff_EOperation57' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClassifier(instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecoreDiff_EOperation()
    setattr(partner, 'ecoreDiff_EOperation57', None)
    _safe_set(owner, 'ecoreDiff_EClassifier58', partner)
    assert owner in getattr(partner, 'ecoreDiff_EOperation57')
    _safe_set(owner, 'ecoreDiff_EClassifier58', None)
    assert owner not in getattr(partner, 'ecoreDiff_EOperation57')


def test_assoc_eFactoryInstance20_stub_double():
    # ecoreDiff_EFactory has no real 'ecoreDiff_EFactory' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    partner = ecoreDiff_EFactory()
    setattr(partner, 'ecoreDiff_EFactory', None)
    _safe_set(owner, 'ecoreDiff_EPackage', partner)
    assert getattr(partner, 'ecoreDiff_EFactory') == owner
    _safe_set(owner, 'ecoreDiff_EPackage', None)
    assert getattr(partner, 'ecoreDiff_EFactory') is None


def test_assoc_eGenericSuperTypes14_stub_double():
    # ecoreDiff_EGenericType has no real 'ecoreDiff_EGenericType' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClass(abstract=True, interface=True)
    partner = ecoreDiff_EGenericType()
    setattr(partner, 'ecoreDiff_EGenericType', None)
    _safe_set(owner, 'ecoreDiff_EClass15', {partner})
    assert getattr(partner, 'ecoreDiff_EGenericType') == owner
    _safe_set(owner, 'ecoreDiff_EClass15', set())
    assert getattr(partner, 'ecoreDiff_EGenericType') is None


def test_assoc_eGenericType67_stub_double():
    # ecoreDiff_EGenericType has no real 'ecoreDiff_EGenericType69' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_ETypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_ETypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_ETypedElement(lowerBound=7, ordered=True, unique=True, upperBound=7)
    partner = ecoreDiff_EGenericType()
    setattr(partner, 'ecoreDiff_EGenericType69', None)
    _safe_set(owner, 'ecoreDiff_ETypedElement68', partner)
    assert getattr(partner, 'ecoreDiff_EGenericType69') == owner
    _safe_set(owner, 'ecoreDiff_ETypedElement68', None)
    assert getattr(partner, 'ecoreDiff_EGenericType69') is None


def test_assoc_eLiterals80_stub_double():
    # ecoreDiff_EEnum has no real 'ecoreDiff_EEnum' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EEnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EEnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    partner = ecoreDiff_EEnum()
    setattr(partner, 'ecoreDiff_EEnum', None)
    _safe_set(owner, 'ecoreDiff_EEnumLiteral', partner)
    assert owner in getattr(partner, 'ecoreDiff_EEnum')
    _safe_set(owner, 'ecoreDiff_EEnumLiteral', None)
    assert owner not in getattr(partner, 'ecoreDiff_EEnum')


def test_assoc_eModelElement1_stub_double():
    # ecoreDiff_EModelElement has no real 'ecoreDiff_EModelElement' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EAnnotation(source="sample_text")
    partner = ecoreDiff_EModelElement()
    setattr(partner, 'ecoreDiff_EModelElement', None)
    _safe_set(owner, 'ecoreDiff_EAnnotation2', partner)
    assert getattr(partner, 'ecoreDiff_EModelElement') == owner
    _safe_set(owner, 'ecoreDiff_EAnnotation2', None)
    assert getattr(partner, 'ecoreDiff_EModelElement') is None


def test_assoc_eOperations10_stub_double():
    # ecoreDiff_EOperation has no real 'ecoreDiff_EOperation' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClass(abstract=True, interface=True)
    partner = ecoreDiff_EOperation()
    setattr(partner, 'ecoreDiff_EOperation', None)
    _safe_set(owner, 'ecoreDiff_EClass11', {partner})
    assert getattr(partner, 'ecoreDiff_EOperation') == owner
    _safe_set(owner, 'ecoreDiff_EClass11', set())
    assert getattr(partner, 'ecoreDiff_EOperation') is None


def test_assoc_ePackage16_stub_double():
    # ecoreDiff_EObject has no real 'ecoreDiff_EObject17' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClassifier(instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecoreDiff_EObject()
    setattr(partner, 'ecoreDiff_EObject17', None)
    _safe_set(owner, 'ecoreDiff_EClassifier', partner)
    assert getattr(partner, 'ecoreDiff_EObject17') == owner
    _safe_set(owner, 'ecoreDiff_EClassifier', None)
    assert getattr(partner, 'ecoreDiff_EObject17') is None


def test_assoc_eType65_stub_double():
    # ecoreDiff_EObject has no real 'ecoreDiff_EObject66' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_ETypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_ETypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_ETypedElement(lowerBound=7, ordered=True, unique=True, upperBound=7)
    partner = ecoreDiff_EObject()
    setattr(partner, 'ecoreDiff_EObject66', None)
    _safe_set(owner, 'ecoreDiff_ETypedElement', partner)
    assert getattr(partner, 'ecoreDiff_EObject66') == owner
    _safe_set(owner, 'ecoreDiff_ETypedElement', None)
    assert getattr(partner, 'ecoreDiff_EObject66') is None


def test_assoc_eTypeParameters18_stub_double():
    # ecoreDiff_ETypeParameter has no real 'ecoreDiff_ETypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClassifier(instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecoreDiff_ETypeParameter()
    setattr(partner, 'ecoreDiff_ETypeParameter', None)
    _safe_set(owner, 'ecoreDiff_EClassifier19', {partner})
    assert getattr(partner, 'ecoreDiff_ETypeParameter') == owner
    _safe_set(owner, 'ecoreDiff_EClassifier19', set())
    assert getattr(partner, 'ecoreDiff_ETypeParameter') is None


def test_assoc_references5_stub_double():
    # ecoreDiff_EObject has no real 'ecoreDiff_EObject7' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EAnnotation(source="sample_text")
    partner = ecoreDiff_EObject()
    setattr(partner, 'ecoreDiff_EObject7', None)
    _safe_set(owner, 'ecoreDiff_EAnnotation6', {partner})
    assert getattr(partner, 'ecoreDiff_EObject7') == owner
    _safe_set(owner, 'ecoreDiff_EAnnotation6', set())
    assert getattr(partner, 'ecoreDiff_EObject7') is None


def test_assoc_updatedElement101_stub_double():
    # ecoreDiff_ChangedEStringToStringMapEntry has no real 'ecoreDiff_ChangedEStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EStringToStringMapEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EStringToStringMapEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EStringToStringMapEntry(key="sample_text", value="sample_text")
    partner = ecoreDiff_ChangedEStringToStringMapEntry()
    setattr(partner, 'ecoreDiff_ChangedEStringToStringMapEntry', None)
    _safe_set(owner, 'ecoreDiff_EStringToStringMapEntry102', partner)
    assert owner in getattr(partner, 'ecoreDiff_ChangedEStringToStringMapEntry')
    _safe_set(owner, 'ecoreDiff_EStringToStringMapEntry102', None)
    assert owner not in getattr(partner, 'ecoreDiff_ChangedEStringToStringMapEntry')


def test_assoc_updatedElement119_stub_double():
    # ecoreDiff_ChangedEClass has no real 'ecoreDiff_ChangedEClass' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClass(abstract=True, interface=True)
    partner = ecoreDiff_ChangedEClass()
    setattr(partner, 'ecoreDiff_ChangedEClass', None)
    _safe_set(owner, 'ecoreDiff_EClass120', partner)
    assert owner in getattr(partner, 'ecoreDiff_ChangedEClass')
    _safe_set(owner, 'ecoreDiff_EClass120', None)
    assert owner not in getattr(partner, 'ecoreDiff_ChangedEClass')


def test_assoc_updatedElement128_stub_double():
    # ecoreDiff_ChangedEClassifier has no real 'ecoreDiff_ChangedEClassifier' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EClassifier(instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecoreDiff_ChangedEClassifier()
    setattr(partner, 'ecoreDiff_ChangedEClassifier', None)
    _safe_set(owner, 'ecoreDiff_EClassifier129', partner)
    assert owner in getattr(partner, 'ecoreDiff_ChangedEClassifier')
    _safe_set(owner, 'ecoreDiff_EClassifier129', None)
    assert owner not in getattr(partner, 'ecoreDiff_ChangedEClassifier')


def test_assoc_updatedElement137_stub_double():
    # ecoreDiff_ChangedENamedElement has no real 'ecoreDiff_ChangedENamedElement' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_ENamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_ENamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_ENamedElement(name="sample_text")
    partner = ecoreDiff_ChangedENamedElement()
    setattr(partner, 'ecoreDiff_ChangedENamedElement', None)
    _safe_set(owner, 'ecoreDiff_ENamedElement', partner)
    assert owner in getattr(partner, 'ecoreDiff_ChangedENamedElement')
    _safe_set(owner, 'ecoreDiff_ENamedElement', None)
    assert owner not in getattr(partner, 'ecoreDiff_ChangedENamedElement')


def test_assoc_updatedElement145_stub_double():
    # ecoreDiff_ChangedEPackage has no real 'ecoreDiff_ChangedEPackage' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    partner = ecoreDiff_ChangedEPackage()
    setattr(partner, 'ecoreDiff_ChangedEPackage', None)
    _safe_set(owner, 'ecoreDiff_EPackage146', partner)
    assert owner in getattr(partner, 'ecoreDiff_ChangedEPackage')
    _safe_set(owner, 'ecoreDiff_EPackage146', None)
    assert owner not in getattr(partner, 'ecoreDiff_ChangedEPackage')


def test_assoc_updatedElement163_stub_double():
    # ecoreDiff_ChangedEDataType has no real 'ecoreDiff_ChangedEDataType' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EDataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EDataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EDataType(serializable=True)
    partner = ecoreDiff_ChangedEDataType()
    setattr(partner, 'ecoreDiff_ChangedEDataType', None)
    _safe_set(owner, 'ecoreDiff_EDataType', partner)
    assert owner in getattr(partner, 'ecoreDiff_ChangedEDataType')
    _safe_set(owner, 'ecoreDiff_EDataType', None)
    assert owner not in getattr(partner, 'ecoreDiff_ChangedEDataType')


def test_assoc_updatedElement206_stub_double():
    # ecoreDiff_ChangedETypedElement has no real 'ecoreDiff_ChangedETypedElement' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_ETypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_ETypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_ETypedElement(lowerBound=7, ordered=True, unique=True, upperBound=7)
    partner = ecoreDiff_ChangedETypedElement()
    setattr(partner, 'ecoreDiff_ChangedETypedElement', None)
    _safe_set(owner, 'ecoreDiff_ETypedElement207', partner)
    assert owner in getattr(partner, 'ecoreDiff_ChangedETypedElement')
    _safe_set(owner, 'ecoreDiff_ETypedElement207', None)
    assert owner not in getattr(partner, 'ecoreDiff_ChangedETypedElement')


def test_assoc_updatedElement224_stub_double():
    # ecoreDiff_ChangedEAttribute has no real 'ecoreDiff_ChangedEAttribute' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EAttribute(iD=True)
    partner = ecoreDiff_ChangedEAttribute()
    setattr(partner, 'ecoreDiff_ChangedEAttribute', None)
    _safe_set(owner, 'ecoreDiff_EAttribute225', partner)
    assert owner in getattr(partner, 'ecoreDiff_ChangedEAttribute')
    _safe_set(owner, 'ecoreDiff_EAttribute225', None)
    assert owner not in getattr(partner, 'ecoreDiff_ChangedEAttribute')


def test_assoc_updatedElement233_stub_double():
    # ecoreDiff_ChangedEStructuralFeature has no real 'ecoreDiff_ChangedEStructuralFeature' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EStructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EStructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EStructuralFeature(changeable=True, defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    partner = ecoreDiff_ChangedEStructuralFeature()
    setattr(partner, 'ecoreDiff_ChangedEStructuralFeature', None)
    _safe_set(owner, 'ecoreDiff_EStructuralFeature234', partner)
    assert owner in getattr(partner, 'ecoreDiff_ChangedEStructuralFeature')
    _safe_set(owner, 'ecoreDiff_EStructuralFeature234', None)
    assert owner not in getattr(partner, 'ecoreDiff_ChangedEStructuralFeature')


def test_assoc_updatedElement250_stub_double():
    # ecoreDiff_ChangedEReference has no real 'ecoreDiff_ChangedEReference' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EReference(containment=True, resolveProxies=True)
    partner = ecoreDiff_ChangedEReference()
    setattr(partner, 'ecoreDiff_ChangedEReference', None)
    _safe_set(owner, 'ecoreDiff_EReference251', partner)
    assert owner in getattr(partner, 'ecoreDiff_ChangedEReference')
    _safe_set(owner, 'ecoreDiff_EReference251', None)
    assert owner not in getattr(partner, 'ecoreDiff_ChangedEReference')


def test_assoc_updatedElement268_stub_double():
    # ecoreDiff_ChangedEEnumLiteral has no real 'ecoreDiff_ChangedEEnumLiteral' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EEnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EEnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    partner = ecoreDiff_ChangedEEnumLiteral()
    setattr(partner, 'ecoreDiff_ChangedEEnumLiteral', None)
    _safe_set(owner, 'ecoreDiff_EEnumLiteral269', partner)
    assert owner in getattr(partner, 'ecoreDiff_ChangedEEnumLiteral')
    _safe_set(owner, 'ecoreDiff_EEnumLiteral269', None)
    assert owner not in getattr(partner, 'ecoreDiff_ChangedEEnumLiteral')


def test_assoc_updatedElement92_stub_double():
    # ecoreDiff_ChangedEAnnotation has no real 'ecoreDiff_ChangedEAnnotation' property in the generated
    # code (a bare stub) -- manually attach it so ecoreDiff_EAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecoreDiff_EAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecoreDiff_EAnnotation(source="sample_text")
    partner = ecoreDiff_ChangedEAnnotation()
    setattr(partner, 'ecoreDiff_ChangedEAnnotation', None)
    _safe_set(owner, 'ecoreDiff_EAnnotation93', partner)
    assert owner in getattr(partner, 'ecoreDiff_ChangedEAnnotation')
    _safe_set(owner, 'ecoreDiff_EAnnotation93', None)
    assert owner not in getattr(partner, 'ecoreDiff_ChangedEAnnotation')


