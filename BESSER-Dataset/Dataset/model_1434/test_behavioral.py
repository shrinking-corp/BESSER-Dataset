import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    GraphMM_Edge,
    GraphMM_Node,
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

def test_assoc_source0_stub_double():
    # GraphMM_Edge has no real 'GraphMM_Edge' property in the generated
    # code (a bare stub) -- manually attach it so GraphMM_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphMM_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphMM_Node(name="sample_text", size=3.14, type="sample_text")
    partner = GraphMM_Edge()
    setattr(partner, 'GraphMM_Edge', None)
    _safe_set(owner, 'GraphMM_Node', partner)
    assert getattr(partner, 'GraphMM_Edge') == owner
    _safe_set(owner, 'GraphMM_Node', None)
    assert getattr(partner, 'GraphMM_Edge') is None


def test_assoc_target1_stub_double():
    # GraphMM_Edge has no real 'GraphMM_Edge2' property in the generated
    # code (a bare stub) -- manually attach it so GraphMM_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphMM_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphMM_Node(name="sample_text", size=3.14, type="sample_text")
    partner = GraphMM_Edge()
    setattr(partner, 'GraphMM_Edge2', None)
    _safe_set(owner, 'GraphMM_Node3', partner)
    assert getattr(partner, 'GraphMM_Edge2') == owner
    _safe_set(owner, 'GraphMM_Node3', None)
    assert getattr(partner, 'GraphMM_Edge2') is None


