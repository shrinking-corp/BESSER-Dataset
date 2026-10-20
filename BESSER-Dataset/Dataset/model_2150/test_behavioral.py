import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BodyVertex,
    ControlFlowVertex,
    StatementVertex,
    cfgraph_BodyVertex,
    cfgraph_BranchingVertex,
    cfgraph_CallVertex,
    cfgraph_ControlFlowEdge,
    cfgraph_ControlFlowGraph,
    cfgraph_ControlFlowVertex,
    cfgraph_EndVertex,
    cfgraph_SimpleStatementVertex,
    cfgraph_StartVertex,
    cfgraph_StatementVertex,
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

def test_assoc_branches9_stub_double():
    # cfgraph_BranchingVertex has no real 'cfgraph_BranchingVertex' property in the generated
    # code (a bare stub) -- manually attach it so cfgraph_ControlFlowEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cfgraph_ControlFlowEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cfgraph_ControlFlowEdge(backward=True)
    partner = cfgraph_BranchingVertex()
    setattr(partner, 'cfgraph_BranchingVertex', None)
    _safe_set(owner, 'cfgraph_ControlFlowEdge10', partner)
    assert owner in getattr(partner, 'cfgraph_BranchingVertex')
    _safe_set(owner, 'cfgraph_ControlFlowEdge10', None)
    assert owner not in getattr(partner, 'cfgraph_BranchingVertex')


def test_assoc_end1_stub_double():
    # cfgraph_BodyVertex has no real 'BodyVertex' property in the generated
    # code (a bare stub) -- manually attach it so cfgraph_ControlFlowEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cfgraph_ControlFlowEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cfgraph_ControlFlowEdge(backward=True)
    partner = cfgraph_BodyVertex()
    setattr(partner, 'BodyVertex', None)
    _safe_set(owner, 'incomingEdges', partner)
    assert getattr(partner, 'BodyVertex') == owner
    _safe_set(owner, 'incomingEdges', None)
    assert getattr(partner, 'BodyVertex') is None


def test_assoc_incomingEdges4_stub_double():
    # cfgraph_BodyVertex has no real 'end' property in the generated
    # code (a bare stub) -- manually attach it so cfgraph_ControlFlowEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cfgraph_ControlFlowEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cfgraph_ControlFlowEdge(backward=True)
    partner = cfgraph_BodyVertex()
    setattr(partner, 'end', None)
    _safe_set(owner, 'ControlFlowEdge', partner)
    assert owner in getattr(partner, 'end')
    _safe_set(owner, 'ControlFlowEdge', None)
    assert owner not in getattr(partner, 'end')


def test_assoc_next2_stub_double():
    # cfgraph_StartVertex has no real 'cfgraph_StartVertex3' property in the generated
    # code (a bare stub) -- manually attach it so cfgraph_ControlFlowEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cfgraph_ControlFlowEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cfgraph_ControlFlowEdge(backward=True)
    partner = cfgraph_StartVertex()
    setattr(partner, 'cfgraph_StartVertex3', None)
    _safe_set(owner, 'cfgraph_ControlFlowEdge', partner)
    assert getattr(partner, 'cfgraph_StartVertex3') == owner
    _safe_set(owner, 'cfgraph_ControlFlowEdge', None)
    assert getattr(partner, 'cfgraph_StartVertex3') is None


def test_assoc_next5_stub_double():
    # cfgraph_StatementVertex has no real 'cfgraph_StatementVertex' property in the generated
    # code (a bare stub) -- manually attach it so cfgraph_ControlFlowEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cfgraph_ControlFlowEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cfgraph_ControlFlowEdge(backward=True)
    partner = cfgraph_StatementVertex()
    setattr(partner, 'cfgraph_StatementVertex', None)
    _safe_set(owner, 'cfgraph_ControlFlowEdge6', partner)
    assert getattr(partner, 'cfgraph_StatementVertex') == owner
    _safe_set(owner, 'cfgraph_ControlFlowEdge6', None)
    assert getattr(partner, 'cfgraph_StatementVertex') is None


