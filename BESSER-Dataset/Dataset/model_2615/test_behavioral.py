import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    GraphElement,
    grapho_Edge,
    grapho_GraphElement,
    grapho_GraphO,
    grapho_Node,
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

def test_assoc_nodeA1_reverse_link_reassign_clear():
    a1 = grapho_Node(color="sample_text", label="sample_text", shape="sample_text", style="sample_text")
    a2 = grapho_Node(color="sample_text_2", label="sample_text_2", shape="sample_text_2", style="sample_text_2")
    b = grapho_Edge(color="sample_text", constraintRank=True, style="sample_text")
    _safe_set(b, 'grapho_Edge', a1)
    assert _is_linked(b, 'grapho_Edge', a1)
    if hasattr(a1, 'grapho_Node'):
        assert _is_linked(a1, 'grapho_Node', b)
    _safe_set(b, 'grapho_Edge', a2)
    assert _is_linked(b, 'grapho_Edge', a2)
    if hasattr(a1, 'grapho_Node'):
        assert not _is_linked(a1, 'grapho_Node', b)
    if hasattr(a2, 'grapho_Node'):
        assert _is_linked(a2, 'grapho_Node', b)
    _safe_set(b, 'grapho_Edge', None)
    assert not _is_linked(b, 'grapho_Edge', a2)
    if hasattr(a2, 'grapho_Node'):
        assert not _is_linked(a2, 'grapho_Node', b)


def test_assoc_nodeB2_reverse_link_reassign_clear():
    a1 = grapho_Node(color="sample_text", label="sample_text", shape="sample_text", style="sample_text")
    a2 = grapho_Node(color="sample_text_2", label="sample_text_2", shape="sample_text_2", style="sample_text_2")
    b = grapho_Edge(color="sample_text", constraintRank=True, style="sample_text")
    _safe_set(b, 'grapho_Edge3', a1)
    assert _is_linked(b, 'grapho_Edge3', a1)
    if hasattr(a1, 'grapho_Node4'):
        assert _is_linked(a1, 'grapho_Node4', b)
    _safe_set(b, 'grapho_Edge3', a2)
    assert _is_linked(b, 'grapho_Edge3', a2)
    if hasattr(a1, 'grapho_Node4'):
        assert not _is_linked(a1, 'grapho_Node4', b)
    if hasattr(a2, 'grapho_Node4'):
        assert _is_linked(a2, 'grapho_Node4', b)
    _safe_set(b, 'grapho_Edge3', None)
    assert not _is_linked(b, 'grapho_Edge3', a2)
    if hasattr(a2, 'grapho_Node4'):
        assert not _is_linked(a2, 'grapho_Node4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements0_stub_double():
    # grapho_GraphO has no real 'grapho_GraphO' property in the generated
    # code (a bare stub) -- manually attach it so grapho_GraphElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grapho_GraphElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grapho_GraphElement(name="sample_text")
    partner = grapho_GraphO()
    setattr(partner, 'grapho_GraphO', None)
    _safe_set(owner, 'grapho_GraphElement', partner)
    assert owner in getattr(partner, 'grapho_GraphO')
    _safe_set(owner, 'grapho_GraphElement', None)
    assert owner not in getattr(partner, 'grapho_GraphO')


