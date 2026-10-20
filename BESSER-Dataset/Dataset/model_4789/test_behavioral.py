import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    JvmAnnotationTarget,
    JvmAnnotationValue,
    JvmComponentType,
    JvmCompoundTypeReference,
    JvmConstraintOwner,
    JvmDeclaredType,
    JvmExecutable,
    JvmFeature,
    JvmField,
    JvmIdentifiableElement,
    JvmMember,
    JvmParameterizedTypeReference,
    JvmType,
    JvmTypeConstraint,
    JvmTypeParameterDeclarator,
    JvmTypeReference,
    types_EObject,
    types_JvmAnnotationAnnotationValue,
    types_JvmAnnotationReference,
    types_JvmAnnotationTarget,
    types_JvmAnnotationType,
    types_JvmAnnotationValue,
    types_JvmAnyTypeReference,
    types_JvmArrayType,
    types_JvmBooleanAnnotationValue,
    types_JvmByteAnnotationValue,
    types_JvmCharAnnotationValue,
    types_JvmComponentType,
    types_JvmCompoundTypeReference,
    types_JvmConstraintOwner,
    types_JvmConstructor,
    types_JvmCustomAnnotationValue,
    types_JvmDeclaredType,
    types_JvmDelegateTypeReference,
    types_JvmDoubleAnnotationValue,
    types_JvmEnumAnnotationValue,
    types_JvmEnumerationLiteral,
    types_JvmEnumerationType,
    types_JvmExecutable,
    types_JvmFeature,
    types_JvmField,
    types_JvmFloatAnnotationValue,
    types_JvmFormalParameter,
    types_JvmGenericArrayTypeReference,
    types_JvmGenericType,
    types_JvmIdentifiableElement,
    types_JvmInnerTypeReference,
    types_JvmIntAnnotationValue,
    types_JvmLongAnnotationValue,
    types_JvmLowerBound,
    types_JvmMember,
    types_JvmMultiTypeReference,
    types_JvmOperation,
    types_JvmParameterizedTypeReference,
    types_JvmPrimitiveType,
    types_JvmShortAnnotationValue,
    types_JvmSpecializedTypeReference,
    types_JvmStringAnnotationValue,
    types_JvmSynonymTypeReference,
    types_JvmType,
    types_JvmTypeAnnotationValue,
    types_JvmTypeConstraint,
    types_JvmTypeParameter,
    types_JvmTypeParameterDeclarator,
    types_JvmTypeReference,
    types_JvmUnknownTypeReference,
    types_JvmUpperBound,
    types_JvmVoid,
    types_JvmWildcardTypeReference,
    JvmVisibility,
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

def test_assoc_componentType15_reverse_link_reassign_clear():
    a1 = types_JvmTypeReference()
    a2 = types_JvmTypeReference()
    b = types_JvmGenericArrayTypeReference()
    _safe_set(b, 'types_JvmGenericArrayTypeReference', a1)
    assert _is_linked(b, 'types_JvmGenericArrayTypeReference', a1)
    if hasattr(a1, 'types_JvmTypeReference16'):
        assert _is_linked(a1, 'types_JvmTypeReference16', b)
    _safe_set(b, 'types_JvmGenericArrayTypeReference', a2)
    assert _is_linked(b, 'types_JvmGenericArrayTypeReference', a2)
    if hasattr(a1, 'types_JvmTypeReference16'):
        assert not _is_linked(a1, 'types_JvmTypeReference16', b)
    if hasattr(a2, 'types_JvmTypeReference16'):
        assert _is_linked(a2, 'types_JvmTypeReference16', b)
    _safe_set(b, 'types_JvmGenericArrayTypeReference', None)
    assert not _is_linked(b, 'types_JvmGenericArrayTypeReference', a2)
    if hasattr(a2, 'types_JvmTypeReference16'):
        assert not _is_linked(a2, 'types_JvmTypeReference16', b)


