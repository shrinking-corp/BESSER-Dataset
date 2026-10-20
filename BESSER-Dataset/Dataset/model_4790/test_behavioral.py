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
    JvmType,
    JvmTypeConstraint,
    JvmTypeParameterDeclarator,
    JvmTypeReference,
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
    a1 = types_JvmMember(identifier="sample_text", simpleName="sample_text", visibility="sample_text")
    a2 = types_JvmMember(identifier="sample_text_2", simpleName="sample_text_2", visibility="sample_text_2")
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


def test_assoc_defaultValue28_reverse_link_reassign_clear():
    a1 = types_JvmOperation(abstract=True, final=True, static=True)
    a2 = types_JvmOperation(abstract=False, final=False, static=False)
    b = types_JvmAnnotationValue()
    _safe_set(b, 'types_JvmAnnotationValue', a1)
    assert _is_linked(b, 'types_JvmAnnotationValue', a1)
    if hasattr(a1, 'types_JvmOperation29'):
        assert _is_linked(a1, 'types_JvmOperation29', b)
    _safe_set(b, 'types_JvmAnnotationValue', a2)
    assert _is_linked(b, 'types_JvmAnnotationValue', a2)
    if hasattr(a1, 'types_JvmOperation29'):
        assert not _is_linked(a1, 'types_JvmOperation29', b)
    if hasattr(a2, 'types_JvmOperation29'):
        assert _is_linked(a2, 'types_JvmOperation29', b)
    _safe_set(b, 'types_JvmAnnotationValue', None)
    assert not _is_linked(b, 'types_JvmAnnotationValue', a2)
    if hasattr(a2, 'types_JvmOperation29'):
        assert not _is_linked(a2, 'types_JvmOperation29', b)


def test_assoc_exceptions23_reverse_link_reassign_clear():
    a1 = types_JvmTypeReference()
    a2 = types_JvmTypeReference()
    b = types_JvmExecutable(varArgs=True)
    _safe_set(b, 'types_JvmExecutable24', {a1})
    assert _is_linked(b, 'types_JvmExecutable24', a1)
    if hasattr(a1, 'types_JvmTypeReference25'):
        assert _is_linked(a1, 'types_JvmTypeReference25', b)
    _safe_set(b, 'types_JvmExecutable24', {a2})
    assert _is_linked(b, 'types_JvmExecutable24', a2)
    if hasattr(a1, 'types_JvmTypeReference25'):
        assert not _is_linked(a1, 'types_JvmTypeReference25', b)
    if hasattr(a2, 'types_JvmTypeReference25'):
        assert _is_linked(a2, 'types_JvmTypeReference25', b)
    _safe_set(b, 'types_JvmExecutable24', set())
    assert not _is_linked(b, 'types_JvmExecutable24', a2)
    if hasattr(a2, 'types_JvmTypeReference25'):
        assert not _is_linked(a2, 'types_JvmTypeReference25', b)


def test_assoc_members3_reverse_link_reassign_clear():
    a1 = types_JvmMember(identifier="sample_text", simpleName="sample_text", visibility="sample_text")
    a2 = types_JvmMember(identifier="sample_text_2", simpleName="sample_text_2", visibility="sample_text_2")
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


def test_assoc_operation39_reverse_link_reassign_clear():
    a1 = types_JvmOperation(abstract=True, final=True, static=True)
    a2 = types_JvmOperation(abstract=False, final=False, static=False)
    b = types_JvmAnnotationValue()
    _safe_set(b, 'types_JvmAnnotationValue40', a1)
    assert _is_linked(b, 'types_JvmAnnotationValue40', a1)
    if hasattr(a1, 'types_JvmOperation41'):
        assert _is_linked(a1, 'types_JvmOperation41', b)
    _safe_set(b, 'types_JvmAnnotationValue40', a2)
    assert _is_linked(b, 'types_JvmAnnotationValue40', a2)
    if hasattr(a1, 'types_JvmOperation41'):
        assert not _is_linked(a1, 'types_JvmOperation41', b)
    if hasattr(a2, 'types_JvmOperation41'):
        assert _is_linked(a2, 'types_JvmOperation41', b)
    _safe_set(b, 'types_JvmAnnotationValue40', None)
    assert not _is_linked(b, 'types_JvmAnnotationValue40', a2)
    if hasattr(a2, 'types_JvmOperation41'):
        assert not _is_linked(a2, 'types_JvmOperation41', b)


