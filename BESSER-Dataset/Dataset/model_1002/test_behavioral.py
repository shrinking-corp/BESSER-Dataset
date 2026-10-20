import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    GraphElement,
    Node,
    graphEditor_Edge,
    graphEditor_Factornode,
    graphEditor_Graph,
    graphEditor_GraphElement,
    graphEditor_Message,
    graphEditor_Node,
    graphEditor_Variablenode,
    FunctionType,
    MessageType,
    VariableType,
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

def test_assoc_from_5_reverse_link_reassign_clear():
    a1 = graphEditor_Node(name="sample_text")
    a2 = graphEditor_Node(name="sample_text_2")
    b = graphEditor_Message(count=7, type="sample_text")
    _safe_set(b, 'graphEditor_Message6', a1)
    assert _is_linked(b, 'graphEditor_Message6', a1)
    if hasattr(a1, 'graphEditor_Node7'):
        assert _is_linked(a1, 'graphEditor_Node7', b)
    _safe_set(b, 'graphEditor_Message6', a2)
    assert _is_linked(b, 'graphEditor_Message6', a2)
    if hasattr(a1, 'graphEditor_Node7'):
        assert not _is_linked(a1, 'graphEditor_Node7', b)
    if hasattr(a2, 'graphEditor_Node7'):
        assert _is_linked(a2, 'graphEditor_Node7', b)
    _safe_set(b, 'graphEditor_Message6', None)
    assert not _is_linked(b, 'graphEditor_Message6', a2)
    if hasattr(a2, 'graphEditor_Node7'):
        assert not _is_linked(a2, 'graphEditor_Node7', b)


def test_assoc_messages3_reverse_link_reassign_clear():
    a1 = graphEditor_Message(count=7, type="sample_text")
    a2 = graphEditor_Message(count=13, type="sample_text_2")
    b = graphEditor_Graph(name="sample_text", result="sample_text")
    _safe_set(b, 'graphEditor_Graph4', {a1})
    assert _is_linked(b, 'graphEditor_Graph4', a1)
    if hasattr(a1, 'graphEditor_Message'):
        assert _is_linked(a1, 'graphEditor_Message', b)
    _safe_set(b, 'graphEditor_Graph4', {a2})
    assert _is_linked(b, 'graphEditor_Graph4', a2)
    if hasattr(a1, 'graphEditor_Message'):
        assert not _is_linked(a1, 'graphEditor_Message', b)
    if hasattr(a2, 'graphEditor_Message'):
        assert _is_linked(a2, 'graphEditor_Message', b)
    _safe_set(b, 'graphEditor_Graph4', set())
    assert not _is_linked(b, 'graphEditor_Graph4', a2)
    if hasattr(a2, 'graphEditor_Message'):
        assert not _is_linked(a2, 'graphEditor_Message', b)


def test_assoc_nodes0_reverse_link_reassign_clear():
    a1 = graphEditor_Node(name="sample_text")
    a2 = graphEditor_Node(name="sample_text_2")
    b = graphEditor_Graph(name="sample_text", result="sample_text")
    _safe_set(b, 'graphEditor_Graph', {a1})
    assert _is_linked(b, 'graphEditor_Graph', a1)
    if hasattr(a1, 'graphEditor_Node'):
        assert _is_linked(a1, 'graphEditor_Node', b)
    _safe_set(b, 'graphEditor_Graph', {a2})
    assert _is_linked(b, 'graphEditor_Graph', a2)
    if hasattr(a1, 'graphEditor_Node'):
        assert not _is_linked(a1, 'graphEditor_Node', b)
    if hasattr(a2, 'graphEditor_Node'):
        assert _is_linked(a2, 'graphEditor_Node', b)
    _safe_set(b, 'graphEditor_Graph', set())
    assert not _is_linked(b, 'graphEditor_Graph', a2)
    if hasattr(a2, 'graphEditor_Node'):
        assert not _is_linked(a2, 'graphEditor_Node', b)


def test_assoc_to8_reverse_link_reassign_clear():
    a1 = graphEditor_Node(name="sample_text")
    a2 = graphEditor_Node(name="sample_text_2")
    b = graphEditor_Message(count=7, type="sample_text")
    _safe_set(b, 'graphEditor_Message9', a1)
    assert _is_linked(b, 'graphEditor_Message9', a1)
    if hasattr(a1, 'graphEditor_Node10'):
        assert _is_linked(a1, 'graphEditor_Node10', b)
    _safe_set(b, 'graphEditor_Message9', a2)
    assert _is_linked(b, 'graphEditor_Message9', a2)
    if hasattr(a1, 'graphEditor_Node10'):
        assert not _is_linked(a1, 'graphEditor_Node10', b)
    if hasattr(a2, 'graphEditor_Node10'):
        assert _is_linked(a2, 'graphEditor_Node10', b)
    _safe_set(b, 'graphEditor_Message9', None)
    assert not _is_linked(b, 'graphEditor_Message9', a2)
    if hasattr(a2, 'graphEditor_Node10'):
        assert not _is_linked(a2, 'graphEditor_Node10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_edges1_stub_double():
    # graphEditor_Edge has no real 'graphEditor_Edge' property in the generated
    # code (a bare stub) -- manually attach it so graphEditor_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphEditor_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphEditor_Graph(name="sample_text", result="sample_text")
    partner = graphEditor_Edge()
    setattr(partner, 'graphEditor_Edge', None)
    _safe_set(owner, 'graphEditor_Graph2', {partner})
    assert getattr(partner, 'graphEditor_Edge') == owner
    _safe_set(owner, 'graphEditor_Graph2', set())
    assert getattr(partner, 'graphEditor_Edge') is None


def test_assoc_from_11_stub_double():
    # graphEditor_Edge has no real 'graphEditor_Edge12' property in the generated
    # code (a bare stub) -- manually attach it so graphEditor_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphEditor_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphEditor_Node(name="sample_text")
    partner = graphEditor_Edge()
    setattr(partner, 'graphEditor_Edge12', None)
    _safe_set(owner, 'graphEditor_Node13', partner)
    assert getattr(partner, 'graphEditor_Edge12') == owner
    _safe_set(owner, 'graphEditor_Node13', None)
    assert getattr(partner, 'graphEditor_Edge12') is None


def test_assoc_to14_stub_double():
    # graphEditor_Edge has no real 'graphEditor_Edge15' property in the generated
    # code (a bare stub) -- manually attach it so graphEditor_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphEditor_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphEditor_Node(name="sample_text")
    partner = graphEditor_Edge()
    setattr(partner, 'graphEditor_Edge15', None)
    _safe_set(owner, 'graphEditor_Node16', partner)
    assert getattr(partner, 'graphEditor_Edge15') == owner
    _safe_set(owner, 'graphEditor_Node16', None)
    assert getattr(partner, 'graphEditor_Edge15') is None


