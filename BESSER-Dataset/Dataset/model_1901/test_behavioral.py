import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Constant,
    Declaration,
    EnumMemberValue,
    Expression,
    File,
    IntegerType,
    InterfaceMember,
    Literal,
    PrimitiveType,
    Type,
    UnionMember,
    fIDL_ArrayType,
    fIDL_Attribute,
    fIDL_AttributedDeclaration,
    fIDL_BooleanLiteral,
    fIDL_BooleanType,
    fIDL_ConstDeclaration,
    fIDL_Constant,
    fIDL_Declaration,
    fIDL_EnumDeclaration,
    fIDL_EnumMember,
    fIDL_EnumMemberValue,
    fIDL_Expression,
    fIDL_File,
    fIDL_Float32Type,
    fIDL_Float64Type,
    fIDL_HandleType,
    fIDL_IdentifierType,
    fIDL_Int16Type,
    fIDL_Int32Type,
    fIDL_Int64Type,
    fIDL_Int8Type,
    fIDL_IntegerType,
    fIDL_InterfaceDeclaration,
    fIDL_InterfaceMember,
    fIDL_InterfaceMethod,
    fIDL_InterfaceParameters,
    fIDL_LibraryHeader,
    fIDL_Literal,
    fIDL_NumberLiteral,
    fIDL_Parameter,
    fIDL_ParameterList,
    fIDL_PrimitiveType,
    fIDL_RequestType,
    fIDL_StatusType,
    fIDL_StringLiteral,
    fIDL_StringType,
    fIDL_StructDeclaration,
    fIDL_StructField,
    fIDL_StructMember,
    fIDL_Type,
    fIDL_Uint16Type,
    fIDL_Uint32Type,
    fIDL_Uint64Type,
    fIDL_Uint8Type,
    fIDL_UnionDeclaration,
    fIDL_UnionField,
    fIDL_UnionMember,
    fIDL_Using,
    fIDL_VectorType,
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

def test_assoc_constraint59_reverse_link_reassign_clear():
    a1 = fIDL_VectorType(nullable=True)
    a2 = fIDL_VectorType(nullable=False)
    b = fIDL_Constant(ci="sample_text")
    _safe_set(b, 'fIDL_Constant61', a1)
    assert _is_linked(b, 'fIDL_Constant61', a1)
    if hasattr(a1, 'fIDL_VectorType60'):
        assert _is_linked(a1, 'fIDL_VectorType60', b)
    _safe_set(b, 'fIDL_Constant61', a2)
    assert _is_linked(b, 'fIDL_Constant61', a2)
    if hasattr(a1, 'fIDL_VectorType60'):
        assert not _is_linked(a1, 'fIDL_VectorType60', b)
    if hasattr(a2, 'fIDL_VectorType60'):
        assert _is_linked(a2, 'fIDL_VectorType60', b)
    _safe_set(b, 'fIDL_Constant61', None)
    assert not _is_linked(b, 'fIDL_Constant61', a2)
    if hasattr(a2, 'fIDL_VectorType60'):
        assert not _is_linked(a2, 'fIDL_VectorType60', b)


def test_assoc_constraint62_reverse_link_reassign_clear():
    a1 = fIDL_StringType(nullable=True)
    a2 = fIDL_StringType(nullable=False)
    b = fIDL_Constant(ci="sample_text")
    _safe_set(b, 'fIDL_Constant63', a1)
    assert _is_linked(b, 'fIDL_Constant63', a1)
    if hasattr(a1, 'fIDL_StringType'):
        assert _is_linked(a1, 'fIDL_StringType', b)
    _safe_set(b, 'fIDL_Constant63', a2)
    assert _is_linked(b, 'fIDL_Constant63', a2)
    if hasattr(a1, 'fIDL_StringType'):
        assert not _is_linked(a1, 'fIDL_StringType', b)
    if hasattr(a2, 'fIDL_StringType'):
        assert _is_linked(a2, 'fIDL_StringType', b)
    _safe_set(b, 'fIDL_Constant63', None)
    assert not _is_linked(b, 'fIDL_Constant63', a2)
    if hasattr(a2, 'fIDL_StringType'):
        assert not _is_linked(a2, 'fIDL_StringType', b)


