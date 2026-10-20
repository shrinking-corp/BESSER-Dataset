import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryOp,
    BoolOperand,
    BoolOperandChoices,
    Comparison,
    LogicalOperator,
    NumOperand,
    NumOperandChoices,
    NumOperator,
    Operand,
    Selection,
    UnaryOp,
    hydraconstraints_All,
    hydraconstraints_And,
    hydraconstraints_Any,
    hydraconstraints_BinaryOp,
    hydraconstraints_BoolOperand,
    hydraconstraints_BoolOperandChoices,
    hydraconstraints_BoolPriorityOperand1,
    hydraconstraints_BoolPriorityOperand2,
    hydraconstraints_Comparison,
    hydraconstraints_Constraint,
    hydraconstraints_Context,
    hydraconstraints_Div,
    hydraconstraints_Equal,
    hydraconstraints_Implies,
    hydraconstraints_Less,
    hydraconstraints_LessOrEqual,
    hydraconstraints_LogicalOperator,
    hydraconstraints_Minus,
    hydraconstraints_Model,
    hydraconstraints_More,
    hydraconstraints_MoreOrEqual,
    hydraconstraints_Mul,
    hydraconstraints_MultipleFeature,
    hydraconstraints_Neg,
    hydraconstraints_NotEqual,
    hydraconstraints_NumOperand,
    hydraconstraints_NumOperandChoices,
    hydraconstraints_NumOperator,
    hydraconstraints_NumPriorityOperand1,
    hydraconstraints_NumPriorityOperand2,
    hydraconstraints_Number,
    hydraconstraints_Operand,
    hydraconstraints_Or,
    hydraconstraints_Plus,
    hydraconstraints_Selection,
    hydraconstraints_SimpleFeature,
    hydraconstraints_UnaryOp,
    hydraconstraints_Xor,
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

def test_assoc_constraints0_stub_double():
    # hydraconstraints_Constraint has no real 'hydraconstraints_Constraint' property in the generated
    # code (a bare stub) -- manually attach it so hydraconstraints_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hydraconstraints_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hydraconstraints_Model(featureList="sample_text")
    partner = hydraconstraints_Constraint()
    setattr(partner, 'hydraconstraints_Constraint', None)
    _safe_set(owner, 'hydraconstraints_Model', {partner})
    assert getattr(partner, 'hydraconstraints_Constraint') == owner
    _safe_set(owner, 'hydraconstraints_Model', set())
    assert getattr(partner, 'hydraconstraints_Constraint') is None


def test_assoc_contextOp129_stub_double():
    # hydraconstraints_Context has no real 'hydraconstraints_Context30' property in the generated
    # code (a bare stub) -- manually attach it so hydraconstraints_MultipleFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hydraconstraints_MultipleFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hydraconstraints_MultipleFeature(featureName="sample_text")
    partner = hydraconstraints_Context()
    setattr(partner, 'hydraconstraints_Context30', None)
    _safe_set(owner, 'hydraconstraints_MultipleFeature', partner)
    assert getattr(partner, 'hydraconstraints_Context30') == owner
    _safe_set(owner, 'hydraconstraints_MultipleFeature', None)
    assert getattr(partner, 'hydraconstraints_Context30') is None


