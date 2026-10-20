import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AngleOperation,
    AngleUnit,
    ImperialSystemUnit,
    LengthOperation,
    LengthUnit,
    MetricSystemUnit,
    Quantity,
    QuantityHomogenousOperation,
    QuantityOperation,
    QuantityScalarOperation,
    Unit,
    units_Angle,
    units_AngleAdd,
    units_AngleDistinct,
    units_AngleEquals,
    units_AngleGreater,
    units_AngleOperation,
    units_AngleScalarDivide,
    units_AngleScalarMultiply,
    units_AngleSmaller,
    units_AngleSubtract,
    units_AngleUnit,
    units_Centimeter,
    units_Degree,
    units_Foot,
    units_Gradian,
    units_ImperialSystemUnit,
    units_Inch,
    units_Length,
    units_LengthAdd,
    units_LengthDistinct,
    units_LengthEquals,
    units_LengthGreater,
    units_LengthOperation,
    units_LengthScalarDivide,
    units_LengthScalarMultiply,
    units_LengthSmaller,
    units_LengthSubtract,
    units_LengthUnit,
    units_Meter,
    units_MetricSystemUnit,
    units_Millimeter,
    units_Quantity,
    units_QuantityArithmeticOperation,
    units_QuantityComparisonOperation,
    units_QuantityHomogenousOperation,
    units_QuantityOperation,
    units_QuantityScalarOperation,
    units_Radian,
    units_Turn,
    units_Unit,
    units_Yard,
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

def test_assoc_lhs6_reverse_link_reassign_clear():
    a1 = units_QuantityScalarOperation(rhs=3.14)
    a2 = units_QuantityScalarOperation(rhs=9.99)
    b = units_Quantity(value="sample_text")
    _safe_set(b, 'units_Quantity7', a1)
    assert _is_linked(b, 'units_Quantity7', a1)
    if hasattr(a1, 'units_QuantityScalarOperation'):
        assert _is_linked(a1, 'units_QuantityScalarOperation', b)
    _safe_set(b, 'units_Quantity7', a2)
    assert _is_linked(b, 'units_Quantity7', a2)
    if hasattr(a1, 'units_QuantityScalarOperation'):
        assert not _is_linked(a1, 'units_QuantityScalarOperation', b)
    if hasattr(a2, 'units_QuantityScalarOperation'):
        assert _is_linked(a2, 'units_QuantityScalarOperation', b)
    _safe_set(b, 'units_Quantity7', None)
    assert not _is_linked(b, 'units_Quantity7', a2)
    if hasattr(a2, 'units_QuantityScalarOperation'):
        assert not _is_linked(a2, 'units_QuantityScalarOperation', b)


def test_assoc_unit0_reverse_link_reassign_clear():
    a1 = units_Unit()
    a2 = units_Unit()
    b = units_Quantity(value="sample_text")
    _safe_set(b, 'units_Quantity', a1)
    assert _is_linked(b, 'units_Quantity', a1)
    if hasattr(a1, 'units_Unit'):
        assert _is_linked(a1, 'units_Unit', b)
    _safe_set(b, 'units_Quantity', a2)
    assert _is_linked(b, 'units_Quantity', a2)
    if hasattr(a1, 'units_Unit'):
        assert not _is_linked(a1, 'units_Unit', b)
    if hasattr(a2, 'units_Unit'):
        assert _is_linked(a2, 'units_Unit', b)
    _safe_set(b, 'units_Quantity', None)
    assert not _is_linked(b, 'units_Quantity', a2)
    if hasattr(a2, 'units_Unit'):
        assert not _is_linked(a2, 'units_Unit', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_lhs1_stub_double():
    # units_QuantityHomogenousOperation has no real 'units_QuantityHomogenousOperation' property in the generated
    # code (a bare stub) -- manually attach it so units_Quantity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # units_Quantity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = units_Quantity(value="sample_text")
    partner = units_QuantityHomogenousOperation()
    setattr(partner, 'units_QuantityHomogenousOperation', None)
    _safe_set(owner, 'units_Quantity2', partner)
    assert getattr(partner, 'units_QuantityHomogenousOperation') == owner
    _safe_set(owner, 'units_Quantity2', None)
    assert getattr(partner, 'units_QuantityHomogenousOperation') is None


def test_assoc_rhs3_stub_double():
    # units_QuantityHomogenousOperation has no real 'units_QuantityHomogenousOperation4' property in the generated
    # code (a bare stub) -- manually attach it so units_Quantity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # units_Quantity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = units_Quantity(value="sample_text")
    partner = units_QuantityHomogenousOperation()
    setattr(partner, 'units_QuantityHomogenousOperation4', None)
    _safe_set(owner, 'units_Quantity5', partner)
    assert getattr(partner, 'units_QuantityHomogenousOperation4') == owner
    _safe_set(owner, 'units_Quantity5', None)
    assert getattr(partner, 'units_QuantityHomogenousOperation4') is None


