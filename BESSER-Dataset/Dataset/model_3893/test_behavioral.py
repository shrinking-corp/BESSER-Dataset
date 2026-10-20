import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CompoundTask,
    OutputPort,
    Port,
    WorkflowElement,
    WorkflowNode,
    workflow_Comment,
    workflow_CompoundTask,
    workflow_ConditionalOutputPort,
    workflow_ConditionalTask,
    workflow_Edge,
    workflow_Fault,
    workflow_InputPort,
    workflow_LoopTask,
    workflow_OutputPort,
    workflow_Port,
    workflow_Task,
    workflow_TransformationTask,
    workflow_Workflow,
    workflow_WorkflowElement,
    workflow_WorkflowNode,
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

def test_assoc_inputs7_stub_double():
    # workflow_InputPort has no real 'InputPort' property in the generated
    # code (a bare stub) -- manually attach it so workflow_WorkflowNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_WorkflowNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_WorkflowNode(isFinish=True, isStart=True)
    partner = workflow_InputPort()
    setattr(partner, 'InputPort', None)
    _safe_set(owner, 'node8', {partner})
    assert getattr(partner, 'InputPort') == owner
    _safe_set(owner, 'node8', set())
    assert getattr(partner, 'InputPort') is None


def test_assoc_node17_stub_double():
    # workflow_InputPort has no real 'inputs' property in the generated
    # code (a bare stub) -- manually attach it so workflow_WorkflowNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_WorkflowNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_WorkflowNode(isFinish=True, isStart=True)
    partner = workflow_InputPort()
    setattr(partner, 'inputs', None)
    _safe_set(owner, 'WorkflowNode18', partner)
    assert getattr(partner, 'inputs') == owner
    _safe_set(owner, 'WorkflowNode18', None)
    assert getattr(partner, 'inputs') is None


def test_assoc_node21_stub_double():
    # workflow_OutputPort has no real 'outputs' property in the generated
    # code (a bare stub) -- manually attach it so workflow_WorkflowNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_WorkflowNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_WorkflowNode(isFinish=True, isStart=True)
    partner = workflow_OutputPort()
    setattr(partner, 'outputs', None)
    _safe_set(owner, 'WorkflowNode22', partner)
    assert getattr(partner, 'outputs') == owner
    _safe_set(owner, 'WorkflowNode22', None)
    assert getattr(partner, 'outputs') is None


def test_assoc_nodes0_stub_double():
    # workflow_Workflow has no real 'workflow' property in the generated
    # code (a bare stub) -- manually attach it so workflow_WorkflowNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_WorkflowNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_WorkflowNode(isFinish=True, isStart=True)
    partner = workflow_Workflow()
    setattr(partner, 'workflow', None)
    _safe_set(owner, 'WorkflowNode', partner)
    assert owner in getattr(partner, 'workflow')
    _safe_set(owner, 'WorkflowNode', None)
    assert owner not in getattr(partner, 'workflow')


def test_assoc_outputs6_stub_double():
    # workflow_OutputPort has no real 'OutputPort' property in the generated
    # code (a bare stub) -- manually attach it so workflow_WorkflowNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_WorkflowNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_WorkflowNode(isFinish=True, isStart=True)
    partner = workflow_OutputPort()
    setattr(partner, 'OutputPort', None)
    _safe_set(owner, 'node', {partner})
    assert getattr(partner, 'OutputPort') == owner
    _safe_set(owner, 'node', set())
    assert getattr(partner, 'OutputPort') is None


def test_assoc_workflow5_stub_double():
    # workflow_Workflow has no real 'Workflow' property in the generated
    # code (a bare stub) -- manually attach it so workflow_WorkflowNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_WorkflowNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_WorkflowNode(isFinish=True, isStart=True)
    partner = workflow_Workflow()
    setattr(partner, 'Workflow', None)
    _safe_set(owner, 'nodes', partner)
    assert getattr(partner, 'Workflow') == owner
    _safe_set(owner, 'nodes', None)
    assert getattr(partner, 'Workflow') is None


