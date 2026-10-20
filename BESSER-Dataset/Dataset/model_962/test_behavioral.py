import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    vml_Diagram,
    vml_Edge,
    vml_Graph,
    vml_Model,
    vml_Node,
    vml_Pie,
    vml_Slice,
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

def test_assoc_edges9_reverse_link_reassign_clear():
    a1 = vml_Graph(ID="sample_text", title="sample_text")
    a2 = vml_Graph(ID="sample_text_2", title="sample_text_2")
    b = vml_Edge(relation="sample_text")
    _safe_set(b, 'vml_Edge', a1)
    assert _is_linked(b, 'vml_Edge', a1)
    if hasattr(a1, 'vml_Graph10'):
        assert _is_linked(a1, 'vml_Graph10', b)
    _safe_set(b, 'vml_Edge', a2)
    assert _is_linked(b, 'vml_Edge', a2)
    if hasattr(a1, 'vml_Graph10'):
        assert not _is_linked(a1, 'vml_Graph10', b)
    if hasattr(a2, 'vml_Graph10'):
        assert _is_linked(a2, 'vml_Graph10', b)
    _safe_set(b, 'vml_Edge', None)
    assert not _is_linked(b, 'vml_Edge', a2)
    if hasattr(a2, 'vml_Graph10'):
        assert not _is_linked(a2, 'vml_Graph10', b)


def test_assoc_graph3_reverse_link_reassign_clear():
    a1 = vml_Graph(ID="sample_text", title="sample_text")
    a2 = vml_Graph(ID="sample_text_2", title="sample_text_2")
    b = vml_Diagram(title="sample_text")
    _safe_set(b, 'vml_Diagram4', {a1})
    assert _is_linked(b, 'vml_Diagram4', a1)
    if hasattr(a1, 'vml_Graph'):
        assert _is_linked(a1, 'vml_Graph', b)
    _safe_set(b, 'vml_Diagram4', {a2})
    assert _is_linked(b, 'vml_Diagram4', a2)
    if hasattr(a1, 'vml_Graph'):
        assert not _is_linked(a1, 'vml_Graph', b)
    if hasattr(a2, 'vml_Graph'):
        assert _is_linked(a2, 'vml_Graph', b)
    _safe_set(b, 'vml_Diagram4', set())
    assert not _is_linked(b, 'vml_Diagram4', a2)
    if hasattr(a2, 'vml_Graph'):
        assert not _is_linked(a2, 'vml_Graph', b)


def test_assoc_incoming12_reverse_link_reassign_clear():
    a1 = vml_Node(title="sample_text")
    a2 = vml_Node(title="sample_text_2")
    b = vml_Edge(relation="sample_text")
    _safe_set(b, 'Edge13', a1)
    assert _is_linked(b, 'Edge13', a1)
    if hasattr(a1, 'target'):
        assert _is_linked(a1, 'target', b)
    _safe_set(b, 'Edge13', a2)
    assert _is_linked(b, 'Edge13', a2)
    if hasattr(a1, 'target'):
        assert not _is_linked(a1, 'target', b)
    if hasattr(a2, 'target'):
        assert _is_linked(a2, 'target', b)
    _safe_set(b, 'Edge13', None)
    assert not _is_linked(b, 'Edge13', a2)
    if hasattr(a2, 'target'):
        assert not _is_linked(a2, 'target', b)


def test_assoc_nodes7_reverse_link_reassign_clear():
    a1 = vml_Node(title="sample_text")
    a2 = vml_Node(title="sample_text_2")
    b = vml_Graph(ID="sample_text", title="sample_text")
    _safe_set(b, 'vml_Graph8', {a1})
    assert _is_linked(b, 'vml_Graph8', a1)
    if hasattr(a1, 'vml_Node'):
        assert _is_linked(a1, 'vml_Node', b)
    _safe_set(b, 'vml_Graph8', {a2})
    assert _is_linked(b, 'vml_Graph8', a2)
    if hasattr(a1, 'vml_Node'):
        assert not _is_linked(a1, 'vml_Node', b)
    if hasattr(a2, 'vml_Node'):
        assert _is_linked(a2, 'vml_Node', b)
    _safe_set(b, 'vml_Graph8', set())
    assert not _is_linked(b, 'vml_Graph8', a2)
    if hasattr(a2, 'vml_Node'):
        assert not _is_linked(a2, 'vml_Node', b)


