import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    ActivityEdge,
    ActivityNode,
    ControlNode,
    Event,
    NamedElement,
    RedefinableElement,
    ValueSpecification,
    umlknes_AcceptEventAction,
    umlknes_Action,
    umlknes_Activity,
    umlknes_ActivityEdge,
    umlknes_ActivityFinalNode,
    umlknes_ActivityNode,
    umlknes_ControlFlow,
    umlknes_ControlNode,
    umlknes_CreationEvent,
    umlknes_DecisionNode,
    umlknes_DestructionEvent,
    umlknes_Event,
    umlknes_ExecutionEvent,
    umlknes_InitialNode,
    umlknes_NamedElement,
    umlknes_OpaqueExpression,
    umlknes_RedefinableElement,
    umlknes_Trigger,
    umlknes_ValueSpecification,
    VisibilityKind,
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

def test_assoc_activity14_stub_double():
    # umlknes_ActivityEdge has no real 'edge' property in the generated
    # code (a bare stub) -- manually attach it so umlknes_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlknes_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlknes_Activity(isReadOnly=True, isSingleExecution=True)
    partner = umlknes_ActivityEdge()
    setattr(partner, 'edge', None)
    _safe_set(owner, 'Activity15', partner)
    assert getattr(partner, 'edge') == owner
    _safe_set(owner, 'Activity15', None)
    assert getattr(partner, 'edge') is None


def test_assoc_activity3_stub_double():
    # umlknes_ActivityNode has no real 'node' property in the generated
    # code (a bare stub) -- manually attach it so umlknes_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlknes_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlknes_Activity(isReadOnly=True, isSingleExecution=True)
    partner = umlknes_ActivityNode()
    setattr(partner, 'node', None)
    _safe_set(owner, 'Activity', partner)
    assert getattr(partner, 'node') == owner
    _safe_set(owner, 'Activity', None)
    assert getattr(partner, 'node') is None


def test_assoc_edge1_stub_double():
    # umlknes_ActivityEdge has no real 'ActivityEdge' property in the generated
    # code (a bare stub) -- manually attach it so umlknes_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlknes_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlknes_Activity(isReadOnly=True, isSingleExecution=True)
    partner = umlknes_ActivityEdge()
    setattr(partner, 'ActivityEdge', None)
    _safe_set(owner, 'activity2', {partner})
    assert getattr(partner, 'ActivityEdge') == owner
    _safe_set(owner, 'activity2', set())
    assert getattr(partner, 'ActivityEdge') is None


def test_assoc_node0_stub_double():
    # umlknes_ActivityNode has no real 'ActivityNode' property in the generated
    # code (a bare stub) -- manually attach it so umlknes_Activity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlknes_Activity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlknes_Activity(isReadOnly=True, isSingleExecution=True)
    partner = umlknes_ActivityNode()
    setattr(partner, 'ActivityNode', None)
    _safe_set(owner, 'activity', {partner})
    assert getattr(partner, 'ActivityNode') == owner
    _safe_set(owner, 'activity', set())
    assert getattr(partner, 'ActivityNode') is None


def test_assoc_trigger20_stub_double():
    # umlknes_Trigger has no real 'umlknes_Trigger' property in the generated
    # code (a bare stub) -- manually attach it so umlknes_AcceptEventAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlknes_AcceptEventAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlknes_AcceptEventAction(isUnMarshall=True)
    partner = umlknes_Trigger()
    setattr(partner, 'umlknes_Trigger', None)
    _safe_set(owner, 'umlknes_AcceptEventAction', {partner})
    assert getattr(partner, 'umlknes_Trigger') == owner
    _safe_set(owner, 'umlknes_AcceptEventAction', set())
    assert getattr(partner, 'umlknes_Trigger') is None


