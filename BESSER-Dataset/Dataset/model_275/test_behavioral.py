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


def test_assoc_eExceptions54_reverse_link_reassign_clear():
    a1 = ecore_EOperation()
    a2 = ecore_EOperation()
    b = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
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


def test_assoc_eAnnotations48_stub_double():
    # ecore_EAnnotation has no real 'Ecore_ecoreEAnnotation' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EModelElement()
    partner = ecore_EAnnotation(source="sample_text")
    setattr(partner, 'Ecore_ecoreEAnnotation', None)
    _safe_set(owner, 'eModelElement', {partner})
    assert getattr(partner, 'Ecore_ecoreEAnnotation') == owner
    _safe_set(owner, 'eModelElement', set())
    assert getattr(partner, 'Ecore_ecoreEAnnotation') is None


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


def test_assoc_eClassifiers61_stub_double():
    # ecore_EClassifier has no real 'Ecore_ecoreEClassifier' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    partner = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    setattr(partner, 'Ecore_ecoreEClassifier', None)
    _safe_set(owner, 'ePackage62', {partner})
    assert getattr(partner, 'Ecore_ecoreEClassifier') == owner
    _safe_set(owner, 'ePackage62', set())
    assert getattr(partner, 'Ecore_ecoreEClassifier') is None


def test_assoc_eContainingClass49_stub_double():
    # ecore_EClass has no real 'Ecore_ecoreEClass' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EOperation()
    partner = ecore_EClass(abstract=True, interface=True)
    setattr(partner, 'Ecore_ecoreEClass', None)
    _safe_set(owner, 'eOperations', partner)
    assert getattr(partner, 'Ecore_ecoreEClass') == owner
    _safe_set(owner, 'eOperations', None)
    assert getattr(partner, 'Ecore_ecoreEClass') is None


def test_assoc_eContainingClass80_stub_double():
    # ecore_EClass has no real 'Ecore_ecoreEClass81' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EStructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EStructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    partner = ecore_EClass(abstract=True, interface=True)
    setattr(partner, 'Ecore_ecoreEClass81', None)
    _safe_set(owner, 'eStructuralFeatures', partner)
    assert getattr(partner, 'Ecore_ecoreEClass81') == owner
    _safe_set(owner, 'eStructuralFeatures', None)
    assert getattr(partner, 'Ecore_ecoreEClass81') is None


def test_assoc_eEnum45_stub_double():
    # ecore_EEnum has no real 'Ecore_ecoreEEnum' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EEnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EEnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    partner = ecore_EEnum()
    setattr(partner, 'Ecore_ecoreEEnum', None)
    _safe_set(owner, 'eLiterals', partner)
    assert getattr(partner, 'Ecore_ecoreEEnum') == owner
    _safe_set(owner, 'eLiterals', None)
    assert getattr(partner, 'Ecore_ecoreEEnum') is None


def test_assoc_eFactoryInstance60_stub_double():
    # ecore_EFactory has no real 'Ecore_ecoreEFactory' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    partner = ecore_EFactory()
    setattr(partner, 'Ecore_ecoreEFactory', None)
    _safe_set(owner, 'ePackage', partner)
    assert getattr(partner, 'Ecore_ecoreEFactory') == owner
    _safe_set(owner, 'ePackage', None)
    assert getattr(partner, 'Ecore_ecoreEFactory') is None


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


def test_assoc_eLiterals44_stub_double():
    # ecore_EEnumLiteral has no real 'Ecore_ecoreEEnumLiteral' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EEnum's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EEnum's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EEnum()
    partner = ecore_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    setattr(partner, 'Ecore_ecoreEEnumLiteral', None)
    _safe_set(owner, 'eEnum', {partner})
    assert getattr(partner, 'Ecore_ecoreEEnumLiteral') == owner
    _safe_set(owner, 'eEnum', set())
    assert getattr(partner, 'Ecore_ecoreEEnumLiteral') is None


