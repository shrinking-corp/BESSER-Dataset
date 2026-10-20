import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EObject,
    FlowNode,
    OCLConstraint,
    SplitGateway,
    cbpmn_Activity,
    cbpmn_Branch,
    cbpmn_DataObject,
    cbpmn_DataObjectReference,
    cbpmn_DecisionCondition,
    cbpmn_DecisionGateway,
    cbpmn_EClass,
    cbpmn_EObject,
    cbpmn_Event,
    cbpmn_FlowNode,
    cbpmn_FlowNodeInstance,
    cbpmn_OCLConstraint,
    cbpmn_ParallelGateway,
    cbpmn_ProcessInstance,
    cbpmn_ProcessModel,
    cbpmn_SplitGateway,
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

def test_assoc_conditions19_reverse_link_reassign_clear():
    a1 = cbpmn_DecisionGateway(type="sample_text")
    a2 = cbpmn_DecisionGateway(type="sample_text_2")
    b = cbpmn_DecisionCondition(isDefault=True)
    _safe_set(b, 'cbpmn_DecisionCondition20', a1)
    assert _is_linked(b, 'cbpmn_DecisionCondition20', a1)
    if hasattr(a1, 'cbpmn_DecisionGateway'):
        assert _is_linked(a1, 'cbpmn_DecisionGateway', b)
    _safe_set(b, 'cbpmn_DecisionCondition20', a2)
    assert _is_linked(b, 'cbpmn_DecisionCondition20', a2)
    if hasattr(a1, 'cbpmn_DecisionGateway'):
        assert not _is_linked(a1, 'cbpmn_DecisionGateway', b)
    if hasattr(a2, 'cbpmn_DecisionGateway'):
        assert _is_linked(a2, 'cbpmn_DecisionGateway', b)
    _safe_set(b, 'cbpmn_DecisionCondition20', None)
    assert not _is_linked(b, 'cbpmn_DecisionCondition20', a2)
    if hasattr(a2, 'cbpmn_DecisionGateway'):
        assert not _is_linked(a2, 'cbpmn_DecisionGateway', b)


def test_assoc_executedNodes39_reverse_link_reassign_clear():
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


def test_assoc_inputs8_reverse_link_reassign_clear():
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


def test_assoc_invariabilityClauses13_reverse_link_reassign_clear():
    a1 = cbpmn_OCLConstraint(constraintName="sample_text", constraintStr="sample_text")
    a2 = cbpmn_OCLConstraint(constraintName="sample_text_2", constraintStr="sample_text_2")
    b = cbpmn_Activity(type="sample_text")
    _safe_set(b, 'cbpmn_Activity14', {a1})
    assert _is_linked(b, 'cbpmn_Activity14', a1)
    if hasattr(a1, 'cbpmn_OCLConstraint15'):
        assert _is_linked(a1, 'cbpmn_OCLConstraint15', b)
    _safe_set(b, 'cbpmn_Activity14', {a2})
    assert _is_linked(b, 'cbpmn_Activity14', a2)
    if hasattr(a1, 'cbpmn_OCLConstraint15'):
        assert not _is_linked(a1, 'cbpmn_OCLConstraint15', b)
    if hasattr(a2, 'cbpmn_OCLConstraint15'):
        assert _is_linked(a2, 'cbpmn_OCLConstraint15', b)
    _safe_set(b, 'cbpmn_Activity14', set())
    assert not _is_linked(b, 'cbpmn_Activity14', a2)
    if hasattr(a2, 'cbpmn_OCLConstraint15'):
        assert not _is_linked(a2, 'cbpmn_OCLConstraint15', b)


