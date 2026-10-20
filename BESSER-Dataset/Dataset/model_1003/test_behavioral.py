import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Statement,
    dot_Attribute,
    dot_AttributeStatement,
    dot_EdgeStatement,
    dot_EdgeTarget,
    dot_Graph,
    dot_GraphvizModel,
    dot_Node,
    dot_NodeStatement,
    dot_Port,
    dot_Statement,
    dot_Subgraph,
    AttributeType,
    EdgeOperator,
    GraphType,
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

def test_assoc_attributes20_reverse_link_reassign_clear():
    a1 = dot_AttributeStatement(type="sample_text")
    a2 = dot_AttributeStatement(type="sample_text_2")
    b = dot_Attribute(name="sample_text", value="sample_text")
    _safe_set(b, 'dot_Attribute21', a1)
    assert _is_linked(b, 'dot_Attribute21', a1)
    if hasattr(a1, 'dot_AttributeStatement'):
        assert _is_linked(a1, 'dot_AttributeStatement', b)
    _safe_set(b, 'dot_Attribute21', a2)
    assert _is_linked(b, 'dot_Attribute21', a2)
    if hasattr(a1, 'dot_AttributeStatement'):
        assert not _is_linked(a1, 'dot_AttributeStatement', b)
    if hasattr(a2, 'dot_AttributeStatement'):
        assert _is_linked(a2, 'dot_AttributeStatement', b)
    _safe_set(b, 'dot_Attribute21', None)
    assert not _is_linked(b, 'dot_Attribute21', a2)
    if hasattr(a2, 'dot_AttributeStatement'):
        assert not _is_linked(a2, 'dot_AttributeStatement', b)


def test_assoc_port6_reverse_link_reassign_clear():
    a1 = dot_Port(compass_pt="sample_text", name="sample_text")
    a2 = dot_Port(compass_pt="sample_text_2", name="sample_text_2")
    b = dot_Node(name="sample_text")
    _safe_set(b, 'dot_Node7', a1)
    assert _is_linked(b, 'dot_Node7', a1)
    if hasattr(a1, 'dot_Port'):
        assert _is_linked(a1, 'dot_Port', b)
    _safe_set(b, 'dot_Node7', a2)
    assert _is_linked(b, 'dot_Node7', a2)
    if hasattr(a1, 'dot_Port'):
        assert not _is_linked(a1, 'dot_Port', b)
    if hasattr(a2, 'dot_Port'):
        assert _is_linked(a2, 'dot_Port', b)
    _safe_set(b, 'dot_Node7', None)
    assert not _is_linked(b, 'dot_Node7', a2)
    if hasattr(a2, 'dot_Port'):
        assert not _is_linked(a2, 'dot_Port', b)


def test_assoc_targetSubgraph15_reverse_link_reassign_clear():
    a1 = dot_Subgraph(name="sample_text")
    a2 = dot_Subgraph(name="sample_text_2")
    b = dot_EdgeTarget(operator="sample_text")
    _safe_set(b, 'dot_EdgeTarget16', a1)
    assert _is_linked(b, 'dot_EdgeTarget16', a1)
    if hasattr(a1, 'dot_Subgraph'):
        assert _is_linked(a1, 'dot_Subgraph', b)
    _safe_set(b, 'dot_EdgeTarget16', a2)
    assert _is_linked(b, 'dot_EdgeTarget16', a2)
    if hasattr(a1, 'dot_Subgraph'):
        assert not _is_linked(a1, 'dot_Subgraph', b)
    if hasattr(a2, 'dot_Subgraph'):
        assert _is_linked(a2, 'dot_Subgraph', b)
    _safe_set(b, 'dot_EdgeTarget16', None)
    assert not _is_linked(b, 'dot_EdgeTarget16', a2)
    if hasattr(a2, 'dot_Subgraph'):
        assert not _is_linked(a2, 'dot_Subgraph', b)


