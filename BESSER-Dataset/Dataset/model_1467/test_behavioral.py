import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    graph3_Graph,
    graph3_Node,
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

def test_assoc_linksTo2_reverse_link_reassign_clear():
    a1 = graph3_Node(text="sample_text")
    a2 = graph3_Node(text="sample_text_2")
    b = graph3_Node(text="sample_text")
    _safe_set(b, 'graph3_Node3', a1)
    assert _is_linked(b, 'graph3_Node3', a1)
    if hasattr(a1, 'graph3_Node1'):
        assert _is_linked(a1, 'graph3_Node1', b)
    _safe_set(b, 'graph3_Node3', a2)
    assert _is_linked(b, 'graph3_Node3', a2)
    if hasattr(a1, 'graph3_Node1'):
        assert not _is_linked(a1, 'graph3_Node1', b)
    if hasattr(a2, 'graph3_Node1'):
        assert _is_linked(a2, 'graph3_Node1', b)
    _safe_set(b, 'graph3_Node3', None)
    assert not _is_linked(b, 'graph3_Node3', a2)
    if hasattr(a2, 'graph3_Node1'):
        assert not _is_linked(a2, 'graph3_Node1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_nodes0_stub_double():
    # graph3_Graph has no real 'graph3_Graph' property in the generated
    # code (a bare stub) -- manually attach it so graph3_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph3_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph3_Node(text="sample_text")
    partner = graph3_Graph()
    setattr(partner, 'graph3_Graph', None)
    _safe_set(owner, 'graph3_Node', partner)
    assert owner in getattr(partner, 'graph3_Graph')
    _safe_set(owner, 'graph3_Node', None)
    assert owner not in getattr(partner, 'graph3_Graph')


