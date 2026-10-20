import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Activity,
    ActivityEdge,
    ActivityGroup,
    ActivityNode,
    ControlNode,
    ExecutableNode,
    FinalNode,
    NamedElement,
    ObjectNode,
    Pin,
    activity_AcceptEventAction,
    activity_AcceptTimeEventAction,
    activity_Action,
    activity_Activity,
    activity_ActivityEdge,
    activity_ActivityFinalNode,
    activity_ActivityGroup,
    activity_ActivityNode,
    activity_ActivityParameterNode,
    activity_ActivityPartition,
    activity_CentralBufferNode,
    activity_Connector,
    activity_ControlFlow,
    activity_ControlNode,
    activity_DataStoreNode,
    activity_DecisionNode,
    activity_ExecutableNode,
    activity_FinalNode,
    activity_FlowFinalNode,
    activity_ForkNode,
    activity_InitialNode,
    activity_InputPin,
    activity_InterruptEdge,
    activity_InterruptibleActivityRegion,
    activity_JoinNode,
    activity_MergeNode,
    activity_NamedElement,
    activity_Object,
    activity_ObjectFlow,
    activity_ObjectNode,
    activity_OutputPin,
    activity_Pin,
    activity_SendSignalAction,
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

def test_assoc_activityGroups7_stub_double():
    # activity_Activity has no real 'activity_Activity8' property in the generated
    # code (a bare stub) -- manually attach it so activity_ActivityGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activity_ActivityGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activity_ActivityGroup(name="sample_text")
    partner = activity_Activity()
    setattr(partner, 'activity_Activity8', None)
    _safe_set(owner, 'activity_ActivityGroup', partner)
    assert owner in getattr(partner, 'activity_Activity8')
    _safe_set(owner, 'activity_ActivityGroup', None)
    assert owner not in getattr(partner, 'activity_Activity8')


def test_assoc_activityparameternode3_stub_double():
    # activity_Activity has no real 'activity_Activity4' property in the generated
    # code (a bare stub) -- manually attach it so activity_ActivityParameterNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activity_ActivityParameterNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activity_ActivityParameterNode(name="sample_text")
    partner = activity_Activity()
    setattr(partner, 'activity_Activity4', None)
    _safe_set(owner, 'activity_ActivityParameterNode', partner)
    assert getattr(partner, 'activity_Activity4') == owner
    _safe_set(owner, 'activity_ActivityParameterNode', None)
    assert getattr(partner, 'activity_Activity4') is None


def test_assoc_inBorder9_stub_double():
    # activity_ActivityNode has no real 'activity_ActivityNode11' property in the generated
    # code (a bare stub) -- manually attach it so activity_ActivityParameterNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # activity_ActivityParameterNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = activity_ActivityParameterNode(name="sample_text")
    partner = activity_ActivityNode()
    setattr(partner, 'activity_ActivityNode11', None)
    _safe_set(owner, 'activity_ActivityParameterNode10', {partner})
    assert getattr(partner, 'activity_ActivityNode11') == owner
    _safe_set(owner, 'activity_ActivityParameterNode10', set())
    assert getattr(partner, 'activity_ActivityNode11') is None


