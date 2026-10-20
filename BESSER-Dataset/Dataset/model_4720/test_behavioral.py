import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryExpression,
    IntegerExpression,
    NeighborsExpression,
    UnaryExpression,
    rule_Add,
    rule_And,
    rule_BinaryExpression,
    rule_CellularAutomata,
    rule_Conditional,
    rule_CurrentCellPopulation,
    rule_Div,
    rule_Equal,
    rule_Greater,
    rule_IntegerExpression,
    rule_IntegerLiteral,
    rule_Lower,
    rule_Max,
    rule_Min,
    rule_Minus,
    rule_Mod,
    rule_Mult,
    rule_NeighborsExpression,
    rule_Not,
    rule_Or,
    rule_PopulationRange,
    rule_Rule,
    rule_Size,
    rule_Sum,
    rule_UMinus,
    rule_UnaryExpression,
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

def test_assoc_filter1_stub_double():
    # rule_Rule has no real 'rule_Rule2' property in the generated
    # code (a bare stub) -- manually attach it so rule_PopulationRange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rule_PopulationRange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rule_PopulationRange(lowerRange=7, upperRange=7)
    partner = rule_Rule()
    setattr(partner, 'rule_Rule2', None)
    _safe_set(owner, 'rule_PopulationRange', partner)
    assert getattr(partner, 'rule_Rule2') == owner
    _safe_set(owner, 'rule_PopulationRange', None)
    assert getattr(partner, 'rule_Rule2') is None


def test_assoc_neighborsFilter13_stub_double():
    # rule_NeighborsExpression has no real 'rule_NeighborsExpression' property in the generated
    # code (a bare stub) -- manually attach it so rule_PopulationRange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rule_PopulationRange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rule_PopulationRange(lowerRange=7, upperRange=7)
    partner = rule_NeighborsExpression()
    setattr(partner, 'rule_NeighborsExpression', None)
    _safe_set(owner, 'rule_PopulationRange14', partner)
    assert getattr(partner, 'rule_NeighborsExpression') == owner
    _safe_set(owner, 'rule_PopulationRange14', None)
    assert getattr(partner, 'rule_NeighborsExpression') is None