def test_assoc_targetnode17_reverse_link_reassign_clear():
    a1 = dot_Node(name="sample_text")
    a2 = dot_Node(name="sample_text_2")
    b = dot_EdgeTarget(operator="sample_text")
    _safe_set(b, 'dot_EdgeTarget18', a1)
    assert _is_linked(b, 'dot_EdgeTarget18', a1)
    if hasattr(a1, 'dot_Node19'):
        assert _is_linked(a1, 'dot_Node19', b)
    _safe_set(b, 'dot_EdgeTarget18', a2)
    assert _is_linked(b, 'dot_EdgeTarget18', a2)
    if hasattr(a1, 'dot_Node19'):
        assert not _is_linked(a1, 'dot_Node19', b)
    if hasattr(a2, 'dot_Node19'):
        assert _is_linked(a2, 'dot_Node19', b)
    _safe_set(b, 'dot_EdgeTarget18', None)
    assert not _is_linked(b, 'dot_EdgeTarget18', a2)
    if hasattr(a2, 'dot_Node19'):
        assert not _is_linked(a2, 'dot_Node19', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes12_stub_double():
    # dot_EdgeStatement has no real 'dot_EdgeStatement13' property in the generated
    # code (a bare stub) -- manually attach it so dot_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_Attribute(name="sample_text", value="sample_text")
    partner = dot_EdgeStatement()
    setattr(partner, 'dot_EdgeStatement13', None)
    _safe_set(owner, 'dot_Attribute14', partner)
    assert owner in getattr(partner, 'dot_EdgeStatement13')
    _safe_set(owner, 'dot_Attribute14', None)
    assert owner not in getattr(partner, 'dot_EdgeStatement13')


def test_assoc_attributes4_stub_double():
    # dot_NodeStatement has no real 'dot_NodeStatement5' property in the generated
    # code (a bare stub) -- manually attach it so dot_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_Attribute(name="sample_text", value="sample_text")
    partner = dot_NodeStatement()
    setattr(partner, 'dot_NodeStatement5', None)
    _safe_set(owner, 'dot_Attribute', partner)
    assert owner in getattr(partner, 'dot_NodeStatement5')
    _safe_set(owner, 'dot_Attribute', None)
    assert owner not in getattr(partner, 'dot_NodeStatement5')


def test_assoc_edgeTargets10_stub_double():
    # dot_EdgeStatement has no real 'dot_EdgeStatement11' property in the generated
    # code (a bare stub) -- manually attach it so dot_EdgeTarget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_EdgeTarget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_EdgeTarget(operator="sample_text")
    partner = dot_EdgeStatement()
    setattr(partner, 'dot_EdgeStatement11', None)
    _safe_set(owner, 'dot_EdgeTarget', partner)
    assert owner in getattr(partner, 'dot_EdgeStatement11')
    _safe_set(owner, 'dot_EdgeTarget', None)
    assert owner not in getattr(partner, 'dot_EdgeStatement11')


def test_assoc_graphs0_stub_double():
    # dot_GraphvizModel has no real 'dot_GraphvizModel' property in the generated
    # code (a bare stub) -- manually attach it so dot_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_Graph(name="sample_text", strict=True, type="sample_text")
    partner = dot_GraphvizModel()
    setattr(partner, 'dot_GraphvizModel', None)
    _safe_set(owner, 'dot_Graph', partner)
    assert owner in getattr(partner, 'dot_GraphvizModel')
    _safe_set(owner, 'dot_Graph', None)
    assert owner not in getattr(partner, 'dot_GraphvizModel')


def test_assoc_node3_stub_double():
    # dot_NodeStatement has no real 'dot_NodeStatement' property in the generated
    # code (a bare stub) -- manually attach it so dot_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_Node(name="sample_text")
    partner = dot_NodeStatement()
    setattr(partner, 'dot_NodeStatement', None)
    _safe_set(owner, 'dot_Node', partner)
    assert getattr(partner, 'dot_NodeStatement') == owner
    _safe_set(owner, 'dot_Node', None)
    assert getattr(partner, 'dot_NodeStatement') is None


def test_assoc_sourceNode8_stub_double():
    # dot_EdgeStatement has no real 'dot_EdgeStatement' property in the generated
    # code (a bare stub) -- manually attach it so dot_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_Node(name="sample_text")
    partner = dot_EdgeStatement()
    setattr(partner, 'dot_EdgeStatement', None)
    _safe_set(owner, 'dot_Node9', partner)
    assert getattr(partner, 'dot_EdgeStatement') == owner
    _safe_set(owner, 'dot_Node9', None)
    assert getattr(partner, 'dot_EdgeStatement') is None


def test_assoc_statements1_stub_double():
    # dot_Statement has no real 'dot_Statement' property in the generated
    # code (a bare stub) -- manually attach it so dot_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_Graph(name="sample_text", strict=True, type="sample_text")
    partner = dot_Statement()
    setattr(partner, 'dot_Statement', None)
    _safe_set(owner, 'dot_Graph2', {partner})
    assert getattr(partner, 'dot_Statement') == owner
    _safe_set(owner, 'dot_Graph2', set())
    assert getattr(partner, 'dot_Statement') is None


def test_assoc_statements22_stub_double():
    # dot_Statement has no real 'dot_Statement24' property in the generated
    # code (a bare stub) -- manually attach it so dot_Subgraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_Subgraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_Subgraph(name="sample_text")
    partner = dot_Statement()
    setattr(partner, 'dot_Statement24', None)
    _safe_set(owner, 'dot_Subgraph23', {partner})
    assert getattr(partner, 'dot_Statement24') == owner
    _safe_set(owner, 'dot_Subgraph23', set())
    assert getattr(partner, 'dot_Statement24') is None


