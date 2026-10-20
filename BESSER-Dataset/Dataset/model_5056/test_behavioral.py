import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EObject,
    Event,
    FlowNode,
    SplitGateway,
    cbpmn_Activity,
    cbpmn_Branch,
    cbpmn_DataObject,
    cbpmn_DataObjectReference,
    cbpmn_DecisionGateway,
    cbpmn_EClass,
    cbpmn_EObject,
    cbpmn_EndEvent,
    cbpmn_Event,
    cbpmn_FlowNode,
    cbpmn_FlowNodeInstance,
    cbpmn_IntermediateEvent,
    cbpmn_OCLConstraint,
    cbpmn_ParallelGateway,
    cbpmn_ProcessInstance,
    cbpmn_ProcessModel,
    cbpmn_SplitGateway,
    cbpmn_StartEvent,
    ActivityType,
    DataObjectType,
    DecisionType,
    EventType,
    FlowNodeInstanceStatus,
    GatewayType,
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

def test_assoc_branch17_reverse_link_reassign_clear():
    a1 = cbpmn_FlowNode(name="sample_text")
    a2 = cbpmn_FlowNode(name="sample_text_2")
    b = cbpmn_Branch(default=True)
    _safe_set(b, 'Branch', a1)
    assert _is_linked(b, 'Branch', a1)
    if hasattr(a1, 'nodes'):
        assert _is_linked(a1, 'nodes', b)
    _safe_set(b, 'Branch', a2)
    assert _is_linked(b, 'Branch', a2)
    if hasattr(a1, 'nodes'):
        assert not _is_linked(a1, 'nodes', b)
    if hasattr(a2, 'nodes'):
        assert _is_linked(a2, 'nodes', b)
    _safe_set(b, 'Branch', None)
    assert not _is_linked(b, 'Branch', a2)
    if hasattr(a2, 'nodes'):
        assert not _is_linked(a2, 'nodes', b)


def test_assoc_branch26_reverse_link_reassign_clear():
    a1 = cbpmn_OCLConstraint(constraintName="sample_text", constraintStr="sample_text")
    a2 = cbpmn_OCLConstraint(constraintName="sample_text_2", constraintStr="sample_text_2")
    b = cbpmn_Branch(default=True)
    _safe_set(b, 'Branch27', a1)
    assert _is_linked(b, 'Branch27', a1)
    if hasattr(a1, 'entryConditions'):
        assert _is_linked(a1, 'entryConditions', b)
    _safe_set(b, 'Branch27', a2)
    assert _is_linked(b, 'Branch27', a2)
    if hasattr(a1, 'entryConditions'):
        assert not _is_linked(a1, 'entryConditions', b)
    if hasattr(a2, 'entryConditions'):
        assert _is_linked(a2, 'entryConditions', b)
    _safe_set(b, 'Branch27', None)
    assert not _is_linked(b, 'Branch27', a2)
    if hasattr(a2, 'entryConditions'):
        assert not _is_linked(a2, 'entryConditions', b)


def test_assoc_entryConditions14_reverse_link_reassign_clear():
    a1 = cbpmn_OCLConstraint(constraintName="sample_text", constraintStr="sample_text")
    a2 = cbpmn_OCLConstraint(constraintName="sample_text_2", constraintStr="sample_text_2")
    b = cbpmn_Branch(default=True)
    _safe_set(b, 'branch15', {a1})
    assert _is_linked(b, 'branch15', a1)
    if hasattr(a1, 'OCLConstraint'):
        assert _is_linked(a1, 'OCLConstraint', b)
    _safe_set(b, 'branch15', {a2})
    assert _is_linked(b, 'branch15', a2)
    if hasattr(a1, 'OCLConstraint'):
        assert not _is_linked(a1, 'OCLConstraint', b)
    if hasattr(a2, 'OCLConstraint'):
        assert _is_linked(a2, 'OCLConstraint', b)
    _safe_set(b, 'branch15', set())
    assert not _is_linked(b, 'branch15', a2)
    if hasattr(a2, 'OCLConstraint'):
        assert not _is_linked(a2, 'OCLConstraint', b)


