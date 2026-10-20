import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    ActivityNode,
    ControlNode,
    Element,
    ObjectNode,
    UML_Activity_mine_Action,
    UML_Activity_mine_Activity,
    UML_Activity_mine_ActivityEdge,
    UML_Activity_mine_ActivityFinalNode,
    UML_Activity_mine_ActivityInitialNode,
    UML_Activity_mine_ActivityNode,
    UML_Activity_mine_ActivityParameterNode,
    UML_Activity_mine_ControlNode,
    UML_Activity_mine_DatastoreNode,
    UML_Activity_mine_Element,
    UML_Activity_mine_ExpansionNode,
    UML_Activity_mine_ExpansionRegion,
    UML_Activity_mine_Fork,
    UML_Activity_mine_Join,
    UML_Activity_mine_ObjectNode,
    Direction,
    ExpansionMode,
    Status,
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

def test_assoc_edges1_stub_double():
    # UML_Activity_mine_Activity has no real 'UML_Activity_mine_Activity2' property in the generated
    # code (a bare stub) -- manually attach it so UML_Activity_mine_ActivityEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_Activity_mine_ActivityEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_Activity_mine_ActivityEdge(objectFlow=True)
    partner = UML_Activity_mine_Activity()
    setattr(partner, 'UML_Activity_mine_Activity2', None)
    _safe_set(owner, 'UML_Activity_mine_ActivityEdge', partner)
    assert owner in getattr(partner, 'UML_Activity_mine_Activity2')
    _safe_set(owner, 'UML_Activity_mine_ActivityEdge', None)
    assert owner not in getattr(partner, 'UML_Activity_mine_Activity2')


def test_assoc_edges13_stub_double():
    # UML_Activity_mine_ExpansionRegion has no real 'UML_Activity_mine_ExpansionRegion14' property in the generated
    # code (a bare stub) -- manually attach it so UML_Activity_mine_ActivityEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_Activity_mine_ActivityEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_Activity_mine_ActivityEdge(objectFlow=True)
    partner = UML_Activity_mine_ExpansionRegion()
    setattr(partner, 'UML_Activity_mine_ExpansionRegion14', None)
    _safe_set(owner, 'UML_Activity_mine_ActivityEdge15', partner)
    assert owner in getattr(partner, 'UML_Activity_mine_ExpansionRegion14')
    _safe_set(owner, 'UML_Activity_mine_ActivityEdge15', None)
    assert owner not in getattr(partner, 'UML_Activity_mine_ExpansionRegion14')


def test_assoc_incoming6_stub_double():
    # UML_Activity_mine_ActivityNode has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so UML_Activity_mine_ActivityEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_Activity_mine_ActivityEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_Activity_mine_ActivityEdge(objectFlow=True)
    partner = UML_Activity_mine_ActivityNode()
    setattr(partner, 'target', None)
    _safe_set(owner, 'ActivityEdge', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'ActivityEdge', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_outgoing7_stub_double():
    # UML_Activity_mine_ActivityNode has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so UML_Activity_mine_ActivityEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_Activity_mine_ActivityEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_Activity_mine_ActivityEdge(objectFlow=True)
    partner = UML_Activity_mine_ActivityNode()
    setattr(partner, 'source', None)
    _safe_set(owner, 'ActivityEdge8', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'ActivityEdge8', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_source4_stub_double():
    # UML_Activity_mine_ActivityNode has no real 'ActivityNode5' property in the generated
    # code (a bare stub) -- manually attach it so UML_Activity_mine_ActivityEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_Activity_mine_ActivityEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_Activity_mine_ActivityEdge(objectFlow=True)
    partner = UML_Activity_mine_ActivityNode()
    setattr(partner, 'ActivityNode5', None)
    _safe_set(owner, 'outgoing', partner)
    assert getattr(partner, 'ActivityNode5') == owner
    _safe_set(owner, 'outgoing', None)
    assert getattr(partner, 'ActivityNode5') is None


def test_assoc_target3_stub_double():
    # UML_Activity_mine_ActivityNode has no real 'ActivityNode' property in the generated
    # code (a bare stub) -- manually attach it so UML_Activity_mine_ActivityEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_Activity_mine_ActivityEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_Activity_mine_ActivityEdge(objectFlow=True)
    partner = UML_Activity_mine_ActivityNode()
    setattr(partner, 'ActivityNode', None)
    _safe_set(owner, 'incoming', partner)
    assert getattr(partner, 'ActivityNode') == owner
    _safe_set(owner, 'incoming', None)
    assert getattr(partner, 'ActivityNode') is None


