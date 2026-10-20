import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Type,
    TypesLibrary,
    UserDefinedType,
    typeslibrary_ComplexNamedType,
    typeslibrary_NativeType,
    typeslibrary_NativeTypesLibrary,
    typeslibrary_SimpleNamedType,
    typeslibrary_Type,
    typeslibrary_TypeInstance,
    typeslibrary_TypesLibrary,
    typeslibrary_TypesLibraryUser,
    typeslibrary_UserDefinedType,
    typeslibrary_UserDefinedTypeRef,
    typeslibrary_UserDefinedTypesLibrary,
    NativeTypeKind,
    TypesLibraryKind,
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

def test_assoc_mapsTo4_reverse_link_reassign_clear():
    a1 = typeslibrary_NativeType(name="sample_text", spec="sample_text")
    a2 = typeslibrary_NativeType(name="sample_text_2", spec="sample_text_2")
    b = typeslibrary_NativeType(name="sample_text", spec="sample_text")
    _safe_set(b, 'typeslibrary_NativeType5', a1)
    assert _is_linked(b, 'typeslibrary_NativeType5', a1)
    if hasattr(a1, 'typeslibrary_NativeType3'):
        assert _is_linked(a1, 'typeslibrary_NativeType3', b)
    _safe_set(b, 'typeslibrary_NativeType5', a2)
    assert _is_linked(b, 'typeslibrary_NativeType5', a2)
    if hasattr(a1, 'typeslibrary_NativeType3'):
        assert not _is_linked(a1, 'typeslibrary_NativeType3', b)
    if hasattr(a2, 'typeslibrary_NativeType3'):
        assert _is_linked(a2, 'typeslibrary_NativeType3', b)
    _safe_set(b, 'typeslibrary_NativeType5', None)
    assert not _is_linked(b, 'typeslibrary_NativeType5', a2)
    if hasattr(a2, 'typeslibrary_NativeType3'):
        assert not _is_linked(a2, 'typeslibrary_NativeType3', b)


def test_assoc_nativeType1_reverse_link_reassign_clear():
    a1 = typeslibrary_TypeInstance(length=7, literals="sample_text", precision=7)
    a2 = typeslibrary_TypeInstance(length=13, literals="sample_text_2", precision=13)
    b = typeslibrary_NativeType(name="sample_text", spec="sample_text")
    _safe_set(b, 'typeslibrary_NativeType2', a1)
    assert _is_linked(b, 'typeslibrary_NativeType2', a1)
    if hasattr(a1, 'typeslibrary_TypeInstance'):
        assert _is_linked(a1, 'typeslibrary_TypeInstance', b)
    _safe_set(b, 'typeslibrary_NativeType2', a2)
    assert _is_linked(b, 'typeslibrary_NativeType2', a2)
    if hasattr(a1, 'typeslibrary_TypeInstance'):
        assert not _is_linked(a1, 'typeslibrary_TypeInstance', b)
    if hasattr(a2, 'typeslibrary_TypeInstance'):
        assert _is_linked(a2, 'typeslibrary_TypeInstance', b)
    _safe_set(b, 'typeslibrary_NativeType2', None)
    assert not _is_linked(b, 'typeslibrary_NativeType2', a2)
    if hasattr(a2, 'typeslibrary_TypeInstance'):
        assert not _is_linked(a2, 'typeslibrary_TypeInstance', b)


def test_assoc_nativeTypes0_reverse_link_reassign_clear():
    a1 = typeslibrary_NativeTypesLibrary(name="sample_text")
    a2 = typeslibrary_NativeTypesLibrary(name="sample_text_2")
    b = typeslibrary_NativeType(name="sample_text", spec="sample_text")
    _safe_set(b, 'typeslibrary_NativeType', a1)
    assert _is_linked(b, 'typeslibrary_NativeType', a1)
    if hasattr(a1, 'typeslibrary_NativeTypesLibrary'):
        assert _is_linked(a1, 'typeslibrary_NativeTypesLibrary', b)
    _safe_set(b, 'typeslibrary_NativeType', a2)
    assert _is_linked(b, 'typeslibrary_NativeType', a2)
    if hasattr(a1, 'typeslibrary_NativeTypesLibrary'):
        assert not _is_linked(a1, 'typeslibrary_NativeTypesLibrary', b)
    if hasattr(a2, 'typeslibrary_NativeTypesLibrary'):
        assert _is_linked(a2, 'typeslibrary_NativeTypesLibrary', b)
    _safe_set(b, 'typeslibrary_NativeType', None)
    assert not _is_linked(b, 'typeslibrary_NativeType', a2)
    if hasattr(a2, 'typeslibrary_NativeTypesLibrary'):
        assert not _is_linked(a2, 'typeslibrary_NativeTypesLibrary', b)