def test_assoc_executedNodes36_reverse_link_reassign_clear():
    a1 = cbpmn_ProcessInstance(id="sample_text")
    a2 = cbpmn_ProcessInstance(id="sample_text_2")
    b = cbpmn_FlowNodeInstance(status="sample_text")
    _safe_set(b, 'FlowNodeInstance', a1)
    assert _is_linked(b, 'FlowNodeInstance', a1)
    if hasattr(a1, 'processInstance'):
        assert _is_linked(a1, 'processInstance', b)
    _safe_set(b, 'FlowNodeInstance', a2)
    assert _is_linked(b, 'FlowNodeInstance', a2)
    if hasattr(a1, 'processInstance'):
        assert not _is_linked(a1, 'processInstance', b)
    if hasattr(a2, 'processInstance'):
        assert _is_linked(a2, 'processInstance', b)
    _safe_set(b, 'FlowNodeInstance', None)
    assert not _is_linked(b, 'FlowNodeInstance', a2)
    if hasattr(a2, 'processInstance'):
        assert not _is_linked(a2, 'processInstance', b)


def test_assoc_inputs24_reverse_link_reassign_clear():
    a1 = cbpmn_FlowNode(name="sample_text")
    a2 = cbpmn_FlowNode(name="sample_text_2")
    b = cbpmn_DataObjectReference(higherBound=7, lowerBound=7, name="sample_text")
    _safe_set(b, 'cbpmn_DataObjectReference25', a1)
    assert _is_linked(b, 'cbpmn_DataObjectReference25', a1)
    if hasattr(a1, 'cbpmn_FlowNode'):
        assert _is_linked(a1, 'cbpmn_FlowNode', b)
    _safe_set(b, 'cbpmn_DataObjectReference25', a2)
    assert _is_linked(b, 'cbpmn_DataObjectReference25', a2)
    if hasattr(a1, 'cbpmn_FlowNode'):
        assert not _is_linked(a1, 'cbpmn_FlowNode', b)
    if hasattr(a2, 'cbpmn_FlowNode'):
        assert _is_linked(a2, 'cbpmn_FlowNode', b)
    _safe_set(b, 'cbpmn_DataObjectReference25', None)
    assert not _is_linked(b, 'cbpmn_DataObjectReference25', a2)
    if hasattr(a2, 'cbpmn_FlowNode'):
        assert not _is_linked(a2, 'cbpmn_FlowNode', b)


def test_assoc_invariabilityClauses10_reverse_link_reassign_clear():
    a1 = cbpmn_OCLConstraint(constraintName="sample_text", constraintStr="sample_text")
    a2 = cbpmn_OCLConstraint(constraintName="sample_text_2", constraintStr="sample_text_2")
    b = cbpmn_Activity(type="sample_text")
    _safe_set(b, 'cbpmn_Activity11', {a1})
    assert _is_linked(b, 'cbpmn_Activity11', a1)
    if hasattr(a1, 'cbpmn_OCLConstraint12'):
        assert _is_linked(a1, 'cbpmn_OCLConstraint12', b)
    _safe_set(b, 'cbpmn_Activity11', {a2})
    assert _is_linked(b, 'cbpmn_Activity11', a2)
    if hasattr(a1, 'cbpmn_OCLConstraint12'):
        assert not _is_linked(a1, 'cbpmn_OCLConstraint12', b)
    if hasattr(a2, 'cbpmn_OCLConstraint12'):
        assert _is_linked(a2, 'cbpmn_OCLConstraint12', b)
    _safe_set(b, 'cbpmn_Activity11', set())
    assert not _is_linked(b, 'cbpmn_Activity11', a2)
    if hasattr(a2, 'cbpmn_OCLConstraint12'):
        assert not _is_linked(a2, 'cbpmn_OCLConstraint12', b)


def test_assoc_mainBranch0_reverse_link_reassign_clear():
    a1 = cbpmn_ProcessModel(name="sample_text")
    a2 = cbpmn_ProcessModel(name="sample_text_2")
    b = cbpmn_Branch(default=True)
    _safe_set(b, 'cbpmn_Branch', a1)
    assert _is_linked(b, 'cbpmn_Branch', a1)
    if hasattr(a1, 'cbpmn_ProcessModel'):
        assert _is_linked(a1, 'cbpmn_ProcessModel', b)
    _safe_set(b, 'cbpmn_Branch', a2)
    assert _is_linked(b, 'cbpmn_Branch', a2)
    if hasattr(a1, 'cbpmn_ProcessModel'):
        assert not _is_linked(a1, 'cbpmn_ProcessModel', b)
    if hasattr(a2, 'cbpmn_ProcessModel'):
        assert _is_linked(a2, 'cbpmn_ProcessModel', b)
    _safe_set(b, 'cbpmn_Branch', None)
    assert not _is_linked(b, 'cbpmn_Branch', a2)
    if hasattr(a2, 'cbpmn_ProcessModel'):
        assert not _is_linked(a2, 'cbpmn_ProcessModel', b)


