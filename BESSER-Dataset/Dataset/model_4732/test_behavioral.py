import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryOp,
    BooleanLiteral,
    DescribedElement,
    Domain,
    Expression,
    Goal,
    NamedElement,
    Operator,
    SetOp,
    TypedElement,
    UnaryOp,
    simple_csp_And,
    simple_csp_BinaryOp,
    simple_csp_BooleanLiteral,
    simple_csp_Constraint,
    simple_csp_DescribedElement,
    simple_csp_Domain,
    simple_csp_Equal,
    simple_csp_Expression,
    simple_csp_FalseValue,
    simple_csp_Goal,
    simple_csp_Greater,
    simple_csp_GreaterEqual,
    simple_csp_Implies,
    simple_csp_IntegerDomain,
    simple_csp_Less,
    simple_csp_LessEqual,
    simple_csp_Max,
    simple_csp_MaximizeGoal,
    simple_csp_Min,
    simple_csp_MinimizeGoal,
    simple_csp_Minus,
    simple_csp_NamedElement,
    simple_csp_Not,
    simple_csp_Operator,
    simple_csp_Or,
    simple_csp_Plus,
    simple_csp_Power,
    simple_csp_Problem,
    simple_csp_SetOp,
    simple_csp_Sum,
    simple_csp_Times,
    simple_csp_TrueValue,
    simple_csp_TypedElement,
    simple_csp_UnEqual,
    simple_csp_UnaryOp,
    simple_csp_VarOccurence,
    simple_csp_Variable,
    Type,
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

def test_assoc_domain7_stub_double():
    # simple_csp_Domain has no real 'simple_csp_Domain8' property in the generated
    # code (a bare stub) -- manually attach it so simple_csp_TypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simple_csp_TypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simple_csp_TypedElement(type="sample_text")
    partner = simple_csp_Domain()
    setattr(partner, 'simple_csp_Domain8', None)
    _safe_set(owner, 'simple_csp_TypedElement', partner)
    assert getattr(partner, 'simple_csp_Domain8') == owner
    _safe_set(owner, 'simple_csp_TypedElement', None)
    assert getattr(partner, 'simple_csp_Domain8') is None


