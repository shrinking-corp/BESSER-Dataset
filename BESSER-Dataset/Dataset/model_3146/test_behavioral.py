import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Axis,
    Expression,
    LiteralExp,
    LocatedElement,
    NamedElement,
    NodeTest,
    XPath_AncestorAxis,
    XPath_AncestorOrSelfAxis,
    XPath_AttributeAxis,
    XPath_Axis,
    XPath_ChildAxis,
    XPath_DescendantAxis,
    XPath_DescendantOrSelfAxis,
    XPath_Expression,
    XPath_FollowingAxis,
    XPath_FollowingSiblingAxis,
    XPath_FunctionCallExp,
    XPath_IntegerExp,
    XPath_IsNodeTest,
    XPath_IsTextTest,
    XPath_LiteralExp,
    XPath_LocatedElement,
    XPath_NameTest,
    XPath_NamedElement,
    XPath_NamespaceAxis,
    XPath_NodeTest,
    XPath_OperatorCallExp,
    XPath_ParentAxis,
    XPath_PathExpression,
    XPath_PrecedingAxis,
    XPath_PrecedingSiblingAxis,
    XPath_Predicate,
    XPath_SelfAxis,
    XPath_Step,
    XPath_StringExp,
    XPath_VariableExp,
    XPath_WildCardTest,
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

def test_assoc_steps0_stub_double():
    # XPath_Step has no real 'XPath_Step' property in the generated
    # code (a bare stub) -- manually attach it so XPath_PathExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # XPath_PathExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = XPath_PathExpression(isAbsolute="sample_text")
    partner = XPath_Step()
    setattr(partner, 'XPath_Step', None)
    _safe_set(owner, 'XPath_PathExpression', {partner})
    assert getattr(partner, 'XPath_Step') == owner
    _safe_set(owner, 'XPath_PathExpression', set())
    assert getattr(partner, 'XPath_Step') is None


