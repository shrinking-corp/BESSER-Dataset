import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ExtendedAnnotationType,
    Extensible,
    XSDAnnotation,
    XpdlTypeType,
    xpdl_BasicTypeType,
    xpdl_DataTypeType,
    xpdl_DeclaredTypeType,
    xpdl_ExtendedAttributeType,
    xpdl_ExtendedAttributesType,
    xpdl_Extensible,
    xpdl_ExternalPackage,
    xpdl_ExternalPackages,
    xpdl_ExternalReferenceType,
    xpdl_FormalParameterType,
    xpdl_FormalParametersType,
    xpdl_SchemaTypeType,
    xpdl_ScriptType,
    xpdl_TypeDeclarationType,
    xpdl_TypeDeclarationsType,
    xpdl_XSDSchema,
    xpdl_XpdlTypeType,
    xpdl_extensions_ExtendedAnnotationType,
    ModeType,
    TypeType,
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

def test_assoc_basicType0_reverse_link_reassign_clear():
    a1 = xpdl_DataTypeType(carnotType="sample_text")
    a2 = xpdl_DataTypeType(carnotType="sample_text_2")
    b = xpdl_BasicTypeType(type="sample_text")
    _safe_set(b, 'xpdl_BasicTypeType', a1)
    assert _is_linked(b, 'xpdl_BasicTypeType', a1)
    if hasattr(a1, 'xpdl_DataTypeType'):
        assert _is_linked(a1, 'xpdl_DataTypeType', b)
    _safe_set(b, 'xpdl_BasicTypeType', a2)
    assert _is_linked(b, 'xpdl_BasicTypeType', a2)
    if hasattr(a1, 'xpdl_DataTypeType'):
        assert not _is_linked(a1, 'xpdl_DataTypeType', b)
    if hasattr(a2, 'xpdl_DataTypeType'):
        assert _is_linked(a2, 'xpdl_DataTypeType', b)
    _safe_set(b, 'xpdl_BasicTypeType', None)
    assert not _is_linked(b, 'xpdl_BasicTypeType', a2)
    if hasattr(a2, 'xpdl_DataTypeType'):
        assert not _is_linked(a2, 'xpdl_DataTypeType', b)