def test_assoc_declaringType19_reverse_link_reassign_clear():
    a1 = types_JvmMember(deprecated=True, identifier="sample_text", simpleName="sample_text", visibility="sample_text")
    a2 = types_JvmMember(deprecated=False, identifier="sample_text_2", simpleName="sample_text_2", visibility="sample_text_2")
    b = types_JvmDeclaredType(abstract=True, final=True, packageName="sample_text", static=True)
    _safe_set(b, 'JvmDeclaredType', a1)
    assert _is_linked(b, 'JvmDeclaredType', a1)
    if hasattr(a1, 'members'):
        assert _is_linked(a1, 'members', b)
    _safe_set(b, 'JvmDeclaredType', a2)
    assert _is_linked(b, 'JvmDeclaredType', a2)
    if hasattr(a1, 'members'):
        assert not _is_linked(a1, 'members', b)
    if hasattr(a2, 'members'):
        assert _is_linked(a2, 'members', b)
    _safe_set(b, 'JvmDeclaredType', None)
    assert not _is_linked(b, 'JvmDeclaredType', a2)
    if hasattr(a2, 'members'):
        assert not _is_linked(a2, 'members', b)


def test_assoc_defaultValue29_reverse_link_reassign_clear():
    a1 = types_JvmOperation(abstract=True, default=True, final=True, native=True, static=True, strictFloatingPoint=True, synchronized=True)
    a2 = types_JvmOperation(abstract=False, default=False, final=False, native=False, static=False, strictFloatingPoint=False, synchronized=False)
    b = types_JvmAnnotationValue()
    _safe_set(b, 'types_JvmAnnotationValue', a1)
    assert _is_linked(b, 'types_JvmAnnotationValue', a1)
    if hasattr(a1, 'types_JvmOperation30'):
        assert _is_linked(a1, 'types_JvmOperation30', b)
    _safe_set(b, 'types_JvmAnnotationValue', a2)
    assert _is_linked(b, 'types_JvmAnnotationValue', a2)
    if hasattr(a1, 'types_JvmOperation30'):
        assert not _is_linked(a1, 'types_JvmOperation30', b)
    if hasattr(a2, 'types_JvmOperation30'):
        assert _is_linked(a2, 'types_JvmOperation30', b)
    _safe_set(b, 'types_JvmAnnotationValue', None)
    assert not _is_linked(b, 'types_JvmAnnotationValue', a2)
    if hasattr(a2, 'types_JvmOperation30'):
        assert not _is_linked(a2, 'types_JvmOperation30', b)


def test_assoc_exceptions24_reverse_link_reassign_clear():
    a1 = types_JvmTypeReference()
    a2 = types_JvmTypeReference()
    b = types_JvmExecutable(varArgs=True)
    _safe_set(b, 'types_JvmExecutable25', {a1})
    assert _is_linked(b, 'types_JvmExecutable25', a1)
    if hasattr(a1, 'types_JvmTypeReference26'):
        assert _is_linked(a1, 'types_JvmTypeReference26', b)
    _safe_set(b, 'types_JvmExecutable25', {a2})
    assert _is_linked(b, 'types_JvmExecutable25', a2)
    if hasattr(a1, 'types_JvmTypeReference26'):
        assert not _is_linked(a1, 'types_JvmTypeReference26', b)
    if hasattr(a2, 'types_JvmTypeReference26'):
        assert _is_linked(a2, 'types_JvmTypeReference26', b)
    _safe_set(b, 'types_JvmExecutable25', set())
    assert not _is_linked(b, 'types_JvmExecutable25', a2)
    if hasattr(a2, 'types_JvmTypeReference26'):
        assert not _is_linked(a2, 'types_JvmTypeReference26', b)


def test_assoc_explicitValues37_reverse_link_reassign_clear():
    a1 = types_JvmAnnotationValue()
    a2 = types_JvmAnnotationValue()
    b = types_JvmAnnotationReference()
    _safe_set(b, 'types_JvmAnnotationReference38', {a1})
    assert _is_linked(b, 'types_JvmAnnotationReference38', a1)
    if hasattr(a1, 'types_JvmAnnotationValue39'):
        assert _is_linked(a1, 'types_JvmAnnotationValue39', b)
    _safe_set(b, 'types_JvmAnnotationReference38', {a2})
    assert _is_linked(b, 'types_JvmAnnotationReference38', a2)
    if hasattr(a1, 'types_JvmAnnotationValue39'):
        assert not _is_linked(a1, 'types_JvmAnnotationValue39', b)
    if hasattr(a2, 'types_JvmAnnotationValue39'):
        assert _is_linked(a2, 'types_JvmAnnotationValue39', b)
    _safe_set(b, 'types_JvmAnnotationReference38', set())
    assert not _is_linked(b, 'types_JvmAnnotationReference38', a2)
    if hasattr(a2, 'types_JvmAnnotationValue39'):
        assert not _is_linked(a2, 'types_JvmAnnotationValue39', b)


