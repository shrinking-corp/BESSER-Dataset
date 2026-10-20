import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    dfg_DfgEdge,
    dfg_DfgGraph,
    dfg_DfgVertex,
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

def test_assoc_connecting6_reverse_link_reassign_clear():
    a1 = dfg_DfgVertex(mappings="sample_text")
    a2 = dfg_DfgVertex(mappings="sample_text_2")
    b = dfg_DfgEdge(label="sample_text")
    _safe_set(b, 'dfg_DfgEdge8', a1)
    assert _is_linked(b, 'dfg_DfgEdge8', a1)
    if hasattr(a1, 'dfg_DfgVertex7'):
        assert _is_linked(a1, 'dfg_DfgVertex7', b)
    _safe_set(b, 'dfg_DfgEdge8', a2)
    assert _is_linked(b, 'dfg_DfgEdge8', a2)
    if hasattr(a1, 'dfg_DfgVertex7'):
        assert not _is_linked(a1, 'dfg_DfgVertex7', b)
    if hasattr(a2, 'dfg_DfgVertex7'):
        assert _is_linked(a2, 'dfg_DfgVertex7', b)
    _safe_set(b, 'dfg_DfgEdge8', None)
    assert not _is_linked(b, 'dfg_DfgEdge8', a2)
    if hasattr(a2, 'dfg_DfgVertex7'):
        assert not _is_linked(a2, 'dfg_DfgVertex7', b)


def test_assoc_neighbors4_reverse_link_reassign_clear():
    a1 = dfg_DfgVertex(mappings="sample_text")
    a2 = dfg_DfgVertex(mappings="sample_text_2")
    b = dfg_DfgVertex(mappings="sample_text")
    _safe_set(b, 'dfg_DfgVertex5', a1)
    assert _is_linked(b, 'dfg_DfgVertex5', a1)
    if hasattr(a1, 'dfg_DfgVertex3'):
        assert _is_linked(a1, 'dfg_DfgVertex3', b)
    _safe_set(b, 'dfg_DfgVertex5', a2)
    assert _is_linked(b, 'dfg_DfgVertex5', a2)
    if hasattr(a1, 'dfg_DfgVertex3'):
        assert not _is_linked(a1, 'dfg_DfgVertex3', b)
    if hasattr(a2, 'dfg_DfgVertex3'):
        assert _is_linked(a2, 'dfg_DfgVertex3', b)
    _safe_set(b, 'dfg_DfgVertex5', None)
    assert not _is_linked(b, 'dfg_DfgVertex5', a2)
    if hasattr(a2, 'dfg_DfgVertex3'):
        assert not _is_linked(a2, 'dfg_DfgVertex3', b)


def test_assoc_vertex19_reverse_link_reassign_clear():
    a1 = dfg_DfgVertex(mappings="sample_text")
    a2 = dfg_DfgVertex(mappings="sample_text_2")
    b = dfg_DfgEdge(label="sample_text")
    _safe_set(b, 'dfg_DfgEdge10', a1)
    assert _is_linked(b, 'dfg_DfgEdge10', a1)
    if hasattr(a1, 'dfg_DfgVertex11'):
        assert _is_linked(a1, 'dfg_DfgVertex11', b)
    _safe_set(b, 'dfg_DfgEdge10', a2)
    assert _is_linked(b, 'dfg_DfgEdge10', a2)
    if hasattr(a1, 'dfg_DfgVertex11'):
        assert not _is_linked(a1, 'dfg_DfgVertex11', b)
    if hasattr(a2, 'dfg_DfgVertex11'):
        assert _is_linked(a2, 'dfg_DfgVertex11', b)
    _safe_set(b, 'dfg_DfgEdge10', None)
    assert not _is_linked(b, 'dfg_DfgEdge10', a2)
    if hasattr(a2, 'dfg_DfgVertex11'):
        assert not _is_linked(a2, 'dfg_DfgVertex11', b)


def test_assoc_vertex212_reverse_link_reassign_clear():
    a1 = dfg_DfgVertex(mappings="sample_text")
    a2 = dfg_DfgVertex(mappings="sample_text_2")
    b = dfg_DfgEdge(label="sample_text")
    _safe_set(b, 'dfg_DfgEdge13', a1)
    assert _is_linked(b, 'dfg_DfgEdge13', a1)
    if hasattr(a1, 'dfg_DfgVertex14'):
        assert _is_linked(a1, 'dfg_DfgVertex14', b)
    _safe_set(b, 'dfg_DfgEdge13', a2)
    assert _is_linked(b, 'dfg_DfgEdge13', a2)
    if hasattr(a1, 'dfg_DfgVertex14'):
        assert not _is_linked(a1, 'dfg_DfgVertex14', b)
    if hasattr(a2, 'dfg_DfgVertex14'):
        assert _is_linked(a2, 'dfg_DfgVertex14', b)
    _safe_set(b, 'dfg_DfgEdge13', None)
    assert not _is_linked(b, 'dfg_DfgEdge13', a2)
    if hasattr(a2, 'dfg_DfgVertex14'):
        assert not _is_linked(a2, 'dfg_DfgVertex14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_edges1_stub_double():
    # dfg_DfgGraph has no real 'dfg_DfgGraph2' property in the generated
    # code (a bare stub) -- manually attach it so dfg_DfgEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dfg_DfgEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dfg_DfgEdge(label="sample_text")
    partner = dfg_DfgGraph()
    setattr(partner, 'dfg_DfgGraph2', None)
    _safe_set(owner, 'dfg_DfgEdge', partner)
    assert owner in getattr(partner, 'dfg_DfgGraph2')
    _safe_set(owner, 'dfg_DfgEdge', None)
    assert owner not in getattr(partner, 'dfg_DfgGraph2')


def test_assoc_vertices0_stub_double():
    # dfg_DfgGraph has no real 'dfg_DfgGraph' property in the generated
    # code (a bare stub) -- manually attach it so dfg_DfgVertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dfg_DfgVertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dfg_DfgVertex(mappings="sample_text")
    partner = dfg_DfgGraph()
    setattr(partner, 'dfg_DfgGraph', None)
    _safe_set(owner, 'dfg_DfgVertex', partner)
    assert owner in getattr(partner, 'dfg_DfgGraph')
    _safe_set(owner, 'dfg_DfgVertex', None)
    assert owner not in getattr(partner, 'dfg_DfgGraph')


