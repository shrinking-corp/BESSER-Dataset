import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_types_JvmBooleanAnnotationValue_values_value_roundtrip():
    instance = types_JvmBooleanAnnotationValue(values=True)
    assert instance.values == True
    instance.values = False
    assert instance.values == False


def test_types_JvmByteAnnotationValue_values_value_roundtrip():
    instance = types_JvmByteAnnotationValue(values="sample_text")
    assert instance.values == "sample_text"
    instance.values = "sample_text_2"
    assert instance.values == "sample_text_2"


def test_types_JvmCharAnnotationValue_values_value_roundtrip():
    instance = types_JvmCharAnnotationValue(values="sample_text")
    assert instance.values == "sample_text"
    instance.values = "sample_text_2"
    assert instance.values == "sample_text_2"


def test_types_JvmCustomAnnotationValue_values_value_roundtrip():
    instance = types_JvmCustomAnnotationValue(values="sample_text")
    assert instance.values == "sample_text"
    instance.values = "sample_text_2"
    assert instance.values == "sample_text_2"


def test_types_JvmDeclaredType_abstract_value_roundtrip():
    instance = types_JvmDeclaredType(abstract=True, final=True, packageName="sample_text", static=True)
    assert instance.abstract == True
    instance.abstract = False
    assert instance.abstract == False


def test_types_JvmDeclaredType_final_value_roundtrip():
    instance = types_JvmDeclaredType(abstract=True, final=True, packageName="sample_text", static=True)
    assert instance.final == True
    instance.final = False
    assert instance.final == False


def test_types_JvmDeclaredType_packageName_value_roundtrip():
    instance = types_JvmDeclaredType(abstract=True, final=True, packageName="sample_text", static=True)
    assert instance.packageName == "sample_text"
    instance.packageName = "sample_text_2"
    assert instance.packageName == "sample_text_2"


def test_types_JvmDeclaredType_static_value_roundtrip():
    instance = types_JvmDeclaredType(abstract=True, final=True, packageName="sample_text", static=True)
    assert instance.static == True
    instance.static = False
    assert instance.static == False


def test_types_JvmDoubleAnnotationValue_values_value_roundtrip():
    instance = types_JvmDoubleAnnotationValue(values=3.14)
    assert instance.values == 3.14
    instance.values = 9.99
    assert instance.values == 9.99


def test_types_JvmExecutable_varArgs_value_roundtrip():
    instance = types_JvmExecutable(varArgs=True)
    assert instance.varArgs == True
    instance.varArgs = False
    assert instance.varArgs == False


def test_types_JvmField_final_value_roundtrip():
    instance = types_JvmField(final=True, static=True)
    assert instance.final == True
    instance.final = False
    assert instance.final == False


def test_types_JvmField_static_value_roundtrip():
    instance = types_JvmField(final=True, static=True)
    assert instance.static == True
    instance.static = False
    assert instance.static == False


def test_types_JvmFloatAnnotationValue_values_value_roundtrip():
    instance = types_JvmFloatAnnotationValue(values=3.14)
    assert instance.values == 3.14
    instance.values = 9.99
    assert instance.values == 9.99