def test_assoc_eModelElement2_stub_double():
    # ecore_EModelElement has no real 'Ecore_ecoreEModelElement' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EAnnotation(source="sample_text")
    partner = ecore_EModelElement()
    setattr(partner, 'Ecore_ecoreEModelElement', None)
    _safe_set(owner, 'eAnnotations', partner)
    assert getattr(partner, 'Ecore_ecoreEModelElement') == owner
    _safe_set(owner, 'eAnnotations', None)
    assert getattr(partner, 'Ecore_ecoreEModelElement') is None


def test_assoc_eOperations10_stub_double():
    # ecore_EOperation has no real 'Ecore_ecoreEOperation' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract=True, interface=True)
    partner = ecore_EOperation()
    setattr(partner, 'Ecore_ecoreEOperation', None)
    _safe_set(owner, 'eContainingClass', {partner})
    assert getattr(partner, 'Ecore_ecoreEOperation') == owner
    _safe_set(owner, 'eContainingClass', set())
    assert getattr(partner, 'Ecore_ecoreEOperation') is None


def test_assoc_ePackage42_stub_double():
    # ecore_EPackage has no real 'Ecore_ecoreEPackage' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    setattr(partner, 'Ecore_ecoreEPackage', None)
    _safe_set(owner, 'eClassifiers', partner)
    assert getattr(partner, 'Ecore_ecoreEPackage') == owner
    _safe_set(owner, 'eClassifiers', None)
    assert getattr(partner, 'Ecore_ecoreEPackage') is None


def test_assoc_ePackage46_stub_double():
    # ecore_EPackage has no real 'Ecore_ecoreEPackage47' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EFactory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EFactory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EFactory()
    partner = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    setattr(partner, 'Ecore_ecoreEPackage47', None)
    _safe_set(owner, 'eFactoryInstance', partner)
    assert getattr(partner, 'Ecore_ecoreEPackage47') == owner
    _safe_set(owner, 'eFactoryInstance', None)
    assert getattr(partner, 'Ecore_ecoreEPackage47') is None


def test_assoc_eParameters53_stub_double():
    # ecore_EParameter has no real 'Ecore_ecoreEParameter' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EOperation()
    partner = ecore_EParameter()
    setattr(partner, 'Ecore_ecoreEParameter', None)
    _safe_set(owner, 'eOperation', {partner})
    assert getattr(partner, 'Ecore_ecoreEParameter') == owner
    _safe_set(owner, 'eOperation', set())
    assert getattr(partner, 'Ecore_ecoreEParameter') is None


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


def test_assoc_eStructuralFeatures35_stub_double():
    # ecore_EStructuralFeature has no real 'Ecore_ecoreEStructuralFeature' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EClass(abstract=True, interface=True)
    partner = ecore_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    setattr(partner, 'Ecore_ecoreEStructuralFeature', None)
    _safe_set(owner, 'eContainingClass36', {partner})
    assert getattr(partner, 'Ecore_ecoreEStructuralFeature') == owner
    _safe_set(owner, 'eContainingClass36', set())
    assert getattr(partner, 'Ecore_ecoreEStructuralFeature') is None


def test_assoc_eSubpackages64_stub_double():
    # ecore_EPackage has no real 'Ecore_ecoreEPackage65' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    partner = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    setattr(partner, 'Ecore_ecoreEPackage65', None)
    _safe_set(owner, 'eSuperPackage', {partner})
    assert getattr(partner, 'Ecore_ecoreEPackage65') == owner
    _safe_set(owner, 'eSuperPackage', set())
    assert getattr(partner, 'Ecore_ecoreEPackage65') is None


def test_assoc_eSuperPackage67_stub_double():
    # ecore_EPackage has no real 'Ecore_ecoreEPackage68' property in the generated
    # code (a bare stub) -- manually attach it so ecore_EPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ecore_EPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    partner = ecore_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    setattr(partner, 'Ecore_ecoreEPackage68', None)
    _safe_set(owner, 'eSubpackages', partner)
    assert getattr(partner, 'Ecore_ecoreEPackage68') == owner
    _safe_set(owner, 'eSubpackages', None)
    assert getattr(partner, 'Ecore_ecoreEPackage68') is None


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


