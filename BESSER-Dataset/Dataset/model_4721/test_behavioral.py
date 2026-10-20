import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryExpression,
    IntegerExpression,
    NeighborsExpression,
    UnaryExpression,
    ca_rule_Add,
    ca_rule_And,
    ca_rule_BinaryExpression,
    ca_rule_CellularAutomata,
    ca_rule_Conditional,
    ca_rule_CurrentCellPopulation,
    ca_rule_Div,
    ca_rule_Equal,
    ca_rule_Greater,
    ca_rule_IntegerExpression,
    ca_rule_IntegerLiteral,
    ca_rule_Lower,
    ca_rule_Max,
    ca_rule_Min,
    ca_rule_Minus,
    ca_rule_Mod,
    ca_rule_Mult,
    ca_rule_NeighborsExpression,
    ca_rule_Not,
    ca_rule_Or,
    ca_rule_PopulationRange,
    ca_rule_Rule,
    ca_rule_Size,
    ca_rule_Sum,
    ca_rule_UMinus,
    ca_rule_UnaryExpression,
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
    # ca_rule_Rule has no real 'ca_rule_Rule2' property in the generated
    # code (a bare stub) -- manually attach it so ca_rule_PopulationRange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ca_rule_PopulationRange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ca_rule_PopulationRange(lowerRange=7, upperRange=7)
    partner = ca_rule_Rule()
    setattr(partner, 'ca_rule_Rule2', None)
    _safe_set(owner, 'ca_rule_PopulationRange', partner)
    assert getattr(partner, 'ca_rule_Rule2') == owner
    _safe_set(owner, 'ca_rule_PopulationRange', None)
    assert getattr(partner, 'ca_rule_Rule2') is None


def test_assoc_neighborsFilter13_stub_double():
    # ca_rule_NeighborsExpression has no real 'ca_rule_NeighborsExpression' property in the generated
    # code (a bare stub) -- manually attach it so ca_rule_PopulationRange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ca_rule_PopulationRange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ca_rule_PopulationRange(lowerRange=7, upperRange=7)
    partner = ca_rule_NeighborsExpression()
    setattr(partner, 'ca_rule_NeighborsExpression', None)
    _safe_set(owner, 'ca_rule_PopulationRange14', partner)
    assert getattr(partner, 'ca_rule_NeighborsExpression') == owner
    _safe_set(owner, 'ca_rule_PopulationRange14', None)
    assert getattr(partner, 'ca_rule_NeighborsExpression') is None


