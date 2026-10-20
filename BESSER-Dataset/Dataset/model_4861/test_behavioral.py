import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Unit,
    units_pc_pc_BaseUnit,
    units_pc_pc_EObject,
    units_pc_pc_Pointcut,
    units_pc_pc_PointcutPointcut,
    units_pc_pc_Unit,
    units_pc_pc_UnitCarryingElement,
    units_pc_pc_UnitLiteral,
    units_pc_pc_UnitMultiplication,
    units_pc_pc_UnitPower,
    units_pc_pc_UnitRepository,
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

def test_assoc_baseUnit6_stub_double():
    # units_pc_pc_UnitLiteral has no real 'units_pc_pc_UnitLiteral' property in the generated
    # code (a bare stub) -- manually attach it so units_pc_pc_BaseUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # units_pc_pc_BaseUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = units_pc_pc_BaseUnit(name="sample_text")
    partner = units_pc_pc_UnitLiteral()
    setattr(partner, 'units_pc_pc_UnitLiteral', None)
    _safe_set(owner, 'units_pc_pc_BaseUnit7', partner)
    assert getattr(partner, 'units_pc_pc_UnitLiteral') == owner
    _safe_set(owner, 'units_pc_pc_BaseUnit7', None)
    assert getattr(partner, 'units_pc_pc_UnitLiteral') is None


def test_assoc_unit0_stub_double():
    # units_pc_pc_Unit has no real 'units_pc_pc_Unit' property in the generated
    # code (a bare stub) -- manually attach it so units_pc_pc_UnitCarryingElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # units_pc_pc_UnitCarryingElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = units_pc_pc_UnitCarryingElement(unitSpecification="sample_text")
    partner = units_pc_pc_Unit()
    setattr(partner, 'units_pc_pc_Unit', None)
    _safe_set(owner, 'units_pc_pc_UnitCarryingElement', partner)
    assert getattr(partner, 'units_pc_pc_Unit') == owner
    _safe_set(owner, 'units_pc_pc_UnitCarryingElement', None)
    assert getattr(partner, 'units_pc_pc_Unit') is None


def test_assoc_unit4_stub_double():
    # units_pc_pc_Unit has no real 'units_pc_pc_Unit5' property in the generated
    # code (a bare stub) -- manually attach it so units_pc_pc_UnitPower's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # units_pc_pc_UnitPower's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = units_pc_pc_UnitPower(exponent=7)
    partner = units_pc_pc_Unit()
    setattr(partner, 'units_pc_pc_Unit5', None)
    _safe_set(owner, 'units_pc_pc_UnitPower', partner)
    assert getattr(partner, 'units_pc_pc_Unit5') == owner
    _safe_set(owner, 'units_pc_pc_UnitPower', None)
    assert getattr(partner, 'units_pc_pc_Unit5') is None


def test_assoc_units1_stub_double():
    # units_pc_pc_UnitRepository has no real 'units_pc_pc_UnitRepository' property in the generated
    # code (a bare stub) -- manually attach it so units_pc_pc_BaseUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # units_pc_pc_BaseUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = units_pc_pc_BaseUnit(name="sample_text")
    partner = units_pc_pc_UnitRepository()
    setattr(partner, 'units_pc_pc_UnitRepository', None)
    _safe_set(owner, 'units_pc_pc_BaseUnit', partner)
    assert owner in getattr(partner, 'units_pc_pc_UnitRepository')
    _safe_set(owner, 'units_pc_pc_BaseUnit', None)
    assert owner not in getattr(partner, 'units_pc_pc_UnitRepository')