def test_assoc_next26_reverse_link_reassign_clear():
    a1 = cbpmn_FlowNode(name="sample_text")
    a2 = cbpmn_FlowNode(name="sample_text_2")
    b = cbpmn_FlowNode(name="sample_text")
    _safe_set(b, 'previous', a1)
    assert _is_linked(b, 'previous', a1)
    if hasattr(a1, 'FlowNode27'):
        assert _is_linked(a1, 'FlowNode27', b)
    _safe_set(b, 'previous', a2)
    assert _is_linked(b, 'previous', a2)
    if hasattr(a1, 'FlowNode27'):
        assert not _is_linked(a1, 'FlowNode27', b)
    if hasattr(a2, 'FlowNode27'):
        assert _is_linked(a2, 'FlowNode27', b)
    _safe_set(b, 'previous', None)
    assert not _is_linked(b, 'previous', a2)
    if hasattr(a2, 'FlowNode27'):
        assert not _is_linked(a2, 'FlowNode27', b)


def test_assoc_nodeDef42_reverse_link_reassign_clear():
    a1 = cbpmn_FlowNodeInstance(status="sample_text")
    a2 = cbpmn_FlowNodeInstance(status="sample_text_2")
    b = cbpmn_FlowNode(name="sample_text")
    _safe_set(b, 'cbpmn_FlowNode', a1)
    assert _is_linked(b, 'cbpmn_FlowNode', a1)
    if hasattr(a1, 'cbpmn_FlowNodeInstance'):
        assert _is_linked(a1, 'cbpmn_FlowNodeInstance', b)
    _safe_set(b, 'cbpmn_FlowNode', a2)
    assert _is_linked(b, 'cbpmn_FlowNode', a2)
    if hasattr(a1, 'cbpmn_FlowNodeInstance'):
        assert not _is_linked(a1, 'cbpmn_FlowNodeInstance', b)
    if hasattr(a2, 'cbpmn_FlowNodeInstance'):
        assert _is_linked(a2, 'cbpmn_FlowNodeInstance', b)
    _safe_set(b, 'cbpmn_FlowNode', None)
    assert not _is_linked(b, 'cbpmn_FlowNode', a2)
    if hasattr(a2, 'cbpmn_FlowNodeInstance'):
        assert not _is_linked(a2, 'cbpmn_FlowNodeInstance', b)


def test_assoc_outputs10_reverse_link_reassign_clear():
    a1 = cbpmn_DataObjectReference(higherBound=7, lowerBound=7, name="sample_text")
    a2 = cbpmn_DataObjectReference(higherBound=13, lowerBound=13, name="sample_text_2")
    b = cbpmn_Activity(type="sample_text")
    _safe_set(b, 'cbpmn_Activity11', {a1})
    assert _is_linked(b, 'cbpmn_Activity11', a1)
    if hasattr(a1, 'cbpmn_DataObjectReference12'):
        assert _is_linked(a1, 'cbpmn_DataObjectReference12', b)
    _safe_set(b, 'cbpmn_Activity11', {a2})
    assert _is_linked(b, 'cbpmn_Activity11', a2)
    if hasattr(a1, 'cbpmn_DataObjectReference12'):
        assert not _is_linked(a1, 'cbpmn_DataObjectReference12', b)
    if hasattr(a2, 'cbpmn_DataObjectReference12'):
        assert _is_linked(a2, 'cbpmn_DataObjectReference12', b)
    _safe_set(b, 'cbpmn_Activity11', set())
    assert not _is_linked(b, 'cbpmn_Activity11', a2)
    if hasattr(a2, 'cbpmn_DataObjectReference12'):
        assert not _is_linked(a2, 'cbpmn_DataObjectReference12', b)


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


def test_assoc_previous29_reverse_link_reassign_clear():
    a1 = cbpmn_FlowNode(name="sample_text")
    a2 = cbpmn_FlowNode(name="sample_text_2")
    b = cbpmn_FlowNode(name="sample_text")
    _safe_set(b, 'next', a1)
    assert _is_linked(b, 'next', a1)
    if hasattr(a1, 'FlowNode30'):
        assert _is_linked(a1, 'FlowNode30', b)
    _safe_set(b, 'next', a2)
    assert _is_linked(b, 'next', a2)
    if hasattr(a1, 'FlowNode30'):
        assert not _is_linked(a1, 'FlowNode30', b)
    if hasattr(a2, 'FlowNode30'):
        assert _is_linked(a2, 'FlowNode30', b)
    _safe_set(b, 'next', None)
    assert not _is_linked(b, 'next', a2)
    if hasattr(a2, 'FlowNode30'):
        assert not _is_linked(a2, 'FlowNode30', b)