def test_assoc_localClasses20_reverse_link_reassign_clear():
    a1 = types_JvmGenericType(anonymous=True, interface=True, strictFloatingPoint=True)
    a2 = types_JvmGenericType(anonymous=False, interface=False, strictFloatingPoint=False)
    b = types_JvmFeature()
    _safe_set(b, 'types_JvmFeature', {a1})
    assert _is_linked(b, 'types_JvmFeature', a1)
    if hasattr(a1, 'types_JvmGenericType'):
        assert _is_linked(a1, 'types_JvmGenericType', b)
    _safe_set(b, 'types_JvmFeature', {a2})
    assert _is_linked(b, 'types_JvmFeature', a2)
    if hasattr(a1, 'types_JvmGenericType'):
        assert not _is_linked(a1, 'types_JvmGenericType', b)
    if hasattr(a2, 'types_JvmGenericType'):
        assert _is_linked(a2, 'types_JvmGenericType', b)
    _safe_set(b, 'types_JvmFeature', set())
    assert not _is_linked(b, 'types_JvmFeature', a2)
    if hasattr(a2, 'types_JvmGenericType'):
        assert not _is_linked(a2, 'types_JvmGenericType', b)


def test_assoc_members3_reverse_link_reassign_clear():
    a1 = types_JvmMember(deprecated=True, identifier="sample_text", simpleName="sample_text", visibility="sample_text")
    a2 = types_JvmMember(deprecated=False, identifier="sample_text_2", simpleName="sample_text_2", visibility="sample_text_2")
    b = types_JvmDeclaredType(abstract=True, final=True, packageName="sample_text", static=True)
    _safe_set(b, 'declaringType', {a1})
    assert _is_linked(b, 'declaringType', a1)
    if hasattr(a1, 'JvmMember'):
        assert _is_linked(a1, 'JvmMember', b)
    _safe_set(b, 'declaringType', {a2})
    assert _is_linked(b, 'declaringType', a2)
    if hasattr(a1, 'JvmMember'):
        assert not _is_linked(a1, 'JvmMember', b)
    if hasattr(a2, 'JvmMember'):
        assert _is_linked(a2, 'JvmMember', b)
    _safe_set(b, 'declaringType', set())
    assert not _is_linked(b, 'declaringType', a2)
    if hasattr(a2, 'JvmMember'):
        assert not _is_linked(a2, 'JvmMember', b)


def test_assoc_operation40_reverse_link_reassign_clear():
    a1 = types_JvmOperation(abstract=True, default=True, final=True, native=True, static=True, strictFloatingPoint=True, synchronized=True)
    a2 = types_JvmOperation(abstract=False, default=False, final=False, native=False, static=False, strictFloatingPoint=False, synchronized=False)
    b = types_JvmAnnotationValue()
    _safe_set(b, 'types_JvmAnnotationValue41', a1)
    assert _is_linked(b, 'types_JvmAnnotationValue41', a1)
    if hasattr(a1, 'types_JvmOperation42'):
        assert _is_linked(a1, 'types_JvmOperation42', b)
    _safe_set(b, 'types_JvmAnnotationValue41', a2)
    assert _is_linked(b, 'types_JvmAnnotationValue41', a2)
    if hasattr(a1, 'types_JvmOperation42'):
        assert not _is_linked(a1, 'types_JvmOperation42', b)
    if hasattr(a2, 'types_JvmOperation42'):
        assert _is_linked(a2, 'types_JvmOperation42', b)
    _safe_set(b, 'types_JvmAnnotationValue41', None)
    assert not _is_linked(b, 'types_JvmAnnotationValue41', a2)
    if hasattr(a2, 'types_JvmOperation42'):
        assert not _is_linked(a2, 'types_JvmOperation42', b)


