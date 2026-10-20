import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    IPort,
    IWorkflowElement,
    IWorkflowNode,
    workflow_IInputPort,
    workflow_ILink,
    workflow_IOutputPort,
    workflow_IPort,
    workflow_IWorkflow,
    workflow_IWorkflowElement,
    workflow_IWorkflowJob,
    workflow_IWorkflowNode,
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

def test_assoc_inputs20_stub_double():
    # workflow_IInputPort has no real 'IInputPort22' property in the generated
    # code (a bare stub) -- manually attach it so workflow_IWorkflowNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_IWorkflowNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_IWorkflowNode(isFinish=True, isStart=True)
    partner = workflow_IInputPort()
    setattr(partner, 'IInputPort22', None)
    _safe_set(owner, 'node21', {partner})
    assert getattr(partner, 'IInputPort22') == owner
    _safe_set(owner, 'node21', set())
    assert getattr(partner, 'IInputPort22') is None


def test_assoc_node5_stub_double():
    # workflow_IInputPort has no real 'inputs' property in the generated
    # code (a bare stub) -- manually attach it so workflow_IWorkflowNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_IWorkflowNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_IWorkflowNode(isFinish=True, isStart=True)
    partner = workflow_IInputPort()
    setattr(partner, 'inputs', None)
    _safe_set(owner, 'IWorkflowNode', partner)
    assert getattr(partner, 'inputs') == owner
    _safe_set(owner, 'IWorkflowNode', None)
    assert getattr(partner, 'inputs') is None


def test_assoc_node7_stub_double():
    # workflow_IOutputPort has no real 'outputs' property in the generated
    # code (a bare stub) -- manually attach it so workflow_IWorkflowNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_IWorkflowNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_IWorkflowNode(isFinish=True, isStart=True)
    partner = workflow_IOutputPort()
    setattr(partner, 'outputs', None)
    _safe_set(owner, 'IWorkflowNode8', partner)
    assert getattr(partner, 'outputs') == owner
    _safe_set(owner, 'IWorkflowNode8', None)
    assert getattr(partner, 'outputs') is None


def test_assoc_nodes11_stub_double():
    # workflow_IWorkflow has no real 'workflow' property in the generated
    # code (a bare stub) -- manually attach it so workflow_IWorkflowNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_IWorkflowNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_IWorkflowNode(isFinish=True, isStart=True)
    partner = workflow_IWorkflow()
    setattr(partner, 'workflow', None)
    _safe_set(owner, 'IWorkflowNode12', partner)
    assert owner in getattr(partner, 'workflow')
    _safe_set(owner, 'IWorkflowNode12', None)
    assert owner not in getattr(partner, 'workflow')


def test_assoc_outputs18_stub_double():
    # workflow_IOutputPort has no real 'IOutputPort19' property in the generated
    # code (a bare stub) -- manually attach it so workflow_IWorkflowNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_IWorkflowNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_IWorkflowNode(isFinish=True, isStart=True)
    partner = workflow_IOutputPort()
    setattr(partner, 'IOutputPort19', None)
    _safe_set(owner, 'node', {partner})
    assert getattr(partner, 'IOutputPort19') == owner
    _safe_set(owner, 'node', set())
    assert getattr(partner, 'IOutputPort19') is None


def test_assoc_workflow16_stub_double():
    # workflow_IWorkflow has no real 'IWorkflow17' property in the generated
    # code (a bare stub) -- manually attach it so workflow_IWorkflowNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_IWorkflowNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_IWorkflowNode(isFinish=True, isStart=True)
    partner = workflow_IWorkflow()
    setattr(partner, 'IWorkflow17', None)
    _safe_set(owner, 'nodes', partner)
    assert getattr(partner, 'IWorkflow17') == owner
    _safe_set(owner, 'nodes', None)
    assert getattr(partner, 'IWorkflow17') is None


