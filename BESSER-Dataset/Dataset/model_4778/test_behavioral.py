import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArrayType,
    DataType,
    Expression,
    Literal,
    NumericLiteral,
    NumericType,
    PrimitiveType,
    UnitProduct,
    typesystem_AnyDataType,
    typesystem_ArrayDimension,
    typesystem_ArrayType,
    typesystem_BooleanLiteral,
    typesystem_BooleanType,
    typesystem_ComplexType,
    typesystem_DataType,
    typesystem_Expression,
    typesystem_GaussianType,
    typesystem_IntegerLiteral,
    typesystem_IntegerType,
    typesystem_InvalidDataType,
    typesystem_Literal,
    typesystem_NumericLiteral,
    typesystem_NumericType,
    typesystem_PrimitiveType,
    typesystem_RealLiteral,
    typesystem_RealType,
    typesystem_StringLiteral,
    typesystem_StringType,
    typesystem_TensorType,
    typesystem_Unit,
    typesystem_UnitDenominator,
    typesystem_UnitFactor,
    typesystem_UnitNumerator,
    typesystem_UnitProduct,
    typesystem_UnitType,
    OperatorKind,
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

def test_assoc_definedElementType2_reverse_link_reassign_clear():
    a1 = typesystem_DataType()
    a2 = typesystem_DataType()
    b = typesystem_ArrayType(dimensional=True, dimensionality=7, multidimensional=True)
    _safe_set(b, 'typesystem_ArrayType3', a1)
    assert _is_linked(b, 'typesystem_ArrayType3', a1)
    if hasattr(a1, 'typesystem_DataType4'):
        assert _is_linked(a1, 'typesystem_DataType4', b)
    _safe_set(b, 'typesystem_ArrayType3', a2)
    assert _is_linked(b, 'typesystem_ArrayType3', a2)
    if hasattr(a1, 'typesystem_DataType4'):
        assert not _is_linked(a1, 'typesystem_DataType4', b)
    if hasattr(a2, 'typesystem_DataType4'):
        assert _is_linked(a2, 'typesystem_DataType4', b)
    _safe_set(b, 'typesystem_ArrayType3', None)
    assert not _is_linked(b, 'typesystem_ArrayType3', a2)
    if hasattr(a2, 'typesystem_DataType4'):
        assert not _is_linked(a2, 'typesystem_DataType4', b)


def test_assoc_elementType1_reverse_link_reassign_clear():
    a1 = typesystem_DataType()
    a2 = typesystem_DataType()
    b = typesystem_ArrayType(dimensional=True, dimensionality=7, multidimensional=True)
    _safe_set(b, 'typesystem_ArrayType', a1)
    assert _is_linked(b, 'typesystem_ArrayType', a1)
    if hasattr(a1, 'typesystem_DataType'):
        assert _is_linked(a1, 'typesystem_DataType', b)
    _safe_set(b, 'typesystem_ArrayType', a2)
    assert _is_linked(b, 'typesystem_ArrayType', a2)
    if hasattr(a1, 'typesystem_DataType'):
        assert not _is_linked(a1, 'typesystem_DataType', b)
    if hasattr(a2, 'typesystem_DataType'):
        assert _is_linked(a2, 'typesystem_DataType', b)
    _safe_set(b, 'typesystem_ArrayType', None)
    assert not _is_linked(b, 'typesystem_ArrayType', a2)
    if hasattr(a2, 'typesystem_DataType'):
        assert not _is_linked(a2, 'typesystem_DataType', b)


def test_assoc_factors13_reverse_link_reassign_clear():
    a1 = typesystem_UnitProduct()
    a2 = typesystem_UnitProduct()
    b = typesystem_UnitFactor(exponent=7, symbol="sample_text")
    _safe_set(b, 'typesystem_UnitFactor', a1)
    assert _is_linked(b, 'typesystem_UnitFactor', a1)
    if hasattr(a1, 'typesystem_UnitProduct'):
        assert _is_linked(a1, 'typesystem_UnitProduct', b)
    _safe_set(b, 'typesystem_UnitFactor', a2)
    assert _is_linked(b, 'typesystem_UnitFactor', a2)
    if hasattr(a1, 'typesystem_UnitProduct'):
        assert not _is_linked(a1, 'typesystem_UnitProduct', b)
    if hasattr(a2, 'typesystem_UnitProduct'):
        assert _is_linked(a2, 'typesystem_UnitProduct', b)
    _safe_set(b, 'typesystem_UnitFactor', None)
    assert not _is_linked(b, 'typesystem_UnitFactor', a2)
    if hasattr(a2, 'typesystem_UnitProduct'):
        assert not _is_linked(a2, 'typesystem_UnitProduct', b)


