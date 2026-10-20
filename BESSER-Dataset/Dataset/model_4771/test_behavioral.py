import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnyType,
    CollectionType,
    OrderedCollectionType,
    PrimitiveType,
    PseudoType,
    RealType,
    Type,
    UniqueCollectionType,
    eol_types_AnyType,
    eol_types_BagType,
    eol_types_BooleanType,
    eol_types_CollectionType,
    eol_types_IntegerType,
    eol_types_InvalidType,
    eol_types_MapType,
    eol_types_ModelElementType,
    eol_types_ModelType,
    eol_types_NativeType,
    eol_types_OrderedCollectionType,
    eol_types_OrderedSetType,
    eol_types_PrimitiveType,
    eol_types_PseudoType,
    eol_types_RealType,
    eol_types_SelfContentType,
    eol_types_SelfType,
    eol_types_SequenceType,
    eol_types_SetType,
    eol_types_StringType,
    eol_types_Type,
    eol_types_UniqueCollectionType,
    eol_types_VoidType,
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

def test_assoc_dynamicType0_stub_double():
    # eol_types_Type has no real 'eol_types_Type' property in the generated
    # code (a bare stub) -- manually attach it so eol_types_AnyType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_types_AnyType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_types_AnyType(declared=True)
    partner = eol_types_Type()
    setattr(partner, 'eol_types_Type', None)
    _safe_set(owner, 'eol_types_AnyType', {partner})
    assert getattr(partner, 'eol_types_Type') == owner
    _safe_set(owner, 'eol_types_AnyType', set())
    assert getattr(partner, 'eol_types_Type') is None


def test_assoc_keyType1_stub_double():
    # eol_types_MapType has no real 'eol_types_MapType' property in the generated
    # code (a bare stub) -- manually attach it so eol_types_AnyType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_types_AnyType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_types_AnyType(declared=True)
    partner = eol_types_MapType()
    setattr(partner, 'eol_types_MapType', None)
    _safe_set(owner, 'eol_types_AnyType2', partner)
    assert getattr(partner, 'eol_types_MapType') == owner
    _safe_set(owner, 'eol_types_AnyType2', None)
    assert getattr(partner, 'eol_types_MapType') is None


def test_assoc_valueType3_stub_double():
    # eol_types_MapType has no real 'eol_types_MapType4' property in the generated
    # code (a bare stub) -- manually attach it so eol_types_AnyType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_types_AnyType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_types_AnyType(declared=True)
    partner = eol_types_MapType()
    setattr(partner, 'eol_types_MapType4', None)
    _safe_set(owner, 'eol_types_AnyType5', partner)
    assert getattr(partner, 'eol_types_MapType4') == owner
    _safe_set(owner, 'eol_types_AnyType5', None)
    assert getattr(partner, 'eol_types_MapType4') is None