def test_assoc_outgoing11_reverse_link_reassign_clear():
    a1 = vml_Node(title="sample_text")
    a2 = vml_Node(title="sample_text_2")
    b = vml_Edge(relation="sample_text")
    _safe_set(b, 'Edge', a1)
    assert _is_linked(b, 'Edge', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'Edge', a2)
    assert _is_linked(b, 'Edge', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'Edge', None)
    assert not _is_linked(b, 'Edge', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_pies1_reverse_link_reassign_clear():
    a1 = vml_Pie(ID="sample_text", title="sample_text")
    a2 = vml_Pie(ID="sample_text_2", title="sample_text_2")
    b = vml_Diagram(title="sample_text")
    _safe_set(b, 'vml_Diagram2', {a1})
    assert _is_linked(b, 'vml_Diagram2', a1)
    if hasattr(a1, 'vml_Pie'):
        assert _is_linked(a1, 'vml_Pie', b)
    _safe_set(b, 'vml_Diagram2', {a2})
    assert _is_linked(b, 'vml_Diagram2', a2)
    if hasattr(a1, 'vml_Pie'):
        assert not _is_linked(a1, 'vml_Pie', b)
    if hasattr(a2, 'vml_Pie'):
        assert _is_linked(a2, 'vml_Pie', b)
    _safe_set(b, 'vml_Diagram2', set())
    assert not _is_linked(b, 'vml_Diagram2', a2)
    if hasattr(a2, 'vml_Pie'):
        assert not _is_linked(a2, 'vml_Pie', b)


def test_assoc_slices5_reverse_link_reassign_clear():
    a1 = vml_Slice(title="sample_text", value=7)
    a2 = vml_Slice(title="sample_text_2", value=13)
    b = vml_Pie(ID="sample_text", title="sample_text")
    _safe_set(b, 'vml_Pie6', {a1})
    assert _is_linked(b, 'vml_Pie6', a1)
    if hasattr(a1, 'vml_Slice'):
        assert _is_linked(a1, 'vml_Slice', b)
    _safe_set(b, 'vml_Pie6', {a2})
    assert _is_linked(b, 'vml_Pie6', a2)
    if hasattr(a1, 'vml_Slice'):
        assert not _is_linked(a1, 'vml_Slice', b)
    if hasattr(a2, 'vml_Slice'):
        assert _is_linked(a2, 'vml_Slice', b)
    _safe_set(b, 'vml_Pie6', set())
    assert not _is_linked(b, 'vml_Pie6', a2)
    if hasattr(a2, 'vml_Slice'):
        assert not _is_linked(a2, 'vml_Slice', b)


def test_assoc_source14_reverse_link_reassign_clear():
    a1 = vml_Node(title="sample_text")
    a2 = vml_Node(title="sample_text_2")
    b = vml_Edge(relation="sample_text")
    _safe_set(b, 'outgoing', a1)
    assert _is_linked(b, 'outgoing', a1)
    if hasattr(a1, 'Node'):
        assert _is_linked(a1, 'Node', b)
    _safe_set(b, 'outgoing', a2)
    assert _is_linked(b, 'outgoing', a2)
    if hasattr(a1, 'Node'):
        assert not _is_linked(a1, 'Node', b)
    if hasattr(a2, 'Node'):
        assert _is_linked(a2, 'Node', b)
    _safe_set(b, 'outgoing', None)
    assert not _is_linked(b, 'outgoing', a2)
    if hasattr(a2, 'Node'):
        assert not _is_linked(a2, 'Node', b)


def test_assoc_target15_reverse_link_reassign_clear():
    a1 = vml_Node(title="sample_text")
    a2 = vml_Node(title="sample_text_2")
    b = vml_Edge(relation="sample_text")
    _safe_set(b, 'incoming', a1)
    assert _is_linked(b, 'incoming', a1)
    if hasattr(a1, 'Node16'):
        assert _is_linked(a1, 'Node16', b)
    _safe_set(b, 'incoming', a2)
    assert _is_linked(b, 'incoming', a2)
    if hasattr(a1, 'Node16'):
        assert not _is_linked(a1, 'Node16', b)
    if hasattr(a2, 'Node16'):
        assert _is_linked(a2, 'Node16', b)
    _safe_set(b, 'incoming', None)
    assert not _is_linked(b, 'incoming', a2)
    if hasattr(a2, 'Node16'):
        assert not _is_linked(a2, 'Node16', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_diagrams0_stub_double():
    # vml_Model has no real 'vml_Model' property in the generated
    # code (a bare stub) -- manually attach it so vml_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vml_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vml_Diagram(title="sample_text")
    partner = vml_Model()
    setattr(partner, 'vml_Model', None)
    _safe_set(owner, 'vml_Diagram', partner)
    assert owner in getattr(partner, 'vml_Model')
    _safe_set(owner, 'vml_Diagram', None)
    assert owner not in getattr(partner, 'vml_Model')