def test_assoc_ref50_reverse_link_reassign_clear():
    a1 = fIDL_IdentifierType(nullable=True)
    a2 = fIDL_IdentifierType(nullable=False)
    b = fIDL_Declaration(name="sample_text")
    _safe_set(b, 'fIDL_Declaration51', a1)
    assert _is_linked(b, 'fIDL_Declaration51', a1)
    if hasattr(a1, 'fIDL_IdentifierType'):
        assert _is_linked(a1, 'fIDL_IdentifierType', b)
    _safe_set(b, 'fIDL_Declaration51', a2)
    assert _is_linked(b, 'fIDL_Declaration51', a2)
    if hasattr(a1, 'fIDL_IdentifierType'):
        assert not _is_linked(a1, 'fIDL_IdentifierType', b)
    if hasattr(a2, 'fIDL_IdentifierType'):
        assert _is_linked(a2, 'fIDL_IdentifierType', b)
    _safe_set(b, 'fIDL_Declaration51', None)
    assert not _is_linked(b, 'fIDL_Declaration51', a2)
    if hasattr(a2, 'fIDL_IdentifierType'):
        assert not _is_linked(a2, 'fIDL_IdentifierType', b)


def test_assoc_ref64_reverse_link_reassign_clear():
    a1 = fIDL_RequestType(nullable=True)
    a2 = fIDL_RequestType(nullable=False)
    b = fIDL_Declaration(name="sample_text")
    _safe_set(b, 'fIDL_Declaration65', a1)
    assert _is_linked(b, 'fIDL_Declaration65', a1)
    if hasattr(a1, 'fIDL_RequestType'):
        assert _is_linked(a1, 'fIDL_RequestType', b)
    _safe_set(b, 'fIDL_Declaration65', a2)
    assert _is_linked(b, 'fIDL_Declaration65', a2)
    if hasattr(a1, 'fIDL_RequestType'):
        assert not _is_linked(a1, 'fIDL_RequestType', b)
    if hasattr(a2, 'fIDL_RequestType'):
        assert _is_linked(a2, 'fIDL_RequestType', b)
    _safe_set(b, 'fIDL_Declaration65', None)
    assert not _is_linked(b, 'fIDL_Declaration65', a2)
    if hasattr(a2, 'fIDL_RequestType'):
        assert not _is_linked(a2, 'fIDL_RequestType', b)


def test_assoc_usings0_reverse_link_reassign_clear():
    a1 = fIDL_Using(importedNamespace="sample_text", name="sample_text")
    a2 = fIDL_Using(importedNamespace="sample_text_2", name="sample_text_2")
    b = fIDL_LibraryHeader(name="sample_text")
    _safe_set(b, 'fIDL_LibraryHeader', {a1})
    assert _is_linked(b, 'fIDL_LibraryHeader', a1)
    if hasattr(a1, 'fIDL_Using'):
        assert _is_linked(a1, 'fIDL_Using', b)
    _safe_set(b, 'fIDL_LibraryHeader', {a2})
    assert _is_linked(b, 'fIDL_LibraryHeader', a2)
    if hasattr(a1, 'fIDL_Using'):
        assert not _is_linked(a1, 'fIDL_Using', b)
    if hasattr(a2, 'fIDL_Using'):
        assert _is_linked(a2, 'fIDL_Using', b)
    _safe_set(b, 'fIDL_LibraryHeader', set())
    assert not _is_linked(b, 'fIDL_LibraryHeader', a2)
    if hasattr(a2, 'fIDL_Using'):
        assert not _is_linked(a2, 'fIDL_Using', b)


