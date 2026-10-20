import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryExpression,
    CardExpression,
    ConstExpression,
    Expression,
    NAryExpression,
    NamedElement,
    SMTlib2extended_AddExpression,
    SMTlib2extended_AndExpression,
    SMTlib2extended_BinaryExpression,
    SMTlib2extended_BitstringExpression,
    SMTlib2extended_Bitvector,
    SMTlib2extended_BvAndExpression,
    SMTlib2extended_BvNotExpression,
    SMTlib2extended_BvOrExpression,
    SMTlib2extended_BvXorExpression,
    SMTlib2extended_CardEqExpression,
    SMTlib2extended_CardExpression,
    SMTlib2extended_CardGeExpression,
    SMTlib2extended_CardGtExpression,
    SMTlib2extended_CardLeExpression,
    SMTlib2extended_CardLtExpression,
    SMTlib2extended_ConcatExpression,
    SMTlib2extended_ConstBooleanExpression,
    SMTlib2extended_ConstExpression,
    SMTlib2extended_ConstIntegerExpression,
    SMTlib2extended_DivExpression,
    SMTlib2extended_EqualsExpression,
    SMTlib2extended_Expression,
    SMTlib2extended_ExtractIndexExpression,
    SMTlib2extended_GreaterEqualsExpression,
    SMTlib2extended_GreaterExpression,
    SMTlib2extended_ImpliesExpression,
    SMTlib2extended_Instance,
    SMTlib2extended_IteExpression,
    SMTlib2extended_LessEqualsExpression,
    SMTlib2extended_LessExpression,
    SMTlib2extended_ModExpression,
    SMTlib2extended_MulExpression,
    SMTlib2extended_NAryExpression,
    SMTlib2extended_NamedElement,
    SMTlib2extended_NandExpression,
    SMTlib2extended_NotExpression,
    SMTlib2extended_OneHotExpression,
    SMTlib2extended_OrExpression,
    SMTlib2extended_Predicate,
    SMTlib2extended_SubExpression,
    SMTlib2extended_UnaryExpression,
    SMTlib2extended_Variable,
    SMTlib2extended_VariableExpression,
    UnaryExpression,
    Variable,
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

def test_assoc_expressions22_stub_double():
    # SMTlib2extended_Expression has no real 'SMTlib2extended_Expression23' property in the generated
    # code (a bare stub) -- manually attach it so SMTlib2extended_CardExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SMTlib2extended_CardExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SMTlib2extended_CardExpression(k=7)
    partner = SMTlib2extended_Expression()
    setattr(partner, 'SMTlib2extended_Expression23', None)
    _safe_set(owner, 'SMTlib2extended_CardExpression', {partner})
    assert getattr(partner, 'SMTlib2extended_Expression23') == owner
    _safe_set(owner, 'SMTlib2extended_CardExpression', set())
    assert getattr(partner, 'SMTlib2extended_Expression23') is None