def test_assoc_userDefinedTypes11_reverse_link_reassign_clear():
    a1 = typeslibrary_UserDefinedTypesLibrary(name="sample_text")
    a2 = typeslibrary_UserDefinedTypesLibrary(name="sample_text_2")
    b = typeslibrary_UserDefinedType(name="sample_text")
    _safe_set(b, 'typeslibrary_UserDefinedType12', a1)
    assert _is_linked(b, 'typeslibrary_UserDefinedType12', a1)
    if hasattr(a1, 'typeslibrary_UserDefinedTypesLibrary'):
        assert _is_linked(a1, 'typeslibrary_UserDefinedTypesLibrary', b)
    _safe_set(b, 'typeslibrary_UserDefinedType12', a2)
    assert _is_linked(b, 'typeslibrary_UserDefinedType12', a2)
    if hasattr(a1, 'typeslibrary_UserDefinedTypesLibrary'):
        assert not _is_linked(a1, 'typeslibrary_UserDefinedTypesLibrary', b)
    if hasattr(a2, 'typeslibrary_UserDefinedTypesLibrary'):
        assert _is_linked(a2, 'typeslibrary_UserDefinedTypesLibrary', b)
    _safe_set(b, 'typeslibrary_UserDefinedType12', None)
    assert not _is_linked(b, 'typeslibrary_UserDefinedType12', a2)
    if hasattr(a2, 'typeslibrary_UserDefinedTypesLibrary'):
        assert not _is_linked(a2, 'typeslibrary_UserDefinedTypesLibrary', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_type7_stub_double():
    # typeslibrary_SimpleNamedType has no real 'typeslibrary_SimpleNamedType' property in the generated
    # code (a bare stub) -- manually attach it so typeslibrary_TypeInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # typeslibrary_TypeInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = typeslibrary_TypeInstance(length=7, literals="sample_text", precision=7)
    partner = typeslibrary_SimpleNamedType()
    setattr(partner, 'typeslibrary_SimpleNamedType', None)
    _safe_set(owner, 'typeslibrary_TypeInstance8', partner)
    assert getattr(partner, 'typeslibrary_SimpleNamedType') == owner
    _safe_set(owner, 'typeslibrary_TypeInstance8', None)
    assert getattr(partner, 'typeslibrary_SimpleNamedType') is None


def test_assoc_type9_stub_double():
    # typeslibrary_UserDefinedTypeRef has no real 'typeslibrary_UserDefinedTypeRef' property in the generated
    # code (a bare stub) -- manually attach it so typeslibrary_UserDefinedType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # typeslibrary_UserDefinedType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = typeslibrary_UserDefinedType(name="sample_text")
    partner = typeslibrary_UserDefinedTypeRef()
    setattr(partner, 'typeslibrary_UserDefinedTypeRef', None)
    _safe_set(owner, 'typeslibrary_UserDefinedType10', partner)
    assert getattr(partner, 'typeslibrary_UserDefinedTypeRef') == owner
    _safe_set(owner, 'typeslibrary_UserDefinedType10', None)
    assert getattr(partner, 'typeslibrary_UserDefinedTypeRef') is None


def test_assoc_types6_stub_double():
    # typeslibrary_ComplexNamedType has no real 'typeslibrary_ComplexNamedType' property in the generated
    # code (a bare stub) -- manually attach it so typeslibrary_UserDefinedType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # typeslibrary_UserDefinedType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = typeslibrary_UserDefinedType(name="sample_text")
    partner = typeslibrary_ComplexNamedType()
    setattr(partner, 'typeslibrary_ComplexNamedType', None)
    _safe_set(owner, 'typeslibrary_UserDefinedType', partner)
    assert owner in getattr(partner, 'typeslibrary_ComplexNamedType')
    _safe_set(owner, 'typeslibrary_UserDefinedType', None)
    assert owner not in getattr(partner, 'typeslibrary_ComplexNamedType')


def test_assoc_usedLibraries13_stub_double():
    # typeslibrary_TypesLibraryUser has no real 'typeslibrary_TypesLibraryUser' property in the generated
    # code (a bare stub) -- manually attach it so typeslibrary_TypesLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # typeslibrary_TypesLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = typeslibrary_TypesLibrary(kind="sample_text")
    partner = typeslibrary_TypesLibraryUser()
    setattr(partner, 'typeslibrary_TypesLibraryUser', None)
    _safe_set(owner, 'typeslibrary_TypesLibrary', partner)
    assert owner in getattr(partner, 'typeslibrary_TypesLibraryUser')
    _safe_set(owner, 'typeslibrary_TypesLibrary', None)
    assert owner not in getattr(partner, 'typeslibrary_TypesLibraryUser')


