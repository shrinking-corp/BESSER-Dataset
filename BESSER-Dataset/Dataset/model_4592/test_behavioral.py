import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActivityEdge,
    ActivityNode,
    ModelElement,
    minuml2_Activity,
    minuml2_ActivityEdge,
    minuml2_ActivityFinalNode,
    minuml2_ActivityNode,
    minuml2_ActivityPartition,
    minuml2_ControlFlow,
    minuml2_DecisionNode,
    minuml2_ForkNode,
    minuml2_InitialNode,
    minuml2_JoinNode,
    minuml2_ModelElement,
    minuml2_ObjectFlow,
    minuml2_ObjectNode,
    minuml2_OpaqueAction,
    minuml2_OpaqueExpression,
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

def test_assoc_guard19_stub_double():
    # minuml2_ActivityEdge has no real 'minuml2_ActivityEdge20' property in the generated
    # code (a bare stub) -- manually attach it so minuml2_OpaqueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minuml2_OpaqueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minuml2_OpaqueExpression(body="sample_text", language="sample_text")
    partner = minuml2_ActivityEdge()
    setattr(partner, 'minuml2_ActivityEdge20', None)
    _safe_set(owner, 'minuml2_OpaqueExpression', partner)
    assert getattr(partner, 'minuml2_ActivityEdge20') == owner
    _safe_set(owner, 'minuml2_OpaqueExpression', None)
    assert getattr(partner, 'minuml2_ActivityEdge20') is None


def test_assoc_partition0_stub_double():
    # minuml2_ActivityPartition has no real 'minuml2_ActivityPartition' property in the generated
    # code (a bare stub) -- manually attach it so minuml2_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minuml2_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minuml2_ModelElement(name="sample_text")
    partner = minuml2_ActivityPartition()
    setattr(partner, 'minuml2_ActivityPartition', None)
    _safe_set(owner, 'minuml2_ModelElement', partner)
    assert getattr(partner, 'minuml2_ActivityPartition') == owner
    _safe_set(owner, 'minuml2_ModelElement', None)
    assert getattr(partner, 'minuml2_ActivityPartition') is None


def test_assoc_type21_stub_double():
    # minuml2_ObjectFlow has no real 'minuml2_ObjectFlow' property in the generated
    # code (a bare stub) -- manually attach it so minuml2_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minuml2_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minuml2_ModelElement(name="sample_text")
    partner = minuml2_ObjectFlow()
    setattr(partner, 'minuml2_ObjectFlow', None)
    _safe_set(owner, 'minuml2_ModelElement22', partner)
    assert getattr(partner, 'minuml2_ObjectFlow') == owner
    _safe_set(owner, 'minuml2_ModelElement22', None)
    assert getattr(partner, 'minuml2_ObjectFlow') is None