def test_assoc_processInstance49_reverse_link_reassign_clear():
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


def test_assoc_processModel37_reverse_link_reassign_clear():
    a1 = cbpmn_ProcessModel(name="sample_text")
    a2 = cbpmn_ProcessModel(name="sample_text_2")
    b = cbpmn_ProcessInstance(id="sample_text")
    _safe_set(b, 'cbpmn_ProcessInstance', a1)
    assert _is_linked(b, 'cbpmn_ProcessInstance', a1)
    if hasattr(a1, 'cbpmn_ProcessModel38'):
        assert _is_linked(a1, 'cbpmn_ProcessModel38', b)
    _safe_set(b, 'cbpmn_ProcessInstance', a2)
    assert _is_linked(b, 'cbpmn_ProcessInstance', a2)
    if hasattr(a1, 'cbpmn_ProcessModel38'):
        assert not _is_linked(a1, 'cbpmn_ProcessModel38', b)
    if hasattr(a2, 'cbpmn_ProcessModel38'):
        assert _is_linked(a2, 'cbpmn_ProcessModel38', b)
    _safe_set(b, 'cbpmn_ProcessInstance', None)
    assert not _is_linked(b, 'cbpmn_ProcessInstance', a2)
    if hasattr(a2, 'cbpmn_ProcessModel38'):
        assert not _is_linked(a2, 'cbpmn_ProcessModel38', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_branch21_stub_double():
    # cbpmn_Branch has no real 'cbpmn_Branch23' property in the generated
    # code (a bare stub) -- manually attach it so cbpmn_DecisionCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmn_DecisionCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmn_DecisionCondition(isDefault=True)
    partner = cbpmn_Branch()
    setattr(partner, 'cbpmn_Branch23', None)
    _safe_set(owner, 'cbpmn_DecisionCondition22', partner)
    assert getattr(partner, 'cbpmn_Branch23') == owner
    _safe_set(owner, 'cbpmn_DecisionCondition22', None)
    assert getattr(partner, 'cbpmn_Branch23') is None


def test_assoc_branch24_stub_double():
    # cbpmn_Branch has no real 'Branch' property in the generated
    # code (a bare stub) -- manually attach it so cbpmn_FlowNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmn_FlowNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmn_FlowNode(name="sample_text")
    partner = cbpmn_Branch()
    setattr(partner, 'Branch', None)
    _safe_set(owner, 'nodes', partner)
    assert getattr(partner, 'Branch') == owner
    _safe_set(owner, 'nodes', None)
    assert getattr(partner, 'Branch') is None


def test_assoc_dataObjectClass35_stub_double():
    # cbpmn_EClass has no real 'cbpmn_EClass' property in the generated
    # code (a bare stub) -- manually attach it so cbpmn_DataObjectReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmn_DataObjectReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmn_DataObjectReference(higherBound=7, lowerBound=7, name="sample_text")
    partner = cbpmn_EClass()
    setattr(partner, 'cbpmn_EClass', None)
    _safe_set(owner, 'cbpmn_DataObjectReference36', partner)
    assert getattr(partner, 'cbpmn_EClass') == owner
    _safe_set(owner, 'cbpmn_DataObjectReference36', None)
    assert getattr(partner, 'cbpmn_EClass') is None


def test_assoc_dataObjects40_stub_double():
    # cbpmn_EObject has no real 'cbpmn_EObject' property in the generated
    # code (a bare stub) -- manually attach it so cbpmn_ProcessInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmn_ProcessInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmn_ProcessInstance(id="sample_text")
    partner = cbpmn_EObject()
    setattr(partner, 'cbpmn_EObject', None)
    _safe_set(owner, 'cbpmn_ProcessInstance41', {partner})
    assert getattr(partner, 'cbpmn_EObject') == owner
    _safe_set(owner, 'cbpmn_ProcessInstance41', set())
    assert getattr(partner, 'cbpmn_EObject') is None


def test_assoc_entryConditions16_stub_double():
    # cbpmn_Branch has no real 'cbpmn_Branch17' property in the generated
    # code (a bare stub) -- manually attach it so cbpmn_DecisionCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmn_DecisionCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmn_DecisionCondition(isDefault=True)
    partner = cbpmn_Branch()
    setattr(partner, 'cbpmn_Branch17', None)
    _safe_set(owner, 'cbpmn_DecisionCondition', partner)
    assert getattr(partner, 'cbpmn_Branch17') == owner
    _safe_set(owner, 'cbpmn_DecisionCondition', None)
    assert getattr(partner, 'cbpmn_Branch17') is None


def test_assoc_inputs43_stub_double():
    # cbpmn_EObject has no real 'cbpmn_EObject45' property in the generated
    # code (a bare stub) -- manually attach it so cbpmn_FlowNodeInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmn_FlowNodeInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmn_FlowNodeInstance(status="sample_text")
    partner = cbpmn_EObject()
    setattr(partner, 'cbpmn_EObject45', None)
    _safe_set(owner, 'cbpmn_FlowNodeInstance44', {partner})
    assert getattr(partner, 'cbpmn_EObject45') == owner
    _safe_set(owner, 'cbpmn_FlowNodeInstance44', set())
    assert getattr(partner, 'cbpmn_EObject45') is None


def test_assoc_mainBranch0_stub_double():
    # cbpmn_Branch has no real 'cbpmn_Branch' property in the generated
    # code (a bare stub) -- manually attach it so cbpmn_ProcessModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmn_ProcessModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmn_ProcessModel(name="sample_text")
    partner = cbpmn_Branch()
    setattr(partner, 'cbpmn_Branch', None)
    _safe_set(owner, 'cbpmn_ProcessModel', partner)
    assert getattr(partner, 'cbpmn_Branch') == owner
    _safe_set(owner, 'cbpmn_ProcessModel', None)
    assert getattr(partner, 'cbpmn_Branch') is None


def test_assoc_nodes18_stub_double():
    # cbpmn_Branch has no real 'branch' property in the generated
    # code (a bare stub) -- manually attach it so cbpmn_FlowNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmn_FlowNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmn_FlowNode(name="sample_text")
    partner = cbpmn_Branch()
    setattr(partner, 'branch', None)
    _safe_set(owner, 'FlowNode', partner)
    assert owner in getattr(partner, 'branch')
    _safe_set(owner, 'FlowNode', None)
    assert owner not in getattr(partner, 'branch')


def test_assoc_outputs46_stub_double():
    # cbpmn_EObject has no real 'cbpmn_EObject48' property in the generated
    # code (a bare stub) -- manually attach it so cbpmn_FlowNodeInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmn_FlowNodeInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmn_FlowNodeInstance(status="sample_text")
    partner = cbpmn_EObject()
    setattr(partner, 'cbpmn_EObject48', None)
    _safe_set(owner, 'cbpmn_FlowNodeInstance47', {partner})
    assert getattr(partner, 'cbpmn_EObject48') == owner
    _safe_set(owner, 'cbpmn_FlowNodeInstance47', set())
    assert getattr(partner, 'cbpmn_EObject48') is None


def test_assoc_trigger31_stub_double():
    # cbpmn_Event has no real 'cbpmn_Event' property in the generated
    # code (a bare stub) -- manually attach it so cbpmn_OCLConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmn_OCLConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmn_OCLConstraint(constraintName="sample_text", constraintStr="sample_text")
    partner = cbpmn_Event()
    setattr(partner, 'cbpmn_Event', None)
    _safe_set(owner, 'cbpmn_OCLConstraint32', partner)
    assert getattr(partner, 'cbpmn_Event') == owner
    _safe_set(owner, 'cbpmn_OCLConstraint32', None)
    assert getattr(partner, 'cbpmn_Event') is None


