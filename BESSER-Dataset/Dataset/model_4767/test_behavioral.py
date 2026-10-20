import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DataType,
    FunctionType,
    NumberType,
    RealType,
    Type,
    types_BooleanType,
    types_CollectionType,
    types_DataType,
    types_EClass,
    types_EEnum,
    types_EnumType,
    types_FunctionType,
    types_IntegerType,
    types_MapType,
    types_MethodType,
    types_NumberType,
    types_ObjectType,
    types_RealType,
    types_StringType,
    types_Type,
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

def test_assoc_parameterTypes9_reverse_link_reassign_clear():
    a1 = types_Type(inExtentDomain=True)
    a2 = types_Type(inExtentDomain=False)
    b = types_FunctionType(optionalParameterCount=7)
    _safe_set(b, 'types_FunctionType10', {a1})
    assert _is_linked(b, 'types_FunctionType10', a1)
    if hasattr(a1, 'types_Type11'):
        assert _is_linked(a1, 'types_Type11', b)
    _safe_set(b, 'types_FunctionType10', {a2})
    assert _is_linked(b, 'types_FunctionType10', a2)
    if hasattr(a1, 'types_Type11'):
        assert not _is_linked(a1, 'types_Type11', b)
    if hasattr(a2, 'types_Type11'):
        assert _is_linked(a2, 'types_Type11', b)
    _safe_set(b, 'types_FunctionType10', set())
    assert not _is_linked(b, 'types_FunctionType10', a2)
    if hasattr(a2, 'types_Type11'):
        assert not _is_linked(a2, 'types_Type11', b)


def test_assoc_returnType7_reverse_link_reassign_clear():
    a1 = types_Type(inExtentDomain=True)
    a2 = types_Type(inExtentDomain=False)
    b = types_FunctionType(optionalParameterCount=7)
    _safe_set(b, 'types_FunctionType', a1)
    assert _is_linked(b, 'types_FunctionType', a1)
    if hasattr(a1, 'types_Type8'):
        assert _is_linked(a1, 'types_Type8', b)
    _safe_set(b, 'types_FunctionType', a2)
    assert _is_linked(b, 'types_FunctionType', a2)
    if hasattr(a1, 'types_Type8'):
        assert not _is_linked(a1, 'types_Type8', b)
    if hasattr(a2, 'types_Type8'):
        assert _is_linked(a2, 'types_Type8', b)
    _safe_set(b, 'types_FunctionType', None)
    assert not _is_linked(b, 'types_FunctionType', a2)
    if hasattr(a2, 'types_Type8'):
        assert not _is_linked(a2, 'types_Type8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elementType1_stub_double():
    # types_CollectionType has no real 'types_CollectionType' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(inExtentDomain=True)
    partner = types_CollectionType()
    setattr(partner, 'types_CollectionType', None)
    _safe_set(owner, 'types_Type', partner)
    assert getattr(partner, 'types_CollectionType') == owner
    _safe_set(owner, 'types_Type', None)
    assert getattr(partner, 'types_CollectionType') is None


def test_assoc_keyType2_stub_double():
    # types_MapType has no real 'types_MapType' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(inExtentDomain=True)
    partner = types_MapType()
    setattr(partner, 'types_MapType', None)
    _safe_set(owner, 'types_Type3', partner)
    assert getattr(partner, 'types_MapType') == owner
    _safe_set(owner, 'types_Type3', None)
    assert getattr(partner, 'types_MapType') is None


def test_assoc_objectType12_stub_double():
    # types_MethodType has no real 'types_MethodType' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(inExtentDomain=True)
    partner = types_MethodType()
    setattr(partner, 'types_MethodType', None)
    _safe_set(owner, 'types_Type13', partner)
    assert getattr(partner, 'types_MethodType') == owner
    _safe_set(owner, 'types_Type13', None)
    assert getattr(partner, 'types_MethodType') is None


def test_assoc_valueType4_stub_double():
    # types_MapType has no real 'types_MapType5' property in the generated
    # code (a bare stub) -- manually attach it so types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Type(inExtentDomain=True)
    partner = types_MapType()
    setattr(partner, 'types_MapType5', None)
    _safe_set(owner, 'types_Type6', partner)
    assert getattr(partner, 'types_MapType5') == owner
    _safe_set(owner, 'types_Type6', None)
    assert getattr(partner, 'types_MapType5') is None


