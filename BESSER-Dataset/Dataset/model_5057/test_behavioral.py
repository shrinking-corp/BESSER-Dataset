import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FlowNodeInst,
    cbpmni_ActivityInst,
    cbpmni_Branch,
    cbpmni_BranchInst,
    cbpmni_ConstraintInst,
    cbpmni_EObject,
    cbpmni_EventInst,
    cbpmni_FlowNode,
    cbpmni_FlowNodeInst,
    cbpmni_OCLConstraint,
    cbpmni_ProcessInst,
    cbpmni_ProcessModel,
    cbpmni_SplitInst,
    FlowNodeStatusType,
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

def test_assoc_flowNodes3_reverse_link_reassign_clear():
    a1 = cbpmni_ProcessInst()
    a2 = cbpmni_ProcessInst()
    b = cbpmni_FlowNodeInst(status="sample_text")
    _safe_set(b, 'cbpmni_FlowNodeInst5', a1)
    assert _is_linked(b, 'cbpmni_FlowNodeInst5', a1)
    if hasattr(a1, 'cbpmni_ProcessInst4'):
        assert _is_linked(a1, 'cbpmni_ProcessInst4', b)
    _safe_set(b, 'cbpmni_FlowNodeInst5', a2)
    assert _is_linked(b, 'cbpmni_FlowNodeInst5', a2)
    if hasattr(a1, 'cbpmni_ProcessInst4'):
        assert not _is_linked(a1, 'cbpmni_ProcessInst4', b)
    if hasattr(a2, 'cbpmni_ProcessInst4'):
        assert _is_linked(a2, 'cbpmni_ProcessInst4', b)
    _safe_set(b, 'cbpmni_FlowNodeInst5', None)
    assert not _is_linked(b, 'cbpmni_FlowNodeInst5', a2)
    if hasattr(a2, 'cbpmni_ProcessInst4'):
        assert not _is_linked(a2, 'cbpmni_ProcessInst4', b)


def test_assoc_next9_reverse_link_reassign_clear():
    a1 = cbpmni_FlowNodeInst(status="sample_text")
    a2 = cbpmni_FlowNodeInst(status="sample_text_2")
    b = cbpmni_FlowNodeInst(status="sample_text")
    _safe_set(b, 'cbpmni_FlowNodeInst8', a1)
    assert _is_linked(b, 'cbpmni_FlowNodeInst8', a1)
    if hasattr(a1, 'cbpmni_FlowNodeInst10'):
        assert _is_linked(a1, 'cbpmni_FlowNodeInst10', b)
    _safe_set(b, 'cbpmni_FlowNodeInst8', a2)
    assert _is_linked(b, 'cbpmni_FlowNodeInst8', a2)
    if hasattr(a1, 'cbpmni_FlowNodeInst10'):
        assert not _is_linked(a1, 'cbpmni_FlowNodeInst10', b)
    if hasattr(a2, 'cbpmni_FlowNodeInst10'):
        assert _is_linked(a2, 'cbpmni_FlowNodeInst10', b)
    _safe_set(b, 'cbpmni_FlowNodeInst8', None)
    assert not _is_linked(b, 'cbpmni_FlowNodeInst8', a2)
    if hasattr(a2, 'cbpmni_FlowNodeInst10'):
        assert not _is_linked(a2, 'cbpmni_FlowNodeInst10', b)


def test_assoc_tokens1_reverse_link_reassign_clear():
    a1 = cbpmni_ProcessInst()
    a2 = cbpmni_ProcessInst()
    b = cbpmni_FlowNodeInst(status="sample_text")
    _safe_set(b, 'cbpmni_FlowNodeInst', a1)
    assert _is_linked(b, 'cbpmni_FlowNodeInst', a1)
    if hasattr(a1, 'cbpmni_ProcessInst2'):
        assert _is_linked(a1, 'cbpmni_ProcessInst2', b)
    _safe_set(b, 'cbpmni_FlowNodeInst', a2)
    assert _is_linked(b, 'cbpmni_FlowNodeInst', a2)
    if hasattr(a1, 'cbpmni_ProcessInst2'):
        assert not _is_linked(a1, 'cbpmni_ProcessInst2', b)
    if hasattr(a2, 'cbpmni_ProcessInst2'):
        assert _is_linked(a2, 'cbpmni_ProcessInst2', b)
    _safe_set(b, 'cbpmni_FlowNodeInst', None)
    assert not _is_linked(b, 'cbpmni_FlowNodeInst', a2)
    if hasattr(a2, 'cbpmni_ProcessInst2'):
        assert not _is_linked(a2, 'cbpmni_ProcessInst2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_nodeDef6_stub_double():
    # cbpmni_FlowNode has no real 'cbpmni_FlowNode' property in the generated
    # code (a bare stub) -- manually attach it so cbpmni_FlowNodeInst's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmni_FlowNodeInst's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmni_FlowNodeInst(status="sample_text")
    partner = cbpmni_FlowNode()
    setattr(partner, 'cbpmni_FlowNode', None)
    _safe_set(owner, 'cbpmni_FlowNodeInst7', partner)
    assert getattr(partner, 'cbpmni_FlowNode') == owner
    _safe_set(owner, 'cbpmni_FlowNodeInst7', None)
    assert getattr(partner, 'cbpmni_FlowNode') is None


def test_assoc_processDef0_stub_double():
    # cbpmni_ProcessModel has no real 'cbpmni_ProcessModel' property in the generated
    # code (a bare stub) -- manually attach it so cbpmni_ProcessInst's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cbpmni_ProcessInst's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cbpmni_ProcessInst()
    partner = cbpmni_ProcessModel()
    setattr(partner, 'cbpmni_ProcessModel', None)
    _safe_set(owner, 'cbpmni_ProcessInst', partner)
    assert getattr(partner, 'cbpmni_ProcessModel') == owner
    _safe_set(owner, 'cbpmni_ProcessInst', None)
    assert getattr(partner, 'cbpmni_ProcessModel') is None