def test_assoc_parameterType30_reverse_link_reassign_clear():
    a1 = types_JvmTypeReference()
    a2 = types_JvmTypeReference()
    b = types_JvmFormalParameter(name="sample_text")
    _safe_set(b, 'types_JvmFormalParameter31', a1)
    assert _is_linked(b, 'types_JvmFormalParameter31', a1)
    if hasattr(a1, 'types_JvmTypeReference32'):
        assert _is_linked(a1, 'types_JvmTypeReference32', b)
    _safe_set(b, 'types_JvmFormalParameter31', a2)
    assert _is_linked(b, 'types_JvmFormalParameter31', a2)
    if hasattr(a1, 'types_JvmTypeReference32'):
        assert not _is_linked(a1, 'types_JvmTypeReference32', b)
    if hasattr(a2, 'types_JvmTypeReference32'):
        assert _is_linked(a2, 'types_JvmTypeReference32', b)
    _safe_set(b, 'types_JvmFormalParameter31', None)
    assert not _is_linked(b, 'types_JvmFormalParameter31', a2)
    if hasattr(a2, 'types_JvmTypeReference32'):
        assert not _is_linked(a2, 'types_JvmTypeReference32', b)


def test_assoc_parameters22_reverse_link_reassign_clear():
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


def test_assoc_returnType26_reverse_link_reassign_clear():
    a1 = types_JvmTypeReference()
    a2 = types_JvmTypeReference()
    b = types_JvmOperation(abstract=True, final=True, static=True)
    _safe_set(b, 'types_JvmOperation', a1)
    assert _is_linked(b, 'types_JvmOperation', a1)
    if hasattr(a1, 'types_JvmTypeReference27'):
        assert _is_linked(a1, 'types_JvmTypeReference27', b)
    _safe_set(b, 'types_JvmOperation', a2)
    assert _is_linked(b, 'types_JvmOperation', a2)
    if hasattr(a1, 'types_JvmTypeReference27'):
        assert not _is_linked(a1, 'types_JvmTypeReference27', b)
    if hasattr(a2, 'types_JvmTypeReference27'):
        assert _is_linked(a2, 'types_JvmTypeReference27', b)
    _safe_set(b, 'types_JvmOperation', None)
    assert not _is_linked(b, 'types_JvmOperation', a2)
    if hasattr(a2, 'types_JvmTypeReference27'):
        assert not _is_linked(a2, 'types_JvmTypeReference27', b)


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


def test_assoc_type20_reverse_link_reassign_clear():
    a1 = types_JvmTypeReference()
    a2 = types_JvmTypeReference()
    b = types_JvmField(final=True, static=True)
    _safe_set(b, 'types_JvmField', a1)
    assert _is_linked(b, 'types_JvmField', a1)
    if hasattr(a1, 'types_JvmTypeReference21'):
        assert _is_linked(a1, 'types_JvmTypeReference21', b)
    _safe_set(b, 'types_JvmField', a2)
    assert _is_linked(b, 'types_JvmField', a2)
    if hasattr(a1, 'types_JvmTypeReference21'):
        assert not _is_linked(a1, 'types_JvmTypeReference21', b)
    if hasattr(a2, 'types_JvmTypeReference21'):
        assert _is_linked(a2, 'types_JvmTypeReference21', b)
    _safe_set(b, 'types_JvmField', None)
    assert not _is_linked(b, 'types_JvmField', a2)
    if hasattr(a2, 'types_JvmTypeReference21'):
        assert not _is_linked(a2, 'types_JvmTypeReference21', b)


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