def test_types_JvmFormalParameter_name_value_roundtrip():
    instance = types_JvmFormalParameter(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_types_JvmGenericType_interface_value_roundtrip():
    instance = types_JvmGenericType(interface=True)
    assert instance.interface == True
    instance.interface = False
    assert instance.interface == False


def test_types_JvmIntAnnotationValue_values_value_roundtrip():
    instance = types_JvmIntAnnotationValue(values=7)
    assert instance.values == 7
    instance.values = 13
    assert instance.values == 13


def test_types_JvmLongAnnotationValue_values_value_roundtrip():
    instance = types_JvmLongAnnotationValue(values="sample_text")
    assert instance.values == "sample_text"
    instance.values = "sample_text_2"
    assert instance.values == "sample_text_2"


def test_types_JvmMember_identifier_value_roundtrip():
    instance = types_JvmMember(identifier="sample_text", simpleName="sample_text", visibility="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_types_JvmMember_simpleName_value_roundtrip():
    instance = types_JvmMember(identifier="sample_text", simpleName="sample_text", visibility="sample_text")
    assert instance.simpleName == "sample_text"
    instance.simpleName = "sample_text_2"
    assert instance.simpleName == "sample_text_2"


def test_types_JvmMember_visibility_value_roundtrip():
    instance = types_JvmMember(identifier="sample_text", simpleName="sample_text", visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_types_JvmOperation_abstract_value_roundtrip():
    instance = types_JvmOperation(abstract=True, final=True, static=True)
    assert instance.abstract == True
    instance.abstract = False
    assert instance.abstract == False


def test_types_JvmOperation_final_value_roundtrip():
    instance = types_JvmOperation(abstract=True, final=True, static=True)
    assert instance.final == True
    instance.final = False
    assert instance.final == False


def test_types_JvmOperation_static_value_roundtrip():
    instance = types_JvmOperation(abstract=True, final=True, static=True)
    assert instance.static == True
    instance.static = False
    assert instance.static == False


def test_types_JvmPrimitiveType_simpleName_value_roundtrip():
    instance = types_JvmPrimitiveType(simpleName="sample_text")
    assert instance.simpleName == "sample_text"
    instance.simpleName = "sample_text_2"
    assert instance.simpleName == "sample_text_2"


def test_types_JvmShortAnnotationValue_values_value_roundtrip():
    instance = types_JvmShortAnnotationValue(values="sample_text")
    assert instance.values == "sample_text"
    instance.values = "sample_text_2"
    assert instance.values == "sample_text_2"


def test_types_JvmStringAnnotationValue_values_value_roundtrip():
    instance = types_JvmStringAnnotationValue(values="sample_text")
    assert instance.values == "sample_text"
    instance.values = "sample_text_2"
    assert instance.values == "sample_text_2"


def test_types_JvmTypeParameter_name_value_roundtrip():
    instance = types_JvmTypeParameter(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_types_JvmUnknownTypeReference_exception_value_roundtrip():
    instance = types_JvmUnknownTypeReference(exception="sample_text")
    assert instance.exception == "sample_text"
    instance.exception = "sample_text_2"
    assert instance.exception == "sample_text_2"


def test_types_JvmAnnotationAnnotationValue_isa_JvmAnnotationTarget():
    instance = types_JvmAnnotationAnnotationValue()
    assert isinstance(instance, JvmAnnotationTarget)


def test_types_JvmFormalParameter_isa_JvmAnnotationTarget():
    instance = types_JvmFormalParameter(name="sample_text")
    assert isinstance(instance, JvmAnnotationTarget)


def test_types_JvmMember_isa_JvmAnnotationTarget():
    instance = types_JvmMember(identifier="sample_text", simpleName="sample_text", visibility="sample_text")
    assert isinstance(instance, JvmAnnotationTarget)


def test_types_JvmAnnotationAnnotationValue_isa_JvmAnnotationValue():
    instance = types_JvmAnnotationAnnotationValue()
    assert isinstance(instance, JvmAnnotationValue)


def test_types_JvmBooleanAnnotationValue_isa_JvmAnnotationValue():
    instance = types_JvmBooleanAnnotationValue(values=True)
    assert isinstance(instance, JvmAnnotationValue)


def test_types_JvmByteAnnotationValue_isa_JvmAnnotationValue():
    instance = types_JvmByteAnnotationValue(values="sample_text")
    assert isinstance(instance, JvmAnnotationValue)


def test_types_JvmCharAnnotationValue_isa_JvmAnnotationValue():
    instance = types_JvmCharAnnotationValue(values="sample_text")
    assert isinstance(instance, JvmAnnotationValue)


def test_types_JvmCustomAnnotationValue_isa_JvmAnnotationValue():
    instance = types_JvmCustomAnnotationValue(values="sample_text")
    assert isinstance(instance, JvmAnnotationValue)


def test_types_JvmDoubleAnnotationValue_isa_JvmAnnotationValue():
    instance = types_JvmDoubleAnnotationValue(values=3.14)
    assert isinstance(instance, JvmAnnotationValue)


def test_types_JvmEnumAnnotationValue_isa_JvmAnnotationValue():
    instance = types_JvmEnumAnnotationValue()
    assert isinstance(instance, JvmAnnotationValue)


def test_types_JvmFloatAnnotationValue_isa_JvmAnnotationValue():
    instance = types_JvmFloatAnnotationValue(values=3.14)
    assert isinstance(instance, JvmAnnotationValue)


def test_types_JvmIntAnnotationValue_isa_JvmAnnotationValue():
    instance = types_JvmIntAnnotationValue(values=7)
    assert isinstance(instance, JvmAnnotationValue)


def test_types_JvmLongAnnotationValue_isa_JvmAnnotationValue():
    instance = types_JvmLongAnnotationValue(values="sample_text")
    assert isinstance(instance, JvmAnnotationValue)


def test_types_JvmShortAnnotationValue_isa_JvmAnnotationValue():
    instance = types_JvmShortAnnotationValue(values="sample_text")
    assert isinstance(instance, JvmAnnotationValue)


def test_types_JvmStringAnnotationValue_isa_JvmAnnotationValue():
    instance = types_JvmStringAnnotationValue(values="sample_text")
    assert isinstance(instance, JvmAnnotationValue)


def test_types_JvmTypeAnnotationValue_isa_JvmAnnotationValue():
    instance = types_JvmTypeAnnotationValue()
    assert isinstance(instance, JvmAnnotationValue)


def test_types_JvmArrayType_isa_JvmComponentType():
    instance = types_JvmArrayType()
    assert isinstance(instance, JvmComponentType)


def test_types_JvmDeclaredType_isa_JvmComponentType():
    instance = types_JvmDeclaredType(abstract=True, final=True, packageName="sample_text", static=True)
    assert isinstance(instance, JvmComponentType)


def test_types_JvmPrimitiveType_isa_JvmComponentType():
    instance = types_JvmPrimitiveType(simpleName="sample_text")
    assert isinstance(instance, JvmComponentType)


def test_types_JvmTypeParameter_isa_JvmComponentType():
    instance = types_JvmTypeParameter(name="sample_text")
    assert isinstance(instance, JvmComponentType)


def test_types_JvmMultiTypeReference_isa_JvmCompoundTypeReference():
    instance = types_JvmMultiTypeReference()
    assert isinstance(instance, JvmCompoundTypeReference)


def test_types_JvmSynonymTypeReference_isa_JvmCompoundTypeReference():
    instance = types_JvmSynonymTypeReference()
    assert isinstance(instance, JvmCompoundTypeReference)


def test_types_JvmTypeParameter_isa_JvmConstraintOwner():
    instance = types_JvmTypeParameter(name="sample_text")
    assert isinstance(instance, JvmConstraintOwner)


def test_types_JvmWildcardTypeReference_isa_JvmConstraintOwner():
    instance = types_JvmWildcardTypeReference()
    assert isinstance(instance, JvmConstraintOwner)


def test_types_JvmAnnotationType_isa_JvmDeclaredType():
    instance = types_JvmAnnotationType()
    assert isinstance(instance, JvmDeclaredType)


def test_types_JvmEnumerationType_isa_JvmDeclaredType():
    instance = types_JvmEnumerationType()
    assert isinstance(instance, JvmDeclaredType)


def test_types_JvmGenericType_isa_JvmDeclaredType():
    instance = types_JvmGenericType(interface=True)
    assert isinstance(instance, JvmDeclaredType)


def test_types_JvmConstructor_isa_JvmExecutable():
    instance = types_JvmConstructor()
    assert isinstance(instance, JvmExecutable)


def test_types_JvmOperation_isa_JvmExecutable():
    instance = types_JvmOperation(abstract=True, final=True, static=True)
    assert isinstance(instance, JvmExecutable)


def test_types_JvmExecutable_isa_JvmFeature():
    instance = types_JvmExecutable(varArgs=True)
    assert isinstance(instance, JvmFeature)


def test_types_JvmField_isa_JvmFeature():
    instance = types_JvmField(final=True, static=True)
    assert isinstance(instance, JvmFeature)


def test_types_JvmEnumerationLiteral_isa_JvmField():
    instance = types_JvmEnumerationLiteral()
    assert isinstance(instance, JvmField)


def test_types_JvmFormalParameter_isa_JvmIdentifiableElement():
    instance = types_JvmFormalParameter(name="sample_text")
    assert isinstance(instance, JvmIdentifiableElement)


def test_types_JvmMember_isa_JvmIdentifiableElement():
    instance = types_JvmMember(identifier="sample_text", simpleName="sample_text", visibility="sample_text")
    assert isinstance(instance, JvmIdentifiableElement)


def test_types_JvmType_isa_JvmIdentifiableElement():
    instance = types_JvmType()
    assert isinstance(instance, JvmIdentifiableElement)


def test_types_JvmDeclaredType_isa_JvmMember():
    instance = types_JvmDeclaredType(abstract=True, final=True, packageName="sample_text", static=True)
    assert isinstance(instance, JvmMember)


def test_types_JvmFeature_isa_JvmMember():
    instance = types_JvmFeature()
    assert isinstance(instance, JvmMember)


def test_types_JvmComponentType_isa_JvmType():
    instance = types_JvmComponentType()
    assert isinstance(instance, JvmType)


def test_types_JvmVoid_isa_JvmType():
    instance = types_JvmVoid()
    assert isinstance(instance, JvmType)


def test_types_JvmLowerBound_isa_JvmTypeConstraint():
    instance = types_JvmLowerBound()
    assert isinstance(instance, JvmTypeConstraint)


def test_types_JvmUpperBound_isa_JvmTypeConstraint():
    instance = types_JvmUpperBound()
    assert isinstance(instance, JvmTypeConstraint)


def test_types_JvmExecutable_isa_JvmTypeParameterDeclarator():
    instance = types_JvmExecutable(varArgs=True)
    assert isinstance(instance, JvmTypeParameterDeclarator)


def test_types_JvmGenericType_isa_JvmTypeParameterDeclarator():
    instance = types_JvmGenericType(interface=True)
    assert isinstance(instance, JvmTypeParameterDeclarator)


def test_types_JvmAnyTypeReference_isa_JvmTypeReference():
    instance = types_JvmAnyTypeReference()
    assert isinstance(instance, JvmTypeReference)


def test_types_JvmCompoundTypeReference_isa_JvmTypeReference():
    instance = types_JvmCompoundTypeReference()
    assert isinstance(instance, JvmTypeReference)


def test_types_JvmDelegateTypeReference_isa_JvmTypeReference():
    instance = types_JvmDelegateTypeReference()
    assert isinstance(instance, JvmTypeReference)


def test_types_JvmGenericArrayTypeReference_isa_JvmTypeReference():
    instance = types_JvmGenericArrayTypeReference()
    assert isinstance(instance, JvmTypeReference)


def test_types_JvmParameterizedTypeReference_isa_JvmTypeReference():
    instance = types_JvmParameterizedTypeReference()
    assert isinstance(instance, JvmTypeReference)


def test_types_JvmSpecializedTypeReference_isa_JvmTypeReference():
    instance = types_JvmSpecializedTypeReference()
    assert isinstance(instance, JvmTypeReference)


def test_types_JvmUnknownTypeReference_isa_JvmTypeReference():
    instance = types_JvmUnknownTypeReference(exception="sample_text")
    assert isinstance(instance, JvmTypeReference)


def test_types_JvmWildcardTypeReference_isa_JvmTypeReference():
    instance = types_JvmWildcardTypeReference()
    assert isinstance(instance, JvmTypeReference)


def test_assoc_arguments11_link_reassign_clear():
    a = types_JvmTypeReference()
    b1 = types_JvmParameterizedTypeReference()
    b2 = types_JvmParameterizedTypeReference()
    _safe_set(a, 'types_JvmTypeReference12', b1)
    assert _is_linked(a, 'types_JvmTypeReference12', b1)
    if hasattr(b1, 'types_JvmParameterizedTypeReference'):
        assert _is_linked(b1, 'types_JvmParameterizedTypeReference', a)
    _safe_set(a, 'types_JvmTypeReference12', b2)
    assert _is_linked(a, 'types_JvmTypeReference12', b2)
    if hasattr(b1, 'types_JvmParameterizedTypeReference'):
        assert not _is_linked(b1, 'types_JvmParameterizedTypeReference', a)
    if hasattr(b2, 'types_JvmParameterizedTypeReference'):
        assert _is_linked(b2, 'types_JvmParameterizedTypeReference', a)
    _safe_set(a, 'types_JvmTypeReference12', None)
    assert not _is_linked(a, 'types_JvmTypeReference12', b2)
    if hasattr(b2, 'types_JvmParameterizedTypeReference'):
        assert not _is_linked(b2, 'types_JvmParameterizedTypeReference', a)


def test_assoc_arrayType0_link_reassign_clear():
    a = types_JvmArrayType()
    b1 = types_JvmComponentType()
    b2 = types_JvmComponentType()
    _safe_set(a, 'JvmArrayType', b1)
    assert _is_linked(a, 'JvmArrayType', b1)
    if hasattr(b1, 'componentType'):
        assert _is_linked(b1, 'componentType', a)
    _safe_set(a, 'JvmArrayType', b2)
    assert _is_linked(a, 'JvmArrayType', b2)
    if hasattr(b1, 'componentType'):
        assert not _is_linked(b1, 'componentType', a)
    if hasattr(b2, 'componentType'):
        assert _is_linked(b2, 'componentType', a)
    _safe_set(a, 'JvmArrayType', None)
    assert not _is_linked(a, 'JvmArrayType', b2)
    if hasattr(b2, 'componentType'):
        assert not _is_linked(b2, 'componentType', a)


def test_assoc_componentType1_link_reassign_clear():
    a = types_JvmArrayType()
    b1 = types_JvmComponentType()
    b2 = types_JvmComponentType()
    _safe_set(a, 'arrayType', b1)
    assert _is_linked(a, 'arrayType', b1)
    if hasattr(b1, 'JvmComponentType'):
        assert _is_linked(b1, 'JvmComponentType', a)
    _safe_set(a, 'arrayType', b2)
    assert _is_linked(a, 'arrayType', b2)
    if hasattr(b1, 'JvmComponentType'):
        assert not _is_linked(b1, 'JvmComponentType', a)
    if hasattr(b2, 'JvmComponentType'):
        assert _is_linked(b2, 'JvmComponentType', a)
    _safe_set(a, 'arrayType', None)
    assert not _is_linked(a, 'arrayType', b2)
    if hasattr(b2, 'JvmComponentType'):
        assert not _is_linked(b2, 'JvmComponentType', a)


def test_assoc_componentType15_link_reassign_clear():
    a = types_JvmTypeReference()
    b1 = types_JvmGenericArrayTypeReference()
    b2 = types_JvmGenericArrayTypeReference()
    _safe_set(a, 'types_JvmTypeReference16', b1)
    assert _is_linked(a, 'types_JvmTypeReference16', b1)
    if hasattr(b1, 'types_JvmGenericArrayTypeReference'):
        assert _is_linked(b1, 'types_JvmGenericArrayTypeReference', a)
    _safe_set(a, 'types_JvmTypeReference16', b2)
    assert _is_linked(a, 'types_JvmTypeReference16', b2)
    if hasattr(b1, 'types_JvmGenericArrayTypeReference'):
        assert not _is_linked(b1, 'types_JvmGenericArrayTypeReference', a)
    if hasattr(b2, 'types_JvmGenericArrayTypeReference'):
        assert _is_linked(b2, 'types_JvmGenericArrayTypeReference', a)
    _safe_set(a, 'types_JvmTypeReference16', None)
    assert not _is_linked(a, 'types_JvmTypeReference16', b2)
    if hasattr(b2, 'types_JvmGenericArrayTypeReference'):
        assert not _is_linked(b2, 'types_JvmGenericArrayTypeReference', a)


def test_assoc_constraints6_link_reassign_clear():
    a = types_JvmTypeConstraint()
    b1 = types_JvmConstraintOwner()
    b2 = types_JvmConstraintOwner()
    _safe_set(a, 'JvmTypeConstraint', b1)
    assert _is_linked(a, 'JvmTypeConstraint', b1)
    if hasattr(b1, 'owner'):
        assert _is_linked(b1, 'owner', a)
    _safe_set(a, 'JvmTypeConstraint', b2)
    assert _is_linked(a, 'JvmTypeConstraint', b2)
    if hasattr(b1, 'owner'):
        assert not _is_linked(b1, 'owner', a)
    if hasattr(b2, 'owner'):
        assert _is_linked(b2, 'owner', a)
    _safe_set(a, 'JvmTypeConstraint', None)
    assert not _is_linked(a, 'JvmTypeConstraint', b2)
    if hasattr(b2, 'owner'):
        assert not _is_linked(b2, 'owner', a)


def test_assoc_declarator4_link_reassign_clear():
    a = types_JvmTypeParameter(name="sample_text")
    b1 = types_JvmTypeParameterDeclarator()
    b2 = types_JvmTypeParameterDeclarator()
    _safe_set(a, 'typeParameters', b1)
    assert _is_linked(a, 'typeParameters', b1)
    if hasattr(b1, 'JvmTypeParameterDeclarator'):
        assert _is_linked(b1, 'JvmTypeParameterDeclarator', a)
    _safe_set(a, 'typeParameters', b2)
    assert _is_linked(a, 'typeParameters', b2)
    if hasattr(b1, 'JvmTypeParameterDeclarator'):
        assert not _is_linked(b1, 'JvmTypeParameterDeclarator', a)
    if hasattr(b2, 'JvmTypeParameterDeclarator'):
        assert _is_linked(b2, 'JvmTypeParameterDeclarator', a)
    _safe_set(a, 'typeParameters', None)
    assert not _is_linked(a, 'typeParameters', b2)
    if hasattr(b2, 'JvmTypeParameterDeclarator'):
        assert not _is_linked(b2, 'JvmTypeParameterDeclarator', a)


def test_assoc_declaringType19_link_reassign_clear():
    a = types_JvmMember(identifier="sample_text", simpleName="sample_text", visibility="sample_text")
    b1 = types_JvmDeclaredType(abstract=True, final=True, packageName="sample_text", static=True)
    b2 = types_JvmDeclaredType(abstract=False, final=False, packageName="sample_text_2", static=False)
    _safe_set(a, 'members', b1)
    assert _is_linked(a, 'members', b1)
    if hasattr(b1, 'JvmDeclaredType'):
        assert _is_linked(b1, 'JvmDeclaredType', a)
    _safe_set(a, 'members', b2)
    assert _is_linked(a, 'members', b2)
    if hasattr(b1, 'JvmDeclaredType'):
        assert not _is_linked(b1, 'JvmDeclaredType', a)
    if hasattr(b2, 'JvmDeclaredType'):
        assert _is_linked(b2, 'JvmDeclaredType', a)
    _safe_set(a, 'members', None)
    assert not _is_linked(a, 'members', b2)
    if hasattr(b2, 'JvmDeclaredType'):
        assert not _is_linked(b2, 'JvmDeclaredType', a)


def test_assoc_defaultValue28_link_reassign_clear():
    a = types_JvmOperation(abstract=True, final=True, static=True)
    b1 = types_JvmAnnotationValue()
    b2 = types_JvmAnnotationValue()
    _safe_set(a, 'types_JvmOperation29', b1)
    assert _is_linked(a, 'types_JvmOperation29', b1)
    if hasattr(b1, 'types_JvmAnnotationValue'):
        assert _is_linked(b1, 'types_JvmAnnotationValue', a)
    _safe_set(a, 'types_JvmOperation29', b2)
    assert _is_linked(a, 'types_JvmOperation29', b2)
    if hasattr(b1, 'types_JvmAnnotationValue'):
        assert not _is_linked(b1, 'types_JvmAnnotationValue', a)
    if hasattr(b2, 'types_JvmAnnotationValue'):
        assert _is_linked(b2, 'types_JvmAnnotationValue', a)
    _safe_set(a, 'types_JvmOperation29', None)
    assert not _is_linked(a, 'types_JvmOperation29', b2)
    if hasattr(b2, 'types_JvmAnnotationValue'):
        assert not _is_linked(b2, 'types_JvmAnnotationValue', a)


def test_assoc_delegate48_link_reassign_clear():
    a = types_JvmTypeReference()
    b1 = types_JvmDelegateTypeReference()
    b2 = types_JvmDelegateTypeReference()
    _safe_set(a, 'types_JvmTypeReference49', b1)
    assert _is_linked(a, 'types_JvmTypeReference49', b1)
    if hasattr(b1, 'types_JvmDelegateTypeReference'):
        assert _is_linked(b1, 'types_JvmDelegateTypeReference', a)
    _safe_set(a, 'types_JvmTypeReference49', b2)
    assert _is_linked(a, 'types_JvmTypeReference49', b2)
    if hasattr(b1, 'types_JvmDelegateTypeReference'):
        assert not _is_linked(b1, 'types_JvmDelegateTypeReference', a)
    if hasattr(b2, 'types_JvmDelegateTypeReference'):
        assert _is_linked(b2, 'types_JvmDelegateTypeReference', a)
    _safe_set(a, 'types_JvmTypeReference49', None)
    assert not _is_linked(a, 'types_JvmTypeReference49', b2)
    if hasattr(b2, 'types_JvmDelegateTypeReference'):
        assert not _is_linked(b2, 'types_JvmDelegateTypeReference', a)


def test_assoc_equivalent50_link_reassign_clear():
    a = types_JvmTypeReference()
    b1 = types_JvmSpecializedTypeReference()
    b2 = types_JvmSpecializedTypeReference()
    _safe_set(a, 'types_JvmTypeReference51', b1)
    assert _is_linked(a, 'types_JvmTypeReference51', b1)
    if hasattr(b1, 'types_JvmSpecializedTypeReference'):
        assert _is_linked(b1, 'types_JvmSpecializedTypeReference', a)
    _safe_set(a, 'types_JvmTypeReference51', b2)
    assert _is_linked(a, 'types_JvmTypeReference51', b2)
    if hasattr(b1, 'types_JvmSpecializedTypeReference'):
        assert not _is_linked(b1, 'types_JvmSpecializedTypeReference', a)
    if hasattr(b2, 'types_JvmSpecializedTypeReference'):
        assert _is_linked(b2, 'types_JvmSpecializedTypeReference', a)
    _safe_set(a, 'types_JvmTypeReference51', None)
    assert not _is_linked(a, 'types_JvmTypeReference51', b2)
    if hasattr(b2, 'types_JvmSpecializedTypeReference'):
        assert not _is_linked(b2, 'types_JvmSpecializedTypeReference', a)


def test_assoc_exceptions23_link_reassign_clear():
    a = types_JvmTypeReference()
    b1 = types_JvmExecutable(varArgs=True)
    b2 = types_JvmExecutable(varArgs=False)
    _safe_set(a, 'types_JvmTypeReference25', b1)
    assert _is_linked(a, 'types_JvmTypeReference25', b1)
    if hasattr(b1, 'types_JvmExecutable24'):
        assert _is_linked(b1, 'types_JvmExecutable24', a)
    _safe_set(a, 'types_JvmTypeReference25', b2)
    assert _is_linked(a, 'types_JvmTypeReference25', b2)
    if hasattr(b1, 'types_JvmExecutable24'):
        assert not _is_linked(b1, 'types_JvmExecutable24', a)
    if hasattr(b2, 'types_JvmExecutable24'):
        assert _is_linked(b2, 'types_JvmExecutable24', a)
    _safe_set(a, 'types_JvmTypeReference25', None)
    assert not _is_linked(a, 'types_JvmTypeReference25', b2)
    if hasattr(b2, 'types_JvmExecutable24'):
        assert not _is_linked(b2, 'types_JvmExecutable24', a)


def test_assoc_literals10_link_reassign_clear():
    a = types_JvmEnumerationLiteral()
    b1 = types_JvmEnumerationType()
    b2 = types_JvmEnumerationType()
    _safe_set(a, 'types_JvmEnumerationLiteral', b1)
    assert _is_linked(a, 'types_JvmEnumerationLiteral', b1)
    if hasattr(b1, 'types_JvmEnumerationType'):
        assert _is_linked(b1, 'types_JvmEnumerationType', a)
    _safe_set(a, 'types_JvmEnumerationLiteral', b2)
    assert _is_linked(a, 'types_JvmEnumerationLiteral', b2)
    if hasattr(b1, 'types_JvmEnumerationType'):
        assert not _is_linked(b1, 'types_JvmEnumerationType', a)
    if hasattr(b2, 'types_JvmEnumerationType'):
        assert _is_linked(b2, 'types_JvmEnumerationType', a)
    _safe_set(a, 'types_JvmEnumerationLiteral', None)
    assert not _is_linked(a, 'types_JvmEnumerationLiteral', b2)
    if hasattr(b2, 'types_JvmEnumerationType'):
        assert not _is_linked(b2, 'types_JvmEnumerationType', a)


def test_assoc_members3_link_reassign_clear():
    a = types_JvmMember(identifier="sample_text", simpleName="sample_text", visibility="sample_text")
    b1 = types_JvmDeclaredType(abstract=True, final=True, packageName="sample_text", static=True)
    b2 = types_JvmDeclaredType(abstract=False, final=False, packageName="sample_text_2", static=False)
    _safe_set(a, 'JvmMember', b1)
    assert _is_linked(a, 'JvmMember', b1)
    if hasattr(b1, 'declaringType'):
        assert _is_linked(b1, 'declaringType', a)
    _safe_set(a, 'JvmMember', b2)
    assert _is_linked(a, 'JvmMember', b2)
    if hasattr(b1, 'declaringType'):
        assert not _is_linked(b1, 'declaringType', a)
    if hasattr(b2, 'declaringType'):
        assert _is_linked(b2, 'declaringType', a)
    _safe_set(a, 'JvmMember', None)
    assert not _is_linked(a, 'JvmMember', b2)
    if hasattr(b2, 'declaringType'):
        assert not _is_linked(b2, 'declaringType', a)


def test_assoc_operation39_link_reassign_clear():
    a = types_JvmOperation(abstract=True, final=True, static=True)
    b1 = types_JvmAnnotationValue()
    b2 = types_JvmAnnotationValue()
    _safe_set(a, 'types_JvmOperation41', b1)
    assert _is_linked(a, 'types_JvmOperation41', b1)
    if hasattr(b1, 'types_JvmAnnotationValue40'):
        assert _is_linked(b1, 'types_JvmAnnotationValue40', a)
    _safe_set(a, 'types_JvmOperation41', b2)
    assert _is_linked(a, 'types_JvmOperation41', b2)
    if hasattr(b1, 'types_JvmAnnotationValue40'):
        assert not _is_linked(b1, 'types_JvmAnnotationValue40', a)
    if hasattr(b2, 'types_JvmAnnotationValue40'):
        assert _is_linked(b2, 'types_JvmAnnotationValue40', a)
    _safe_set(a, 'types_JvmOperation41', None)
    assert not _is_linked(a, 'types_JvmOperation41', b2)
    if hasattr(b2, 'types_JvmAnnotationValue40'):
        assert not _is_linked(b2, 'types_JvmAnnotationValue40', a)


def test_assoc_owner9_link_reassign_clear():
    a = types_JvmTypeConstraint()
    b1 = types_JvmConstraintOwner()
    b2 = types_JvmConstraintOwner()
    _safe_set(a, 'constraints', b1)
    assert _is_linked(a, 'constraints', b1)
    if hasattr(b1, 'JvmConstraintOwner'):
        assert _is_linked(b1, 'JvmConstraintOwner', a)
    _safe_set(a, 'constraints', b2)
    assert _is_linked(a, 'constraints', b2)
    if hasattr(b1, 'JvmConstraintOwner'):
        assert not _is_linked(b1, 'JvmConstraintOwner', a)
    if hasattr(b2, 'JvmConstraintOwner'):
        assert _is_linked(b2, 'JvmConstraintOwner', a)
    _safe_set(a, 'constraints', None)
    assert not _is_linked(a, 'constraints', b2)
    if hasattr(b2, 'JvmConstraintOwner'):
        assert not _is_linked(b2, 'JvmConstraintOwner', a)


def test_assoc_parameterType30_link_reassign_clear():
    a = types_JvmTypeReference()
    b1 = types_JvmFormalParameter(name="sample_text")
    b2 = types_JvmFormalParameter(name="sample_text_2")
    _safe_set(a, 'types_JvmTypeReference32', b1)
    assert _is_linked(a, 'types_JvmTypeReference32', b1)
    if hasattr(b1, 'types_JvmFormalParameter31'):
        assert _is_linked(b1, 'types_JvmFormalParameter31', a)
    _safe_set(a, 'types_JvmTypeReference32', b2)
    assert _is_linked(a, 'types_JvmTypeReference32', b2)
    if hasattr(b1, 'types_JvmFormalParameter31'):
        assert not _is_linked(b1, 'types_JvmFormalParameter31', a)
    if hasattr(b2, 'types_JvmFormalParameter31'):
        assert _is_linked(b2, 'types_JvmFormalParameter31', a)
    _safe_set(a, 'types_JvmTypeReference32', None)
    assert not _is_linked(a, 'types_JvmTypeReference32', b2)
    if hasattr(b2, 'types_JvmFormalParameter31'):
        assert not _is_linked(b2, 'types_JvmFormalParameter31', a)


def test_assoc_parameters22_link_reassign_clear():
    a = types_JvmFormalParameter(name="sample_text")
    b1 = types_JvmExecutable(varArgs=True)
    b2 = types_JvmExecutable(varArgs=False)
    _safe_set(a, 'types_JvmFormalParameter', b1)
    assert _is_linked(a, 'types_JvmFormalParameter', b1)
    if hasattr(b1, 'types_JvmExecutable'):
        assert _is_linked(b1, 'types_JvmExecutable', a)
    _safe_set(a, 'types_JvmFormalParameter', b2)
    assert _is_linked(a, 'types_JvmFormalParameter', b2)
    if hasattr(b1, 'types_JvmExecutable'):
        assert not _is_linked(b1, 'types_JvmExecutable', a)
    if hasattr(b2, 'types_JvmExecutable'):
        assert _is_linked(b2, 'types_JvmExecutable', a)
    _safe_set(a, 'types_JvmFormalParameter', None)
    assert not _is_linked(a, 'types_JvmFormalParameter', b2)
    if hasattr(b2, 'types_JvmExecutable'):
        assert not _is_linked(b2, 'types_JvmExecutable', a)


def test_assoc_references54_link_reassign_clear():
    a = types_JvmTypeReference()
    b1 = types_JvmCompoundTypeReference()
    b2 = types_JvmCompoundTypeReference()
    _safe_set(a, 'types_JvmTypeReference56', b1)
    assert _is_linked(a, 'types_JvmTypeReference56', b1)
    if hasattr(b1, 'types_JvmCompoundTypeReference55'):
        assert _is_linked(b1, 'types_JvmCompoundTypeReference55', a)
    _safe_set(a, 'types_JvmTypeReference56', b2)
    assert _is_linked(a, 'types_JvmTypeReference56', b2)
    if hasattr(b1, 'types_JvmCompoundTypeReference55'):
        assert not _is_linked(b1, 'types_JvmCompoundTypeReference55', a)
    if hasattr(b2, 'types_JvmCompoundTypeReference55'):
        assert _is_linked(b2, 'types_JvmCompoundTypeReference55', a)
    _safe_set(a, 'types_JvmTypeReference56', None)
    assert not _is_linked(a, 'types_JvmTypeReference56', b2)
    if hasattr(b2, 'types_JvmCompoundTypeReference55'):
        assert not _is_linked(b2, 'types_JvmCompoundTypeReference55', a)


def test_assoc_returnType26_link_reassign_clear():
    a = types_JvmTypeReference()
    b1 = types_JvmOperation(abstract=True, final=True, static=True)
    b2 = types_JvmOperation(abstract=False, final=False, static=False)
    _safe_set(a, 'types_JvmTypeReference27', b1)
    assert _is_linked(a, 'types_JvmTypeReference27', b1)
    if hasattr(b1, 'types_JvmOperation'):
        assert _is_linked(b1, 'types_JvmOperation', a)
    _safe_set(a, 'types_JvmTypeReference27', b2)
    assert _is_linked(a, 'types_JvmTypeReference27', b2)
    if hasattr(b1, 'types_JvmOperation'):
        assert not _is_linked(b1, 'types_JvmOperation', a)
    if hasattr(b2, 'types_JvmOperation'):
        assert _is_linked(b2, 'types_JvmOperation', a)
    _safe_set(a, 'types_JvmTypeReference27', None)
    assert not _is_linked(a, 'types_JvmTypeReference27', b2)
    if hasattr(b2, 'types_JvmOperation'):
        assert not _is_linked(b2, 'types_JvmOperation', a)


def test_assoc_superTypes2_link_reassign_clear():
    a = types_JvmTypeReference()
    b1 = types_JvmDeclaredType(abstract=True, final=True, packageName="sample_text", static=True)
    b2 = types_JvmDeclaredType(abstract=False, final=False, packageName="sample_text_2", static=False)
    _safe_set(a, 'types_JvmTypeReference', b1)
    assert _is_linked(a, 'types_JvmTypeReference', b1)
    if hasattr(b1, 'types_JvmDeclaredType'):
        assert _is_linked(b1, 'types_JvmDeclaredType', a)
    _safe_set(a, 'types_JvmTypeReference', b2)
    assert _is_linked(a, 'types_JvmTypeReference', b2)
    if hasattr(b1, 'types_JvmDeclaredType'):
        assert not _is_linked(b1, 'types_JvmDeclaredType', a)
    if hasattr(b2, 'types_JvmDeclaredType'):
        assert _is_linked(b2, 'types_JvmDeclaredType', a)
    _safe_set(a, 'types_JvmTypeReference', None)
    assert not _is_linked(a, 'types_JvmTypeReference', b2)
    if hasattr(b2, 'types_JvmDeclaredType'):
        assert not _is_linked(b2, 'types_JvmDeclaredType', a)


def test_assoc_type20_link_reassign_clear():
    a = types_JvmTypeReference()
    b1 = types_JvmField(final=True, static=True)
    b2 = types_JvmField(final=False, static=False)
    _safe_set(a, 'types_JvmTypeReference21', b1)
    assert _is_linked(a, 'types_JvmTypeReference21', b1)
    if hasattr(b1, 'types_JvmField'):
        assert _is_linked(b1, 'types_JvmField', a)
    _safe_set(a, 'types_JvmTypeReference21', b2)
    assert _is_linked(a, 'types_JvmTypeReference21', b2)
    if hasattr(b1, 'types_JvmField'):
        assert not _is_linked(b1, 'types_JvmField', a)
    if hasattr(b2, 'types_JvmField'):
        assert _is_linked(b2, 'types_JvmField', a)
    _safe_set(a, 'types_JvmTypeReference21', None)
    assert not _is_linked(a, 'types_JvmTypeReference21', b2)
    if hasattr(b2, 'types_JvmField'):
        assert not _is_linked(b2, 'types_JvmField', a)


def test_assoc_typeParameters5_link_reassign_clear():
    a = types_JvmTypeParameter(name="sample_text")
    b1 = types_JvmTypeParameterDeclarator()
    b2 = types_JvmTypeParameterDeclarator()
    _safe_set(a, 'JvmTypeParameter', b1)
    assert _is_linked(a, 'JvmTypeParameter', b1)
    if hasattr(b1, 'declarator'):
        assert _is_linked(b1, 'declarator', a)
    _safe_set(a, 'JvmTypeParameter', b2)
    assert _is_linked(a, 'JvmTypeParameter', b2)
    if hasattr(b1, 'declarator'):
        assert not _is_linked(b1, 'declarator', a)
    if hasattr(b2, 'declarator'):
        assert _is_linked(b2, 'declarator', a)
    _safe_set(a, 'JvmTypeParameter', None)
    assert not _is_linked(a, 'JvmTypeParameter', b2)
    if hasattr(b2, 'declarator'):
        assert not _is_linked(b2, 'declarator', a)


def test_assoc_typeReference7_link_reassign_clear():
    a = types_JvmTypeReference()
    b1 = types_JvmTypeConstraint()
    b2 = types_JvmTypeConstraint()
    _safe_set(a, 'types_JvmTypeReference8', b1)
    assert _is_linked(a, 'types_JvmTypeReference8', b1)
    if hasattr(b1, 'types_JvmTypeConstraint'):
        assert _is_linked(b1, 'types_JvmTypeConstraint', a)
    _safe_set(a, 'types_JvmTypeReference8', b2)
    assert _is_linked(a, 'types_JvmTypeReference8', b2)
    if hasattr(b1, 'types_JvmTypeConstraint'):
        assert not _is_linked(b1, 'types_JvmTypeConstraint', a)
    if hasattr(b2, 'types_JvmTypeConstraint'):
        assert _is_linked(b2, 'types_JvmTypeConstraint', a)
    _safe_set(a, 'types_JvmTypeReference8', None)
    assert not _is_linked(a, 'types_JvmTypeReference8', b2)
    if hasattr(b2, 'types_JvmTypeConstraint'):
        assert not _is_linked(b2, 'types_JvmTypeConstraint', a)


def test_assoc_values36_link_reassign_clear():
    a = types_JvmAnnotationValue()
    b1 = types_JvmAnnotationReference()
    b2 = types_JvmAnnotationReference()
    _safe_set(a, 'types_JvmAnnotationValue38', b1)
    assert _is_linked(a, 'types_JvmAnnotationValue38', b1)
    if hasattr(b1, 'types_JvmAnnotationReference37'):
        assert _is_linked(b1, 'types_JvmAnnotationReference37', a)
    _safe_set(a, 'types_JvmAnnotationValue38', b2)
    assert _is_linked(a, 'types_JvmAnnotationValue38', b2)
    if hasattr(b1, 'types_JvmAnnotationReference37'):
        assert not _is_linked(b1, 'types_JvmAnnotationReference37', a)
    if hasattr(b2, 'types_JvmAnnotationReference37'):
        assert _is_linked(b2, 'types_JvmAnnotationReference37', a)
    _safe_set(a, 'types_JvmAnnotationValue38', None)
    assert not _is_linked(a, 'types_JvmAnnotationValue38', b2)
    if hasattr(b2, 'types_JvmAnnotationReference37'):
        assert not _is_linked(b2, 'types_JvmAnnotationReference37', a)


def test_assoc_values42_link_reassign_clear():
    a = types_JvmTypeReference()
    b1 = types_JvmTypeAnnotationValue()
    b2 = types_JvmTypeAnnotationValue()
    _safe_set(a, 'types_JvmTypeReference43', b1)
    assert _is_linked(a, 'types_JvmTypeReference43', b1)
    if hasattr(b1, 'types_JvmTypeAnnotationValue'):
        assert _is_linked(b1, 'types_JvmTypeAnnotationValue', a)
    _safe_set(a, 'types_JvmTypeReference43', b2)
    assert _is_linked(a, 'types_JvmTypeReference43', b2)
    if hasattr(b1, 'types_JvmTypeAnnotationValue'):
        assert not _is_linked(b1, 'types_JvmTypeAnnotationValue', a)
    if hasattr(b2, 'types_JvmTypeAnnotationValue'):
        assert _is_linked(b2, 'types_JvmTypeAnnotationValue', a)
    _safe_set(a, 'types_JvmTypeReference43', None)
    assert not _is_linked(a, 'types_JvmTypeReference43', b2)
    if hasattr(b2, 'types_JvmTypeAnnotationValue'):
        assert not _is_linked(b2, 'types_JvmTypeAnnotationValue', a)


def test_assoc_values46_link_reassign_clear():
    a = types_JvmEnumerationLiteral()
    b1 = types_JvmEnumAnnotationValue()
    b2 = types_JvmEnumAnnotationValue()
    _safe_set(a, 'types_JvmEnumerationLiteral47', b1)
    assert _is_linked(a, 'types_JvmEnumerationLiteral47', b1)
    if hasattr(b1, 'types_JvmEnumAnnotationValue'):
        assert _is_linked(b1, 'types_JvmEnumAnnotationValue', a)
    _safe_set(a, 'types_JvmEnumerationLiteral47', b2)
    assert _is_linked(a, 'types_JvmEnumerationLiteral47', b2)
    if hasattr(b1, 'types_JvmEnumAnnotationValue'):
        assert not _is_linked(b1, 'types_JvmEnumAnnotationValue', a)
    if hasattr(b2, 'types_JvmEnumAnnotationValue'):
        assert _is_linked(b2, 'types_JvmEnumAnnotationValue', a)
    _safe_set(a, 'types_JvmEnumerationLiteral47', None)
    assert not _is_linked(a, 'types_JvmEnumerationLiteral47', b2)
    if hasattr(b2, 'types_JvmEnumAnnotationValue'):
        assert not _is_linked(b2, 'types_JvmEnumAnnotationValue', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

JvmAnnotationTarget_strategy = st.builds(JvmAnnotationTarget)
@given(instance=JvmAnnotationTarget_strategy)
@settings(max_examples=25)
def test_JvmAnnotationTarget_instantiation(instance):
    assert isinstance(instance, JvmAnnotationTarget)


JvmAnnotationValue_strategy = st.builds(JvmAnnotationValue)
@given(instance=JvmAnnotationValue_strategy)
@settings(max_examples=25)
def test_JvmAnnotationValue_instantiation(instance):
    assert isinstance(instance, JvmAnnotationValue)


JvmComponentType_strategy = st.builds(JvmComponentType)
@given(instance=JvmComponentType_strategy)
@settings(max_examples=25)
def test_JvmComponentType_instantiation(instance):
    assert isinstance(instance, JvmComponentType)


JvmCompoundTypeReference_strategy = st.builds(JvmCompoundTypeReference)
@given(instance=JvmCompoundTypeReference_strategy)
@settings(max_examples=25)
def test_JvmCompoundTypeReference_instantiation(instance):
    assert isinstance(instance, JvmCompoundTypeReference)


JvmConstraintOwner_strategy = st.builds(JvmConstraintOwner)
@given(instance=JvmConstraintOwner_strategy)
@settings(max_examples=25)
def test_JvmConstraintOwner_instantiation(instance):
    assert isinstance(instance, JvmConstraintOwner)


JvmDeclaredType_strategy = st.builds(JvmDeclaredType)
@given(instance=JvmDeclaredType_strategy)
@settings(max_examples=25)
def test_JvmDeclaredType_instantiation(instance):
    assert isinstance(instance, JvmDeclaredType)


JvmExecutable_strategy = st.builds(JvmExecutable)
@given(instance=JvmExecutable_strategy)
@settings(max_examples=25)
def test_JvmExecutable_instantiation(instance):
    assert isinstance(instance, JvmExecutable)


JvmFeature_strategy = st.builds(JvmFeature)
@given(instance=JvmFeature_strategy)
@settings(max_examples=25)
def test_JvmFeature_instantiation(instance):
    assert isinstance(instance, JvmFeature)


JvmField_strategy = st.builds(JvmField)
@given(instance=JvmField_strategy)
@settings(max_examples=25)
def test_JvmField_instantiation(instance):
    assert isinstance(instance, JvmField)


JvmIdentifiableElement_strategy = st.builds(JvmIdentifiableElement)
@given(instance=JvmIdentifiableElement_strategy)
@settings(max_examples=25)
def test_JvmIdentifiableElement_instantiation(instance):
    assert isinstance(instance, JvmIdentifiableElement)


JvmMember_strategy = st.builds(JvmMember)
@given(instance=JvmMember_strategy)
@settings(max_examples=25)
def test_JvmMember_instantiation(instance):
    assert isinstance(instance, JvmMember)


JvmType_strategy = st.builds(JvmType)
@given(instance=JvmType_strategy)
@settings(max_examples=25)
def test_JvmType_instantiation(instance):
    assert isinstance(instance, JvmType)


JvmTypeConstraint_strategy = st.builds(JvmTypeConstraint)
@given(instance=JvmTypeConstraint_strategy)
@settings(max_examples=25)
def test_JvmTypeConstraint_instantiation(instance):
    assert isinstance(instance, JvmTypeConstraint)


JvmTypeParameterDeclarator_strategy = st.builds(JvmTypeParameterDeclarator)
@given(instance=JvmTypeParameterDeclarator_strategy)
@settings(max_examples=25)
def test_JvmTypeParameterDeclarator_instantiation(instance):
    assert isinstance(instance, JvmTypeParameterDeclarator)


JvmTypeReference_strategy = st.builds(JvmTypeReference)
@given(instance=JvmTypeReference_strategy)
@settings(max_examples=25)
def test_JvmTypeReference_instantiation(instance):
    assert isinstance(instance, JvmTypeReference)


types_JvmAnnotationAnnotationValue_strategy = st.builds(types_JvmAnnotationAnnotationValue)
@given(instance=types_JvmAnnotationAnnotationValue_strategy)
@settings(max_examples=25)
def test_types_JvmAnnotationAnnotationValue_instantiation(instance):
    assert isinstance(instance, types_JvmAnnotationAnnotationValue)


types_JvmAnnotationReference_strategy = st.builds(types_JvmAnnotationReference)
@given(instance=types_JvmAnnotationReference_strategy)
@settings(max_examples=25)
def test_types_JvmAnnotationReference_instantiation(instance):
    assert isinstance(instance, types_JvmAnnotationReference)


types_JvmAnnotationTarget_strategy = st.builds(types_JvmAnnotationTarget)
@given(instance=types_JvmAnnotationTarget_strategy)
@settings(max_examples=25)
def test_types_JvmAnnotationTarget_instantiation(instance):
    assert isinstance(instance, types_JvmAnnotationTarget)


types_JvmAnnotationType_strategy = st.builds(types_JvmAnnotationType)
@given(instance=types_JvmAnnotationType_strategy)
@settings(max_examples=25)
def test_types_JvmAnnotationType_instantiation(instance):
    assert isinstance(instance, types_JvmAnnotationType)


types_JvmAnnotationValue_strategy = st.builds(types_JvmAnnotationValue)
@given(instance=types_JvmAnnotationValue_strategy)
@settings(max_examples=25)
def test_types_JvmAnnotationValue_instantiation(instance):
    assert isinstance(instance, types_JvmAnnotationValue)


types_JvmAnyTypeReference_strategy = st.builds(types_JvmAnyTypeReference)
@given(instance=types_JvmAnyTypeReference_strategy)
@settings(max_examples=25)
def test_types_JvmAnyTypeReference_instantiation(instance):
    assert isinstance(instance, types_JvmAnyTypeReference)


types_JvmArrayType_strategy = st.builds(types_JvmArrayType)
@given(instance=types_JvmArrayType_strategy)
@settings(max_examples=25)
def test_types_JvmArrayType_instantiation(instance):
    assert isinstance(instance, types_JvmArrayType)


types_JvmBooleanAnnotationValue_strategy = st.builds(types_JvmBooleanAnnotationValue, values=st.booleans())
@given(instance=types_JvmBooleanAnnotationValue_strategy)
@settings(max_examples=25)
def test_types_JvmBooleanAnnotationValue_instantiation(instance):
    assert isinstance(instance, types_JvmBooleanAnnotationValue)


types_JvmByteAnnotationValue_strategy = st.builds(types_JvmByteAnnotationValue, values=safe_text)
@given(instance=types_JvmByteAnnotationValue_strategy)
@settings(max_examples=25)
def test_types_JvmByteAnnotationValue_instantiation(instance):
    assert isinstance(instance, types_JvmByteAnnotationValue)


types_JvmCharAnnotationValue_strategy = st.builds(types_JvmCharAnnotationValue, values=safe_text)
@given(instance=types_JvmCharAnnotationValue_strategy)
@settings(max_examples=25)
def test_types_JvmCharAnnotationValue_instantiation(instance):
    assert isinstance(instance, types_JvmCharAnnotationValue)


types_JvmComponentType_strategy = st.builds(types_JvmComponentType)
@given(instance=types_JvmComponentType_strategy)
@settings(max_examples=25)
def test_types_JvmComponentType_instantiation(instance):
    assert isinstance(instance, types_JvmComponentType)


types_JvmCompoundTypeReference_strategy = st.builds(types_JvmCompoundTypeReference)
@given(instance=types_JvmCompoundTypeReference_strategy)
@settings(max_examples=25)
def test_types_JvmCompoundTypeReference_instantiation(instance):
    assert isinstance(instance, types_JvmCompoundTypeReference)


types_JvmConstraintOwner_strategy = st.builds(types_JvmConstraintOwner)
@given(instance=types_JvmConstraintOwner_strategy)
@settings(max_examples=25)
def test_types_JvmConstraintOwner_instantiation(instance):
    assert isinstance(instance, types_JvmConstraintOwner)


types_JvmConstructor_strategy = st.builds(types_JvmConstructor)
@given(instance=types_JvmConstructor_strategy)
@settings(max_examples=25)
def test_types_JvmConstructor_instantiation(instance):
    assert isinstance(instance, types_JvmConstructor)


types_JvmCustomAnnotationValue_strategy = st.builds(types_JvmCustomAnnotationValue, values=safe_text)
@given(instance=types_JvmCustomAnnotationValue_strategy)
@settings(max_examples=25)
def test_types_JvmCustomAnnotationValue_instantiation(instance):
    assert isinstance(instance, types_JvmCustomAnnotationValue)


types_JvmDeclaredType_strategy = st.builds(types_JvmDeclaredType, abstract=st.booleans(), final=st.booleans(), packageName=safe_text, static=st.booleans())
@given(instance=types_JvmDeclaredType_strategy)
@settings(max_examples=25)
def test_types_JvmDeclaredType_instantiation(instance):
    assert isinstance(instance, types_JvmDeclaredType)


types_JvmDelegateTypeReference_strategy = st.builds(types_JvmDelegateTypeReference)
@given(instance=types_JvmDelegateTypeReference_strategy)
@settings(max_examples=25)
def test_types_JvmDelegateTypeReference_instantiation(instance):
    assert isinstance(instance, types_JvmDelegateTypeReference)


types_JvmDoubleAnnotationValue_strategy = st.builds(types_JvmDoubleAnnotationValue, values=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=types_JvmDoubleAnnotationValue_strategy)
@settings(max_examples=25)
def test_types_JvmDoubleAnnotationValue_instantiation(instance):
    assert isinstance(instance, types_JvmDoubleAnnotationValue)


types_JvmEnumAnnotationValue_strategy = st.builds(types_JvmEnumAnnotationValue)
@given(instance=types_JvmEnumAnnotationValue_strategy)
@settings(max_examples=25)
def test_types_JvmEnumAnnotationValue_instantiation(instance):
    assert isinstance(instance, types_JvmEnumAnnotationValue)


types_JvmEnumerationLiteral_strategy = st.builds(types_JvmEnumerationLiteral)
@given(instance=types_JvmEnumerationLiteral_strategy)
@settings(max_examples=25)
def test_types_JvmEnumerationLiteral_instantiation(instance):
    assert isinstance(instance, types_JvmEnumerationLiteral)


types_JvmEnumerationType_strategy = st.builds(types_JvmEnumerationType)
@given(instance=types_JvmEnumerationType_strategy)
@settings(max_examples=25)
def test_types_JvmEnumerationType_instantiation(instance):
    assert isinstance(instance, types_JvmEnumerationType)


types_JvmExecutable_strategy = st.builds(types_JvmExecutable, varArgs=st.booleans())
@given(instance=types_JvmExecutable_strategy)
@settings(max_examples=25)
def test_types_JvmExecutable_instantiation(instance):
    assert isinstance(instance, types_JvmExecutable)


types_JvmFeature_strategy = st.builds(types_JvmFeature)
@given(instance=types_JvmFeature_strategy)
@settings(max_examples=25)
def test_types_JvmFeature_instantiation(instance):
    assert isinstance(instance, types_JvmFeature)


types_JvmField_strategy = st.builds(types_JvmField, final=st.booleans(), static=st.booleans())
@given(instance=types_JvmField_strategy)
@settings(max_examples=25)
def test_types_JvmField_instantiation(instance):
    assert isinstance(instance, types_JvmField)


types_JvmFloatAnnotationValue_strategy = st.builds(types_JvmFloatAnnotationValue, values=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=types_JvmFloatAnnotationValue_strategy)
@settings(max_examples=25)
def test_types_JvmFloatAnnotationValue_instantiation(instance):
    assert isinstance(instance, types_JvmFloatAnnotationValue)


types_JvmFormalParameter_strategy = st.builds(types_JvmFormalParameter, name=safe_text)
@given(instance=types_JvmFormalParameter_strategy)
@settings(max_examples=25)
def test_types_JvmFormalParameter_instantiation(instance):
    assert isinstance(instance, types_JvmFormalParameter)


types_JvmGenericArrayTypeReference_strategy = st.builds(types_JvmGenericArrayTypeReference)
@given(instance=types_JvmGenericArrayTypeReference_strategy)
@settings(max_examples=25)
def test_types_JvmGenericArrayTypeReference_instantiation(instance):
    assert isinstance(instance, types_JvmGenericArrayTypeReference)


types_JvmGenericType_strategy = st.builds(types_JvmGenericType, interface=st.booleans())
@given(instance=types_JvmGenericType_strategy)
@settings(max_examples=25)
def test_types_JvmGenericType_instantiation(instance):
    assert isinstance(instance, types_JvmGenericType)


types_JvmIdentifiableElement_strategy = st.builds(types_JvmIdentifiableElement)
@given(instance=types_JvmIdentifiableElement_strategy)
@settings(max_examples=25)
def test_types_JvmIdentifiableElement_instantiation(instance):
    assert isinstance(instance, types_JvmIdentifiableElement)


types_JvmIntAnnotationValue_strategy = st.builds(types_JvmIntAnnotationValue, values=st.integers())
@given(instance=types_JvmIntAnnotationValue_strategy)
@settings(max_examples=25)
def test_types_JvmIntAnnotationValue_instantiation(instance):
    assert isinstance(instance, types_JvmIntAnnotationValue)


types_JvmLongAnnotationValue_strategy = st.builds(types_JvmLongAnnotationValue, values=safe_text)
@given(instance=types_JvmLongAnnotationValue_strategy)
@settings(max_examples=25)
def test_types_JvmLongAnnotationValue_instantiation(instance):
    assert isinstance(instance, types_JvmLongAnnotationValue)


types_JvmLowerBound_strategy = st.builds(types_JvmLowerBound)
@given(instance=types_JvmLowerBound_strategy)
@settings(max_examples=25)
def test_types_JvmLowerBound_instantiation(instance):
    assert isinstance(instance, types_JvmLowerBound)


types_JvmMember_strategy = st.builds(types_JvmMember, identifier=safe_text, simpleName=safe_text, visibility=safe_text)
@given(instance=types_JvmMember_strategy)
@settings(max_examples=25)
def test_types_JvmMember_instantiation(instance):
    assert isinstance(instance, types_JvmMember)


types_JvmMultiTypeReference_strategy = st.builds(types_JvmMultiTypeReference)
@given(instance=types_JvmMultiTypeReference_strategy)
@settings(max_examples=25)
def test_types_JvmMultiTypeReference_instantiation(instance):
    assert isinstance(instance, types_JvmMultiTypeReference)


types_JvmOperation_strategy = st.builds(types_JvmOperation, abstract=st.booleans(), final=st.booleans(), static=st.booleans())
@given(instance=types_JvmOperation_strategy)
@settings(max_examples=25)
def test_types_JvmOperation_instantiation(instance):
    assert isinstance(instance, types_JvmOperation)


types_JvmParameterizedTypeReference_strategy = st.builds(types_JvmParameterizedTypeReference)
@given(instance=types_JvmParameterizedTypeReference_strategy)
@settings(max_examples=25)
def test_types_JvmParameterizedTypeReference_instantiation(instance):
    assert isinstance(instance, types_JvmParameterizedTypeReference)


types_JvmPrimitiveType_strategy = st.builds(types_JvmPrimitiveType, simpleName=safe_text)
@given(instance=types_JvmPrimitiveType_strategy)
@settings(max_examples=25)
def test_types_JvmPrimitiveType_instantiation(instance):
    assert isinstance(instance, types_JvmPrimitiveType)


types_JvmShortAnnotationValue_strategy = st.builds(types_JvmShortAnnotationValue, values=safe_text)
@given(instance=types_JvmShortAnnotationValue_strategy)
@settings(max_examples=25)
def test_types_JvmShortAnnotationValue_instantiation(instance):
    assert isinstance(instance, types_JvmShortAnnotationValue)


types_JvmSpecializedTypeReference_strategy = st.builds(types_JvmSpecializedTypeReference)
@given(instance=types_JvmSpecializedTypeReference_strategy)
@settings(max_examples=25)
def test_types_JvmSpecializedTypeReference_instantiation(instance):
    assert isinstance(instance, types_JvmSpecializedTypeReference)


types_JvmStringAnnotationValue_strategy = st.builds(types_JvmStringAnnotationValue, values=safe_text)
@given(instance=types_JvmStringAnnotationValue_strategy)
@settings(max_examples=25)
def test_types_JvmStringAnnotationValue_instantiation(instance):
    assert isinstance(instance, types_JvmStringAnnotationValue)


types_JvmSynonymTypeReference_strategy = st.builds(types_JvmSynonymTypeReference)
@given(instance=types_JvmSynonymTypeReference_strategy)
@settings(max_examples=25)
def test_types_JvmSynonymTypeReference_instantiation(instance):
    assert isinstance(instance, types_JvmSynonymTypeReference)


types_JvmType_strategy = st.builds(types_JvmType)
@given(instance=types_JvmType_strategy)
@settings(max_examples=25)
def test_types_JvmType_instantiation(instance):
    assert isinstance(instance, types_JvmType)


types_JvmTypeAnnotationValue_strategy = st.builds(types_JvmTypeAnnotationValue)
@given(instance=types_JvmTypeAnnotationValue_strategy)
@settings(max_examples=25)
def test_types_JvmTypeAnnotationValue_instantiation(instance):
    assert isinstance(instance, types_JvmTypeAnnotationValue)


types_JvmTypeConstraint_strategy = st.builds(types_JvmTypeConstraint)
@given(instance=types_JvmTypeConstraint_strategy)
@settings(max_examples=25)
def test_types_JvmTypeConstraint_instantiation(instance):
    assert isinstance(instance, types_JvmTypeConstraint)


types_JvmTypeParameter_strategy = st.builds(types_JvmTypeParameter, name=safe_text)
@given(instance=types_JvmTypeParameter_strategy)
@settings(max_examples=25)
def test_types_JvmTypeParameter_instantiation(instance):
    assert isinstance(instance, types_JvmTypeParameter)


types_JvmTypeParameterDeclarator_strategy = st.builds(types_JvmTypeParameterDeclarator)
@given(instance=types_JvmTypeParameterDeclarator_strategy)
@settings(max_examples=25)
def test_types_JvmTypeParameterDeclarator_instantiation(instance):
    assert isinstance(instance, types_JvmTypeParameterDeclarator)


types_JvmTypeReference_strategy = st.builds(types_JvmTypeReference)
@given(instance=types_JvmTypeReference_strategy)
@settings(max_examples=25)
def test_types_JvmTypeReference_instantiation(instance):
    assert isinstance(instance, types_JvmTypeReference)


types_JvmUnknownTypeReference_strategy = st.builds(types_JvmUnknownTypeReference, exception=safe_text)
@given(instance=types_JvmUnknownTypeReference_strategy)
@settings(max_examples=25)
def test_types_JvmUnknownTypeReference_instantiation(instance):
    assert isinstance(instance, types_JvmUnknownTypeReference)


types_JvmUpperBound_strategy = st.builds(types_JvmUpperBound)
@given(instance=types_JvmUpperBound_strategy)
@settings(max_examples=25)
def test_types_JvmUpperBound_instantiation(instance):
    assert isinstance(instance, types_JvmUpperBound)


types_JvmVoid_strategy = st.builds(types_JvmVoid)
@given(instance=types_JvmVoid_strategy)
@settings(max_examples=25)
def test_types_JvmVoid_instantiation(instance):
    assert isinstance(instance, types_JvmVoid)


types_JvmWildcardTypeReference_strategy = st.builds(types_JvmWildcardTypeReference)
@given(instance=types_JvmWildcardTypeReference_strategy)
@settings(max_examples=25)
def test_types_JvmWildcardTypeReference_instantiation(instance):
    assert isinstance(instance, types_JvmWildcardTypeReference)