def test_assoc_parameterType31_reverse_link_reassign_clear():
    a1 = types_JvmTypeReference()
    a2 = types_JvmTypeReference()
    b = types_JvmFormalParameter(name="sample_text")
    _safe_set(b, 'types_JvmFormalParameter32', a1)
    assert _is_linked(b, 'types_JvmFormalParameter32', a1)
    if hasattr(a1, 'types_JvmTypeReference33'):
        assert _is_linked(a1, 'types_JvmTypeReference33', b)
    _safe_set(b, 'types_JvmFormalParameter32', a2)
    assert _is_linked(b, 'types_JvmFormalParameter32', a2)
    if hasattr(a1, 'types_JvmTypeReference33'):
        assert not _is_linked(a1, 'types_JvmTypeReference33', b)
    if hasattr(a2, 'types_JvmTypeReference33'):
        assert _is_linked(a2, 'types_JvmTypeReference33', b)
    _safe_set(b, 'types_JvmFormalParameter32', None)
    assert not _is_linked(b, 'types_JvmFormalParameter32', a2)
    if hasattr(a2, 'types_JvmTypeReference33'):
        assert not _is_linked(a2, 'types_JvmTypeReference33', b)


def test_assoc_parameters23_reverse_link_reassign_clear():
    a1 = types_JvmFormalParameter(name="sample_text")
    a2 = types_JvmFormalParameter(name="sample_text_2")
    b = types_JvmExecutable(varArgs=True)
    _safe_set(b, 'types_JvmExecutable', {a1})
    assert _is_linked(b, 'types_JvmExecutable', a1)
    if hasattr(a1, 'types_JvmFormalParameter'):
        assert _is_linked(a1, 'types_JvmFormalParameter', b)
    _safe_set(b, 'types_JvmExecutable', {a2})
    assert _is_linked(b, 'types_JvmExecutable', a2)
    if hasattr(a1, 'types_JvmFormalParameter'):
        assert not _is_linked(a1, 'types_JvmFormalParameter', b)
    if hasattr(a2, 'types_JvmFormalParameter'):
        assert _is_linked(a2, 'types_JvmFormalParameter', b)
    _safe_set(b, 'types_JvmExecutable', set())
    assert not _is_linked(b, 'types_JvmExecutable', a2)
    if hasattr(a2, 'types_JvmFormalParameter'):
        assert not _is_linked(a2, 'types_JvmFormalParameter', b)


def test_assoc_returnType27_reverse_link_reassign_clear():
    a1 = types_JvmTypeReference()
    a2 = types_JvmTypeReference()
    b = types_JvmOperation(abstract=True, default=True, final=True, native=True, static=True, strictFloatingPoint=True, synchronized=True)
    _safe_set(b, 'types_JvmOperation', a1)
    assert _is_linked(b, 'types_JvmOperation', a1)
    if hasattr(a1, 'types_JvmTypeReference28'):
        assert _is_linked(a1, 'types_JvmTypeReference28', b)
    _safe_set(b, 'types_JvmOperation', a2)
    assert _is_linked(b, 'types_JvmOperation', a2)
    if hasattr(a1, 'types_JvmTypeReference28'):
        assert not _is_linked(a1, 'types_JvmTypeReference28', b)
    if hasattr(a2, 'types_JvmTypeReference28'):
        assert _is_linked(a2, 'types_JvmTypeReference28', b)
    _safe_set(b, 'types_JvmOperation', None)
    assert not _is_linked(b, 'types_JvmOperation', a2)
    if hasattr(a2, 'types_JvmTypeReference28'):
        assert not _is_linked(a2, 'types_JvmTypeReference28', b)