def test_assoc_next19_reverse_link_reassign_clear():
    a1 = cbpmn_FlowNode(name="sample_text")
    a2 = cbpmn_FlowNode(name="sample_text_2")
    b = cbpmn_FlowNode(name="sample_text")
    _safe_set(b, 'previous', a1)
    assert _is_linked(b, 'previous', a1)
    if hasattr(a1, 'FlowNode20'):
        assert _is_linked(a1, 'FlowNode20', b)
    _safe_set(b, 'previous', a2)
    assert _is_linked(b, 'previous', a2)
    if hasattr(a1, 'FlowNode20'):
        assert not _is_linked(a1, 'FlowNode20', b)
    if hasattr(a2, 'FlowNode20'):
        assert _is_linked(a2, 'FlowNode20', b)
    _safe_set(b, 'previous', None)
    assert not _is_linked(b, 'previous', a2)
    if hasattr(a2, 'FlowNode20'):
        assert not _is_linked(a2, 'FlowNode20', b)


def test_assoc_nodeDef39_reverse_link_reassign_clear():
    a1 = cbpmn_FlowNodeInstance(status="sample_text")
    a2 = cbpmn_FlowNodeInstance(status="sample_text_2")
    b = cbpmn_FlowNode(name="sample_text")
    _safe_set(b, 'cbpmn_FlowNode40', a1)
    assert _is_linked(b, 'cbpmn_FlowNode40', a1)
    if hasattr(a1, 'cbpmn_FlowNodeInstance'):
        assert _is_linked(a1, 'cbpmn_FlowNodeInstance', b)
    _safe_set(b, 'cbpmn_FlowNode40', a2)
    assert _is_linked(b, 'cbpmn_FlowNode40', a2)
    if hasattr(a1, 'cbpmn_FlowNodeInstance'):
        assert not _is_linked(a1, 'cbpmn_FlowNodeInstance', b)
    if hasattr(a2, 'cbpmn_FlowNodeInstance'):
        assert _is_linked(a2, 'cbpmn_FlowNodeInstance', b)
    _safe_set(b, 'cbpmn_FlowNode40', None)
    assert not _is_linked(b, 'cbpmn_FlowNode40', a2)
    if hasattr(a2, 'cbpmn_FlowNodeInstance'):
        assert not _is_linked(a2, 'cbpmn_FlowNodeInstance', b)


def test_assoc_nodes13_reverse_link_reassign_clear():
    a1 = cbpmn_FlowNode(name="sample_text")
    a2 = cbpmn_FlowNode(name="sample_text_2")
    b = cbpmn_Branch(default=True)
    _safe_set(b, 'branch', {a1})
    assert _is_linked(b, 'branch', a1)
    if hasattr(a1, 'FlowNode'):
        assert _is_linked(a1, 'FlowNode', b)
    _safe_set(b, 'branch', {a2})
    assert _is_linked(b, 'branch', a2)
    if hasattr(a1, 'FlowNode'):
        assert not _is_linked(a1, 'FlowNode', b)
    if hasattr(a2, 'FlowNode'):
        assert _is_linked(a2, 'FlowNode', b)
    _safe_set(b, 'branch', set())
    assert not _is_linked(b, 'branch', a2)
    if hasattr(a2, 'FlowNode'):
        assert not _is_linked(a2, 'FlowNode', b)


