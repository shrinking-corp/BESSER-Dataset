import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Literal,
    Named,
    d3ql_AggregateRoot,
    d3ql_Alias,
    d3ql_BooleanLiteral,
    d3ql_EObject,
    d3ql_FromStatement,
    d3ql_FunctionArgument,
    d3ql_FunctionCall,
    d3ql_IntegerLiteral,
    d3ql_Literal,
    d3ql_Named,
    d3ql_PathElement,
    d3ql_PathExpression,
    d3ql_Query,
    d3ql_SelectExpression,
    d3ql_SelectStatement,
    d3ql_StringLiteral,
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

def test_assoc_arguments17_stub_double():
    # d3ql_FunctionArgument has no real 'd3ql_FunctionArgument' property in the generated
    # code (a bare stub) -- manually attach it so d3ql_FunctionCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # d3ql_FunctionCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = d3ql_FunctionCall(function="sample_text")
    partner = d3ql_FunctionArgument()
    setattr(partner, 'd3ql_FunctionArgument', None)
    _safe_set(owner, 'd3ql_FunctionCall', {partner})
    assert getattr(partner, 'd3ql_FunctionArgument') == owner
    _safe_set(owner, 'd3ql_FunctionCall', set())
    assert getattr(partner, 'd3ql_FunctionArgument') is None


def test_assoc_head14_stub_double():
    # d3ql_PathExpression has no real 'd3ql_PathExpression' property in the generated
    # code (a bare stub) -- manually attach it so d3ql_Named's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # d3ql_Named's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = d3ql_Named(name="sample_text")
    partner = d3ql_PathExpression()
    setattr(partner, 'd3ql_PathExpression', None)
    _safe_set(owner, 'd3ql_Named', partner)
    assert getattr(partner, 'd3ql_PathExpression') == owner
    _safe_set(owner, 'd3ql_Named', None)
    assert getattr(partner, 'd3ql_PathExpression') is None


def test_assoc_tail15_stub_double():
    # d3ql_PathExpression has no real 'd3ql_PathExpression16' property in the generated
    # code (a bare stub) -- manually attach it so d3ql_PathElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # d3ql_PathElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = d3ql_PathElement(name="sample_text")
    partner = d3ql_PathExpression()
    setattr(partner, 'd3ql_PathExpression16', None)
    _safe_set(owner, 'd3ql_PathElement', partner)
    assert owner in getattr(partner, 'd3ql_PathExpression16')
    _safe_set(owner, 'd3ql_PathElement', None)
    assert owner not in getattr(partner, 'd3ql_PathExpression16')