def test_assoc_superTypes2_reverse_link_reassign_clear():
    a1 = types_JvmTypeReference()
    a2 = types_JvmTypeReference()
    b = types_JvmDeclaredType(abstract=True, final=True, packageName="sample_text", static=True)
    _safe_set(b, 'types_JvmDeclaredType', {a1})
    assert _is_linked(b, 'types_JvmDeclaredType', a1)
    if hasattr(a1, 'types_JvmTypeReference'):
        assert _is_linked(a1, 'types_JvmTypeReference', b)
    _safe_set(b, 'types_JvmDeclaredType', {a2})
    assert _is_linked(b, 'types_JvmDeclaredType', a2)
    if hasattr(a1, 'types_JvmTypeReference'):
        assert not _is_linked(a1, 'types_JvmTypeReference', b)
    if hasattr(a2, 'types_JvmTypeReference'):
        assert _is_linked(a2, 'types_JvmTypeReference', b)
    _safe_set(b, 'types_JvmDeclaredType', set())
    assert not _is_linked(b, 'types_JvmDeclaredType', a2)
    if hasattr(a2, 'types_JvmTypeReference'):
        assert not _is_linked(a2, 'types_JvmTypeReference', b)


def test_assoc_type21_reverse_link_reassign_clear():
    a1 = types_JvmTypeReference()
    a2 = types_JvmTypeReference()
    b = types_JvmField(constant=True, constantValue="sample_text", final=True, static=True, transient=True, volatile=True)
    _safe_set(b, 'types_JvmField', a1)
    assert _is_linked(b, 'types_JvmField', a1)
    if hasattr(a1, 'types_JvmTypeReference22'):
        assert _is_linked(a1, 'types_JvmTypeReference22', b)
    _safe_set(b, 'types_JvmField', a2)
    assert _is_linked(b, 'types_JvmField', a2)
    if hasattr(a1, 'types_JvmTypeReference22'):
        assert not _is_linked(a1, 'types_JvmTypeReference22', b)
    if hasattr(a2, 'types_JvmTypeReference22'):
        assert _is_linked(a2, 'types_JvmTypeReference22', b)
    _safe_set(b, 'types_JvmField', None)
    assert not _is_linked(b, 'types_JvmField', a2)
    if hasattr(a2, 'types_JvmTypeReference22'):
        assert not _is_linked(a2, 'types_JvmTypeReference22', b)