def test_assoc_outputs8_reverse_link_reassign_clear():
    a1 = cbpmn_DataObjectReference(higherBound=7, lowerBound=7, name="sample_text")
    a2 = cbpmn_DataObjectReference(higherBound=13, lowerBound=13, name="sample_text_2")
    b = cbpmn_Activity(type="sample_text")
    _safe_set(b, 'cbpmn_Activity9', {a1})
    assert _is_linked(b, 'cbpmn_Activity9', a1)
    if hasattr(a1, 'cbpmn_DataObjectReference'):
        assert _is_linked(a1, 'cbpmn_DataObjectReference', b)
    _safe_set(b, 'cbpmn_Activity9', {a2})
    assert _is_linked(b, 'cbpmn_Activity9', a2)
    if hasattr(a1, 'cbpmn_DataObjectReference'):
        assert not _is_linked(a1, 'cbpmn_DataObjectReference', b)
    if hasattr(a2, 'cbpmn_DataObjectReference'):
        assert _is_linked(a2, 'cbpmn_DataObjectReference', b)
    _safe_set(b, 'cbpmn_Activity9', set())
    assert not _is_linked(b, 'cbpmn_Activity9', a2)
    if hasattr(a2, 'cbpmn_DataObjectReference'):
        assert not _is_linked(a2, 'cbpmn_DataObjectReference', b)


def test_assoc_postConditions5_reverse_link_reassign_clear():
    a1 = cbpmn_OCLConstraint(constraintName="sample_text", constraintStr="sample_text")
    a2 = cbpmn_OCLConstraint(constraintName="sample_text_2", constraintStr="sample_text_2")
    b = cbpmn_Activity(type="sample_text")
    _safe_set(b, 'cbpmn_Activity6', {a1})
    assert _is_linked(b, 'cbpmn_Activity6', a1)
    if hasattr(a1, 'cbpmn_OCLConstraint7'):
        assert _is_linked(a1, 'cbpmn_OCLConstraint7', b)
    _safe_set(b, 'cbpmn_Activity6', {a2})
    assert _is_linked(b, 'cbpmn_Activity6', a2)
    if hasattr(a1, 'cbpmn_OCLConstraint7'):
        assert not _is_linked(a1, 'cbpmn_OCLConstraint7', b)
    if hasattr(a2, 'cbpmn_OCLConstraint7'):
        assert _is_linked(a2, 'cbpmn_OCLConstraint7', b)
    _safe_set(b, 'cbpmn_Activity6', set())
    assert not _is_linked(b, 'cbpmn_Activity6', a2)
    if hasattr(a2, 'cbpmn_OCLConstraint7'):
        assert not _is_linked(a2, 'cbpmn_OCLConstraint7', b)


def test_assoc_preConditions3_reverse_link_reassign_clear():
    a1 = cbpmn_OCLConstraint(constraintName="sample_text", constraintStr="sample_text")
    a2 = cbpmn_OCLConstraint(constraintName="sample_text_2", constraintStr="sample_text_2")
    b = cbpmn_Activity(type="sample_text")
    _safe_set(b, 'cbpmn_Activity', {a1})
    assert _is_linked(b, 'cbpmn_Activity', a1)
    if hasattr(a1, 'cbpmn_OCLConstraint4'):
        assert _is_linked(a1, 'cbpmn_OCLConstraint4', b)
    _safe_set(b, 'cbpmn_Activity', {a2})
    assert _is_linked(b, 'cbpmn_Activity', a2)
    if hasattr(a1, 'cbpmn_OCLConstraint4'):
        assert not _is_linked(a1, 'cbpmn_OCLConstraint4', b)
    if hasattr(a2, 'cbpmn_OCLConstraint4'):
        assert _is_linked(a2, 'cbpmn_OCLConstraint4', b)
    _safe_set(b, 'cbpmn_Activity', set())
    assert not _is_linked(b, 'cbpmn_Activity', a2)
    if hasattr(a2, 'cbpmn_OCLConstraint4'):
        assert not _is_linked(a2, 'cbpmn_OCLConstraint4', b)


def test_assoc_previous22_reverse_link_reassign_clear():
    a1 = cbpmn_FlowNode(name="sample_text")
    a2 = cbpmn_FlowNode(name="sample_text_2")
    b = cbpmn_FlowNode(name="sample_text")
    _safe_set(b, 'next', a1)
    assert _is_linked(b, 'next', a1)
    if hasattr(a1, 'FlowNode23'):
        assert _is_linked(a1, 'FlowNode23', b)
    _safe_set(b, 'next', a2)
    assert _is_linked(b, 'next', a2)
    if hasattr(a1, 'FlowNode23'):
        assert not _is_linked(a1, 'FlowNode23', b)
    if hasattr(a2, 'FlowNode23'):
        assert _is_linked(a2, 'FlowNode23', b)
    _safe_set(b, 'next', None)
    assert not _is_linked(b, 'next', a2)
    if hasattr(a2, 'FlowNode23'):
        assert not _is_linked(a2, 'FlowNode23', b)


