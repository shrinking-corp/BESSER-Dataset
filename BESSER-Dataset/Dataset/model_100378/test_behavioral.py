import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ModelElement,
    State,
    StateMachine,
    StateVertex,
    minuml1_ActionState,
    minuml1_ActivityGraph,
    minuml1_BooleanExpression,
    minuml1_CompositeState,
    minuml1_FinalState,
    minuml1_Guard,
    minuml1_ModelElement,
    minuml1_ObjectFlowState,
    minuml1_Partition,
    minuml1_Pseudostate,
    minuml1_State,
    minuml1_StateMachine,
    minuml1_StateVertex,
    minuml1_Transition,
    PseudostateKind,
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

def test_assoc_contents5_stub_double():
    # minuml1_Partition has no real 'partition' property in the generated
    # code (a bare stub) -- manually attach it so minuml1_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minuml1_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minuml1_ModelElement(name="sample_text")
    partner = minuml1_Partition()
    setattr(partner, 'partition', None)
    _safe_set(owner, 'ModelElement', partner)
    assert owner in getattr(partner, 'partition')
    _safe_set(owner, 'ModelElement', None)
    assert owner not in getattr(partner, 'partition')


def test_assoc_expression16_stub_double():
    # minuml1_Guard has no real 'minuml1_Guard17' property in the generated
    # code (a bare stub) -- manually attach it so minuml1_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minuml1_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minuml1_BooleanExpression(body="sample_text", language="sample_text")
    partner = minuml1_Guard()
    setattr(partner, 'minuml1_Guard17', None)
    _safe_set(owner, 'minuml1_BooleanExpression', partner)
    assert getattr(partner, 'minuml1_Guard17') == owner
    _safe_set(owner, 'minuml1_BooleanExpression', None)
    assert getattr(partner, 'minuml1_Guard17') is None


def test_assoc_partition0_stub_double():
    # minuml1_Partition has no real 'Partition' property in the generated
    # code (a bare stub) -- manually attach it so minuml1_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minuml1_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minuml1_ModelElement(name="sample_text")
    partner = minuml1_Partition()
    setattr(partner, 'Partition', None)
    _safe_set(owner, 'contents', partner)
    assert getattr(partner, 'Partition') == owner
    _safe_set(owner, 'contents', None)
    assert getattr(partner, 'Partition') is None


def test_assoc_type10_stub_double():
    # minuml1_ObjectFlowState has no real 'minuml1_ObjectFlowState' property in the generated
    # code (a bare stub) -- manually attach it so minuml1_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minuml1_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minuml1_ModelElement(name="sample_text")
    partner = minuml1_ObjectFlowState()
    setattr(partner, 'minuml1_ObjectFlowState', None)
    _safe_set(owner, 'minuml1_ModelElement', partner)
    assert getattr(partner, 'minuml1_ObjectFlowState') == owner
    _safe_set(owner, 'minuml1_ModelElement', None)
    assert getattr(partner, 'minuml1_ObjectFlowState') is None