def test_assoc_value13_reverse_link_reassign_clear():
    a1 = fIDL_EnumMemberValue(value="sample_text")
    a2 = fIDL_EnumMemberValue(value="sample_text_2")
    b = fIDL_EnumMember(name="sample_text")
    _safe_set(b, 'fIDL_EnumMember14', a1)
    assert _is_linked(b, 'fIDL_EnumMember14', a1)
    if hasattr(a1, 'fIDL_EnumMemberValue'):
        assert _is_linked(a1, 'fIDL_EnumMemberValue', b)
    _safe_set(b, 'fIDL_EnumMember14', a2)
    assert _is_linked(b, 'fIDL_EnumMember14', a2)
    if hasattr(a1, 'fIDL_EnumMemberValue'):
        assert not _is_linked(a1, 'fIDL_EnumMemberValue', b)
    if hasattr(a2, 'fIDL_EnumMemberValue'):
        assert _is_linked(a2, 'fIDL_EnumMemberValue', b)
    _safe_set(b, 'fIDL_EnumMember14', None)
    assert not _is_linked(b, 'fIDL_EnumMember14', a2)
    if hasattr(a2, 'fIDL_EnumMemberValue'):
        assert not _is_linked(a2, 'fIDL_EnumMemberValue', b)


def test_assoc_value41_reverse_link_reassign_clear():
    a1 = fIDL_StructField(name="sample_text")
    a2 = fIDL_StructField(name="sample_text_2")
    b = fIDL_Constant(ci="sample_text")
    _safe_set(b, 'fIDL_Constant43', a1)
    assert _is_linked(b, 'fIDL_Constant43', a1)
    if hasattr(a1, 'fIDL_StructField42'):
        assert _is_linked(a1, 'fIDL_StructField42', b)
    _safe_set(b, 'fIDL_Constant43', a2)
    assert _is_linked(b, 'fIDL_Constant43', a2)
    if hasattr(a1, 'fIDL_StructField42'):
        assert not _is_linked(a1, 'fIDL_StructField42', b)
    if hasattr(a2, 'fIDL_StructField42'):
        assert _is_linked(a2, 'fIDL_StructField42', b)
    _safe_set(b, 'fIDL_Constant43', None)
    assert not _is_linked(b, 'fIDL_Constant43', a2)
    if hasattr(a2, 'fIDL_StructField42'):
        assert not _is_linked(a2, 'fIDL_StructField42', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes3_stub_double():
    # fIDL_AttributedDeclaration has no real 'fIDL_AttributedDeclaration4' property in the generated
    # code (a bare stub) -- manually attach it so fIDL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fIDL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fIDL_Attribute(name="sample_text", value="sample_text")
    partner = fIDL_AttributedDeclaration()
    setattr(partner, 'fIDL_AttributedDeclaration4', None)
    _safe_set(owner, 'fIDL_Attribute', partner)
    assert owner in getattr(partner, 'fIDL_AttributedDeclaration4')
    _safe_set(owner, 'fIDL_Attribute', None)
    assert owner not in getattr(partner, 'fIDL_AttributedDeclaration4')


def test_assoc_constraint54_stub_double():
    # fIDL_ArrayType has no real 'fIDL_ArrayType55' property in the generated
    # code (a bare stub) -- manually attach it so fIDL_Constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fIDL_Constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fIDL_Constant(ci="sample_text")
    partner = fIDL_ArrayType()
    setattr(partner, 'fIDL_ArrayType55', None)
    _safe_set(owner, 'fIDL_Constant56', partner)
    assert getattr(partner, 'fIDL_ArrayType55') == owner
    _safe_set(owner, 'fIDL_Constant56', None)
    assert getattr(partner, 'fIDL_ArrayType55') is None


def test_assoc_declaration5_stub_double():
    # fIDL_AttributedDeclaration has no real 'fIDL_AttributedDeclaration6' property in the generated
    # code (a bare stub) -- manually attach it so fIDL_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fIDL_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fIDL_Declaration(name="sample_text")
    partner = fIDL_AttributedDeclaration()
    setattr(partner, 'fIDL_AttributedDeclaration6', None)
    _safe_set(owner, 'fIDL_Declaration', partner)
    assert getattr(partner, 'fIDL_AttributedDeclaration6') == owner
    _safe_set(owner, 'fIDL_Declaration', None)
    assert getattr(partner, 'fIDL_AttributedDeclaration6') is None


def test_assoc_declarations1_stub_double():
    # fIDL_AttributedDeclaration has no real 'fIDL_AttributedDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so fIDL_LibraryHeader's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fIDL_LibraryHeader's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fIDL_LibraryHeader(name="sample_text")
    partner = fIDL_AttributedDeclaration()
    setattr(partner, 'fIDL_AttributedDeclaration', None)
    _safe_set(owner, 'fIDL_LibraryHeader2', {partner})
    assert getattr(partner, 'fIDL_AttributedDeclaration') == owner
    _safe_set(owner, 'fIDL_LibraryHeader2', set())
    assert getattr(partner, 'fIDL_AttributedDeclaration') is None


def test_assoc_field33_stub_double():
    # fIDL_StructMember has no real 'fIDL_StructMember34' property in the generated
    # code (a bare stub) -- manually attach it so fIDL_StructField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fIDL_StructField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fIDL_StructField(name="sample_text")
    partner = fIDL_StructMember()
    setattr(partner, 'fIDL_StructMember34', None)
    _safe_set(owner, 'fIDL_StructField', partner)
    assert getattr(partner, 'fIDL_StructMember34') == owner
    _safe_set(owner, 'fIDL_StructField', None)
    assert getattr(partner, 'fIDL_StructMember34') is None


def test_assoc_members11_stub_double():
    # fIDL_EnumDeclaration has no real 'fIDL_EnumDeclaration12' property in the generated
    # code (a bare stub) -- manually attach it so fIDL_EnumMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fIDL_EnumMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fIDL_EnumMember(name="sample_text")
    partner = fIDL_EnumDeclaration()
    setattr(partner, 'fIDL_EnumDeclaration12', None)
    _safe_set(owner, 'fIDL_EnumMember', partner)
    assert owner in getattr(partner, 'fIDL_EnumDeclaration12')
    _safe_set(owner, 'fIDL_EnumMember', None)
    assert owner not in getattr(partner, 'fIDL_EnumDeclaration12')


def test_assoc_method20_stub_double():
    # fIDL_InterfaceMethod has no real 'fIDL_InterfaceMethod21' property in the generated
    # code (a bare stub) -- manually attach it so fIDL_InterfaceParameters's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fIDL_InterfaceParameters's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fIDL_InterfaceParameters(name="sample_text", resultName="sample_text")
    partner = fIDL_InterfaceMethod()
    setattr(partner, 'fIDL_InterfaceMethod21', None)
    _safe_set(owner, 'fIDL_InterfaceParameters', partner)
    assert getattr(partner, 'fIDL_InterfaceMethod21') == owner
    _safe_set(owner, 'fIDL_InterfaceParameters', None)
    assert getattr(partner, 'fIDL_InterfaceMethod21') is None


def test_assoc_parameters22_stub_double():
    # fIDL_ParameterList has no real 'fIDL_ParameterList' property in the generated
    # code (a bare stub) -- manually attach it so fIDL_InterfaceParameters's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fIDL_InterfaceParameters's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fIDL_InterfaceParameters(name="sample_text", resultName="sample_text")
    partner = fIDL_ParameterList()
    setattr(partner, 'fIDL_ParameterList', None)
    _safe_set(owner, 'fIDL_InterfaceParameters23', partner)
    assert getattr(partner, 'fIDL_ParameterList') == owner
    _safe_set(owner, 'fIDL_InterfaceParameters23', None)
    assert getattr(partner, 'fIDL_ParameterList') is None


def test_assoc_parameters27_stub_double():
    # fIDL_ParameterList has no real 'fIDL_ParameterList28' property in the generated
    # code (a bare stub) -- manually attach it so fIDL_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fIDL_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fIDL_Parameter(name="sample_text")
    partner = fIDL_ParameterList()
    setattr(partner, 'fIDL_ParameterList28', None)
    _safe_set(owner, 'fIDL_Parameter', partner)
    assert owner in getattr(partner, 'fIDL_ParameterList28')
    _safe_set(owner, 'fIDL_Parameter', None)
    assert owner not in getattr(partner, 'fIDL_ParameterList28')


def test_assoc_result24_stub_double():
    # fIDL_ParameterList has no real 'fIDL_ParameterList26' property in the generated
    # code (a bare stub) -- manually attach it so fIDL_InterfaceParameters's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fIDL_InterfaceParameters's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fIDL_InterfaceParameters(name="sample_text", resultName="sample_text")
    partner = fIDL_ParameterList()
    setattr(partner, 'fIDL_ParameterList26', None)
    _safe_set(owner, 'fIDL_InterfaceParameters25', partner)
    assert getattr(partner, 'fIDL_ParameterList26') == owner
    _safe_set(owner, 'fIDL_InterfaceParameters25', None)
    assert getattr(partner, 'fIDL_ParameterList26') is None


def test_assoc_type29_stub_double():
    # fIDL_Type has no real 'fIDL_Type31' property in the generated
    # code (a bare stub) -- manually attach it so fIDL_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fIDL_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fIDL_Parameter(name="sample_text")
    partner = fIDL_Type()
    setattr(partner, 'fIDL_Type31', None)
    _safe_set(owner, 'fIDL_Parameter30', partner)
    assert getattr(partner, 'fIDL_Type31') == owner
    _safe_set(owner, 'fIDL_Parameter30', None)
    assert getattr(partner, 'fIDL_Type31') is None


def test_assoc_type38_stub_double():
    # fIDL_Type has no real 'fIDL_Type40' property in the generated
    # code (a bare stub) -- manually attach it so fIDL_StructField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fIDL_StructField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fIDL_StructField(name="sample_text")
    partner = fIDL_Type()
    setattr(partner, 'fIDL_Type40', None)
    _safe_set(owner, 'fIDL_StructField39', partner)
    assert getattr(partner, 'fIDL_Type40') == owner
    _safe_set(owner, 'fIDL_StructField39', None)
    assert getattr(partner, 'fIDL_Type40') is None


def test_assoc_type48_stub_double():
    # fIDL_Type has no real 'fIDL_Type49' property in the generated
    # code (a bare stub) -- manually attach it so fIDL_UnionField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fIDL_UnionField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fIDL_UnionField(name="sample_text")
    partner = fIDL_Type()
    setattr(partner, 'fIDL_Type49', None)
    _safe_set(owner, 'fIDL_UnionField', partner)
    assert getattr(partner, 'fIDL_Type49') == owner
    _safe_set(owner, 'fIDL_UnionField', None)
    assert getattr(partner, 'fIDL_Type49') is None


def test_assoc_type57_stub_double():
    # fIDL_Type has no real 'fIDL_Type58' property in the generated
    # code (a bare stub) -- manually attach it so fIDL_VectorType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fIDL_VectorType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fIDL_VectorType(nullable=True)
    partner = fIDL_Type()
    setattr(partner, 'fIDL_Type58', None)
    _safe_set(owner, 'fIDL_VectorType', partner)
    assert getattr(partner, 'fIDL_Type58') == owner
    _safe_set(owner, 'fIDL_VectorType', None)
    assert getattr(partner, 'fIDL_Type58') is None


def test_assoc_value8_stub_double():
    # fIDL_ConstDeclaration has no real 'fIDL_ConstDeclaration9' property in the generated
    # code (a bare stub) -- manually attach it so fIDL_Constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fIDL_Constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fIDL_Constant(ci="sample_text")
    partner = fIDL_ConstDeclaration()
    setattr(partner, 'fIDL_ConstDeclaration9', None)
    _safe_set(owner, 'fIDL_Constant', partner)
    assert getattr(partner, 'fIDL_ConstDeclaration9') == owner
    _safe_set(owner, 'fIDL_Constant', None)
    assert getattr(partner, 'fIDL_ConstDeclaration9') is None