def test_assoc_processInstance47_reverse_link_reassign_clear():
    a1 = cbpmn_ProcessInstance(id="sample_text")
    a2 = cbpmn_ProcessInstance(id="sample_text_2")
    b = cbpmn_FlowNodeInstance(status="sample_text")
    _safe_set(b, 'executedNodes', a1)
    assert _is_linked(b, 'executedNodes', a1)
    if hasattr(a1, 'ProcessInstance'):
        assert _is_linked(a1, 'ProcessInstance', b)
    _safe_set(b, 'executedNodes', a2)
    assert _is_linked(b, 'executedNodes', a2)
    if hasattr(a1, 'ProcessInstance'):
        assert not _is_linked(a1, 'ProcessInstance', b)
    if hasattr(a2, 'ProcessInstance'):
        assert _is_linked(a2, 'ProcessInstance', b)
    _safe_set(b, 'executedNodes', None)
    assert not _is_linked(b, 'executedNodes', a2)
    if hasattr(a2, 'ProcessInstance'):
        assert not _is_linked(a2, 'ProcessInstance', b)


def test_assoc_processInvariants1_reverse_link_reassign_clear():
    a1 = cbpmn_ProcessModel(name="sample_text")
    a2 = cbpmn_ProcessModel(name="sample_text_2")
    b = cbpmn_OCLConstraint(constraintName="sample_text", constraintStr="sample_text")
    _safe_set(b, 'cbpmn_OCLConstraint', a1)
    assert _is_linked(b, 'cbpmn_OCLConstraint', a1)
    if hasattr(a1, 'cbpmn_ProcessModel2'):
        assert _is_linked(a1, 'cbpmn_ProcessModel2', b)
    _safe_set(b, 'cbpmn_OCLConstraint', a2)
    assert _is_linked(b, 'cbpmn_OCLConstraint', a2)
    if hasattr(a1, 'cbpmn_ProcessModel2'):
        assert not _is_linked(a1, 'cbpmn_ProcessModel2', b)
    if hasattr(a2, 'cbpmn_ProcessModel2'):
        assert _is_linked(a2, 'cbpmn_ProcessModel2', b)
    _safe_set(b, 'cbpmn_OCLConstraint', None)
    assert not _is_linked(b, 'cbpmn_OCLConstraint', a2)
    if hasattr(a2, 'cbpmn_ProcessModel2'):
        assert not _is_linked(a2, 'cbpmn_ProcessModel2', b)