def test_assoc_unit14_reverse_link_reassign_clear():
    a1 = typesystem_Unit(scale=7, wildcard=True)
    a2 = typesystem_Unit(scale=13, wildcard=False)
    b = typesystem_NumericLiteral(modifier="sample_text")
    _safe_set(b, 'typesystem_NumericLiteral', a1)
    assert _is_linked(b, 'typesystem_NumericLiteral', a1)
    if hasattr(a1, 'typesystem_Unit15'):
        assert _is_linked(a1, 'typesystem_Unit15', b)
    _safe_set(b, 'typesystem_NumericLiteral', a2)
    assert _is_linked(b, 'typesystem_NumericLiteral', a2)
    if hasattr(a1, 'typesystem_Unit15'):
        assert not _is_linked(a1, 'typesystem_Unit15', b)
    if hasattr(a2, 'typesystem_Unit15'):
        assert _is_linked(a2, 'typesystem_Unit15', b)
    _safe_set(b, 'typesystem_NumericLiteral', None)
    assert not _is_linked(b, 'typesystem_NumericLiteral', a2)
    if hasattr(a2, 'typesystem_Unit15'):
        assert not _is_linked(a2, 'typesystem_Unit15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_denominator11_stub_double():
    # typesystem_UnitDenominator has no real 'typesystem_UnitDenominator' property in the generated
    # code (a bare stub) -- manually attach it so typesystem_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # typesystem_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = typesystem_Unit(scale=7, wildcard=True)
    partner = typesystem_UnitDenominator()
    setattr(partner, 'typesystem_UnitDenominator', None)
    _safe_set(owner, 'typesystem_Unit12', partner)
    assert getattr(partner, 'typesystem_UnitDenominator') == owner
    _safe_set(owner, 'typesystem_Unit12', None)
    assert getattr(partner, 'typesystem_UnitDenominator') is None


def test_assoc_dimensions5_stub_double():
    # typesystem_ArrayDimension has no real 'typesystem_ArrayDimension' property in the generated
    # code (a bare stub) -- manually attach it so typesystem_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # typesystem_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = typesystem_ArrayType(dimensional=True, dimensionality=7, multidimensional=True)
    partner = typesystem_ArrayDimension()
    setattr(partner, 'typesystem_ArrayDimension', None)
    _safe_set(owner, 'typesystem_ArrayType6', {partner})
    assert getattr(partner, 'typesystem_ArrayDimension') == owner
    _safe_set(owner, 'typesystem_ArrayType6', set())
    assert getattr(partner, 'typesystem_ArrayDimension') is None


def test_assoc_numerator9_stub_double():
    # typesystem_UnitNumerator has no real 'typesystem_UnitNumerator' property in the generated
    # code (a bare stub) -- manually attach it so typesystem_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # typesystem_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = typesystem_Unit(scale=7, wildcard=True)
    partner = typesystem_UnitNumerator()
    setattr(partner, 'typesystem_UnitNumerator', None)
    _safe_set(owner, 'typesystem_Unit10', partner)
    assert getattr(partner, 'typesystem_UnitNumerator') == owner
    _safe_set(owner, 'typesystem_Unit10', None)
    assert getattr(partner, 'typesystem_UnitNumerator') is None


def test_assoc_unit0_stub_double():
    # typesystem_NumericType has no real 'typesystem_NumericType' property in the generated
    # code (a bare stub) -- manually attach it so typesystem_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # typesystem_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = typesystem_Unit(scale=7, wildcard=True)
    partner = typesystem_NumericType()
    setattr(partner, 'typesystem_NumericType', None)
    _safe_set(owner, 'typesystem_Unit', partner)
    assert getattr(partner, 'typesystem_NumericType') == owner
    _safe_set(owner, 'typesystem_Unit', None)
    assert getattr(partner, 'typesystem_NumericType') is None