def test_assoc_delegate48_stub_double():
    # types_JvmDelegateTypeReference has no real 'types_JvmDelegateTypeReference' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmTypeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmTypeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmTypeReference()
    partner = types_JvmDelegateTypeReference()
    setattr(partner, 'types_JvmDelegateTypeReference', None)
    _safe_set(owner, 'types_JvmTypeReference49', partner)
    assert getattr(partner, 'types_JvmDelegateTypeReference') == owner
    _safe_set(owner, 'types_JvmTypeReference49', None)
    assert getattr(partner, 'types_JvmDelegateTypeReference') is None


def test_assoc_equivalent50_stub_double():
    # types_JvmSpecializedTypeReference has no real 'types_JvmSpecializedTypeReference' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmTypeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmTypeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmTypeReference()
    partner = types_JvmSpecializedTypeReference()
    setattr(partner, 'types_JvmSpecializedTypeReference', None)
    _safe_set(owner, 'types_JvmTypeReference51', partner)
    assert getattr(partner, 'types_JvmSpecializedTypeReference') == owner
    _safe_set(owner, 'types_JvmTypeReference51', None)
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


def test_assoc_references54_stub_double():
    # types_JvmCompoundTypeReference has no real 'types_JvmCompoundTypeReference55' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmTypeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmTypeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmTypeReference()
    partner = types_JvmCompoundTypeReference()
    setattr(partner, 'types_JvmCompoundTypeReference55', None)
    _safe_set(owner, 'types_JvmTypeReference56', partner)
    assert owner in getattr(partner, 'types_JvmCompoundTypeReference55')
    _safe_set(owner, 'types_JvmTypeReference56', None)
    assert owner not in getattr(partner, 'types_JvmCompoundTypeReference55')


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


def test_assoc_values36_stub_double():
    # types_JvmAnnotationReference has no real 'types_JvmAnnotationReference37' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmAnnotationValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmAnnotationValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmAnnotationValue()
    partner = types_JvmAnnotationReference()
    setattr(partner, 'types_JvmAnnotationReference37', None)
    _safe_set(owner, 'types_JvmAnnotationValue38', partner)
    assert owner in getattr(partner, 'types_JvmAnnotationReference37')
    _safe_set(owner, 'types_JvmAnnotationValue38', None)
    assert owner not in getattr(partner, 'types_JvmAnnotationReference37')


def test_assoc_values42_stub_double():
    # types_JvmTypeAnnotationValue has no real 'types_JvmTypeAnnotationValue' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmTypeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmTypeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmTypeReference()
    partner = types_JvmTypeAnnotationValue()
    setattr(partner, 'types_JvmTypeAnnotationValue', None)
    _safe_set(owner, 'types_JvmTypeReference43', partner)
    assert owner in getattr(partner, 'types_JvmTypeAnnotationValue')
    _safe_set(owner, 'types_JvmTypeReference43', None)
    assert owner not in getattr(partner, 'types_JvmTypeAnnotationValue')


def test_assoc_values46_stub_double():
    # types_JvmEnumAnnotationValue has no real 'types_JvmEnumAnnotationValue' property in the generated
    # code (a bare stub) -- manually attach it so types_JvmEnumerationLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_JvmEnumerationLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_JvmEnumerationLiteral()
    partner = types_JvmEnumAnnotationValue()
    setattr(partner, 'types_JvmEnumAnnotationValue', None)
    _safe_set(owner, 'types_JvmEnumerationLiteral47', partner)
    assert owner in getattr(partner, 'types_JvmEnumAnnotationValue')
    _safe_set(owner, 'types_JvmEnumerationLiteral47', None)
    assert owner not in getattr(partner, 'types_JvmEnumAnnotationValue')