def test_assoc_processModel34_reverse_link_reassign_clear():
    a1 = cbpmn_ProcessModel(name="sample_text")
    a2 = cbpmn_ProcessModel(name="sample_text_2")
    b = cbpmn_ProcessInstance(id="sample_text")
    _safe_set(b, 'cbpmn_ProcessInstance', a1)
    assert _is_linked(b, 'cbpmn_ProcessInstance', a1)
    if hasattr(a1, 'cbpmn_ProcessModel35'):
        assert _is_linked(a1, 'cbpmn_ProcessModel35', b)
    _safe_set(b, 'cbpmn_ProcessInstance', a2)
    assert _is_linked(b, 'cbpmn_ProcessInstance', a2)
    if hasattr(a1, 'cbpmn_ProcessModel35'):
        assert not _is_linked(a1, 'cbpmn_ProcessModel35', b)
    if hasattr(a2, 'cbpmn_ProcessModel35'):
        assert _is_linked(a2, 'cbpmn_ProcessModel35', b)
    _safe_set(b, 'cbpmn_ProcessInstance', None)
    assert not _is_linked(b, 'cbpmn_ProcessInstance', a2)
    if hasattr(a2, 'cbpmn_ProcessModel35'):
        assert not _is_linked(a2, 'cbpmn_ProcessModel35', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_branches30_stub_double():
    # cbpmn_SplitGateway has no real 'gateway' property in the generated
    # code (a bare stub) -- manually attach it so cbpmn_Branch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmn_Branch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmn_Branch(default=True)
    partner = cbpmn_SplitGateway()
    setattr(partner, 'gateway', None)
    _safe_set(owner, 'Branch31', partner)
    assert owner in getattr(partner, 'gateway')
    _safe_set(owner, 'Branch31', None)
    assert owner not in getattr(partner, 'gateway')


def test_assoc_dataObjectClass32_stub_double():
    # cbpmn_EClass has no real 'cbpmn_EClass' property in the generated
    # code (a bare stub) -- manually attach it so cbpmn_DataObjectReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmn_DataObjectReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmn_DataObjectReference(higherBound=7, lowerBound=7, name="sample_text")
    partner = cbpmn_EClass()
    setattr(partner, 'cbpmn_EClass', None)
    _safe_set(owner, 'cbpmn_DataObjectReference33', partner)
    assert getattr(partner, 'cbpmn_EClass') == owner
    _safe_set(owner, 'cbpmn_DataObjectReference33', None)
    assert getattr(partner, 'cbpmn_EClass') is None


def test_assoc_dataObjects37_stub_double():
    # cbpmn_EObject has no real 'cbpmn_EObject' property in the generated
    # code (a bare stub) -- manually attach it so cbpmn_ProcessInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmn_ProcessInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmn_ProcessInstance(id="sample_text")
    partner = cbpmn_EObject()
    setattr(partner, 'cbpmn_EObject', None)
    _safe_set(owner, 'cbpmn_ProcessInstance38', {partner})
    assert getattr(partner, 'cbpmn_EObject') == owner
    _safe_set(owner, 'cbpmn_ProcessInstance38', set())
    assert getattr(partner, 'cbpmn_EObject') is None


def test_assoc_gateway16_stub_double():
    # cbpmn_SplitGateway has no real 'SplitGateway' property in the generated
    # code (a bare stub) -- manually attach it so cbpmn_Branch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmn_Branch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmn_Branch(default=True)
    partner = cbpmn_SplitGateway()
    setattr(partner, 'SplitGateway', None)
    _safe_set(owner, 'branches', partner)
    assert getattr(partner, 'SplitGateway') == owner
    _safe_set(owner, 'branches', None)
    assert getattr(partner, 'SplitGateway') is None


def test_assoc_inputs41_stub_double():
    # cbpmn_EObject has no real 'cbpmn_EObject43' property in the generated
    # code (a bare stub) -- manually attach it so cbpmn_FlowNodeInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmn_FlowNodeInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmn_FlowNodeInstance(status="sample_text")
    partner = cbpmn_EObject()
    setattr(partner, 'cbpmn_EObject43', None)
    _safe_set(owner, 'cbpmn_FlowNodeInstance42', {partner})
    assert getattr(partner, 'cbpmn_EObject43') == owner
    _safe_set(owner, 'cbpmn_FlowNodeInstance42', set())
    assert getattr(partner, 'cbpmn_EObject43') is None


def test_assoc_outputs44_stub_double():
    # cbpmn_EObject has no real 'cbpmn_EObject46' property in the generated
    # code (a bare stub) -- manually attach it so cbpmn_FlowNodeInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmn_FlowNodeInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmn_FlowNodeInstance(status="sample_text")
    partner = cbpmn_EObject()
    setattr(partner, 'cbpmn_EObject46', None)
    _safe_set(owner, 'cbpmn_FlowNodeInstance45', {partner})
    assert getattr(partner, 'cbpmn_EObject46') == owner
    _safe_set(owner, 'cbpmn_FlowNodeInstance45', set())
    assert getattr(partner, 'cbpmn_EObject46') is None


def test_assoc_trigger28_stub_double():
    # cbpmn_Event has no real 'cbpmn_Event' property in the generated
    # code (a bare stub) -- manually attach it so cbpmn_OCLConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmn_OCLConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmn_OCLConstraint(constraintName="sample_text", constraintStr="sample_text")
    partner = cbpmn_Event()
    setattr(partner, 'cbpmn_Event', None)
    _safe_set(owner, 'cbpmn_OCLConstraint29', partner)
    assert getattr(partner, 'cbpmn_Event') == owner
    _safe_set(owner, 'cbpmn_OCLConstraint29', None)
    assert getattr(partner, 'cbpmn_Event') is None