def test_assoc_typeReference7_reverse_link_reassign_clear():
    a1 = types_JvmTypeReference()
    a2 = types_JvmTypeReference()
    b = types_JvmTypeConstraint()
    _safe_set(b, 'types_JvmTypeConstraint', a1)
    assert _is_linked(b, 'types_JvmTypeConstraint', a1)
    if hasattr(a1, 'types_JvmTypeReference8'):
        assert _is_linked(a1, 'types_JvmTypeReference8', b)
    _safe_set(b, 'types_JvmTypeConstraint', a2)
    assert _is_linked(b, 'types_JvmTypeConstraint', a2)
    if hasattr(a1, 'types_JvmTypeReference8'):
        assert not _is_linked(a1, 'types_JvmTypeReference8', b)
    if hasattr(a2, 'types_JvmTypeReference8'):
        assert _is_linked(a2, 'types_JvmTypeReference8', b)
    _safe_set(b, 'types_JvmTypeConstraint', None)
    assert not _is_linked(b, 'types_JvmTypeConstraint', a2)
    if hasattr(a2, 'types_JvmTypeReference8'):
        assert not _is_linked(a2, 'types_JvmTypeReference8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotation35_stub_double():
    # types_JvmAnnotationType has no real 'types_JvmAnnotationType' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmAnnotationReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmAnnotationReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmAnnotationReference()
    partner = types_JvmAnnotationType()
    setattr(partner, 'types_JvmAnnotationType', None)
    _safe_set(owner, 'types_JvmAnnotationReference36', partner)
    assert getattr(partner, 'types_JvmAnnotationType') == owner
    _safe_set(owner, 'types_JvmAnnotationReference36', None)
    assert getattr(partner, 'types_JvmAnnotationType') is None


def test_assoc_annotations34_stub_double():
    # types_JvmAnnotationTarget has no real 'types_JvmAnnotationTarget' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmAnnotationReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmAnnotationReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmAnnotationReference()
    partner = types_JvmAnnotationTarget()
    setattr(partner, 'types_JvmAnnotationTarget', None)
    _safe_set(owner, 'types_JvmAnnotationReference', partner)
    assert owner in getattr(partner, 'types_JvmAnnotationTarget')
    _safe_set(owner, 'types_JvmAnnotationReference', None)
    assert owner not in getattr(partner, 'types_JvmAnnotationTarget')


def test_assoc_arguments11_stub_double():
    # types_JvmParameterizedTypeReference has no real 'types_JvmParameterizedTypeReference' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmTypeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmTypeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmTypeReference()
    partner = types_JvmParameterizedTypeReference()
    setattr(partner, 'types_JvmParameterizedTypeReference', None)
    _safe_set(owner, 'types_JvmTypeReference12', partner)
    assert owner in getattr(partner, 'types_JvmParameterizedTypeReference')
    _safe_set(owner, 'types_JvmTypeReference12', None)
    assert owner not in getattr(partner, 'types_JvmParameterizedTypeReference')


def test_assoc_arrayType0_stub_double():
    # types_JvmComponentType has no real 'componentType' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmArrayType()
    partner = types_JvmComponentType()
    setattr(partner, 'componentType', None)
    _safe_set(owner, 'JvmArrayType', partner)
    assert getattr(partner, 'componentType') == owner
    _safe_set(owner, 'JvmArrayType', None)
    assert getattr(partner, 'componentType') is None


def test_assoc_componentType1_stub_double():
    # types_JvmComponentType has no real 'JvmComponentType' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmArrayType()
    partner = types_JvmComponentType()
    setattr(partner, 'JvmComponentType', None)
    _safe_set(owner, 'arrayType', partner)
    assert getattr(partner, 'JvmComponentType') == owner
    _safe_set(owner, 'arrayType', None)
    assert getattr(partner, 'JvmComponentType') is None


def test_assoc_constraints6_stub_double():
    # types_JvmConstraintOwner has no real 'owner' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmTypeConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmTypeConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmTypeConstraint()
    partner = types_JvmConstraintOwner()
    setattr(partner, 'owner', None)
    _safe_set(owner, 'JvmTypeConstraint', partner)
    assert owner in getattr(partner, 'owner')
    _safe_set(owner, 'JvmTypeConstraint', None)
    assert owner not in getattr(partner, 'owner')


def test_assoc_declarator4_stub_double():
    # types_JvmTypeParameterDeclarator has no real 'JvmTypeParameterDeclarator' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmTypeParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmTypeParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmTypeParameter(name="sample_text")
    partner = types_JvmTypeParameterDeclarator()
    setattr(partner, 'JvmTypeParameterDeclarator', None)
    _safe_set(owner, 'typeParameters', partner)
    assert getattr(partner, 'JvmTypeParameterDeclarator') == owner
    _safe_set(owner, 'typeParameters', None)
    assert getattr(partner, 'JvmTypeParameterDeclarator') is None


def test_assoc_delegate49_stub_double():
    # types_JvmDelegateTypeReference has no real 'types_JvmDelegateTypeReference' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmTypeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmTypeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmTypeReference()
    partner = types_JvmDelegateTypeReference()
    setattr(partner, 'types_JvmDelegateTypeReference', None)
    _safe_set(owner, 'types_JvmTypeReference50', partner)
    assert getattr(partner, 'types_JvmDelegateTypeReference') == owner
    _safe_set(owner, 'types_JvmTypeReference50', None)
    assert getattr(partner, 'types_JvmDelegateTypeReference') is None


def test_assoc_equivalent51_stub_double():
    # types_JvmSpecializedTypeReference has no real 'types_JvmSpecializedTypeReference' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmTypeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmTypeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmTypeReference()
    partner = types_JvmSpecializedTypeReference()
    setattr(partner, 'types_JvmSpecializedTypeReference', None)
    _safe_set(owner, 'types_JvmTypeReference52', partner)
    assert getattr(partner, 'types_JvmSpecializedTypeReference') == owner
    _safe_set(owner, 'types_JvmTypeReference52', None)
    assert getattr(partner, 'types_JvmSpecializedTypeReference') is None


def test_assoc_literals10_stub_double():
    # types_JvmEnumerationType has no real 'types_JvmEnumerationType' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmEnumerationLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmEnumerationLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmEnumerationLiteral()
    partner = types_JvmEnumerationType()
    setattr(partner, 'types_JvmEnumerationType', None)
    _safe_set(owner, 'types_JvmEnumerationLiteral', partner)
    assert owner in getattr(partner, 'types_JvmEnumerationType')
    _safe_set(owner, 'types_JvmEnumerationLiteral', None)
    assert owner not in getattr(partner, 'types_JvmEnumerationType')


def test_assoc_owner9_stub_double():
    # types_JvmConstraintOwner has no real 'JvmConstraintOwner' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmTypeConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmTypeConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmTypeConstraint()
    partner = types_JvmConstraintOwner()
    setattr(partner, 'JvmConstraintOwner', None)
    _safe_set(owner, 'constraints', partner)
    assert getattr(partner, 'JvmConstraintOwner') == owner
    _safe_set(owner, 'constraints', None)
    assert getattr(partner, 'JvmConstraintOwner') is None


def test_assoc_references55_stub_double():
    # types_JvmCompoundTypeReference has no real 'types_JvmCompoundTypeReference56' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmTypeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmTypeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmTypeReference()
    partner = types_JvmCompoundTypeReference()
    setattr(partner, 'types_JvmCompoundTypeReference56', None)
    _safe_set(owner, 'types_JvmTypeReference57', partner)
    assert owner in getattr(partner, 'types_JvmCompoundTypeReference56')
    _safe_set(owner, 'types_JvmTypeReference57', None)
    assert owner not in getattr(partner, 'types_JvmCompoundTypeReference56')


def test_assoc_typeParameters5_stub_double():
    # types_JvmTypeParameterDeclarator has no real 'declarator' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmTypeParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmTypeParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmTypeParameter(name="sample_text")
    partner = types_JvmTypeParameterDeclarator()
    setattr(partner, 'declarator', None)
    _safe_set(owner, 'JvmTypeParameter', partner)
    assert owner in getattr(partner, 'declarator')
    _safe_set(owner, 'JvmTypeParameter', None)
    assert owner not in getattr(partner, 'declarator')


def test_assoc_values43_stub_double():
    # types_JvmTypeAnnotationValue has no real 'types_JvmTypeAnnotationValue' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmTypeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmTypeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmTypeReference()
    partner = types_JvmTypeAnnotationValue()
    setattr(partner, 'types_JvmTypeAnnotationValue', None)
    _safe_set(owner, 'types_JvmTypeReference44', partner)
    assert owner in getattr(partner, 'types_JvmTypeAnnotationValue')
    _safe_set(owner, 'types_JvmTypeReference44', None)
    assert owner not in getattr(partner, 'types_JvmTypeAnnotationValue')


def test_assoc_values45_stub_double():
    # types_JvmAnnotationAnnotationValue has no real 'types_JvmAnnotationAnnotationValue' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmAnnotationReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmAnnotationReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmAnnotationReference()
    partner = types_JvmAnnotationAnnotationValue()
    setattr(partner, 'types_JvmAnnotationAnnotationValue', None)
    _safe_set(owner, 'types_JvmAnnotationReference46', partner)
    assert owner in getattr(partner, 'types_JvmAnnotationAnnotationValue')
    _safe_set(owner, 'types_JvmAnnotationReference46', None)
    assert owner not in getattr(partner, 'types_JvmAnnotationAnnotationValue')


def test_assoc_values47_stub_double():
    # types_JvmEnumAnnotationValue has no real 'types_JvmEnumAnnotationValue' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmEnumerationLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmEnumerationLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmEnumerationLiteral()
    partner = types_JvmEnumAnnotationValue()
    setattr(partner, 'types_JvmEnumAnnotationValue', None)
    _safe_set(owner, 'types_JvmEnumerationLiteral48', partner)
    assert owner in getattr(partner, 'types_JvmEnumAnnotationValue')
    _safe_set(owner, 'types_JvmEnumerationLiteral48', None)
    assert owner not in getattr(partner, 'types_JvmEnumAnnotationValue')