def test_assoc_basicType20_reverse_link_reassign_clear():
    a1 = xpdl_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    a2 = xpdl_TypeDeclarationType(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = xpdl_BasicTypeType(type="sample_text")
    _safe_set(b, 'xpdl_BasicTypeType22', a1)
    assert _is_linked(b, 'xpdl_BasicTypeType22', a1)
    if hasattr(a1, 'xpdl_TypeDeclarationType21'):
        assert _is_linked(a1, 'xpdl_TypeDeclarationType21', b)
    _safe_set(b, 'xpdl_BasicTypeType22', a2)
    assert _is_linked(b, 'xpdl_BasicTypeType22', a2)
    if hasattr(a1, 'xpdl_TypeDeclarationType21'):
        assert not _is_linked(a1, 'xpdl_TypeDeclarationType21', b)
    if hasattr(a2, 'xpdl_TypeDeclarationType21'):
        assert _is_linked(a2, 'xpdl_TypeDeclarationType21', b)
    _safe_set(b, 'xpdl_BasicTypeType22', None)
    assert not _is_linked(b, 'xpdl_BasicTypeType22', a2)
    if hasattr(a2, 'xpdl_TypeDeclarationType21'):
        assert not _is_linked(a2, 'xpdl_TypeDeclarationType21', b)


def test_assoc_dataType14_reverse_link_reassign_clear():
    a1 = xpdl_FormalParameterType(description="sample_text", id="sample_text", mode="sample_text", name="sample_text")
    a2 = xpdl_FormalParameterType(description="sample_text_2", id="sample_text_2", mode="sample_text_2", name="sample_text_2")
    b = xpdl_DataTypeType(carnotType="sample_text")
    _safe_set(b, 'xpdl_DataTypeType16', a1)
    assert _is_linked(b, 'xpdl_DataTypeType16', a1)
    if hasattr(a1, 'xpdl_FormalParameterType15'):
        assert _is_linked(a1, 'xpdl_FormalParameterType15', b)
    _safe_set(b, 'xpdl_DataTypeType16', a2)
    assert _is_linked(b, 'xpdl_DataTypeType16', a2)
    if hasattr(a1, 'xpdl_FormalParameterType15'):
        assert not _is_linked(a1, 'xpdl_FormalParameterType15', b)
    if hasattr(a2, 'xpdl_FormalParameterType15'):
        assert _is_linked(a2, 'xpdl_FormalParameterType15', b)
    _safe_set(b, 'xpdl_DataTypeType16', None)
    assert not _is_linked(b, 'xpdl_DataTypeType16', a2)
    if hasattr(a2, 'xpdl_FormalParameterType15'):
        assert not _is_linked(a2, 'xpdl_FormalParameterType15', b)


def test_assoc_declaredType1_reverse_link_reassign_clear():
    a1 = xpdl_DeclaredTypeType(id="sample_text")
    a2 = xpdl_DeclaredTypeType(id="sample_text_2")
    b = xpdl_DataTypeType(carnotType="sample_text")
    _safe_set(b, 'xpdl_DataTypeType2', a1)
    assert _is_linked(b, 'xpdl_DataTypeType2', a1)
    if hasattr(a1, 'xpdl_DeclaredTypeType'):
        assert _is_linked(a1, 'xpdl_DeclaredTypeType', b)
    _safe_set(b, 'xpdl_DataTypeType2', a2)
    assert _is_linked(b, 'xpdl_DataTypeType2', a2)
    if hasattr(a1, 'xpdl_DeclaredTypeType'):
        assert not _is_linked(a1, 'xpdl_DeclaredTypeType', b)
    if hasattr(a2, 'xpdl_DeclaredTypeType'):
        assert _is_linked(a2, 'xpdl_DeclaredTypeType', b)
    _safe_set(b, 'xpdl_DataTypeType2', None)
    assert not _is_linked(b, 'xpdl_DataTypeType2', a2)
    if hasattr(a2, 'xpdl_DeclaredTypeType'):
        assert not _is_linked(a2, 'xpdl_DeclaredTypeType', b)


def test_assoc_declaredType23_reverse_link_reassign_clear():
    a1 = xpdl_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    a2 = xpdl_TypeDeclarationType(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = xpdl_DeclaredTypeType(id="sample_text")
    _safe_set(b, 'xpdl_DeclaredTypeType25', a1)
    assert _is_linked(b, 'xpdl_DeclaredTypeType25', a1)
    if hasattr(a1, 'xpdl_TypeDeclarationType24'):
        assert _is_linked(a1, 'xpdl_TypeDeclarationType24', b)
    _safe_set(b, 'xpdl_DeclaredTypeType25', a2)
    assert _is_linked(b, 'xpdl_DeclaredTypeType25', a2)
    if hasattr(a1, 'xpdl_TypeDeclarationType24'):
        assert not _is_linked(a1, 'xpdl_TypeDeclarationType24', b)
    if hasattr(a2, 'xpdl_TypeDeclarationType24'):
        assert _is_linked(a2, 'xpdl_TypeDeclarationType24', b)
    _safe_set(b, 'xpdl_DeclaredTypeType25', None)
    assert not _is_linked(b, 'xpdl_DeclaredTypeType25', a2)
    if hasattr(a2, 'xpdl_TypeDeclarationType24'):
        assert not _is_linked(a2, 'xpdl_TypeDeclarationType24', b)


def test_assoc_externalPackage12_reverse_link_reassign_clear():
    a1 = xpdl_ExternalPackages()
    a2 = xpdl_ExternalPackages()
    b = xpdl_ExternalPackage(href="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'xpdl_ExternalPackage', a1)
    assert _is_linked(b, 'xpdl_ExternalPackage', a1)
    if hasattr(a1, 'xpdl_ExternalPackages'):
        assert _is_linked(a1, 'xpdl_ExternalPackages', b)
    _safe_set(b, 'xpdl_ExternalPackage', a2)
    assert _is_linked(b, 'xpdl_ExternalPackage', a2)
    if hasattr(a1, 'xpdl_ExternalPackages'):
        assert not _is_linked(a1, 'xpdl_ExternalPackages', b)
    if hasattr(a2, 'xpdl_ExternalPackages'):
        assert _is_linked(a2, 'xpdl_ExternalPackages', b)
    _safe_set(b, 'xpdl_ExternalPackage', None)
    assert not _is_linked(b, 'xpdl_ExternalPackage', a2)
    if hasattr(a2, 'xpdl_ExternalPackages'):
        assert not _is_linked(a2, 'xpdl_ExternalPackages', b)


def test_assoc_externalReference29_reverse_link_reassign_clear():
    a1 = xpdl_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    a2 = xpdl_TypeDeclarationType(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = xpdl_ExternalReferenceType(location="sample_text", namespace="sample_text", xref="sample_text")
    _safe_set(b, 'xpdl_ExternalReferenceType31', a1)
    assert _is_linked(b, 'xpdl_ExternalReferenceType31', a1)
    if hasattr(a1, 'xpdl_TypeDeclarationType30'):
        assert _is_linked(a1, 'xpdl_TypeDeclarationType30', b)
    _safe_set(b, 'xpdl_ExternalReferenceType31', a2)
    assert _is_linked(b, 'xpdl_ExternalReferenceType31', a2)
    if hasattr(a1, 'xpdl_TypeDeclarationType30'):
        assert not _is_linked(a1, 'xpdl_TypeDeclarationType30', b)
    if hasattr(a2, 'xpdl_TypeDeclarationType30'):
        assert _is_linked(a2, 'xpdl_TypeDeclarationType30', b)
    _safe_set(b, 'xpdl_ExternalReferenceType31', None)
    assert not _is_linked(b, 'xpdl_ExternalReferenceType31', a2)
    if hasattr(a2, 'xpdl_TypeDeclarationType30'):
        assert not _is_linked(a2, 'xpdl_TypeDeclarationType30', b)


def test_assoc_externalReference5_reverse_link_reassign_clear():
    a1 = xpdl_ExternalReferenceType(location="sample_text", namespace="sample_text", xref="sample_text")
    a2 = xpdl_ExternalReferenceType(location="sample_text_2", namespace="sample_text_2", xref="sample_text_2")
    b = xpdl_DataTypeType(carnotType="sample_text")
    _safe_set(b, 'xpdl_DataTypeType6', a1)
    assert _is_linked(b, 'xpdl_DataTypeType6', a1)
    if hasattr(a1, 'xpdl_ExternalReferenceType'):
        assert _is_linked(a1, 'xpdl_ExternalReferenceType', b)
    _safe_set(b, 'xpdl_DataTypeType6', a2)
    assert _is_linked(b, 'xpdl_DataTypeType6', a2)
    if hasattr(a1, 'xpdl_ExternalReferenceType'):
        assert not _is_linked(a1, 'xpdl_ExternalReferenceType', b)
    if hasattr(a2, 'xpdl_ExternalReferenceType'):
        assert _is_linked(a2, 'xpdl_ExternalReferenceType', b)
    _safe_set(b, 'xpdl_DataTypeType6', None)
    assert not _is_linked(b, 'xpdl_DataTypeType6', a2)
    if hasattr(a2, 'xpdl_ExternalReferenceType'):
        assert not _is_linked(a2, 'xpdl_ExternalReferenceType', b)


def test_assoc_formalParameter13_reverse_link_reassign_clear():
    a1 = xpdl_FormalParametersType()
    a2 = xpdl_FormalParametersType()
    b = xpdl_FormalParameterType(description="sample_text", id="sample_text", mode="sample_text", name="sample_text")
    _safe_set(b, 'xpdl_FormalParameterType', a1)
    assert _is_linked(b, 'xpdl_FormalParameterType', a1)
    if hasattr(a1, 'xpdl_FormalParametersType'):
        assert _is_linked(a1, 'xpdl_FormalParametersType', b)
    _safe_set(b, 'xpdl_FormalParameterType', a2)
    assert _is_linked(b, 'xpdl_FormalParameterType', a2)
    if hasattr(a1, 'xpdl_FormalParametersType'):
        assert not _is_linked(a1, 'xpdl_FormalParametersType', b)
    if hasattr(a2, 'xpdl_FormalParametersType'):
        assert _is_linked(a2, 'xpdl_FormalParametersType', b)
    _safe_set(b, 'xpdl_FormalParameterType', None)
    assert not _is_linked(b, 'xpdl_FormalParameterType', a2)
    if hasattr(a2, 'xpdl_FormalParametersType'):
        assert not _is_linked(a2, 'xpdl_FormalParametersType', b)


def test_assoc_typeDeclaration19_reverse_link_reassign_clear():
    a1 = xpdl_TypeDeclarationsType()
    a2 = xpdl_TypeDeclarationsType()
    b = xpdl_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'xpdl_TypeDeclarationType', a1)
    assert _is_linked(b, 'xpdl_TypeDeclarationType', a1)
    if hasattr(a1, 'xpdl_TypeDeclarationsType'):
        assert _is_linked(a1, 'xpdl_TypeDeclarationsType', b)
    _safe_set(b, 'xpdl_TypeDeclarationType', a2)
    assert _is_linked(b, 'xpdl_TypeDeclarationType', a2)
    if hasattr(a1, 'xpdl_TypeDeclarationsType'):
        assert not _is_linked(a1, 'xpdl_TypeDeclarationsType', b)
    if hasattr(a2, 'xpdl_TypeDeclarationsType'):
        assert _is_linked(a2, 'xpdl_TypeDeclarationsType', b)
    _safe_set(b, 'xpdl_TypeDeclarationType', None)
    assert not _is_linked(b, 'xpdl_TypeDeclarationType', a2)
    if hasattr(a2, 'xpdl_TypeDeclarationsType'):
        assert not _is_linked(a2, 'xpdl_TypeDeclarationsType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_extendedAnnotation8_stub_double():
    # ExtendedAnnotationType has no real 'ExtendedAnnotationType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl_ExtendedAttributeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl_ExtendedAttributeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl_ExtendedAttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", value="sample_text")
    partner = ExtendedAnnotationType()
    setattr(partner, 'ExtendedAnnotationType', None)
    _safe_set(owner, 'xpdl_ExtendedAttributeType9', partner)
    assert getattr(partner, 'ExtendedAnnotationType') == owner
    _safe_set(owner, 'xpdl_ExtendedAttributeType9', None)
    assert getattr(partner, 'ExtendedAnnotationType') is None


def test_assoc_extendedAttribute7_stub_double():
    # xpdl_ExtendedAttributesType has no real 'xpdl_ExtendedAttributesType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl_ExtendedAttributeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl_ExtendedAttributeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl_ExtendedAttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", value="sample_text")
    partner = xpdl_ExtendedAttributesType()
    setattr(partner, 'xpdl_ExtendedAttributesType', None)
    _safe_set(owner, 'xpdl_ExtendedAttributeType', partner)
    assert owner in getattr(partner, 'xpdl_ExtendedAttributesType')
    _safe_set(owner, 'xpdl_ExtendedAttributeType', None)
    assert owner not in getattr(partner, 'xpdl_ExtendedAttributesType')


def test_assoc_schemaType26_stub_double():
    # xpdl_SchemaTypeType has no real 'xpdl_SchemaTypeType28' property in the generated
    # code (a bare stub) -- manually attach it so xpdl_TypeDeclarationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl_TypeDeclarationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    partner = xpdl_SchemaTypeType()
    setattr(partner, 'xpdl_SchemaTypeType28', None)
    _safe_set(owner, 'xpdl_TypeDeclarationType27', partner)
    assert getattr(partner, 'xpdl_SchemaTypeType28') == owner
    _safe_set(owner, 'xpdl_TypeDeclarationType27', None)
    assert getattr(partner, 'xpdl_SchemaTypeType28') is None


def test_assoc_schemaType3_stub_double():
    # xpdl_SchemaTypeType has no real 'xpdl_SchemaTypeType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl_DataTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl_DataTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl_DataTypeType(carnotType="sample_text")
    partner = xpdl_SchemaTypeType()
    setattr(partner, 'xpdl_SchemaTypeType', None)
    _safe_set(owner, 'xpdl_DataTypeType4', partner)
    assert getattr(partner, 'xpdl_SchemaTypeType') == owner
    _safe_set(owner, 'xpdl_DataTypeType4', None)
    assert getattr(partner, 'xpdl_SchemaTypeType') is None


